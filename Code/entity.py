#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple[int, int]):
        self.name = name
        self.surf = pygame.image.load(f'./Asset/{name}.png').convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.topleft = position
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
