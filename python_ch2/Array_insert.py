def insertion (arr ,num):
 print (arr)   
 for x in range(len (arr)):
  if arr[x]>num and arr[x-1]<num :
    #arr[x-1] = num
    arr.insert(x,num)
    break
  else:
    continue
    
  
 print(arr)        
    
insertion([1,2,4],3)  
insertion([42,8,15,23,42], 16)  
insertion([2,4,6,-8], 5)