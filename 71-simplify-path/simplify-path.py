class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split('/'):
            if part == '' or part == '.': # represents current directory or extra slashes
                continue
            elif part == '..': # go one level up
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        
        return '/' + '/'.join(stack)