// init row and col to zero
@row
M=0

@col
M=0

@printval
M=-1

(NEXTPRINT)
  // set screenval to SCREEN base
  @16384 // screen base
  D=A
  @screenval
  M=D

  // if row == 8192 goto end (256*32) (256=>nrows) 
  @row
  D=M
  @8192
  D=D-A
  @END
  D;JEQ


  // screenval += row + col
  @col
  D=M
  @screenval
  M=D+M

  @row
  D=M
  @screenval
  M=D+M

  // print/set 16 pixels to black (16-bit 1's)
  @screenval
  A=M // set A = M[screenval]
  M=-1

  // if col < 32 => col++, goto nextprint
  @col
  D=M
  @31 // previously 32, but guess we write from 0-31
  D=D-A
  @INCCOL
  D;JLT

  // else col = 0, row += row, goto nextprint
  @col
  M=0

  @32
  D=A
  @row    // not sure if necessary to reinit M, but we'll do anyway
  M=D+M

  @NEXTPRINT
  0;JMP


// endless loop
(END)
  @END
  0;JMP


// col++, JMP NEXTPRINT
(INCCOL)
  @col
  D=M
  M=D+1
  
  @NEXTPRINT
  0;JMP
