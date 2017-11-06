from swiglpk import *
from dfs import branch

def solve_with_relax(lp2, bound):
    lp = glp_create_prob()
    glp_copy_prob(lp, lp2, GLP_ON)
    # bound = (0, 1, -1, -1, -1)
    for i, value in enumerate(bound):
        if value == 0 or value == 1:
            # print('x({0}) was bounded to {1}'.format(i+1, value))
            # i th column has fixed value
            glp_set_col_bnds(lp, i+1, GLP_FX, value, value)
        else:
            print('x({0}) was unfixed'.format(i+1))
            # value == -1 and unfixed
            # glp_set_col_bnds(lp, i+1, GLP_LO, 0, 0)
    # solve
    glp_simplex(lp, None)

    result = []
    for i in range(glp_get_num_cols(lp)):
        result.append(glp_get_col_prim(lp, i+1))

    status = glp_get_status(lp)
    if status == GLP_OPT:
        # optimal solution found
        opt = glp_get_obj_val(lp)
        glp_delete_prob(lp)
        return (opt, result)
    else:
        # not optimal
        glp_delete_prob(lp)
        return ()

def is_satisfies_binary_constraint(solution):
    for i in solution:
        if not(i == 1 or i == 0):
            return False
    return True

def is_leaf_node(x):
    for i in x:
        if not(i == 1 or i == 0):
            return False
    return True

def main():
    lp = glp_create_prob()
    glp_read_lp(lp, None, "data2.txt")

    # init = [-1, -1, ... (repeated for numbers of variables)]
    init = [-1 for _ in range(glp_get_num_rows(lp))]

    stack = []
    stack.append(init)

    leaf_LBs = []
    max_leaf_LB = 0

    while stack:
        x = stack.pop()
        print('processing', x)
        result = solve_with_relax(lp, x)
        if result:
            print('[**]', result[0], result[1])
            if is_leaf_node(x):
                # leaf node
                leaf_LBs.append(result)
                max_leaf_LB = max(leaf_LBs, key=lambda item: item[0])[0]

            else:
                # internal node
                opt_value = result[0]
                if opt_value < max_leaf_LB:
                    # prune
                    print('prune')
                elif is_satisfies_binary_constraint(result[1]):
                    print('found good solutino')
                else:
                    # branching
                    next_pos = branch(x)
                    stack.extend(next_pos)
        else:
            # cannot get optimal solution for relaxed subproblem
            # so dont have to branch to subproblem(s) of this subproblem
            print('not optimal, skip')

    glp_delete_prob(lp)
    print(leaf_LBs)


if __name__ == '__main__':
    main()
