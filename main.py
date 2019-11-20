import auth
from flask import Flask
import pdb

from collections import defaultdict
from constants.enums import Sport
from models.league import League


LEAGUES = {
	2019	:	90555,
	2018	:	18039,
	2017	:	60085,
	2016	:	37796,
}

DESIRED_YEAR = 2019

app = Flask(__name__)

@app.route("/")
def initialize_data():
	league_id = LEAGUES[DESIRED_YEAR]	
	sport = Sport.MLB

	league = League(sport, league_id)
	pdb.set_trace()
	return "hello christina"

if __name__ == "__main__":
	# TODO: investigate, can we use UserCollection to get all available leagues
	print("howdy")