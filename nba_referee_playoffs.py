from bs4 import BeautifulSoup
from lxml import html
import pandas as pd 
import requests



dataFrameConstructor = {
	"REFEREE":[],
	"TYPE":[],
	"EXPERIENCE(Yrs)":[],
	"GAMES OFFICIATED":[],
	"HOME TEAM WIN%":[],
	"HOME TEAM POINTS DIFFERENTIAL":[],
	"TOTAL POINTS PER GAME":[],
	"CALLED FOULS PER GAME":[],
	"FOUL% AGAINST ROAD TEAMS":[],
	"FOUL% AGAINST HOME TEAMS":[],
	"FOUL DIFFERENTIAL":[]
}


url='https://www.nbastuffer.com/2019-2020-nba-referee-stats/'
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")
ref_table = soup.find('tbody')
#print(ref_table)

rows = ref_table.find_all('tr')

for ref in rows:
	ref_name = ref.find('td',class_="column-2").text.strip()
	dataFrameConstructor['REFEREE'].append(ref_name)
	ref_type = ref.find('td',class_="column-3").text.strip()
	dataFrameConstructor['TYPE'].append(ref_type)
	ref_exp = ref.find('td',class_="column-4").text.strip()
	dataFrameConstructor["EXPERIENCE(Yrs)"].append(ref_exp)
	ref_games = ref.find('td',class_="column-5").text.strip()
	dataFrameConstructor["GAMES OFFICIATED"].append(ref_games)
	home_team_win = ref.find('td',class_="column-6").text.strip()
	dataFrameConstructor["HOME TEAM WIN%"].append(home_team_win)
	home_team_pts_diff = ref.find('td',class_="column-7").text.strip()
	dataFrameConstructor["HOME TEAM POINTS DIFFERENTIAL"].append(home_team_pts_diff)
	total_points_per_game = ref.find('td',class_="column-8").text.strip()
	dataFrameConstructor["TOTAL POINTS PER GAME"].append(total_points_per_game)
	called_fouls_per_game = ref.find('td',class_="column-9").text.strip()
	dataFrameConstructor["CALLED FOULS PER GAME"].append(called_fouls_per_game)
	foul_percent_agnst_road = ref.find('td',class_="column-10").text.strip()
	dataFrameConstructor["FOUL% AGAINST ROAD TEAMS"].append(foul_percent_agnst_road)
	foul_percent_agnst_home = ref.find('td',class_="column-11").text.strip()
	dataFrameConstructor["FOUL% AGAINST HOME TEAMS"].append(foul_percent_agnst_home)
	foul_differential = ref.find('td',class_="column-12").text.strip()
	dataFrameConstructor["FOUL DIFFERENTIAL"].append(foul_differential)

	#print(ref_name)
	#print(ref_type)
	#print(ref_exp)
	#print(ref_games)

dataframe = pd.DataFrame(dataFrameConstructor)
print(dataframe)


'''

Stats Updated  
<'div', class_="x-alert x-alert-muted x-alert-block">

soup.find('tbody') #table 

soup.find_all('tr',class_="row-2 even")  #role="row"
	.find('td',class_="column-1")     
	.find('td',class_="column-2")
	.find('td',class_="column-3")
	.find('td',class_="column-4")
	.find('td',class_="column-5")
	
'''