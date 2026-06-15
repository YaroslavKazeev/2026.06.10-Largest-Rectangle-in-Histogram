def largestRectangleArea(heights: list[int]) -> int:
    maxArea = 0
    heightsDict = {}
    residualIndexes = set()
    for i, height in enumerate(heights):
        residualIndexes.add(i)
        if height in heightsDict:
            heightsDict[height].append(i)
        else:
            heightsDict[height] = [i]

    sortedHeights = sorted(heightsDict.keys())

    firstHeight = sortedHeights[0]
    maxArea = firstHeight * len(heights)
    residualIndexes.difference_update(heightsDict[firstHeight])
    sortedHeights.pop(0)

    for height in sortedHeights:
        indexes = heightsDict[height]
        for i in indexes:
            leftCurrInd = rightCurrInd = i
            width = 1
            while leftCurrInd - 1 in residualIndexes:
                leftCurrInd -= 1
                width += 1
            while rightCurrInd + 1 in residualIndexes:
                rightCurrInd += 1
                width += 1

            area = height * width
            if area > maxArea:
                maxArea = area

            residualIndexes.remove(i)

    return maxArea
