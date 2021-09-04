from space_probe import SpaceProbe
import sys


def read_file():
    highland = [(0, 0), (0, 0)]
    space_probes = []
    x, y, direction, instructions = 0, 0, '', ""
    GETTING_SIZE = 0
    GETTING_INITIAL_POINT = 1
    GETTING_INSTRUCTIONS = 2
    step = GETTING_SIZE
    for line in sys.stdin:
        line = line.strip()
        if line:
            if step == GETTING_SIZE:
                input = line.split()
                x, y = int(input[0]), int(input[1])
                highland[1] = (x, y)
                step = GETTING_INITIAL_POINT
            elif step == GETTING_INITIAL_POINT:
                input = line.split()
                x, y, direction = int(input[0]), int(input[1]), input[2]
                step = GETTING_INSTRUCTIONS
            elif step == GETTING_INSTRUCTIONS:
                instructions = line
                space_probes.append(SpaceProbe(x, y, direction, instructions))
                step = GETTING_INITIAL_POINT
    return highland, space_probes


if __name__ == "__main__":
    highland, space_probes = read_file()
    for probe in space_probes:
        probe.run(highland)