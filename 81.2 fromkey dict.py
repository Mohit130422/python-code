#fromkey() create a dictionary from the value of keys.
key={'a','e','i','o','u'}
d1={}.fromkeys(key)
print(d1)
key={'a','e','i','o','u'}
d2={}.fromkeys(key,'vowel')
print(d2)
d2['a']=100
print(d2)
#run