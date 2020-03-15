class CommonCommand:
    def __init__(self, point, menu_name) -> None:
        self.point = point
        self.__menu_name__ = menu_name

    def menu_name(self):
        return self.__menu_name__

    def get_point(self):
        return self.point
