from scripts import CA


def mix(n, s1, s2, c1, c2):
  i = (n - s2) / (s1 - s2)
  return int((c1 * i) + (c2 * (1 - i)))


def nontot_generate(b, s, c):
  c = int(c)
  result = f"""@RULE Wire_B{b.replace("-", "_")}_S{s.replace("-", "_")}_C{c}\n\n@TABLE\nn_states: {c + 1}\nneighborhood: Moore\nsymmetries: rotate4reflect\n\n"""
  var_dead = "0,1"
  for i in range(3, c + 1):
    var_dead += ","
    var_dead += str(i)
  for i in range(8):
    result += "var dead.{} = {}\n".format(i, "{" + var_dead + "}")
  for i in range(8):
    result += "var any.{} = {}\n".format(i, "{2," + var_dead + "}")
  result += "\n"
  bt = CA.parse(b)
  st = CA.parse(s)
  for i in bt:
    j = 0
    t = list(CA.transitions[i].replace("1", "2"))
    for k in range(8):
      if t[k] == "0":
        t[k] = f"dead.{j}"
        j += 1
    result += "1,{},2\n".format(",".join(t))
  for i in st:
    j = 0
    t = list(CA.transitions[i].replace("1", "2"))
    for k in range(8):
      if t[k] == "0":
        t[k] = f"dead.{j}"
        j += 1
    result += "2,{},2\n".format(",".join(t))
  result += "2,any.0,any.1,any.2,any.3,any.4,any.5,any.6,any.7,3\n"
  result += f"{c},any.0,any.1,any.2,any.3,any.4,any.5,any.6,any.7,1\n"
  for i in range(3, c):
    result += f"{i},any.0,any.1,any.2,any.3,any.4,any.5,any.6,any.7,{i + 1}\n"
  result += f"\n@COLORS\n0 48 48 48\n"
  result += "1 0 128 255\n"
  for i in range(2, c + 1):
    result += f"{i} {mix(i, c + 1, 2, 0, 255)} {mix(i, c + 1, 2, 128, 255)} {255}\n"
  return result


def tot_generate(b, s, c):
  c = int(c)
  result = f"""@RULE Wire_B{b.replace("-", "_")}_S{s.replace("-", "_")}_C{c}\n\n@TABLE\nn_states: {c + 1}\nneighborhood: Moore\nsymmetries: permute\n\n"""
  var_dead = "0,1"
  for i in range(3, c + 1):
    var_dead += ","
    var_dead += str(i)
  for i in range(8):
    result += "var dead.{} = {}\n".format(i, "{" + var_dead + "}")
  for i in range(8):
    result += "var any.{} = {}\n".format(i, "{2," + var_dead + "}")
  result += "\n"
  for i in b:
    result += "1,"
    for j in range(int(i)):
      result += "2,"
    for j in range(8 - int(i)):
      result += "dead.{},".format(j)
    result += "2\n"
  for i in s:
    result += "2,"
    for j in range(int(i)):
      result += "2,"
    for j in range(8 - int(i)):
      result += "dead.{},".format(j)
    result += "2\n"
  result += "2,any.0,any.1,any.2,any.3,any.4,any.5,any.6,any.7,3\n"
  result += f"{c},any.0,any.1,any.2,any.3,any.4,any.5,any.6,any.7,1\n"
  for i in range(3, c):
    result += f"{i},any.0,any.1,any.2,any.3,any.4,any.5,any.6,any.7,{i + 1}\n"
  result += f"\n@COLORS\n0 48 48 48\n"
  result += "1 255 128 0\n"
  for i in range(2, c + 1):
    result += f"{i} {mix(i, c + 1, 2, 0, 255)} {mix(i, c + 1, 2, 128, 255)} {255}\n"
  return result


def main(string):
  s, b, c = string.split("/")
  if CA.istotalistic(b) and CA.istotalistic(s):
    return tot_generate(b, s, c)
  else:
    return nontot_generate(b, s, c)
