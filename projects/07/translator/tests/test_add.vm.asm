// self coded - init SP (R0) with 20
@SP
M=1
M=M+1
M=M+1

//push constant 7
@7
D=A
@SP
A=M
M=D

@SP
M=M+1
//push constant 8
@8
D=A
@SP
A=M
M=D

@SP
M=M+1
//add

@SP
M=M-1
@SP
A=M
D=M

@SP
M=M-1
@SP
A=M
M=D+M

@SP
M=M+1