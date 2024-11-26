from tiles import TilesNode
from queue import PriorityQueue

def heuristic(node: TilesNode) -> int:
    goal_state = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    current_state = node.state
    return sum(1 for i in range(4) for j in range(4) if current_state[i][j] != 0 and current_state[i][j] != goal_state[i][j])


def AStar(root, heuristic: callable) -> TilesNode or None:  # type: ignore
    unexplored = PriorityQueue()
    counter = 0
    unexplored.put((0, counter, root))
    explored = set()
    g_score = {root: 0}
    f_score = {root: heuristic(root)}

    while not unexplored.empty():
        current_node = unexplored.get()[2]
        if current_node.is_goal():
            return current_node.get_path()
        explored.add(current_node)
        for child in current_node.get_children():
            if child in explored:
                continue
            temp_g_score = g_score[current_node] + 1
            if child not in g_score or temp_g_score < g_score[child]:
                g_score[child] = temp_g_score
                f_score[child] = temp_g_score + heuristic(child)
                counter += 1
                unexplored.put((f_score[child], counter, child))
                child.parent = current_node

    return None