import sys
from scripts import circuitgen, tablegen

processes = {
  "circuit": circuitgen.main,
  "toruletable": tablegen.main
}


def main():
  process = sys.argv[1]
  args = sys.argv[2:]
  if not (process in processes):
    print("Program {} not found!".format(process))
    return -1
  try:
    print(processes[process](*args))
  except TypeError:
    print("Invalid arguments!")
    return -1
  return 0


if __name__ == "__main__":
  main()
