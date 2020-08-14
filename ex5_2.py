largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
    	break
    try:
    	num_float=float(num)

    except:
    	print ('Invalid input')
    	continue
    if largest == None:
    	largest=num_float
    elif largest<num_float:
    	largest=num_float

    if smallest=None:
    	smallest=num_float
    elif smallest>num_float:
    	smallest=num_float
    print(num)

    print ('Maximum is', largest)
    print ('Minimum is', smallest)


print("Maximum", largest)