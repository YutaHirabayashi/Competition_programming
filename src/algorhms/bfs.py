from collections import deque

def bfs(start_node:int, node_number:int, edge_tuple_list:list) -> list:
    """BFS

    Args:
        start_node (int) : 距離を図る基準の頂点
        node_number (int): 頂点の数
        edge_tuple_list (list): 各頂点ごとにつながってる頂点の値が入ったTupleのリスト
    
    Example:
        node_number = 8
        edge_tuple_list = [
            (1, 2), (0, 3), (0, 5), (1, 4), (3, 5), (2, 4)
        ]

        0 -- 1 -- 3 -- 4
        |              |
        |              |
        2 -------------5

    Returns:
        list: start_nodeから各頂点までの距離
    """

    queue = deque([start_node])

    #initialize
    distance_from_start_node = [None] * node_number

    distance_from_start_node[start_node] = 0

    while queue:
        node = queue.popleft()
        for next_node in edge_tuple_list[node]:
            if distance_from_start_node[next_node] is None: #未調査の場合
                #現在までの距離に＋１した値をいれる
                distance_from_start_node[next_node] = distance_from_start_node[node] + 1 
                #キューに追加する（今キューに入ってる頂点が終わったら、その後そこを起点として調査する）
                queue.append(next_node)

    return distance_from_start_node

if __name__ == "__main__":
    bfs(
        0, 6, 
        [(1, 2), (0, 3), (0, 5), (1, 4), (3, 5), (2, 4)]
    )
    
    pass