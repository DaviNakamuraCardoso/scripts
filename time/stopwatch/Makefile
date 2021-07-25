
# Header, Libs, Source 
H = ./include
L = ./libs
S = ./src

# Compiler and flags
CC = gcc
CFLAGS = -Wall -Ofast

# Libraries
LIBS = $(L)/libcontrol.a
LINKS = -lcontrol

./libs/libcontrol.a: ./obj/control/control.o 


all: main.o $(LIBS)
	$(CC) $(CFLAGS) -I $(H) -L $(L) main.o -o stopwatch $(LINKS)



# Patterns 
./obj/%.o: ./src/%.c
	$(CC) $(CFLAGS) -I $(H) -c $^ -o $@

%.o: %.c
	$(CC) $(CFLAGS) -I $(H) -c $^ -o $@

./libs/lib%.a: 
	ar -rcs $@ $^
