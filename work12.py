def working(string):
	holy1=['Sunday','Saturday']
	work1=['Monday','Tuesday','Wednesday','Thursday','Friday']
	if string in holy1:
		return no
	elif string in work1:
		return yes
	return 'invalid'
def main():
	try:
		day=input()
		print(working(day))
	except:
		print('invalid')
		
main()
