#Maximum number

#1. Prompt the user for and input
#2. Prompt for another input
#3. Compare the inputs and store the maximum input
#4. Repeat steps 2 and 3
#5. Stop if the input is negative
#6. Print the maximum input


num_int = int(input("Input a number: "))

max_int = 0

#Continue if input is a positive number
if num_int > 0 :
    
    #Repeat the while loop while input is a positive number
    while num_int > 0 :
        
        #Switch out the max_input number when a greater number is input
        if num_int > max_int :
            max_int = num_int

        num_int = int(input("Input a number: "))

            
    
    print("The maximum is", max_int)
