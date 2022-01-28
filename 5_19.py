source = input()
substring = input()
answer = ''
for i in range(len(source)):
    if substring == source[i:(i + len(substring))]:
        answer += f' {i}'
print(answer[1:]) if answer else print(-1)