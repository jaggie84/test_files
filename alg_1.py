
# def fizzbuzz(n):

#     if n % 3 == 0 and n % 5 == 0:
#         return 'FizzBuzz'
#     elif n % 3 == 0:
#         return 'Fizz'
#     elif n % 5 == 0:
#         return 'Buzz'
#     else:
#         return str(n)

# print "\n".join(fizzbuzz(n) for n in xrange(0, 101))

for num in range(0, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num,'FizzBuzz')
    elif num % 3 == 0:
        print(num,'Fizz')
    elif num % 5 == 0:
        print(num,'Buzz')
    else:
        print(num)