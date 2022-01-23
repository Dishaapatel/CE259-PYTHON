#Find the Runner-up .
n = int(input())
arr = list(map(int, input().split()))
#It will find the max number.
l = max(arr)

for i in range(n):
    if l == max(arr):
      #It will remove the maximum number.
        arr.remove(max(arr))
   #Now the new maximum number will be the second last. 
print(max(arr))
