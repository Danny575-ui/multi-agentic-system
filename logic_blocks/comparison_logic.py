"""
Reusable logic block for product comparison.
Pure ALGORITHMIC logic - NO LLM dependency.
"""

def _extract_price(price_str: str) -> int:
    """Extract numeric price from string with currency symbols"""
    # Only keep ASCII digits 0-9
    digits = ''.join(c for c in price_str if c in '0123456789')
    return int(digits) if digits else 0

def compare_products(product_a: dict, product_b: dict) -> dict:
    """
    Compare two products using ALGORITHMS (NO LLM).
    Returns structured comparison data.
    """
    # Extract prices as integers (FIXED for ₹ symbol)
    price_a = _extract_price(product_a['price'])
    price_b = _extract_price(product_b['price'])
    
    # Extract concentration values
    try:
        conc_a = int(''.join(c for c in product_a['concentration'][:3] if c in '0123456789'))
        conc_b = int(''.join(c for c in product_b['concentration'][:3] if c in '0123456789'))
    except:
        conc_a = 0
        conc_b = 0
    
    comparison = {
        "product_a_name": product_a['name'],
        "product_b_name": product_b['name'],
        
        # Price comparison (ALGORITHM)
        "price_a": price_a,
        "price_b": price_b,
        "price_diff": abs(price_a - price_b),
        "cheaper_product": product_a['name'] if price_a < price_b else product_b['name'],
        "better_price": "product_a" if price_a < price_b else "product_b",
        
        # Concentration comparison (ALGORITHM)
        "concentration_a": conc_a,
        "concentration_b": conc_b,
        "concentration_diff": f"{abs(conc_a - conc_b)}%",
        "higher_concentration": product_a['name'] if conc_a > conc_b else product_b['name'],
        
        # Skin type analysis (LOGIC)
        "skin_type_a": product_a['skin_type'],
        "skin_type_b": product_b['skin_type'],
        "skin_type_match": _analyze_skin_type_overlap(
            product_a['skin_type'], 
            product_b['skin_type']
        ),
        
        # Ingredient analysis (ALGORITHM)
        "ingredients_a": product_a['key_ingredients'],
        "ingredients_b": product_b['key_ingredients'],
        "ingredient_similarity": _calculate_ingredient_overlap(
            product_a['key_ingredients'],
            product_b['key_ingredients']
        ),
        
        # Versatility (LOGIC)
        "more_versatile": _determine_versatility(
            product_a['skin_type'],
            product_b['skin_type']
        )
    }
    
    return comparison

def generate_comparison_analysis(product_a: dict, product_b: dict, comparison: dict) -> str:
    """
    Generate comparison text using RULE-BASED TEMPLATES (NO LLM).
    This is structured text generation from data.
    """
    
    # Paragraph 1: Overview
    para1 = f"""Both {product_a['name']} and {product_b['name']} are skincare serums designed to improve skin health and appearance. {product_a['name']} features {product_a['concentration']} and is formulated for {product_a['skin_type']} skin, while {product_b['name']} contains {product_b['concentration']} and targets {product_b['skin_type']} skin. These products serve different needs in a comprehensive skincare routine."""
    
    # Paragraph 2: Key Differences
    price_comparison = f"{comparison['cheaper_product']} is more affordable at ₹{comparison['price_a'] if comparison['better_price'] == 'product_a' else comparison['price_b']}"
    
    conc_comparison = f"{comparison['higher_concentration']} has a higher concentration" if comparison['concentration_a'] != comparison['concentration_b'] else "Both have similar concentrations"
    
    ingredient_note = f"The formulations show {comparison['ingredient_similarity'].lower()}"
    
    para2 = f"""Key differences include formulation and targeting. {conc_comparison}, which may indicate different potency levels. {ingredient_note}, with {product_a['name']} focusing on {product_a['key_ingredients']} and {product_b['name']} utilizing {product_b['key_ingredients']}. In terms of pricing, {price_comparison}, making it the more budget-friendly option."""
    
    # Paragraph 3: Value Assessment
    versatility_winner = product_a['name'] if comparison['more_versatile'] == 'product_a' else product_b['name']
    
    para3 = f"""{versatility_winner} offers greater versatility in terms of skin type compatibility. For those seeking {product_a['benefits'].lower()}, {product_a['name']} is the clear choice, while {product_b['name']} excels at {product_b['benefits'].lower()}. The price difference of ₹{comparison['price_diff']} should be weighed against your specific skin concerns and budget constraints."""
    
    return f"{para1}\n\n{para2}\n\n{para3}"

def _analyze_skin_type_overlap(skin_type_a: str, skin_type_b: str) -> str:
    """Algorithm: Analyze skin type compatibility"""
    types_a = set(skin_type_a.lower().replace(' ', '').split(','))
    types_b = set(skin_type_b.lower().replace(' ', '').split(','))
    
    overlap = types_a.intersection(types_b)
    
    if "all" in skin_type_b.lower() or "all" in skin_type_a.lower():
        return "One product suits all skin types"
    elif len(overlap) == 0:
        return "Different target skin types"
    elif len(overlap) == len(types_a) and len(overlap) == len(types_b):
        return "Identical skin type targeting"
    else:
        return "Partial overlap in skin types"

def _calculate_ingredient_overlap(ingredients_a: str, ingredients_b: str) -> str:
    """Algorithm: Calculate ingredient similarity"""
    ing_a = set(ingredients_a.lower().replace(' ', '').split(','))
    ing_b = set(ingredients_b.lower().replace(' ', '').split(','))
    
    overlap = ing_a.intersection(ing_b)
    total = ing_a.union(ing_b)
    
    if len(total) == 0:
        return "Unknown"
    
    similarity = len(overlap) / len(total)
    
    if similarity > 0.7:
        return "High similarity"
    elif similarity > 0.3:
        return "Medium similarity"
    else:
        return "Different formulations"

def _determine_versatility(skin_type_a: str, skin_type_b: str) -> str:
    """Algorithm: Determine which product is more versatile"""
    if "all" in skin_type_b.lower():
        return "product_b"
    elif "all" in skin_type_a.lower():
        return "product_a"
    
    count_a = len(skin_type_a.split(','))
    count_b = len(skin_type_b.split(','))
    
    return "product_a" if count_a > count_b else "product_b"

def generate_comparison_table(product_a: dict, product_b: dict) -> str:
    """
    Generate HTML comparison table (TEMPLATE, NO LLM).
    """
    html = f"""
    <table class="comparison-table">
        <thead>
            <tr>
                <th>Feature</th>
                <th>{product_a['name']}</th>
                <th>{product_b['name']}</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Concentration</td>
                <td>{product_a['concentration']}</td>
                <td>{product_b['concentration']}</td>
            </tr>
            <tr>
                <td>Skin Type</td>
                <td>{product_a['skin_type']}</td>
                <td>{product_b['skin_type']}</td>
            </tr>
            <tr>
                <td>Key Ingredients</td>
                <td>{product_a['key_ingredients']}</td>
                <td>{product_b['key_ingredients']}</td>
            </tr>
            <tr>
                <td>Benefits</td>
                <td>{product_a['benefits']}</td>
                <td>{product_b['benefits']}</td>
            </tr>
            <tr>
                <td>Price</td>
                <td><strong>{product_a['price']}</strong></td>
                <td><strong>{product_b['price']}</strong></td>
            </tr>
        </tbody>
    </table>
    """
    return html.strip()