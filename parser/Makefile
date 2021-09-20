
CC = gcc 
FLAGS = -Wall 

I = ./include/
O = ./obj/
S = ./src/

T = tokenizer/


TOKENIZER = types tokenizer tokens error defrag list
TKN = $(foreach src, $(TOKENIZER), $(addprefix $(T), $(src)))

OBJECTS = $(TKN) main
OBJF = $(foreach obj, $(OBJECTS), $(addprefix $(O), $(obj)))
OBJ = $(foreach obj, $(OBJF), $(addsuffix .o, $(obj)))

./obj/%.o: ./src/%.c
	$(CC) -I $(I) $(FLAGS) -c $^ -o $@ 

parser: $(OBJ) 
	$(CC) $(FLAGS) $^ -o $@

clean:
	rm $(OBJ) 
