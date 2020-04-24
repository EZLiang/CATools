import CA


def mix(n, s1, s2, c1, c2):
  i = (n - s2) / (s1 - s2)
  return int((c1 * i) + (c2 * (1 - i)))


def nontot_generations_generate(b, s, c):
  c = int(c)
  result = f"""@RULE B{b.replace("-", "_")}_S{s.replace("-", "_")}_C{c}\n\n@TABLE\nn_states: {c}\nneighborhood: Moore\nsymmetries: rotate4reflect\n\n"""
  var_dead = "0"
  for i in range(2, c):
    var_dead += ","
    var_dead += str(i)
  for i in range(8):
    result += "var dead.{} = {}\n".format(i, "{" + var_dead + "}")
  for i in range(8):
    result += "var any.{} = {}\n".format(i, "{1," + var_dead + "}")
  result += "\n"
  bt = CA.parse(b)
  st = CA.parse(s)
  for i in bt:
    j = 0
    t = list(CA.transitions[i])
    for k in range(8):
      if t[k] == "0":
        t[k] = f"dead.{j}"
        j += 1
    result += "0,{},1\n".format(",".join(t))
  for i in st:
    j = 0
    t = list(CA.transitions[i])
    for k in range(8):
      if t[k] == "0":
        t[k] = f"dead.{j}"
        j += 1
    result += "1,{},1\n".format(",".join(t))
  result += "1,any.0,any.1,any.2,any.3,any.4,any.5,any.6,any.7,2\n"
  result += f"{c - 1},any.0,any.1,any.2,any.3,any.4,any.5,any.6,any.7,0\n"
  for i in range(2, c - 1):
    result += f"{i},any.0,any.1,any.2,any.3,any.4,any.5,any.6,any.7,{i + 1}\n"
  result += f"\n@COLORS\n0 0 0 0\n"
  for i in range(1, c):
    result += f"{i} {mix(i, c, 1, 0, 255)} {mix(i, c, 1, 255, 0)} 0\n"
  return result


def tot_generations_generate(b, s, c):
  c = int(c)
  result = f"""@RULE B{b.replace("-", "_")}_S{s.replace("-", "_")}_C{c}\n\n@TABLE\nn_states: {c}\nneighborhood: Moore\nsymmetries: permute\n\n"""
  var_dead = "0"
  for i in range(2, c):
    var_dead += ","
    var_dead += str(i)
  for i in range(8):
    result += "var dead.{} = {}\n".format(i, "{" + var_dead + "}")
  for i in range(8):
    result += "var any.{} = {}\n".format(i, "{1," + var_dead + "}")
  result += "\n"
  for i in b:
    result += "0,"
    for j in range(int(i)):
      result += "1,"
    for j in range(8 - int(i)):
      result += "dead.{},".format(j)
    result += "1\n"
  for i in s:
    result += "1,"
    for j in range(int(i)):
      result += "1,"
    for j in range(8 - int(i)):
      result += "dead.{},".format(j)
    result += "1\n"
  result += "1,any.0,any.1,any.2,any.3,any.4,any.5,any.6,any.7,2\n"
  result += f"{c - 1},any.0,any.1,any.2,any.3,any.4,any.5,any.6,any.7,0\n"
  for i in range(2, c - 1):
    result += f"{i},any.0,any.1,any.2,any.3,any.4,any.5,any.6,any.7,{i + 1}\n"
  result += f"\n@COLORS\n0 0 0 0\n"
  for i in range(1, c):
    result += f"{i} {mix(i, c, 1, 0, 255)} {mix(i, c, 1, 255, 0)} 0\n"
  return result


def nontot_hensel_generate(b, s):
  result = f"""@RULE B{b.replace("-", "_")}_S{s.replace("-", "_")}\n\n@TABLE\nn_states: 2\nneighborhood: Moore\nsymmetries: rotate4reflect\n\n"""
  for i in range(8):
    result += "var any.{} = {}\n".format(i, "{0,1}")
  result += "\n"
  bt = CA.parse(b)
  st = CA.parse(s)
  for i in bt:
    t = list(CA.transitions[i])
    result += "0,{},1\n".format(",".join(t))
  for i in st:
    t = list(CA.transitions[i])
    result += "1,{},1\n".format(",".join(t))
  result += "1,any.0,any.1,any.2,any.3,any.4,any.5,any.6,any.7,0\n"
  result += f"\n@COLORS\n0 0 0 0\n1 255 255 255\n"
  return result


def tot_hensel_generate(b, s):
  result = f"""@RULE B{b.replace("-", "_")}_S{s.replace("-", "_")}\n\n@TABLE\nn_states: 2\nneighborhood: Moore\nsymmetries: permute\n\n"""
  for i in range(8):
    result += "var any.{} = {}\n".format(i, "{0,1}")
  result += "\n"
  for i in b:
    result += "0,"
    for j in range(int(i)):
      result += "1,"
    for j in range(8 - int(i)):
      result += "0,"
    result += "1\n"
  for i in s:
    result += "1,"
    for j in range(int(i)):
      result += "1,"
    for j in range(8 - int(i)):
      result += "0,"
    result += "1\n"
  result += "1,any.0,any.1,any.2,any.3,any.4,any.5,any.6,any.7,0\n"
  result += f"\n@COLORS\n0 0 0 0\n1 255 255 255\n"
  return result


def main(string):
  a = string.split("/")
  if len(a) == 3:
    if CA.istotalistic(a[1]) and CA.istotalistic(a[0]):
      return tot_generations_generate(a[1], a[0], a[2])
    else:
      return nontot_generations_generate(a[1], a[0], a[2])
  elif len(a) == 2:
    if a[0][0] == "B":
      if CA.istotalistic(a[0][1:]) and CA.istotalistic(a[1][1:]):
        return tot_hensel_generate(a[0][1:], a[1][1:])
      else:
        return nontot_hensel_generate(a[0][1:], a[1][1:])
    else:
      if CA.istotalistic(a[0]) and CA.istotalistic(a[1]):
        return tot_hensel_generate(a[1], a[0])
      else:
        return nontot_hensel_generate(a[1], a[0])
  else:
    return "Invalid string!"
