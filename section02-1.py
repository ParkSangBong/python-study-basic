# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본출력

print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Separator 옵션 사용

print('T', 'E', 'S', 'T', sep = '')
print('2021', '01', '28', sep = '-')
print('niceman', 'google.com', sep = '@')

# end 옵션 사용

print('Wlecome To', end = ' ')
print('the black parade', end = ' ')
print('piano notes')

print()

# format 사용

print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a = 'You', b = 'Me'))

print("%s's favorite number is %d" % ('Park', 7)) # %s : 문자, %d : 정수, %f : 실수

print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776, 6543.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a = 776, b = 6543.123))