from pypdf import PdfReader, PdfWriter, PdfMerger, DocumentInformation, PageObject
from pypdf._doc_common import PdfDocCommon
from pypdf.generic import RectangleObject
from pypdf.constants import PageAttributes as PG
from pypdf.constants import PagesAttributes as PA
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from typing import (
    IO,
    Any,
    Callable,
    Deque,
    Dict,
    Iterable,
    List,
    Optional,
    Pattern,
    Tuple,
    Type,
    Union,
    cast,
)

from pypdf.generic import (
    PAGE_FIT,
    ArrayObject,
    BooleanObject,
    ByteStringObject,
    ContentStream,
    DecodedStreamObject,
    Destination,
    DictionaryObject,
    Fit,
    FloatObject,
    IndirectObject,
    NameObject,
    NullObject,
    NumberObject,
    PdfObject,
    RectangleObject,
    StreamObject,
    TextStringObject,
    TreeObject,
    ViewerPreferences,
    create_string_object,
    hex_to_rgb,
)
