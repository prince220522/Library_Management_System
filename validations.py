import constants
from datetime import datetime
import re

class Validation:
    def checkUserInput(option):

        # check user input value match our options
        check_input = bool(re.fullmatch(constants.USER_INPUT_CHECK_USING_REGEX, option))
        return check_input

    def checkStudentName(studentName):

        # Student Name validation using regex
        stu_name_check = bool(re.fullmatch(constants.STUDENT_NAME_REGEX, studentName))
        return stu_name_check

    def checkFatherName(fatherName):

        # Father Name validation using regex
        father_name_check = bool(re.fullmatch(constants.FATHER_NAME_REGEX, fatherName))
        return father_name_check

    def checkDateofBirth(studentDOB):

        # Student Date of Birth validation using regex
        # Date of Birth [01/01/1985  --  31/12/2004]
        student_dob_check = bool(re.fullmatch(constants.STUDENT_DOB_REGEX, studentDOB))
        
        isValidDate = True
        try:
            day, month, year = studentDOB.split('/')
            datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False
        return (student_dob_check and isValidDate)

    def checkMobileNo(MobileNo):

        # Student Mobile Number validation using regex
        mobile_no_check = bool(re.fullmatch(constants.STUDENT_MOBILE_NO_REGEX, MobileNo))
        return mobile_no_check

    def checkAdhaarNo(AdhaarNo):

        # Student Adhaar Number validation using regex
        adhaar_no_check = bool(re.fullmatch(constants.STUDENT_ADHAAR_NO_REGEX, AdhaarNo))
        return adhaar_no_check

    def checkSeatNo(reserved_seat_no):

        # Reserved Seat No validation using regex
        seat_no_check = bool(re.fullmatch(constants.RESERVED_SEAT_NO_REGEX, reserved_seat_no))
        return seat_no_check

    def checkUserDecision(decision):

        # User decision (yes|no) using regex
        decision_check = bool(re.fullmatch(constants.USER_DECISION_REGEX, decision))
        return decision_check
