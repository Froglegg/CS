from linkedStructures import Node


class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None) -> None:
        super().__init__(data, next=next)
        self.previous = previous
