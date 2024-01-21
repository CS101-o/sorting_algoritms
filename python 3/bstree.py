import config
import time

class bstree:
    def __init__(self, value=None):
        self.verbose = config.verbose
        self.value = value
        self.left = None
        self.right = None
        self.insert_comparisons = 0
        self.find_comparisons = 0
        self.insert_count = 0
        self.find_count = 0

    def tree(self):
        return self.value is not None

    def insert(self, value):
        if self.tree():
            self.insert_comparisons += 1
            if value < self.value:
                if self.left is None:
                    self.left = bstree(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = bstree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value
            self.left = None
            self.right = None
        self.insert_count += 1

    def find(self, value):
        self.find_count += 1
        if self.tree():
            self.find_comparisons += 1
            if value == self.value:
                return True
            elif value < self.value and self.left is not None:
                return self.left.find(value)
            elif value > self.value and self.right is not None:
                return self.right.find(value)
        return False

    def height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))

    def print_set(self):
        if self.left:
            self.left.print_set()
        if self.tree():
            print(self.value)
        if self.right:
            self.right.print_set()

    def print_stats(self):

        start_time = time.perf_counter()
        # Perform the operation here
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Operation took {elapsed_time} seconds")

        tree_height = self.height(self)
        avg_insert_cmp = self.insert_comparisons / self.insert_count if self.insert_count > 0 else 0
        avg_find_cmp = self.find_comparisons / self.find_count if self.find_count > 0 else 0
        print(f"Height of the tree: {tree_height}, Avg insert comparisons: {avg_insert_cmp:.2f}, Avg find comparisons: {avg_find_cmp:.2f}")

