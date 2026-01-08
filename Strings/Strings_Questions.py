#1. Write a program to check whether the input string's first letter is a vowel or not.

a=input()
if a[0].lower() in ['a','e','i','o','u']:
    print("Yes")
else:
    print("No")

# 2. Given two Input strings in two lines. Write a program to print "Yes" if they are equal otherwise "No". Note that Input strings are case-sensitive and different cases should print No.

a=input()
b=input()

if a==b:
    print("Yes")
else:
    print("No")

# 3. Given two Input strings str1 and str2 in a single line. Concatenate str1 and str2 and check if they are equal to the given third string str in the second line of Input. If they are equal print "yes" otherwise print "no".

str1,str2=input().split()
str=input()
summ=str1+str2
if summ==str:
    print("yes")
else:
    print("no")

# 4. Write a program to measure the length of the given string and print its length. Given that there are no spaces in the Input strings

n=input()
a=len(n)

print(a)


# 5. Write a program to print "Yes" if '#' is present in a string otherwise print "No".

s=input()
flag=1
for i in range(len(s)):
    if s[i]=='#':
     print('Yes')
     flag=0
     break

if flag==1:
    print("No")


# 6.You are given an Input string S. Write a program to print the number of hashes present in it.

s=input()
a=s.count('#')

print(a)

# 7.Write a program to print the character at the given index of string s. Given that there are no white spaces between the string.

s, index=input().split()
index=int(index)
print(s[index])

# 8.Your task is to write a program that takes a string Str, a starting position start, and a length n, and prints the substring starting from the given position and of the specified length.

st=input()
a,b=map(int,input().split())
ans=st[a:a+b]
print(ans)

# 9. Given an Input string s. Write a program to insert space in the string where a lowercase alphabet is followed by a uppercase alphabet. Given that the Input string has no spaces.

n=input()
result=""

for i in range(len(n)-1):
    result+=n[i]

    if n[i].islower() and n[i+1].isupper():
        result+=" "
result+=n[-1]

print(result)

# 10.Given a string s that contains lowercase alphabets, numbers, and some special characters, write a program to count the number of special characters in the string.

s=input()
count=0

for i in range (len(s)):

    if not s[i].isalnum():
        count+=1
print(count)


# 11.Given an input string containing alphabets and special characters, write a program to remove all special characters and print the final string consisting only of alphabets. The input string may include both uppercase and lowercase letters along with special characters.

s = input()
result = ""

for char in s:
    if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z'):
        result += char
    else:
        continue  

print(result)

# 12.Write a program that counts the number of positions in a string where an uppercase letter follows directly after a lowercase letter.

st=input()
count=0
for i in range(len(st)-1):
    if st[i].islower() and st[i+1].isupper():
        count+=1
print(count)


# 13. Write a program that takes a string as input and checks if it contains both the characters "b" and "ac" (where "ac" should appear as a sequence in that order within the string). If both "b" and "ac" are found anywhere in the string, the program should output "yes". If either or both are missing, the program should output "no".

s=input()

if "b" in s and "ac" in s:
     print("yes")
else:
    print("no")


# 14. Given a string s which consist of numerical values, write a program to print the count of 0,1 and 2.

s=input()
count_0=0
count_1=0
count_2=0

for i in s:
    if i=='0':
        count_0+=1
    if i=='1':
        count_1+=1
    if i=='2':
        count_2+=1
print(count_0, count_1, count_2, end=" ")

# 15.Given a string, remove all occurrences of the letter "b" and the substring "ac" from it. Do this by going through the string only once.

# You need to make changes directly in the string and keep track of the updated string as you go through it.

n=input()
u=n.replace("b", "")
o=u.replace("ac", "")
print(o)

# 16. Given an input string, write a program to print:

# "U" if the string contains only uppercase alphabets.
# "L" if the string contains only lowercase alphabets.
# "Both" if the string contains a mix of both lowercase and uppercase alphabet

s=input()

if s.isupper():
    print("U")

elif s.islower():
    print("L")

else:
    print("Both")

# 17. Write a program to count the Number of Vowels in a String

s=input()

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

count=0

for i in s:
    if i in vowels:
        count+=1
print(count)

# 18. Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longest_common_prefix(strs):
    return os.path.commonprefix(strs)

import os
n = int(input())
strs = [input().strip() for _ in range(n)]

print(longest_common_prefix(strs))

# 19.Check if s is a subsequence of t. Two strings are given s and t, print true otherwise print false.

s,t = input().split()

# Initialize pointers
i = 0
j = 0

# Loop until either string ends
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
    j += 1

# Check if all characters of s were found in t in order
if i == len(s):
    print("true")
else:
    print("false")

