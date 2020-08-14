score=input('Enter score: ')

try:
    scr=float(score)
    if scr>0.0 and scr<1.0:
        if scr < 0.6:
            print ('F')

        elif scr >= 0.9:
            print('A')
        elif scr >= 0.8:
            print("B")
        elif scr >= 0.7:
            print ("C")
        elif scr >= 0.6:
            print ('D')
    else:
        print ('Enter a value within the range 0.0 and 1.0')
except:
    print ('Enter a valid value')