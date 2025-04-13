m = int(input("Enter the size of the square matrices (m x m): "))   

A = []  
B = []  

print("\nEnter the elements of Matrix A:")
for i in range(m):     
    row = []      
    for j in range(m):         
        value = int(input(f"Enter element A[{i+1}][{j+1}]: "))
        row.append(value)     
    A.append(row)  

print("\nEnter the elements of Matrix B:")
for i in range(m):     
    row = []     
    for j in range(m):         
        value = int(input(f"Enter element B[{i+1}][{j+1}]: "))
        row.append(value)     
    B.append(row)  

print("\nMatrix A + Matrix B:")
for i in range(m):     
    row = []     
    for j in range(m):         
        row.append(A[i][j] + B[i][j])     
    print(row)   

print("\nMatrix A - Matrix B:")
for i in range(m):     
    row = []     
    for j in range(m):         
        row.append(A[i][j] - B[i][j])     
    print(row)  

print("\nMatrix A * Matrix B:")
for i in range(m):     
    row = []     
    for j in range(m):         
        sum_product = 0         
        for k in range(m):             
            sum_product += A[i][k] * B[k][j]         
        row.append(sum_product)     
    print(row)   

print("\nMatrix A / Matrix B (Element-wise Division):")
for i in range(m):     
    row = []     
    for j in range(m):         
        if B[i][j] != 0:  #             
            row.append(A[i][j] / B[i][j])      
        else:             
            row.append('undefined') 
    print(row)
