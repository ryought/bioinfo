"""
dfs.py

depth first search for 2-tree
"""

def solve_with_relax(param):
    # param = {1:1, 2:0, 3:1}
    print('not ywe')

# f:: (1, 0, -1, -1) -> (1, 0, 1, -1) and (1, 0, 0, -1)
def branch(position):
    try:
        i = position.index(-1)

        # deep copy https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
        n1, n2 = list(position), list(position)
        n1[i] = 1
        n2[i] = 0
        return [n1, n2]

    except ValueError:
        return []


print(branch([1, 0, 1, 1]))


# FIX: 0 or 1, UNFIXED: -1
def dfs():
    stack = []
    stack.append([-1,-1,-1,-1])

    while stack:
        x = stack.pop()
        print('processing', x)
        next_pos = branch(x)
        stack.extend(next_pos)


dfs()
