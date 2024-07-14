def print_formatted(number):
    # Calculate the width for formatting
    width = len(bin(number)) - 2
    
    for i in range(1, number + 1):
        # Decimal
        decimal_val = str(i)
        
        # Octal
        result = ""
        n = i
        while n > 0:
            result = str(n % 8) + result
            n = n // 8
        octal_val = result
        
        # Hexadecimal
        dic = "0123456789ABCDEF"
        result = ""
        n = i
        while n > 0:
            result = dic[n % 16] + result
            n = n // 16
        hex_val = result
        
        # Binary
        binary_number = ""
        temp = i
        while temp > 0:
            if temp % 2 == 0:
                binary_number = '0' + binary_number
            else:
                binary_number = '1' + binary_number
            temp = temp // 2
        
        # Print all values formatted
        print(f"{decimal_val:>{width}} {octal_val:>{width}} {hex_val:>{width}} {binary_number:>{width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
