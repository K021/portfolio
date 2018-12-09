"""
xenmark: 비개발자도 pdxen homepage 웹 컨텐츠를 편집할 수 있게하는 markup language.
이 문서는 xenmark 를 html 로 효과적으로 변환하기 위한 함수를 담고있다.
"""

from .variables import *
from .linef import *

__all__ = (
    'xenmark_to_html',
    'xenmark_modularize',
    'module_formatter',
)


def xenmark_to_html(string):
    if not isinstance(string, str):
        raise TypeError('input of xenmark_to_html() must be string')

    # xenmark string 을 모듈화한다.
    xenmark_module_list = xenmark_modularize(string)
    html_module_list = [module_formatter(module) for module in xenmark_module_list]
    # 모듈 앞 뒤에 와야 하는 태그를 wrapping 해준다.
    for index, module in enumerate(html_module_list):
        html_module_list[index] = f'<div class="paragraph text-justify">\n{module}\n</div>\n'

    # html 모둘은 끝에 '\n'가 하나 없는 상태로 반환된다. 그래서 붙여주는 것.
    return '\n'.join(html_module_list)


def xenmark_modularize(string):
    """
    xenmark string 을 받아서 xenmark module 로 이루어진 list 를 뱉는다.

    :param string: xenmark string
    :return: xenmark module list
    """
    if not isinstance(string, str):
        raise TypeError('input of xenmark_modularize() must be string')

    string = string.replace('\r', '')
    string = string.replace('\ufeff', '')  # window 에서 만든 utf-8 인코딩 문서 맨 앞 기호 지움

    # 줄바꿈 두 개를 기준으로 모듈 분리, 리스트에 할당
    module_list = string.split('\n\n')

    # 줄바꿈 세개가 입력되었을 경우, 줄바꿈 문자로 시작하는 행의 줄바꿈문자 삭제
    for index, value in enumerate(module_list):
        if value.startswith('\n'):
            module_list[index] = value[1:]

    # 내용 없는 모듈 삭제. 줄바꿈이 네개일 때는 내용 없는 모듈이 생김
    while '' in module_list:
        module_list.remove('')

    # 정제된 모듈리스트 반환
    return module_list


def module_formatter(xenmark_module):
    """
    xenmark module string 을 받아서 html 로 변환해준다.

    :param xenmark_module:
    :return:
    """
    if not isinstance(xenmark_module, str):
        raise TypeError('xenmark_module must be string')

    # paragraph 기호인 @ 아래선, 마음대로 줄바꿈을 할 수 있다
    # 그런데 모듈을 줄바꿈 문자를 기준으로 리스트로 분류할 것이기 때문에,
    # 이 쓸데 없는 개행문자를 전부 없에준다 (공백 한 개로 바꾸어 준다. 줄바꿈은 단락의 전환이므로)
    xenmark_module = PATTERN_REDUNDANT_NEWLINE.sub(' ', xenmark_module)

    lines = xenmark_module.split('\n')
    line_properties = [line_property(line) for line in lines]  # 해당 라인이 header 인지, paragraph 인지 등을 구분
    formatted_lines = []
    for index, line in enumerate(lines):
        line_formatted = line_formatter(line)  # 각 라인 타입에 맞추어 html 변환
        # 리스트의 경우에는 바깥에 한 번 더 감싸주어야 한다.
        if line_properties[index] in [ORDERED_LIST, UNORDERED_LIST, TWO_COLUMN_LIST]:
            line_formatted = list_wrapper(line_formatted, index, line_properties)
        formatted_lines.append(line_formatted)

    html_module = '\n'.join(formatted_lines)
    return html_module
