
CC = clang 
FLAGS = -Wall -Ofast 

%.o: %.c
	$(CC) $(FLAGS) -c $^ -o $@ 

parser: main.o types.o tokenizer.o tokens.o 
	$(CC) $(FLAGS) $^ -o $@
