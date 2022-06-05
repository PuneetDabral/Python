array = ['a','b','c','d']

for a in array:
    print(a)


print('-----------------------------------------')

for b in array[1:3]:
    print(b)




# add additional logic to for loops
print('-----')
for c in array:
    if c == 'd':
        print(f'{c} - black belt')
        break
    else:
        print(c)