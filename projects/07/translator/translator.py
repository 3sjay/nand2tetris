import os
import sys
import parser
import code_writer
from enumerations import CommandType

def main():
  if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <file.vm/dir with .vm files>")
    sys.exit(1)


  # if 1. arg is a file, just translate for the file
  if os.path.isfile(sys.argv[1]):

    # init Parser
    p = parser.Parser(sys.argv[1])

    # init CodeWriter
    cw = code_writer.CodeWriter(sys.argv[1] + ".asm")

    while p.hasMoreCommands():
      p.advance()
      if p.commandType() == CommandType.C_RETURN:
        # do return stuff
        pass
      elif p.commandType() == CommandType.C_ARITHMETIC:
        cw.writeArithmetic(p.arg1(), p.current_cmd)

      elif p.commandType() == CommandType.C_PUSH or \
           p.commandType() == CommandType.C_POP:
        
        segment = p.arg1()
        index = p.arg2()

        cw.writePushPop(p.commandType(), segment, index, p.current_cmd)

    cw.Close()
        
      

  # if it is  a dir, translate for every .vm file
  elif os.path.isdir(sys.argv[1]):
    pass

  else:
    print(f"Usage: python3 {sys.argv[0]} <file.vm/dir with .vm files>")
    sys.exit(1)


if __name__ == "__main__":
  main()
