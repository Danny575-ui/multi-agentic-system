#!/usr/bin/env python3
"""
Multi-Agent Content Generation System
Entry point for CLI execution
"""
import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Import orchestrator
from orchestrator.workflow import WorkflowOrchestrator

def main():
    """Main entry point"""
    print("🚀 Starting Multi-Agent Workflow...")
    print()
    
    orchestrator = WorkflowOrchestrator()
    results = orchestrator.run()
    
    print("\n✅ SUCCESS! All pages generated.")
    print("\n🌐 Want to view results in a web browser?")
    print("Run: python web_app/app.py")
    print("Then open: http://localhost:5000")

if __name__ == "__main__":
    main()