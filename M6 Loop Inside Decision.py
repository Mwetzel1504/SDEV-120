Start
    Declarations
        times = integer
    output "Would you like to play the 'Hello' game? (yes/no): "
    Input userResponse

    IF userResponse = "yes" or "Yes" or "YES" THEN
        Output "How many times should 'Hello' be printed? "
        Input times
    IF times IS NOT a positive integer THEN
        Output "Inaccurate input. Please enter a positive number. "
        TERMINATE PROGRSM
    ENDIF

    FOR counter FROM 1 TO times DO
        Output "Hello"


    ELSE IF userResponse = 'no" or "NO" or "No" THEN
        Ouput "Alright, thank you!"
        TERMINATE PROGRAM
    ELSE
        Ouput "Inaccurate response. Please enter 'yes' or 'no'."
    ENDIF
STOP
