.SUFFIX:
.PHONY: compile test checkstyle clean format all
.PRECIOUS: %.o

all: compile run

run:
	./$(BASENAME)Main

CXX = clang++

BASENAME = GameOfLife

HEADER = GameOfLife.h

LIBRARIES = -lncurses

compile: $(BASENAME)Main

$(BASENAME)Main: $(addsuffix .o ,$(BASENAME)Main $(BASENAME))
	$(CXX) -o $(BASENAME)Main $^ $(LIBRARIES) -g


$(BASENAME)Test: $(addsuffix .o ,$(BASENAME)Main $(BASENAME))
	$(CXX) -o $(BASENAME)Test $^ $(LIBRARIES) -lgtest -lgtest_main

%.o: %.cpp $(HEADER)
	$(CXX) -c $<


test:
	$(CXX) -o test test.cpp

checkstyle:
	clang-format-14 --dry-run -Werror *.cpp *.h

clean:
	rm -f *Main
	rm -f *Test
	rm -f ./*.o

format:
	clang-format-14 -i *.cpp
	clang-format-14 -i *.h