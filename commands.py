import requests
import clock
import json
import teams
import game_cache
import api_ids as ids

START_MSG = 'Hi. I am CampaBot(BETA Version). I will keep you updated about Facundo Campazzo NBA games. Please go to /help to find what can I do for you.'
HELP_MSG = 'Commands available: \n/today - checks if today Denver is playing \n/stats - gives the stats for Campazzo in a given day[YYYYMMDD]\n/season - all Facu games in the season\n/about - about this bot\n/feedback - tell us what you think'
ABOUT_MSG = 'This bot is in BETA Version. No optimizations are being made. All the data is from https://rapidapi.com/theapiguy/api/free-nba (unofficial).'
NO_GAME_MSG = 'No luck, Culeao. I could not find a game.'
FEEDBACK_MSG = 'Give us feedback in our public channel: https://t.me/CampaBotFeedback'
RESPONSE_ERROR = 'Something went wrong. I dropped the ball.'
GAME_FOUND_PREFIX = """YES!! Let's make a Fernet and cheer for Facu. """
INVALID_DATE_MSG= 'Oh, I am expecting the date in YYYYMMDD format. You dropped the ball.'
DATE_IN_THE_FUTURE='That date is in the future man. Facu is the wizard but I am not.'
NO_DATE="You didn't give me a date to find. I am expecting it in YYYYMMDD format. Write the command and the date with a space or with underscore. For example /stats_20210103"

headers_for_all_req={'x-rapidapi-key': 'XXX', 'x-rapidapi-host': 'free-nba.p.rapidapi.com', 'useQueryString': 'true'}

def takeFirst(elem):
    return elem[0]

def start_command():
    return START_MSG

def help_command():
    return HELP_MSG

def season_command():
    response = requests.get(
        'https://free-nba.p.rapidapi.com/games', 
        headers= headers_for_all_req,
        params={
            'team_ids[]':ids.team_id, 
            'page':ids.page,
            'per_page':ids.per_page, 
            'seasons[]':ids.default_season})
    json_response = json.loads(response.text)
    data = json_response['data']
    if response.status_code != 200 :
        return RESPONSE_ERROR
    elif len(data) >= 1:
        result = []
        for d in data:
            if d['status'] == 'Final':
                id = d['id']
                date = d['date'][:10]
                transformed_date = clock.remove_separators(date)
                home_team = d['home_team']['full_name']
                visitor_team = d['visitor_team']['full_name']
                home_team_score = d['home_team_score']
                visitor_team_score = d['visitor_team_score']
                line = f'{date}\t{visitor_team}: {visitor_team_score} - {home_team}: {home_team_score}-> /stats_{transformed_date}'
                result.append((transformed_date,line))
        result.sort(key=takeFirst)
        command_result = ''
        for res in result:
            command_result += (res[1] + '\n\n')
        return command_result
    else:
        return NO_GAME_MSG

def stats_command(input_date):
    if input_date == '':
        return NO_DATE

    if not clock.validate(input_date):
        return INVALID_DATE_MSG

    date = clock.transform_date_time_format(input_date)

    if clock.after(date,clock.now()):
        return DATE_IN_THE_FUTURE
    
    if game_cache.is_game_cached(date):
        return game_cache.get_cached_game(date)

    response = requests.get(
        'https://free-nba.p.rapidapi.com/stats', 
        headers= headers_for_all_req,
        params={
            'team_ids[]':ids.team_id, 
            'player_ids[]':ids.player_id,
            'page[]':ids.page,
            'per_page[]':ids.per_page, 
            'dates[]':f'{date}{ids.date_prefix}',
            'seasons[]':ids.default_season})
    result = json.loads(response.text)
    data = result['data']
    if response.status_code != 200 :
        return RESPONSE_ERROR
    elif len(data) == 1:
        try:
            home_team = teams.get_team(data[0]['game']['home_team_id'])
            home_team_score = data[0]['game']['home_team_score']
            visitor = teams.get_team(data[0]['game']['visitor_team_id'])
            visitor_team_score = data[0]['game']['visitor_team_score']
            game_date = data[0]['game']['date'][:10]
            minutes = data[0]['min']
            points = data[0]['pts']
            assist = data[0]['ast']
            rebound = data[0]['reb']
            steals = data[0]['stl']
            turnover = data[0]['turnover']
            blk = data[0]['blk']
            fga = data[0]['fga']
            fgm = data[0]['fgm']
            fg3a = data[0]['fg3a']
            fg3m = data[0]['fg3m']
            fta = data[0]['fta']
            ftm = data[0]['ftm']
            return f'{game_date} | {visitor}: {visitor_team_score} - {home_team}: {home_team_score}\n\nMinutes: {minutes}\nPoints: {points} \nRebounds: {rebound}\nAssists: {assist}\nSteals: {steals}\nBlocks: {blk}\nTurnovers: {turnover}\nField Goal: {fgm}/{fga}\n3-Point Field Goal: {fg3m}/{fg3a}\nFree throw: {ftm}/{fta}'
        except ValueError:
            return RESPONSE_ERROR
    else:
        return NO_GAME_MSG

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
    elif len(data) == 1:
        home_team = data[0]['home_team']['full_name']
        visitor = data[0]['visitor_team']['full_name']
        status = data[0]['status']
        return f'{GAME_FOUND_PREFIX}{visitor} @ {home_team}. {status}.'
    else:
        return NO_GAME_MSG