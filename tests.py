import unittest
import commands


class CommandSuite(unittest.TestCase):

    def test_today_has_a_game(self):
        result = commands.today_command('2021-01-19')
        home_team = 'Denver Nuggets'
        visitor = 'Oklahoma City Thunder'
        status = '9:00 PM ET'
        self.assertEqual(f'{commands.GAME_FOUND_PREFIX}{visitor} @ {home_team}. {status}.',result)
    
    def test_today_has_no_game(self):
        result = commands.today_command('2021-01-18')
        self.assertEqual(commands.NO_GAME_MSG,result)

if __name__ == '__main__':
    unittest.main()