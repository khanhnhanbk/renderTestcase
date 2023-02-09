import os
import sys

def read_file(path):
    with open(path, 'r') as f:
        content = f.read()
        # replace escape characters
        content = content.translate(str.maketrans({'\r': '\\r', '\t': '\\t', '\n': '\\n', '\\': '\\\\', '\f': '\\f', '\b': '\\b'}))
        return content

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def create_def(name, testcase, expect):
    return f"""    def test{name}(self):
        testcase = '''{testcase}'''
        expect = '''{expect}'''
        self.assertTrue(TestLexer.test(testcase, expect, {name}))"""

if __name__ == '__main__':
    testcases_folder = 'testcases'
    expected_folder = 'expected'
    output_file = 'LexerSuite.py'
    testcases = os.listdir(testcases_folder)
    expected = os.listdir(expected_folder)
    testcases.sort()
    expected.sort()
    content = """import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
"""

    content += '\n'.join([create_def(i, read_file(os.path.join(testcases_folder, t)), read_file(os.path.join(expected_folder, e))) for i, (t, e) in enumerate(zip(testcases, expected))])
    write_file(output_file, content)