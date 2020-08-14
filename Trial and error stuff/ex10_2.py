name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)

time_dict=dict()
for line in handle:

    if line.startswith("From "):
        words=line.split()
        time=words[-2]
        print (time)
        hours=int(time[:2])
        print (hours)
        time_dict[hours]=time_dict.get(hours, 0)+1
    else:
        continue

hour_list=time_dict.items()
print (hour_list)
hour_list.sort()

for hour,count in hour_list:
    print (hour,count)



