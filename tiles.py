from copy import deepcopy

class TilesNode:
    def __init__(
        self,
        state,
        parent=None,
    ):
        self.state = state
        self.parent = parent

    def is_goal(self) -> bool:
        return self.state == [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

    def find_empty_space(self) -> tuple[int, int]:
        for i, row in enumerate(self.state):
            for j, col in enumerate(row):
                if col == 0:
                    return i, j

    def swap_tiles(self, row1, col1, row2, col2):
        new_state = deepcopy(self.state)
        new_state[row1][col1], new_state[row2][col2] = (
            new_state[row2][col2],
            new_state[row1][col1],
        )
        return new_state

    def get_children(self) -> list["TilesNode"]:
        children = []
        empty_row, empty_col = self.find_empty_space()
        moves = [(-1,0), (1,0), (0,-1), (0,1)]
        for row_offset, col_offset in moves:
            new_row, new_col = empty_row + row_offset, empty_col + col_offset
            if 0 <= new_row < 4 and 0 <= new_col < 4:
                new_state = self.swap_tiles(empty_row, empty_col, new_row, new_col)
                child_node = TilesNode(new_state, parent=self)
                children.append(child_node)
        return children

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.state)

    def __repr__(self) -> str:
        return self.__str__()

    def get_path(self) -> list["TilesNode"]:
        path = []
        current_node = self
        while current_node:
            path.append(current_node)
            current_node = current_node.parent
        return path[::-1]

    def __eq__(self, other):
        if isinstance(other, TilesNode):
            return self.state == other.state
        return False

    def __hash__(self):
        return hash(tuple(map(tuple, self.state)))

    def is_solvable(self):
        flat_state = [tile if tile != 0 else 16 for row in self.state for tile in row]

        inversions = 0
        for i in range(len(flat_state)):
            for j in range(i + 1, len(flat_state)):
                if flat_state[i] > flat_state[j]:
                    inversions += 1

        return inversions % 2 == 0