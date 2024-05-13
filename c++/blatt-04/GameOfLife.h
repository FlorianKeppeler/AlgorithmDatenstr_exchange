
#include <ncurses.h>

#pragma once

const int MAX_NUMBER_CELLS = 10000;

extern bool PIXELS[MAX_NUMBER_CELLS];

extern bool CURRENT_CELLS[MAX_NUMBER_CELLS];
extern bool NEXT_CELLS[MAX_NUMBER_CELLS];

extern bool *P_CURRENT;
extern bool *P_Next;

extern int nrRows;
extern int nrCols;

extern int ROW;
extern int COL;

extern int STEPS;
extern int CELLS_ALIVE;

extern bool RUNNING;
extern bool EXIT;

extern MEVENT event;



void initTerminal();

void initGame();

void showState();

int numAliveNeighbors(int row, int col);

void updateState();

bool processUserInput(int keycode);

// helper functions

bool processMouseClick(MEVENT event);

void setPixel(int row, int column, bool value);

bool getPixel(int row, int column);

void resetArray(bool *pointer);

void drawPixel(int row, int column, int color);

void drawBorder(int color);

int numAlivePixel();

void setRandomPixels();

void setGliderPixels(int row, int col);