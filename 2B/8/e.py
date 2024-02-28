# E. Дерево Хаффмана

from dataclasses import dataclass
from enum import Enum


class Type(Enum):
    ROOT = 0
    LEFT = 1
    RIGHT = 2


@dataclass
class Node:
    type: Type
    parent: 'Node' = None
    left: 'Node' = None
    right: 'Node' = None


def make_tree(traversal: str) -> Node:
    root = Node(type=Type.ROOT)

    now = root
    for t in traversal:
        if t == 'D':
            new = Node(type=Type.LEFT, parent=now)
            now.left = new
            now = now.left
        else:
            while now.type == Type.RIGHT:
                now = now.parent
            now = now.parent
            new = Node(type=Type.RIGHT, parent=now)
            now.right = new
            now = now.right

    return root


def solution(tree: Node) -> list[str]:
    def traverse(node: Node, code: list[str]):
        if node.left is None and node.right is None:
            answer.append(''.join(code))
            return

        code.append('0')
        traverse(node.left, code)
        code.pop()

        code.append('1')
        traverse(node.right, code)
        code.pop()

    answer = []
    traverse(tree, [])

    return answer


n = int(input())
for _ in range(n):
    tree = make_tree(input())
    answer = solution(tree)
    print(len(answer))
    print('\n'.join(answer))
