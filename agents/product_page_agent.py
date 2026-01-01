from agents.base_agent import BaseAgent
from logic_blocks.llm_client import OllamaClient
from logic_blocks.benefits_extractor import extract_benefits, format_benefits_html, get_benefit_summary
from templates.product_template import ProductTemplate
from datetime import datetime
from typing import Any, Dict

class ProductPageAgent(BaseAgent):
    """
    Autonomous agent that generates product description pages.
    
    Capabilities:
    - Extract structured benefits
    - Generate compelling descriptions
    - Create usage guides
    - Format product specifications
    
    Decision-making:
    - Determines content depth
    - Chooses appropriate tone
    - Decides which features to highlight
    """
    
    def __init__(self):
        super().__init__("ProductPageAgent")
        self.capabilities = ["generate_product_page", "extract_benefits"]
        self.llm = OllamaClient()
        self.template = ProductTemplate()
    
    def can_handle(self, task_type: str) -> bool:
        """Check if this agent can handle the task"""
        return task_type in self.capabilities
    
    def process(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate product description page autonomously.
        Agent makes decisions about content structure and emphasis.
        """
        self.log(f"Creating product page for: {product_data.get('name', 'Unknown')}")
        
        # Autonomous extraction of benefits
        self.log("Extracting product benefits...")
        benefits = extract_benefits(product_data)
        benefit_summary = get_benefit_summary(benefits)
        
        # Autonomous decision: Generate description based on product data
        self.log("Generating product description...")
        description = self._generate_description(product_data, benefit_summary)
        
        # Build comprehensive product page
        product_page_data = {
            "page_type": "Product Description",
            "title": product_data['name'],
            "product_id": product_data['product_id'],
            "tagline": f"Experience the Power of {product_data['concentration']}",
            "description": description.strip(),
            "benefits": benefits,
            "benefits_html": format_benefits_html(benefits),
            "specifications": {
                "concentration": product_data['concentration'],
                "skin_type": product_data['skin_type'],
                "key_ingredients": product_data['key_ingredients'],
                "benefits_summary": product_data['benefits'],
                "usage": product_data['how_to_use'],
                "side_effects": product_data['side_effects'],
                "price": product_data['price']
            },
            "usage_guide": self._generate_usage_guide(product_data),
            "target_audience": self._determine_target_audience(product_data),
            "safety_info": {
                "side_effects": product_data['side_effects'],
                "warnings": [
                    "Perform a patch test before first use",
                    "Avoid contact with eyes",
                    "Use sunscreen during the day"
                ],
                "patch_test_recommended": True
            },
            "generated_at": datetime.now().isoformat()
        }
        
        result = self.template.fill(product_page_data)
        self.log("Product page complete!")
        
        return result
    
    def _generate_description(self, product_data: Dict, benefit_summary: str) -> str:
        """
        Autonomous content generation using LLM.
        Agent decides appropriate tone and emphasis.
        """
        prompt = f"""Write a compelling 3-paragraph product description for this skincare product:

Product: {product_data['name']}
Concentration: {product_data['concentration']}
Skin Type: {product_data['skin_type']}
Ingredients: {product_data['key_ingredients']}
Benefits: {product_data['benefits']}
Usage: {product_data['how_to_use']}
Price: {product_data['price']}

PARAGRAPH 1: Introduction - What is this product and why it's special
PARAGRAPH 2: Key benefits and how the ingredients work together
PARAGRAPH 3: Expected results and why customers love it

Requirements:
- Professional, marketing-focused tone
- Each paragraph should be 3-4 sentences
- Make it compelling but factual
- Do NOT use bullet points

Write the 3 paragraphs now:"""

        description = self.llm.generate(prompt, max_tokens=400)
        return description.strip()
    
    def _generate_usage_guide(self, product_data: Dict) -> list:
        """
        Autonomous decision: Create comprehensive usage guide
        """
        return [
            "Cleanse your face thoroughly before application",
            product_data['how_to_use'],
            "Follow with moisturizer and sunscreen",
            "Use consistently for best results"
        ]
    
    def _determine_target_audience(self, product_data: Dict) -> list:
        """
        Autonomous decision: Identify target audience based on product data
        """
        return [
            f"People with {product_data['skin_type'].lower()} skin",
            f"Those seeking {product_data['benefits'].lower()}",
            "Anyone wanting to improve skin radiance"
        ]