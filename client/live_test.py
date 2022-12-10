
import unittest
from inventory_client import Client
from get_book_titles import get_titles
import grpc
import inventoryService_pb2_grpc

class Test_get_book_titles(unittest.TestCase):
    def test_01(self):
        '''get book title success'''
        print("get book title success live test")
        # mock client api, each time return book1 as result
        client = Client()
        client.channel = grpc.insecure_channel('{}:{}'.format('localhost', 50051))
        client.stub = inventoryService_pb2_grpc.InventoryServiceStub(client.channel)
    
        # get book titles based on mock result
        book_title_list = get_titles(client, ["1", "2", "3"])
        print(book_title_list)
        self.assertEqual(len(book_title_list), 3)
        self.assertEqual(book_title_list[0], "book1")
        self.assertEqual(book_title_list[1], "book2")
        self.assertEqual(book_title_list[2], "book3")

    
    def test_02(self):
        '''get book title fail'''
        print("get book title fail live test")
        # get book titles 
        client = Client()
        client.channel = grpc.insecure_channel('{}:{}'.format('localhost', 50051))
        client.stub = inventoryService_pb2_grpc.InventoryServiceStub(client.channel)
    
        # if the book does not exist, should not include its title
        book_title_list = get_titles(client, ["not exist1", "not exist2"])
        print(book_title_list)
        self.assertEqual(len(book_title_list), 0)


if __name__ == "__main__":
    unittest.main()
