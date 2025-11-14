<h2><a href="https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/">
3085. Minimum Deletions to Make String K-Special
</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>
You are given a string <code>word</code> and an integer <code>k</code>.
A string is considered <strong>k-special</strong> if for every pair of characters <code>i</code> and <code>j</code>,
the absolute difference in their frequencies satisfies:
</p>

<p style="text-align: center;">
<strong>|freq(word[i]) − freq(word[j])| ≤ k</strong>
</p>

<p>
Your goal is to compute the <strong>minimum number of deletions</strong> required to make the string k-special.
</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> word = "aabcaba", k = 0  
<strong>Output:</strong> 3
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> word = "dabdcbdcdcd", k = 2  
<strong>Output:</strong> 2
</pre>

<h3>Example 3:</h3>
<pre>
<strong>Input:</strong> word = "aaabaaa", k = 2  
<strong>Output:</strong> 1
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>1 ≤ word.length ≤ 10⁵</code></li>
  <li><code>0 ≤ k ≤ 10⁵</code></li>
  <li>word consists only of lowercase English letters</li>
</ul>

<hr>

<h2>Approach</h2>

<p>
Let each character frequency be <code>f</code>.  
We want all frequencies to lie within some interval <code>[fmin, fmax]</code> with <code>fmax - fmin ≤ k</code>.
</p>

<p>
We try all possible <code>fmax</code> values (from 0 up to max frequency), compute the required <code>fmin = max(0, fmax - k)</code>,
and calculate how many deletions are needed to force all frequencies into that interval.
</p>

<p>
The minimum deletions across all choices of <code>fmax</code> is the answer.
</p>
