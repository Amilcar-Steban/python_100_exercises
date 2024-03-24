n = int(input())
arr = list(map(int, input().split()))

maxi = max(arr)
result = []

for i in arr:
    if i != maxi:
        result.append(i)
    
print(max(result))