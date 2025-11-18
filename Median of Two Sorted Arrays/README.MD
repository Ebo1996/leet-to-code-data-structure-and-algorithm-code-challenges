<h2><a href="https://leetcode.com/problems/median-of-two-sorted-arrays/">
4. Median of Two Sorted Arrays
</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Hard-red" alt="Difficulty: Hard" />
<hr>

<p>
You are given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code>.
Return the <strong>median</strong> of the two sorted arrays.  
The required time complexity is <strong>O(log (m + n))</strong>.
</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.0
Explanation: merged array is [1,2,3].
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.5
Explanation: median = (2 + 3) / 2 = 2.5.
</pre>

<h3>Constraints:</h3>
<ul>
  <li>0 ≤ m, n ≤ 1000</li>
  <li>1 ≤ m + n ≤ 2000</li>
  <li><code>-10⁶ ≤ nums1[i], nums2[i] ≤ 10⁶</code></li>
</ul>

<hr>

<h2>Approach</h2>

<p>
To achieve <strong>O(log (m + n))</strong>, use binary search on the smaller array.
We find a partition point such that:
</p>

<p style="text-align:center;">
<strong>Left side max ≤ Right side min</strong>
</p>

<p>
This ensures the combined left half contains exactly half of all elements.  
Depending on whether the total length is even or odd, the median is:
</p>

<ul>
  <li><strong>Odd:</strong> minimum of the right partition</li>
  <li><strong>Even:</strong> average of max(left) and min(right)</li>
</ul>

<p>
Binary search adjusts the partition until this condition is met.
</p>
