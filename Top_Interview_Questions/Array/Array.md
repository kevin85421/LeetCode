# Array
## Q1: Remove Duplicates from Sorted Array
*   My Solution is good enough
## Q2: Best Time to Buy and Sell Stock II
###  My Solution
*   Flow
    * Step1: Remove duplicates in ***prices*** (list)
    * Step2: Iterate ***prices*** to record buying points and selling points
    * Step3: Compute ***maxProfit***
*   Cons
    * Time Complexity: Need to iterate ***prices*** two times
    * Space Complexity: Need two extra list ***buy*** and ***sell*** to store buying points and selling points
### LeetCode Solution: [Link](https://leetcode.com/articles/best-time-to-buy-and-sell-stock-ii/)
*   Approach 2: Peak Valley Approach   
    * The concepts of ***valley*** and ***peak*** are very similar with the concepts of ***buy*** and ***sell***
    * Better than My Solution
      * Time Complexity: Find respective ***valley/peak pair*** in one iteration
      * Space Complexity: Update ***maxProfit*** as soon as a ***valley/peak pair*** is found
      * ***peak/valley*** definitions can avoid necessity to ***remove duplicates***

        |  | My Solution | Approach 2 |
        | :-----| :----: | :----: |
        | valley | `(prices[i] < prices[i+1]) and (prices[i] < prices[i-1])` | `prices[i] < prices[i + 1]`|
        | peak | `(prices[i] > prices[i+1]) and (prices[i] > prices[i-1])` | `prices[i] > prices[i + 1]` |

```java
class Solution {
    public int maxProfit(int[] prices) {
        int i = 0;
        int valley = prices[0];
        int peak = prices[0];
        int maxprofit = 0;
        while (i < prices.length - 1) {
            while (i < prices.length - 1 && prices[i] >= prices[i + 1])
                i++;
            valley = prices[i];
            while (i < prices.length - 1 && prices[i] <= prices[i + 1])
                i++;
            peak = prices[i];
            maxprofit += peak - valley;
        }
        return maxprofit;
    }
}
```
*   Approach 3: Simple One Pass
    * In this case, instead of looking for every peak following a valley, we can simply go on crawling over the slope and keep on adding the profit obtained from every consecutive transaction.
    * Better than Approach 2
      * Easy to implement 
```java
class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1])
                maxprofit += prices[i] - prices[i - 1];
        }
        return maxprofit;
    }
}
```