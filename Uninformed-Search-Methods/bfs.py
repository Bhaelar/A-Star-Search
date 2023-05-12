import time
import tkinter as tk

window = tk.Tk()

coordinates = {}


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def draw_tree(node, canvas, x, y, x_gap, y_gap):
    if node.left:
        canvas.create_line(x, y, x - x_gap, y + y_gap)
        draw_tree(node.left, canvas, x - x_gap, y + y_gap, x_gap / 2, y_gap)
    if node.right:
        canvas.create_line(x, y, x + x_gap, y + y_gap)
        draw_tree(node.right, canvas, x + x_gap, y + y_gap, x_gap / 2, y_gap)

    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="white")
    canvas.create_text(x, y, text=str(node.data))
    coordinates[node.data] = {
        "x": x - 10,
        "y": y - 10,
        "x_gap": x + 10,
        "y_gap": y + 10,
    }


def bfs(node, goal, visited):
    queue = []
    queue.append(node)

    while queue:
        current = queue.pop(0)
        visited.append(current)
        canvas.create_oval(
            coordinates[current.data]["x"],
            coordinates[current.data]["y"],
            coordinates[current.data]["x_gap"],
            coordinates[current.data]["y_gap"],
            fill="yellow",
        )
        canvas.create_text(
            coordinates[current.data]["x"] + 10,
            coordinates[current.data]["y"] + 10,
            text=str(current.data),
        )
        window.update()
        time.sleep(1)

        if current.data == goal:
            return True

        if current.left:
            if current.left not in visited:
                queue.append(current.left)

        if current.right:
            if current.right not in visited:
                queue.append(current.right)
    return False


def main():
    # Create a binary tree
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    root.left.left = Node("D")
    root.left.right = Node("E")
    root.right.left = Node("F")
    root.right.right = Node("G")

    # Draw tree
    draw_tree(root, canvas, 400, 50, 200, 100)
    # Perform BFS traversal
    visited = []

    search = bfs(root, "G", visited)
    i = 0
    if search == False:
        canvas.create_text(400 + 20 * i, 460, text="Goal node not found", fill="black")
    else:
        # Highlight visited nodes
        while i < len(visited):
            node = visited[i]
            canvas.create_oval(
                (400 + 20 * i) - 10, 450, (400 + 20 * i) + 10, 470, fill="yellow"
            )
            canvas.create_text(400 + 20 * i, 460, text=str(node.data), fill="black")
            i += 1


# Create tkinter window and canvas

window.title("Breadth first search")
canvas = tk.Canvas(window, width=800, height=500)
canvas.pack()

# Call main function and start tkinter event loop
main()
window.mainloop()
