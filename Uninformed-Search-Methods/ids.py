import time
import tkinter as tk

window = tk.Tk()

coordinates = {}


def draw_tree(graph, visited, start, canvas, x, y, x_gap, y_gap):
    for i in range(len(graph[start])):
        current = graph[start][i]
        if current not in visited:
            visited.append(current)
            if i % 2 == 0:
                canvas.create_line(x, y, x - x_gap, y + y_gap)
                draw_tree(
                    graph,
                    visited,
                    current,
                    canvas,
                    x - x_gap,
                    y + y_gap,
                    x_gap / 2,
                    y_gap,
                )
            else:
                canvas.create_line(x, y, x + x_gap, y + y_gap)
                draw_tree(
                    graph,
                    visited,
                    current,
                    canvas,
                    x + x_gap,
                    y + y_gap,
                    x_gap / 2,
                    y_gap,
                )
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="white")
    canvas.create_text(x, y, text=str(start))
    coordinates[start] = {
        "x": x - 10,
        "y": y - 10,
        "x_gap": x + 10,
        "y_gap": y + 10,
    }


def DLS(graph, visited, src, target, maxDepth):
    if src not in visited:
        visited.append(src)
        canvas.create_oval(
            coordinates[src]["x"],
            coordinates[src]["y"],
            coordinates[src]["x_gap"],
            coordinates[src]["y_gap"],
            fill="yellow",
        )
        canvas.create_text(
            coordinates[src]["x"] + 10,
            coordinates[src]["y"] + 10,
            text=str(src),
        )
        window.update()
        time.sleep(1)

    if src == target:
        return True

    # If reached the maximum depth, stop recursing.
    if maxDepth <= 0:
        return False

    # Recur for all the vertices adjacent to this vertex
    for current in graph[src]:
        if DLS(graph, visited, current, target, maxDepth - 1):
            return True
    return False


def ids(graph, visited, source, target, maxDepth):
    for i in range(maxDepth + 1):
        if DLS(graph, visited, source, target, i):
            return True
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
    draw_visited = []
    draw_tree(graph, draw_visited, "A", canvas, 400, 50, 200, 100)
    # Perform BFS traversal
    visited = []
    depth = 2
    search = ids(graph, visited, "A", "F", depth)

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

window.title("Iterative Deepening Search")
canvas = tk.Canvas(window, width=800, height=500)
canvas.pack()

# Call main function and start tkinter event loop
main()
window.mainloop()
