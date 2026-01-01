from flask import Flask, render_template, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    """API endpoint to fetch all generated data"""
    try:
        # Load all JSON files
        with open('output/faq.json', 'r') as f:
            faq = json.load(f)
        
        with open('output/product_page_1.json', 'r') as f:
            product = json.load(f)
        
        with open('output/comparison_page.json', 'r') as f:
            comparison = json.load(f)
        
        with open('output/questions.json', 'r') as f:
            questions = json.load(f)
        
        return jsonify({
            'success': True,
            'faq': faq,
            'product': product,
            'comparison': comparison,
            'questions': questions
        })
    except FileNotFoundError as e:
        return jsonify({
            'success': False,
            'error': f'JSON files not found: {str(e)}. Run main.py first.'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    print("🚀 Starting web server...")
    print("📊 Open browser: http://localhost:5000")
    app.run(debug=True, port=5000)