from mensuration import Mensuration
from numerical import NumericOperation


class MainMenu:
    def main_menu():
        print("""\nWelcome to 'MATH_UTILS'. Please select Operation Category...\n
\t1 -> Basic Operations
\t2 -> Mensuration 
\t0 -> Exit App""")
        selection = int(input("--> "))
        return selection


class Options:
    GO_BACK = 0
    NUMERICAL = 1
    MENSURATION = 2
    
    
class MainFunction:
    def __init__(self):
        self.__show_main_menu = True

    def home_menu(self):
        while self.__show_main_menu:
            option = MainMenu.main_menu()

            if option == Options.GO_BACK:
                self.__show_main_menu = False

            elif option == Options.NUMERICAL:
                n = NumericOperation()
                n.numeric_calculation()

            elif option == Options.MENSURATION:
                try:
                    m = Mensuration()
                    m.perform_operation()
                except TypeError:
                    print("WARNING ! Please give all required values only!!")


if __name__ == "__main__":
    f = MainFunction()
    f.home_menu()
