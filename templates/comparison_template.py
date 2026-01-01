class ComparisonTemplate:
    """
    Template for Comparison page structure.
    """
    
    def __init__(self):
        self.structure = {
            "page_type": str,
            "title": str,
            "product_a": dict,
            "product_b": dict,
            "detailed_comparison": dict,
            "comparison_analysis": str,
            "recommendations": dict,
            "insights": list,
            "comparison_table_html": str,
            "winner": str,
            "generated_at": str
        }
    
    def fill(self, data):
        """Fill template with data"""
        return {
            "page_type": data.get("page_type", "Product Comparison"),
            "title": data.get("title", ""),
            "product_a": data.get("product_a", {}),
            "product_b": data.get("product_b", {}),
            "detailed_comparison": data.get("detailed_comparison", {}),
            "comparison_analysis": data.get("comparison_analysis", ""),
            "recommendations": data.get("recommendations", {}),
            "insights": data.get("insights", []),
            "comparison_table_html": data.get("comparison_table_html", ""),
            "winner": data.get("winner", ""),
            "generated_at": data.get("generated_at", "")
        }