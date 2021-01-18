import requests
import clock
import json
import api_ids as ids

NO_GAME_MSG = 'No luck Culeao!!'
RESPONSE_ERROR = 'Something went wrong. We drop the ball.'
GAME_FOUND_PREFIX = """YES!! Let's make a Fernet for that game. """

headers_for_all_req={'x-rapidapi-key': '0fe22cb13emshb468f395b7d2b7fp13c79cjsnb5e281bc6f44', 'x-rapidapi-host': 'free-nba.p.rapidapi.com', 'useQueryString': 'true'}

def today_command(now=clock.now()):
    response = requests.get(
        'https://free-nba.p.rapidapi.com/games', 
        headers= headers_for_all_req,
        params={
            'team_ids[]':ids.team_id, 
            'dates[]':f'{now}{ids.date_prefix}',
            'seasons[]':ids.default_season})
    result = json.loads(response.text)
    data = result['data']
    if response.status_code != 200 :
        return ""
    elif data.__len__() == 1:
        home_team = data[0]['home_team']['full_name']
        visitor = data[0]['visitor_team']['full_name']
        status = data[0]['status']
        return f'{GAME_FOUND_PREFIX}{visitor} @ {home_team}. {status}.'
    else:
        return NO_GAME_MSG