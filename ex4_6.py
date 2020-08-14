hrs = input("Enter Hours:")
h = float(hrs)
rph=input('Enter rate per hour: ')
r=float(rph)
#checking for the value of hrs
def computepay(h, r):
	if h > 40:
		#print ('Damn')
		pay=r*40
		r=r*1.5
		overtime= (h-40.0)*r
		pay= pay + overtime
		return pay
		#print ('oye')
	else:
		pay=h*r
		return pay

#callingthefunc
pay=computepay(h, r)
print ('Pay:', pay)