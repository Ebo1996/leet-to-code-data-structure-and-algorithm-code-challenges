<h2>
  <a href="https://leetcode.com/problems/set-intersection-size-at-least-two/">
    757. Set Intersection Size At Least Two
  </a>
</h2>

<img src="https://img.shields.io/badge/Difficulty-Hard-red" alt="Difficulty: Hard" />
<hr>

<p>
You are given a list of intervals, where each interval is represented as <code>[start, end]</code>.  
Your task is to build the smallest possible set of integers such that <strong>each interval contains at least two numbers</strong> from that set.
</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> intervals = [[1,3],[3,7],[8,9]]
<strong>Output:</strong> 5
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> intervals = [[1,3],[1,4],[2,5],[3,5]]
<strong>Output:</strong> 3
</pre>

<h3>Example 3:</h3>
<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3],[2,4],[4,5]]
<strong>Output:</strong> 5
</pre>

<h3>Constraints:</h3>
<ul>
  <li>1 ≤ intervals.length ≤ 3000</li>
  <li>intervals[i].length = 2</li>
</ul>

<hr>

<h2>Approach</h2>

<p>
This problem is solved optimally using a <strong>greedy</strong> strategy.  
The key idea is to sort intervals in a way that allows reusing selected numbers as much as possible.
</p>

<p><strong>Sort intervals by:</strong></p>
<ul>
  <li><strong>end</strong> in ascending order</li>
  <li>if ends are equal, <strong>start</strong> in descending order</li>
</ul>

<p>
This ensures we always handle the interval that "forces" the earliest choices first, while preventing conflicts where a shorter interval comes after a longer overlapping one.
</p>

<h3>Selection Rules:</h3>
<ul>
  <li>If the interval has <strong>zero</strong> overlap with previously chosen numbers → add two numbers (<code>end-1</code> and <code>end</code>).</li>
  <li>If the interval has <strong>one</strong> overlapping number → add one number (<code>end</code>).</li>
  <li>If it already has <strong>two</strong> → no action needed.</li>
</ul>

<p>
By carefully updating the last two selected numbers, the solution maintains correctness while achieving minimal size.
</p>
