import re
user_input = input()
# s = "1a2bb34a"
output = ""
pattern = r"[\d+]*[\D]"
formatted = re.findall(pattern, user_input)
for el in formatted:
    if len(el) > 1:
        output += int(el[:-1]) * el[-1]
    else:
        output += el
print(output)