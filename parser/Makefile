
CC = gcc 
FLAGS = -Wall 


I = ./include/
O = ./obj/
S = ./src/

SRC = main types tokenizer tokens error defrag
OBJF = $(foreach obj, $(SRC), $(addprefix $(O), $(obj)))
OBJ = $(foreach obj, $(OBJF), $(addsuffix .o, $(obj)))

./obj/%.o: ./src/%.c
	$(CC) -I $(I) $(L) $(FLAGS) -c $^ -o $@ 

parser: $(OBJ) 
	$(CC) $(FLAGS) $^ -o $@

clean:
	rm *.o
