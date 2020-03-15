from commands.CommonCommand import CommonCommand
from entities.Points import Points


class AddPointCommand(CommonCommand):

    def __init__(self, menu_point, point_storage: Points) -> None:
        super().__init__(menu_point, 'Добавить точку')
        self.point_storage = point_storage

    def run(self):
        print("Enter point")
        self.point_storage.add_point()
