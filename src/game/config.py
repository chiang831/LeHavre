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
