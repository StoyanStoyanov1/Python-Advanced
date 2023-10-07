from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    WEIGHT = 7
    POSSIBLE_SERVICE = "SecondaryService"

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=self.WEIGHT)

    def eating(self):
        self.weight += 1
