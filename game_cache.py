cache = {'2020-12-29': '2020-12-29 | Denver Nuggets: 115 - Sacramento Kings: 125\n\nMinutes: 13:34\nPoints: 1 \nRebounds: 2\nAssists: 5\nSteals: 2\nBlocks: 0\nTurnovers: 3\nField Goal: 0/3\n3-Point Field Goal: 0/3\nFree throw: 1/2'}

def is_game_cached(date):
    return date in cache.keys()

def get_cached_game(date):
    return cache[date]