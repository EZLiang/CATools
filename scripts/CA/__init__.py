"""
Evin Liang's Python CA utilities
"""

transitions = {
  "0": "00000000",
  "1c": "01000000", "1e": "10000000",
  "2c": "01010000", "2e": "10100000", "2k": "10010000", "2a": "11000000", "2i": "10001000", "2n": "01000100",
  "3c": "01010100", "3e": "10101000", "3k": "10100100", "3a": "11100000", "3i": "01110000", "3n": "11010000",
          "3y": "10010100", "3q": "11000100", "3j": "11000010", "3r": "11001000",
  "4c": "01010101", "4e": "10101010", "4k": "11010010", "4a": "11110000", "4i": "11011000", "4n": "11000101",
          "4y": "11010100", "4q": "11100100", "4j": "11010100", "4r": "11101000", "4t": "11001001", "4w": "11011000",
          "4z": "11001100",
  "5c": "10101011", "5e": "11010101", "5k": "11010110", "5a": "11110001", "5i": "11111000", "5n": "11101001",
          "5y": "11011010", "5q": "11101100", "5j": "11110100", "5r": "11011100",
  "6c": "11111010", "6e": "11110101", "6k": "10111101", "6a": "11111100", "6i": "11011101", "6n": "11101110",
  "7c": "11111110", "7e": "01111111",
  "8": "11111111"
}


def parse(string):
  s = string.replace("1", "|1").replace("2", "|2").replace("3", "|3").replace("4", "|4").replace("5", "|5").replace("5", "|5").replace("7", "|7").replace("8", "|8").split("|")
  st = []
  for i in s:
    if not (i == ""):
      t = list(i)
      n = t.pop(0)
      if t == []:
        for j in transitions:
          if j[0] == n:
            st.append(j)
      elif t[0] == "-":
        del t[0]
        ts = []
        for j in transitions:
          if j[0] == n:
            ts.append(j[1])
        for j in ts:
          if not (j in t):
            st.append(f"{n}{j}")
      else:
        for j in transitions:
          if j[0] == str(n):
            st.append(f"{j}")
  return st


def istotalistic(string):
  if string == "":
    return True
  try:
    int(string)
    return True
  except:
    return False
