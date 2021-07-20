import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import os

players = pd.read_csv("emlemmon.github.io/python/Week12/basketball_players.csv")
#print(players) 
#print(players.columns)
min = players["points"].min()
max = players["points"].max()
mean = players["points"].mean()
median = players["points"].median()

print("Points per season: Min:{}, Max:{}, Mean:{:.2f}, Median:{}".format(min, max, mean, median))
#print(players.sort_values("points", ascending=False).head(10))
#print(players[["playerID", "year", "tmID", "points"]].sort_values("points", ascending=False).head(10))

#####  Points per season: Min:0, Max:4029, Mean:492.13, Median:329.0  #####
#####  2078   1961     Wilt   Chamberlain  PHW    4029 (highest number of points scored in a single season and who did it and when)  #####

master = pd.read_csv("emlemmon.github.io/python/Week12/basketball_master.csv")

# We can do a left join to "merge" these two datasets together
nba = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")
#print(nba.columns)

#print(nba[["year", "useFirst", "lastName", "tmID", "points"]].sort_values("points", ascending=False).head(10))

#sns.boxplot(data=nba.points)
#sns.boxplot(data=nba[["points", "assists", "rebounds"]])
#plt.show()
low_memory=False
#nba_grouped_year = nba[["points", "year"]].groupby("year").median()
#print(nba_grouped_year)

#nba_grouped_year = nba_grouped_year.reset_index()
#sns.regplot(data=nba_grouped_year, x="year", y="points")
#plt.show()

#print(nba.columns)
#print(nba[["year", "useFirst", "lastName", "points", "rebounds", "blocks", "assists", "fgAttempted", "fgMade"]].sort_values("points", ascending=False).head(15))
top35 = nba[["year", "useFirst", "lastName", "points", "fgMade", "fgAttempted"]].sort_values("points", ascending=False).head(35)
#print(top35)

topPoints = top35.drop_duplicates(subset="useFirst", keep="first").head(10)
#print(topPoints)
topPoints["fgPercentage"] = topPoints["fgMade"] / topPoints["fgAttempted"]
#print(topPoints[["useFirst", "lastName", "fgPercentage"]].sort_values("fgPercentage", ascending=False))
#print(topPoints[["useFirst", "lastName", "fgPercentage", "points"]].sort_values("points", ascending=False))

topRebounds = nba[["year", "useFirst", "lastName", "rebounds"]].sort_values("rebounds", ascending=False).head(35)
top10Rebounds = topRebounds.drop_duplicates(subset="useFirst", keep="first").head(10)
#print(top10Rebounds)

topPoint = nba[["year", "useFirst", "lastName", "points"]].sort_values("points", ascending=False).head(35)
top10Point = topPoint.drop_duplicates(subset="useFirst", keep="first").head(10)
#print(top10Point)

topBlocks = nba[["year", "useFirst", "lastName", "blocks"]].sort_values("blocks", ascending=False).head(35)
top10Blocks = topBlocks.drop_duplicates(subset="useFirst", keep="first").head(10)
#print(top10Blocks)

topAssists = nba[["year", "useFirst", "lastName", "assists"]].sort_values("assists", ascending=False).head(35)
top10Assists = topAssists.drop_duplicates(subset="useFirst", keep="first").head(10)
#print(top10Assists)

topSteals = nba[["year", "useFirst", "lastName", "steals"]].sort_values("steals", ascending=False).head(35)
top10Steals = topSteals.drop_duplicates(subset="useFirst", keep="first").head(10)
#print(top10Steals)

topThreeMade = nba[["year", "useFirst", "lastName", "threeMade"]].sort_values("threeMade", ascending=False).head(35)
top10ThreeMade = topThreeMade.drop_duplicates(subset="useFirst", keep="first").head(10)
print(top10ThreeMade)

       year useFirst    lastName  threeMade
18202  2005      Ray       Allen        269
13692  1995   Dennis       Scott        267
13573  1995   George     McCloud        257
19600  2007    Jason  Richardson        243
17589  2003     Peja  Stojakovic        240
13338  1995   Mookie    Blaylock        231
14095  1996   Reggie      Miller        229
17946  2004     Kyle      Korver        226
19489  2007  Rashard       Lewis        226
18070  2004  Quentin  Richardson        226