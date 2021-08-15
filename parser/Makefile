
CC = gcc 
FLAGS = -Wall -Ofast

%.o: %.c
	$(CC) $(FLAGS) -c $^ -o $@ 

parser: main.o tokenizer.o tokens.o
	$(CC) $(FLAGS) $^ -o $@
