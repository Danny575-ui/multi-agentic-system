from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """
    Abstract base class for all agents.
    Enforces single responsibility principle.
    """
    
    def __init__(self, name):
        self.name = name
        print(f"[{self.name}] Initialized")
    
    @abstractmethod
    def process(self, input_data):
        """
        Process input and return output.
        Must be implemented by all agents.
        """
        pass
    
    def log(self, message):
        """Helper method for consistent logging"""
        print(f"[{self.name}] {message}")