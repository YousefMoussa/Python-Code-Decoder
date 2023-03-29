import numpy as np

## Rule 1: This part of the code asks for an input number from the user which
## is the code the user wants to test. It then tests the length of the code
## and if it is not nine digits, it terminates the program and produces the 
## error message 'Decoy Message: Not a nine-digit number.'. If the code is 
## nine digits it turns into an array of integers.
code = input('Please enter a code to break: ')
if len(code) != 9:
   print("Decoy Message: Not a nine-digit number.")
else: 
    code = np.array(list(code),dtype=int)
    ## Rule 2: Next test2 becomes the sum of all of the numbers that make up
    ## the array 'code'. If the remainder after the number is divided by 2 is 
    ## zero, then the error message 'Decoy Message: Sum is even.' is printed and the
    ## program terminated. Otherwise, the program continues to rule 3.
    test2 = int(np.sum(code))
    if (test2 % 2) == 0:
        print("Decoy Message: Sum is even.")
    else:
        ## Rule 3: Here, the third and second number in the array are multiplied
        ## and the first number is subtracted afterward. This value is labeled 
        ## 'day_num' and if the number is not greater than or equal to one or
        ## less than or equal to seven, the program is terminated. The error 
        ## message 'Decoy Message: Invalid rescue day.' is then produced.
        ## If not, then the program checks which integer the 'day_num' is and 
        ## matches it to the appropriate day, with 'day' now equal to the day
        ## of the extraction.
        day_num = ((code[2]*code[1])-code[0])
        if (day_num <1) or (day_num >7): 
            print ("Decoy Message: Invalid rescue day.")
        else:
            if (day_num == 1):
                day = ("Monday")
            if (day_num == 2):
                day = ("Tuesday")
            if (day_num == 3):
                day = ("Wednesday")
            if (day_num == 4):
                day = ("Thursday")
            if (day_num == 5):
                day = ("Friday")
            if (day_num == 6):
                day = ("Saturday")
            if (day_num == 7):
                day = ("Sunday")
            ## Rule 4: The final rule takes the 3rd number in the 'code' array
            ## and puts it to the power of the 2nd number in that array.
            ## If the number is divisible by three with a remainder of zero
            ## than the 6th number is subtracted from the 5th in the array.
            ## and if the number is not divisible by three, the 5th 
            ## number is subtracted from the 6th number. This value is called
            ## 'place_num' and if it is less than one or greater than seven,
            ## the code terminates and displays 'Decoy Message: Invalid 
            ## rendezvous point.'. If not, then the value 'place_num' is then 
            ## connected to the place it represents and a final message is produced
            ## representing the day and rendezvous location.
            temp_num = (code[2]**code[1])
            if (temp_num % 3) == 0:
                place_num = (code[5]-code[4])
            else:
                place_num = (code[4]-code[5])
            if (place_num <1) or (place_num >7):
                print("Decoy Message: Invalid rendezvous point.")
            else:
                if (place_num == 1):
                    place = ("bridge")
                if (place_num == 2):
                    place = ("library")
                if (place_num == 3):
                    place = ("river crossing")
                if (place_num == 4):
                    place = ("airport")
                if (place_num == 5):
                    place = ("bus terminal")
                if (place_num == 6):
                    place = ("hospital")
                if (place_num == 7):
                    place = ("railway station")
                print("Rescued on", day, ("at the"), place)
            