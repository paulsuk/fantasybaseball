import xmltodict

def make_league_code(sport, league_id):
	'''
	@param sport: Enum of type Sport
	@param league_id: league id, some int
	'''
	return "{}.l.{}".format(sport.name, league_id)

def make_team_code(sport, league_id, team_id):
	'''
	@param sport: Enum of type Sport
	@param league_id: league id, some int
	@param team_id: team id, some int in range 1-NUM_TEAMS
	'''
	return "{}.t.{}".format(make_league_code(sport, league_id), team_id)

def make_player_code(sport, player_id):
	return "{}.p.{}".format(sport.name, player_id)

def get_fantasy_content(y, url):
	raw = y.get(url)
	return xmltodict.parse(raw.text)['fantasy_content']

if __name__ == "__main__":
	print("howdy")