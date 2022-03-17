# code_writer - translates VM commands to Hack assembly language
from enumerations import CommandType


INC_SP = """
@SP
M=M+1
"""

DEC_SP = """
@SP
M=M-1
"""

class CodeWriter():
  
  # name of the output file
  fname = ""
  # asm instructions later on writter to the .asm file
  asm_contents = ""

  # if true outputs also the current VM command
  debug = 1

  # counter which functions as a unique value for the various introduced loops
  counter = 0

  def __init__(self, fname = ""):
    self.fname = fname

  # informs the code writer that the translation of a new VM file is started
  def setFileName(self, fname: str):
    self.fname = fname

  # wirtes the assembly code that is the translation of the given
  # arithmetic command
  def writeArithmetic(self, command: str, full_cmd = ""):
    if full_cmd != "":
      self.asm_contents += f"//{full_cmd}\n"
    if command == "add":
      # decrement the stack pointer
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    # M[0] into A
      self.asm_contents += "D=M\n"    # M[257] into D
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    # M[0] into A
      self.asm_contents += "M=D+M\n"  # M[256] = D + M[256]
      self.asm_contents += INC_SP

    if command == "sub":
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    # M[0] into A   // M[SP] into A
      self.asm_contents += "D=M\n"    # M[257] into D // M[A] into D
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    # M[0] into A
      self.asm_contents += "M=M-D\n"  # M[256] = M[256] - D
      self.asm_contents += INC_SP

    if command == "neg":
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"
      self.asm_contents += "M=-M\n"
      self.asm_contents += INC_SP

    if command == "eq":
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    # M[0] into A   // M[SP] into A
      self.asm_contents += "D=M\n"    # M[257] into D // M[A] into D
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    # M[0] into A
      self.asm_contents += "D=M-D\n"  # M[256] = M[256] - D
      self.asm_contents += f"@ISEQ{self.counter}\n"
      self.asm_contents += "D;JEQ\n"    # if x == y we write -1 in the current *SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    
      self.asm_contents += "M=0\n"         # if x != y we write 0 in the current *SP
      self.asm_contents += f"@END{self.counter}\n" # and then jmp to the end of the comparison
      self.asm_contents += f"0;JMP\n"
      self.asm_contents += f"(ISEQ{self.counter})\n" 
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    
      self.asm_contents += "M=-1\n"         # if x != y we write 0 in the current *SP
      self.asm_contents += f"(END{self.counter})\n" 
      self.asm_contents += "@SP\n"
      self.asm_contents += "@M=M+1\n"

      self.counter += 1

    if command == "gt":
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    # M[0] into A   // M[SP] into A
      self.asm_contents += "D=M\n"    # M[257] into D // M[A] into D
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    # M[0] into A
      self.asm_contents += "D=D-M\n"  # M[256] = M[256] - D
      self.asm_contents += f"@ISGT{self.counter}\n"
      self.asm_contents += "D;JGT\n"    # if x == y we write -1 in the current *SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    
      self.asm_contents += "M=0\n"         # if x != y we write 0 in the current *SP
      self.asm_contents += f"@END{self.counter}\n" # and then jmp to the end of the comparison
      self.asm_contents += f"0;JMP\n"
      self.asm_contents += f"(ISGT{self.counter})\n" 
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    
      self.asm_contents += "M=-1\n"         # if x != y we write 0 in the current *SP
      self.asm_contents += f"(END{self.counter})\n" 
      self.asm_contents += "@SP\n"
      self.asm_contents += "@M=M+1\n"

      self.counter += 1
    if command == "lt":
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    # M[0] into A   // M[SP] into A
      self.asm_contents += "D=M\n"    # M[257] into D // M[A] into D
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    # M[0] into A
      self.asm_contents += "D=D-M\n"  # M[256] = M[256] - D
      self.asm_contents += f"@ISLT{self.counter}\n"
      self.asm_contents += "D;JLT\n"    # if x == y we write -1 in the current *SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    
      self.asm_contents += "M=0\n"         # if x != y we write 0 in the current *SP
      self.asm_contents += f"@END{self.counter}\n" # and then jmp to the end of the comparison
      self.asm_contents += f"0;JMP\n"
      self.asm_contents += f"(ISLT{self.counter})\n" 
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    
      self.asm_contents += "M=-1\n"         # if x != y we write 0 in the current *SP
      self.asm_contents += f"(END{self.counter})\n" 
      self.asm_contents += "@SP\n"
      self.asm_contents += "@M=M+1\n"

      self.counter += 1

    if command == "and":
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    # M[0] into A
      self.asm_contents += "D=M\n"    # M[257] into D
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    # M[0] into A
      self.asm_contents += "M=M&D\n"  # M[256] = M[256] AND D
      self.asm_contents += INC_SP
      
    if command == "or":
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    # M[0] into A
      self.asm_contents += "D=M\n"    # M[257] into D
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"    # M[0] into A
      self.asm_contents += "M=M|D\n"  # M[256] = M[256] OR D
      self.asm_contents += INC_SP

    if command == "not":
      self.asm_contents += DEC_SP
      self.asm_contents += "@SP\n"    
      self.asm_contents += "A=M\n"    # M[SP] into A
      self.asm_contents += "M=!M\n"   # M[256] = !M[256]
      self.asm_contents += INC_SP


  # writes the assembly code that is the tranlsation of the given command (pop/push)
  def writePushPop(self, pop_push: CommandType, segment: str, index: int, full_cmd = ""):
    if full_cmd != "":
      self.asm_contents += f"//{full_cmd}\n"
    if pop_push == CommandType.C_PUSH and segment == "constant":
      self.asm_contents += f"@{index}\n"
      self.asm_contents += "D=A\n"
      self.asm_contents += "@SP\n" # *SP=D
      self.asm_contents += "A=M\n"
      self.asm_contents += "M=D\n"
      self.asm_contents += INC_SP

    elif pop_push == CommandType.C_POP and segment == "local":
      # General Idea: addr = LCL+i; SP--; *addr=*SP

      # SP--
      self.asm_contents += DEC_SP

      # save value of *SP into D
      self.asm_contents += "@SP\n"
      self.asm_contents += "D=M\n"

      # *addr=*SP
      self.asm_contents += "@LCL\n"
      self.asm_contents += "D=M\n"        # D=M[LCL] 
      self.asm_contents += f"@{index}\n"
      self.asm_contents += "A=D+A\n"      # A=LCL+index
      self.asm_contents += "A=M"


    elif pop_push == CommandType.C_PUSH and segment == "local":
      # General Idea: addr = LCL+i; *SP = *addr; SP++
      # save value of *addr into D
      self.asm_contents += "@LCL\n"
      self.asm_contents += "D=M\n"
      self.asm_contents += f"@{index}\n"
      self.asm_contents += "A=D+A\n"
      self.asm_contents += "D=M\n"

      # write value to stack => *SP = *addr
      self.asm_contents += "@SP\n"
      self.asm_contents += "A=M\n"
      self.asm_contents += "M=D\n"
      
      # SP++
      self.asm_contents += INC_SP

  def Close(self):
    print(f"[*] Writing translation output to {self.fname}")
    with open(self.fname, 'w') as f:
      f.write(self.asm_contents)

