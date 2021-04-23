import unittest
import modulePlane


class TestMyModule(unittest.TestCase):

    vectorFinal = [1,2,3,4,5,6]

    vector1 = [1, 2, 3, [4, 5, [6]]]
    a = 1

    def test_vector1(self):
        self.assertEqual(modulePlane.printList(self.vector1), self.vectorFinal)


if __name__ == "__main__":
    unittest.main()
