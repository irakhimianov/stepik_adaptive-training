values = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
first, second = input().split()
suit = input()

if first[-1] == second[-1]:
    print((values.index(first[:-1]) > values.index(second[:-1])) * "First",
          (values.index(first[:-1]) < values.index(second[:-1])) * "Second",
          (values.index(first[:-1]) == values.index(second[:-1])) * "Error",
          sep="")
elif (first[-1] != second[-1]) and (first[-1] != suit and second[-1] != suit):
    print("Error")
else:
    print((first[-1] == suit) * "First",
          (second[-1] == suit) * "Second",
          sep="")