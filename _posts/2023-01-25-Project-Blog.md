---
toc: true
layout: post
description: Planning for the College Board Create Performance Task
categories: [T2, post]
title: Project Blog
author: Evan Aparri
show_tags: true
comments: true
---
For the College Board Performance task, it is necessary to adhere to all the guidelines set forth for the project. After receiving feedback from my group's presentation, I realized that our project should be able to house 4 different Create Performance Tasks with each group member doing one. For my Create Performance Task, it will be on the leaderboard for our snake game. 

## Outline of CPT Written response

3 a.
3.a.i.
The program provides a leaderboard helps create a competitive environment among fellow snake users. 

3.a.ii.
The function of the program is to compare your snake score with top 5 scores of the game. 

3.a.iii.
The input will be the username, score obtained from the game, and the date the game was played. The output will be the rank of the user's score compared to any game played.

3.b.i.
(Will likely show code where the different users and there scores are being stored)

3.b.ii.
(Will likely show our api accessing the code sorting it based on rank)

3.b.iii.
(TBD)

3.b.iv.
The data that my list contains is important to my program because it holds the individuals scores of the users needed to fill up the leaderboard.

3.b.v.
If the program were to run without the ____ list, it would make everything very inefficient because I would have to make a new variable every time a user completed a game to store their score.

3.c.i.
(Will likely show the update function that updates the player's highscore) This code will likely change because our group is still deciding whether a user can have multiple scores on the leaderboard

3.c.ii.
(Will show above function being called)

3.c.iii.
The function takes the new score obtained by a user from their game and compares it to see if their score is greater their high score. If it is, then it replaces it if it does then it replaces the high score. If it isn't, then it doesn't replace the high score.

3.c.iv.
(TBD)

3.c.v.
(TBD)

3.d.i.
First example will be when the users inputs a score that is not part of the top 5.


Second example will be when the user reaches a score in the top 5 and replaces the previous holder and pushes the rest down.

3.d.ii.
Condition 1:
(Will show score #1 being passed through an if statement deciding whether a score is higher than another)

Condition 2:
(Will show score #2 being passed through an if statement deciding whether a score is higher than another)

3.d.iii.
Results #1:
The result of the first call will display the rank of the user's score without it being displayed on the top 5 leaderboard.

Result #2:
The result of the second call will display the rank of the user's score while also being displayed on the top 5 leaderboard.


## Code I will need for CPT
- code showing how data has been stored in a list ( other collection type)
- - code showing how the data is the list above is being used to fulfill the program's purpose
- code showing a student-developed procedure with at least one parameter that has an effect on the functionality of the procedure.
- - code showing how the procedure above is being called
- program code segment from a student-developed algorithm that includes sequencing, selection, iteration.

## Code plan
- I will need to create a code that stores the past games and it being accessed to create a leaderboard
- I will need to show a procedure that has a parameter and effect on the program's function and also it being called
- I will need an algorithm sorting the rank of the users based on their score

## Video plan
- I will show me running the snake game and getting a low score and then inputting submitting the score to go to the leaderboard
- Then I will show me running the snake game and getting a high score that will become part of the top 5 leaderboard