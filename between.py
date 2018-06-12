t=int(input())
u=int(input())
for n in range(t+1,u):
	fl=0
	for i in range(2,n//2):
			if n%i==0:
				fl=1
				break
	if fl==0:
		print(n)
