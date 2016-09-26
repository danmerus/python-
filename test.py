import unittest
import tempfile
import suggest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.words_file = tempfile.mktemp()
        with open(self.words_file, 'w') as f:
            f.write('word1\n')
            f.write('word2\n')
        self.suggester = suggest.Suggester(self.words_file)

    def test_sample(self):
        self.assertIn('word1', self.suggester.get('w'))

    

if __name__ == '__main__':
    unittest.main()