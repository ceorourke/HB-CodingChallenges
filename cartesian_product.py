def make_cartesian_product(input):
    """Constructs the cartesian product - hard coded for depth of 3"""

    output = []   

    # for i in input[0]:
    #     for j in input[1]:
    #         for k in input[2]:
    #             output.append((i,j,k))
    for i in range(len(input)-1):
        for j in range(len(input[i])):
            for k in range(len(input[i+1])):
                output.append((input[i][j], input[i+1][k]))
    return output

    
# def make_cartesian_product_recursive(input):
#     """Constructs the cartesian product - recursive answer for any depth"""
    
#     if not input:
#         return [()]

#     output = []
#     # recursively loop over lists
#     for x in make_cartesian_product_recursive(input[:-1]):
#         # loop through the element in the last list each time
#         for y in input[-1]:
#             # add tuples to output
#             output.append(x + (y,))
#     return output


input = [[1,2,3],[4,5]]

print make_cartesian_product(input)
# print make_cartesian_product_recursive(input)


# output should be:
# [(1,4,6), (1,4,7), (1,4,8), (1,5,6), (1,5,7), (1,5,8),
#  (2,4,6), (2,4,7), (2,4,8), (2,5,6), (2,5,7), (2,5,8),
#  (3,4,6), (3,4,7), (3,4,8), (3,5,6), (3,5,7), (3,5,8)] 