class StockSpanner:

    def __init__(self):
        self.stack = []
        # stack[-1][0] --> price
        # stack[-1][1] --> span
        
    def next(self, price: int) -> int:
        curr_span = 1
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            curr_span += prev_span
            
            
        self.stack.append([price, curr_span])
        return curr_span
        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)