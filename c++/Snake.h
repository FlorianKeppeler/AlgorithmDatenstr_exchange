// copyright 2024: Florian Keppeler
// code and snippets from lectures were used as well as documentation of
// ncurses.h, gtest/gtest.h and also cstdlib for the use of rand()

#pragma once

extern int DIM_X; // x dimension of game are
extern int DIM_Y; // y dimension of game area

extern int ROW; // current row of Snake
extern int COL; // current column of Snake
extern int DIR; // current direction of Snake

extern int FOOD_ROW; // current row of food item
extern int FOOD_COL; // current column of food item

extern int POINTS; // store points
extern bool EMPTY; // is screen without food item

// sets up Terminal and defines color schemes
void initTerminal();

// sets up starting position and initial direction of snake
void initGame();

// draws one Pixel in position of row and column and in color defined by
// initTerminal()
void drawPixel(int row, int column, int color);

// draws border around the game area in color scheme defined in initTerminal()
void drawBorder(int color);

// draws current position of snake
void drawSnake(int color);

// checks if snake collided with border
bool collidesWithBorder();

// moves snake in direction of DIR
void moveSnake();

// changes direction DIR according to keyboard input
bool handleKey(int key);

// (optional) adds food item to game area in random location
void addFood(int color);

// (optional) checks if snake has eaten food item
void eatFood();