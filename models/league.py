import auth
from collections import defaultdict
import time

from constants.strings import BASE_URI
from models.team import Team
from models.utils import make_league_code, make_team_code, get_fantasy_content

class League(object):
	def __init__(self, sport, league_id):
		# League id used in uri to get league data
		self.league_id = league_id
		self.sport = sport
		y = auth.get_yahoo_session()

		self._get_league_data(y)

	'''
	Get league data and initializes them
	@param y: yahoo session
	'''
	def _get_league_data(self, y):
		url = "{}/league/{}/settings".format(BASE_URI, make_league_code(self.sport, self.league_id))
		data = get_fantasy_content(y, url)['league']

		self.league_name = data['name']
		self._process_league_settings(data['settings'])
		num_teams = int(data['num_teams'])
		print("PROCESSING_TEAM_DATA")
		start = time.time()
		self._get_teams_data(y, num_teams)
		end = time.time()
		print("PROCESSED TEAM DATA IN {} SECONDS".format(end-start))
		print("GETTING_ROSTERS")
		for team in self.teams:
			team._get_yahoo_stats_for_roster(self.league_id)

	def _get_teams_data(self, y, num_teams):
		self.teams = []
		for i in range(1, num_teams + 1):
			url = "{}/team/{}".format(BASE_URI, make_team_code(self.sport, self.league_id, i))
			team = Team(y, url)
			self.teams.append(team)

	def _process_league_settings(self, settings):
		position_settings = settings['roster_positions']['roster_position']
		position_settings = filter(lambda position : 'position_type' in position.keys(), position_settings)
		self.league_positions = {}
		for position in position_settings:
			position_name = position.pop('position')
			self.league_positions[position_name] = position

		category_settings = settings['stat_categories']['stats']['stat']
		category_settings = filter(lambda category : 'is_only_display_stat' not in category.keys(), category_settings)

		self.categories = defaultdict(list)
		for category in category_settings:
			cat = {k : category[k] for k in ["stat_id", "display_name", "position_type"]}
			position_type = cat.pop('position_type')
			self.categories[position_type].append(cat)

if __name__ == "__main__":
	print("howdy")