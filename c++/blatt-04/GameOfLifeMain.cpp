
#include "GameOfLife.h"

#include <ncurses.h>
#include <unistd.h>

int main() {

  initTerminal();

  

  bool *P_tmp{nullptr};

  initGame();

  //   drawBorder(4);

  while (true) {

    processUserInput(getch());

    if (EXIT == true) { // EXIT is true when ESC is pressed

      endwin(); // needed to close ncurses screen
      break;
    }

    // mvprintw(5, 80, "Einfach damit hier was steht");

    showState();

    refresh();

    mvprintw(5, 80, "Alive N: %d", numAliveNeighbors(ROW, COL));

    if (RUNNING) {

      updateState();

      usleep(50000);
    }
  }

  return 0;
}