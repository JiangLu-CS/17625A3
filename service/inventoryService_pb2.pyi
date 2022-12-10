import book_pb2 as _book_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateReply(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    def __init__(self, isbn: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ["author", "genre", "publishing_year", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHING_YEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: _book_pb2.Genre
    publishing_year: int
    title: str
    def __init__(self, title: _Optional[str] = ..., author: _Optional[str] = ..., publishing_year: _Optional[int] = ..., genre: _Optional[_Union[_book_pb2.Genre, str]] = ...) -> None: ...

class GetReply(_message.Message):
    __slots__ = ["book"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: _book_pb2.Book
    def __init__(self, book: _Optional[_Union[_book_pb2.Book, _Mapping]] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    def __init__(self, isbn: _Optional[str] = ...) -> None: ...
