from enum import Enum
import sqlparse

class Select:
    def __init__(self, table, columns) -> None:
        self.table = table
        self.columns = columns

class Executor:
    def __init__(self):
        self.history = []

    def _parse_input(self, input: str):
        output, _ = sqlparse.parse(input)


    def execute(self, input: str):
        self.history.append(input) 
        print("Cannot execute SQL command yet.")

    def show_history(self):
        for el in self.history:
            print(el)

class REPL:
    def __init__(self) -> None:
        self.running = True
        self.executor = Executor()

    def stop(self):
        self.running = False
    
    def execute_sql(self, command_as_string: str):
        if command_as_string == "!quit":
            print("Exiting the program.")
            self.running = False
            return
        elif command_as_string == "!hist":
            self.executor.show_history()
            return
        self.executor.execute(command_as_string)

    def run(self):
        while self.running:
            try:
                self.execute_sql(input("csql> "))
            except KeyboardInterrupt:
                print('Exiting the program from interruption.')
                self.running = False