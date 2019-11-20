from enum import Enum

class Sport(Enum):
	# Maps sport to league_id
	MLB = "mlb"
	NBA = "nba"
	NHL = "nhl" 

class BaseballPositionType(Enum):
	PITCHER = "P"
	BATTER = "B"

if __name__ == "__main__":
	print("howdy")