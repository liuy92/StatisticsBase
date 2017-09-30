#-*-coding:utf-8-*-
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
  2. 
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
    marked = dict(zip(list(V), [False] * n))
    edgeTo = dict(zip(list(V), [0] * n))
    def dfs(v):
        marked[v] = True
        while set(marked) != set([True]):
            w_list = Graph[v]
            m_list = []
            for w in w_list:
                m_list.append(marked[w])
            if set(m_list) != set([True]):
                print 'if', v
                i = 0
                w = w_list[i]
                while marked[w] == False:
                    marked[w] = True
                    edgeTo[w] = v
                    print w, marked[w]
                    dfs(w)
                    i += 1
                return edgeTo
            else:
                print 'else', v
                dfs(edgeTo[v])
                return edgeTo
    return dfs(start)


depthSearch(b, 0)