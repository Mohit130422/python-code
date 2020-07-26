#enumerate()- it returns a enumerated (ऐसा object जिसे loop लगाकर access किया जाता है) object
a=[10,2,30,14,5,3,True]
res=enumerate(a,101)
print(type(res))
b=list(res)
print(b)
#run

az=[10,2,3,40,14,5,6]
print(sum(az))
print(max(az))
print(min(az))
print(sorted(az))