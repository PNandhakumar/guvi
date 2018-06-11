def countdigs(m):
	c=0
	while(m!=0):
		m//=10
		c+=1
	print(c)
def main():
	try:
		m=int(input())
		countdigs(m)
	except:
		print('invalid')
main()
