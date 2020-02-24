import heapq

dist = {}
startState = 1
t = 0
pq = []
tcost = 0
theuristicCost = 0
dist[startState] = 0
heapq.heappush(pq, (0, startState))
print(pq)
visited = set()
solvable = False
curNode = None
exploredNode = 0
expandedNode = 0

curNode = heapq.heappop(pq)[1]
print(curNode)
expandedNode += 1

dist[t] = tcost + theuristicCost
heapq.heappush(pq, (tcost + theuristicCost, t))
exploredNode += 1

print("Total number of explored node : ", exploredNode)
print("Total numbe of expanded node :", expandedNode)