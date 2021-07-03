
%.o: %.c
	gcc -I./ -c $^ -o $@

all: hash.o lord.o
	gcc -I./ $^ -o lord
