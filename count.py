count = 0
while (True):
	print(count)
	count+=1
	time.sleep(.500)
	
count=0
while(count<10):
	print('iter=', count)
	time.sleep(.500)

count=0
iter_count=1
while(count<=10):
	print(iter_count, '--iter=', count)
	count+=1
	iter_count+=1
	time.sleep(.500)
	

ll=[11,22,33,44]
for i in range(0,10):
	print(i)
	time.sleep(.200)
	
ll=[11,22,33,44,55 ['qq','ww','ee','rr','tt','yy'],66,77]
count=0
for i in ll:
	print(count,ll[count])
	count+=1
	time.sleep(.200)