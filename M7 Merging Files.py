Start
    //OPEN Input and Output files
    OPEN "magic.dat" FOR INPUT AS MagicFile
    OPEN "super.dat" FOR INPUT AS SuperFile
    OPEN "merged_cleaning.dat" FOR PUTPUT AS OutputFile

    //Priming reads: Get the first record from each file
    IF NOT E0F 9MagicFIle) THEN
        READ MagicNum, MagicName, MagicLoc, MagicSqFt, FROM MagicFile
    ENDIF


    IF NOT E0F (SuperFile) THEN
        READ SuperNum, SuperName, SuperLoc, SuperSqFt, FROM SuperFile
    ENDIF

    //Main loop: Merge files while records exist in both files
    WHILE NOT E0F (MagicFile) AND NOT E0F 9SuperFile)
        IF MagicNum < SuperNum THEN
            WRITE MagicNum, MagicName, MagicLOc, MagicSqFt TO OutputFile
            IF NOT E0F (MagicFile) THEN
                READ MagicNum, MagicName, MagicLOc, MagicSqFt FROM MagicFile
            ENDIF
        ELSE
            WRITE SuperNum, SuperName, SuoerLoc, SuperSqFt TO OutputFile
            IF NOT E0F (SuperFile) THEN
                READ SuperNum, SuperName, SuperLoc, SuperSqFt, FROM SuperFile
            ENDIF
        ENDIF
    END WHILE



    //CLean-up loop 1: Write any remaining records left in MagicFile
    WHILE NOT E0F (MagicFile)
        WRITE  MagicNum, MagicName, MagicLOc, MagicSqFt TO OutputFile
        IF NOT E0F (MagicFile) THEN
            READ  MagicNum, MagicName, MagicLOc, MagicSqFt  FROM MagicFile
        ENDIF
    END WHILE


     //CLean-up loop 1: Write any remaining records left in SuperFile
    WHILE NOT E0F (SuperFile)
        WRITE SuperNum, SuperName, SuperLoc, SuperSqFt TO OutputFile
        IF NOT E0F (SuperFile) THEN
            IF NOT E0F (SuperFile) THEN
                READ SuperNum, SuperName, SuperLoc, SuperSqFt, FROM SuperFile
            ENDIF
        END WHILE

        //Close files
        CLOSE MagicFile
        CLOSE SuperFile
        CLOSE OutputFile
Stop
        
