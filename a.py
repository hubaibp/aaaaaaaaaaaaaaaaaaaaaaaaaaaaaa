# l1=[]
# for i in range(1,51):
#     l1.append(i)
# print(l1)




# l1=["python","java","php"]
# s=input("enter the element")
# if s in l1:
#     print("elemtn",s,"is present")
# els    



# l1 = [11,12,13,14,15,16]

# odd=[]
# even=[]
# for i in l1:
#     if i % 2 ==0:
#         even.append(i)
#     else:
#         odd.append(i) 
# print(odd)
# print(even)           



'''find max without using max()'''

# l1=[17,8,1,2,6,9]
# n=l1[0]
# for i in l1:
#     if i>n:
#         n=i
# print(n)      



'''enter userinput  elements to dict'''

# d1=dict()
# for i in range(5):
#     keey,vaalue =input("key"),input("value")
#     d1.update({keey:vaalue})
# print(d1)    
    
'''prime or not'''

# n=input("enter the limit")
# for i in range(2,n+1):
#     if 
        
    


# def factorial(num):
#     sum=1
#     for i in range (1,num+1):
#         sum*=i
#     print(sum)
# factorial(2)        


# n=9474
# k=str(n)
# l=len(k)
# sum=0

# while n>0:
#     last=n%10
#     sum+=last**l
#     n//=10
# if n==sum:
#     print("amstrong")
    
# else:
#     print("not")    
        



''' rearrange array'''         
# def move_zeroes(arr):
#     non_zero_index = 0
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
#             non_zero_index += 1
#     return arr

# # Example usage:
# arr = [4, 5, 0, 1, 9, 0, 5, 0]
# print(move_zeroes(arr))  # Output: [4, 5, 1, 9, 5, 0, 0, 0]



# def greter(arr):
#     count=0
#     k=arr[0]
#     for i in range(len(arr)):
#         if arr[i]>k:
            
        
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(reverse_array([1, 2, 3, 4, 5]))


def missing_number(arr, n):
    total = n * (n + 1)// 2
    return total - sum(arr)

print(missing_number([1, 3,4, 5, 6], 6))  # Output: 3

print(missing_number([1, 2, 3, 5, 6], 6))  # Output: 4
case1 = [1, 2, 3, 4, 5]

sssssssssssssssssssssssssssssssssssssssssssssss
print(case1)
































