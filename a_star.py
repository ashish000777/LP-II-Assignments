def AStarAlgo(startNode, stopNode):
	openSet = set(startNode)
	closedSet = set()
	g{}	#Store distance from starting
	parents{}	#Parents contains adjacency of all nodes
	#Distance of starting node is zero
	g[startNode] = 0
	#Start node is root node i.e it has no parent node
	#So start node is set to its own parent node
	parents[startNode] = startNode
	
	while len(openSet) > 0:
		n = None
		#Find f() lowest
		for v in openSet:
			if n==None or g[v] + heuristic[v] < g[n] + heuristic[n]:
				n = v
		if n==stopNode or GraphNodes[n]==None:
			pass
		else:
			for (m,weight) in getNeighbours(n):
				if m not in openSet and m not in closedSet:
					openSet.add(m)
					parents[m] = n
					g[m] = g[n] + weight
					# Compare m from start
				else:
					if g[m] > g[n] + weight:
						#Update g[m]
						g[m] g[n] + weight
						#Change parent of m to n
						parents[m] = n;
						#If m is in closed set then remove it and put it into open set
						if m in closedSet:
							closeSet.remove(m)
							openSet.add(m)
		if n==None:
			print("Path does not exist")
			return None
			
		# If current node is stop node then we reconstruct from start node
		if n == stopNode:
			path = []
			while parents[n] != n:
				path.append(n)
				n = parents[n]
			
			path.append(startNode)
			path.reverse()
			print('Path found: {}', .format(path))
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
							
			
