// copyright 2024: Florian Keppeler
// code and snippets from lectures were used as well as documentation of
// ncurses.h, gtest/gtest.h and also cstdlib for the use of rand()

#include <cstdlib>
#include <ncurses.h>

#include "./Snake.h"

//____________________________________________________
void initTerminal() {

  initscr();

  curs_set(false); // don't show cursor when printung

  DIM_Y = 50;  // game area is of height DIM_Y
  DIM_X = 100; // and width of DIM_X

  noecho();              // no input is not shown on screen
  nodelay(stdscr, true); // getch() does no longer wait for input

  start_color();
  init_pair(1, COLOR_RED, COLOR_BLACK);
  init_pair(2, COLOR_BLUE, COLOR_BLACK);
  init_pair(3, COLOR_BLACK, COLOR_RED);
  init_pair(4, COLOR_GREEN, COLOR_BLACK);

  keypad(stdscr, true); // allow special ascii keys > 255
}

//__________________________________________________________
void initGame() {

  ROW = DIM_Y / 2;
  COL = DIM_X / 2 - 2;

  DIR = 4;

  POINTS = 0;
}

//__________________________________________________________
void drawPixel(int row, int column, int color) {

  attron(COLOR_PAIR(color)); // define color scheme
  attron(A_REVERSE);         // swap color scheme

  mvprintw(row, column, "  "); // print Text in row and col position

  attroff(A_REVERSE);
  attroff(COLOR_PAIR(color));
}

//___________________________________________________
void drawBorder(int color) {

  int i = 0;

  while (i <= DIM_Y - 1) {

    drawPixel(i, 0, color);
    drawPixel(i, DIM_X - 2, color);

    ++i;
  }

  i = 2; // first two Pixels have been already drawn by previous loop

  while (i <= DIM_X - 2) {

    drawPixel(0, i, color);
    drawPixel(DIM_Y - 1, i, color);

    ++i;
  }
}

//________________________________
void drawSnake(int color) { drawPixel(ROW, COL, color); }

//____________________________________
bool collidesWithBorder() {

  if (COL > DIM_X - 4 || COL <= 0) { // Snake moves always 2 COL in x dimension
                                     // and border is 2 columns wide
    return true;
  }

  if (ROW > DIM_Y - 2 || ROW <= 0) { // border is to rows wide
    return true;
  }

  return false;
}

//____________________________________________
void moveSnake() {

  switch (DIR) {

  case 1:
    ROW += 1;
    break;
  case 2:
    COL -= 2;
    break;
  case 3:
    ROW -= 1;
    break;
  case 4:
    COL += 2;
    break;
  }
}

//________________________________________________
bool handleKey(int key) {

  int tmp_dir = 0;

  switch (key) {

  case KEY_DOWN:
    tmp_dir = 1;
    break;
  case KEY_LEFT:
    tmp_dir = 2;
    break;
  case KEY_UP:
    tmp_dir = 3;
    break;
  case KEY_RIGHT:
    tmp_dir = 4;
    break;
  case 27:
    return true;
  }

  int dif_tmp = DIR - tmp_dir;

  if (dif_tmp != 2 &&
      dif_tmp !=
          -2) { // if difference of DIR and new input is either 2 or -2 change
                // in directions would be 180 degrees wich is forbidden

    DIR = tmp_dir;
  }

  return false;
}

//_________________________________________________
void addFood(int color) {

  FOOD_ROW = rand() % DIM_Y - 1;
  FOOD_COL =
      (rand() % DIM_X / 2) * 2; // snake moves only on even numbers of column so
                                // food item must also be on even columns

  drawPixel(FOOD_ROW, FOOD_COL, color);
  EMPTY = false; // store information in global variable, that there is a food
                 // item in game area
}

//___________________________________________________
void eatFood() {

  if (FOOD_ROW == ROW && FOOD_COL == COL) {

    drawPixel(FOOD_ROW, FOOD_COL, 3); // to delete food from canvas

    POINTS += 100; // for each food item player gets 100 points
    EMPTY = true;  // game area is empty -> no food items on screen
  }
}