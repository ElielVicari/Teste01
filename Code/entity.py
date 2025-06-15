#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from const import ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple[int, int]):
        self.name = name
        self.surf = pygame.image.load(f'./Asset/{name}.png').convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.topleft = position
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self, ):
        pass
