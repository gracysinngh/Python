# 1.Write a program to initialise an array of size 10 and print the even elements

arr=list(map(int,input().split()))

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        print(arr[i], end=' ')

# 2.Given an array of size n , write a program to print the last element of the array

n=int(input(""))
nums= list(map(int, input("").split()))
print(nums[-1])

# 3.Given input of an array of size n, write a program to print it's first and last element

n=int(input(""))
nums=list(map(int,input("").split()))

print(nums[0], nums[-1], end=" ")

# 4.Write a program to take an Integer Input N and an array Input of size N to print the second last element of the array.

n=int(input(""))
nums=list(map(int,input().split()))

print(nums[-2])

# 5. Write a program to take an array Input of size 8 and print the smallest element of the array.

nums=list(map(int,input().split()))

min = nums[0]
for i in range(1,len(nums)):
	if nums[i] < min:
		min = nums[i]
print (min)

# 6.Given an array of size and index, you need to write a program to print the element present on that index.

inputs = list(map(int, input().split()))
n = inputs[0]
index = inputs[1]

arr = list(map(int, input().split()))

if 0 <= index < n:
    print(arr[index])
else:
    print("Invalid index")

# 7.For the given array and the given element k, write a program to print it's index if it is present in the array or print -1.


n = int(input())
arr = list(map(int, input().split()))
k = int(input())

if k in arr:
    print(arr.index(k))
else:
    print(-1)

# 8.Given an array of size n, write a program to print the middle element.
n=int(input())
arr=list(map(int,input().split()))

mid=arr[n//2]
print(mid)

# 9.Write a program to take an array Input of length 5 and print the average value of all the array elements.

arr=list(map(float,input().split()))

total=sum(arr)
avg=total/5
print(avg)

# 10.Write a program to take the Integer Input N and then Input N elements in the next line and output the sum of the first two elements of an array.

N=int(input())
arr=list(map(int,input().split()))

result= arr[0] + arr[1]
print(result)


# 11.Write a program to find the sum of elements in an array.

n=int(input())
arr=list(map(int,input().split()))

tot=sum(arr)
print(tot)

# 12.Given a array of size n with repeating elements print the sum of the unique elements that are present in the array Example:

n=int(input())
arr=list(map(int,input().split()))

unique_sum = 0
for i in range(n):
    count = 0
    for j in range(n):
        if i != j and arr[i] == arr[j]:
            count += 1
    if count == 0:
        unique_sum += arr[i]

print(unique_sum)

# 13.Write a program to print "E" if any even element is present in the array otherwise print "O". Take the Input of N and in the next line take the Input of N elements of the array.

N = int(input())
arr = list(map(int, input().split()))[:N]

flag = 1

for i in arr:
    if i % 2 == 0:
        print("E")
        flag = 0
        break

if flag == 1:
    print("O")

# 14.Write a program that takes an array of integers as input and counts the number of even and odd numbers in the array. The program should then display the count of even and odd numbers.

n = int(input())


arr = list(map(int, input().split()))[:n]

even_count = 0
odd_count = 0


for num in arr:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count)
print(odd_count)


# 15.Write a program to print sum of elements present at even index in an array.

n = int(input())
arr = list(map(int, input().split()))[:n]


summ = 0

for i in range(n):
    if i % 2 == 0:
        summ += arr[i]


print(summ)


# 16.You are given an array of integers. Your task is to write a program to swap the largest and smallest element in the array.

n=int(input(""))
arr=list(map(int,input().split()))
minn_numb=min(arr)
max_numb=max(arr)

minn_index = arr.index(minn_numb)
max_index = arr.index(max_numb)

arr[minn_index],arr[max_index]=arr[max_index],arr[minn_index]
print(*arr)


# 17.Write a program to take an Integer Input n and swap the first and the last element mutually in the array whose size is n.

n=int(input(""))
arr=list(map(int,input().split()))

if n>1:
    arr[0], arr[-1] = arr[-1], arr[0]
print(*arr)

# 18.Write a program to Initialise an array of size 6 and print the count of only prime elements in an arra

def isprime(num):
    if num <= 1:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

# getting the soace separated input with the help of split function
arr=list(map(int, input().split()))
# initializing the count variable with 0
count=0
for i in arr:
    if isprime(i):
        # updating the count if we find any prime number in the array
        count+=1
# printing the count variable
print(count)


# 19.Given an array of integers and a target element x, write a program to find the index of x in the array. If x does not exist in the array, return -1.
# Linear Search

n = int(input())
arr=list(map(int,input().split()))
target=int(input())
ans=-1
for i in range(len(arr)):
    if arr[i] == target:
        ans = i
        break
print(ans)


# 20.Write a program that takes an array of integers as input and finds the index of a given element x in the array using binary search. If the element is present in the array, the program should return its 0-based index. If the element is not found, the program should return -1.

# The array will be sorted in ascending order. You must implement the binary search algorithm to find the element efficiently.

def binarySearch(array, x, low, high):
    while low<=high:
        mid=(low+high)//2

        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1

N = int(input())
array = list(map(int, input().split()))[:N]
x = int(input())

result = binarySearch(array, x, 0, len(array) - 1)

if result != -1:
    print(str(result))
else:
    print(-1)

