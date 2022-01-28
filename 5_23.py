def get_int(start_message, error_message, end_message):
    x = input(f"{start_message}\n")
    # while not re.match(r'(0$)|(^-?[1-9]\d*$)', x):
    while True:
        if x.isdigit() or (x[0] == "-" and x[1:].isdigit()):
            print(end_message)
            return int(x)
        else:
            print(error_message)
            x = input()