from enum import Enum, auto

class CommandType(Enum):
  C_ARITHMETIC = "C_ARITHMETIC"
  C_PUSH       = "C_PUSH"
  C_POP        = "C_POP"
  C_LABEL      = auto()
  C_GOTO       = auto()
  C_IF         = auto()
  C_FUNCTION   = auto()
  C_RETURN     = auto()
  C_CALL       = auto()
  NOT_IMPLEMENTED = auto() # for errors
