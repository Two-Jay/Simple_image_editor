from abc import ABC, abstractmethod
import sys

class Command(ABC):
    keyword = ""
    def __init__(self, keyword):
        self.keyword = keyword

    @abstractmethod
    def run(self):
        pass

class Exit_command(Command):
    def __init__(self):
        super(Exit_command, self).__init__("exit")

    def run(self):
        sys.exit()

class Save_command(Command):
    def __init__(self):
        super(Save_command, self).__init__("save")

    def run(self):
        print(f"{type(self).__name__} : {self.keyword} command is running.")

class Open_command(Command):
    def __init__(self):
        super(Open_command, self).__init__("open")

    def run(self):
        print(f"{type(self).__name__} : {self.keyword} command is running.")