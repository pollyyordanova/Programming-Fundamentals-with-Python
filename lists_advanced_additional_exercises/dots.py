def dfs(board, visited, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(row, col)]
    count = 0

    while stack:
        r, c = stack.pop()
        if visited[r][c]:
            continue
        visited[r][c] = True
        count += 1

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]):
                if board[new_r][new_c] == '.' and not visited[new_r][new_c]:
                    stack.append((new_r, new_c))

    return count

def largest_connected_dots(board):
    n = len(board)
    visited = [[False] * len(board[0]) for _ in range(n)]
    max_dots = 0

    for r in range(n):
        for c in range(len(board[r])):
            if board[r][c] == '.' and not visited[r][c]:
                dots_count = dfs(board, visited, r, c)
                max_dots = max(max_dots, dots_count)

    return max_dots

if __name__ == "__main__":
    n = int(input())
    board = [input().strip().split() for _ in range(n)]
    result = largest_connected_dots(board)
    print(result)

