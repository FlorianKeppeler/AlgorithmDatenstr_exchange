// copyright 2024: Florian Keppeler
// code and snippets from lectures were used as well as documentation of STL


#pragma once

#include <algorithm>

#include <gtest/gtest.h>
#include <vector>

class Points {

private:
  std::vector<float> x_;
  std::vector<float> y_;

  std::size_t size_;

public:
  // Constructor
  Points();

  // add coordinate to Points class
  void add_coordinate(const float x, const float y);

  // get coordinates at given index
  std::pair<float, float> get_coordinate(std::size_t index) const;

  // get coordinates via []
  std::pair<float, float> operator[](std::size_t index);

  // get size
  std::size_t size() const;

  // get min and max of x coordinates
  std::pair<float, float> get_range_x() const;

  // get min and max of y coordinates
  std::pair<float, float> get_range_y() const;

  FRIEND_TEST(HeatMap, readPointsFromFile);
};