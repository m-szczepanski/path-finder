# Project Description: Pathfinding Algorithm for Obstacle-Rich Boards

## This project implements the A* (A-star) algorithm to find the optimal path from a starting point to a goal on a board with obstacles. Here’s a brief overview of the project:

<ol>
  <li><b>Project Goal:</b></li>
  Create a program that automatically finds the shortest path from a given starting point to a goal on a grid-based board, taking obstacles into account.
  <li><b>Assumptions:</b></li>
    <ul>
      <li>The board is a square grid with dimensions of 100x100 cells.</li>
      <li>Obstacles are randomly placed on the board.</li>
      <li>The player starts at position (0, 0).</li>
      <li>The coin (goal) is placed randomly on the board.</li>
    </ul>
  <li><b>Implementation:</b></li>
    <ul>
      <li>The Pygame library is used for visualizing the board.</li>
      <li>The A* algorithm calculates the optimal path based on heuristics and movement cost.</li>
      <li>Movement is allowed in four directions: up, down, left, and right.</li>
      <li>Obstacles are considered during path calculations.</li>
    </ul>
  <li><b>Visualization:</b></li>
    <ul>
      <li>The board is drawn in a Pygame window.</li>
      <li>The path is marked on the board.</li>
    </ul>
  <li><b>Insights:</b></li>
    <ul>
      <li>This project provides an understanding of how the A* algorithm works and its application in finding optimal paths.</li>
      <li>It can be extended with additional features, such as dynamically generated obstacles or different heuristics.</li>
    </ul>
  <li>Python libraries used:</li>
    <ul>
      <li>Pygame</li>
      <li>Pytest</li>
      <li>time</li>
      <li>heapq</li>
    </ul>
</ol>

### More about A* algorithm
> A* is a graph traversal and pathfinding algorithm, which is used in many fields of computer science due to its completeness, optimality, and optimal efficiency. Given a weighted graph, a source node and a goal node, the algorithm finds the shortest path (with respect to the given weights) from source to goal.
> One major practical drawback is its O(b^d) space complexity, as it stores all generated nodes in memory. Thus, in practical travel-routing systems, it is generally outperformed by algorithms that can pre-process the graph to attain better performance, as well as by memory-bounded approaches; however, A* is still the best solution in many cases.
<br>

More informations here:<br>
[wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)<br>
[geeksforgeeks](https://www.geeksforgeeks.org/a-search-algorithm/)
