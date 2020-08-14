#Solving problem using regex 

import re 

filename=input("Enter file name:")
data = open(filename)

sum_numbers=0 
number_list=[]
for line in data: 
    number=re.findall('\d+', line)
    #print (number)
    #number_list.append(number)

    for num in number:
        print (num)
        number_list.append(num)
        sum_numbers+=int(num)
        
print (sum_numbers)
    
    

