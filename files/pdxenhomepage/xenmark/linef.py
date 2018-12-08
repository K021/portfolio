"""
xenmark 패키지에서 line 관련 함수를 담고 있는 모듈
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
    xenmark line 을 받아서 line 종류를 반환한다.
    :param string: xenmark line
    :return: xenmark line property
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
    elif is_link(string):
        return LINK
    elif is_highlight(string):
        return HIGHLIGHT
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
    xenmark line 을 받아서 html string 으로 변환해준다.
    TWO_COLUMN_LIST 의 경우에는 column variable 을 반환한다.
    :param string: xenmark line
    :return: html string or column variable(str)
    """
    prop = line_property(string)
    formatted = ''

    if prop == HEADER_1:
        formatted = f'<h1 class="contents">{is_header_1(string)}</h1>'
    elif prop == HEADER_2:
        formatted = f'<h2 class="contents">{is_header_2(string)}</h2>'
    elif prop == HEADER_3:
        formatted = f'<h3 class="contents">{is_header_3(string)}</h3>'
    elif prop == HEADER_4:
        formatted = f'<h4 class="contents">{is_header_4(string)}</h4>'
    elif prop == PARAGRAPH:
        formatted = f'<p class="contents">{is_paragraph(string)}</p>'
    elif prop == IMAGE:
        formatted_list = []
        for img_name in is_image(string):
            formatted_list.append(
                '<img class="img-responsive img-mxw8 center-block" ' +
                f'src="/media/{POST_IMG_UPLOAD_PATH}/{img_name}" alt="">'
            )
        for line in formatted_list:
            formatted += line + '\n'
        formatted = formatted[:-1]
    elif prop == BORDER_LINE:
        formatted = f'<hr class="margin4">'
    elif prop == UNORDERED_LIST:
        formatted = f'<li>{is_unordered_list(string)}</li>'
    elif prop == ORDERED_LIST:
        formatted = f'<li>{is_ordered_list(string)}</li>'
    elif prop == TWO_COLUMN_LIST:
        formatted = is_two_column_list(string)

    formatted = link_inspector(formatted)
    formatted = highlight_inspector(formatted)

    return formatted


def link_inspector(line_formatted):
    """
    한 번 formatted 된 line 에 link 타입의 xenmark string 이 있는지 검사한다.
    :param line_formatted:
    :return:
    """
    link_data_list = is_link(line_formatted)
    if link_data_list:
        for link_data in link_data_list:
            html_link = f'<a href="{link_data.address}">{link_data.name}</a>'
            line_formatted = line_formatted.replace(link_data.xenmark, html_link)
    return line_formatted


def highlight_inspector(line_formatted):
    highlight_data_list = is_highlight(line_formatted)
    if highlight_data_list:
        for highlight_data in highlight_data_list:
            html_highlight = f'<code>{highlight_data.content}</code>'
            line_formatted = line_formatted.replace(highlight_data.xenmark, html_highlight)
    return line_formatted


def is_header_1(string):
    """
    True: '#', '#제목', '#   제목'
    Necessary: 맨 앞에 # 하나. 둘 이상 안됨
    Allow: # 뒤에 무제한
    Return: '제목'
    """
    m = PATTERN_HEADER_1.match(string)
    if m:
        return string[m.end():]


def is_header_2(string):
    """
    True: '##', '##제목', '##   제목'
    Necessary: 맨 앞에 # 둘. 셋 이상 안됨
    Allow: ## 뒤에 무제한
    Return: '제목'
    """
    m = PATTERN_HEADER_2.match(string)
    if m:
        return string[m.end():]


def is_header_3(string):
    """
    True: '###', '###제목', '###   제목'
    Necessary: 맨 앞에 # 셋. 넷 이상 안됨
    Allow: ### 뒤에 무제한
    Return: '제목'
    """
    m = PATTERN_HEADER_3.match(string)
    if m:
        return string[m.end():]


def is_header_4(string):
    """
    True: '####', '####제목', '####   제목'
    Necessary: 맨 앞에 # 넷. 다섯 이상 안됨
    Allow: #### 뒤에 무제한
    Return: '제목'
    """
    m = PATTERN_HEADER_4.match(string)
    if m:
        return string[m.end():]


def is_paragraph(string):
    """
    True: '@', '@   이것은 일반 문단입니다.'
    Necessary: 맨 앞에 @
    Allow: @ 뒤 공백 무제한
    Return: '이것은 일반 문단입니다.'
    """
    m = PATTERN_PARAGRAPH.match(string)
    if m:
        return string[m.end():]


def is_link(string):
    """
    True: '[링크](http://naver.com)',
        '물론 [링크](http://naver.com)도 들어갈 수 있죠. 심지어는 두 개도 가능하답니다. [링크2](http://naver2.com)!!!!'
    Necessary: '[줄바꿈제외모든문자](줄바꿈제외모든문자)' 존재
    Allow: 패턴 갯수 무제한. 패턴 이외 문자 무제한.
    Return:
        [
            LinkData(xenmark='[링크](http://naver.com)', name='링크', address='http://naver.com'),
            LinkData(xenmark='[링크2](http://naver2.com)', name='링크2', address='http://naver2.com')
        ]
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
    True: '`highlight`', '문장 내 `어디에서나`'
    Necessary :
    Allow:
    Return:
    :param string:
    :return:
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
    True: '|(genome-analysis1.png)|',
        '  |(genome-analysis1.png)|  |(genome-analysis2.png)|  \n |(genome-analysis3.png)|'
    Necessary: '|(비공백문자)|' 형태의 문자열이 존재하기만 하면 된다. 이미지 이름에는 공백문자(공백, 탭, 줄바꿈 등)가 올 수 없다.
    Allow: 패턴 갯수 무제한. 패턴 이외 문자 무제한.
    Return: ['genome-analysis1.png', 'genome-analysis2.png', 'genome-analysis3.png']
    """
    img_name_list = PATTERN_IMAGE.findall(string)
    if img_name_list:
        return img_name_list


def is_border_line(string):
    """
    True: '---', '  ---------  \n', '  --------\n  '
    Necessary: 대쉬 세개
    Allow: 대쉬 갯수, 대쉬 전후 공백, 대쉬 후 줄바꿈 문자
    """
    m = PATTERN_BORDER_LINE.match(string)
    if m:
        return True


def is_unordered_list(string):
    """
    True: '- 순서 없는 리스트', '  -    순서 없는 리스트'
    Necessary : 대쉬, 대쉬 후 공백
    Allow: 대쉬 전후 공백 무제한
    Return: '순서 있는 리스트' (공백 뒤부터 끝까지 출력된다.)
    """
    m = PATTERN_UNORDERED_LIST.match(string)
    if m:
        return string[m.end():]


def is_ordered_list(string):
    """
    True: '1. 순서 있는 리스트', '  232.     순서 있는 리스트'
    Necessary: 숫자, 숫자 후 점(.)과 공백( )
    Allow: 숫자 자릿수, 숫자 전 공백, 점(.) 후 공백 무제한
    Return: '순서 있는 리스트' (공백 뒤부터 끝까지 출력된다.)
    """
    m = PATTERN_ORDERED_LIST.match(string)
    if m:
        return string[m.end():]


def is_two_column_list(string):
    m = PATTERN_TWO_COLUMN_LIST.match(string)
    if m:
        return m.group()


def list_wrapper(line_formatted, index, line_properties):
    if line_properties[index] == TWO_COLUMN_LIST:
        line_formatted = two_column_list_wrapper(line_formatted)
        return line_formatted

    try:
        # 현재 라인이 이전 라인과 다를 때 == 현재 라인이 첫번째 라인일 때
        if not line_properties[index-1] == line_properties[index]:
            if line_properties[index] == UNORDERED_LIST:
                line_formatted = unordered_list_wrapper(line_formatted)
            elif line_properties[index] == ORDERED_LIST:
                line_formatted = ordered_list_wrapper(line_formatted)

        # 현재 라인이 다음 라인과 다를 때 == 현재 라인이 마지막 라인일 때
        if not line_properties[index] == line_properties[index+1]:
            if line_properties[index] == UNORDERED_LIST:
                line_formatted = unordered_list_wrapper(line_formatted, False)
            elif line_properties[index] == ORDERED_LIST:
                line_formatted = ordered_list_wrapper(line_formatted, False)
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
