canvas = [
            ['b', 'b', 'r', 'r'],
            ['b', 'b', 'b', 'r'],
            ['g', 'g', 'g', 'b'],
            ['g', 'g', 'g', 'r'],
            ['g', 'w', 'g', 'r']
        ]

def get_color(v, h):
    """Gets the color at a given coordinate"""

    color = canvas[v][h]

    if color == 'w':
        return None

    return color

# color = get_color(2, 1)
# print color

def get_neighbors(v, h):
    """Gets all tuples representing coordinates of neighboring canvas points."""
    coord = canvas[v][h]
    neighbors = []
    off_grid = [-1, len(canvas) + 1]

    coords_to_check = [(v + 1, h),
                       (v - 1, h),
                       (v, h + 1),
                       (v, h - 1)
                      ]
    for coord in coords_to_check:
        if coord[0] in off_grid or coord[1] in off_grid:
            continue
        neighbors.append(coord)

    return neighbors

# print get_neighbors(0, 1)


def paint(v, h, color, canvas):
    """Given a coordinate and a color, paint that coordinate and all coordinates
    touching the given coordinate that are the same color as the original coordinate
    the given color
    """

    box_color = get_color(v, h)

    if box_color == color:
        return canvas

    canvas[v][h] = color
    neighbors = get_neighbors(v, h)

    while neighbors:
        to_check = neighbors.pop()
        if canvas[to_check[0]][to_check[1]] == box_color:
            canvas[to_check[0]][to_check[1]] = color
            neighbors += get_neighbors(*to_check)

    for line in canvas:
        print line

def paint_recursive(v, h, new_color, canvas, start_color=None):
    if start_color is None:
        start_color = get_color(v, h)
    if v < 0 or v > 4 or h < 0 or h > 4:
        return
    if start_color != get_color(v, h):
        return
    else:
        canvas[v][h] = new_color
        paint_recursive(v-1, h, new_color, canvas, start_color)
        paint_recursive(v+1, h, new_color, canvas, start_color)
        paint_recursive(v, h-1, new_color, canvas, start_color)
        paint_recursive(v, h+1, new_color, canvas, start_color)

# paint(1, 1, 'r', canvas)
for array in canvas:
    print array
paint_recursive(1, 1, 'r', canvas)

print "\n\n\n\n\n\n"
for line in canvas:
    print line


