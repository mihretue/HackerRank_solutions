# this is to get the number of levels that the door mat has

N = int(input("please input the Number of rows"))
M = N *3

middle_pattern = '.|.'
normal_pattern = '-'
center_content = 'WELCOME'

# for the upper part of the mat 
for i in range(N//2):
    pattern = middle_pattern * (2 * i + 1)
    upper_part = pattern.center(M, normal_pattern)
    print(upper_part)

# for the middle "Welcome" text
print(center_content.center(M,normal_pattern))

# for the last part of the mat

for i in range( N // 2 -1, -1, -1):
    pattern = middle_pattern * (2 * i + 1)
    lowwer_part = pattern.center(M, normal_pattern)
    print(lowwer_part)