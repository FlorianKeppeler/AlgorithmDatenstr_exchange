// copyright 2024: Florian Keppeler
// code and snippets from lectures were used as well as documentation of STL


#include "HeatMap.h"
#include "TerminalManager.h"

#include <fstream>
#include <iostream>
#include <string>
#include <ncurses.h>

int main(int argc, char **argv) {

  if (argc != 2) {
    std::cerr << "usage HeatMapMain <FilePath>" << std::endl;
    return (1);
  }

  

  HeatMap heat_map;

  heat_map.readPointsFromFile(argv[1]);

    int numCols;
    int numRows;

  TerminalManager terminal_manager;

  heat_map.computeHeatMap(terminal_manager.numRows(), terminal_manager.numCols());

  numCols = terminal_manager.numCols();
  numRows = terminal_manager.numRows();

  

  heat_map.normalizeHeatMap();

// mvprintw(10, 2 * 10, printf("%d",terminal_manager.numCols()));
// mvprintw(12, 2 * 10, printf("%d",terminal_manager.numRows()));



  heat_map.drawHeatMap(&terminal_manager);

    // std::cout << terminal_manager.numCols() << std::endl;
    
    // std::cout << terminal_manager.numRows() << std::endl;

//   for(const auto& pairs : heat_map.points_per_pixel_normalized_) {

//       std::cout << pairs.first << "; " << pairs.second << std::endl;
//   }

    int tmp_col;
    int tmp_row;

    std::cout << numCols << " : " << numRows << std::endl;

  for (const auto &pair : heat_map.points_per_pixel_normalized_) {

        tmp_col = pair.first % numCols;
        tmp_row = pair.first / numCols;

        std::cout << tmp_col << " : " << tmp_row << std::endl;
      }

  //   for(const auto& pairs : heat_map.points_per_pixel_) {

  //     std::cout << pairs.first << "; " << pairs.second << std::endl;
  // }
}