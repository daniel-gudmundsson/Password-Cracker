import argparse
import itertools

#def leet(word, i):
#    if i >= len(word):
#        return word
#    for c in word[i:]:
#        leetSymbols = leetDictonary[c]
#        leetSymbols.append(c)
#        for symbol in leetSymbols:
#            ans.append(leet(symbol+word[i+1:], i+1))


def leet(word, leetDictonary):
    symbolLists = []
    for c in word:
        
        if c.lower() in leetDictonary:
            symbolLists.append(leetDictonary[c.lower()])
        else:
            symbolLists.append([c])
    res = leetHelper(symbolLists)
    return res

def leetHelper(lsts):
    return list(itertools.product(*lsts))

def wordToLeet(pw):
#    leetDictonary = {'a': ['4'],
#                 'b': ['b'],
#                 'c':  ['c'],
#                 'd': ['d'],
#                 'e': ['3'],
#                 'f': ['f'],
#                 'g': ['6'],
#                 'h': ['h'],
#                 'i': ['1'],
#                 'j': ['1'],
#                 'k': ['k'],
#                 'l': ['1'], 
#                 'm': ['m'],
#                 'n': ['n'],
#                 'o': ['0'],
#                 'p': ['p'],
#                 'q': ['9'],
#                 'r': ['r'],
#                 's': ['5'],
#                 't': ['7'],
#                 'u': ['u'],
#                 'v':['v'],
#                 'w': ['w'],
#                 'x': ['x'],
#                 'y': ['y'],
#                 'z': ['2'],
#                 '0': ['o'],
#                '1': ['l'],
#                '2': ['z','Z'],
#                '3': ['e', 'E'],
#                '4': ['a', 'A', 'h'],
#                '5': ['s', 'S'],
#                '6': ['g', 'G'],
#                '7': ['t', 'T'],
#                '8': ['b', 'B'],
#                '9': ['g', 'G']
#                 }
    leetDictonary = {'a': ['a','4'],
                 'b': ['b'],
                 'c':  ['c'],
                 'd': ['d'],
                 'e': ['e','3'],
                 'f': ['f'],
                 'g': ['g''6'],
                 'h': ['h'],
                 'i': ['i','1'],
                 'j': ['j','1'],
                 'k': ['k'],
                 'l': ['l','1'], 
                 'm': ['m'],
                 'n': ['n'],
                 'o': ['o','0'],
                 'p': ['p'],
                 'q': ['q','9'],
                 'r': ['r'],
                 's': ['s','5'],
                 't': ['t','7'],
                 'u': ['u'],
                 'v':['v'],
                 'w': ['w'],
                 'x': ['x'],
                 'y': ['y'],
                 'z': ['z','2'],
                 '0': ['0','o'],
                '1': ['1','l'],
                '2': ['2','z','Z'],
                '3': ['3','e', 'E'],
                '4': ['4','a', 'A', 'h'],
                '5': ['5','s', 'S'],
                '6': ['6','g', 'G'],
                '7': ['7','t', 'T'],
                '8': ['8','b', 'B'],
                '9': ['9','g', 'G']
                }
    return list(map(lambda x: "".join(x), leet(pw, leetDictonary)))

#parser = argparse.ArgumentParser('73x7 70 l3375p34k')
#parser.add_argument('file', help="The text file")
#parser.add_argument('output', help="The output")
#args = parser.parse_args()
#encoded = []
#file = args.file
#output = args.output
leetDictonary = {'a': ['a','4'],
                 'b': ['b'],
                 'c':  ['c'],
                 'd': ['d'],
                 'e': ['3','e'],
                 'f': ['f'],
                 'g': ['g','6'],
                 'h': ['h'],
                 'i': ['1', 'i', 'l'],
                 'j': ['j', 'i', '1', 'l'],
                 'k': ['k'],
                 'l': ['l', 'i', '1', 'j'], 
                 'm': ['m'],
                 'n': ['n'],
                 'o': ['0'],
                 'p': ['p'],
                 'q': ['q', '9'],
                 'r': ['r'],
                 's': ['s', '5'],
                 't': ['t', '7'],
                 'u': ['u'],
                 'v':['v', 'u'],
                 'w': ['w', 'vv', 'uu', '2u'],
                 'x': ['x', '*', '+'],
                 'y': ['y'],
                 'z': ['z', '2'],
                 '0': ['o', '0'],
                '1': ['1', 'i', 'l', 'I', 'L'],
                '2': ['2', 'z','Z'],
                '3': ['3', 'e', 'E'],
                '4': ['4', 'a', 'A', 'h', 'H'],
                '5': ['5', 's', 'S'],
                '6': ['6', 'b', 'B', 'g', 'G'],
                '7': ['7', 't', 'T'],
                '8': ['8', 'b', 'B', 'x', 'X'],
                '9': ['9', 'g', 'G', 'j', 'J']
                 }

                
                
                
                
                
                
                
                