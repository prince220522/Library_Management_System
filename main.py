from tabulate import tabulate
from colorama import init, Fore
init()
import feature
from validations import Validation

# Section : Main Code
feature.clr_scrren()

def main_section():
    print("\nAre You?")
    print(tabulate([["1 - Admin"], ["2 - Student"]], tablefmt="grid"))


while True:
    main_section()
    temp = True
    while temp:
        try:
            option = input("\nOption -> ")

            # using if..else block to check user input value match our options
            if Validation.checkUserInput(option):
                break
            else:
                print(Fore.RED + "You choose invalid option. Choose right one" + Fore.RESET)
        except:
            feature.clr_scrren()
            print(Fore.RED + "Maybe you entered somthing wrong. Choose right one" + Fore.RESET)
            main_section()
            temp = True

    if option == str(1):
        print("Admin section feature will be added soon")
    elif option == str(2):
        print("Student scetion feature will be added soon")
    



