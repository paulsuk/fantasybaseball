import auth
import pdb

from constants.enums import BaseballPositionType, Sport
from constants.strings import BASE_URI
from models.utils import make_league_code, make_team_code, make_player_code, get_fantasy_content

class Player(object):
	'''
	@param data, data from yahoo API
	TODO: possibly make this a separate init like _init_from_yahoo
	TODO: will need to refactor/abstract out player class as an interface, with baseball implementation
	'''
	def __init__(self, y, data):
		self.yahoo_player_key = data['player_key']
		self.yahoo_id = data['player_id']

		# TODO: will probably have to do more differentiation here, especially for accents for weird players
		self.name = data['name']['full']

		# might want to split this into all available positions, or grab 'eligible positions'
		# pdb.set_trace()
		self.positions = self._parse_positions(data['display_position'])

		'''
		create a new session, get stats from yahoo, may need to be associated with League for league cat settings
		dates might support for a given week, or individual day, ideally in 7 day increments
		'''

	def _get_yahoo_stats(self, sport, league_id, dates=None):
		pass

	def _parse_positions(self, data):
		self.positions = data

class BaseballPlayer(Player):
	def __init__(self, y, data):
		super().__init__(y, data)
		self.position_type = BaseballPositionType(data['position_type'])

	def _parse_positions(self, data):
		self.positions = data

	def _get_yahoo_stats(self, league_id, dates=None):
		# TODO: PASS DOWN LEAGUE CATS AND THEN PARSE THE DATA
		y = auth.get_yahoo_session()
		url = "{}/league/{}/players;player_keys={}/stats".format(BASE_URI, make_league_code(Sport.MLB, league_id), self.yahoo_player_key)
		data = get_fantasy_content(y, url)['league']['players']['player']['player_stats']['stats']['stat']
		self.stats = {}
		for stat in data:
			self.stats[stat['stat_id']] = stat['value']


if __name__ == "__main__":
	print("howdy")