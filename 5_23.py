import re

def get_int(start_message, error_message, end_message):
    print(start_message)
    x = input()
    if re.match(r"-*[1-9][\d]+$", x):
        print(end_message)
        return int(x)
    else:
        print(error_message)
        return get_int("", error_message, end_message)


x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
print(x)