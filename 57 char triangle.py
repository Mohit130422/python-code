#character triangle
for i in range (65,70):
    for j in range (65,i+1):
        print(chr(j),end=' ')
    print()
#run
print("----------------------------")

for i in range (65,70):
    for j in range(69,i-1,-1):
        print(chr(j),end=' ' )
    print()
#run
print('-----------------------------')

for i in range (65,70):
    for k in range (65,i):
        print(" ",end=' ')
    for j in range (69,i-1,-1):
        print(chr(j),end=' ')
    print()
#run
print("-------------------------------")

for i in range(65,70):
    for k in range(69,i,-1):
        print(" ",end=' ')
    for j in range (65,i+1,):
        print(chr(j),end=' ')
    print()
#run
print("------------------------------")

for i in range(65,70):
    for k in range (69,i,-1):
        print(" ",end=' ')
    for j in range (65,i+1):
        print(chr(j),end=' ')
    for a in range (i-1,64,-1):
        print(chr(a),end=' ')
    print()
#run

