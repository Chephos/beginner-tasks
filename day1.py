redundant_list =['a','b','a','a',3,3,2,'hello','b']


def optimise_list(lists):
    """Transform a redundant list to a non redundant one."""
    optimised_list = []
    sets = set(lists)
    while sets:
        """Transfer the set elements into the empty list."""
        new_list=sets.pop()
        optimised_list.append(new_list)
        
    return print(optimised_list)

optimise_list(redundant_list)