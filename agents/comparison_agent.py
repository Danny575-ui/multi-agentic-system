from agents.base_agent import BaseAgent
from logic_blocks.comparison_logic import compare_products, generate_comparison_table, generate_comparison_analysis
from templates.comparison_template import ComparisonTemplate
from datetime import datetime
from typing import Any, Dict

class ComparisonAgent(BaseAgent):
    """
    Autonomous agent that generates product comparison pages.
    Uses PURE LOGIC for comparison (NO LLM).
    
    Capabilities:
    - Compare product attributes
    - Analyze differences using algorithms
    - Generate recommendations using logic
    - Create comparison tables
    
    Decision-making:
    - Determines comparison criteria
    - Weighs different factors using rules
    - Makes product recommendations algorithmically
    - Decides which insights to highlight
    """
    
    def __init__(self):
        super().__init__("ComparisonAgent")
        self.capabilities = ["generate_comparison", "analyze_products"]
        self.template = ComparisonTemplate()
    
    def can_handle(self, task_type: str) -> bool:
        """Check if this agent can handle the task"""
        return task_type in self.capabilities
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate product comparison page using PURE LOGIC (NO LLM).
        Agent makes analytical decisions using algorithms.
        """
        product_a = data.get("product_a", {})
        product_b = data.get("product_b", {})
        
        self.log(f"Comparing: {product_a.get('name')} vs {product_b.get('name')}")
        
        # Algorithmic analysis (NO LLM - PURE LOGIC)
        comparison_details = compare_products(product_a, product_b)
        
        # Generate text analysis using LOGIC BLOCK (NO LLM)
        self.log("Generating comparison analysis using rule-based logic...")
        analysis = generate_comparison_analysis(product_a, product_b, comparison_details)
        
        # Algorithmic recommendations (NO LLM)
        self.log("Creating recommendations using decision logic...")
        recommendations = self._generate_recommendations(product_a, product_b, comparison_details)
        
        # Create comparison page structure
        comparison_data = {
            "page_type": "Product Comparison",
            "title": f"{product_a['name']} vs {product_b['name']}",
            "product_a": {
                "name": product_a['name'],
                "concentration": product_a['concentration'],
                "skin_type": product_a['skin_type'],
                "ingredients": product_a['key_ingredients'],
                "benefits": product_a['benefits'],
                "price": product_a['price']
            },
            "product_b": {
                "name": product_b['name'],
                "concentration": product_b['concentration'],
                "skin_type": product_b['skin_type'],
                "ingredients": product_b['key_ingredients'],
                "benefits": product_b['benefits'],
                "price": product_b['price']
            },
            "detailed_comparison": comparison_details,
            "comparison_analysis": analysis,
            "recommendations": recommendations,
            "insights": self._extract_insights(comparison_details),
            "comparison_table_html": generate_comparison_table(product_a, product_b),
            "winner": self._determine_winner(comparison_details),
            "generated_at": datetime.now().isoformat()
        }
        
        result = self.template.fill(comparison_data)
        self.log("Comparison complete!")
        
        return result
    
    def _generate_recommendations(self, product_a: Dict, product_b: Dict,
                                  comparison: Dict) -> Dict:
        """
        Autonomous decision-making using ALGORITHMS (NO LLM).
        Pure logic-based recommendations.
        """
        return {
            "for_oily_skin": self._recommend_for_skin_type(product_a, product_b, "oily"),
            "for_sensitive_skin": self._recommend_for_skin_type(product_a, product_b, "sensitive"),
            "for_budget_conscious": self._recommend_by_price(product_a, product_b),
            "for_maximum_results": self._recommend_by_effectiveness(product_a, product_b)
        }
    
    def _recommend_for_skin_type(self, product_a: Dict, product_b: Dict, 
                                 skin_type: str) -> str:
        """Algorithm: Recommend based on skin type compatibility"""
        a_compatible = skin_type.lower() in product_a['skin_type'].lower()
        b_compatible = skin_type.lower() in product_b['skin_type'].lower()
        
        if a_compatible and not b_compatible:
            return product_a['name']
        elif b_compatible and not a_compatible:
            return product_b['name']
        else:
            return "Both products suitable"
    
    def _recommend_by_price(self, product_a: Dict, product_b: Dict) -> str:
        """Algorithm: Recommend based on price value"""
        price_a = int(''.join(c for c in product_a['price'] if c in '0123456789'))
        price_b = int(''.join(c for c in product_b['price'] if c in '0123456789'))
        
        return product_a['name'] if price_a < price_b else product_b['name']
    
    def _recommend_by_effectiveness(self, product_a: Dict, product_b: Dict) -> str:
        """Algorithm: Recommend based on concentration heuristic"""
        try:
            conc_a = int(''.join(c for c in product_a['concentration'][:3] if c in '0123456789'))
            conc_b = int(''.join(c for c in product_b['concentration'][:3] if c in '0123456789'))
            return product_a['name'] if conc_a >= conc_b else product_b['name']
        except:
            return "Both equally effective"
    
    def _extract_insights(self, comparison: Dict) -> list:
        """Extract key insights using data analysis (NO LLM)"""
        return [
            f"Concentration difference: {comparison.get('concentration_diff', 'N/A')}",
            f"Price difference: ₹{comparison.get('price_diff', 'N/A')}",
            f"Skin type compatibility: {comparison.get('skin_type_match', 'Similar')}",
            f"Ingredient overlap: {comparison.get('ingredient_similarity', 'Medium')}"
        ]
    
    def _determine_winner(self, comparison: Dict) -> str:
        """
        Algorithm: Determine winner using scoring system (NO LLM).
        """
        score_a = 0
        score_b = 0
        
        # Price factor
        if comparison.get('better_price') == 'product_a':
            score_a += 1
        else:
            score_b += 1
        
        # Versatility factor
        if comparison.get('more_versatile') == 'product_a':
            score_a += 1
        else:
            score_b += 1
        
        if score_a > score_b:
            return comparison.get('product_a_name', 'Product A')
        elif score_b > score_a:
            return comparison.get('product_b_name', 'Product B')
        else:
            return "Tie - Both excellent choices"