import time
import tkinter as tk

window = tk.Tk()

coordinates = {}

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": ["L", "M"],
    "G": ["N", "O"],
    "H": ["P"],
    "I": [],
    "J": [],
    "K": ["Q"],
    "L": [],
    "M": [],
    "N": [],
    "O": [],
    "P": [],
    "Q": [],
}

source_queue = list()
last_node_queue = list()

source_visited = {}
last_node_visited = {}

source_parent = {}
last_node_parent = {}


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


def get_neighbors(node):
    neighbors_arr = set()
    for key in graph.keys():
        if key == node:
            for node_key in graph[key]:
                neighbors_arr.add(node_key)
        if node in graph[key]:
            neighbors_arr.add(key)

    return list(neighbors_arr)


def path_st(intersecting_node, source, last_node):
    path = list()
    path.append(intersecting_node)
    i = intersecting_node

    while i != source:
        path.append(source_parent[i])
        i = source_parent[i]

    path = path[::-1]
    i = intersecting_node

    while i != last_node:
        path.append(last_node_parent[i])
        i = last_node_parent[i]

    path = list(map(str, path))

    for i in range(len(path)):
        canvas.create_oval(
            coordinates[path[i]]["x"],
            coordinates[path[i]]["y"],
            coordinates[path[i]]["x_gap"],
            coordinates[path[i]]["y_gap"],
            fill="yellow",
        )
        canvas.create_text(
            coordinates[path[i]]["x"] + 10,
            coordinates[path[i]]["y"] + 10,
            text=str(path[i]),
        )
        window.update()
        time.sleep(1)

        canvas.create_oval(
            coordinates[path[len(path) - i - 1]]["x"],
            coordinates[path[len(path) - i - 1]]["y"],
            coordinates[path[len(path) - i - 1]]["x_gap"],
            coordinates[path[len(path) - i - 1]]["y_gap"],
            fill="yellow",
        )
        canvas.create_text(
            coordinates[path[len(path) - i - 1]]["x"] + 10,
            coordinates[path[len(path) - i - 1]]["y"] + 10,
            text=str(path[len(path) - i - 1]),
        )
        window.update()
        time.sleep(1)

        if i >= len(path)/2:
            break
    return path


def breadth_fs(direction="forward"):
    if direction == "forward":
        current = source_queue.pop(0)
        neighbors = get_neighbors(current)

        for node in neighbors:
            if not node in source_visited.keys():
                source_queue.append(node)
                source_visited[node] = True
                source_parent[node] = current
    else:
        current = last_node_queue.pop(0)
        neighbors = get_neighbors(current)

        for node in neighbors:
            if not node in last_node_visited.keys():
                last_node_queue.append(node)
                last_node_visited[node] = True
                last_node_parent[node] = current


def is_intersecting():
    nodes = "A B C D E F G H I J K L M N O P Q".split(" ")
    for node in nodes:
        if (
            node in source_visited.keys()
            and source_visited[node]
            and node in last_node_visited.keys()
            and last_node_visited[node]
        ):
            return node

    return -1


def bidi(start, goal):
    source_queue.append(start)
    source_visited[start] = True
    source_parent[start] = -1

    last_node_queue.append(goal)
    last_node_visited[goal] = True
    last_node_parent[goal] = -1

    while source_queue and last_node_queue:
        breadth_fs(direction="forward")

        breadth_fs(direction="backward")

        intersecting_node = is_intersecting()

        if intersecting_node != -1:
            print(f"Path exists between {start} and {goal}")
            print(f"Intersection at : {intersecting_node}")
            path = path_st(intersecting_node, start, goal)
            return True, path
    return False


def main():
    # Create a binary tree

    # Draw tree
    draw_tree(graph, "A", canvas, 400, 50, 200, 100)
    # Perform BIDI traversal
    search, path = bidi("P", "O")

    i = 0
    if search == False:
        canvas.create_text(
            400 + 20 * i, 460, text="Goal node not found within limit", fill="black"
        )
    else:
        # Highlight visited nodes
        while i < len(path):
            node = path[i]
            canvas.create_oval(
                (400 + 20 * i) - 10, 500, (400 + 20 * i) + 10, 520, fill="yellow"
            )
            canvas.create_text(400 + 20 * i, 510, text=str(node), fill="black")
            i += 1


# Create tkinter window and canvas

window.title("Bidirectional search")
canvas = tk.Canvas(window, width=800, height=800)
canvas.pack()

# Call main function and start tkinter event loop
main()
window.mainloop()
