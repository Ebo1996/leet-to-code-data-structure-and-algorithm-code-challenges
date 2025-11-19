<h2><a href="https://leetcode.com/problems/search-in-rotated-sorted-array/">
33. Search in Rotated Sorted Array
</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>
You are given a sorted array <code>nums</code> that may have been rotated at some unknown pivot.
Given an integer <code>target</code>, return its index if found, or <code>-1</code> otherwise.
The solution must run in <strong>O(log n)</strong> time.
</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 0
<strong>Output:</strong> 4
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 3
<strong>Output:</strong> -1
</pre>

<h3>Example 3:</h3>
<pre>
<strong>Input:</strong> nums = [1], target = 0
<strong>Output:</strong> -1
</pre>

<h3>Constraints:</h3>
<ul>
  <li>1 ≤ nums.length ≤ 5000</li>
  <li><code>-10⁴ ≤ nums[i] ≤ 10⁴</code></li>
  <li>All values in <code>nums</code> are distinct.</li>
</ul>

<hr>

<h2>Approach</h2>

<p>
This problem is an adaptation of binary search.  
Even though the array is rotated, <strong>one half is always sorted</strong>.
</p>

<p>
At each step:
</p>
<ul>
  <li>Check which half (left or right) is sorted.</li>
  <li>Determine if the <code>target</code> lies inside that sorted half.</li>
  <li>Narrow the search space accordingly.</li>
</ul>

<p>
This ensures the algorithm remains <strong>O(log n)</strong> while efficiently locating the target.
</p>
