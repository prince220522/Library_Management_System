from time import sleep
from tabulate import tabulate
import sqlite3
from datetime import datetime
from colorama import init, Fore
init()
from UserManager import UserManager
import feature
from validations import Validation
import all_queries

# Section : Main Code
feature.clr_scrren()
def main_section():
    print("\nAre You?")
    print(tabulate([["1", "Admin"], ["2", "Student"]], tablefmt="grid"))

curDate = datetime.today().strftime("%d/%m/%Y")

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
        feature.clr_scrren()
        while True:
            print(tabulate([["1", "Sign Up"], ["2", "Update Seat No"], ["6", "Log Out"]], tablefmt="grid"))
            while True:
                try:
                    admin_option = int(input("Option -> "))
                    break
                except:
                    print(Fore.RED + "Maybe you entered something wrong. Choose right one" + Fore.RESET)

            if admin_option == 1:
                feature.clr_scrren()
                print("\nFirst we will be checking unreserved seats", end="")
                for _ in range(3):
                    sleep(1.00)
                    print(".", end="")

                try:
                    # make connection to SQLite database
                    connection = sqlite3.connect("library.db")

                    cursor = connection.cursor()
                    
                    # cursor.execute("DROP TABLE IF EXISTS SeatManagement")
                    # Table_1 = """CREATE TABLE SeatManagement (
                    #                 SeatNo INT NOT NULL,
                    #                 RegId TEXT,
                    #                 PRIMARY KEY (SeatNo),
                    #                 FOREIGN KEY(RegId) REFERENCES SignUpTable(MobileNo)
                    #             );"""

                    # cursor.execute(Table_1)

                    # insert 20 rows in SeatManagement
                    # for i in range(1, 21):
                    #     cursor.execute(all_queries.Query_1_1_1, (i,))

                    cursor.execute(all_queries.Query_1_1_2)
                    for i in cursor.fetchall():
                        for j in i:
                            count_unreserved_seats = j

                except Exception as error:
                    print(error)

                finally:
                    # Commit your changes in the database    
                    connection.commit()

                    # Closing the connection
                    connection.close()

                    print()
                    print("\nUnreserved Seats  =  ", count_unreserved_seats)
                    feature.clr_scrren()

                    if count_unreserved_seats != 0:
                        student_signup_details = UserManager.SignUp()

                        try:
                            # make connection to SQLite database
                            connection = sqlite3.connect("library.db")

                            cursor = connection.cursor()
                            
                            # cursor.execute("DROP TABLE IF EXISTS SignUpTable")
                            # Table_2 = """CREATE TABLE SignUpTable (
                            #                 StudentName VARCHAR(100) NOT NULL,
                            #                 FatherName VARCHAR(100) NOT NULL,
                            #                 DateOfBirth TEXT NOT NULL,
                            #                 MobileNo TEXT NOT NULL,
                            #                 AdhaarNo TEXT NOT NULL,
                            #                 DateOfJoining TEXT NOT NULL,
                            #                 DateOfLeaving TEXT,
                            #                 PRIMARY KEY (MobileNo)
                            #             );"""

                            # cursor.execute(Table_2)

                            cursor.execute(all_queries.Query_1_1_3, student_signup_details)

                            cursor.execute(all_queries.Query_1_1_4)
                            for i in cursor.fetchall():
                                for j in i:
                                    book_seat_no = j

                            cursor.execute(all_queries.Query_1_1_5.format(student_signup_details[3]))
                            
                            sleep(2.00)
                            print(Fore.GREEN + "\nThank you for filling out our sign up form. We are glad that you joined us.\n" + Fore.RESET)
                            sleep(2.00)

                            cursor.execute(all_queries.Query_1_1_6.format(book_seat_no))

                            print(tabulate(cursor.fetchall(), headers=["Reg Id", "Seat No", "Student Name", "Date of Joining"], tablefmt="grid", colalign=("center", "center", "center", "center")))
                            print("\nYou will be redirected automatically in admin section", end="")
                            for _ in range(5, 0, -1):
                                sleep(1.00)
                                print(".", end="")

                        except Exception as error:
                            print(error)

                        finally:
                            # Commit your changes in the database    
                            connection.commit()

                            # Closing the connection
                            connection.close()

                        feature.clr_scrren()

                    else:
                        print("We don't have any unreserved seats\nPlease, try after some time\nThank You...")
                        feature.clr_scrren()


            elif admin_option == 2:
                feature.clr_scrren()
                reserved_seatNo = int(UserManager.UpdateSeatNo())
                print()
                try:
                    # make connection to SQLite database
                    connection = sqlite3.connect("library.db")
                    cursor = connection.cursor()

                    cursor.execute(all_queries.Query_1_2_1)
                    
                    if reserved_seatNo in [j for i in cursor.fetchall() for j in i]:

                        cursor.execute(all_queries.Query_1_2_2.format(reserved_seatNo))
                        print(tabulate(cursor.fetchall(), headers=["Seat No", "Reg Id", "Student Name", "Father Name", "Date of Joining", "Date of Leaving"], tablefmt="grid", colalign=("center", "center", "center", "center", "center", "center")))
                        
                        while True:
                            decision = input("\nDo you want to update seat no (Yes/No)\t:\t").lower()

                            if Validation.checkUserDecision(decision):
                                break
                            else:
                                print(Fore.RED + "\nYou entered something wrong. Try Again!\n" + Fore.RESET)

                        if decision == "yes":

                            cursor.execute(all_queries.Query_1_2_3.format(reserved_seatNo))
                            for i in cursor.fetchall():
                                for j in i:
                                    StudentRegId = j

                            cursor.execute(all_queries.Query_1_2_4.format(reserved_seatNo))
                            cursor.execute(all_queries.Query_1_2_5, (curDate, StudentRegId))

                            sleep(2.00)
                            print(Fore.GREEN + "\nThanks for confirmation." + Fore.RESET)
                            feature.clr_scrren()
                        else:
                            sleep(2.00)
                            print(Fore.GREEN + "\nThanks for confirmation." + Fore.RESET)
                            feature.clr_scrren()

                    else:
                        sleep(2.00)
                        print(Fore.RED + "Your seat number don't exist our database" + Fore.RESET)
                        feature.clr_scrren()

                except Exception as error:
                    print(error)

                finally:
                    # Commit your changes in the database    
                    connection.commit()

                    # Closing the connection
                    connection.close()
                    
            elif admin_option == 6:
                sleep(2.00)
                print(Fore.GREEN + "\nYou have been logged out " + Fore.RESET, end="")
                for _ in range(3):
                    sleep(1.00)
                    print(Fore.GREEN + "." + Fore.RESET, end="")
                feature.clr_scrren()
                break
            else:
                print(Fore.RED + "You choose invalid option. Choose right one" + Fore.RESET)

    elif option == str(2):
        print("Student scetion feature will be added soon")
        feature.clr_scrren()
    



