def largestRectangleArea(heights: list[int]) -> int:
    stack = []
    max_area = 0
    for i in range(len(heights) + 1):
        h = 0 if i == len(heights) else heights[i]
        while stack and h < heights[stack[-1]]:
            width = i if len(stack) == 1 else i - stack[-1]
            height = heights[stack.pop()]
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area
