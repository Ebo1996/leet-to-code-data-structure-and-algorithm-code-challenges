<h2><a href="https://leetcode.com/problems/regular-expression-matching/">
10. Regular Expression Matching
</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Hard-red" alt="Difficulty: Hard" />
<hr>

<p>
You are given an input string <code>s</code> and a pattern <code>p</code>.  
Implement regular expression matching with support for the special characters:
</p>

<ul>
  <li><code>.</code> — Matches any single character.</li>
  <li><code>*</code> — Matches zero or more occurrences of the preceding element.</li>
</ul>

<p>
The match must cover the <strong>entire</strong> input string.
</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> s = "aa", p = "a"
<strong>Output:</strong> false
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> s = "aa", p = "a*"
<strong>Output:</strong> true
</pre>

<h3>Example 3:</h3>
<pre>
<strong>Input:</strong> s = "ab", p = ".*"
<strong>Output:</strong> true
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>1 ≤ s.length ≤ 20</code></li>
  <li><code>1 ≤ p.length ≤ 20</code></li>
  <li><code>s</code> consists only of lowercase English letters.</li>
  <li><code>p</code> consists of lowercase letters, <code>.</code>, and <code>*</code>.</li>
  <li>Every <code>*</code> has a valid character before it.</li>
</ul>

<hr>

<h2>Approach</h2>

<p>
We use dynamic programming, defining <code>dp(i, j)</code> as whether the substring <code>s[i:]</code>
matches the pattern <code>p[j:]</code>.
</p>

<p>
For each position, we first check whether the current characters match (direct character match or <code>.</code>).
Then we handle the two scenarios:
</p>

<ul>
  <li>If the next pattern character is <code>*</code>, we can either skip the <code>x*</code> block entirely,
      or if the first character matches, consume one character from <code>s</code> while keeping the same pattern index.</li>

  <li>If the next character is not <code>*</code>, we simply check direct match and move both indices forward.</li>
</ul>

<p>
Memoization ensures each (i, j) pair is computed once, making the solution efficient.
</p>
