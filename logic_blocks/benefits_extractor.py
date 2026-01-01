from logic_blocks.llm_client import OllamaClient

def extract_benefits(product_data):
    """
    Extract and elaborate on product benefits.
    Returns list of benefit objects with descriptions.
    """
    llm = OllamaClient()
    
    raw_benefits = product_data.get('benefits', '')
    
    prompt = f"""Extract and elaborate on the benefits of this product:

Product: {product_data.get('name', '')}
Listed Benefits: {raw_benefits}
Ingredients: {product_data.get('key_ingredients', '')}

For each benefit, provide a brief 1-sentence explanation.

Format your response as:
1. [Benefit Name] - [How it works]
2. [Benefit Name] - [How it works]

Generate the benefits now:"""

    response = llm.generate(prompt, max_tokens=200)
    
    # Parse or use fallback
    benefits = []
    lines = response.strip().split('\n')
    
    for line in lines:
        line = line.strip().lstrip('0123456789.- ')
        if '-' in line and line:
            try:
                parts = line.split('-', 1)
                benefits.append({
                    'name': parts[0].strip(),
                    'description': parts[1].strip()
                })
            except:
                continue
    
    # Fallback if parsing fails
    if len(benefits) == 0:
        for benefit in raw_benefits.split(','):
            benefit = benefit.strip()
            if benefit:
                benefits.append({
                    'name': benefit,
                    'description': f'This product provides {benefit.lower()} benefits.'
                })
    
    return benefits


def format_benefits_html(benefits):
    """Format benefits as HTML list"""
    html = '<ul>'
    for benefit in benefits:
        html += f'<li><strong>{benefit["name"]}</strong>: {benefit["description"]}</li>'
    html += '</ul>'
    return html


def get_benefit_summary(benefits):
    """Get a one-line summary of all benefits"""
    if not benefits:
        return "Multiple skincare benefits"
    
    benefit_names = [b['name'] for b in benefits[:3]]
    
    if len(benefit_names) == 1:
        return benefit_names[0]
    elif len(benefit_names) == 2:
        return f"{benefit_names[0]} and {benefit_names[1]}"
    else:
        return f"{', '.join(benefit_names[:-1])}, and {benefit_names[-1]}"