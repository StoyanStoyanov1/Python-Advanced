from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    WEIGHT = 9
    POSSIBLE_SERVICE = "MainService"

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=self.WEIGHT)

    def eating(self):
        self.weight += 3
