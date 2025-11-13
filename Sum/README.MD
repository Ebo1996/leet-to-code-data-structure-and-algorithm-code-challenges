<h2><a href="https://leetcode.com/problems/3sum/">15. 3Sum</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>Given an integer array <code>nums</code>, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.</p>

<p><strong>Notice</strong> that the solution set must not contain duplicate triplets.</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]

<strong>Explanation:</strong>
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> []

<strong>Explanation:</strong> The only possible triplet does not sum up to 0.
</pre>

<h3>Example 3:</h3>
<pre>
<strong>Input:</strong> nums = [0,0,0]
<strong>Output:</strong> [[0,0,0]]

<strong>Explanation:</strong> The only possible triplet sums up to 0.
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>3 &lt;= nums.length &lt;= 3000</code></li>
  <li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
