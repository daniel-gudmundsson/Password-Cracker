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


def leet(word):
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

parser = argparse.ArgumentParser('73x7 70 l3375p34k')
parser.add_argument('file', help="The text file")
parser.add_argument('output', help="The output")
args = parser.parse_args()
encoded = []
file = args.file
output = args.output
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
#leetDictonary = {'a': ['a','4', '/-\\', '/_\\', '@', '/\\'],
#             'b': ['b', '8','|3', '13', '|}', '|:', '|8', '18', '6', '|B', '|8', 'lo', '|o', 'j3', 'ß'],
#             'c': ['c','<', '{', '[', '(', '©', '¢'],
#             'd': ['d','|)', '|}', '|]', '|>'],
#             'e': ['e','3', '£', '₤', '€'],
#             'f': ['f','|=', 'ph', '|#', '|"'],
#            'g':  ['g', '[', '-', '[+', '6', 'C-'],
#            'h':  ['h','4', '|-|', '[-]', '{-}', '}-{', '}{', '|=|', '[=]', '{=}', '/-/', '(-)', ')-(', ':-:', 'I+I'],
#            'i': ['i','1', '|', '!', '9'],
#            'j': ['j','_|', '_/', '_7', '_)', '_]', '_}'],
#            'k':  ['k','|<', '1<', 'l<', '|{', 'l{'],
#            'l': ['l','|_', '|', '1', ']['],
#            'm': ['m','44', '|\/|', '^^', '/\/\\', '/X\\', '[]\/][', '[]V[]', '][\\//][', '(V)','//.', '.\\', 'N\\'],
#            'n':  ['n', '|\|', '/\/', '/V', '][\\][', 'И'],
#            'o': ['o', '0', '()', '[]', '{}', '<>', 'Ø', 'oh'],
#            'p': ['p','|o', '|O', '|>', '|*', '|°', '|D', '/o', '[]D', '|7'],
#            'q': ['q','O_', '9', '(,)', '0','kw'],
#            'r': ['r','|2', '12', '.-', '|^', 'l2', 'Я', '®'],
#            's': ['s','5', '$', '§'],
#            't':  ['t','7', '+', '7`', "'|'" , "`|`" , '~|~' , '-|-', "']['"],
#            'u': ['u','|_|', '\_\\', '/_/', '\_/', '(_)', '[_]', '{_}'],
#            'v':  ['v','\/'],
#            'w':  ['w','\/\/', '(/\)', '\^/', '|/\|', '\X/', "\\'", "'//", 'VV', '\_|_/', '\\//\\//', 'Ш', '2u', '\V/'],
#            'x': ['x','%', '*', '><', '}{', ')(', 'Ж'],
#            'y': ['y',"`/", '¥', '\|/', 'Ч'],
#            'z': ['z','2', '5', '7_', '>_','(/)'],
#            '0': ['0','o', 'O', 'd', 'D', ' '],
#            '1': ['1','i','I', 'l', 'L'],
#            '2': ['2', 'z', 'Z', 'r', 'R'],
#            '3': ['3','e', 'E'],
#            '4': ['4','h', 'H', 'a', 'A',],
#            '5': ['5','s', 'S'],
#            '6': ['6','b', 'B', 'g', 'G'],
#            '7': ['7','T', 't', 'j', 'J'],
#            '8': ['8','b', 'B', 'x', 'X'],
#            '9': ['9','g', 'G', 'j', 'J'],
#            '10': ['10','i', 'I', 'o', 'O'],
#            '11': ['11','n', 'N']
#            }
#    

       
#ans = []
#
#test = 'abba'
#
#res = leet2(test)

#print(res)

with open(file, "r") as f_in:
    with open(output, "w") as f_out:
        for l in f_in:
            l = l.strip(" \r\n")
            if not l or len(l)==0: continue
            res = leet(l)
            for word in res:
                f_out.write("%s\n" %"".join(word))
                
                
                
                
                
                
                
                
                
                