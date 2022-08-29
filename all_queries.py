INSERT_SEAT_NO_INTO_SEAT_MANAGEMENT = "INSERT INTO SeatManagement (SeatNo) VALUES(?)"

COUNT_UNRESERVED_SEATS = "SELECT count(SeatNo) FROM SeatManagement WHERE RegId IS NULL"

INSERT_STUDENT_INFO = "INSERT INTO SignUpTable (StudentName, FatherName, DateOfBirth, MobileNo, AdhaarNo, DateOfJoining) VALUES (?, ?, ?, ?, ?, ?)"

SELECT_ONE_REGID_FROM_SEATMANGEMENT = "SELECT SeatNo FROM SeatManagement WHERE RegId IS NULL LIMIT 1"

RESERVED_SEAT_FOR_NEW_STUDENT = "UPDATE SeatManagement SET RegId = {} WHERE SeatNo = (SELECT SeatNo FROM SeatManagement WHERE RegId IS NULL LIMIT 1)"

SHOW_NEW_STUDENT_INFO = "SELECT RegId, SeatNo, StudentName, DateOfJoining FROM SignUpTable INNER JOIN SeatManagement ON SignUpTable.MobileNo = SeatManagement.RegId WHERE SeatNo = {}"

RESERVED_SEATS_LIST = "SELECT SeatNo FROM SeatManagement WHERE RegId IS NOT NULL"

SHOW_STUDENT_INFO_FOR_CONFIRMATION = "SELECT SeatNo, RegId, StudentName, FatherName, DateOfJoining, DateOfLeaving FROM SignUpTable INNER JOIN SeatManagement ON SignUpTable.MobileNo = SeatManagement.RegId WHERE SeatNo = {}"

REGID_FOR_STUDENT_EXIT = "SELECT RegId FROM SeatManagement WHERE SeatNo = {}"

UPDATE_SEAT_NO_REGID = "UPDATE SeatManagement SET RegId = NULL WHERE SeatNo = {}"

INSERT_DATE_OF_LEAVING_INTO_SIGNUPTABLE = "UPDATE SignUpTable SET DateOfLeaving = ? WHERE MobileNo = ?"

COUNT_NEW_JOINING_STUDENT = "SELECT count(StudentName) FROM SignUpTable WHERE DateOfJoining = '{}'"

DISPLAY_NEW_JOINING_STUDENT = "SELECT * FROM SignUpTable WHERE DateOfJoining = '{}'"

COUNT_STUDENT_LEFT_THE_LIBRARY = "SELECT count(StudentName) FROM SignUpTable WHERE DateOfLeaving = '{}'"

DISPLAY_LEAVING_STUDENT_DATA = "SELECT * FROM SignUpTable WHERE DateOfLeaving = '{}'"

EXISTS_REG_ID_LIST = "SELECT RegId FROM SeatManagement WHERE RegId IS NOT NULL"

CHECK_REG_ID_IN_STUDENT_ATTENDANCE_TABLE = "SELECT RegId FROM StudentAttendance WHERE CurrentDate = '{}'"

INSERT_STUDENT_ATTENDANCE = "INSERT INTO StudentAttendance (RegId, InTime, CurrentDate) VALUES (?, ?, ?)"

DISPLAY_STUDENT_ATTENDANCE = "SELECT SeatManagement.RegId, SeatManagement.SeatNo, SignUpTable.StudentName, StudentAttendance.InTime FROM SignUpTable INNER JOIN SeatManagement ON SignUpTable.MobileNo = SeatManagement.RegId INNER JOIN StudentAttendance ON SignUpTable.MobileNo = StudentAttendance.RegId WHERE StudentAttendance.RegId = {} AND StudentAttendance.CurrentDate = '{}'"

STUDENT_ATTENDANCE_IN_TIME = "SELECT InTime FROM StudentAttendance WHERE RegId = {}"