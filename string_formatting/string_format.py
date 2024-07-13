# Given an integer, , print the following values for each integer  from  to :

#Decimal
#Octal
#Hexadecimal (capitalized)
#Binary
def print_formatted(number):
    # Binary
    for i in range(1, number + 1):
        print(i)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)