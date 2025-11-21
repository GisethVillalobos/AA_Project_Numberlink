# numberlinkPlayer.py

import pprint

def solve_board(file_path):

    board = read_board(file_path)

    pairs = get_pairs(board)

    ordered_pairs = order_pairs_by_heuristic(pairs, board)

    solved = solve_numberlink(board, ordered_pairs, index_pair=0)

    if solved:
        print("Solution found:\n")
        print_board(board)
    else:
        print("There is not solution for this board.")

# end def

def read_board(file_path):
    with open(file_path, 'r') as f:
        lines = [line.rstrip("\n") for line in f]

    dims = lines[0].split()
    rows, cols = int(dims[0]), int(dims[1])

    board = []
    for i in range(1, rows + 1):
        row = list(lines[i])
        if len(row) < cols:
            row += [' '] * (cols - len(row))
        board.append(row)

    return board
# end def

def get_pairs(board):
    positions = {}

    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell != ' ':
                positions.setdefault(cell, []).append((r, c))

    pairs = []
    for symbol in sorted(positions.keys()):
        if len(positions[symbol]) == 2:
            start, end = positions[symbol]
            pairs.append((start, end))

    return pairs
# end def


def order_pairs_by_heuristic(pairs, board):
    rows = len(board)
    cols = len(board[0])

    def free_neighbors(r, c):
        count = 0
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if board[nr][nc] == ' ' or board[nr][nc].isalpha():
                    count += 1
        return count
    # end def

    def get_restriction_score(pair):
        (r1, c1), (r2, c2) = pair
        
        manhattan_dist = abs(r1 - r2) + abs(c1 - c2)
        
        min_free_neighbors = min(free_neighbors(r1, c1), free_neighbors(r2, c2))
        
        score = (min_free_neighbors * 10) + manhattan_dist
        
        return score
    # end def

    ordered = sorted(pairs, key=get_restriction_score)
    return ordered
# end def

def solve_numberlink(board, pairs, index_pair):
    if index_pair > len(pairs) - 1:
        return is_board_full(board)

    start, end = pairs[index_pair]
    symbol = board[start[0]][start[1]]

    roads = generate_possible_roads(start, end, board)

    for road in roads:
        mark_road(board, road, symbol)

        if solve_numberlink(board, pairs, index_pair + 1):
            return True

        unmark_road(board, road)

    return False
# end def

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True
# end def

def mark_road(board, road, symbol):
    for r, c in road:
        board[r][c] = symbol
# end def

def unmark_road(board, road):
    for r, c in road[1:-1]:
        board[r][c] = ' '
# end def

def generate_possible_roads(start, end, board):
    m, n = len(board), len(board[0])
    max_roads = 2 * m * n
    (sr, sc) = start
    (er, ec) = end

    roads = []
    visited = [[False] * n for _ in range(m)]
    path = [start]

    def is_valid_cell(r, c, current_path):
        if (r, c) == end:
            return True
        if (r, c) == start and len(current_path) > 1:
            return False
        return board[r][c] == ' '

    def dfs(r, c, current_path):
        nonlocal roads
        
        if len(roads) >= max_roads:
            return

        if (r, c) == end:
            roads.append(current_path.copy())
            return

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        directions.sort(key=lambda dr_dc: abs(r + dr_dc[0] - er) + abs(c + dr_dc[1] - ec))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                if is_valid_cell(nr, nc, current_path):
                    visited[nr][nc] = True
                    current_path.append((nr, nc))
                    
                    dfs(nr, nc, current_path)
                    
                    current_path.pop()
                    visited[nr][nc] = False

    visited[sr][sc] = True
    dfs(sr, sc, path)
    
    return roads
# end def


def print_board(board):
    for row in board:
        print(''.join(row))
# end def

if __name__ == "__main__":  
    import sys
    if len(sys.argv) != 2:
        print("Usage: python numberlinkPlayer.py <board_file>")
        sys.exit(1)
    file_path = sys.argv[1]
    solve_board(file_path)
# end if

# eof numberlinkPlayer.py