# 14. Гистограмма и прямоугольник

heights = list(map(int, input().split()[1:]))

stack = list()
area = 0
for i in range(len(heights)):
	while stack and heights[stack[-1]] > heights[i]:
		top = stack.pop()
		height = heights[top]
		width = i - stack[-1] - 1 if stack else i
		area = max(area, height * width)
	stack.append(i)
while stack:
	top = stack.pop()
	height = heights[top]
	width = len(heights) - stack[-1] - 1 if stack else len(heights)
	area = max(area, height * width)
print(area)
