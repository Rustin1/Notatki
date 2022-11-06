from typing import Any


class TreeNode:
    value: Any
    children = []

    def is_leaf(self):
        return len(self.children) == 0

    def add(self, child: 'TreeNode'):
        new = TreeNode()
        new.value = child
        new.children = []
        self.children.append(new)

    def for_each_deep_first(self, visit):
        visit(self)
        for child in self.children:
            child.for_each_deep_first(visit)

    def for_each_level_order(self, visit):
        children = [self]
        for child in children:
            for childs_child in child:
                children.append(childs_child)

        for child in children:
            visit(child)

    def search(self, value):
        if self.value == value:
            return self
        for child in self.children:
            return child.search(value)
        return False

    def __str__(self):
        children = [self]
        for child in children:
            for childs_child in child.children:
                print(childs_child.value)
                children.append(childs_child)
        values = []
        for child in children:
            values.append(child.value)
        return str(values)
