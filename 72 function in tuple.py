#function in tuple:-
#all()
t2=(1,2,3,4,4,5,4,5,6,7,8,9)
t3=()
t4=(1,2,0)
print(type(t2))
print(all(t2))
print(all(t3))
print(all(t4))
print('----------------------------------')
#any()
print(any(t2))
print(any(t3))
print(any(t4))
print('----------------------------------')
#enumerate()
res=enumerate(t2,101)
print(type(res))
b=tuple(res)
print(b)
print('----------------------------------')
#sum()
print(sum(t2),'sum')
print('----------------------------------')
#max()
print(max(t2),'maximum')
print('----------------------------------')
#min()
print(min(t2),'minimum')
print('----------------------------------')
#sorted()
print(sorted(t2),'sorting')
