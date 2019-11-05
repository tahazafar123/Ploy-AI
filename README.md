[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Ftahazafar123%2FPloy-AI.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Ftahazafar123%2FPloy-AI?ref=badge_shield)

Question 1
Mr. Little Z is on winter vacation, and he has decided to go to the planet Zearth. The only way of traveling through space is by using the aliens' teleportation machines. Mr. Little Z can teleport directly from planet Earth to the planet Zearth, but it is really risky. The aliens haven't perfected their teleportation machine. The greater the distance of traveling the bigger is risk. Because of this, the aliens have built more teleportation stations all throughout space. Teleporting through consecutive teleportation stations lowers the risk.

Mr. Little Z wants to go to the planet Zearth using the path where the teleportations are as short as possible - the path where the longest teleportation on it is minimized.

Mr. Little Z opened http://www.Space-net.spc and found a list of all the space teleportation stations. He decided to use the least risky path, as described above.

Help Mr. Little Z find the safest path from Earth to the planet Zearth: the path where the longest distance he has to teleport is minimized.

INPUT:
The first line of the standard input contains three real numbers, each from the interval [-10000.00, 10000.00], representing the 3D coordinates of the planet Zearth. The next line contains a number N, corresponding to the number of teleportation stations in space (1<=N<=500). Each of the next N lines contains three real numbers each from the interval [-10000.00, 10000.00], representing the 3D coordinates for each station.

Note: The 3D coordinates of Earth are (0.0, 0.0, 0.0). On the planets Earth and Zearth there are teleportation stations, too.

OUTPUT:
To the standard output write one real number to 2 decimal places, representing the maximum distance of the safest path on Mr. Little Z's way to Zearth.

Input:
2.00 2.00 2.00
3
0.00 0.00 2.00
0.00 2.00 2.00
2.00 0.00 0.00

Output:
2.00

Additional example:

Input:
2.00 2.00 2.00
3
1.00 1.00 1.00
1.00 2.00 2.00
2.00 2.00 1.00

Output:
1.73

1. Write down your thoughts on how would you approach this problem briefly.

Ans1 :

The given problem is a type of analytical mathematics. After reading the question in detail I found that to solve this question I need to study mathematical algorithms for shortest path. There are several methods available to state such problems like Bellman Ford's Algorithm, Dijkstra's Algorithm and Floyd–Warshall's Algorithm. I chose Dijkstra’s Algorithm because it is very efficient in finding the shortest path from one node to every other node within the same graph data structure and calculate all nodes at the same time. Therefore, after implementing the selected technique I obtained required output for my given question. 

2. Code down the solution with a language of your choice.

3. What is the complexity of your approach? Can we do better?

Ans3: 
In the developed algorithm Dijkstra's method is used to determine the shortest path. The working principle behind this technique is that given the shortest path between and each of a given set of nodes  , there must be another node x. Therefore, the shortest path from x must go from to  to x, for some 1 < i < 500. The code is developed on the discussed logic to determine the shortest path for Mr. Little Z to reach planet Zearth. The approach can further be improved by introducing an algorithm that works on the negative edges as well. Moreover, the processing time can be improved by avoiding blind search. 

Question 2 
After a long deferment, the mayor of Z-city has allowed pizzerias to be opened in town. Pizzerias used to be unlawful because of health reasons (according to the mayor). The city is big, and suddenly there are pizzerias everywhere.

We can imagine the city like a matrix with NxN squares, where every square represents one block of the city. Every pizzeria only delivers pizza to the nearby blocks. Specifically, every pizzeria delivers pizza to every block that is at most R blocks away from block the pizzeria's location. Distance is determined by the minimum number of blocks that the delivery guy must take if he is going East/West or North/South (moving diagonally is forbidden in Z-city). For example, let's say that N=5 and a pizzeria is located at the block (3, 3). It can deliver to a 2 block distance at most. The following map shows where the given pizzeria delivers pizzas.

00X00 
0XXX0 
XXXXX 
0XXX0 
00X00

Mr. Little Z loves pizza, so he wants to move to the block where he can have the greatest selection of pizzas (the block that has the maximum number of pizzerias delivering to it).

Help Mr. Little Z find that maximum. In other words, if he moves to the block with the greatest selection of pizzas, how many pizzerias will be able to deliver to his block?

INPUT:
The first line of the standard input contains the two numbers N and M, and both numbers are on the interval [1, 1000]. The number N represents the dimension of the city in blocks (the city has NxN blocks). M is the number of pizzerias in the city. The following M lines contain information about each pizzeria, given by the three numbers X, Y, R. The numbers X and Y represent the block where the pizzeria is located, (1 <= X, Y <= N) and the number R represents the maximum distance that the given pizzeria's delivery guy will travel to deliver pizza (1 <= R <= 100).

OUTPUT:
Write one number to the standard output that represents the number of pizzerias that deliver pizzas to the block with the greatest selection of pizzas.

Input: 
5 2 
3 3 2 
1 1 2

Output: 
2

Explanation: 

The first pizzeria delivers pizzas to the following blocks: 

00X00 
0XXX0 
XXXXX 
0XXX0 
00X00

and the second one: 

00000 
00000 
X0000 
XX000 
XXX00

So the number of pizzerias that deliver pizzas to each block is: 

00100 
01110 
21111 
12110 
11200

So the maximum number is 2.

1. Write down your thoughts on how would you approach this problem briefly.

Ans1 : 
This problem reflects the minimum spanning tree concept. After studying different minimum spanning tree algorithm like Prim, Boruvka and Kruskal. I  found Kruskal’s method is more efficient than the other. Because it utilizes the greedy approach for finding a minimum spanning tree. It treats every node as an independent tree and connects one with another only if it has the lowest cost compared to all other options available. The problem is given on the same pattern and can be solved easily by this algorithm. I implemented this technique and obtained required output successfully. 

2. Code down the solution with a language of your choice.

Ans2:
	Code files has been shared via Google drive link in email.

3. What is the complexity of your approach? Can we do better?

Ans3:
The implemented method in the code is used to solve the minimum spanning tree problems. The working principle of this algorithm is firstly it sorts the graph edges according to their weights. Then it started adding edges to the minimum spanning tree from the edge with the smallest edge of the largest weight.  Sort the graph edges with respect to their weights. It added edges which do not form a cycle like edges which connect only disconnected components. The code can be enhanced by avoiding the formation of cycles from arcs that usually slow down the execution process. For same weights this code can become more complex and difficult to develop. Therefore, an easy logic can be developed to reduce the complexity of code for the same weights.  
 





## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Ftahazafar123%2FPloy-AI.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Ftahazafar123%2FPloy-AI?ref=badge_large)