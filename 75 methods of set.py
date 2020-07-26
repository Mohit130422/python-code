#methods of SET
#add() it is used to add element in SET
s1={1,2,3,4,5,6,7,8}
s1.add(34)
print(s1)
#run
print('-------------------')

#update() it is used to add more element in SET
s2={1,2,3,4,5,6,7,8,9}
t=(10,11,12,13)
s2.update(t)
print(s2)
#run
print('-------------------')

#clear()it is used to clear all the element of SET
s1.clear()
s2.clear()
print(s1,' ',s2)
print('-------------------')

#remove() it is used to remove an element from SET.
s3={1,2,3,4,5,6,7}
res=s3.remove(2)
print(s3,' ',res)
#run
print('------------------')

#discard() it is used to discard element from the SET.
s4={1,2,3,4,5,6,7}
res=s4.discard(3)
print(s4)
#run
print('-----------------')

#pop() it is used to 'pop' an element.
s11={1,2,3,4,5,6,7,8,9}
res=s11.pop()
print(s11,' ',res)
print('-------------------')

#union() it is used to perform of the union of two SETS.
s5={1,2,3,4,5,6,7,8,9}
s6={10,11,12,13,14}
print(s5.union(s6))
#print(s5|s6)
#run
print('-------------------')

#Intersection() it is used to perform intersection operation of two 'SET'
s7={1,2,3,4,5,6}
s8={4,5,6,8,9}
print(s7.intersection(s8))
#print(s7 & s8)
#run
print('-------------------------')

#diffrence() diffrence operation of the two 'SET'
s9={1,2,3,4,5,6}
s10={4,5,6,8,9}
print(s9.difference(s10))
#print(s9-s10)
#run
print('----------------------------------')

#symmetric diffrence():- It is used to perform symmetric difference of two SET
s12={1,2,3,4,5,6}
s13={4,5,6,8,9}
print(s12.symmetric_difference(s13))
#print(s12^s13)
print('----------------------------------')
#issubset():-it is used to check a SET is a subset to another SET or NOT
s14={1,2,3,4,5}
s15={1,4,5}
s16={10,11,12}
print(s15.issubset(s14))
print(s15.issubset(s16))
#run
print('----------------------------------')
#issuperset():-it is used to check a SET is superset of another SET of NOt.
s17={1,2,3,4,5}
s18={1,4,5}
s19={10,11,12}
print(s17.issuperset(s18))
print(s18.issuperset(s19))
#run
print('-----------------------------------')
#frozenset():- it is used to make a frozen SET
a={1,2,3,4,5}
s20=frozenset(a)
print(type(s20))
print(s20)
#run


