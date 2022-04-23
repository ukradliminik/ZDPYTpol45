from typing import Union, List


def nested_lists_flattener_gen(nested_list):
    '''
    Takes a (deeply)nested list and returns a flattened one as a generator
    '''
    for lst in nested_list:
        if isinstance(lst, list):
            yield from nested_lists_flattener(lst)
        else:
            yield lst


def nested_lists_flattener(nested_list):
    return list(nested_lists_flattener_gen(nested_list))


a = [1, [2, [3, 4]], 5, [6, 7], 8, [9, []]]


def make_flat_list(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return make_flat_list(list_of_lists[0]) + make_flat_list(list_of_lists[1:])
    return list_of_lists[:1] + make_flat_list(list_of_lists[1:])


def flatten_list(lst: List[Union[List, int]]) -> List[int]:
    if not lst:
        return []

    result = []
    for element in lst:
        if isinstance(element, int):
            result.append(element)
        else:
            result += flatten_list(element)

    return result

print(flatten_list(a))