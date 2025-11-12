<h2><a href="https://leetcode.com/problems/combination-sum/">39. Combination Sum</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>Given an array of <strong>distinct integers</strong> <code>candidates</code> and a target integer <code>target</code>, return <strong>all unique combinations</strong> of <code>candidates</code> where the chosen numbers sum to <code>target</code>. You may return the combinations in any order.</p>

<p>The same number may be chosen from <code>candidates</code> an <strong>unlimited number of times</strong>. Two combinations are unique if the frequency of at least one of the chosen numbers is different.</p>

<p>The test cases are generated such that the number of unique combinations that sum up to <code>target</code> is less than <code>150</code> combinations for the given input.</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> candidates = [2,3,6,7], target = 7
<strong>Output:</strong> [[2,2,3],[7]]
<strong>Explanation:</strong> 
2 and 3 are candidates, and 2 + 2 + 3 = 7. 
Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> candidates = [2,3,5], target = 8
<strong>Output:</strong> [[2,2,2,2],[2,3,3],[3,5]]
</pre>

<h3>Example 3:</h3>
<pre>
<strong>Input:</strong> candidates = [2], target = 1
<strong>Output:</strong> []
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>1 &lt;= candidates.length &lt;= 30</code></li>
  <li><code>2 &lt;= candidates[i] &lt;= 40</code></li>
  <li>All elements of <code>candidates</code> are distinct.</li>
  <li><code>1 &lt;= target &lt;= 40</code></li>
</ul>
