hrs = input("Enter Hours:")
h = float(hrs)
rph=input('Enter rate per hour: ')
rate=float(rph)
#checking for the value of hrs
if h > 40:
	#print ('Damn')
	pay=rate*40
	rate=rate*1.5
	overtime= (h-40.0)*rate
	pay= pay + overtime
	print (pay)
	#print ('oye')
else:
	pay=h*rate
	print (pay)