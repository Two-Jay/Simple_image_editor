

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
    """Command class for the 'test' command."""
    def _validate_args(self):
        """Validate the arguments passed to the command."""
        if not self.args:
            raise ValueError("No arguments passed to the command.")

    def run(self):
        """Run the command."""
        print("Running the 'test' command.")