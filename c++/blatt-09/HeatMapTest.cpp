// copyright 2024: Florian Keppeler
// code and snippets from lectures were used as well as documentation of STL

#include "HeatMap.h"

#include <gtest/gtest.h>

TEST(HeatMap, readPointsFromFile) {

  HeatMap hm;

  hm.readPointsFromFile("test_data.tsv");

  ASSERT_EQ(28, hm.size());

  ASSERT_FLOAT_EQ(10.0465295, hm.points_.get_coordinate(0).first);
  ASSERT_FLOAT_EQ(53.5919293, hm.points_.get_coordinate(0).second);

  ASSERT_FLOAT_EQ(12.2147021, hm.points_.get_coordinate(27).first);
  ASSERT_FLOAT_EQ(49.1165041, hm.points_.get_coordinate(27).second);
}