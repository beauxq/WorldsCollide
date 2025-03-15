# https://stackoverflow.com/a/12238093
# shuffle elements of given list that meet given condition
def shuffle_if(lst, condition):
    indices, elements = zip(*[(i, e) for i, e in enumerate(lst) if condition(e)], strict=False)
    indices = list(indices)

    import random
    random.shuffle(indices)

    for i, e in zip(indices, elements, strict=False):
        lst[i] = e
