
#include "GameOfLife.h"

#include <cstdlib> // for rand()
#include <ncurses.h>

bool CURRENT_CELLS[MAX_NUMBER_CELLS];
bool NEXT_CELLS[MAX_NUMBER_CELLS];

bool PIXELS[MAX_NUMBER_CELLS];

bool *P_CURRENT;
bool *P_Next;

int nrRows;
int nrCols;

int ROW;
int COL;

int STEPS;
int CELLS_ALIVE;

bool RUNNING;
bool EXIT;

MEVENT event;


//____________________________________________________
void initTerminal() {

  initscr();

  curs_set(false); // don't show cursor when printung

  noecho();              // no input is shown on screen
  nodelay(stdscr, true); // getch() does no longer wait for input

  start_color();
  init_pair(1, COLOR_RED, COLOR_BLACK);
  init_pair(2, COLOR_BLUE, COLOR_BLACK);

  //   init_pair(2, COLOR_BLACK, COLOR_BLUE);
  init_pair(3, COLOR_BLACK, COLOR_RED);
  init_pair(4, COLOR_GREEN, COLOR_BLACK);

  keypad(stdscr, true); // allow special ascii keys > 255

  mousemask(ALL_MOUSE_EVENTS, NULL);
  mouseinterval(0);
}

void initGame() {

  P_CURRENT = CURRENT_CELLS;
  P_Next = NEXT_CELLS;

  nrRows = LINES;
  nrCols = COLS / 2;

  ROW = 0;
  COL = 0;

  STEPS = 0;
  CELLS_ALIVE = 0;

  RUNNING = false;
  EXIT = false;
}

// ____________________________________________________________________________
bool processMouseClick(MEVENT event) {

  if (event.bstate & BUTTON1_PRESSED) {

    ROW = event.y;
    COL = event.x / 2;

    mvprintw(5, 80, "clicked: %d, %d", ROW, COL);

    return true;

  } else {

    return false;
  }
}

void setPixel(int row, int column, bool value) {
    if (row * nrCols + column < 0 | row * nrCols + column > MAX_NUMBER_CELLS)
    {
      return;
    }
  P_CURRENT[row * nrCols + column] = value;
}

bool getPixel(int row, int column) { return P_CURRENT[row * nrCols + column]; }

void showState() {

  attron(COLOR_PAIR(1));

  for (int it_rows = 0; it_rows < nrRows; ++it_rows) {
    for (int it_cols = 0; it_cols < nrCols; ++it_cols) {

      if (getPixel(it_rows, it_cols)) {
        attron(A_REVERSE);
      }
      mvprintw(it_rows, it_cols * 2, "  ");

      if (getPixel(it_rows, it_cols)) {
        attroff(A_REVERSE);
      }
    }
  }

  attroff(COLOR_PAIR(1));
}

int numAliveNeighbors(int row, int col) {

  int neighbors = 0;

  for (int n_rows = row - 1; n_rows - row <= 1; ++n_rows) {
    for (int n_cols = col - 1; n_cols - col <= 1; ++n_cols) {

      if (n_cols > 0 && n_cols < nrCols && n_rows > 0 && n_rows < nrRows) {

        if (n_rows == row && n_cols == col) {
          continue;
        }

        if (getPixel(n_rows, n_cols) == true) {
          ++neighbors;
        }
      }
    }
  }

  return neighbors;
}


void updateState() {

  int alive = 0;

  for (int it_rows = 0; it_rows < nrRows; ++it_rows) {
    for (int it_cols = 0; it_cols < nrCols; ++it_cols) {

      alive = numAliveNeighbors(it_rows, it_cols);

      switch (alive) {

      case 2:
        P_Next[it_rows * nrCols + it_cols] =
            P_CURRENT[it_rows * nrCols + it_cols];
        break;

      case 3:
        P_Next[it_rows * nrCols + it_cols] = true;
        break;

      default:
        P_Next[it_rows * nrCols + it_cols] = false;
      }
    }
  }

  bool *P_tmp = P_Next;
  P_Next = P_CURRENT;
  P_CURRENT = P_tmp;

  resetArray(P_Next);
}


bool processUserInput(int keycode) {

  // process Mous Events:
  if (getmouse(&event) == OK) {
    if (processMouseClick(event)) {

      setPixel(ROW, COL, !getPixel(ROW, COL));
    }
  }

  // process key input:
  switch (keycode) {
  case 32: // Space: Pause or start the simulation
    RUNNING = !RUNNING;
    return true;
    break;

  case 114: // 'r': set random pixels with 20% probality to be alive
    if (!RUNNING) {
      setRandomPixels();
      return true;
    } else {
      return false;
    }
    break;

  case 103: // 'g': create 'glider' at location of last mouse event
    if (!RUNNING) {
      setGliderPixels(ROW, COL);
      return true;
    } else {
      return false;
    }
    break;

  case 27: // ESC: exit simulation
    EXIT = !EXIT;
    return true;
    break;

  default:
    return false;
  }
}

//-------------------helper functions--------------------------

void resetArray(bool *pointer) {

  for (int i = 0; i < sizeof(pointer); ++i) {
    pointer[i] = false;
  }
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

  while (i <= LINES - 1) {

    drawPixel(i, 0, color);
    drawPixel(i, COLS - 2, color);

    ++i;
  }

  i = 2; // first two Pixels have been already drawn by previous loop

  while (i <= COLS - 2) {

    drawPixel(0, i, color);
    drawPixel(LINES - 1, i, color);

    ++i;
  }
}

int numAlivePixel() {

  int alive = 0;

  for (int it_rows = 0; it_rows < nrRows; ++it_rows) {
    for (int it_cols = 0; it_cols < nrCols; ++it_cols) {

      if (getPixel(it_rows, it_cols) == true) {
        ++alive;
      }
    }
  }

  return alive;
}

void setGliderPixels(int row, int col) {

  setPixel(row, col, true);
  setPixel(row - 1, col, true);
  setPixel(row - 2, col, true);
  setPixel(row, col + 1, true);
  setPixel(row - 1, col + 2, true);
}

void setRandomPixels() {

  for (int it_rows = 0; it_rows < nrRows; ++it_rows) {
    for (int it_cols = 0; it_cols < nrCols; ++it_cols) {

      if (rand() % 5 == 0) { // probability of 20%

        setPixel(it_rows, it_cols, true);
      }
    }
  }
}