// copyright 2024: Florian Keppeler
// code and snippets from lectures were used as well as documentation of
// ncurses.h, gtest/gtest.h and also cstdlib for the use of rand()

#include <ncurses.h>
#include <unistd.h>

#include <cstdio>
#include <cstdlib>

#include "./Snake.h"

// definition of global variables after declaration in Snake.h
int DIM_X;
int DIM_Y;

int ROW;
int COL;
int DIR;

int FOOD_ROW;
int FOOD_COL;

int POINTS;
bool EMPTY = true;

// main function runs the game with input speed [pixel/second] and acceleration
// [pixel/second^2]
int main(int argc, char **argv) {

  // support for calling function from terminal:
  if (argc != 3) {
    printf("Usage: ./SnakeMain <speed> <acceleration>\n");
    return 1;
  }

  float speed = atof(argv[1]);        // in Pixels per second
  float acceleration = atof(argv[2]); // in Pixels per second^2

  initTerminal(); // initialize ncurses with properties

  initGame(); // defines game area dimensions and starting location of snake

  int key;

  // int timer = 0;

  while (true) {

    if (collidesWithBorder()) { // when snake colides with border, stay in this
                                // loop until ESC is pressed

      mvprintw(DIM_Y / 3, DIM_X / 2 - 18,
               "Your Score: %d ---Press ESC to exit---",
               POINTS); // final message after game is over

      int escape_key = getch();

      if (escape_key == 27) {
        break;

      } else {
        continue;
      }
    }

    key = getch();

    if (key != 27) { // key 27 is id for esc input

      drawBorder(2); // draws border around game area

      drawSnake(1); // draws snake at current location of ROW and COL

      mvprintw(DIM_Y + 1, DIM_X / 2 - 5, "Points: %d", POINTS);
      mvprintw(DIM_Y + 1, DIM_X - 18, "Speed: %f", speed);

      refresh(); // printing takes place only when refresh is called!

      if (key != -1) {

        handleKey(key);
      }

      drawSnake(3); // to delete previous position of snake

      moveSnake(); // move Snake one pixel in current direction

      eatFood(); // check if Snake ate food item

      if (EMPTY) { // if no food item is on the screen:

        addFood(4);                    // add food item to game area
        speed += acceleration / speed; // increase speed
      }

      usleep((1000000) / speed); // the sleep time of one second is divided by
                                 // speed to get pixel/second

      speed += acceleration / speed; // increase speed

    } else { // if ESC is pressed exit while loop -> end game
      break;
    }
  }

  endwin(); // needed to close ncurses screen

  return 0;
}