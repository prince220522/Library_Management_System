Query_1_1_1 = "INSERT INTO SeatManagement (SeatNo) VALUES(?)"

Query_1_1_2 = "SELECT count(SeatNo) FROM SeatManagement WHERE RegId IS NULL"

Query_1_1_3 = "INSERT INTO SignUpTable (StudentName, FatherName, DateOfBirth, MobileNo, AdhaarNo, DateOfJoining) VALUES (?, ?, ?, ?, ?, ?)"

Query_1_1_4 = "SELECT SeatNo FROM SeatManagement WHERE RegId IS NULL LIMIT 1"

Query_1_1_5 = "UPDATE SeatManagement SET RegId = {} WHERE SeatNo = (SELECT SeatNo FROM SeatManagement WHERE RegId IS NULL LIMIT 1)"

Query_1_1_6 = "SELECT RegId, SeatNo, StudentName, DateOfJoining FROM SignUpTable INNER JOIN SeatManagement ON SignUpTable.MobileNo = SeatManagement.RegId WHERE SeatNo = {}"