@SP
M=1
M=M+1

//push constant 1
@1
D=A
@SP
A=M
M=D

@SP
M=M+1
//push constant 2
@2
D=A
@SP
A=M
M=D

@SP
M=M+1
//lt

@SP
M=M-1
@SP
A=M
D=M

@SP
M=M-1
@SP
A=M
D=D-M
@ISLT0
D;JLT
@SP
A=M
M=0
@END0
0;JMP
(ISLT0)
@SP
A=M
M=-1
(END0)
@SP
@M=M+1
