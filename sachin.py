timesBreaksHighestScore = 0;
timesBreaksLowestScore= 0;
ScoreList = [];
NoofGamesPlayed = input("Please enter number of games played:");
for i in range(int(NoofGamesPlayed)):
	score = input("Please enter game "+str(i+1)+" score:");
	ScoreList.append(int(score));
highestScore = ScoreList[0];
lowestScore = ScoreList[0];
for i in range(len(ScoreList)):
	if( highestScore < ScoreList[i]):
		timesBreaksHighestScore += 1;
		highestScore = ScoreList[i];	
	if(lowestScore > ScoreList[i]):
		timesBreaksLowestScore += 1;
		lowestScore = ScoreList[i];
print(timesBreaksHighestScore,timesBreaksLowestScore);
