def truncated_discrete_distribution(
    mean: int, stddev: int, minimum: int | None = None, maximum: int | None = None,
) -> int:
    """ not a "real" distribution, the discretization and clamping skew it """
    import random
    result = round(random.gauss(mean, stddev))
    if minimum and result < minimum:
        return truncated_discrete_distribution(mean, stddev, minimum, maximum)
    if maximum and result > maximum:
        return truncated_discrete_distribution(mean, stddev, minimum, maximum)
    return result
