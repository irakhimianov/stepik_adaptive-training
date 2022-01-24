pattern = '''😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏'''
shifr = int(input())
my_str = input().strip()
output = ""
for ind, val in enumerate(my_str):
    if val in pattern:
        new_index = pattern.index(val) + shifr
        if abs(new_index) >= 79:
            new_index %= 80
        output += pattern[new_index]
print(output)