class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])

        original_color = image[sr][sc]

        if original_color == color: # to prevent infinite loop
            return image 

        q = deque([(sr,sc)])
        image[sr][sc] = color
        while q:
            r, c = q.popleft()
            for dr, dc in [[0,1], [1,0], [-1,0], [0, -1]]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == original_color:
                    image[nr][nc] = color
                    q.append((nr, nc))

        return image


