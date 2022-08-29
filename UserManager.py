from validations import Validation
from curDate_curTime import curDate
from colorama import init, Fore
init()

class UserManager:
    def SignUp():
        
        # Section : Admin/Sign Up code
        print("~" * 41)
        print("|"+"\tNew Student (Sign Up)\t\t"+"|")
        print("~" * 41)
        print()

        # Section (1): Student Full Name
        while True:
            student_name = input("  Student's Name\t:   ")
            
            # using if..else block to check Student Name valid or not
            if Validation.checkStudentName(student_name):
                break
            else:
                print(Fore.RED + "\n  Invalid Student's Name. Try again!\n" + Fore.RESET)

        # Section (2): Student Father's Name
        while True:
            father_name = input("  Father's Name\t\t:   ")
        
            # using if..else block to check Student Father Name is valid or not 
            if Validation.checkFatherName(father_name):
                break
            else:
                print(Fore.RED + "\n  Invalid Father's Name. Try Again!\n" + Fore.RESET)

        # Section (3): Student Date of Birth / Format : DD/MM/YYYY / [01/01/1985 to 31/12/2004]
        while True:
            student_dob = input("  DOB [dd/mm/yyyy]\t:   ")
            
            # using if..else block to check DOB is valid or not
            if Validation.checkDateofBirth(student_dob):
                break
            else:
                print(Fore.RED + "\n  DOB should be between [01/01/1985 to 31/12/2004]. Try Again!\n" + Fore.RESET)

        # Section (4): Student Mobile Number
        while True:
            mobile_no = input("  Mobile No.\t\t:   ")
            
            # using if..else block to check Student Mobile Number is valid or not
            if Validation.checkMobileNo(mobile_no):
                break
            else:
                print(Fore.RED + "\n  Invalid Mobile No. Try Again!\n" + Fore.RESET)

        # Section (5): Student Adhaar Card Number
        while True:
            adhaar_no = input("  Adhaar No.\t\t:   ")
            
            # using if..else block to check Student Adhaar Number is valid or not
            if Validation.checkAdhaarNo(adhaar_no):
                break
            else:
                print(Fore.RED + "\n  You entered invalid adhaar no. Try Again!\n" + Fore.RESET)

        current_date = curDate
        
        return (student_name, father_name, student_dob, mobile_no, adhaar_no, current_date)

    def UpdateSeatNo():

        # Section : Admin/Update Seat No code
        print("\nWhich seat no do you want to update?")
        while True:
            try:
                reserved_seat_no = input("Enter reserved seat no ->   ")

                # using if...else block to check seat no valid or not
                if Validation.checkSeatNo(reserved_seat_no):
                    break
                else:
                    print(Fore.RED + "You entered invalid seat no. Try Again!" + Fore.RESET)

            except Exception as error:
                print(error)

        return reserved_seat_no

    def StudentAttendance():

        # Section : Student/ Student_Attendance
        while True:
            try:
                student_reg_id = input("\nEnter your RegId  -->  ")

                # if user enter Q means (Quit) then you will be redirected in main scetion 
                if student_reg_id != "Q":
                    if Validation.checkMobileNo(student_reg_id):
                        break
                    else:
                        print(Fore.RED + "You entered invalid RegId. Try Again!" + Fore.RESET)
                else:
                    return student_reg_id

            except Exception as error:
                print(error)

        return student_reg_id



 