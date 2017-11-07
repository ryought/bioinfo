CC = gcc
.PHONY: all run-kadai1 run-kadai2 run-kadai3 clean
all: cplex  # all targets

cplex: cplex.c
	$(CC) -c $@.c; \
	$(CC) $@.o -lglpk -lm -o $@; \

# run kadai files
run-kadai1:
	cplex
	./cplex lp-datas/data.txt

run-kadai2:
	python branchAndBound.py lp-datas/data2.txt

run-kadai3:
	python combinatorial_auction.py

clean:
	rm *.o cplex
