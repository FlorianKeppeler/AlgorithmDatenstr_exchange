
from dataclasses import dataclass
from typing import Optional

type T = int | float


@dataclass
class Node[T]:

    key_: T
    left_: Optional["Node[T]"] = None
    right_: Optional["Node[T]"] = None
    parent_: T = 0


type BTree = Optional[Node[T]]


ar = [14, 15, 9, 16, 17, 19, 18, 1, 12, 1, 4, 4, 11, 5, 8, 20, 7, 6, 13, 3, 10, 2]

ar2 = [8.45, 13.49, 12.01, 19.62, 1.60, 2.63, 15.30, 9.54, 3.48, 0.62, 17.68, 10.57, 0.51, 16.93, 18.50, 17.31, 6.40, 5.80, 8.07, 18.11]


def insert(tree: BTree, x: T) -> None:

    match tree:
        case Node(m, l, r):
            if m is None:
                tree.key_ = x
                tree.parent_ = 0
                return
            if m == x:
                return
            else:
                if x < m:
                    if l is None:
                        tree.left_ = Node(x)
                        tree.left_.parent_ = m
                    else:
                        insert(l, x)
                else:
                    if r is None:
                        tree.right_ = Node(x)
                        tree.right_.parent_ = m
                    else:
                        insert(r, x)


def inorder(tree: BTree) -> list[T]:

    match tree:
        case Node(m, l, r):
            return inorder(l) + [m] + inorder(r)
        case None:
            return []


def closest(tree: BTree) -> tuple[T, T]:

    ar_sort = inorder(tree)

    prev = abs(ar_sort[1] - ar_sort[0])  # just to initialize with some value
    res = (ar_sort[0], ar_sort[1])       # and save current pair

    for i in range(2, len(ar_sort)):
        tmp = abs(ar_sort[i] - ar_sort[i - 1])

        if tmp < prev:
            prev = tmp
            res = (ar_sort[i - 1], ar_sort[i])

    return res


def path(tree: BTree, prev: list[T]) -> list[list[T]]:

    tmp = []

    match tree:
        case Node(m, l, r):
            if l is None and r is None:
                return [prev + [m]]
            else:
                prev += [m]
                tmp = path(l, prev)
                tmp += path(r, prev)
                return tmp

        case None:
            return []


def weight(tree: BTree) -> list[T]:

    paths = path(tree, [0])

    tmp_max = sum(paths[0])
    res = paths[0]

    for i in range(1, len(paths)):
        if sum(paths[i]) > tmp_max:
            tmp_max = sum(paths[i])
            res = paths[i]

    return res[1:]


def closest_ar(ar: list[T]) -> tuple[T, T]:

    prev = abs(ar[1] - ar[0])   # just to initialize with some value
    res = (ar[0], ar[1])        # and save current pair

    for j in range(len(ar)):

        for i in range(j + 1, len(ar)):
            tmp = abs(ar[i] - ar[j])
            if tmp < prev:
                prev = tmp
                res = (ar[j], ar[i])

    return res


t = Node(None)

for x in ar:
    insert(t, x)

# print(inorder(t))
# print(closest(t))
print(t)
# print(closest_ar(ar2))
print(weight(t))
# print(sum(ar))
