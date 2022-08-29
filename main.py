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

def display_message():
    sleep(2.00)
    print(Fore.GREEN + "\nYou will be redirected automatically in admin section" + Fore.RESET, end="")
    for _ in range(5, 0, -1):
        sleep(1.00)
        print(Fore.GREEN + "." + Fore.RESET, end="")

curDate = datetime.today().strftime("%d/%m/%Y")
curTime = datetime.today().strftime("%H:%M:%S")

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
            print(tabulate([["1", "Sign Up"], ["2", "Update Seat No"], ["3", "Joining Student"], ["4", "Leaving Student"], ["5", "Check Attendance"], ["6", "Log Out"]], tablefmt="grid"))
            while True:
                try:
                    admin_option = int(input("Option -> "))
                    break
                except:
                    print(Fore.RED + "Maybe you entered something wrong. Choose right one" + Fore.RESET)

            if admin_option == 1:

                # Section : Admin/Sign Up 
                feature.clr_scrren()
                print("\nFirst we will be checking unreserved seats" , end="")
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
                    #     cursor.execute(all_queries.INSERT_SEAT_NO_INTO_SEAT_MANAGEMENT, (i,))

                    cursor.execute(all_queries.COUNT_UNRESERVED_SEATS)
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

                            cursor.execute(all_queries.INSERT_STUDENT_INFO, student_signup_details)

                            cursor.execute(all_queries.SELECT_ONE_REGID_FROM_SEATMANGEMENT)
                            for i in cursor.fetchall():
                                for j in i:
                                    book_seat_no = j

                            cursor.execute(all_queries.RESERVED_SEAT_FOR_NEW_STUDENT.format(student_signup_details[3]))
                            
                            sleep(2.00)
                            print(Fore.GREEN + "\nThank you for filling out our sign up form. We are glad that you joined us.\n" + Fore.RESET)
                            sleep(2.00)

                            cursor.execute(all_queries.SHOW_NEW_STUDENT_INFO.format(book_seat_no))

                            print(tabulate(cursor.fetchall(), headers=["Reg Id", "Seat No", "Student Name", "Date of Joining"], tablefmt="grid", colalign=("center", "center", "center", "center")))
                            display_message()

                        except Exception as error:
                            print(error)

                        finally:
                            # Commit your changes in the database    
                            connection.commit()

                            # Closing the connection
                            connection.close()

                        feature.clr_scrren()

                    else:
                        sleep(2.00)
                        print("We don't have any unreserved seats\nPlease, try after some time\nThank You...")
                        feature.clr_scrren()


            elif admin_option == 2:

                # Section : Admin/Update Seat No 
                feature.clr_scrren()
                reserved_seatNo = int(UserManager.UpdateSeatNo())
                print()
                try:
                    # make connection to SQLite database
                    connection = sqlite3.connect("library.db")
                    cursor = connection.cursor()

                    cursor.execute(all_queries.RESERVED_SEATS_LIST)
                    
                    if reserved_seatNo in [j for i in cursor.fetchall() for j in i]:

                        cursor.execute(all_queries.SHOW_STUDENT_INFO_FOR_CONFIRMATION.format(reserved_seatNo))
                        print(tabulate(cursor.fetchall(), headers=["Seat No", "Reg Id", "Student Name", "Father Name", "Date of Joining", "Date of Leaving"], tablefmt="grid", colalign=("center", "center", "center", "center", "center", "center")))
                        
                        while True:
                            decision = input("\nDo you want to update seat no - {} (Yes/No)\t:\t".format(reserved_seatNo)).lower()

                            if Validation.checkUserDecision(decision):
                                break
                            else:
                                print(Fore.RED + "\nYou entered something wrong. Try Again!\n" + Fore.RESET)

                        if decision == "yes":

                            cursor.execute(all_queries.REGID_FOR_STUDENT_EXIT.format(reserved_seatNo))
                            for i in cursor.fetchall():
                                for j in i:
                                    StudentRegId = j

                            cursor.execute(all_queries.UPDATE_SEAT_NO_REGID.format(reserved_seatNo))
                            cursor.execute(all_queries.INSERT_DATE_OF_LEAVING_INTO_SIGNUPTABLE, (curDate, StudentRegId))

                            sleep(2.00)
                            print(Fore.GREEN + "\nThanks for confirmation." + Fore.RESET)
                            feature.clr_scrren()
                        else:
                            sleep(2.00)
                            print(Fore.GREEN + "\nThanks for confirmation." + Fore.RESET)
                            feature.clr_scrren()

                    else:
                        sleep(2.00)
                        print(Fore.RED + "Your seat number don't exists our library system." + Fore.RESET)
                        sleep(2.00)
                        feature.clr_scrren()

                except Exception as error:
                    print(error)

                finally:
                    # Commit your changes in the database    
                    connection.commit()

                    # Closing the connection
                    connection.close()

            elif admin_option == 3:

                # Section : Admin/New Joining Students the library
                feature.clr_scrren()
                try:
                    # make connection to SQLite database
                    connection = sqlite3.connect("library.db")
                    cursor = connection.cursor()
                    
                    cursor.execute(all_queries.COUNT_NEW_JOINING_STUDENT.format(curDate))
                    for i in cursor.fetchall():
                        for j in i:
                            count_new_joining_student = j
                    
                    if count_new_joining_student != 0:
                        cursor.execute(all_queries.DISPLAY_NEW_JOINING_STUDENT.format(curDate))
                        sleep(2.00)
                        print(tabulate(cursor.fetchall(), headers=["Student Name", "Father Name", "DOB", "Mobile No", "Adhaar No", "Date of Joining", "Date of Leaving"], tablefmt="grid", colalign=("center","center","center","center","center","center","center")))
                        sleep(2.00)
                        print(Fore.GREEN + "\n{}  -->  {} students have joined library".format(curDate, count_new_joining_student) + Fore.RESET)
                        display_message()
                        feature.clr_scrren()
                    else:
                        sleep(2.00)
                        print(Fore.RED + "\n{}  -->  No one have joined the library.".format(curDate) + Fore.RESET)
                        sleep(2.00)
                        feature.clr_scrren()

                except Exception as error:
                    print(error)

                finally:
                    # Commit your changes in the database    
                    connection.commit()

                    # Closing the connection
                    connection.close()

            elif admin_option == 4:

                # Section : Admin/Leaving Students the Library 
                feature.clr_scrren()
                try:
                    # make connection to SQLite database
                    connection = sqlite3.connect("library.db")
                    cursor = connection.cursor()
                    
                    cursor.execute(all_queries.COUNT_STUDENT_LEFT_THE_LIBRARY.format(curDate))
                    for i in cursor.fetchall():
                        for j in i:
                            count_student_left_library = j
                    
                    if count_student_left_library != 0:
                        cursor.execute(all_queries.DISPLAY_LEAVING_STUDENT_DATA.format(curDate))
                        sleep(2.00)
                        print(tabulate(cursor.fetchall(), headers=["Student Name", "Father Name", "DOB", "Mobile No", "Adhaar No", "Date of Joining", "Date of Leaving"], tablefmt="grid", colalign=("center","center","center","center","center","center","center")))
                        sleep(2.00)
                        print(Fore.GREEN + "\n{}  -->  {} students have left the library".format(curDate, count_student_left_library) + Fore.RESET)
                        display_message()
                        feature.clr_scrren()
                    else:
                        sleep(2.00)
                        print(Fore.RED + "\n{}  -->  No one have left the library".format(curDate) + Fore.RESET)
                        display_message()
                        feature.clr_scrren()

                except Exception as error:
                    print(error)

                finally:
                    # Commit your changes in the database    
                    connection.commit()

                    # Closing the connection
                    connection.close()

            elif admin_option == 5:

                # Section : Admin/check student attendance
                feature.clr_scrren()
                try:
                    # make connection to SQLite database
                    connection = sqlite3.connect("library.db")
                    cursor = connection.cursor()

                    cursor.execute(all_queries.CURRENT_DATE_STUDENTS_ATTEDANCE.format(curDate))
                
                    sleep(2.00)
                    print(tabulate(cursor.fetchall(), headers=["Seat No", "Reg ID", "In Time", "Date"], tablefmt="grid", colalign=("center", "center", "center", "center")))
                    display_message()
     
                except Exception as error:
                    print(error)

                finally:
                    # Commit your changes in the database    
                    connection.commit()

                    # Closing the connection
                    connection.close()
                feature.clr_scrren()

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
        
        # Section : Students Attendance
        feature.clr_scrren()
        while True:
            student_RegId = UserManager.StudentAttendance()

            # if user enter Q means (Quit) then you will be redirected automatically in main scetion.
            if student_RegId == "Q":
                feature.clr_scrren()
                break
            try:
                # make connection to SQLite database
                connection = sqlite3.connect("library.db")
                cursor = connection.cursor()

                # CREATE_STUDENT_ATTENDANCE_RECORDS_TABLE = """CREATE TABLE StudentAttendance (
                #                                         RegId TEXT NOT NULL,
                #                                         InTime TEXT,
                #                                         CurrentDate TEXT,
                #                                         FOREIGN KEY(RegId) REFERENCES SignUpTable(MobileNo)
                #                                     );"""

                # cursor.execute(CREATE_STUDENT_ATTENDANCE_RECORDS_TABLE)

                cursor.execute(all_queries.EXISTS_REG_ID_LIST)

                if student_RegId in [j for i in cursor.fetchall() for j in i]:
                    
                    cursor.execute(all_queries.CHECK_REG_ID_IN_STUDENT_ATTENDANCE_TABLE.format(curDate))
                    if student_RegId not in [j for i in cursor.fetchall() for j in i]:

                        cursor.execute(all_queries.INSERT_STUDENT_ATTENDANCE, (student_RegId, curTime, curDate))
                        cursor.execute(all_queries.DISPLAY_STUDENT_ATTENDANCE.format(student_RegId, curDate))
                        sleep(2.00)
                        print(tabulate(cursor.fetchall(), headers=["Reg ID", "Seat No", "Student Name", "In Time"], tablefmt="grid", colalign=("center","center","center","center")))
                        sleep(2.00)
                    else:
                        cursor.execute(all_queries.STUDENT_ATTENDANCE_IN_TIME.format(student_RegId))
                        for i in cursor.fetchall():
                            for j in i:
                                student_library_inTime = j
                        sleep(2.00)
                        print(Fore.RED + "\nYour attendance captured at {}, {}".format(student_library_inTime, curDate) + Fore.RESET)
                        sleep(2.00)

                else:
                    sleep(2.00)
                    print(Fore.RED + "\nThis RegId don't exists our library system." + Fore.RESET)

                feature.clr_scrren()

            except Exception as error:
                print(error)

            finally:
                # Commit your changes in the database    
                connection.commit()

                # Closing the connection
                connection.close()



