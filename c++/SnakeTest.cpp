// copyright 2024: Florian Keppeler
// code and snippets from lectures were used as well as documentation of
// ncurses.h, gtest/gtest.h and also cstdlib for the use of rand()

#include "./Snake.h"

#include <gtest/gtest.h>

int DIM_X;
int DIM_Y;

int ROW;
int COL;
int DIR;

int FOOD_ROW;
int FOOD_COL;

int POINTS;
bool EMPTY = true;

TEST(CollisionTest, border_and_food) {

  // Test for correct collision with border
  DIM_X = 12;
  DIM_Y = 12;
  COL = 6;
  ROW = 6;
  ASSERT_EQ(collidesWithBorder(), false);

  COL = 0;
  ROW = 6;
  ASSERT_EQ(collidesWithBorder(), true);

  COL = 6;
  ROW = 0;
  ASSERT_EQ(collidesWithBorder(), true);

  COL = 10;
  ROW = 6;
  ASSERT_EQ(collidesWithBorder(), true);

  COL = 6;
  ROW = 11;
  ASSERT_EQ(collidesWithBorder(), true);

  // Test for correct collision with food item
  ROW = 6;
  FOOD_COL = 6;
  FOOD_ROW = 6;
  EMPTY = false;
  POINTS = 0;
  eatFood();
  ASSERT_EQ(EMPTY, true);
  ASSERT_EQ(POINTS, 100);

  FOOD_COL = 8;
  FOOD_ROW = 6;
  EMPTY = false;
  eatFood();
  ASSERT_EQ(EMPTY, false);
  ASSERT_EQ(POINTS, 100);

  FOOD_COL = 6;
  FOOD_ROW = 8;
  EMPTY = false;
  eatFood();
  ASSERT_EQ(EMPTY, false);
  ASSERT_EQ(POINTS, 100);
}

TEST(KeyHandleTEST, handleKey) {

  DIR = 1;
  ASSERT_EQ(handleKey(258), false);
  ASSERT_EQ(handleKey(260), false);
  ASSERT_EQ(handleKey(259), false);
  ASSERT_EQ(handleKey(261), false);
  ASSERT_EQ(handleKey(27), true);
}

TEST(MoveTest, moveSnake) {
  COL = 6;
  ROW = 6;

  DIR = 1;
  moveSnake();
  ASSERT_EQ(ROW, 7);
  handleKey(259);
  moveSnake();
  ASSERT_EQ(ROW, 8);

  DIR = 2;
  moveSnake();
  ASSERT_EQ(COL, 4);
  handleKey(261);
  moveSnake();
  ASSERT_EQ(COL, 2);

  DIR = 3;
  moveSnake();
  ASSERT_EQ(ROW, 7);
  handleKey(258);
  moveSnake();
  ASSERT_EQ(ROW, 6);

  DIR = 4;
  moveSnake();
  ASSERT_EQ(COL, 4);
  handleKey(260);
  moveSnake();
  ASSERT_EQ(COL, 6);
}

// int main() {
//   ::testing::InitGoogleTest();
//   return RUN_ALL_TESTS();
// }
