Start
        Declarations
                    InputFile employeeData 
                    string name
                    num PayRate
                    //Loop through the file line by line until reaching the end 
                    // Read the fields from the current record
                    READ FirstName, LastName, PayRate, HoursWorked FROM InputFile

                    // Calculate the gross pay
                    GrossPay = PayRate * HoursWorked

                    //Write all five fields into the new updated file
                    WRITE FirstName, LastName, PayRate, HoursWorked, GrossPay TO OutputFile
        END WHILE

        //CLose both files to save progress and release resources
        CLOSE InputFile
        CLOSE OutputFile
STOP
