"""
This module contains functions that converts xenmark to html on a line basis
"""

from .variables import *
from post.models import POST_IMG_UPLOAD_PATH

__all__ = (
    'line_property',
    'line_formatter',

    'link_inspector',
    'highlight_inspector',

    'is_header_1',
    'is_header_2',
    'is_header_3',
    'is_header_4',
    'is_paragraph',
    'is_link',
    'is_highlight',
    'is_image',
    'is_border_line',
    'is_unordered_list',
    'is_ordered_list',
    'is_two_column_list',

    'list_wrapper',
    'unordered_list_wrapper',
    'ordered_list_wrapper',
    'two_column_list_wrapper',
)


def line_property(string):
    """
    Returns property of the given xenmark line
    If the given string is not xenmark-type, returns None
    :param string: xenmark line
    :return: xenmark line property or None
    """
    if is_header_1(string):
        return HEADER_1
    elif is_header_2(string):
        return HEADER_2
    elif is_header_3(string):
        return HEADER_3
    elif is_header_4(string):
        return HEADER_4
    elif is_paragraph(string):
        return PARAGRAPH
    elif is_image(string):
        return IMAGE
    elif is_border_line(string):
        return BORDER_LINE
    elif is_unordered_list(string):
        return UNORDERED_LIST
    elif is_ordered_list(string):
        return ORDERED_LIST
    elif is_two_column_list(string):
        return TWO_COLUMN_LIST


def line_formatter(string):
    """
    Converts xenmark line to html string
    If the line property is TWO_COLUMN_LIST, it returns column variable like: '|2-1|', '|2-2|', '|2-3|'
    :param string: xenmark line
    :return: html string or column variable(str)
    """

    def header_1_formatter(string):
        return f'<h1 class="contents">{is_header_1(string)}</h1>'

    def header_2_formatter(string):
        return f'<h2 class="contents">{is_header_2(string)}</h2>'

    def header_3_formatter(string):
        return f'<h3 class="contents">{is_header_3(string)}</h3>'

    def header_4_formatter(string):
        return f'<h4 class="contents">{is_header_4(string)}</h4>'

    def paragraph_formatter(string):
        return f'<p class="contents">{is_paragraph(string)}</p>'

    def image_formatter(string):
        formatted_list = []
        for img_name in is_image(string):
            formatted_list.append(
                '<img class="img-responsive img-mxw8 center-block" ' +
                f'src="/media/{POST_IMG_UPLOAD_PATH}/{img_name}" alt="">'
            )
        return '\n'.join(formatted_list)

    def border_line_formatter(string):  # parameter is needed
        return f'<hr class="margin4">'

    def unordered_list_formatter(string):
        return f'<li>{is_unordered_list(string)}</li>'

    def ordered_list_formatter(string):
        return f'<li>{is_ordered_list(string)}</li>'

    def two_column_list_formatter(string):
        return is_two_column_list(string)

    prop_to_formatter = {
        HEADER_1: header_1_formatter,
        HEADER_2: header_2_formatter,
        HEADER_3: header_3_formatter,
        HEADER_4: header_4_formatter,
        PARAGRAPH: paragraph_formatter,
        IMAGE: image_formatter,
        BORDER_LINE: border_line_formatter,
        UNORDERED_LIST: unordered_list_formatter,
        ORDERED_LIST: ordered_list_formatter,
        TWO_COLUMN_LIST: two_column_list_formatter,
        None: lambda x: '',  # for exceptions: line_property() may return None.
    }

    prop = line_property(string)

    formatted = prop_to_formatter[prop](string)
    formatted = link_inspector(formatted)
    formatted = highlight_inspector(formatted)

    return formatted


def link_inspector(line_formatted):
    """
    Inspect xenmark-type link in the given string and convert it to html
    :param line_formatted: a string that may contain xenmark-type link
    :return: formatted string
    """
    link_data_list = is_link(line_formatted)
    if link_data_list:
        for link_data in link_data_list:
            html_link = f'<a href="{link_data.address}">{link_data.name}</a>'
            line_formatted = line_formatted.replace(link_data.xenmark, html_link)
    return line_formatted


def highlight_inspector(line_formatted):
    """
    Inspect xenmark-type highlight in the given string and convert it to html
    :param line_formatted: a string that may contain xenmark-type highlight
    :return: formatted string
    """
    highlight_data_list = is_highlight(line_formatted)
    if highlight_data_list:
        for highlight_data in highlight_data_list:
            html_highlight = f'<code>{highlight_data.content}</code>'
            line_formatted = line_formatted.replace(highlight_data.xenmark, html_highlight)
    return line_formatted


def is_header_1(string):
    """
    Necessary: line starts with only one #
    Allow: unlimited spaces after #
    Example:
        True: '#', '#title', '#   title'
        Param string: '# title'
        Return: 'title'
    :param string: xenmark type string
    :return: header content string or None
    """
    m = PATTERN_HEADER_1.match(string)
    if m:
        return string[m.end():]


def is_header_2(string):
    """
    Necessary: line starts with only two #, no less or more than that
    Allow: unlimited spaces after ##
    Example:
        True: '##', '##title', '##   title'
        Param string: '## title'
        Return: 'title'
    :param string: xenmark type string
    :return: header content string or None
    """
    m = PATTERN_HEADER_2.match(string)
    if m:
        return string[m.end():]


def is_header_3(string):
    """
    Necessary: line starts with only three #, no less or more than that
    Allow: unlimited spaces after ###
    Example:
        True: '###', '###title', '###   title'
        Param string: '### title'
        Return: 'title'
    :param string: xenmark type string
    :return: header content string or None
    """
    m = PATTERN_HEADER_3.match(string)
    if m:
        return string[m.end():]


def is_header_4(string):
    """
    Necessary: line starts with only four #, no less or more than that
    Allow: unlimited spaces after ####
    Example:
        True: '####', '####title', '####   title'
        Param string: '#### title'
        Return: 'title'
    :param string: xenmark type string
    :return: header content string or None
    """
    m = PATTERN_HEADER_4.match(string)
    if m:
        return string[m.end():]


def is_paragraph(string):
    """
    Necessary: line starts with @
    Allow: unlimited spaces after @
    Example:
        True: '@', '@   this is paragraph'
        Param string: '@   this is paragraph'
        Return: 'this is paragraph'
    :param string: xenmark type string
    :return: paragraph content string or None
    """
    m = PATTERN_PARAGRAPH.match(string)
    if m:
        return string[m.end():]


def is_link(string):
    """
    Necessary: '[]()' pattern
    Allow: any letter in the brackets except bracket letters and '\n'
    Example:
        True:
            '[this is link](http://naver.com)',
            '[this is link](http://naver.com) more than two links works fine: [this is link2](http://naver2.com)!!!!'
        Param string:
            '[this is link](http://naver.com) more than two links works fine: [this is link2](http://naver2.com)!!!!'
        Return:
            [
                LinkData(
                    xenmark='[this is link](http://naver.com)',
                    name='this is link',
                    address='http://naver.com'
                ),
                LinkData(
                    xenmark='[this is link2](http://naver2.com)',
                    name='this is link2',
                    address='http://naver2.com'
                )
            ]
    :param string: string
    :return: list of LinkData object or None
    """
    i = PATTERN_LINK.finditer(string)
    link_data_list = []
    for m in i:
        link_data_list.append(
            LinkData(
                xenmark=m.group(),
                name=m.group('link_name'),
                address=m.group('link_address'),
            )
        )
    return link_data_list if link_data_list else None


def is_highlight(string):
    """
    Necessary: two backticks(`)
    Allow: any letters in the two backticks, except '\n'
    Example:
        True: '`highlight`', 'possible `anywhere` in a sentence, and `more than two!`'
        Param string: 'possible `anywhere` in a sentence, and `more than two!`'
        Return:
            [
                HighlightData(xenmark='`anywhere`', content='anywhere'),
                HighlightData(xenmark='`more than two!`', content='more than two!')
            ]
    :param string: string
    :return: list of HighlightData object or None
    """
    h = PATTERN_HIGHLIGHT.finditer(string)
    highlight_data_list = []
    for m in h:
        highlight_data_list.append(
            HighlightData(
                xenmark=m.group(),
                content=m.group('content'),
            )
        )
    return highlight_data_list if highlight_data_list else None


def is_image(string):
    """
    Necessary:
        1. '|()|' pattern
        2. image name can not include whitespace characters(' \t\n\r\x0b\x0c')
        3. bracket must be right next to the pipeline like: '|(' or ')|' ('|  (' is not acceptable)
    Allow:
        1. any letters in the bracket except the pattern letters('|()') and whitespace characters
        2. '\n' can be included in the given string.
    Example:
        True:
            '|(genome-analysis1.png)|',
            '  |(genome-analysis1.png)|  |(genome-analysis2.png)|  \n |(genome-analysis3.png)|'
        Param string: '  |(genome-analysis1.png)|  |(genome-analysis2.png)|  \n |(genome-analysis3.png)|'
        Return: ['genome-analysis1.png', 'genome-analysis2.png', 'genome-analysis3.png']
    :param string: string
    :return: list of image name string or None
    """
    img_name_list = PATTERN_IMAGE.findall(string)
    if img_name_list:
        return img_name_list


def is_border_line(string):
    """
    Necessary: three dashes
    Allow:
        1. more than three dashes
        2. spaces before and after three dashes
        3. '\n' after three dashes
    Example:
        True: '---', '  ---------  \n', '  --------\n  '
        Param string: '  ---------  \n   '
        Return: True
    :param string: string
    :return: True or None
    """
    m = PATTERN_BORDER_LINE.match(string)
    if m:
        return True


def is_unordered_list(string):
    """
    Necessary: a dash and a space after the dash: '- '
    Allow: spaces before and after the dash
    Example:
        True: '- unordered list', '  -     unordered list'
        Param string: '  -     unordered list'
        Return: 'unordered list'
    :param string: string
    :return: string of content or None
    """
    m = PATTERN_UNORDERED_LIST.match(string)
    if m:
        return string[m.end():]


def is_ordered_list(string):
    """
    Necessary: number and a dot after the number and a space: '1. '
    Allow:
        1. any number
        2. spaces before the number
        3. spaces after the dot
    Example:
        True: '1. ordered list', '  232.     ordered list'
        Param string: '  232.     ordered list'
        Return: 'ordered list'
    :param string: string
    :return: content string or None
    """
    m = PATTERN_ORDERED_LIST.match(string)
    if m:
        return string[m.end():]


def is_two_column_list(string):
    """
    Necessary: '|2-1|' or '|2-2|' or '|2-0|' (these are indicators of two column list)
    Allow: spaces or '\n' after the indicators
    Example:
        True: '|2-1|', '|2-2|   ', '|2-0|   \n'
        Param string: '|2-0|    \n'
        Return: '|2-0|'
    :param string: string
    :return: content string or None
    """
    m = PATTERN_TWO_COLUMN_LIST.match(string)
    if m:
        return m.group()


def list_wrapper(line_formatted, index, line_properties):
    """
    add <ul> or <ol> wrapper before or after list-type html string
    :param line_formatted: string of html type list
    :param index: index of property of line_formatted in line_properties
    :param line_properties: list of properties of each line
    :return: string
    """
    # if property of the given formatted line is TWO_COLUMN_LIST
    if line_properties[index] == TWO_COLUMN_LIST:
        line_formatted = two_column_list_wrapper(line_formatted)
        return line_formatted

    try:
        # if the property of the given line is different from the former line,
        # it means the given line is the first line of the html list
        if index == 0 or not line_properties[index-1] == line_properties[index]:
            if line_properties[index] == UNORDERED_LIST:
                line_formatted = unordered_list_wrapper(line_formatted)
            elif line_properties[index] == ORDERED_LIST:
                line_formatted = ordered_list_wrapper(line_formatted)

        # if the property of the given line is different from the next line,
        # it means the given line is the last line of the html list
        max_index = len(line_properties)-1
        if index == max_index or not line_properties[index] == line_properties[index+1]:
            if line_properties[index] == UNORDERED_LIST:
                line_formatted = unordered_list_wrapper(line_formatted, first_line=False)
            elif line_properties[index] == ORDERED_LIST:
                line_formatted = ordered_list_wrapper(line_formatted, first_line=False)
    except IndexError:
        return line_formatted

    return line_formatted


def unordered_list_wrapper(line_formatted, first_line=True):
    if first_line:
        return '<ul class="contents">\n' + line_formatted
    else:
        return line_formatted + '\n</ul>'


def ordered_list_wrapper(line_formatted, first_line=True):
    if first_line:
        return '<ol class="contents">\n' + line_formatted
    else:
        return line_formatted + '\n</ol>'


def two_column_list_wrapper(line_formatted):
    if line_formatted == COLUMN_NUMBER_1:
        line_formatted = '<div class="paragraph column2-wrapper clearfix text-left">\n' + \
                         '<div class="first-column col-md-6">'
    elif line_formatted == COLUMN_NUMBER_2:
        line_formatted = '</div>\n<div class="second-column col-md-6">'
    elif line_formatted == COLUMN_END:
        line_formatted = '</div>\n</div>'

    return line_formatted
