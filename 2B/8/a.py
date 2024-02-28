# A. Бинарное дерево (вставка, поиск, обход)

from sys import stdin
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: Any
    left: 'Node' = None
    right: 'Node' = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def __str__(self) -> str:
        def in_order(node: Node, depth: int):
            if node is None:
                return
            in_order(node.left, depth + 1)
            tree.append('.' * depth + str(node.value))
            in_order(node.right, depth + 1)

        tree = []
        in_order(self.root, 0)
        return '\n'.join(tree)

    def add(self, value: Any) -> bool:
        if self.root is None:
            self.root = Node(value)
            return True

        node = self.root
        while True:
            if node.value == value:
                return False
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    return True
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    return True
                node = node.right

    def search(self, value: Any) -> bool:
        node = self.root
        while node is not None:
            if node.value == value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return False


tree = BinaryTree()
for line in stdin:
    q = line.split()
    match q[0]:
        case 'ADD':
            if tree.add(int(q[1])):
                print('DONE')
            else:
                print('ALREADY')
        case 'SEARCH':
            if tree.search(int(q[1])):
                print('YES')
            else:
                print('NO')
        case 'PRINTTREE':
            print(tree)
