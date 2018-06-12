try:
	o=int(input())
	temp=o
	rev=0
	while(temp!=0):
		rem=temp%10
		rev=rev*10+rem
		temp=int(temp/10)
	if rev==o:
		print('palindrome')
	else :
		print('not palindrome')
except:
	print('invalid')
