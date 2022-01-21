# -*- coding: utf-8 -*-
import unittest

from ternary_search_tree import Node, insert, in_order_print, retrieve_value

class TestTree(unittest.TestCase):
    def setUp(self):
        self.root = Node(12, 'twelve')
        insert(self.root, Node(6, 'six'))
        insert(self.root, Node(11, 'eleven'))
        insert(self.root, Node(3, 'three'))
        insert(self.root, Node(10, 'ten'))
        insert(self.root, Node(8, 'eight'))
        insert(self.root, Node(14, 'fourteen'))
        print('\nTree in order:')
        in_order_print(self.root)

    def test_non_existent_value_retrieval(self):
        """
        Test that it can retrieve the values entered by searching
        """
        result = retrieve_value(self.root, 7)
        self.assertEqual(result, None)

    def test_existent_value_retrieval(self):
        """
        Test that it can retrieve the values entered by searching
        """
        result = retrieve_value(self.root, 14)
        self.assertEqual(result, 'fourteen')

    def test_directional_value_retrieval(self):
        self.assertEqual(retrieve_value(self.root, 14, direction='left'), None)
        self.assertEqual(retrieve_value(self.root, 14, direction='middle'), None)
        self.assertEqual(retrieve_value(self.root, 14, direction='right'), 'fourteen')

        self.assertEqual(retrieve_value(self.root, 11, direction='left'), None)
        self.assertEqual(retrieve_value(self.root, 11, direction='middle'), 'eleven')
        self.assertEqual(retrieve_value(self.root, 11, direction='right'), None)

if __name__ == '__main__':
    unittest.main()
