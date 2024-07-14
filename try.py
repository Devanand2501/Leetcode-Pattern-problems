
from collections import deque

def min_turns_to_top(n, H, X, heights, slips):
    queue = deque([(0, X)])  # (turns, current_height)
    visited = set()
    visited.add((X, 0))
    
    while queue:
        turns, current_height = queue.popleft()
        
        # Check if we have reached the top of any tree
        if current_height >= H:
            return turns
        
        # Calculate the next heights for jumping up and slipping down
        jump_up = current_height + heights[turns % n]
        slip_down = max(current_height - slips[turns % n], 0)
        
        # If jumping up reaches or exceeds the height, return the current number of turns + 1
        if jump_up >= H:
            return turns + 1
        
        # Add the next positions to the queue if not visited
        if (jump_up, turns + 1) not in visited:
            queue.append((turns + 1, jump_up))
            visited.add((jump_up, turns + 1))
        
        if (slip_down, turns + 1) not in visited:
            queue.append((turns + 1, slip_down))
            visited.add((slip_down, turns + 1))
    
    # If we cannot reach the top of any tree, return -1
    return -1

# Example usage:
n = 6
H = 10
X = 3
heights = [4, 3, 1, 1, 5, 2]
slips = [1, 1, 1, 1, 1, 1]
result = min_turns_to_top(n, H, X, heights, slips)
print(result)  # Output should be 7
























'''
def add_parentheses(expression):
    def helper(expr):
        if expr.isdigit():
            return [expr]
        
        results = []
        for i in range(len(expr)):
            if expr[i] in '+-*/':
                left_expr = helper(expr[:i])
                right_expr = helper(expr[i+1:])
                
                for l in left_expr:
                    for r in right_expr:
                        results.append(f'({l}{expr[i]}{r})')
        
        return results

    # Get all combinations of the expression with parentheses
    return helper(input1)

# Example usage:
input1 = "5*3/7-3"
# input1 = "9-7*4"
result = add_parentheses(input1)
print(result)


'''
























'''
def find_b(input2, input3):
    n = len(input2)
    
    # If input3 is greater than the sum of all elements in a, return -1
    if input3 > sum(input2):
        return -1
    
    b = [0] * n
    
    # Iterate over the bit positions from high to low
    for bit in range(31, -1, -1):
        current_sum = sum(input2[i] & b[i] for i in range(n))
        
        if current_sum + (1 << bit) <= input3:
            for i in range(n):
                if input2[i] & (1 << bit):
                    b[i] |= (1 << bit)
                    current_sum += (1 << bit)
                    if current_sum == input3:
                        return b
    return b if sum(input2[i] & b[i] for i in range(n)) == input3 else -1

# Example usage:
a = [1, 4,4,4]
# a = [1,2,3,4]
x = 2
result = find_b(a, x)
print(result)  # Output should be [1, 2, 3] or -1 if no valid combination exists

'''