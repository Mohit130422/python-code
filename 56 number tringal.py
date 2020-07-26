#Number triangle string
for i in range (1,6):
    for j in range (1,i+1):
        print(j,end=' ')
    print()
    #run
print('------------------------------')

for i in range (1,6):
    for j in range(5,i-1,-1):
        print(j,end=' ')
    print()
    #run
print('------------------------------')

for i in range (1,6):
    for k in range (5,i,-1):
        print (" ",end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()
    #run
print('------------------------------')

for i in range (1,6):
    for k in range (5,i,-1):
        print(" ",end=' ')
    for j in range (1,i+1):
        print(j,end=' ')
    for a in range (i-1,0,-1):
        print(a,end=' ')
    print()
#run


