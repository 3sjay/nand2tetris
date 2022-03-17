import sys


predef_symbols = {"R0" : 0, "R1" : 1, "R2" : 2, "R3" : 3, "R4" : 4, "R5" : 5, "R6" : 6, "R7" : 7, "R8" : 8, "R9" : 9, "R10" : 10, "R11" : 11, "R12" : 12, "R13" : 13, "R14" : 14, "R15" : 15, "SCREEN" : 16384, "KBD" : 24576, "SP" : 0, "LCL" : 1, "ARG" : 2, "THIS" : 3, "THAT" : 4}

symbol_dict = {}

var_dict = {}

if len(sys.argv) != 2:
  print(f"Usage: {sys.argv[0]} text.asm")
  sys.exit(1)

# Clean line of spaces, tabs and comments
def clean_line(line):
  l = line.replace(" ", "")
  l = line.replace("\t", "")
  if "//" in l:
    l = l[:l.find("/")]
  return l

# fill the symbol_dict 
with open(sys.argv[1]) as f:
  line_num = 0
  for l in f.readlines():
    l = l.strip()
    l = clean_line(l)

    if l == "":
      continue
    if "(" in l:
      # this is a symbol we want to store in the global symbol dictionary
      sym_name = l.split("(")[1].split(")")[0]
      symbol_dict[sym_name] = line_num
    else:
      line_num += 1
  #for k,v in symbol_dict.items():
  #  print(k,v)

with open(sys.argv[1]) as f:
  line_num = 0
  current_var_num = 16
  for l in f.readlines():
    l = l.strip()
    l = clean_line(l)
    if l == "":
      continue


    if "@" in l:
      # label/variable or constant
      value = l.split("@")[1]
      try:
        # if constant - we immediatly print the corresponding A-instruction
        i = int(value)
        print(format(i, "016b"))
        
      except ValueError:
        if value in predef_symbols.keys():
          i = predef_symbols[value]
          print(format(i, "016b"))
        elif value in symbol_dict.keys():
          i = symbol_dict[value]
          print(format(i, "016b"))
        else:
          # this is a variable
          #print("IN VARIABLE STATEMENT")
          if value in var_dict.keys():
            # this is already known and we just replace the value
            i = var_dict[value]
            print(format(i, "016b"))
          else:
            var_dict[value] = current_var_num
            print(format(current_var_num, "016b"))
            current_var_num += 1


      except Exception as e:
        print(e)
    else:
      # this is a C-instruction
      a = 0
      d1, d2, d3 = 0,0,0
      j1, j2, j3 = 0,0,0
      c1, c2, c3, c4, c5, c6 = 0,0,0,0,0,0

      if "=" in l:
        # we need to assign something
        left, right = l.split("=")
        right = right.replace(" ", "").replace("\t", "")
        #print(f"LEFT: {left} - RIGHT: {right} (=)")

        # set the dest parts
        if "A" in left:
          d1 = 1
        if "D" in left:
          d2 = 1
        if "M" in left:
          d3 = 1

        # set the comp parts
        if right == "0":
          c1, c2, c3, c4, c5, c6 = 1,0,1,0,1,0
        if right == "1":
          c1, c2, c3, c4, c5, c6 = 1,1,1,1,1,1
        if right == "-1":
          c1, c2, c3, c4, c5, c6 = 1,1,1,0,1,0
        if right == "D":
          c1, c2, c3, c4, c5, c6 = 0,0,1,1,0,0
        if right == "A" or right == "M":
          c1, c2, c3, c4, c5, c6 = 1,1,0,0,0,0
        if right == "!D":
          c1, c2, c3, c4, c5, c6 = 0,0,1,1,0,1
        if right == "!A" or right == "!M":
          c1, c2, c3, c4, c5, c6 = 1,1,0,0,0,1
        if right == "-D":
          c1, c2, c3, c4, c5, c6 = 0,0,1,1,1,1
        if right == "-A" or right == "-M":
          c1, c2, c3, c4, c5, c6 = 1,1,0,0,1,1
        if right == "D+1":
          c1, c2, c3, c4, c5, c6 = 0,1,1,1,1,1
        if right == "A+1" or right == "M+1":
          c1, c2, c3, c4, c5, c6 = 1,1,0,1,1,1
        if right == "D-1":
          c1, c2, c3, c4, c5, c6 = 0,0,1,1,1,0
        if right == "A-1" or right == "M-1":
          c1, c2, c3, c4, c5, c6 = 1,1,0,0,1,0
        if right == "D+A" or right == "D+M":
          c1, c2, c3, c4, c5, c6 = 0,0,0,0,1,0
        if right == "D-A" or right == "D-M":
          c1, c2, c3, c4, c5, c6 = 0,1,0,0,1,1
        if right == "A-D" or right == "M-D":
          c1, c2, c3, c4, c5, c6 = 0,0,0,1,1,1
        if right == "D&A" or right == "D&M":
          c1, c2, c3, c4, c5, c6 = 0,0,0,0,0,0
        if right == "D|A" or right == "D|M":
          c1, c2, c3, c4, c5, c6 = 0,1,0,1,0,1
          
        if "M" in right:
          a = 1




      elif ";" in l:
        # we will jmp ... maybe
        left, right = l.split(";")
        right = right.replace(" ", "").replace("\t", "")
        #print(f"LEFT: {left} - RIGHT: {right} (;)")
        # set the comp field to D
        c1, c2, c3, c4, c5, c6 = 0,0,1,1,0,0
        # set the jump parts
        if "JGT" in right:
          j3 = 1
        if "JEQ" in right:
          j2 = 1
        if "JGE" in right:
          j2, j3 = 1,1
        if "JLT" in right:
          j1 = 1
        if "JNE" in right:
          j1, j3 = 1,1
        if "JLE" in right:
          j1, j2 = 1,1
        if "JMP" in right:
          j1, j2, j3 = 1,1,1
          c1, c2, c3, c4, c5, c6 = 1,0,1,0,1,0

      elif "(" in l:
        continue
      else:
        #print(f"whatz this: {l}")
        continue
      out = f"111{a}{c1}{c2}{c3}{c4}{c5}{c6}{d1}{d2}{d3}{j1}{j2}{j3}"
      #print(f"DBG: {l} -> {out}")
      print(out)

    # increment the line num
    line_num += 1





