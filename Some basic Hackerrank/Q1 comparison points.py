while i < len(a):
        if a[i]==b[i]:
            continue
        elif a[i]<b[i]:
            points_b= points_b+1
        else:
            points_a=points_a+1
        i+=1


for i in range (0, len(a)):
    if a[i]==b[i]:
        continue
    elif a[i]<b[i]:
        points_b= points_b+1
    else:
        points_a=points_a+1
    


