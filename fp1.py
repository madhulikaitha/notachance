# f=open('sample.text','w')
# f.close()
a=open('/Users/Maddie/desktop/ib/pass.txt','w+')
a.write('''Hello, it's me
I was wondering if after all these years you'd like to meet
To go over everything
They say that time's supposed to heal ya
But I ain't done much healing

Hello, can you hear me
I'm in California dreaming about who we used to be
When we were younger and free
I've forgotten how it felt before the world fell at our feet''')
a.close()

b=open('/Users/Maddie/desktop/ib/pass.txt','r')

#r1 = b.read()
#rint(r1)


print(b.readline())