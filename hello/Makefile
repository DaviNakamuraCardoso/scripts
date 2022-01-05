CC = gcc
CCPP = g++
ASM = nasm

%: %.c
	$(CC) $^ -o $@

%: %.cpp
	$(CCPP) $^ -o $@

%: %.go
	go build $^

%.o: %.asm
	$(ASM) -felf64 $^ -o $@

%.vm: %.jack
	dcc $^

%: %.o
	ld $^ -o $@

%.class: %.java
	javac $^ 
	
all: hello.swift hello Hello.class hello.rb hellogo hellocpp Hello.vm
