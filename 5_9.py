user_input = [int(x) for x in input().split()]
print(user_input)
for i in range(user_input[0], user_input[1] + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    else:
        if i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)