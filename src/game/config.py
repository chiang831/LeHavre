"""This module provides game configs and constants."""
import collections

START_RESOURCES_PILES = dict(
    franc=2, fish=2, wood=2, clay=1)
LONG_GAME_STARTING_OFFER = dict(
    franc=2, fish=2, wood=2, clay=1)

RESOURCE_GENERATOR_DICTS = [
    dict(clay=1, wood=1),
    dict(wood=1, cattle=1),
    dict(fish=1, grain=1),
    dict(fish=1, wood=1),
    dict(clay=1, fish=1),
    dict(franc=1, wood=1),
    dict(franc=1, iron=1),
]

NUMBER_OF_TURNS = len(RESOURCE_GENERATOR_DICTS)

EndOfRound = collections.namedtuple('EndOfRound', ['food'])
END_OF_ROUND_DICT = {
    1: [
        EndOfRound(food=5),
        EndOfRound(food=10),
        EndOfRound(food=15),
        EndOfRound(food=20),
        EndOfRound(food=25),
        EndOfRound(food=30),
        EndOfRound(food=35),
    ],
    2: [
        EndOfRound(food=3),
        EndOfRound(food=4),
        EndOfRound(food=5),
        EndOfRound(food=7),
        EndOfRound(food=9),
        EndOfRound(food=11),
        EndOfRound(food=13),
        EndOfRound(food=15),
        EndOfRound(food=16),
        EndOfRound(food=17),
        EndOfRound(food=18),
        EndOfRound(food=19),
        EndOfRound(food=20),
        EndOfRound(food=20),
    ],
    3: [
        EndOfRound(food=2),
        EndOfRound(food=2),
        EndOfRound(food=3),
        EndOfRound(food=3),
        EndOfRound(food=4),
        EndOfRound(food=5),
        EndOfRound(food=6),
        EndOfRound(food=7),
        EndOfRound(food=8),
        EndOfRound(food=9),
        EndOfRound(food=10),
        EndOfRound(food=11),
        EndOfRound(food=12),
        EndOfRound(food=13),
        EndOfRound(food=14),
        EndOfRound(food=14),
        EndOfRound(food=15),
        EndOfRound(food=15),
    ],
    4: [
        EndOfRound(food=1),
        EndOfRound(food=1),
        EndOfRound(food=2),
        EndOfRound(food=2),
        EndOfRound(food=2),
        EndOfRound(food=3),
        EndOfRound(food=3),
        EndOfRound(food=4),
        EndOfRound(food=4),
        EndOfRound(food=5),
        EndOfRound(food=5),
        EndOfRound(food=6),
        EndOfRound(food=7),
        EndOfRound(food=8),
        EndOfRound(food=9),
        EndOfRound(food=10),
        EndOfRound(food=10),
        EndOfRound(food=11),
        EndOfRound(food=11),
        EndOfRound(food=11),
    ],
    5: [
        EndOfRound(food=0),
        EndOfRound(food=1),
        EndOfRound(food=1),
        EndOfRound(food=1),
        EndOfRound(food=1),
        EndOfRound(food=2),
        EndOfRound(food=2),
        EndOfRound(food=2),
        EndOfRound(food=2),
        EndOfRound(food=3),
        EndOfRound(food=3),
        EndOfRound(food=3),
        EndOfRound(food=4),
        EndOfRound(food=4),
        EndOfRound(food=4),
        EndOfRound(food=5),
        EndOfRound(food=5),
        EndOfRound(food=5),
        EndOfRound(food=6),
        EndOfRound(food=6),
    ],
}

STARTING_BUILDINGS = [
    'Building Firm 1',
    'Building Firm 2',
    'Construction Firm',
]
