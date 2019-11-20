from models.player import Player, BaseballPlayer
from models.utils import make_league_code, make_team_code, get_fantasy_content

class Team(object):
	'''
	@param y, yahoo session
	@param url, url to get team data from
	'''
	def __init__(self, y, url):
		self.base_url = url

		data = get_fantasy_content(y, url)['team']
		self.id = data['team_id']
		self.name = data['name']

		self._get_roster(y)

	def _get_roster(self, y):
		self.roster = []
		roster_url = "{}/roster/players".format(self.base_url)
		players = get_fantasy_content(y, roster_url)['team']['roster']['players']
		for player_data in players['player']:
			# may need to do some async work here or db work
			player = BaseballPlayer(y, player_data)
			self.roster.append(player)

	'''
		get stats from yahoo, for entire year aggregated, may need some league settings thing
	'''
	def _get_total_stats(self, dates=None):
		pass

	def _get_yahoo_stats_for_roster(self, league_id):
		for player in self.roster:
			player._get_yahoo_stats(league_id)

if __name__ == "__main__":
	print("howdy")