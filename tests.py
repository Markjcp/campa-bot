import unittest
import commands
import teams


class CommandSuite(unittest.TestCase):

    def test_team_ids(self):
        self.assertEqual(teams.get_team(1),'Atlanta Hawks')
        self.assertEqual(teams.get_team(2),'Boston Celtics')
        self.assertEqual(teams.get_team(3),'Brooklyn Nets')
        self.assertEqual(teams.get_team(4),'Charlotte Hornets')
        self.assertEqual(teams.get_team(5),'Chicago Bulls')
        self.assertEqual(teams.get_team(6),'Cleveland Cavaliers')
        self.assertEqual(teams.get_team(7),'Dallas Mavericks')
        self.assertEqual(teams.get_team(8),'Denver Nuggets')
        self.assertEqual(teams.get_team(9),'Detroit Pistons')
        self.assertEqual(teams.get_team(10),'Golden State Warriors')
        self.assertEqual(teams.get_team(11),'Houston Rockets')
        self.assertEqual(teams.get_team(12),'Indiana Pacers')
        self.assertEqual(teams.get_team(13),'LA Clippers')
        self.assertEqual(teams.get_team(14),'Los Angeles Lakers')
        self.assertEqual(teams.get_team(15),'Memphis Grizzlies')
        self.assertEqual(teams.get_team(16),'Miami Heat')
        self.assertEqual(teams.get_team(17),'Milwaukee Bucks')
        self.assertEqual(teams.get_team(18),'Minnesota Timberwolves')
        self.assertEqual(teams.get_team(19),'New Orleans Pelicans')
        self.assertEqual(teams.get_team(20),'New York Knicks')
        self.assertEqual(teams.get_team(21),'Oklahoma City Thunder')
        self.assertEqual(teams.get_team(22),'Orlando Magic')
        self.assertEqual(teams.get_team(23),'Philadelphia 76ers')
        self.assertEqual(teams.get_team(24),'Phoenix Suns')
        self.assertEqual(teams.get_team(25),'Portland Trail Blazers')
        self.assertEqual(teams.get_team(26),'Sacramento Kings')
        self.assertEqual(teams.get_team(27),'San Antonio Spurs')
        self.assertEqual(teams.get_team(28),'Toronto Raptors')
        self.assertEqual(teams.get_team(29),'Utah Jazz')
        self.assertEqual(teams.get_team(30),'Washington Wizards')

    def test_today_has_a_game(self):
        result = commands.today_command('2021-01-19')
        home_team = 'Denver Nuggets'
        visitor = 'Oklahoma City Thunder'
        status = 'Final'
        self.assertEqual(f'{commands.GAME_FOUND_PREFIX}{visitor} @ {home_team}. {status}.',result)
    
    def test_today_has_no_game(self):
        result = commands.today_command('2021-01-18')
        self.assertEqual(commands.NO_GAME_MSG,result)

    def test_stats_game_day(self):
        result = commands.stats_command('2021-01-03')
        self.assertEqual('2021-01-03 | Denver Nuggets: 124 - Minnesota Timberwolves: 109\n\nMinutes: 21:24\nPoints: 15 \nRebounds: 1\nAssists: 2\nSteals: 3\nBlocks: 1\nTurnovers: 1\nField Goal: 5/8\n3-Point Field Goal: 5/7\nFree throw: 0/0',result)

    def test_stats_no_game(self):
        result = commands.stats_command('2021-01-22')
        self.assertEqual(commands.NO_GAME_MSG,result)
    
    def test_stats_future_game(self):
        result = commands.stats_command('2050-01-22')
        self.assertEqual(commands.DATE_IN_THE_FUTURE,result)

    def test_stats_bad_format(self):
        result = commands.stats_command('[YYYY-MM-DD]')
        self.assertEqual(commands.INVALID_DATE_MSG,result)
    
    def test_stats_no_date(self):
        result = commands.stats_command('')
        self.assertEqual(commands.NO_DATE,result)

if __name__ == '__main__':
    unittest.main()