def find_kate_exit(maze):
    rows = len(maze)
    cols = len(maze[0])
    visited = set()
    start = None

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'k':
                start = (r, c)
                break
        if start:
            break

    if not start:
        return "Kate cannot get out"

    def is_exit(r, c):
        return r == 0 or r == rows - 1 or c == 0 or c == cols - 1

    def dfs(r, c, moves):
        if r < 0 or r >= rows or c < 0 or c >= cols or maze[r][c] == '#' or (r, c) in visited:
            return -1

        if is_exit(r, c):
            return moves

        visited.add((r, c))

        max_moves = -1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            result = dfs(r + dr, c + dc, moves + 1)
            if result > max_moves:
                max_moves = result

        visited.remove((r, c))
        return max_moves

    number_of_moves = dfs(start[0], start[1], 0)

    if number_of_moves == -1:
        return "Kate cannot get out"
    else:
        return f"Kate got out in {number_of_moves + 1} moves"


if __name__ == "__main__":
    n = int(input())
    maze = [input().strip() for _ in range(n)]
    result = find_kate_exit(maze)
    print(result)


