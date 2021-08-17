
CC = gcc 
FLAGS = -Wall -Ofast

%.o: %.c
	$(CC) $(FLAGS) -c $^ -o $@

downloads: downloads.o
	$(CC) $(FLAGS) $^ -o $@ -lcurl
