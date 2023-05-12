import time
import tkinter as tk

window = tk.Tk()

coordinates = {}


def draw_tree(graph, start, canvas, x, y, x_gap, y_gap):
    for i in range(len(graph[start])):
        if i == 0:
            canvas.create_line(x, y, x - x_gap, y + y_gap)
            draw_tree(
                graph, graph[start][i], canvas, x - x_gap, y + y_gap, x_gap / 2, y_gap
            )
        if i == 1:
            canvas.create_line(x, y, x + x_gap, y + y_gap)
            draw_tree(
                graph, graph[start][i], canvas, x + x_gap, y + y_gap, x_gap / 2, y_gap
            )

    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="white")
    canvas.create_text(x, y, text=str(start))
    coordinates[start] = {
        "x": x - 10,
        "y": y - 10,
        "x_gap": x + 10,
        "y_gap": y + 10,
    }


def dls(graph, source, goal, visited, limit=2):
    stack = []

    stack.append({"data": source, "depth": 0})
    while len(stack) > 0:
        current = stack.pop()
        canvas.create_oval(
            coordinates[current["data"]]["x"],
            coordinates[current["data"]]["y"],
            coordinates[current["data"]]["x_gap"],
            coordinates[current["data"]]["y_gap"],
            fill="yellow",
        )
        canvas.create_text(
            coordinates[current["data"]]["x"] + 10,
            coordinates[current["data"]]["y"] + 10,
            text=str(current["data"]),
        )
        window.update()
        time.sleep(1)
        if current["data"] not in visited:
            visited.append(current["data"])
        if current["data"] == goal:
            return True
        if current["depth"] < limit:
            for child in reversed(graph[current["data"]]):
                if child not in visited:
                    visited.append(child)
                    stack.append({"data": child, "depth": current["depth"] + 1})

    return False


def main():
    # Create a binary tree
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": ["G"],
        "G": [],
    }

    # Draw tree
    draw_tree(graph, "A", canvas, 400, 50, 200, 100)
    # Perform DLS traversal
    visited = []
    depth = 2
    search = dls(graph, "A", "G", visited, depth)

    i = 0
    if search == False:
        canvas.create_text(
            400 + 20 * i, 460, text="Goal node not found within limit", fill="black"
        )
    else:
        # Highlight visited nodes
        while i < len(visited):
            node = visited[i]
            canvas.create_oval(
                (400 + 20 * i) - 10, 450, (400 + 20 * i) + 10, 470, fill="yellow"
            )
            canvas.create_text(400 + 20 * i, 460, text=str(node), fill="black")
            i += 1


# Create tkinter window and canvas

window.title("Depth Limited search")
canvas = tk.Canvas(window, width=800, height=500)
canvas.pack()

# Call main function and start tkinter event loop
main()
window.mainloop()
