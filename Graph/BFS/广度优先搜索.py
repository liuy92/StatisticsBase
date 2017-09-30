#-*-coding:utf-8-*-
"""
广度优先搜索(BFS):
目的：搜索两点之间的最短路径
实质：按照玉器店的距离来遍历所有的点
步骤：
  1. 寻找队列中下个顶点v，并进行标记
  2. 将与v相邻且未被标记过的点加入队列
"""
def  BreadthFirstPaths(Graph, start):
    V = Graph.keys()
    n = len(Graph)
    edgeTo = dict(zip(V, [0] * n))
    marked = dict(zip(V, [False] * n))
    def BreadthSearch(v):
        marked[v] = True
        for w in set(Graph[v]):
            if marked[w] == False:
                edgeTo[w] = v
                BreadthSearch(w)
                return edgeTo
    BreadthSearch(start)
    return edgeTo

b = dict(zip(range(6), [[2,1,5], [0,2], [0, 1,3,4], [5,4,2], [3,2], [3,0]]))
BreadthFirstPaths(b, 1)