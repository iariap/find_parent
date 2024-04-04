class File:
    def __init__(self, name: str):
        self.children = []
        self.name = name

    def add_child(self, file):
        self.children.append(file)

    def __repr__(self) -> str:
        return f"{self.name} -> {self.children}"


def get_path(from_file: File, to_file: File) -> list[File]:
    # are we there?
    if from_file == to_file:
        return [from_file]
    else:
        # iterate over the children list
        for child in from_file.children:
            path = get_path(child, to_file)
            # we found a way to our destination, so we add it to our path and return it
            if path:
                return [from_file] + path

        # no path found this way
        return []


def find_parent(root: File, a: File, b: File):
    # we get the paths from root to to both files
    path_to_a = get_path(root, a)
    path_to_b = get_path(root, b)

    parent = None
    for element_a, element_b in zip(path_to_a, path_to_b):
        if element_a == element_b:
            parent = element_b
        else:
            break

    return parent


"""
Example input

root ->
  a ->
    c
    d
  b    
"""

root = File("root")
a, b, c, d = map(File, "abcd")

root.add_child(a)
root.add_child(b)
a.add_child(c)
a.add_child(d)

print(list(map(lambda c: c.name, get_path(root, c))))

assert find_parent(root, a, b) == root
# //-> root

assert find_parent(root, c, d) == a
# //-> a


print(find_parent(root, b, c))
