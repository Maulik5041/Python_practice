# Approach 1: Sorting
# Time Complexity: O(n log n)


# Space Complexity: O(1)
def is_perm_1(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))

    n = len(str_1)

    for i in range(n):
        if str_1[i] != str_2[i]:
            return False
    return True


# Approach 2: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_perm_2(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    d = dict()

    for i in str_1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in str_2:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1

    # all() function returns True if all items in an iterable are True
    return all(value == 0 for value in d.values())


VALID_PERM_1 = "google"
VALID_PERM_2 = "ooggle"

INVALID_PERM_1 = "not"
INVALID_PERM_2 = "top"

print(is_perm_1(VALID_PERM_1, VALID_PERM_2))
print(is_perm_1(INVALID_PERM_1, INVALID_PERM_2))

print(is_perm_2(VALID_PERM_1, VALID_PERM_2))
print(is_perm_2(INVALID_PERM_1, INVALID_PERM_2))
