// SET SP to 4
@SP
M=1
M=M+1
M=M+1
M=M+1


// set LCL to 9
@LCL
M=1
M=M+1
M=M+1
M=M+1
M=M+1
M=M+1
M=M+1
M=M+1
M=M+1

// value to be pop'd 
@9
M=1

// SP--
//@SP
//M=M-1

// addr = LCL + i (i=0)
@LCL
D=M
@0
A=D+A
D=M // this is then already the value to be pop'd from local and pushed to stack (*addr)

@SP
A=M
M=D


// SP++
@SP
M=M+1

