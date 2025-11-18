<h2><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/">
3. Longest Substring Without Repeating Characters
</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>
Given a string <code>s</code>, return the length of the <strong>longest substring</strong>
without repeating characters.
</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> s = "abcabcbb"
<strong>Output:</strong> 3
Explanation: "abc" is the longest substring without repeating characters.
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> s = "bbbbb"
<strong>Output:</strong> 1
Explanation: The answer is "b".
</pre>

<h3>Example 3:</h3>
<pre>
<strong>Input:</strong> s = "pwwkew"
<strong>Output:</strong> 3
Explanation: "wke" is the longest substring.  
Note: "pwke" is a subsequence, not a substring.
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>0 ≤ s.length ≤ 5 × 10⁴</code></li>
  <li><code>s</code> may contain English letters, digits, symbols, and spaces.</li>
</ul>

<hr>

<h2>Approach</h2>

<p>
Use a <strong>sliding window</strong> and a <strong>set</strong> to track characters currently in the window.
</p>

<p>
Expand the window using the right pointer.  
If a duplicate is found, shrink from the left until it is removed.
</p>

<p>
At each step, compute the window size <code>(right - left + 1)</code> and keep the maximum.
</p>

<p>
This yields an efficient <strong>O(n)</strong> time solution.
</p>
