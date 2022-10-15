from collections import defaultdict
from typing import Dict


def num_sum(num: int):
    return sum(map(int, str(num).split()))


def count_by_groups(n_customers: int) -> Dict[int, int]:
    groups = defaultdict(int)
    for id in range(n_customers):
        groups[num_sum(id) % 64] += 1
    return groups


# С параметром по-умолчанию равнозначна count_by_groups
def count_by_groups_with_first_id(n_customers: int, n_first_id: int = 0) -> Dict[int, int]:
    groups = defaultdict(int)
    for id in range(n_first_id, n_first_id + n_customers):
        groups[num_sum(id) % 64] += 1
    return groups


if __name__ == '__main__':
    print(count_by_groups(7000))
    print(count_by_groups_with_first_id(7000, 11111))
