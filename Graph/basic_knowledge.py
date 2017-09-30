#-*-coding:utf-8-*-

"""
相关概念：
组成元素：顶点、边
自环：一条连接顶点和自身的边
平行边：两条边公用两个顶点
多重图：包含平行边的图
简单图：不含平行边、自环的图
顶点相邻：两个顶点可通过一条边连接
边依附：顶点相邻时，该边姨父与这两个顶点
路径：由边顺序连接的一系列顶点
简单路径：没有重复顶点的路径
环：至少含有一条边，且起点和终点相同的路径
简单环：除了起点、终点外，不包含其他重复点和边的环
长度：路径或环包含的变的个数
连通：当两个点之间存在一条连接对方的路径，称两点连通
连通图：任意一个顶点到其余任意一个顶点都存在一条路径的图
密度：已经连接的顶点占所有可能被连接的顶点对应的边的占比
二分图：可将所有丁点分为两部分，且每对相邻的顶点都属于不同的部分

树：
  实质：无环连通图
  性质：1. 有V个顶点、V-1条边，没有环
        2. 为连通的
        3. 删除任意一条边，起都不联通
        4. 增加任意一条边，都会形成环
        5. 任意一堆顶点之间仅存在一个简单路径
"""
#计算顶点v的度数,每个Graph对应的是顺序列表
def degree(Graph, v):
    if Graph[0] == v:
        d = 1
    else:
        d = 0
    for i in range(1, len(Graph) - 1):
        if Graph[i] == v:
            if Graph[i+1] == v:
                d += 1
            else:
                d += 2
    if Graph[len(Graph) - 1] == v:
        d += 1
    return d

#计算所有顶点最大度数
def maxDegree(Graph):
    degree_list = []
    for vi in set(Graph):
        di = degree(Graph, vi)
        print vi, '--', di
        degree_list.append(di)
    return max(degree_list)

#计算所有顶点的平均度数
def avgDegree(Graph):
    degree_list = []
    for vi in set(Graph):
        di = degree(Graph, vi)
        degree_list.append(di)
    return np.mean(degree_list)

#计算自环的个数
def selfLoops(Graph):
    number = 0
    for i in range(len(Graph) - 1):
        if Graph[i] == Graph[i + 1]:
            number += 1
    return number

"""
图的表示方法：
  1. 邻接矩阵
     V * V矩阵，横轴、纵轴分别是所有顶点，对应的矩阵值为相应横纵轴对应的顶点之间是否存在边的布尔值
     所需空间：V^2，遍历顶点的复杂度：V，检查是否相邻的复杂度：1，添加边的复杂度：1
  2. 邻接表
     将图中所有顶点存储到一张表中，并统计每个顶点，会对应一张该图中的相邻顶点的链表，若出现重复顶点，则记多次
     性能：同V+E成正比(V：顶点数；E：边数)；添加一条边所需的时间时一定的；遍历顶点v的所有相邻顶点的时间同v的度数是成正比
     常用的操作：添加、删除顶点，添加、删除边，检查图是否存在边
     所需空间：E + V，遍历顶点的复杂度：degree(V)，检查是否相邻的复杂度：degree(V)，添加一条边的复杂度：1
  3. 十字链表
"""
#创建邻接表(针对无向图)
def createGraph(l):
    V = set(l)
    n = len(l)
    result = []
    for vi in V:
        if l[n - 1] == vi:
            li = [l[n - 2]]
        elif l[0] == vi:
            li = [l[1]]
        else: 
            li = []
        for i in range(1, n - 1):
            if l[i] == vi:
                if l[i + 1] == vi:
                    li.append(l[i - 1])
                else:
                    li.append(l[i - 1])
                    li.append(l[i + 1])
        result.append(li)
    return dict(zip(list(V), result))
#创建邻接表(针对有向图)
def createGraph(l):
    V = set(l)
    n = len(l)
    result = []
    for vi in V:
        for i in range(n - 1):
            li = []
            if l[i] == vi:
                li.append(l[i + 1])
        result.append(li)
    return dict(zip(list(V), result))
"""
深度优先搜索(DFS)：
类似走迷宫的策略(Tremaux搜索)
  1. 选择一条没有走过的路径，并标记绳子
  2. 遇到走过的路口，返回上一个路口
  3. 若上个路口没有可选的其他未走过的路径，继续回退
DFS搜索策略：
  1. 访问一点后则标记其为已访问
  2. 递归的访问其没被标记过的所有邻居顶点
性质：
  1. 深度优先搜索标记与起点连通的所有顶点的搜索时间同顶点的度数之和成正比
  2. DFS从给定起点到任意顶点所需的时间和路径长度成正比
  3. 其得到的路径取决于图的结构+图的表示+递归的调用
"""
def depthSearch(Graph, start, end):
    V = Graph.keys()
    n = len(Graph)
    ct = 0
    marked = [False] * n
    result = dict(zip(list(V), marked))
    def dfs(Graph, v, ct, end):
        result[start] = False
        if v != end:
            result[v] = True
            ct += 1
            try:
                for w in Graph[v]:
                    if result[w] == False:
                        print w, marked[w]
                        dfs(Graph, w, ct, end)
                        return w
            except:
                return v
    dfs(Graph, start, ct, end)

b = dict(zip(range(6), [[2,1,5], [0,2], [0, 1,3,4], [5,4,2], [3,2], [3,0]]))
depthSearch(b, 0, 4)

def depthSearch(Graph, start):
    V = Graph.keys()
    n = len(Graph)
    ct = [0] * n
    marked = [False] * n
    result = dict(zip(list(V), marked))
    edgeTo = dizt(zip(list(V), ct))
    def dfs(Graph, v, ct, end):
        #result[start] = False
        result[v] = True
        ct += 1
        mark = []
        for w in Graph[v]:
            if result[w] == False:
                edgeTo[w] = v
                print w, marked[w]
                dfs(Graph, w, ct, end)
                return w
    dfs(Graph, start, ct, end)
    def hasPathTo(v):
        if result[v] == False:
            return null
        if v != start:
            for x in edgeTo[]

"""
广度优先搜索(BFS)：
目的：单点最短路径
"""
