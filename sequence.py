n = int(input("Enter the length of the sequence: ")) # Do not change this line
#Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

# Algorithm
#1. Get input for the length of the sequence
#2. Start the sequence with 1
#3. After three numbers in the sequence, the next number is the sum of the three previous numbers.
#4. Stop when the sequence length reaches the input number
#4. Print the sequence


n1 = 1
n2 = 2
n3 = 3


for i in range (1, n+1) :

    if i == 1 :
        print(n1)

    elif i == 2 :
        print(n2)

    elif i == 3 :
        print(n3)
    
    else :
        next_number = n1+n2+n3
        print(next_number)
        n1 = n2
        n2 = n3
        n3 = next_number




