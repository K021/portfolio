# Xenmark

Xenmark is a markup language, made for non-programmer to make html contents for [Pdxen hompage](http://pdxen.com).

## Basic Example

xenmark is made similer to markdown, and designed to be apt for pdxen-like post. You can see the [user guide](./xenmark-guide-pub.md)

```
# header 1
## header 2
### header 3
#### header 4
@ this is paragraph. `highlights` and
[link](https://link.com) can be included
and you can press enter.
---
	# separate division by enter twice ('\n\n')
	# this division is called xenmark-module in this project: a xenmark paragraph, which is separated by '\n\n' and becomes a separate division in html
- unordered list
- unordered list
- unordered list
1. ordered list
2. ordered list
3. ordered list
---
	# separate division by enter twice ('\n\n')
|2-1|
- unordered list
- unordered list
- this is called 'two column list'
|2-2|
1. ordered list
2. ordered list
3. ordered list
|2-0|
|(image_file_name.extensions)|
```

this is converted to:

```html
<div class="paragraph text-justify">
	<h1 class="contents">header 1</h1>
	<h2 class="contents">header 2</h2>
	<h3 class="contents">header 3</h3>
	<h4 class="contents">header 4</h4>
		<p class="contents">this is paragraph. <code>highlights</code> and <a href="https://link.com">link</a> can be included and you can press enter.</p>
	<hr class="margin4">
</div>

<div class="paragraph text-justify">
	<ul class="contents">
		<li>unordered list</li>
		<li>unordered list</li>
		<li>unordered list</li>
	</ul>
	<ol class="contents">
		<li>ordered list</li>
		<li>ordered list</li>
		<li>ordered list</li>
	</ol>
<hr class="margin4">
</div>

<div class="paragraph text-justify">
	<div class="paragraph column2-wrapper clearfix text-left">
		<div class="first-column col-md-6">
			<ul class="contents">
				<li>unordered list</li>
				<li>unordered list</li>
				<li>this is called 'two column list'</li>
			</ul>
		</div>
		<div class="second-column col-md-6">
			<ol class="contents">
				<li>ordered list</li>
				<li>ordered list</li>
				<li>ordered list</li>
			</ol>
		</div>
	</div>
	<img class="img-responsive img-mxw8 center-block" src="/media/post/img/image_file_name.extensions" alt="">
</div>
```

## Module Structure

> [Xenmark module source file](files/pdxenhomepage/xenmark)

```
xenmark/
	- __init__.py
	- linef.py		# functions that converts xenmark to html on a line basis
	- variables.py	# variables like xenmark indicator pattern, namedtuple
	- xenmark.py  	# main functions that converts on a xenmark-module basis
```

> xenmark-module: a xenmark paragraph, which is separated by '\n\n' and becomes a separate division in html

- `xenmark.py`: contains main functions
	- `xenmark_to_html()`: main function
	- `xenmark_modularize()`: break down into xenmark-module
	- `module_formatter()`: converts xenmark-module to html using functions from `linef.py`
- `linef.py`: functions that converts xenmark line to html line
- `variables.py`: variables like xenmark indicator pattern, namedtuple


## Converting Structure

1. divide xenmark string into xenmark-modules (`xenmark.xenmark_modularize()`)
2. divide xenmark-module into xenmark lines (`xenmark.module_formatter()`)
3. convert xenmark line to html line (`linef.line_formatter()`)
    1. detect the line property (`linef.line_property()`)
    2. convert the line (`linef.line_formatter()`)
    3. inspect and convert links and highlights (`linef.link_inspector()`, `linef.highlight_inspector()`)
4. wrap html list with `<ul>` or `<ol>` (`xenmark.module_formatter()`)
5. wrap html-module with `<div class='paragraph ...'>` (`xenmark.xenmark_to_html()`)
6. join all html-modules into one string (`xenmark.xenmark_to_html()`)


## Xenmark.py

### 1. `xenmark.xenmark_to_html`

Converting process starts from this function. Recives xenmark string, and returns html string.

```python
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
```


### 2. `xenmark.xenmark_modularize`

Receives xenmark string, and returns list of xenmark-module string.
 
```python
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
```


### 3. `module_formatter`

Recieves xenmark-module string, and returns converted html-module string.

```python
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
```


## linef.py

### 1. `linef.line_property`

Recieves xenmark line string, and returns its property like: header, paragraph etc.

```python
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
```

### 2. `linef.line_formatter`

Recieves xenmark line string, and returns html line string.

```python
def line_formatter(string):
    """
    Converts xenmark line to html string
    If the line property is TWO_COLUMN_LIST, it returns column variable like: '|2-1|', '|2-2|', '|2-3|'
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
        formatted = '\n'.join(formatted_list)
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
```

Inside this function, the following functions are called. Because, link and highlight can be in everywhere like in headers and lists etc. These functions inspect the indicator of xenmark-type link and highlight, and convert it to html.

```python
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
```

### 3. functions that inspect line property

The following functions inspect the given string, and returns the string of its content.

```python
def is_header_1(string):
    """
    Necessary: line starts with only one #
    Allow: unlimited spaces after #
    Example:
        True: '#', '#title', '#   title'
        Param string: '#  title'
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
```

### 4. functions of wrapping list

`linef.line_formatter` function only adds `<li>` tag. We need the following fuctions to add `<ul>` or `<ol>` tags:

```python
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
```

## variables.py

### 1. Patterns

Patterns for xenmark indicator.

```python
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
PATTERN_TWO_COLUMN_LIST = re.compile(r'^\|2-(?P<cn>[120])\|(?![^ \n])')

# find pattern like: '123. '
# '\n    ' is allowed before '123. '
# '#', '@', '|', '-', ' ', is not allowed before '123. '
PATTERN_REDUNDANT_NEWLINE = re.compile(r'\n[ ]*(?![#@|\- ]|(\d+[.][ ]+))')
```

### 2. line properties, and any other variables.

```python
# line properties
HEADER_1 = 'header_1'
HEADER_2 = 'header_2'
HEADER_3 = 'header_3'
HEADER_4 = 'header_4'
PARAGRAPH = 'paragraph'
IMAGE = 'image'
BORDER_LINE = 'border_line'
UNORDERED_LIST = 'unordered_list'
ORDERED_LIST = 'ordered_list'
TWO_COLUMN_LIST = 'two_column_list'

# column variables in two column list
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
```
