from unittest import mock
import unittest
from get_book_titles import get_titles
import get_book_titles
from inventory_client import Client


book1 = dict(isbn = "1", title = "book1", author = "Jane", publishing_year = 1980)
notExistRes = dict(isbn = "-1")

class Test_get_book_titles(unittest.TestCase):
    def test_01(self):
        '''get book title success'''
        print("get book title success mock test")
        # mock client api, each time return book1 as result
        client = Client()
        client.get_book = mock.Mock(return_value = book1)
        # get book titles based on mock result
        book_title_list = get_titles(client, ["1", "2", "3"])
        print(book_title_list)
        self.assertEqual(len(book_title_list), 3)
        self.assertEqual(book_title_list[0], "book1")
        self.assertEqual(book_title_list[1], "book1")
        self.assertEqual(book_title_list[2], "book1")

    
    def test_02(self):
        '''get book title fail'''
        print("get book title fail mock test")
        # mock client api, each time return book1 as result
        # get book titles based on mock result
        client = Client()
        client.get_book = mock.Mock(return_value = notExistRes)
        # if the book does not exist, should not include its title
        book_title_list = get_titles(client, ["not exist1", "not exist2"])
        print(book_title_list)
        self.assertEqual(len(book_title_list), 0)


if __name__ == "__main__":
    unittest.main()
