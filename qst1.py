import numpy as ny
arr1=ny.array([1,2,3,4,5])
arr2=ny.array([6,7,8,9,10])
print("\n arr1 :- ")
print(arr1)
print("\n arr2 :-")
print(arr2)
print("\n Sum of  arr1 & arr2 :-")
result_add=arr1 +arr2
print(result_add)
result_multiply=arr1*arr2
print("\n Multiple of  arr1 & arr2 :-")
print(result_multiply)
print("\n mean of result_add")
mean=ny.mean(result_add)
print(mean)
print("\n  maximum value in result_multiply")
max=ny.max(result_multiply)
print( max)