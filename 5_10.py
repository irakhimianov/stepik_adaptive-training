scale = {'mile': 1609,
         'yard': 0.9144,
         'foot': 0.3048,
         'inch': 0.0254,
         'km': 1000,
         'm': 1,
         'cm': 0.01,
         'mm': 0.001}

user_input = input().split()
num = float(user_input[0])
unit_from = user_input[1]
unit_to = user_input[-1]
print('{:3.2e}'.format(num * scale[unit_from] / scale[unit_to]))
