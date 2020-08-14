matrix=[]
for i in range(4):          # A for loop for row entries 
    a =[] 
    for j in range(4):
        if i+j>=3:
            a.append('#')
        else:
            a.append(' ')
    matrix.append(a) 
  
# For printing the matrix 
for i in range(4): 
    for j in range(4): 
        print(matrix[i][j], end = "") #end with nothing not space ie "" not " " 
    print() 