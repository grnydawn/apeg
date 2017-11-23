from context import apeg
import unittest, sys, os

here = os.path.dirname(os.path.realpath(__file__))
grammar_test = 'fruites'
#grammar_test = 'simple'
grammar_rules = os.path.join(here, 'grammar_%s.txt'%grammar_test)
sample_input = os.path.join(here, 'sample_%s.txt'%grammar_test)

class TestParser(unittest.TestCase):

    def test_apeg(self):
        with open(grammar_rules, 'r') as fg:
            grammar = apeg.Grammar(fg.read())
            with open(sample_input, 'r') as fi:
                input_text = fi.read().strip()
                tree = grammar.parse(input_text)
                print(str(tree))

if __name__ == '__main__':
    unittest.main.main()
