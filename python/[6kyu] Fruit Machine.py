"""
Task
You will be given three reels of different images and told at which index the reels stop. From this information your job is to return the score of the resulted reels.
Rules
1. There are always exactly three reels

2. Each reel has 10 different items.

3. The three reel inputs may be different.

4. The spin array represents the index of where the reels finish.

5. The three spin inputs may be different

6. Three of the same is worth more than two of the same

7. Two of the same plus one "Wild" is double the score.

8. No matching items returns 0.


Returns
Return an integer of the score.

Example
Initialise
reel1 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel2 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel3 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
spin = [5,5,5]
result = fruit([reel1,reel2,reel3],spin)
Scoring
reel1[5] == "Cherry"
reel2[5] == "Cherry"
reel3[5] == "Cherry"

Cherry + Cherry + Cherry == 50
Return
result == 50
Good luck and enjoy!

Kata Series
If you enjoyed this, then please try one of my other Katas. Any feedback, translations and grading of beta Katas are greatly appreciated. Thank you.

Rank
"""

from collections import Counter

SCORING = {
    "Wild": [0, 10, 100],
    "Star": [18, 9, 90],
    "Bell": [16, 8, 80],
    "Shell": [14, 7, 70],
    "Seven": [12, 6, 60],
    "Cherry": [10, 5, 50],
    "Bar": [8, 4, 40],
    "King": [6, 3, 30],
    "Queen": [4, 2, 20],
    "Jack": [2, 1, 10]
}

def fruit(reels, spins):
    result = Counter([reels[0][spins[0]], reels[1][spins[1]], reels[2][spins[2]]])
    final_score = 0

    for key, value in result.items():
        if value == 3 and len(list(result)) == 1:
            final_score = SCORING[key][2]
        elif (value == 2 and not "Wild" in result) or (key == "Wild" and value == 2):
            final_score = SCORING[key][1]
        elif key != "Wild" and value == 2 and "Wild" in result:
            final_score = SCORING[key][0]

    return final_score
