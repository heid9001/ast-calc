from re import match
import analyzer


s = "2*3+2^3+4"
operators = analyzer.tokenize(s)
analyzer.analyze(operators)
root = sorted(operators, key=lambda e: len(e), reverse=True)[0]

# just printing syntax tree
root.traverse()

print ("answer: ", analyzer.traverse(root))