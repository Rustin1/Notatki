import TreeNode


class Tree:
    root: TreeNode

    def add(self, value, parent_name):
        self.root.search(parent_name).add(value)

    def for_each_level_order(self, visit):
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit):
        self.root.for_each_deep_first(visit)

    def show(self):
        return
