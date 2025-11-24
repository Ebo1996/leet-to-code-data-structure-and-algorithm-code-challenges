<h2><a href="https://leetcode.com/problems/binary-prefix-divisible-by-5/">1018. Binary Prefix Divisible By 5</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />
<hr>

<p>You are given a binary array <code>nums</code> (0-indexed).</p>

<p>We define <code>x<sub>i</sub></code> as the number whose binary representation is the subarray <code>nums[0..i]</code>.</p>

<p>Return an array of booleans <code>answer</code> where <code>answer[i]</code> is <code>true</code> if <code>x<sub>i</sub></code> is divisible by 5.</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> [true,false,false]
<strong>Explanation:</strong>
Binary prefixes: 0 → 0, 01 → 1, 011 → 3 (base-10).
Only 0 is divisible by 5.
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> [false,false,false]
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
  <li><code>nums[i]</code> is either <code>0</code> or <code>1</code></li>
</ul>

<h3>Solution (Python):</h3>

<pre>
class Solution(object):
    def prefixesDivBy5(self, nums):
        res = []
        prefix = 0
        
        for bit in nums:
            prefix = (prefix * 2 + bit) % 5
            res.append(prefix == 0)
        
        return res
</pre>
