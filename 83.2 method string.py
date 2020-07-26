#methods of String
#lower():- it is used to convert string into lower case.
s1='ALIGARH'
print(s1.lower())
#run
print("-----------------")
#upper():- it is used to convert string into upper case.
s2='aligarh'
print(s2.upper())
#run
print("----------------")
#endswith():- it is used to check is and with particular content or not.
s3='index.html'
print(s3.endswith('html'))
print(s3.endswith('js'))
print("----------------")
#startswith():- it is used to check string is start with particular sequence or not.
s4='index.html'
print(s3.startswith('html'))
print(s3.startswith('index'))
print("---------------")
#format():- to format a string.
s5="{},{} and {}".format("mohit","akhil","rahul")
print(s5)
s6="{c},{a} and {b}".format(a="mohit",b="akhil",c="rahul")
print(s6)
print("----------------")
#count():- count a accurence in the string object.
s7="aligarh"
print(s7.count('a'))
#run
print("----------------")
#index():- find out index in string object.
s8="aligarh"
print(s8.index('g'))
#run
print("----------------")
#upper():-
s9="aligarh"
s10=s9.upper()
print(s10)
print(s10.isupper())

