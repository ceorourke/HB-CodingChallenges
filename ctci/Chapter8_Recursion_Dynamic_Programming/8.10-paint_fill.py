def paint_fill(image, col, row, color, orig_color):
    """Recursively fill a spot in a matrix with a new color"""

    if image[row][col] != orig_color:
        return
    if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
        return

    image[row][col] = color

    paint_fill(image, col - 1, row, color, orig_color)
    paint_fill(image, col + 1, row, color, orig_color)
    paint_fill(image, col, row - 1, color, orig_color)
    paint_fill(image, col, row + 1, color, orig_color)

    return


image = [['r', 'g', 'g', 'b'],
         ['r', 'o', 'o', 'b'],
         ['r', 'o', 'g', 'b'],
         ['r', 'o', 'o', 'b'],
         ['r', 'o', 'g', 'b'],
         ['r', 'w', 'g', 'b'],
        ]

paint_fill(image, 1, 2, 'p', 'o')

for row in image:
    print row