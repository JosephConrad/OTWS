import copy


class Subset:

    def __init__(self, n):
        self.subsets = [[]]
        for i in range(1, n+1):
            new = []
            for elt in self.subsets:
                x = copy.deepcopy(elt)
                x.append(i)
                new.append(x)
            self.subsets.extend(new)

    def subsetSize(self, x):
        return len(filter(lambda subset: len(subset) == x, self.subsets))

if __name__ == "__main__":
    main()