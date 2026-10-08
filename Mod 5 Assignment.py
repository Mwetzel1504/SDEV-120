
BEGIN_PROGRAM

DECLARE numbers_list AS empty list
DECLARE TOTAL_NUMBERS AS INTEGER = 15
DECLARE user_input AS INTEGER

    FOR i FROM 1 TO TOTAL_NUMBERS DO
        REPEAT
            DISPLAY "Enter integer #" + i + ": "
            READ user_input
            IF user_input is an integer THEN
                APPEND user_input TO numbers_list
                EXIT REPEAT
            ELSE
                DISPLAY "Invalid input. Please enter an integer."
            ENDIF
        UNTIL valid integer entered
    ENDFOR

    FOR EACH number IN numbers_list DO
        IF (number MOD 2) == 0 THEN
            DISPLAY number + " is even"
        ELSE
            DISPLAY number + " is odd"
        ENDIF
    ENDFOR

END PROGRAM

