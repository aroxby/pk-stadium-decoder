#!/usr/bin/env python3
from enum import Enum


class Type(Enum):
    NORMAL = 0
    FIGHTING = 1
    FLYING = 2
    POISON = 3
    GROUND = 4
    ROCK = 5
    BIRD = 6
    BUG = 7
    GHOST = 8
    FIRE = 20
    WATER = 21
    GRASS = 22
    ELECTRIC = 23
    PSYCHIC = 24
    ICE = 25
    DRAGON = 26

    def __str__(self):
        MAPPING = {
            self.BIRD: 'Bird',
            self.BUG: 'Bug',
            self.ELECTRIC: 'Electric',
            self.FIGHTING: 'Fighting',
            self.FIRE: 'Fire',
            self.FLYING: 'Flying',
            self.GHOST: 'Ghost',
            self.GRASS: 'Grass',
            self.GROUND: 'Ground',
            self.ICE: 'Ice',
            self.NORMAL: 'Normal',
            self.POISON: 'Poison',
            self.PSYCHIC: 'Psychic',
            self.ROCK: 'Rock',
            self.WATER: 'Water',
        }
        name = MAPPING.get(self, f'<Type {self.value}>')
        return name
