#a={3:56,'hello':'something',56.45:'bye'}

#print(a)
#print(type(a))
#print(a[3])
#squ={a:a**2 for a in range(1,11)}
#cub={a:a**3 for a in range(1,11)}
#print(squ.keys())
#print(squ.values())
#print(squ.items())
#squ.clear()
#print(squ)

#key=[1,2,3,4,5]
#value='samevile'
#dic=dict.fromkeys(key,value)
#print(dic)

#squ={a:a**2 for a in range(1,5)}
#cub={a:a**3 for a in range(1,11)}
#print(squ)
#print(cub)
#squ.update(cub)
#print(squ)

key=[1,2,3,4,5]
value=[i for i in range(1,5)]
dic=dict.fromkeys(key,value)
print(dic)