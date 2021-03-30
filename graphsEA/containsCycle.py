def cycleInGraph(edges):
    # Write your code here.
    noOfNodes = len(edges)
    visited = [False for _ in range(noOfNodes)]
    nodesInStack = [False for _ in range(noOfNodes)]

    for node in range(noOfNodes):
        if visited[node]:
            continue
        
        containsCycle = isNodeInCycle(node, edges, visited, nodesInStack)
        if containsCycle:
            return True

    return False


def isNodeInCycle(node, edges, visited, nodesInStack):
    visited[node]  = True
    nodesInStack[node] = True

    neighbors = edges[node]
    for neighbor in neighbors:
        if not visited[neighbor]:
            containsCycle = isNodeInCycle(neighbor, edges, visited, nodesInStack)
            if containsCycle:
                return True
        elif nodesInStack[neighbor]:
            return True

    nodesInStack[node] = False
	return False
