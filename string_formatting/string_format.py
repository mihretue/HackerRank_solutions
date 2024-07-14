def print_formatted(number):
    width = len(bin(number)) - 2  # Calculate the width for formatting
    
    for i in range(1, number + 1):
        # Decimal
        decimal_val = str(i)
        
        # Octal
        if i < 8:
            octal_val = str(i)
        else:    
            result = i // 8
            remainder = i % 8
            if result == 0:
                octal_val = str(remainder)
            else:    
                octal_val = str(result) + str(remainder)
        
        # Hexadecimal
        if i <= 9:
            hex_val = str(i)
        else:
            dic = "123456789ABCDEF"
            result = i // 16
            remainder = i % 16
            if result == 0:
                hex_val = dic[remainder - 1]
            elif remainder == 0:
                hex_val = dic[result - 1] + '0'
            else:
                hex_val = dic[result - 1] + dic[remainder - 1]
        
        # Binary
        binary_number = ""
        temp = i
        if temp == 0:  # Special case for 0
            binary_number = '0'
        
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