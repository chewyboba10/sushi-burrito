---
toc: true
layout: post
description: AppLab Quiz Notes
categories: [T1, Notes, Week 3, markdown, post]
title: Notes - AppLab Quiz Creation
author: Evan Aparri
show_tags: true
comments: true
---

# AppLab Quiz Creation

Here is the link to my [quiz](https://studio.code.org/projects/applab/5_onrC4AXLX0LVnWsf8bupLPLI6vCGO9nh-xtGI9vmU)

## Starting off

Here is what I noticed when exploring:
- the dimensions of the screen were 320 by 450. This Note is mainly used to help center the objects I add
- I could change the color of the objects color, or the color of texts using setting the rgba values
- I can duplicate the screen if I want to keep the format of the screen I created
- I saw that the user can input text and that they can choose from a dropdown menu
- I can switch between block code and text code

## Plan

- Create a math themed quiz
- Create different difficulties
- Find a way to go to a quiz of matching difficulty using the dropdown menu
- Be able to show the final score at the end of the quiz
- Be able to use only

## Process

I ended up designing a total of 13 different screens with three pairs of 3 questions, each with a different corresponding difficulty, a starting screen: `Start_Window`, a correct answer screen: `CorrectScreen`, a incorrect answer screen: `WrongAnswer`, and a end screen: `End_Screen`

![]({{ site.baseurl }}/images/appscreen.png "List of the different screens in the app")

I created 3 different difficulties corresponding to different school levels

![]({{ site.baseurl }}/images/differentdifficulties.png "List of the different difficulties in the quiz")

I initially had problems figuring out how to make it so that the dropdown option I chose would result in the app taking me to the different quizzes. However, after exploring a bit more in the code blocks, I was able to create an if else statement that would take me to different screens depending on what was chosen from the dropdown option.

![]({{ site.baseurl }}/images/changedifficultycode.png "Here is the code on how I managed to switch to different quizzes")

The format for all the questions is a user inputted response based one. The code I wrote makes it so that after you click the button the reads "Check Answer", if the inputted texts matches the answer, you go to the `CorrectScreen` screen. If you get it wrong, you'll go to the `WrongAnswer` screen. (the question shown below, `Normal_Question_1`, is the only one where there were two possible answers, which I was able to do using double vertical bars)

![]({{ site.baseurl }}/images/question-example.png "Screen and code for that screen")

For the final question of each difficulty, I created a string concatenation that would show the results of the quiz in the blank text box in the `End_Screen`.

![]({{ site.baseurl }}/images/appresultsmessage.png "Screen and code for that screen")


## Results and Findings

The block form of code made it really easy to visualize how each block of code worked and made it easier to find out what went wrong. It was also cool to be able to convert the blocks into JavaScript, which made JavaScript muc easier to understand. While thinking back to how I made this quiz, I realize there are a few bugs that need to be patched up such as:
- If I go back to the `Start_Window` clicking a "Quit" or "Home" button, the dropdown menu defaults to the previously chosen item. So if I end up choose the "Choose Difficulty" item and press start, it goes to the "Hard" difficulty.
- The `var correct` does not reset back to 0 after starting another quiz