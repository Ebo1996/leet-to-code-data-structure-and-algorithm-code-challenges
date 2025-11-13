<h2><a href="https://leetcode.com/problems/search-insert-position/">35. Search Insert Position</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Easy-green" alt="Difficulty: Easy" />
<hr>

<p>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>

<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> Target 5 is found at index 2.
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> Target 2 is not found, so it would be inserted at index 1.
</pre>

<h3>Example 3:</h3>
<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 7
<strong>Output:</strong> 4
<strong>Explanation:</strong> Target 7 is not found, so it would be inserted at index 4.
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>1 <= nums.length <= 10<sup>4</sup></code></li>
  <li><code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code></li>
  <li><code>nums</code> contains distinct values sorted in ascending order</li>
  <li><code>-10<sup>4</sup> <= target <= 10<sup>4</sup></code></li>
</ul>

<h3>Solution Approach:</h3>
<p>This problem can be solved efficiently using <strong>binary search</strong>:</p>
<ul>
  <li>Use binary search to find the target in O(log n) time</li>
  <li>If found, return the index immediately</li>
  <li>If not found, the <code>left</code> pointer will naturally point to the correct insertion position</li>
</ul>
<p>The key insight is that when binary search terminates without finding the target, the <code>left</code> pointer indicates where the target should be inserted to maintain sorted order.</p>