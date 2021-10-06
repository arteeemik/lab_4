
# part 1
def has_empty_domains(csp) -> bool:
    for domain in csp.domains:
        if len(domain) == 0:
            return True
    return False

def check_all_constraints(csp) -> bool:
    if len(csp.constraints) == 0:
        return True

    for constraint in csp.get_all_constraints():
        if csp.get_assignment(constraint.var1) is None or csp.get_assignment(constraint.var2) is None:
            continue
        if not constraint.check(csp.get_assignment(constraint.var1), csp.get_assignment(constraint.var2)):
            return False

    return True

# part 2
def solve_constraint_dfs(problem):
    num = 0
    agenda = [problem]

    while len(agenda) > 0:
        p = agenda.pop(0)
        num += 1
        if not has_empty_domains(p) and check_all_constraints(p):
            unassigned_var = p.pop_next_unassigned_var()

            if unassigned_var is None:
                return p.assignments, num

            new_agenda = [p.copy().set_assignment(unassigned_var, value) for value in p.get_domain(unassigned_var)]
            new_agenda = new_agenda + agenda
            agenda = new_agenda
    return None, num

#part 3

def eliminate_from_neighbors(csp, var):
    dom = set()
    for nb in csp.get_neighbors(var):
        constraints_between = csp.constraints_between(nb, var)
        if len(constraints_between) > 1:
            return None
        else:
            for val1 in csp.get_domain(nb):
                count_errors = 0

                for val2 in csp.get_domain(var):
                    if not constraints_between[0].check(val1, val2):
                        count_errors += 1

                if count_errors == len(csp.get_domain(var)):
                    csp.eliminate(nb, val1)
                    if len(csp.get_domain(nb)) == 0:
                        return None
                    dom.add(nb)
    return sorted([*dom])


if __name__ == '__main__':


