import copy
import sys


class Subset:

    def __init__(self, n):
        self.subsets = [""]
        for i in range(1, n+1):
            new = []
            for elt in self.subsets:
                x = elt 
                x += str(i)
                new.append(x)
            self.subsets += new

    def subsetSize(self, x):
        return len(filter(lambda subset: len(subset) == x, self.subsets))

def main():
	subset = Subset(int(sys.argv[1]))

if __name__ == "__main__":
    main()
