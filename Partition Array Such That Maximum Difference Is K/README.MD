<h2><a href="https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/">
2294. Partition Array Such That Maximum Difference Is K
</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>
You're given an integer array <code>nums</code> and an integer <code>k</code>.  
Your task is to split <code>nums</code> into the smallest number of subsequences such that:
</p>

<ul>
  <li>Each element appears in exactly one subsequence.</li>
  <li>The difference between the maximum and minimum value in every subsequence is <strong>≤ k</strong>.</li>
</ul>

<p>
A subsequence is formed by deleting some or no elements without changing the order of remaining elements.
</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> nums = [3,6,1,2,5], k = 2
<strong>Output:</strong> 2
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> nums = [1,2,3], k = 1
<strong>Output:</strong> 2
</pre>

<h3>Example 3:</h3>
<pre>
<strong>Input:</strong> nums = [2,2,4,5], k = 0
<strong>Output:</strong> 3
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>1 ≤ nums.length ≤ 100000</code></li>
  <li><code>0 ≤ nums[i], k ≤ 100000</code></li>
</ul>

<hr>

<h2>Approach</h2>

<p>
The optimal strategy is greedy:
</p>

<ol>
  <li>Sort <code>nums</code>.</li>
  <li>Start a new subsequence from the smallest unused number.</li>
  <li>As long as the next element differs from the start by ≤ k, keep it in the same group.</li>
  <li>If it exceeds k, start a new subsequence.</li>
</ol>

<p>
This guarantees the <strong>minimum</strong> number of subsequences.
</p>
