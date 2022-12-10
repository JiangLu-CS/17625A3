from inventory_client import Client
import grpc
import inventoryService_pb2_grpc


isbn_list = ["1", "2", "3"]

def get_titles(client, isbn_list):
    book_title_list = []
    for i in isbn_list:
        b = client.get_book(isbns = i)
        if b.book.isbn == "-1":
            continue
        book_title_list.append(b.book.title)
    return book_title_list


if __name__ == '__main__':
    client = Client()

    client.channel = grpc.insecure_channel('{}:{}'.format('localhost', 50051))

    # bind the client and the server
    client.stub = inventoryService_pb2_grpc.InventoryServiceStub(client.channel)
    book_title_list = get_titles(client, isbn_list)
    print(book_title_list)
