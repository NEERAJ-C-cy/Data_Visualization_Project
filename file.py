import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv('IPL.csv')
#print(df.head())

#print(df.info())

print(f'your rows are {df.shape[0]} and columns are {df.shape[1]}')

#print(df.isnull().sum())

# 1.Which team has won the most matches?

match_wins = df['match_winner'].value_counts()
#sns.barplot(y=match_wins.index, x=match_wins.values, palette='viridis')

#plt.xlabel('Number of Matches Won')
#plt.ylabel('Teams')    
#plt.title('Most Successful IPL Teams')
#plt.savefig('most_successful_ipl_teams.png')


# Toss Decision Trends

#sns.countplot(data=df, x="toss_decision")
#plt.title("Toss Decision Trends")
# Save the figure correctly using matplotlib
#plt.savefig("Toss_Decision_Trends.png", bbox_inches="tight")



#Toss Decision vs Match Winner
count = df[df['toss_winner'] == df['match_winner']]['match_id'].count()

percentage = (count* 100)/df.shape[0]
print(f'Number of matches where toss winner also won the match: {count}')
print(f'Percentage of such matches: {percentage:.2f}%')


#4.How do teams win?(Runs vs Wickets)

#sns.countplot(x = df['won_by'], palette='Set2')
#plt.title("How Teams Win: Runs vs Wickets")
#plt.xlabel("Won By")
#plt.ylabel("Count")
#plt.savefig("How_Teams_Win_Runs_vs_Wickets.png", bbox_inches="tight")



# Key Players Analysis

# 1 Most "Player of the Match" Awards

count = df['player_of_the_match'].value_counts().head(10)
# sns.barplot(y=count.index, x=count.values, palette='magma') 
# plt.title("Top 10 Players with Most 'Player of the Match' Awards")
# plt.xlabel("Players")
# plt.ylabel("Number of Awards")
# plt.xticks(rotation=45)
# plt.savefig("Top_10_Players_Player_of_the_Match_Awards.png", bbox_inches="tight")
# plt.show()


# 2.  2 Top Scorers 

high = df.groupby('top_scorer')['highscore'].sum().sort_values(ascending=False).head(2)
print(high)

# high.plot(kind='bar', color=['#1f77b4', '#ff7f0e'])
# plt.title("Top 2 Scorers in IPL")
# plt.xlabel("Players")
# plt.ylabel("Total Runs Scored")
# plt.xticks(rotation=45)
# plt.savefig("Top_2_Scorers_in_IPL.png", bbox_inches="tight")


# 10 Best Bowlers

df['highest_wickets'] = df['best_bowling_figure'].apply(lambda x : x.split('--')[0])

df['highest_wickets'] = df['highest_wickets'].astype(int)

top_bowlers = df.groupby('best_bowling')['highest_wickets'].sum().sort_values(ascending=False).head(10)

#top_bowlers.plot(kind = 'barh', color=['#1f77b4', '#ff7f0e'])
#plt.savefig("Top_Bowlers.png", bbox_inches="tight")

# Venue Analysis
# Most Matches Played by Venue
venue_count = df['venue'].value_counts()

sns.barplot(y = venue_count.index,x = venue_count.values,palette='rainbow')
plt.savefig("Most_Matches_Played_by_Venue.png", bbox_inches="tight")


# Who won the highest margin by runs?

df[df['won_by'] == 'Runs'].sort_values(by = 'margin',ascending=False).head(1)[['match_winner','margin']]

# Q2: Which player had the highest individual score?

df[df['highscore'] == df['highscore'].max()][['top_scorer','highscore']]

#Q3: Which bowler had the best bowling figures?

df[df['highest_wickets'] == df['highest_wickets'].max()][['best_bowling','best_bowling_figure']]