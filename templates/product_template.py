class ProductTemplate:
    """
    Template for Product Description page structure.
    """
    
    def __init__(self):
        self.structure = {
            "page_type": str,
            "title": str,
            "product_id": str,
            "tagline": str,
            "description": str,
            "benefits": list,
            "benefits_html": str,
            "specifications": dict,
            "usage_guide": list,
            "target_audience": list,
            "safety_info": dict,
            "generated_at": str
        }
    
    def fill(self, data):
        """Fill template with data and ensure all fields are present"""
        return {
            "page_type": data.get("page_type", "Product Description"),
            "title": data.get("title", ""),
            "product_id": data.get("product_id", ""),
            "tagline": data.get("tagline", ""),
            "description": data.get("description", ""),
            "benefits": data.get("benefits", []),
            "benefits_html": data.get("benefits_html", ""),
            "specifications": data.get("specifications", {}),
            "usage_guide": data.get("usage_guide", []),
            "target_audience": data.get("target_audience", []),
            "safety_info": data.get("safety_info", {
                "side_effects": "",
                "warnings": [],
                "patch_test_recommended": False
            }),
            "generated_at": data.get("generated_at", "")
        }