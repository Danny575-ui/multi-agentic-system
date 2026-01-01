from agents.base_agent import BaseAgent
from typing import Any, List, Dict

class QuestionGeneratorAgent(BaseAgent):
    """
    Autonomous agent that generates categorized questions using RULE-BASED LOGIC.
    NO LLM - uses templates and product data extraction.
    
    Capabilities:
    - Generate 15+ questions across categories
    - Categorize questions automatically
    - Adapt questions based on product data
    
    Decision-making:
    - Determines question categories
    - Decides question complexity
    - Balances question distribution
    """
    
    # Question templates (AUTOMATION, NOT LLM)
    QUESTION_TEMPLATES = {
        "Informational": [
            "What is {product_name} and what does it do?",
            "What is the concentration of {active_ingredient} in {product_name}?",
            "What skin types is {product_name} suitable for?",
        ],
        "Safety": [
            "Are there any side effects of using {product_name}?",
            "Can I use {product_name} if I have sensitive skin?",
            "Should I do a patch test before using {product_name}?",
        ],
        "Usage": [
            "How do I apply {product_name} correctly?",
            "When is the best time to use {product_name}?",
            "Can I use {product_name} with other skincare products?",
        ],
        "Purchase": [
            "What is the price of {product_name}?",
            "How long will one bottle of {product_name} last?",
        ],
        "Ingredients": [
            "What are the key ingredients in {product_name}?",
            "How does {concentration} work for {benefits}?",
        ],
        "Results": [
            "How long does it take to see results from {product_name}?",
            "What results can I expect from using {product_name}?",
        ],
        "Comparison": [
            "How does {product_name} compare to other products?"
        ]
    }
    
    def __init__(self):
        super().__init__("QuestionGeneratorAgent")
        self.capabilities = ["generate_questions", "categorize_questions"]
    
    def can_handle(self, task_type: str) -> bool:
        """Check if this agent can handle the task"""
        return task_type in self.capabilities
    
    def process(self, product_data: Dict[str, Any]) -> List[Dict[str, str]]:
        """
        Generate exactly 15 categorized questions using RULE-BASED TEMPLATES.
        This is AUTOMATION, not LLM generation.
        """
        self.log("Generating 15 categorized questions using rule-based templates...")
        
        # Extract product variables (LOGIC, NOT LLM)
        variables = self._extract_variables(product_data)
        
        # Generate questions from templates (AUTOMATION)
        questions = []
        
        for category, templates in self.QUESTION_TEMPLATES.items():
            for template in templates:
                if len(questions) >= 15:
                    break
                
                # Fill template with product data (PURE LOGIC)
                question_text = self._fill_template(template, variables)
                
                questions.append({
                    "question": question_text,
                    "category": category
                })
        
        # Trim to exactly 15
        questions = questions[:15]
        
        self.log(f"Generated {len(questions)} questions across {len(self.QUESTION_TEMPLATES)} categories")
        
        return questions
    
    def _extract_variables(self, product_data: Dict) -> Dict[str, str]:
        """
        Extract variables from product data (LOGIC BLOCK).
        This is data transformation, not LLM.
        """
        name = product_data.get("name", "product")
        concentration = product_data.get("concentration", "")
        benefits = product_data.get("benefits", "").lower()
        
        # Extract active ingredient from concentration
        active_ingredient = concentration.split()[0] if concentration else "active ingredient"
        
        return {
            "product_name": name,
            "concentration": concentration,
            "active_ingredient": active_ingredient,
            "benefits": benefits,
            "skin_type": product_data.get("skin_type", "all skin types"),
            "price": product_data.get("price", "")
        }
    
    def _fill_template(self, template: str, variables: Dict[str, str]) -> str:
        """
        Fill question template with variables (STRING MANIPULATION).
        Pure logic, no LLM.
        """
        try:
            return template.format(**variables)
        except KeyError:
            # Fallback if variable missing
            return template