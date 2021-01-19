import requests
import clock
import json
import api_ids as ids

START_MSG = 'Hi. I am CampaBot(BETA Version). I will keep you updated about Facundo Campazzo NBA games. Please go to /help to find what can I do for you.'
HELP_MSG = 'Commands available: \n/today - checks if today Denver is playing \n/stats - gives the stats for Campazzo in a given day\n/season - all Facu games in the season\n/about - about this bot\n/feedback - tell us what you think'
ABOUT_MSG = 'This bot is in BETA Version. No optimizations are being made. All the data is from https://rapidapi.com/theapiguy/api/free-nba (unofficial).'
NO_GAME_MSG = 'No luck, Culeao!!'
FEEDBACK_MSG = 'Give us feedback in our public channel: https://t.me/CampaBotFeedback'
RESPONSE_ERROR = 'Something went wrong. We dropped the ball.'
GAME_FOUND_PREFIX = """YES!! Let's make a Fernet and cheer for Facu. """

headers_for_all_req={'x-rapidapi-key': '0fe22cb13emshb468f395b7d2b7fp13c79cjsnb5e281bc6f44', 'x-rapidapi-host': 'free-nba.p.rapidapi.com', 'useQueryString': 'true'}

def start_command():
    return START_MSG

def help_command():
    return HELP_MSG

def stats_command():
    return "Not implemented yet"

def season_command():
    return "Not implemented yet"

def about_command():
    return ABOUT_MSG

def feedback_command():
    return FEEDBACK_MSG

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
        return RESPONSE_ERROR
    elif data.__len__() == 1:
        home_team = data[0]['home_team']['full_name']
        visitor = data[0]['visitor_team']['full_name']
        status = data[0]['status']
        return f'{GAME_FOUND_PREFIX}{visitor} @ {home_team}. {status}.'
    else:
        return NO_GAME_MSG