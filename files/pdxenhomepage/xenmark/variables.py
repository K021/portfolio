import re
from typing import NamedTuple

__all__ = (
    'PATTERN_HEADER_1',
    'PATTERN_HEADER_2',
    'PATTERN_HEADER_3',
    'PATTERN_HEADER_4',
    'PATTERN_PARAGRAPH',
    'PATTERN_LINK',
    'PATTERN_HIGHLIGHT',
    'PATTERN_IMAGE',
    'PATTERN_BORDER_LINE',
    'PATTERN_UNORDERED_LIST',
    'PATTERN_ORDERED_LIST',
    'PATTERN_TWO_COLUMN_LIST',

    'PATTERN_REDUNDANT_NEWLINE',

    'HEADER_1',
    'HEADER_2',
    'HEADER_3',
    'HEADER_4',
    'PARAGRAPH',
    'LINK',
    'HIGHLIGHT',
    'IMAGE',
    'BORDER_LINE',
    'UNORDERED_LIST',
    'ORDERED_LIST',
    'TWO_COLUMN_LIST',

    'COLUMN_NUMBER_1',
    'COLUMN_NUMBER_2',
    'COLUMN_END',
)

__all__ += (
    'LinkData',
    'HighlightData',
)

# Patterns
PATTERN_HEADER_1 = re.compile(r'^#(?!#)[ ]*')
PATTERN_HEADER_2 = re.compile(r'^##(?!#)[ ]*')
PATTERN_HEADER_3 = re.compile(r'^###(?!#)[ ]*')
PATTERN_HEADER_4 = re.compile(r'^####(?!#)[ ]*')
PATTERN_PARAGRAPH = re.compile(r'^@[ ]*')
PATTERN_LINK = re.compile(r'\[(?P<link_name>.+?)\]\((?P<link_address>.+?)\)')
PATTERN_HIGHLIGHT = re.compile(r'`(?P<content>.+?)`')
PATTERN_IMAGE = re.compile(r'\|\((?P<img_name>\S+)\)\|')
PATTERN_BORDER_LINE = re.compile(r'^[ ]*-{3,}[ \n]*$')
PATTERN_UNORDERED_LIST = re.compile(r'^[ ]*-[ ]+')
PATTERN_ORDERED_LIST = re.compile(r'^[ ]*\d+[.][ ]+')
PATTERN_TWO_COLUMN_LIST = re.compile(r'^\|2-(?P<cn>[120])\|(?!^ \n)')

# '\n    '을 허용
# 그 뒤에 #, @, |, -, 공백, 123.공백 중 하나가 오지 않는 경우
PATTERN_REDUNDANT_NEWLINE = re.compile(r'\n[ ]*(?![#@|\- ]|(\d+[.][ ]+))')

# line properties
HEADER_1 = 'header_1'
HEADER_2 = 'header_2'
HEADER_3 = 'header_3'
HEADER_4 = 'header_4'
PARAGRAPH = 'paragraph'
LINK = 'link'
HIGHLIGHT = 'highlight'
IMAGE = 'image'
BORDER_LINE = 'border_line'
UNORDERED_LIST = 'unordered_list'
ORDERED_LIST = 'ordered_list'
TWO_COLUMN_LIST = 'two_column_list'

# column variables
COLUMN_NUMBER_1 = '|2-1|'
COLUMN_NUMBER_2 = '|2-2|'
COLUMN_END = '|2-0|'


class LinkData(NamedTuple):
    xenmark: str
    name: str
    address: str


class HighlightData(NamedTuple):
    xenmark: str
    content: str
