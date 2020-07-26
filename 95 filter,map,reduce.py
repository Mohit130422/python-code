#filter, map, reduce:-
#eg.
from functools import *
mylist=[1,2,3,4,5,6,7,8,9,10]
even_list=list(filter(lambda n:n%2==0,mylist))
print(type(even_list))
print(even_list)
#run
print("---------------------")
mylist2=list(map(lambda n:n*n,even_list))
print(type(mylist2))
print(mylist2)
#run
print("--------------------")
result=reduce(lambda a,b:a+b,mylist2)
print("result:-",result)
print("average:-",result/mylist2.__len__())
#run

