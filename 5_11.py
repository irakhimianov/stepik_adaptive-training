user_input = [int(x) for x in input().split()]
b = user_input[:-1]
c = user_input[1:]
diff = []
for i, v in enumerate(b):
    diff.append(abs(b[i] - c[i]))
if set(diff)== set(range(1, len(user_input))):
    print("Jolly")
else:
    print("Not jolly")