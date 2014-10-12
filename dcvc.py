import sys
import random
from subset import Subset

# A -set of agents
A = {1,2,3,4,5,6}
# n - number of agents
n = len(A)
# S - set of permitted coalition sizes
S = {1,2,3,4,5,6}


def evalFunction(index, myShare):
    return [random.random() for i in range(myShare)]

def printResult(result, string):
    result = '\n'.join(format(x, "10.3f") for x in result)
    print string+' eval function: \n{0}'.format(result)

def main():
    # alp - alpha
    alp = 1
    ID = int(sys.argv[1])
    subsets = Subset(n)
    for s in S:
        print '\nProcessing {0}-element subsets...'.format(s)

        Ns = subsets.subsetSize(s)
        if Ns >= n:
            myShare = subsets.subsetSize(s)/n
            index = ID * myShare
            toPrint = (myShare, index)
            print 'Start from {1} and process upper {0} elts'.format(*toPrint)
            result = evalFunction(index, myShare)
            printResult(result, "Normal")
            NPrim = Ns - (n * myShare)
        else:
            NPrim = Ns

        if NPrim > 0:
            APrim = range(alp, alp+NPrim) if alp+NPrim-1 <= n else \
                    range(alp, n+1) + range(1, alp+NPrim-n)
            print "Residual indexes: \n" + str(APrim)
            if ID in APrim:
                printResult(evalFunction(APrim.index(ID), 1), "Residual")
            alp += NPrim if alp + NPrim <= n else NPrim - n

if __name__ == "__main__":
    main()