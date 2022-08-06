from functools import reduce

class InputMethods:
    def get_operands():
        operands_string_list = input("Enter operands(space separated) >> ").split()
        operands = list(map(int, operands_string_list))
        return operands

    def menu():
        print("""\nSelect operation...\n
    \t1 -> Summation
    \t2 -> Subtraction
    \t3 -> Multiplication
    \t4 -> Division
    \t5 -> Exponential
    \t6 -> Average
    \t0 -> Back to Home Menu""")
        option = int(input("\t->> "))
        return option

class Operations:
    GO_BACK = 0
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    EXPONENT = 5
    AVERAGE = 6

class BasicOperation:                # Basic operations.
    # functions
    def addition(operands):
        total = 0
        for element in range(len(operands)):
            total += operands[element]
        return total

    def subtract(operands):
        result = operands[0]
        for element in operands[1:]:
            result -= element
        return result

    def multiply(operands):
        mul = 1
        for element in range(0, len(operands)):
            mul *= operands[element]
        return mul

    def division(operands):
        div = 0
        if len(operands) == 2:
            div = operands[0] / operands[1]
        else:
            div = "Invalid input! please give only 2 values for division\n"
        return div


class AlternativeBasicOperation:
    def addition(operands):
        total = reduce(lambda total, num: total + num, operands)
        return total

    def subtract(operands):
        total = reduce(lambda total, num: total + num, operands[1:])
        result = operands[0] - total
        return result
    
    def multiply(operands):
        result = reduce(lambda total, num: total * num, operands)
        return result


class AdditionalOperation:
    def exponential(operands, power):
        result = []
        for element in range(0, len(operands)):
            value = operands[element] ** power
            result.append(value)
        return result

    def average(operands):
        total = AlternativeBasicOperation.addition(operands)
        result = total / len(operands)
        return result


class NumericOperation:
    def __init__(self):
        self.__show_numerical_menu = True

    def numeric_calculation(self):
        while self.__show_numerical_menu:
            operation = InputMethods.menu()

            if operation == Operations.GO_BACK:
                self.__show_numerical_menu = False

            elif operation == Operations.ADD:
                numbers = InputMethods.get_operands()
                print(f"Sum = {BasicOperation.addition(numbers)}")

            elif operation == Operations.SUBTRACT:
                numbers = InputMethods.get_operands()
                print(f"Answer = {BasicOperation.subtract(numbers)}")

            elif operation == Operations.MULTIPLY:
                numbers = InputMethods.get_operands()
                print(f"Answer = {BasicOperation.multiply(numbers)}")

            elif operation == Operations.DIVIDE:
                numbers = InputMethods.get_operands()
                print(f"Answer = {BasicOperation.division(numbers)}")
            
            elif operation == Operations.EXPONENT:
                numbers = InputMethods.get_operands()
                power = int(input("Enter power: "))
                print(f"Answer = {AdditionalOperation.exponential(numbers, power)}")

            elif operation == Operations.AVERAGE:
                numbers = InputMethods.get_operands()
                print(f"Average = {AdditionalOperation.average(numbers)}")
            