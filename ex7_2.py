fname = input("Enter file name: ")
fh = open(fname)
num=0
add=0

count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    #print(line)
    pos=line.find(" ")
    num=float(line[pos+1:])
    add+=num
    count+=1
    
avg=add/count
print ('Average spam confidence:', avg)   
#print("Done")