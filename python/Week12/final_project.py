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
nba_grouped_year = nba[["points", "year"]].groupby("year").median()
print(nba_grouped_year)

nba_grouped_year = nba_grouped_year.reset_index()
sns.regplot(data=nba_grouped_year, x="year", y="points")
plt.show()