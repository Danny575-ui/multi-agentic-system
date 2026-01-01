from agents.base_agent import BaseAgent
from logic_blocks.llm_client import OllamaClient
from logic_blocks.answer_generator import AnswerGenerator
from templates.faq_template import FAQTemplate
from datetime import datetime
from typing import Any, Dict, List

class FAQAgent(BaseAgent):
    """
    Autonomous agent that generates FAQ pages.
    Uses LOGIC BLOCKS for most work, LLM only when needed.
    
    Capabilities:
    - Select best 5 questions from available questions
    - Generate contextual answers (uses logic + minimal LLM)
    - Format FAQ page
    
    Decision-making:
    - Chooses which questions to answer
    - Determines answer depth
    - Decides if LLM needed or rule-based answer sufficient
    """
    
    def __init__(self):
        super().__init__("FAQAgent")
        self.capabilities = ["generate_faq", "answer_questions"]
        self.llm = OllamaClient()
        self.answer_gen = AnswerGenerator(self.llm)
        self.template = FAQTemplate()
    
    def can_handle(self, task_type: str) -> bool:
        """Check if this agent can handle the task"""
        return task_type in self.capabilities
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate FAQ page with autonomous question selection and answering.
        Agent makes decisions about which questions to prioritize.
        """
        questions = data.get("questions", [])
        product_data = data.get("product_data", {})
        
        self.log("Creating FAQ page...")
        
        # Autonomous decision: Select top 5 questions
        selected_questions = self._select_top_questions(questions, 5)
        self.log(f"Selected {len(selected_questions)} questions for FAQ")
        
        # Generate answers - try rule-based first, LLM as fallback
        faq_items = []
        for q_data in selected_questions:
            self.log(f"Generating answer for: {q_data['category']}")
            
            # Try rule-based answer first (NO LLM)
            answer = self._try_rule_based_answer(q_data, product_data)
            
            # If rule-based fails, use LLM (FALLBACK ONLY)
            if not answer:
                self.log("Using LLM for complex question...")
                answer = self.answer_gen.generate_answer(
                    q_data["question"],
                    product_data
                )
            
            faq_items.append({
                "question": q_data["question"],
                "answer": answer,
                "category": q_data["category"]
            })
        
        # Build final FAQ structure using template
        faq_data = {
            "page_type": "FAQ",
            "title": "Frequently Asked Questions",
            "product_name": product_data.get("name", ""),
            "questions": faq_items,
            "total_questions": len(faq_items),
            "generated_at": datetime.now().isoformat()
        }
        
        result = self.template.fill(faq_data)
        self.log("FAQ page complete!")
        
        return result
    
    def _try_rule_based_answer(self, question_data: Dict, product_data: Dict) -> str:
        """
        Try to answer using PURE LOGIC (no LLM).
        Returns empty string if can't answer with rules.
        """
        question = question_data["question"].lower()
        
        # Rule-based answers for common questions (ALL SAFE ACCESS)
        if "price" in question:
            return f"The price of {product_data.get('name', 'this product')} is {product_data.get('price', 'available on request')}."
        
        elif "side effects" in question or "side effect" in question:
            return f"The known side effects are: {product_data.get('side_effects', 'Please consult product label')}."
        
        elif "how to use" in question or "how do i apply" in question:
            return f"Usage instructions: {product_data.get('how_to_use', 'Follow product instructions')}."
        
        elif "skin type" in question:
            return f"{product_data.get('name', 'This product')} is suitable for {product_data.get('skin_type', 'various')} skin."
        
        elif "ingredients" in question:
            return f"The key ingredients in {product_data.get('name', 'this product')} are: {product_data.get('key_ingredients', 'listed on packaging')}."
        
        elif "benefits" in question or "what does it do" in question:
            return f"{product_data.get('name', 'This product')} provides the following benefits: {product_data.get('benefits', 'multiple skin benefits')}."
        
        elif "concentration" in question:
            return f"{product_data.get('name', 'This product')} contains {product_data.get('concentration', 'active ingredients')}."
        
        # If no rule matches, return empty (will use LLM)
        return ""
    
    def _select_top_questions(self, questions: List[Dict], count: int) -> List[Dict]:
        """
        Autonomous decision-making: Select most important questions.
        Prioritizes different categories for comprehensive coverage.
        """
        # Ensure diverse category coverage
        categories_seen = set()
        selected = []
        
        # First pass: One from each category
        for q in questions:
            category = q.get("category", "")
            if category not in categories_seen and len(selected) < count:
                selected.append(q)
                categories_seen.add(category)
        
        # Second pass: Fill remaining slots
        remaining = count - len(selected)
        if remaining > 0:
            for q in questions:
                if q not in selected and len(selected) < count:
                    selected.append(q)
        
        return selected[:count]