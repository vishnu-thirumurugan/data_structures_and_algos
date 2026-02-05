class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:

        answer = 0

        for command in commands:
            if command == 'RIGHT':
                answer += 1
            elif command == 'LEFT':
                answer -= 1
            elif command == 'DOWN':
                answer += n
            else:
                answer -= n

        return answer

            
        