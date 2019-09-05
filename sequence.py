#Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

# Algorithm
#1. Get input for the length of the sequence
#2. Start the sequence with 1
#3. After three numbers in the sequence, the next number is the sum of the three previous numbers.
#4. Stop when the sequence length reaches the input number
#4. Print the sequence in the format 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …


n = int(input("Enter the length of the sequence: ")) # Do not change this line

seq_number = 1

print ("1, 2, 3, ", end='')



