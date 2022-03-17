// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.


//* r0=5, r1=7
// * Pseudocode:
// * tmp = 0
// * while r1 > 0 and r0 > 0:
// *   if r1 == 1:
// *     tmp += r0
// *     jmp END
// *   tmp += (r0 + r0) // r0*2
// *   r1 -= 2
// * (END)
// * result = tmp
// *
// */

// Put your code here.
// init output (R2) to zero
@2
M=0

// if r1 == 0 jmp end
@1
D=M
@END
D;JEQ

// if r0 == 0 jmp end
@0
D=M
@END
D;JEQ


// begin the multiplication loop
(BEGINMULTI)
  // if r1 == 1 jmp odd
  @1
  D=M-1
  @ODD
  D;JEQ
  
  // multiply r1 * 2 and store value in r2
  // ADD R2, R0, R0
  @0
  D=M
  @2
  M=D+M
  @2
  M=D+M

  // if r1 > 0 (and r1 != 1 as checked previously)
  // decrement by two
  @1
  MD=M-1
  MD=M-1
  @END
  D;JEQ

  @BEGINMULTI
  0;JMP


(ODD)
  // ADD R2, R2, R0
  @0
  D=M
  @2
  M=D+M

(END)
  @END
  0;JMP

