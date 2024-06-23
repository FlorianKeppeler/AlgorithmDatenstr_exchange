// copyright 2024: Florian Keppeler
// code and snippets from lectures were used as well as documentation of STL

#pragma once

#include <algorithm>
#include <fstream>
#include <gtest/gtest.h>
#include <iostream>
#include <string>
#include <unistd.h>
#include <unordered_map>

#include "Points.h"
#include "TerminalManager.h"

class HeatMap {

private:
public:
  // std::unordered_map<int, float> points_per_pixel_;

  std::vector<std::pair<std::size_t, std::size_t>> points_per_pixel_;
  std::vector<std::pair<std::size_t, float>> points_per_pixel_normalized_;

  Points points_;

  // reads coordinates from input file
  void readPointsFromFile(const std::string &filename);

  // get size of Points object
  std::size_t size() const;

  // get coordinates from Points object
  std::pair<float, float> get_coordinate(std::size_t index) const;

  // computes heatmap with given dimensions for columns and rows
  void computeHeatMap(std::size_t numRows, std::size_t numCols);

  // normalizes heatmap Values to values [0, 1]
  void normalizeHeatMap();

  // prints heatmap on canvas via TerminalManager class
  void drawHeatMap(TerminalManager *terminal_manager);

  FRIEND_TEST(HeatMap, readPointsFromFile);
};