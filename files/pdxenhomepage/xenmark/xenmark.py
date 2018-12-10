"""
Xenmark is a markup language for non-programmer to be able to create html contents for Pdxen homepage.
And this module contains main functions that converts xenmark to html.
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

    # break xenmark string into small pieces
    xenmark_module_list = xenmark_modularize(string)
    html_module_list = [module_formatter(module) for module in xenmark_module_list]
    # add wrapping tag
    for index, module in enumerate(html_module_list):
        html_module_list[index] = f'<div class="paragraph text-justify">\n{module}\n</div>\n'

    return '\n'.join(html_module_list)


def xenmark_modularize(string):
    """
    break xenmark string into xenmark module, by '\n\n' as a separator
    xenmark module: small pieces of xenmark string which is separated by '\n\n'

    :param string: xenmark string
    :return: list of xenmark module string
    """
    if not isinstance(string, str):
        raise TypeError('input of xenmark_modularize() must be string')

    string = string.replace('\r', '')
    string = string.replace('\ufeff', '')  # a plain text made in window starts with '\ufeff'

    # separate each module by '\n\n' as a separator
    module_list = string.split('\n\n')

    # if the given string contains '\n\n\n', some module starts with '\n'
    for index, value in enumerate(module_list):
        if value.startswith('\n'):
            module_list[index] = value[1:]

    # if the given string contains '\n\n\n\n', blank module is made
    while '' in module_list:
        module_list.remove('')

    # return refined xenmark modules
    return module_list


def module_formatter(xenmark_module):
    """
    convert xenmark module string to html

    :param xenmark_module: xenmark module string
    :return: html string
    """
    if not isinstance(xenmark_module, str):
        raise TypeError('xenmark_module must be string')

    # after a paragraph indicator, '@', multiple '\n' is allowed, and it is redundant
    xenmark_module = PATTERN_REDUNDANT_NEWLINE.sub(' ', xenmark_module)

    lines = xenmark_module.split('\n')
    # get line properties like: header, paragraph, list ...
    line_properties = [line_property(line) for line in lines]
    formatted_lines = []
    for index, line in enumerate(lines):
        line_formatted = line_formatter(line)  # convert each line into html
        # if it's list(<li>...</li>), wrapping tags are needed like: <ul>, <ol>
        if line_properties[index] in [ORDERED_LIST, UNORDERED_LIST, TWO_COLUMN_LIST]:
            line_formatted = list_wrapper(line_formatted, index, line_properties)
        formatted_lines.append(line_formatted)

    html_module = '\n'.join(formatted_lines)
    return html_module
