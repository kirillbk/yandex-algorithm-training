# D. Бинарное дерево (вставка, поиск, обход)

from dataclasses import dataclass
from sys import stdin
from typing import Any


@dataclass
class Node:
    key: Any
    left: "Node" = None
    right: "Node" = None


class BinaryTree:
    def __init__(self) -> None:
        self._root: Node = None

    def __str__(self) -> str:
        def _tree_traverse(node: Node, depth: int) -> str:
            if not node:
                return
            _tree_traverse(node.left, depth + 1)
            tree.append("." * depth + str(node.key))
            _tree_traverse(node.right, depth + 1)

        tree = []
        _tree_traverse(self._root, 0)
        return "\n".join(tree)

    def add(self, key: Any) -> bool:
        if not self._root:
            self._root = Node(key)
            return True

        node = self._root
        while node:
            if key < node.key:
                if not node.left:
                    node.left = Node(key)
                    return True
                node = node.left
            elif key > node.key:
                if not node.right:
                    node.right = Node(key)
                    return True
                node = node.right
            else:
                return False

    def search(self, key: Any) -> bool:
        node = self._root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return True
        return False


tree = BinaryTree()
for line in stdin:
    cmd, *arg = line.split()
    match cmd:
        case "ADD":
            key = int(arg[0])
            print("DONE" if tree.add(key) else "ALREADY")
        case "SEARCH":
            key = int(arg[0])
            print("YES" if tree.search(key) else "NO")
        case "PRINTTREE":
            print(tree)
        case _:
            raise RuntimeError()
