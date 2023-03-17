from abc import ABC, abstractmethod
import sys

class Base_command():
    """Base class for all commands."""

    @abstractmethod
    def run(self):
        """Run the command."""
        pass

class Command(Base_command):
    keyword = ""
    def __init__(self, keyword):
        self.keyword = keyword

    def run(self):
        print(f"Running the {self.keyword} command.")
        if self.keyword == "escape":
            sys.exit()