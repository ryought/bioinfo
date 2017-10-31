CC = gcc
CFLAGS = -Wall -lglpk  
.PHONY: all debug sanitize clean run
all: cplex  # all targets

cplex: cplex.c
	$(CC) -c $@.c; \
	$(CC) $@.o -lglpk -lm -o $@; \

run:
	./a.out
debug:
	gcc -g 
	lldb a.out
sanitize:
	gcc -g -fsanitize=address 
clean:
	rm *.out
