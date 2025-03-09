from collections import deque

def water_jug_solver(jug1, jug2, goal):
    queue = deque([(0, 0, [])])  # Initial state with empty jugs
    visited = set()
    
    while queue:
        x, y, path = queue.popleft()
        
        # If we reach the goal, print the solution steps
        if x == goal or y == goal:
            print("Solution found:")
            for i, (rule, (a, b)) in enumerate(path):
                print(f"Step {i+1}: {rule} -> ({a}, {b})")
            return
        
        # Possible moves
        moves = [
            ("Fill jug1", (jug1, y)),
            ("Fill jug2", (x, jug2)),
            ("Empty jug1", (0, y)),
            ("Empty jug2", (x, 0)),
            ("Pour jug1 into jug2", (x - min(x, jug2 - y), y + min(x, jug2 - y))),
            ("Pour jug2 into jug1", (x + min(y, jug1 - x), y - min(y, jug1 - x)))
        ]
        
        for rule, (new_x, new_y) in moves:
            if (new_x, new_y) not in visited:
                queue.append((new_x, new_y, path + [(rule, (new_x, new_y))]))
                visited.add((new_x, new_y))
    
    print("No solution found.")

def main():
    jug1 = int(input("Enter the capacity of jug1: "))
    jug2 = int(input("Enter the capacity of jug2: "))
    goal = int(input("Enter the target amount: "))
    water_jug_solver(jug1, jug2, goal)

if __name__ == "__main__":
    main()