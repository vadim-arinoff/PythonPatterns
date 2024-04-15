from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def display(self):
        pass

class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Leaf: {self.name}")

class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, child):
        self.children.append(child)

    def display(self):
        print(f"Composite: {self.name}")
        for child in self.children:
            child.display()

# Пример
root = Composite("root")
leaf1 = Leaf("leaf1")
leaf2 = Leaf("leaf2")
root.add(leaf1)
root.add(leaf2)

subcomp = Composite("subcomp")
leaf3 = Leaf("leaf3")
leaf4 = Leaf("leaf4")
subcomp.add(leaf3)
subcomp.add(leaf4)
root.add(subcomp)

root.display()