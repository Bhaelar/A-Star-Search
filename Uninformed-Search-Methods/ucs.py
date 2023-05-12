import time
from cmath import inf
import tkinter as tk

window = tk.Tk()

coordinates = {
    "A": {"x": 100, "y": 200},
    "B": {"x": 200, "y": 50},
    "C": {"x": 300, "y": 200},
    "D": {"x": 400, "y": 50},
    "E": {"x": 500, "y": 200},
    "F": {"x": 300, "y": 150},
}


def draw_tree(canvas):
    x1, y1 = 100, 200
    x2, y2 = 200, 50
    x3, y3 = 300, 200
    x4, y4 = 400, 50
    x5, y5 = 500, 200
    x6, y6 = 300, 150

    # draw edges
    canvas.create_line(x1 + 10, y1, x2 - 10, y2)
    canvas.create_text(((x1 + x2) / 2) - 10, (y1 + y2) / 2, text="9")

    canvas.create_line(x1 + 10, y1, x3 - 10, y3)
    canvas.create_text(((x1 + x3) / 2), ((y1 + y3) / 2) - 10, text="4")

    canvas.create_line(x2 + 10, y2 + 5, x3 - 10, y3)
    canvas.create_text(((x2 + x3) / 2) + 10, ((y2 + y3) / 2), text="2")

    canvas.create_line(x2 + 10, y2, x4 - 10, y4)
    canvas.create_text(((x2 + x4) / 2), ((y2 + y4) / 2) - 10, text="7")

    canvas.create_line(x2 + 10, y2, x5 - 10, y5)
    canvas.create_text(((x2 + x5) / 2) + 10, ((y2 + y5) / 2) - 10, text="3")

    canvas.create_line(x3 + 10, y3, x5 - 10, y5)
    canvas.create_text(((x3 + x5) / 2), ((y3 + y5) / 2) - 10, text="6")

    canvas.create_line(x4 + 10, y4 + 3, x5 - 10, y5 - 3)
    canvas.create_text(((x4 + x5) / 2) + 10, ((y4 + y5) / 2) - 10, text="4")

    canvas.create_line(x4 - 10, y4, x6 + 10, y6)
    canvas.create_text(((x4 + x6) / 2) - 10, ((y4 + y6) / 2) - 10, text="8")

    canvas.create_line(x5 - 10, y5, x6 + 10, y6)
    canvas.create_text(((x5 + x6) / 2) - 10, ((y5 + y6) / 2) - 10, text="2")

    # draw nodes
    canvas.create_oval(x1 - 10, y1 - 10, x1 + 10, y1 + 10)
    canvas.create_text(x1, y1, text="A")

    canvas.create_oval(x2 - 10, y2 - 10, x2 + 10, y2 + 10)
    canvas.create_text(x2, y2, text="B")

    canvas.create_oval(x3 - 10, y3 - 10, x3 + 10, y3 + 10)
    canvas.create_text(x3, y3, text="C")

    canvas.create_oval(x4 - 10, y4 - 10, x4 + 10, y4 + 10)
    canvas.create_text(x4, y4, text="D")

    canvas.create_oval(x5 - 10, y5 - 10, x5 + 10, y5 + 10)
    canvas.create_text(x5, y5, text="E")

    canvas.create_oval(x6 - 10, y6 - 10, x6 + 10, y6 + 10)
    canvas.create_text(x6, y6, text="F")


heuristics = {
    "A": inf,
    "B": inf,
    "C": inf,
    "D": inf,
    "E": inf,
    "F": inf,
}

parents = {
    "A": "",
    "B": "",
    "C": "",
    "D": "",
    "E": "",
    "F": "",
}

opened = []
closed = []
visiting = set()


def get_old_node(value):
    for node in opened:
        if heuristics[node] == value:
            return node
    return None


def get_neighbors(graph, node):
    neighbors = []
    for item in graph:
        if item == node:
            for adj in graph[item]:
                neighbors.append(adj)
        for adj in graph[item]:
            if list(adj.keys())[0] == item:
                neighbors.append({item, adj.values()[0]})
    return neighbors


def calculate_path(goal):
    path = [goal]
    current_node = parents[goal]
    while True:
        path.append(current_node)
        if parents[current_node] == "":
            break
        current_node = parents[current_node]
    path.reverse()
    return path


def calculate_distance(graph, parent, child):
    for neighbor in get_neighbors(graph, parent):
        if list(neighbor.keys())[0] == child:
            distance = heuristics[parent] + list(neighbor.values())[0]
            if distance < heuristics[child]:
                parents[child] = parent
                return distance
            return heuristics[child]


def remove_from_opened():
    opened.sort()
    node = opened.pop()
    closed.append(node)
    return node


def get_old_node(node):
    for item in opened:
        if item == node:
            return item
    return None


def ucs(graph, start, goal):
    heuristics[start] = 0
    opened.append(start)
    steps = 0

    while True:
        steps += 1
        if not opened:
            print(f"No solution found after {steps} steps")
            return False
        current_node = remove_from_opened()

        merged_list = closed
        i = 0
        while i in range(len(merged_list) - 1):
            if (
                merged_list[i] > merged_list[i + 1]
                and heuristics[merged_list[i]] > heuristics[merged_list[i + 1]]
            ):
                merged_list.pop(i)
                i = 0
            else:
                i += 1

        for key in list(coordinates.keys()):
            if key in merged_list:
                canvas.create_oval(
                    coordinates[key]["x"] - 10,
                    coordinates[key]["y"] - 10,
                    coordinates[key]["x"] + 10,
                    coordinates[key]["y"] + 10,
                    fill="yellow",
                )
                canvas.create_text(
                    coordinates[key]["x"],
                    coordinates[key]["y"],
                    text=str(key),
                )
            else:
                canvas.create_oval(
                    coordinates[key]["x"] - 10,
                    coordinates[key]["y"] - 10,
                    coordinates[key]["x"] + 10,
                    coordinates[key]["y"] + 10,
                    fill=window.cget("bg"),
                )
                canvas.create_text(
                    coordinates[key]["x"],
                    coordinates[key]["y"],
                    text=str(key),
                )
        window.update()
        time.sleep(1)

        if current_node == goal:
            path = calculate_path(goal)
            return True, path, heuristics[goal]
        child_nodes = graph[current_node]
        if len(child_nodes) > 0:
            for child_node in child_nodes:
                key = list(child_node.keys())[0]
                heuristics[key] = calculate_distance(graph, current_node, key)
                if key not in opened and key not in closed:
                    opened.append(key)
                elif key in opened and parents[key] != current_node:
                    old_node = get_old_node(key)
                    if heuristics[key] < heuristics[old_node]:
                        parents[key] = current_node
                        closed.append(key)


def main():
    graph = {
        "A": [{"B": 9}, {"C": 4}],
        "B": [{"A": 9}, {"C": 2}, {"D": 7}, {"E": 3}],
        "C": [{"A": 4}, {"B": 2}, {"E": 6}],
        "D": [{"B": 7}, {"E": 4}, {"F": 8}],
        "E": [{"B": 3}, {"C": 6}, {"D": 4}, {"F": 2}],
        "F": [{"D": 8}, {"E": 2}],
    }
    # Draw tree
    draw_tree(canvas)
    # Perform UCS traversal
    found, path, cost = ucs(graph, "A", "F")

    i = 0
    if found == False:
        canvas.create_text(400 + 20 * i, 460, text="Goal node not found", fill="black")
    else:
        # Highlight visited nodes
        while i < len(path):
            node = path[i]
            canvas.create_oval(
                (400 + 20 * i) - 10, 450, (400 + 20 * i) + 10, 470, fill="yellow"
            )
            canvas.create_text(400 + 20 * i, 460, text=str(node), fill="black")
            i += 1
        canvas.create_text(
            400 + 20, 480, text=f"Node found with cost: {cost}", fill="black"
        )


# Create tkinter window and canvas

window.title("Uniform Cost Search")
canvas = tk.Canvas(window, width=800, height=500)
canvas.pack()

# Call main function and start tkinter event loop
main()
window.mainloop()
