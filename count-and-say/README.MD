<h2><a href="https://leetcode.com/problems/count-and-say/">38. Count and Say</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>The <strong>count-and-say</strong> sequence is a sequence of digit strings defined by the recursive formula:</p>

<ul>
  <li><code>countAndSay(1) = "1"</code></li>
  <li><code>countAndSay(n)</code> is the run-length encoding of <code>countAndSay(n - 1)</code>.</li>
</ul>

<p><strong>Run-length encoding (RLE)</strong> is a string compression method that replaces consecutive identical characters with the character and the count of its occurrences.</p>

<p>Given a positive integer <code>n</code>, return the <strong>n<sup>th</sup></strong> element of the count-and-say sequence.</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> "1211"

<strong>Explanation:</strong>
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> "1"

<strong>Explanation:</strong> This is the base case.
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>1 &lt;= n &lt;= 30</code></li>
</ul>
