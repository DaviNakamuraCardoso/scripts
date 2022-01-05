global _start

section .data
    hello db "Hello, World!", 0x0a
    len equ $ - hello

section .text
_start:
    mov     rax, 0x01
    mov     rdi, 0x01
    mov     rsi, hello
    mov     rdx, len
    syscall

    mov rsi,    0x00
    mov rax,    0x3c
    syscall
