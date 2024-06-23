.SUFFIX:
.PHONY: compile test checkstyle clean format all
.PRECIOUS: %.o

all: checkstyle test clean


CXX = clang++-14 -std=c++17 -Wall -Wextra -Wdeprecated -fsanitize=address
# CXX = clang++-14 -std=c++17 -Wall -Wextra -Wdeprecated -O3
# CXX = clang++-14 -std=c++17 -Wall -Wextra -Wdeprecated

BASENAME = HeatMap

OBJECTS = $(BASENAME) Points TerminalManager

HEADER = $(addsuffix .h, $(OBJECTS))

TEST_LIBRARIES = -lgtest -lgtest_main -lpthread

LIBRARIES = -lncurses



$(BASENAME)Test: $(addsuffix .o ,$(BASENAME)Test $(OBJECTS))
	$(CXX) -o $(BASENAME)Test $^ $(TEST_LIBRARIES) $(LIBRARIES)


%.o: %.cpp $(HEADER)
	$(CXX) -c $<

$(BASENAME)Main: $(addsuffix .o ,$(BASENAME)Main $(OBJECTS))
	$(CXX) -o $(BASENAME)Main $^ $(LIBRARIES)


compile: $(BASENAME)Main

# run: compile
# 	./$(BASENAME)Main ./test_data.tsv

run: compile
	./$(BASENAME)Main /mnt/c/Studium/C++/Daten/de.tsv


test: $(BASENAME)Test
	./$(BASENAME)Test
	

checkstyle:
	clang-format-14 --dry-run -Werror *.cpp *.h

clean:
	rm -f *Main
	rm -f *Test
	rm -f ./*.o

format:
	clang-format-14 -i *.cpp
	clang-format-14 -i *.h