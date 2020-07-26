#methods of list:-
#append()add element in the end
mylist=[1,2,3,4,5]
mylist.append(10)
print(mylist)
#run
print('-----------------------')
#extend()adding another list
mylist1=[1,2,3,4,5,6]
a=[10,11,12,]
mylist1.extend(a)
print(mylist1)
#run
print('-----------------------')
#insert() insert a element
mylist2=[1,2,3,4,5,6]
mylist2.insert(1,'Mohit')
print(mylist2)
#run
print('-----------------------')
#remove() remove element
mylist3=[1,2,3,4,5,6]
res=mylist3.remove(4)
print(mylist3,' ',res)
#run
print('-----------------------')
#pop() return index value
mylist4=[1,2,3,4,5,6]
res=mylist.pop(4)
print(mylist4,' ',res)
#run
print('-----------------------')
#clear() empty a list
mylist5=[1,2,3,4,5,6]
mylist5.clear()
print(mylist5)
#run
print('-----------------------')
#index() find the index
mylist20=[1,2,3,4,5,6,7]
res20=mylist20.index(3)
print(res20)
#run
print("-----------------------")
#count() the accqurence of the element
mylist6=[1,2,3,4,5,6,3,4,5,4]
res=mylist6.count(4)
print(res)
#run
print('-----------------------')
#sort() sort the element in acending order
mylist7=[1,2,4,6,8,12,22,24,13]
mylist7.sort()
#mylist7.sort(reverse=True)
print(mylist7)
#run
print('-----------------------')
#reverse() to reverse the element
mylist8=[1,2,3,4,5,6,7,8,9,3]
mylist8.reverse()
print(mylist8)
#run
print('-----------------------')
#copy() it returns a shallow copy of a list.
a=[10,2,30,14,5,3]
b=a.copy()# if b=a so id is equal and a's simillar with b's value
print(type(b),' ',id(a),' ',id(b))
print(b)
b[1]=100
print(b)
print(a)
#run
print('-----------------------')