from commands.CommonCommand import CommonCommand
from entities.Points import Points


class ShowAllPointCommand(CommonCommand):
    def __init__(self, menu_point, point_storage: Points) -> None:
        super().__init__(menu_point, 'Показать точки')
        self.point_storage = point_storage

    def run(self):
        self.point_storage.show_all()
