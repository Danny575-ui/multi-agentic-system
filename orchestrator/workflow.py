import json
import os
from agents.parser_agent import ParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.faq_agent import FAQAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_agent import ComparisonAgent

class WorkflowOrchestrator:
    """
    Orchestrates the multi-agent workflow.
    Handles multiple products and generates all required pages.
    """
    
    def __init__(self):
        self.parser = ParserAgent()
        self.question_generator = QuestionGeneratorAgent()
        self.faq_agent = FAQAgent()
        self.product_agent = ProductPageAgent()
        self.comparison_agent = ComparisonAgent()
        
        # Create output directory
        os.makedirs('output', exist_ok=True)
    
    def run(self, input_file='data/input_product.json'):
        """Run the complete workflow"""
        print("=" * 60)
        print("MULTI-AGENT WORKFLOW STARTED")
        print("=" * 60)
        print()
        
        # Step 1: Load and parse all products
        print("Step 1: Loading and parsing product data...")
        with open(input_file, 'r') as f:
            raw_data = json.load(f)
        
        # Handle both single product and multiple products
        if 'products' in raw_data:
            products = [self.parser.process(p) for p in raw_data['products']]
        else:
            products = [self.parser.process(raw_data)]
        
        print(f"✓ Parsed {len(products)} product(s)")
        for prod in products:
            print(f"  - {prod['name']}")
        print()
        
        # Step 2: Generate questions for first product
        print("Step 2: Generating questions...")
        questions = self.question_generator.process(products[0])
        print(f"✓ Generated {len(questions)} questions")
        print()
        
        # Save questions
        with open('output/questions.json', 'w') as f:
            json.dump(questions, f, indent=2)
        
        # Step 3: Create FAQ page for first product
        print("Step 3: Creating FAQ page...")
        faq_data = self.faq_agent.process({
            'questions': questions,
            'product': products[0]
        })
        print(f"✓ FAQ created with {faq_data['total_questions']} Q&As")
        print()
        
        # Save FAQ
        with open('output/faq.json', 'w') as f:
            json.dump(faq_data, f, indent=2)
        
        # Step 4: Create product pages for all products
        print("Step 4: Creating product pages...")
        product_pages = []
        for i, product in enumerate(products):
            print(f"  Creating page for {product['name']}...")
            product_page = self.product_agent.process(product)
            product_pages.append(product_page)
            
            # Save individual product page
            filename = f"output/product_page_{i+1}.json"
            with open(filename, 'w') as f:
                json.dump(product_page, f, indent=2)
        
        print(f"✓ Created {len(product_pages)} product page(s)")
        print()
        
        # Step 5: Create comparison page
        print("Step 5: Creating comparison page...")
        if len(products) >= 2:
            comparison_page = self.comparison_agent.process({
                'product_a': products[0],
                'product_b': products[1]
            })
            print(f"✓ Comparison: {products[0]['name']} vs {products[1]['name']}")
        else:
            # Use fictional product B
            comparison_page = self.comparison_agent.process({
                'product': products[0]
            })
            print(f"✓ Comparison with fictional competitor")
        print()
        
        # Save comparison page
        with open('output/comparison_page.json', 'w') as f:
            json.dump(comparison_page, f, indent=2)
        
        print("=" * 60)
        print("WORKFLOW COMPLETE")
        print("=" * 60)
        print()
        print("✓ Saved: output/questions.json")
        print("✓ Saved: output/faq.json")
        for i in range(len(products)):
            print(f"✓ Saved: output/product_page_{i+1}.json")
        print("✓ Saved: output/comparison_page.json")
        print()
        print("🎉 All outputs saved successfully!")
        
        return {
            'products': products,
            'questions': questions,
            'faq': faq_data,
            'product_pages': product_pages,
            'comparison': comparison_page
        }