import inventoryService_pb2

class Client:
    def get_book(self, isbns):
        # call server
        request = inventoryService_pb2.GetRequest(isbn = isbns)
        print(f'{request}')
        print(self.stub.GetBook(request))
        return self.stub.GetBook(request)