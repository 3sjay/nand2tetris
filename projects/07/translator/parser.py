# parser - handles the parsing of a single .vm file and encapsulates access to the input code
# it reads VM commands, parses them, and proivdes convenient access to their components.
# In addition, it removes all white spaces and comments.

from enumerations import CommandType


ARITHMETIC_CMDS = ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]

class Parser:

  lines = ""
  lines_idx = 0
  current_cmd = ""
  
  def __init__(self, fname: str):
    with open(fname) as f:
      self.lines = f.readlines()
    
  def hasMoreCommands(self) -> bool:
    if self.lines_idx + 1 > len(self.lines):
      return False
    if self.lines_idx == len(self.lines):
      if not isCmd(lines[self.lines_idx]):
        return False
    return True
    
  def advance(self):
    self.current_cmd = self.cleanCmd(self.lines[self.lines_idx])
    # lowercase all letters for later parsing
    self.current_cmd = self.current_cmd.lower()
    # increment lines index 
    self.lines_idx += 1

  def commandType(self) -> CommandType:
    if self.current_cmd.startswith("push"):
      return CommandType.C_PUSH

    elif self.current_cmd.startswith("pop"):
      return CommandType.C_POP

    elif self.current_cmd.split(" ")[0] in ARITHMETIC_CMDS:
      return CommandType.C_ARITHMETIC

    elif self.current_cmd.startswith("goto"):
      return CommandType.C_GOTO

    elif self.current_cmd.startswith("function"):
      return CommandType.C_FUNCTION

    elif self.current_cmd.startswith("label"):
      return CommandType.C_LABEL

    elif self.current_cmd.startswith("if"):
      return CommandType.C_IF

    elif self.current_cmd.startswith("return"):
      return CommandType.C_RETURN

    # assumption as no CALL statement has been observed yet
    elif self.current_cmd.startswith("call"):
      return CommandType.C_CALL

    else:
      return CommandType.NOT_IMPLEMENTED

  def arg1(self) -> str:
    cmdType = self.commandType()
    assert(cmdType != CommandType.C_RETURN)

    print(self.current_cmd)
    if cmdType == CommandType.C_ARITHMETIC:
      return self.current_cmd.split(" ")[0]
    else:
      return self.current_cmd.split(" ")[1]

  def arg2(self) -> int:
    cmdType = self.commandType()
    assert(cmdType == CommandType.C_PUSH or \
           cmdType == CommandType.C_POP or \
           cmdType == CommandType.C_FUNCTION or \
           cmdType == CommandType.C_CALL)

    assert(len(self.current_cmd.split(" ")) == 3)

    return int(self.current_cmd.split(" ")[2])

  def isCmd(self, cmd: str) -> bool:
    cmd = self.cleanCmd(cmd)
    if cmd == "" :
      return False
    return True

  def cleanCmd(self, cmd: str) -> str:
    #cmd = cmd.strip("\n") # remove the trailing newline
    #cmd = cmd.replace(" ", "").replace("\t", "")
    cmd = cmd.replace("\t", "")
    cmd = cmd[:cmd.find("//")]
    return cmd
    
