#Initialize matrix a  
a = [    
        [1, 2, 3],  
        [4, 5, 6],  
        [7, 8, 9]  
    ];  
   
rows = len(a);  
cols = len(a[0]);  
   
for i in range(0, rows):  
    sumRow = 0;  
    for j in range(0, cols):  
        sumRow = sumRow + a[i][j];  
    print("Sum of " + str(i+1) +" row: " + str(sumRow));