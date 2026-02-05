class Solution {
    public int finalPositionOfSnake(int n, List<String> commands) {
        int answer = 0;

        for (String command : commands){
            if (command.equals("RIGHT")){
                answer += 1;
            }
            else if (command.equals("LEFT")){
                answer -= 1;
            }
            else if (command.equals("DOWN")){
                answer += n;
            }
            else {   // UP
                answer -= n;
            }
        }
        return answer;
    }
}
