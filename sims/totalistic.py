import matplotlib.pyplot as plt


Moore = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
c3D = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]
e3D = [(0, 1, 1), (0, 1, -1), (0, -1, 1), (0, -1, -1), (1, 0, 1), (1, 0, -1), (-1, 0, 1), (-1, 0, -1), (1, 1, 0),
       (1, -1, 0), (-1, 1, 0), (-1, -1, 0)]
f3D = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
Moore3D = c3D + e3D + f3D


fig = plt.figure()


class Simulator2D:
  def __init__(self, b, s, cells, neighborhood=Moore):
    self.b = [int(i) for i in list(b)]
    self.s = [int(i) for i in list(s)]
    self.cells = cells
    self.neighborhood = neighborhood
    self.range = max([abs(i[0]) for i in neighborhood] + [abs(i[1]) for i in neighborhood])
    self.plt = fig.add_subplot()

  def getboundaries(self):
    return [max([i[0] for i in self.cells]), max([i[1] for i in self.cells]), min([i[0] for i in self.cells]),
            min([i[1] for i in self.cells])]

  def sumneighbors(self, cell):
    return sum([int((cell[0] + i[0], cell[1] + i[1]) in self.cells) for i in self.neighborhood])

  def advance(self):
    bounds = self.getboundaries()
    new = []
    for x in range(bounds[2] - self.range, bounds[0] + 1 + self.range):
      for y in range(bounds[3] - self.range, bounds[1] + 1 + self.range):
        if (x, y) in self.cells:
          if self.sumneighbors((x, y)) in self.s:
            new.append((x, y))
        else:
          if self.sumneighbors((x, y)) in self.b:
            new.append((x, y))
    self.cells = new

  def plot(self):
    xs = [i[0] for i in self.cells]
    ys = [i[1] for i in self.cells]
    self.plt.scatter(xs, ys)


class Simulator3D:
  def __init__(self, b, s, cells, neighborhood=Moore3D):
    self.b = [int(i) for i in list(b)]
    self.s = [int(i) for i in list(s)]
    self.cells = cells
    self.neighborhood = neighborhood
    self.range = max([abs(i[0]) for i in neighborhood] + [abs(i[1]) for i in neighborhood] + [abs(i[2]) for i in neighborhood])
    self.plt = fig.add_subplot(projection="3d")

  def getboundaries(self):
    return [max([i[0] for i in self.cells]), max([i[1] for i in self.cells]), max([i[2] for i in self.cells]),
            min([i[0] for i in self.cells]), min([i[1] for i in self.cells]), min([i[2] for i in self.cells])]

  def sumneighbors(self, cell):
    return sum([int((cell[0] + i[0], cell[1] + i[1], cell[2] + i[2]) in self.cells) for i in self.neighborhood])

  def advance(self):
    bounds = self.getboundaries()
    new = []
    for x in range(bounds[3] - self.range, bounds[0] + 1 + self.range):
      for y in range(bounds[4] - self.range, bounds[1] + 1 + self.range):
        for z in range(bounds[5] - self.range, bounds[2] + 1 + self.range):
          if (x, y, z) in self.cells:
            if self.sumneighbors((x, y, z)) in self.s:
              new.append((x, y, z))
          else:
            if self.sumneighbors((x, y, z)) in self.b:
              new.append((x, y, z))
    self.cells = new

  def plot(self):
    xs = [i[0] for i in self.cells]
    ys = [i[1] for i in self.cells]
    zs = [i[2] for i in self.cells]
    self.plt.scatter(xs, ys, zs)
