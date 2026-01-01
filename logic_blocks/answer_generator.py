"""
Reusable logic block for generating answers to questions.
Pure logic component - can be used by any agent.
"""

class AnswerGenerator:
    """
    Logic block that generates contextual answers based on product data.
    This is NOT an agent - it's a reusable content generation component.
    """
    
    def __init__(self, llm_client):
        self.llm = llm_client
    
    def generate_answer(self, question: str, product_data: dict, 
                       max_length: int = 200) -> str:
        """
        Generate a contextual answer based on product data.
        
        Args:
            question: The question to answer
            product_data: Product information context
            max_length: Maximum answer length in tokens
        
        Returns:
            Generated answer string
        """
        # Build context from product data
        context = self._build_context(product_data)
        
        # Create prompt for answer generation
        prompt = f"""Answer this customer question about the product using ONLY the provided information:

Product Information:
{context}

Customer Question: {question}

Provide a clear, helpful answer in 2-3 sentences. Be informative but concise. Use only the facts provided above.

Answer:"""
        
        # Generate answer using LLM
        answer = self.llm.generate(prompt, max_tokens=max_length)
        return answer.strip()
    
    def _build_context(self, product_data: dict) -> str:
        """Build context string from product data"""
        context_parts = []
        
        if 'name' in product_data:
            context_parts.append(f"Product Name: {product_data['name']}")
        
        if 'concentration' in product_data:
            context_parts.append(f"Concentration: {product_data['concentration']}")
        
        if 'skin_type' in product_data:
            context_parts.append(f"Suitable for: {product_data['skin_type']}")
        
        if 'key_ingredients' in product_data:
            context_parts.append(f"Key Ingredients: {product_data['key_ingredients']}")
        
        if 'benefits' in product_data:
            context_parts.append(f"Benefits: {product_data['benefits']}")
        
        if 'how_to_use' in product_data:
            context_parts.append(f"How to Use: {product_data['how_to_use']}")
        
        if 'side_effects' in product_data:
            context_parts.append(f"Side Effects: {product_data['side_effects']}")
        
        if 'price' in product_data:
            context_parts.append(f"Price: {product_data['price']}")
        
        return "\n".join(context_parts)