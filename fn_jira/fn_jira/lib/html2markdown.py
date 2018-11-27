import re
import logging

try:
    from HTMLParser import HTMLParser
except:
    from html.parser import HTMLParser

class MarkdownParser(HTMLParser):
    QUILL_RTE = "rte"       # first <div> will have this class

    HTML_STYLE_COLOR = r'rgb\(([\d]*)[,\s]*([\d]*)[,\s]*([\d]*)\)'

    SUPPORTED_TAGS = ["div", "span", "br", "strong", "em", "s", "u", "ol", "ul", "li", "a",
                      "h", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote"]

    MARKDOWN_NEWLINE = "\n"
    MARKDOWN_NEWSECTION = "\n\n"

    DEFAULT_LIST = "*"

    def __init__(self, bold="**", italic="*", underline="__", strikeout="~~", bullets=DEFAULT_LIST, number=0, indent=4,
                 monospace=["{{", "}}"], headers=['h1.', 'h2.', 'h3.', 'h4.', 'h5.', 'h6.'], blockquote="```"):
        HTMLParser.__init__(self)
        self.log = logging.getLogger(__name__)

        self.buffer = []      # end markdown buffer
        self.curr_tag = []    # stack of tags to track
        self.curr_attrs = []  # stack of tag attributes to track
        self.curr_list = []   # stack of embedded ordered and unordered list symbols
        self.data = []        # buffer for a given tag, cleared when and ending tag is found (ex. </p>)
        self.data_pre = []    # markdown data to prefix the data
        self.data_post = []   # markdown data to follow the data

        # customizable attributes
        self.bold = bold
        self.italic = italic
        self.underscore = underline
        self.strikeout = strikeout
        self.list_bullets = bullets if isinstance(bullets, list) else [bullets] * 6
        self.list_number = number
        self.indent = indent
        self.monospace = monospace
        self.headers = headers
        self.blockquote = blockquote

    def convert(self, data):
        """
        starting point for app, wrapper to htmlparser.feed
        :param data: html string
        :return: converted text to markdown
        """
        self.feed(data)
        return self.toString()

    def handle_starttag(self, tag, attrs):
        """
        handler for the start of tags. Logic is added to surround data with markdown
        :param tag:
        :param attrs:
        :return: None
        """

        # flush any data accumulated
        self.push_data(True)

        # retain the hierarchy of nested command, which may be needed
        self.curr_tag.append(tag)
        self.curr_attrs.append(attrs)

        if tag == "strong":
            self.data_pre.append(self.bold)
            self.data_post.insert(0, self.bold)

        elif tag == "em":
            self.data_pre.append(self.italic)
            self.data_post.insert(0, self.italic)

        elif tag == "s":
            self.data_pre.append(self.strikeout)
            self.data_post.insert(0, self.strikeout)

        elif tag == "u":
            self.data_pre.append(self.underscore)
            self.data_post.insert(0, self.underscore)

        elif tag == "ol":
            self.curr_list.append(self.list_number)  # number to be incremented with every <li>

        elif tag == "ul":
            if self.list_bullets:
                self.curr_list.append(self.list_bullets.pop(0))  # get the symbol to use
            else:
                # default list marker
                self.curr_list.append(MarkdownParser.DEFAULT_LIST)

        elif tag == "li":
            # add proper # of spaces
            self.data_pre.append(MarkdownParser.MARKDOWN_NEWLINE)
            self.data_pre.append((" " * self.indent) * len(self.curr_list))

            if not isinstance(self.curr_list[-1], int):
                self.data_pre.append('{} '.format(self.curr_list[-1]))
            else:
                num = self.curr_list.pop()
                num = num+1
                self.curr_list.append(num)
                self.data_pre.append("{}. ".format(num))

        elif tag == "a":
            href = self.get_attr(attrs, 'href')
            self.data_pre.extend(["[{}]".format(href), '('])
            self.data_post.insert(0, ")")

        elif tag in ('h', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            if tag == 'h':
                tag = 'h1'
            # get the number of header and use as index into the header array
            idx = int(tag[-1:])-1
            if idx < len(self.headers):
                self.data_pre.append("{} ".format(self.headers[idx]))

            self.data_post.append(MarkdownParser.MARKDOWN_NEWLINE)

        elif tag == "blockquote":
            self.data_pre.append(self.blockquote)
            self.data_post.insert(0, self.blockquote)

        elif tag not in MarkdownParser.SUPPORTED_TAGS:
            self.log.warning("Unknown html tag: {}".format(tag))
            self.data_post.insert(0, MarkdownParser.MARKDOWN_NEWLINE)

        # determine if styling is needed
        style = self.get_attr(attrs, 'style')
        if style:
            rgb = self.get_style_attr(style, 'color')
            if rgb:
                rgb_hex = self.convert_rgb(self.get_rgb(rgb))
                self.data_pre.append("{{color:{0}}}".format(rgb_hex))
                self.data_post.insert(0, "{color}")

            # format monospace data blocks
            font_family = self.get_style_attr(style, 'font-family')
            if font_family and font_family == "monospace":
                if isinstance(self.monospace, list):
                    self.data_pre.append(self.monospace[0])
                    self.data_post.insert(0, self.monospace[1])
                else:
                    self.data_pre.append(self.monospace)
                    self.data_post.insert(0, self.monospace)


    def handle_data(self, data):
        """
        data handler. Basically, add tagged data to the growing buffer
        :param data:
        :return: None
        """
        # clean data of prefix whitespace
        cleaned = re.search(r"^[\n\t\r]*(.*)", data, re.S)
        cleaned and self.data.append(cleaned.group(1))


    def handle_endtag(self, tag):
        """
        handler for end tags.
        :param tag:
        :return: None
        """

        # remove existing tag from stack
        prev_tag = self.curr_tag.pop()
        prev_attrs = self.curr_attrs.pop()

        if prev_tag != tag:
            raise ValueError("Mismatch tag {} expecting {}".format(tag, prev_tag))

        if tag == "div":
            self.data_post.append(MarkdownParser.MARKDOWN_NEWLINE)

        elif tag in ("ol", "ul"):
            if len(self.curr_list) > 0:
                bullet = self.curr_list.pop()   # remove existing bullet, exposing previous bullet
                if tag == "ul":
                    if self.list_bullets:
                        self.list_bullets.insert(0, bullet)      # clear top item on list symbols
                    else:
                        self.list_bullets = [bullet]

        elif tag == "br":
            # this is data rather than pre or post data
            self.data.append(MarkdownParser.MARKDOWN_NEWSECTION)

        self.push_data()


    def push_data(self, data_only=False):
        """
        flush the data buffer and reset for next html tag
        :return: None
        """

        if data_only:
            self.buffer.extend(self.data)
            self.data = []
        else:
            self.buffer.extend([item for sublist in [self.data_pre, self.data, self.data_post] for item in sublist])

            # clean up
            self.data = []
            self.data_pre = []
            self.data_post = []


    def convert_rgb(self, rgb):
        """
        convert rgb values to hexcode format
        :param rgb:
        :return:
        """
        return '#'+''.join('%02x'% int(i) for i in rgb)


    def get_attr(self, attrs, key):
        """
        get an attribute from the data's previous block
        ex. <div style='font-family: monospace'>zzz</div>
        :param attrs:
        :param key:
        :return: found attribute or None
        """
        for attr in attrs:
            if attr[0] == key:
                return attr[1]

        return None


    def get_style_attr(self, style, key):
        """
        find css data within the style attribute
        :param style:
        :param key: css label
        :return: css data
        """
        for attr in style.split(';'):
            attr_split = attr.split(':')
            if attr_split[0].strip() == key:
                return attr_split[1].strip()

        return None


    def get_rgb(self, str):
        """
        format of rgb information is "rgb(rrr, ggg, bbb)"
        :param str:
        :return: list of values
        """
        m = re.search(MarkdownParser.HTML_STYLE_COLOR,  str)
        return m.group(1, 2, 3) if m else None


    def __str__(self):
        return self.toString()

    def __repr__(self):
        return self.toString()

    def toString(self):
        """
        we're done. flush the data buffer and print entire content
        :return: markdown result
        """
        self.push_data()

        result = ''.join(self.buffer)
        # clean up ending new line characters
        while result[-1:] == '\n':
            result = result[:-1]

        return result
