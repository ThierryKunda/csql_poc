class REPL:
    def __init__(self) -> None:
        self.running = True

    def stop(self):
        self.running = False
    
    def execute_sql(self, command_as_string: str):
        if command_as_string == "!quit":
            print("Exiting the program.")
            self.running = False
            return
        print("Cannot execute SQL command yet.")

    def run(self):
        while self.running:
            try:
                self.execute_sql(input("csql> "))
            except KeyboardInterrupt:
                print('Exiting the program from interruption.')
                self.running = False