<h2><a href="https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/">
Divide Array Into Arrays With Max Difference
</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>
You are given an integer array <code>nums</code> and an integer <code>k</code>.  
Split all elements of <code>nums</code> into groups of size <strong>3</strong> such that the difference between the maximum and minimum value in every group is <strong>&lt;= k</strong>.  
If it's possible, return any valid 2D array of groups; otherwise return <code>[]</code>.
</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> nums = [1,3,4,8,7,9,3,5,1], k = 2
<strong>Output:</strong> [[1,1,3],[3,4,5],[7,8,9]]
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> nums = [2,4,2,2,5,2], k = 2
<strong>Output:</strong> []
</pre>

<h3>Example 3:</h3>
<pre>
<strong>Input:</strong> nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14
<strong>Output:</strong> [[2,2,2],[4,5,5],[5,5,7],[7,8,8],[9,9,10],[11,12,12]]
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
  <li><code>1 &lt;= nums[i] &lt;= 10^5</code></li>
</ul>

<hr>

<h2>Solution</h2>

```python
class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            group = nums[i:i+3]
            if len(group) < 3 or group[-1] - group[0] > k:
                return []
            res.append(group)
        return res
