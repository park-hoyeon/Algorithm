n = int(input())
numbers= list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_value = -10**9
min_value = 10**9
def dfs(current, result, add, sub, mul, div):
    global max_value, min_value
    if current == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return
    if add > 0: dfs(current+1, result + numbers[current], add-1, sub, mul, div)
    if sub > 0: dfs(current+1, result - numbers[current], add, sub-1, mul, div)
    if mul > 0: dfs(current+1, result * numbers[current], add, sub, mul-1, div)
    if div > 0: dfs(current+1, -((-result)//numbers[current]) if result < 0 else result//numbers[current], add, sub, mul, div-1)

dfs(1,numbers[0], add, sub, mul, div)
print(max_value)
print(min_value)