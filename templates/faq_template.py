class FAQTemplate:
    """
    Template for FAQ page structure.
    Defines fields and formatting rules.
    """
    
    def __init__(self):
        self.structure = {
            "page_type": str,
            "title": str,
            "product_name": str,
            "questions": list,
            "total_questions": int,
            "generated_at": str
        }
    
    def fill(self, data):
        """Fill template with data"""
        return {
            "page_type": data.get("page_type", "FAQ"),
            "title": data.get("title", ""),
            "product_name": data.get("product_name", ""),
            "questions": data.get("questions", []),
            "total_questions": data.get("total_questions", 0),
            "generated_at": data.get("generated_at", "")
        }