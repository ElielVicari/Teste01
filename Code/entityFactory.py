#!/usr/bin/python
# -*- coding: utf-8 -*-

from const import WIN_WIDTH
from Code.background import Background  # ajuste o caminho se necessário

class EntityFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
             case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
        return list_bg