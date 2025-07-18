from Code.entity import Entity
from const import ENTITY_SPEED


class EnemyShot(Entity):

     def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

     def move(self):
         self.rect.centerx -= ENTITY_SPEED[self.name]
