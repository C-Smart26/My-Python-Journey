import random
print('====================')
print('Rock Paper Scissors')
print('====================')
print()
print('1. Rock✊')
print('2. Paper✋')
print('3. Scissors✌')
print()
p=int(input('Pick a number: '))
print('You chose: ',p)
c=random.randint(1,3)
print('Computer chose: ',c)
if p==1 and c==3:
    print('You Won!!')
elif p==3 and c==2:
    print('You Won!!')
elif p==2 and c==1:
    print('You Won!!')
elif p==c:
    print('Drawn Game')
else:
    print('You Lost 😞')