from datetime import datetime
from collections import Counter


# Custom Exception
class InvalidInputError(Exception):
    pass


# Logger Class
class Logger:

    @staticmethod
    def log_error(error_message):
        with open("error_log.txt", "a") as file:
            timestamp = datetime.now()
            file.write(f"{timestamp} - {error_message}\n")


# History Class
class History:

    @staticmethod
    def save_history(data):
        with open("history.txt", "a") as file:
            file.write(data + "\n")

    @staticmethod
    def view_history():
        try:
            with open("history.txt", "r") as file:
                data = file.read()

                if data:
                    print("\n----- Calculation History -----")
                    print(data)
                else:
                    print("No history available")

        except FileNotFoundError:
            print("History file not found")


# Calculator Class
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):

        if b == 0:
            raise ZeroDivisionError(
                "Division by zero is not allowed")

        return a / b


# Report Class
class Report:

    @staticmethod
    def generate_report():

        total_calculations = 0
        total_errors = 0
        error_list = []

        try:
            with open("history.txt", "r") as file:
                total_calculations = len(file.readlines())

        except:
            pass

        try:
            with open("error_log.txt", "r") as file:
                errors = file.readlines()

                total_errors = len(errors)

                for line in errors:
                    parts = line.split("-")

                    if len(parts) > 1:
                        error_list.append(parts[-1].strip())

        except:
            pass

        common_error = "No errors"

        if error_list:
            common_error = Counter(
                error_list).most_common(1)[0][0]

        print("\n----- REPORT -----")
        print("Total calculations:", total_calculations)
        print("Total errors:", total_errors)
        print("Most common error:", common_error)


# Main Program
calculator = Calculator()

while True:

    print("\n===== Secure Calculator Pro =====")

    print("1. Perform Calculation")
    print("2. View Calculation History")
    print("3. View Error Report")
    print("4. Exit")

    choice = input("Enter choice: ")

    try:

        if choice == "1":

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

            except ValueError:
                raise InvalidInputError(
                    "Only numeric values allowed")

            print("\nChoose Operation")
            print("1.Addition")
            print("2.Subtraction")
            print("3.Multiplication")
            print("4.Division")

            operation = input(
                "Enter operation choice: ")

            result = None
            expression = ""

            if operation == "1":
                result = calculator.add(
                    num1, num2)

                expression = f"{num1} + {num2} = {result}"

            elif operation == "2":
                result = calculator.subtract(
                    num1, num2)

                expression = f"{num1} - {num2} = {result}"

            elif operation == "3":
                result = calculator.multiply(
                    num1, num2)

                expression = f"{num1} * {num2} = {result}"

            elif operation == "4":
                result = calculator.divide(
                    num1, num2)

                expression = f"{num1} / {num2} = {result}"

            else:
                raise InvalidInputError(
                    "Invalid operation selected")

        elif choice == "2":
            History.view_history()
            continue

        elif choice == "3":
            Report.generate_report()
            continue

        elif choice == "4":
            print("Exiting Program...")
            break

        else:
            raise InvalidInputError(
                "Invalid menu choice")

    except Exception as e:

        print("Error:", e)

        Logger.log_error(str(e))

    else:

        print("\nResult =", result)

        History.save_history(expression)

    finally:

        print("\nOperation completed")