class Node(object):
    """A node in a tree"""

    def __init__(self, data, children=None):
        self.data = data
        if children is None:
            self.children = []
        else:
            self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node %s>" % self.data

    def breadth_first_search(self, data):
        to_visit = [self]

        while to_visit:
            current = to_visit.pop(0)

            if current.data == data:
                return current

            to_visit.extend(current.children)

    def depth_first_search(self, data):
        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)


if __name__ == '__main__':

    resume = Node("resume.txt")
    recipes = Node("recipes.txt")
    jane = Node("jane/", [resume, recipes])
    server = Node("server.py")
    jessica = Node("jessica/", [server])
    users = Node("Users/", [jane, jessica])
    root = Node("/", [users])


    print root.breadth_first_search("resume.txt")
    print root.depth_first_search('recipes.txt')

    crabbe = Node("Crabbe", [])
    seamus = Node("Seamus", [])
    neville = Node("Neville", [])
    parvati = Node("Parvati", [])
    lavender = Node("Lavender", [])
    malfoy = Node("Malfoy", [crabbe])
    ron = Node("Ron", [seamus, neville])
    hermione = Node("Hermione", [parvati, lavender])
    padma = Node("Padma", [])
    snape = Node("Snape", [malfoy])
    mcgonagall = Node("McGonagall", [ron, hermione])
    flitwick = Node("Flitwick", [padma])
    dumbledore = Node("Dumbledore", [snape, mcgonagall, flitwick])

    print dumbledore.breadth_first_search("Crabbe")
    print dumbledore.depth_first_search("Crabbe")