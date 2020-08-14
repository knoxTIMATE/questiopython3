def miniMaxSum(arr):
    
    sumlist=[]
    arr=[5, 5, 5, 5, 5]
    print (len(arr))
    print (max(arr))
    print (min(arr))

    for i in arr:
        sum=0
        for j in arr:
            if i==j:
                continue
            elif max(arr)==min(arr):
                sum+=j 
            else:
                sum+=j
        sumlist.append(sum)

    print (min(sumlist), max(sumlist))

        
