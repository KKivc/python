# total=0
# i=1
# while i < 100:
#     if i % 2 == 0:
#         total += i

#     i += 1
    
# else:
#     print(total)
#     print("Loop is done")


# a=int(input('Enter a number: '))
# for i in range(1, a+1):
    
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()


# a_id = 'admin'
# a_pwd = '666888'
# b_id = 'ii'
# b_pwd = '123456'
# c_id = 'uuu'
# c_pwd = '888888'

# while True:
#     id = input('Enter your id: ')
#     pwd = input('Enter your password: ')
#     if (id == a_id and pwd == a_pwd) or (id == b_id and pwd == b_pwd) or (id == c_id and pwd == c_pwd):
#         print('Login successful!')
#         break
#     else:
#         print('Login failed, please try again.')


# a = input('Enter string: ')

# if len(a) == 10:
#     i = a[-1:-11:-1]
#     print(i.upper())

# else:
#     print('String length is not 10.')


stu = [
	['1', 'ii', 90,44,50],
	['2', 'uu', 86,38,78],
	['3','oo', 77,89,59]
]

chinese = [s[2] for s in stu]
print(f'chinese = {chinese}')