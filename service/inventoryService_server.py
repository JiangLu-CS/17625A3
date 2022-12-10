import inventoryService_pb2_grpc
import inventoryService_pb2
import grpc
from concurrent import futures
import book_pb2

# hardcode db
book1 = dict(isbn = "1", title = "book1", author = "Jane", genre = book_pb2.GENRE_HISTORICAL, publishing_year = 1980)
book2 = dict(isbn = "2", title = "book2", author = "Bob", genre = book_pb2.GENRE_MYSTERY, publishing_year = 2000)
book3 = dict(isbn = "3", title = "book3", author = "Lu", genre = book_pb2.GENRE_ROMANCE, publishing_year = 2021)
booklist = [book1, book2, book3]

class InventoryService(inventoryService_pb2_grpc.InventoryServiceServicer):

    def CreateBook(self, request, context):
        """Create a book
        """
        # avoid duplicate
        for b in booklist:
            if b["title"] == request.title:
                return inventoryService_pb2.CreateReply(isbn = "-1")

        # add book
        booklist.append(dict(isbn = str(len(booklist) + 1), title = request.title, 
        author = request.author, genre = request.genre, publishing_year = request.publishing_year))
        return inventoryService_pb2.CreateReply(isbn = str(len(booklist)))

    def GetBook(self, request, context):
        """Get a book
        """
        for b in booklist:
            if b["isbn"] == request.isbn:
                return inventoryService_pb2.GetReply(book = b)
        # book not exist
        return inventoryService_pb2.GetReply(book = dict(isbn = "-1", title = "", author = "", publishing_year = 0))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventoryService_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
