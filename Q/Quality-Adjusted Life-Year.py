"""Quality-Adjusted Life-Year"""

# qaly

periods = int(input())
result = 0

for i in range(periods):
    quality, years = map(float, input().split())
    result += quality * years

print(result)
