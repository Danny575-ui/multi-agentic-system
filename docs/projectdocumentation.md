# Project Documentation: Multi-Agent Content Generation System

**Kasparro Applied AI Engineer Challenge - Resubmission**  
**Author**: Dhanush P  
**Date**: January 2026

---

## Table of Contents

1. [Problem Statement](#1-problem-statement)
2. [Solution Overview](#2-solution-overview)
3. [Scopes & Assumptions](#3-scopes--assumptions)
4. [System Design](#4-system-design)
5. [Addressing Previous Feedback](#5-addressing-previous-feedback)
6. [Agent Architecture](#6-agent-architecture)
7. [Workflow Orchestration](#7-workflow-orchestration)
8. [Logic Blocks](#8-logic-blocks)
9. [Template System](#9-template-system)
10. [Performance & Scalability](#10-performance--scalability)

---

## 1. Problem Statement

### 1.1 Challenge Requirements

The Kasparro Applied AI Engineer challenge requires designing a modular agentic automation system with the following specifications:

**Input Requirements:**
- Accept minimal product data (exactly 8 fields per product)
- No external data sources permitted
- JSON format input only

**Processing Requirements:**
- Implement true multi-agent architecture
- Agents must demonstrate autonomous decision-making
- Dynamic agent coordination (capability-based, not hard-coded)
- Reusable logic components
- Template-driven output generation

**Output Requirements:**
- Generate 15+ categorized user questions
- Create FAQ page (minimum 5 Q&As)
- Produce product description pages
- Generate product comparison page
- All outputs in machine-readable JSON format

### 1.2 Critical Distinction

**What qualifies as a true multi-agent system:**
- Dynamic agent discovery via registry
- Capability-based routing
- Agent autonomy with internal decision-making
- Event-driven coordination
- No hard-coded agent calls

**What does NOT qualify:**
- Sequential function calls labeled as "agents"
- Hard-coded agent instantiation
- Static control flow
- External control of agent internal logic

### 1.3 Evaluation Criteria

| Criterion | Weight | Requirements |
|-----------|--------|-------------|
| Agentic System Design | 45% | Clear responsibilities, modularity, extensibility, correct flow |
| Types & Quality of Agents | 25% | Meaningful roles, appropriate boundaries, correct I/O |
| Content System Engineering | 20% | Template quality, logic block composability |
| Data & Output Structure | 10% | JSON correctness, clean data mapping |

---

## 2. Solution Overview

### 2.1 Architectural Approach

This system implements a **capability-based multi-agent architecture** using Registry + Strategy design patterns.

**Core Innovations:**

1. **Agent Registry Pattern**
   - Central registry maintains all available agents
   - Agents register their capabilities at initialization
   - Dynamic discovery eliminates hard-coded dependencies

2. **Capability-Based Routing**
   - Tasks routed based on required capabilities
   - Agents discovered dynamically, not instantiated directly
   - Orchestrator has no knowledge of agent implementations

3. **Agent Autonomy**
   - Each agent independently decides processing approach
   - Internal logic is encapsulated and private
   - Agents make decisions without external control

4. **Minimal LLM Dependency**
   - Automation-first, prompting-last philosophy
   - Rule-based logic prioritized over LLM calls
   - LLM used only when rule-based approaches insufficient

### 2.2 System Components

**Five Specialized Agents:**
1. ParserAgent - Data validation and transformation
2. QuestionGeneratorAgent - Rule-based question generation
3. FAQAgent - FAQ creation with logic-first approach
4. ProductPageAgent - Product description generation
5. ComparisonAgent - Algorithmic product comparison

**Four Logic Blocks:**
1. LLMClient - Centralized LLM API wrapper
2. AnswerGenerator - Context-based answer generation
3. BenefitsExtractor - Benefit parsing and elaboration
4. ComparisonLogic - Algorithmic comparison functions

**Three Templates:**
1. FAQTemplate - FAQ page structure
2. ProductTemplate - Product page structure
3. ComparisonTemplate - Comparison page structure

### 2.3 Architecture Diagram

```
INPUT: product data (JSON)
         ↓
┌─────────────────────────────────────┐
│      Workflow Orchestrator          │
│  • register_agent()                 │
│  • find_agent_for_task()            │
│  • run_workflow()                   │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│         Agent Registry               │
│  {                                   │
│    "parse_data": ParserAgent,       │
│    "generate_questions": QGenAgent, │
│    "create_faq": FAQAgent,          │
│    "create_product_page": PPAgent,  │
│    "compare_products": CmpAgent     │
│  }                                   │
└──────────────┬──────────────────────┘
               ↓
        [5 Agents]
               ↓
     [4 Logic Blocks]
               ↓
      [3 Templates]
               ↓
OUTPUT: 5 JSON files
```

---

## 3. Scopes & Assumptions

### 3.1 In Scope

**Agent Capabilities:**
- Data parsing with validation
- Rule-based question generation (15 questions, 7 categories)
- FAQ creation (5 Q&As)
- Product description generation
- Algorithmic product comparison

**Architecture Features:**
- Dynamic agent discovery
- Capability-based routing
- Autonomous agent decision-making
- Reusable logic blocks
- Template-driven formatting
- Web visualization dashboard

### 3.2 Out of Scope

**External Data:**
- No web scraping
- No external APIs
- No database lookups

**Advanced Features:**
- Distributed deployment
- Agent learning/adaptation
- Real-time collaboration
- Persistent state management

### 3.3 Key Assumptions

**Input:**
- JSON is well-formed
- All 8 fields present per product
- Exactly 2 products provided

**LLM:**
- Ollama running locally
- Llama 3.2 model available
- Sufficient compute resources

**Environment:**
- Python 3.8+
- File write permissions
- No concurrent execution

---

## 4. System Design

### 4.1 Design Principles

**SOLID Principles Applied:**

1. **Single Responsibility**: Each agent has ONE task
2. **Open/Closed**: System open for extension, closed for modification
3. **Liskov Substitution**: All agents interchangeable via BaseAgent
4. **Interface Segregation**: Minimal interface in BaseAgent
5. **Dependency Inversion**: Depend on abstractions, not implementations

### 4.2 Architecture Patterns

**Registry Pattern:**
- Central agent registry
- Dynamic lookup by capability
- Runtime discovery

**Strategy Pattern:**
- Each agent is a strategy
- Encapsulates algorithms
- Interchangeable processing

**Template Pattern:**
- BaseAgent defines structure
- Subclasses implement behavior
- Consistent interface

### 4.3 Data Flow

```
INPUT: input_product.json (2 products, 8 fields each)
  ↓
ParserAgent: Validates & structures data
  ↓
QuestionGeneratorAgent: Creates 15 questions (rule-based)
  ↓ (questions)
  ├→ FAQAgent: Generates 5 Q&As (logic + LLM)
  |
ProductPageAgent: Creates descriptions (logic + LLM)
  |
ComparisonAgent: Analyzes products (algorithmic)
  ↓
OUTPUT: 5 JSON files
```

---

## 5. Addressing Previous Feedback

### 5.1 Feedback Received

**Original Submission Issues:**

> "Simply hard-coding multiple functions or sequential logic and labeling them as 'agents' does not satisfy this requirement."

**Required:**
- Clear separation of agent responsibilities
- Dynamic agent interaction and coordination
- Architecture that supports agent autonomy

### 5.2 How Current Solution Addresses Feedback

#### Issue 1: Hard-Coded Sequential Calls

**Before (Wrong):**
```python
# Direct instantiation - WRONG
parser = ParserAgent()
question_gen = QuestionGeneratorAgent()
faq = FAQAgent()
```

**After (Correct):**
```python
# Dynamic discovery - CORRECT
parser = orchestrator.find_agent_for_task("parse_data")
question_gen = orchestrator.find_agent_for_task("generate_questions")
faq = orchestrator.find_agent_for_task("create_faq")
```

#### Issue 2: No Agent Autonomy

**Current Implementation:**
- FAQAgent independently decides: data extraction vs rule logic vs LLM
- Each agent has private methods for internal decision-making
- No external control of agent logic

#### Issue 3: Static Control Flow

**Current Implementation:**
- Agents register capabilities: `self.capabilities = ["parse_data"]`
- Orchestrator discovers dynamically: `agent.can_handle(task_type)`
- No if/else chains based on agent names

### 5.3 Key Improvements Summary

| Aspect | Before | After |
|--------|--------|-------|
| Agent Discovery | Hard-coded | Dynamic via registry |
| Task Routing | Static if/else | Capability-based |
| Agent Control | External | Autonomous |
| Extensibility | Requires code changes | Just register new agent |
| Coupling | Tight | Loose |

---

## 6. Agent Architecture

### 6.1 BaseAgent: Foundation

**Purpose:** Abstract base class enforcing consistent interface

**Key Methods:**
- `can_handle(task_type)`: Checks capability
- `process(data)`: Processes input (must be implemented)
- `log(message)`: Consistent logging

**Design Pattern:** Template Method Pattern

### 6.2 Agent Specifications

#### ParserAgent
- **Capability:** `parse_data`
- **Method:** Pure data processing (no LLM)
- **Input:** File path
- **Output:** Validated product objects
- **Logic:** Schema validation, ID assignment, error handling

#### QuestionGeneratorAgent
- **Capability:** `generate_questions`
- **Method:** Rule-based templates (no LLM)
- **Input:** Product data
- **Output:** 15 categorized questions
- **Logic:** Template filling, 7 categories
- **Generation Time:** < 1 second

**Question Templates Example:**
```python
TEMPLATES = {
    "Informational": [
        "What is {product_name} and what does it do?",
        "What is the concentration of {concentration_value}?",
        "What skin types is {product_name} suitable for?"
    ],
    "Safety": [
        "Are there any side effects?",
        "Can I use with sensitive skin?",
        "Should I do a patch test?"
    ]
    # ... 5 more categories
}
```

#### FAQAgent
- **Capability:** `create_faq`
- **Method:** Logic-first with LLM fallback
- **Input:** Questions + product data
- **Output:** 5 Q&As with diverse categories
- **Autonomy:** Decides answer method per question

**Decision Tree:**
```
Question → Simple lookup? 
    Yes → Extract from data
    No → Rule pattern?
        Yes → Apply rule
        No → Use LLM
```

#### ProductPageAgent
- **Capability:** `create_product_page`
- **Method:** Hybrid (logic blocks + LLM)
- **Input:** Single product
- **Output:** Complete product page
- **Pipeline:** Extract benefits → Generate narrative → Structure specs → Create guide

**3-Paragraph Structure:**
1. Introduction & target audience
2. How it works (ingredients & mechanism)
3. Expected results & outcomes

#### ComparisonAgent
- **Capability:** `compare_products`
- **Method:** Algorithmic (no LLM for scoring)
- **Input:** Two products
- **Output:** Detailed comparison analysis
- **Dimensions:** Price, concentration, ingredients, skin type, usage

**Algorithmic Comparisons:**
- Price: Regex extraction + arithmetic
- Ingredients: Set operations (intersection, difference)
- Skin type: String matching for versatility
- Recommendations: Decision tree logic

---

## 7. Workflow Orchestration

### 7.1 Orchestrator Design

**Core Responsibilities:**
1. Maintain agent registry
2. Discover agents by capability
3. Route tasks dynamically
4. Aggregate results
5. Handle errors

### 7.2 Implementation

```python
class WorkflowOrchestrator:
    def __init__(self):
        self.registry = {}  # Dynamic agent storage
    
    def register_agent(self, agent: BaseAgent):
        """Add agent to registry"""
        self.registry[agent.name] = agent
    
    def find_agent_for_task(self, task_type: str) -> BaseAgent:
        """Discover agent by capability"""
        for agent in self.registry.values():
            if agent.can_handle(task_type):
                return agent
        raise ValueError(f"No agent for: {task_type}")
    
    def run_workflow(self, input_file: str):
        """Execute complete workflow"""
        # Dynamic discovery at each step
        parser = self.find_agent_for_task("parse_data")
        products = parser.process({"file": input_file})
        
        question_gen = self.find_agent_for_task("generate_questions")
        questions = question_gen.process(products)
        
        # ... continues with dynamic discovery
```

### 7.3 Why This is Not Hard-Coded

**Key Differences from Static Approach:**

1. **No Direct Imports in Workflow**
   - Orchestrator never imports specific agent classes
   - Only knows BaseAgent interface

2. **Runtime Discovery**
   - Agents found at execution time, not compile time
   - New agents add without orchestrator changes

3. **Capability-Based Routing**
   - Tasks routed by capability string
   - No agent name checking or if/else chains

4. **Extensibility Example:**
```python
# Add new agent - NO orchestrator changes needed
class SEOAgent(BaseAgent):
    def __init__(self):
        super().__init__("SEOAgent")
        self.capabilities = ["optimize_seo"]
    
    def process(self, data):
        # SEO logic
        pass

# Just register
orchestrator.register_agent(SEOAgent())

# Use immediately
seo = orchestrator.find_agent_for_task("optimize_seo")
```

---

## 8. Logic Blocks

### 8.1 Design Philosophy

**Purpose:** Reusable, composable functions shared across agents

**Principles:**
- Single Responsibility
- Stateless operation
- Composability
- Independent testing
- Multi-agent reuse

### 8.2 Logic Block Catalog

#### 8.2.1 LLMClient
**Purpose:** Centralized LLM API wrapper

**Features:**
- Consistent interface for all LLM calls
- Centralized error handling
- Configuration management
- Easy provider swapping

**Used By:** FAQAgent, ProductPageAgent, ComparisonAgent

#### 8.2.2 AnswerGenerator
**Purpose:** Generate contextual FAQ answers

**Features:**
- Context building from product data
- Prompt engineering
- Response formatting

**Used By:** FAQAgent

#### 8.2.3 BenefitsExtractor
**Purpose:** Parse and elaborate benefits

**Features:**
- Benefit splitting and cleaning
- Rule-based elaboration
- Mechanism explanation

**Used By:** ProductPageAgent

#### 8.2.4 ComparisonLogic
**Purpose:** Algorithmic comparison functions

**Features:**
- Price comparison (regex + arithmetic)
- Ingredient analysis (set operations)
- Skin type assessment
- Recommendation generation

**Used By:** ComparisonAgent

### 8.3 Logic Block vs Agent

**When to use Logic Block:**
- Reusable across multiple agents
- Stateless operation
- Single focused function

**When to use Agent:**
- Owns complete workflow step
- Maintains internal state
- Makes autonomous decisions

---

## 9. Template System

### 9.1 Template Purpose

**Purpose:** Define structured output formats as contracts

**Benefits:**
- Consistent output structure
- Type safety
- Default values
- Documentation

### 9.2 Template Specifications

#### FAQTemplate
```python
{
    "page_type": "FAQ",
    "title": str,
    "product_name": str,
    "questions": [
        {
            "question": str,
            "answer": str,
            "category": str
        }
    ],
    "total_questions": int,
    "generated_at": datetime
}
```

#### ProductTemplate
```python
{
    "page_type": "Product Description",
    "title": str,
    "product_id": str,
    "tagline": str,
    "description": str (3 paragraphs),
    "benefits": [
        {"name": str, "description": str}
    ],
    "specifications": dict,
    "usage_guide": list,
    "target_audience": list,
    "safety_info": dict
}
```

#### ComparisonTemplate
```python
{
    "page_type": "Product Comparison",
    "title": str,
    "product_a": dict,
    "product_b": dict,
    "detailed_comparison": dict,
    "comparison_analysis": str,
    "recommendations": dict,
    "insights": list,
    "winner": str
}
```

### 9.3 Template Usage

Templates ensure:
1. All required fields present
2. Correct data types
3. Nested structure consistency
4. Machine-readable output

---

## 10. Performance & Scalability

### 10.1 Performance Metrics

| Task | Method | Time | LLM Used |
|------|--------|------|----------|
| Question Generation | Rule-based | < 1 sec | No |
| FAQ Creation | Logic + LLM | 2-5 sec | Minimal |
| Product Pages (2) | Logic + LLM | 10-15 sec | Yes |
| Comparison | Algorithmic | < 1 sec | No |
| **Total Pipeline** | **Mixed** | **30-45 sec** | **Minimal** |

### 10.2 Scalability Considerations

**Current Design:**
- Sequential agent execution
- Single-threaded processing
- Suitable for 2-10 products

**Future Enhancements:**
- Async agent execution
- Parallel product processing
- Distributed agent deployment
- Message queue for coordination

### 10.3 LLM Optimization

**Minimization Strategy:**
- Questions: 100% rule-based (0 LLM calls)
- Comparison: 100% algorithmic (0 LLM calls for scoring)
- FAQ: Logic-first, LLM fallback (reduced calls)
- Product: LLM only for narrative (not structure)

**Result:** ~70% of processing without LLM

### 10.4 System Strengths

**Strengths:**
1. Dynamic agent coordination
2. Minimal LLM dependency
3. Modular, extensible design
4. Clear separation of concerns
5. Production-ready patterns

**Trade-offs:**
1. Sequential vs parallel execution
2. Simplicity vs maximum performance
3. Local LLM vs cloud API

---

## Conclusion

This multi-agent system demonstrates true agentic architecture through:

1. **Dynamic Coordination**: Agents discovered by capability, not hard-coded
2. **Agent Autonomy**: Each agent makes independent processing decisions
3. **Extensibility**: New agents register without code changes
4. **Minimal LLM Usage**: Automation-first approach (70% rule-based)
5. **Production Patterns**: SOLID principles, clean architecture

The system successfully addresses all feedback from the initial submission by implementing genuine multi-agent architecture with dynamic discovery, capability-based routing, and agent autonomy.

**Key Innovation:** Capability-based registry enables true dynamic coordination without static control flow.

**Result:** Production-ready system generating 5 structured content pages (15 questions, 5 Q&As, 2 product pages, 1 comparison) from minimal input data in 30-45 seconds.

---

## Appendix: Output Examples

### Example 1: Questions Output
15 questions across 7 categories generated via rule-based templates (< 1 second, no LLM).

### Example 2: FAQ Output
5 Q&As with diverse categories using logic-first approach with LLM fallback (2-5 seconds).

### Example 3: Product Page
Complete product description with 3-paragraph narrative, benefits, specifications, and usage guide (10-15 seconds per product).

### Example 4: Comparison Page
Algorithmic comparison with price analysis, ingredient overlap, skin type assessment, and recommendations (< 1 second for logic, minimal LLM for narrative only).

---

**End of Documentation**