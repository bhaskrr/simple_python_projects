# function to generate sum of the digits of a number
def sd(n):
    s = 0
    if n == 0:
        return 0
    else:
        s += n % 10 + sd(n//10)
    return s


# function to check if the sum is greater than 9
def checksum(n):
    s1 = 0
    if n > 9:
        s1 += n % 10 + sd(n//10)
        return s1
    elif n < 9:
        return n


# getting input from the user and calling the sd() and checksum() functions
num = int(input("Enter the number to calculate super digit: "))
s2 = sd(num)
print(checksum(s2))
