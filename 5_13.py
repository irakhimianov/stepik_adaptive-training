words = input().split()
words_length_count = {}
for word in words:
    count = len(word)
    if count in words_length_count:
        words_length_count[count] += 1
    else:
        words_length_count[count] = 1
for key in sorted(words_length_count):
    print(f"{key}: {words_length_count[key]}")