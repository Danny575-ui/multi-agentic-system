# Multi-Agent Content Generation System

**A true multi-agent system for autonomous content generation with dynamic agent coordination.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Multi--Agent-green)](/)
[![Status](https://img.shields.io/badge/Status-Production--Ready-success)](/)

---

## 🎯 Project Overview

This system implements a **capability-based multi-agent architecture** that autonomously generates structured content pages (FAQ, Product Description, Comparison) from minimal product data. Unlike traditional sequential scripts, this system features:

- ✅ **Autonomous agents** with independent decision-making logic
- ✅ **Dynamic agent discovery** through capability-based registry
- ✅ **Event-driven orchestration** without hard-coded sequences
- ✅ **Minimal LLM dependency** - automation over prompting
- ✅ **Modular & extensible** design for production use

**Key Innovation**: Agents are discovered dynamically based on capabilities, not called in a fixed order.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────┐
│         Agent Registry                   │
│   (Dynamic Capability Discovery)         │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│      Workflow Orchestrator               │
│  • Task routing by capability            │
│  • Event-driven coordination             │
│  • No hard-coded agent calls             │
└──────────────┬──────────────────────────┘
               │
      ┌────────┴────────┐
      ▼                 ▼
┌──────────┐      ┌──────────────┐
│  Agents  │◄─────┤ Logic Blocks │
│ (5 types)│      │ (Reusable)   │
└────┬─────┘      └──────────────┘
     │
     ▼
┌──────────┐
│Templates │
└──────────┘
```

### Agent Types

| Agent | Responsibility | Automation Method |
|-------|---------------|-------------------|
| **ParserAgent** | Data validation & transformation | Pure data processing |
| **QuestionGeneratorAgent** | Generate 15 categorized questions | Rule-based templates (NO LLM) |
| **FAQAgent** | Create FAQ with 5 Q&As | Logic blocks + LLM fallback |
| **ProductPageAgent** | Generate product descriptions | Logic blocks + LLM for creative text |
| **ComparisonAgent** | Analyze & compare products | Pure algorithmic logic (NO LLM) |

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
Ollama (for LLM tasks)
```

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd kasparro-multi-agent-system-dhanush-p
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Start Ollama** (in separate terminal)
```bash
ollama serve
ollama pull llama3.2
```

### Usage

**Step 1: Generate Content**
```bash
python main.py
```

Output:
```
✓ Saved: output/questions.json (15 questions)
✓ Saved: output/faq.json (5 Q&As)
✓ Saved: output/product_page_1.json
✓ Saved: output/product_page_2.json
✓ Saved: output/comparison_page.json
```

**Step 2: View Results in Browser**
```bash
python web_app/app.py
```

Open: `http://localhost:5000`

---

## 📁 Project Structure

```
kasparro-multi-agent-system-dhanush-p/
│
├── agents/                     # Autonomous agent implementations
│   ├── base_agent.py           # Abstract base with capabilities
│   ├── parser_agent.py         # Data validation & parsing
│   ├── question_generator_agent.py  # Rule-based question generation
│   ├── faq_agent.py            # FAQ creation with logic blocks
│   ├── product_page_agent.py   # Product page generation
│   └── comparison_agent.py     # Algorithmic product comparison
│
├── logic_blocks/               # Reusable logic components
│   ├── llm_client.py           # Ollama API wrapper
│   ├── answer_generator.py     # Context-based answer generation
│   ├── benefits_extractor.py   # Benefit extraction logic
│   └── comparison_logic.py     # Comparison algorithms
│
├── templates/                  # Output structure contracts
│   ├── faq_template.py         # FAQ page template
│   ├── product_template.py     # Product page template
│   └── comparison_template.py  # Comparison page template
│
├── orchestrator/               # Coordination layer
│   └── workflow.py             # Agent registry & dynamic routing
│
├── data/                       # Input data
│   └── input_product.json      # Product data (2 products)
│
├── output/                     # Generated content
│   ├── questions.json          # 15 categorized questions
│   ├── faq.json                # FAQ page
│   ├── product_page_1.json     # Product 1 description
│   ├── product_page_2.json     # Product 2 description
│   └── comparison_page.json    # Product comparison
│
├── web_app/                    # Web visualization
│   ├── app.py                  # Flask server
│   └── templates/
│       └── index.html          # Dashboard UI
│
├── docs/                       # Documentation
│   └── projectdocumentation.md # Detailed system design
│
├── main.py                     # CLI entry point
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

---

## 🎨 Features

### 1. True Multi-Agent Architecture
- **Agent Registry** for dynamic discovery
- **Capability-based routing** (not hard-coded calls)
- **Autonomous decision-making** by each agent
- **Message-passing infrastructure** (BaseAgent)

### 2. Minimal LLM Dependency
- **Questions**: 100% rule-based templates
- **FAQ Answers**: Logic-first, LLM fallback
- **Comparison**: 100% algorithmic
- **Product Descriptions**: LLM only for creative text

### 3. Modular & Extensible
- Add new agents → Register in orchestrator
- Add new logic blocks → Import in agents
- Modify templates → Update output contracts

### 4. Production-Ready Patterns
- Type hints throughout
- Safe defaults in templates
- Validation at boundaries
- Structured error handling

---

## 📊 Sample Outputs

### Questions (15 total across 7 categories)
```json
[
  {
    "question": "What is GlowBoost Vitamin C Serum and what does it do?",
    "category": "Informational"
  },
  {
    "question": "Are there any side effects of using GlowBoost Vitamin C Serum?",
    "category": "Safety"
  },
  // ... 13 more
]
```

### FAQ (5 Q&As with diverse categories)
```json
{
  "page_type": "FAQ",
  "product_name": "GlowBoost Vitamin C Serum",
  "questions": [
    {
      "question": "...",
      "answer": "...",
      "category": "Informational"
    }
    // ... 4 more
  ]
}
```

### Product Page
```json
{
  "page_type": "Product Description",
  "title": "GlowBoost Vitamin C Serum",
  "description": "...",
  "specifications": { ... },
  "usage_guide": [ ... ],
  "safety_info": { ... }
}
```

### Comparison Page
```json
{
  "page_type": "Product Comparison",
  "product_a": { ... },
  "product_b": { ... },
  "comparison_analysis": "...",
  "recommendations": { ... },
  "winner": "..."
}
```

---

## 🔧 Technical Highlights

### Dynamic Agent Coordination
```python
# Orchestrator doesn't hard-code agent calls
parser = registry.find_agent_for_task("parse_data")
question_gen = registry.find_agent_for_task("generate_questions")

# Agents are discovered based on capabilities
```

### Rule-Based Automation
```python
# Question generation: NO LLM
QUESTION_TEMPLATES = {
    "Safety": [
        "Are there any side effects of using {product_name}?",
        "Can I use {product_name} if I have sensitive skin?"
    ]
}
# Fill with product data → instant questions
```

### Algorithmic Comparison
```python
# Comparison logic: NO LLM
def compare_products(a, b):
    price_a = extract_price(a['price'])
    price_b = extract_price(b['price'])
    winner = determine_winner_by_scoring(...)
    return structured_comparison
```

---

## 🎯 Key Differentiators

### Addressing Assignment Feedback

✅ **Clear separation of responsibilities**
- Each agent has one well-defined role
- No overlapping functionality

✅ **Dynamic agent interaction**
- Agent Registry enables discovery
- Capability-based routing (not static calls)

✅ **Agent autonomy**
- Agents make independent decisions
- Example: FAQAgent decides "rules or LLM?"

✅ **True agentic architecture**
- BaseAgent foundation for all agents
- Message-passing infrastructure
- Polymorphic agent handling

---

##  Extensibility Examples

### Add New Agent
```python
class SEOAgent(BaseAgent):
    def __init__(self):
        super().__init__("SEOAgent")
        self.capabilities = ["optimize_seo"]
    
    def can_handle(self, task_type):
        return task_type in self.capabilities
    
    def process(self, data):
        # SEO optimization logic
        pass

# Register in orchestrator
registry.register(SEOAgent())
```

### Add New Logic Block
```python
# logic_blocks/sentiment_analyzer.py
def analyze_sentiment(text):
    # Reusable sentiment analysis
    pass

# Use in any agent
from logic_blocks.sentiment_analyzer import analyze_sentiment
```

---

##  Testing

```bash
# Run all tests
pytest

# Test individual agents
pytest tests/test_parser_agent.py
pytest tests/test_question_generator.py
```

---

##  Documentation

- **Detailed System Design**: [docs/projectdocumentation.md](docs/projectdocumentation.md)
- **API Reference**: See docstrings in each module
- **Architecture Diagrams**: In project documentation

---

##  Contributing

This is a showcase project for Kasparro's Applied AI Engineer assignment. For questions or suggestions, please contact the author.

---

##  License

This project is created for educational and evaluation purposes.

---

##  Author

**Dhanush P**
- Assignment: Kasparro Applied AI Engineer Challenge
- Focus: Multi-Agent Systems, Content Automation, System Design

---

##  Technical Stack

- **Language**: Python 3.8+
- **LLM**: Ollama (Llama 3.2)
- **Web Framework**: Flask
- **Architecture**: Multi-Agent System with Dynamic Coordination
- **Design Patterns**: Registry, Template, Strategy

---

##  Performance

- **Question Generation**: < 1 second (rule-based)
- **FAQ Creation**: 2-5 seconds (mostly logic, minimal LLM)
- **Product Pages**: 10-15 seconds (LLM for descriptions)
- **Comparison**: < 1 second (pure algorithms)

**Total Pipeline**: ~30-45 seconds for complete content generation

---

## 🔮 Future Enhancements

- [ ] Async agent execution
- [ ] Distributed agent deployment
- [ ] Inter-agent messaging system
- [ ] Advanced error recovery
- [ ] Multi-language support
- [ ] Real-time collaboration

