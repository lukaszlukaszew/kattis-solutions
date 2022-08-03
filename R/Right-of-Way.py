"""Right-of-Way"""

# vajningsplikt

result = "NO"

right = {"South": "East", "East": "North", "North": "West", "West": "South"}
left = {"South": "West", "East": "South", "North": "East", "West": "North"}
front = {"South": "North", "East": "West", "North": "South", "West": "East"}

start, end, another = input().split()

if (another == right[start] and end != right[start]) or (
    another == front[start] and end == left[start]
):
    result = "YES"

print(result)
