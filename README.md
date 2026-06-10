# Problem: Largest Rectangle in Histogram

## Problem Statement
Given an array representing heights of histogram bars, where the width of each bar is 1, find the area of the largest rectangle that can be formed in the histogram.

## Example
**Input**: `[2,1,5,6,2,3]`
**Output**: `10`

**Explanation**: The largest rectangle has area = 10, formed by bars with heights 5 and 6.

## Assignment Requirements

### 1. Situation & Task
We need to compute the maximum rectangular area under a histogram. Avoid brute force O(n²) and compute efficiently.

### 2. Approach: Monotonic Increasing Stack
For every bar, find how far it can extend to the left and right. We use a monotonic increasing stack to find:

*   `leftBoundary[i]` → first smaller element on the left
*   `rightBoundary[i]` → first smaller element on the right

#### Algorithm Steps

1.  **Traverse left → right**:
    *   Maintain increasing stack
    *   Compute `leftBoundary`
2.  **Traverse right → left**:
    *   Maintain increasing stack
    *   Compute `rightBoundary`
3.  **For each index**:
    *   `Width = rightBoundary[i] - leftBoundary[i] + 1`
    *   `Area = height[i] × Width`
    *   Take maximum area

#### Key Insight
The stack helps identify boundaries of rectangle where a bar is the minimum height. When a lower bar appears, pop from stack until the invariant holds. Each pop knows its left and right limits, giving max area in O(n).

### 3. Complexity Requirements

*   **Time Complexity**: O(n)
*   **Space Complexity**: O(n)
