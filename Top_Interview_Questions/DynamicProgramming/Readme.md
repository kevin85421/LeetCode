# Dynamic Programming
## Overview
*   **Easy:** Q1 ~ Q4
*   **Medium:**
*   **Worth it:** Q1
## Q1: Climbing stairs
### My Solution (Good enough)
*   Same as Approach 4 (Fibonacci Number) 
*   Time Complexity: `O(n)` --> beat 98.93%
*   Space Complexity: `O(1)`
### LeetCode Solution: [Link](https://leetcode.com/problems/climbing-stairs/solution/)
*   Approach 5: Binets Method (matrix multiplication)(**Good technique**)
    *   Time Complexity: `O(log n)`
    *   Space Complexity: `O(1)`
## Q2: Best Time to Buy and Sell Stock 
### My Solution (Good enough)
*   Same as Approach 2
*   Time Complexity: `O(n)` --> beat 96.8%
*   Space Complexity: `O(1)` --> beat 55%
*   How to make the code more concise? --> LeetCode Solution (Approach 2)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max_profit if (price - min_price) < max_profit else (price - min_price)
        return max_profit
```
### LeetCode Solution
*   Approach 2: One pass
    * **Good technique:** `int minprice = Integer.MAX_VALUE;`
```java
public class Solution {
    public int maxProfit(int prices[]) {
        int minprice = Integer.MAX_VALUE;
        int maxprofit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minprice)
                minprice = prices[i];
            else if (prices[i] - minprice > maxprofit)
                maxprofit = prices[i] - minprice;
        }
        return maxprofit;
    }
}
```