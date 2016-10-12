first = []
second = []

first_word = 'Programming'
second_word = 'Gram Ring Mop'
for x in first_word.replace(" ", ""):
    first.append(x.lower())
    
for x in second_word.replace(" ", ""):
    second.append(x.lower())

if len(first) != len(second):
   print(1)
    
    
first_copy = first[:]
second_copy = second[:]

for x,y in zip(first_copy, second_copy):
    if x in second and y in first:
        try:
            first.remove(y)
            second.remove(x)
        except ValueError: print(2)
    else:
        print(3)

print(4)