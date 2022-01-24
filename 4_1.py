user_input = input()
user_input += "_"
output = ""
count = 1
for ind, val in enumerate(user_input):
    if user_input[ind] != "_":
        if user_input[ind] == user_input[ind + 1]:
            count += 1
        else:
            if count != 1:
                output += (str(count) + user_input[ind])
            else:
                output += user_input[ind]
            count = 1
print(output)