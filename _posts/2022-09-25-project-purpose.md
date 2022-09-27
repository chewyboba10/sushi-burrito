---
toc: true
layout: post
description: The Program Purpose of my team's final project idea, including the roles within the SCRUM team.
categories: [T1, Week 5, markdown, post]
title: Final Project Idea's Program Purpose
author: Evan Aparri
show_tags: true
comments: true
---

# Project Idea

Our team wishes to build a minesweeper game with a python backend that could consistently communicate with our frontend website while creating a new aesthetic to this classic game. This project would be split into two main portions each with it's own challenge. The first portion would be making the game engine in python, while the latter portion would be to design and create an aesthetically pleasing and functional frontend to display the Game Status.

## The Frontend
The frontend aspect of this project should preferably display a grid of the game and incorporate some aspect of user input. Preliminary testing and experimentation could be done through textbox inputs of coordinate values, while prospective functions could include individual buttons on the Grid itself to provide a GUI for the user to interact with. In both cases, the frontend should be able to communicate with the python backend through JSON data to send and receive data.

More aspects about the Frontend aspects will be added with additional planning in the future.

## The Backend
Arguably the more challenging half of this project, the backend would primarily serve to be the game engine of the minesweeper game. Additionally, the backend would also control and organize the various pages and menus on the website. In this writeup, we will only be focusing on the main goals and challenges faced by the Backend team.

- Using Object Oriented Programming to create individual objects for the game. Some aspects that could be represented by such objects would be the gameboard and also the individual cells and nodes present within the game board.
    -Doing so would simplify the algorithmic aspect of the game, as the board itself could have methods and attributes to help control the game logic.
    -Moreover, using an object to represent an individual cell in the board would provide greater functionalities than just using a single variable
- Use Enumerated types with the python `enum` module to create different values for the type and status of each node. Each of these types could then be bound to a constant value which could then be printed on the screen
- Use Recursion to create an algorithm to recursively detect adjacent cells that are safe (AKA not mines). This algorithm would work in the following format:
    - Maintain a list of current cells already determined to be safe
    - Verify if the four adjacent (up, down, left, right) cells next to the selected cell are safe or not, if safe, store the coordinate point in the list, if not, record the cell as a "border cell", terminate the recursive process, and run another helper function to determine the precise number of mines surrounding the cell
    - Re-call the function for each of the surrounding adjacent cells to identify other consecutive cells who are safe.
    - Return a list of the coordinates of a contiguous block of safe cells
    - Mark the cells to be safe and calculate number of surrounding mines for border cells.
- Verify the Game status:
    - Game is won if all mines are flagged
    - Game is lost if a mine was dug by the user
- Return the final result back to the front end. If a safe cell was dug, send out a JSON containing an array of the coordinates of the cell and it's safe neighbors. If a mine was dug, send a JSON containing a boolean value to signify the end of the game.

# SCRUM Team
> Here is an infographic of the scrum process showing our roles as a team

![]({{site.baseurl}}/images/scrum_methodology.png)