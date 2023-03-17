

class Base_command():
    """Base class for all commands."""
    def __init__(self, args):
        self.args = args
        self._validate_args()

    def _validate_args(self):
        """Validate the arguments passed to the command."""
        pass

    def run(self):
        """Run the command."""
        pass

class Command(Base_command):
    keyword = ""
    def _validate_args(self, command : str):
        self.keyword = command

    def run(self):
        print(f"Running the {self.keyword} command.")