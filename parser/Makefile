
CC = gcc 
FLAGS = -Wall 

%.o: %.c
	$(CC) $(FLAGS) -c $^ -o $@ 

parser: main.o tokenizer.o tokens.o
	$(CC) $(FLAGS) $^ -o $@
