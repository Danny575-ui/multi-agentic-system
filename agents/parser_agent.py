from agents.base_agent import BaseAgent

class ParserAgent(BaseAgent):
    """
    Agent responsible for parsing and normalizing product data.
    Input: Raw product dict
    Output: Structured product model
    """
    
    def __init__(self):
        super().__init__("ParserAgent")
    
    def process(self, raw_data):
        """Parse raw product data into clean structure"""
        self.log("Starting to parse product data...")
        
        # Normalize and structure the data
        parsed = {
            "product_id": "GLOW_001",
            "name": raw_data.get("name", ""),
            "concentration": raw_data.get("concentration", ""),
            "skin_type": raw_data.get("skin_type", ""),
            "key_ingredients": raw_data.get("key_ingredients", ""),
            "benefits": raw_data.get("benefits", ""),
            "how_to_use": raw_data.get("how_to_use", ""),
            "side_effects": raw_data.get("side_effects", ""),
            "price": raw_data.get("price", "")
        }
        
        self.log(f"Successfully parsed: {parsed['name']}")
        return parsed