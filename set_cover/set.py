states_needed = {'A','B', 'C', 'D', 'E'}

sets = {
    "s1": {'A', 'B', 'C'},
    "s2": {'A', 'D'},
    "s3": {'B', 'E'},
    "s4": {'C', 'D', 'E'}
}

final_sets = set()

while states_needed:

    best_set = None
    covered = set()

    for set_name, elements in sets.items():

        covered_now = states_needed & elements

        if len(covered_now) > len(covered):
            best_set = set_name
            covered = covered_now

    states_needed -= covered

    final_sets.add(best_set)

print(final_sets)