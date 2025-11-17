<h2><a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/">
19. Remove Nth Node From End of List
</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>
Given the <strong>head</strong> of a linked list, remove the <strong>n-th node from the end</strong> of the list and return its head.
</p>

<h3>Example 1:</h3>
<img src="https://assets.leetcode.com/uploads/2020/09/09/remove_ex1.jpg" alt="Example 1" />

<pre>
<strong>Input:</strong> head = [1,2,3,4,5], n = 2  
<strong>Output:</strong> [1,2,3,5]
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> head = [1], n = 1  
<strong>Output:</strong> []
</pre>

<h3>Example 3:</h3>
<pre>
<strong>Input:</strong> head = [1,2], n = 1  
<strong>Output:</strong> [1]
</pre>

<h3>Constraints:</h3>
<ul>
  <li>The number of nodes in the list is <code>sz</code>.</li>
  <li><code>1 ≤ sz ≤ 30</code></li>
  <li><code>0 ≤ Node.val ≤ 100</code></li>
  <li><code>1 ≤ n ≤ sz</code></li>
</ul>

<hr>

<h2>Approach</h2>

<p>
Use the classic <strong>two-pointer technique</strong>.  
Create a dummy node to simplify edge cases (such as removing the head).
</p>

<p>
Move the <code>fast</code> pointer <strong>n + 1</strong> steps ahead to create a gap of <strong>n</strong> nodes between <code>fast</code> and <code>slow</code>.  
Then move both pointers until <code>fast</code> reaches the end.  
At this point, <code>slow</code> is exactly before the node to remove.  
Adjust its pointer to skip the target node.
</p>

<p>
This ensures a clean <strong>one-pass</strong> solution with <strong>O(1)</strong> extra space.
</p>
