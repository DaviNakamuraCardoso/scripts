
CC = gcc 
FLAGS = -Wall 

%.o: %.c
	$(CC) $(FLAGS) -c $^ -o $@ 

parser: main.o types.o tokenizer.o tokens.o 
	$(CC) $(FLAGS) $^ -o $@

clean:
	rm *.o
