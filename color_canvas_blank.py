canvas = [
            ['b', 'b', 'r', 'r'],
            ['b', 'b', 'b', 'r'],
            ['g', 'g', 'g', 'b'],
            ['g', 'g', 'g', 'r'],
            ['g', 'w', 'g', 'r']
        ]

def get_color(v, h):
    """Gets the color at a given coordinate"""

    return canvas[v][h]

def get_neighbors(v, h):
    """Gets all tuples representing coordinates of neighboring canvas points."""

    neighbors = []
    out_of_bounds = [-1, len(canvas)+1]

    coordinates = [(v-1, h), # left
                  (v+1, h), # right
                  (v, h-1), # down
                  (v, h+1)]  # up

    for coord in coordinates:
        if coord[0] in out_of_bounds or coord[1] in out_of_bounds:
            continue
        neighbors.append(coord)

    return neighbors

def paint(v, h, color, canvas):
    """Given a coordinate and a color, paint that coordinate and all coordinates
    touching the given coordinate that are the same color as the original coordinate
    the given color
    """
    
    box_color = get_color(v, h)

    if box_color == color: #no need to paint
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
    pass


for array in canvas:
    print array

print "\n\n\n\n"

paint(1, 1, 'r', canvas)
# paint_recursive(1, 1, 'r', canvas)

# for line in canvas:
#     print line


