def split_string_to_tags(string):
    tags = list()
    i = 0
    while i < len(string):
        tag = list()
        if string[i] == '<':
            tag.append(string[i])
            i += 1
            while i < len(string):
                tag.append(string[i])
                if string[i] == '>':
                    tags.append(''.join(tag).replace(' ', '').strip())
                    break
                i += 1

        i += 1
    return tags


def is_correct_html(string):
    letters = 'h1, h2, h3, h4, h5, h6, b, i, em, div, p'
    opening_tags = [f'<{char}>' for char in letters.split(', ')]
    closing_tags = [f'</{char}>' for char in letters.split(', ')]
    tags = split_string_to_tags(string)

    stack = list()

    for tag in tags:
        if tag in opening_tags:
            stack.append(tag)
        elif tag in closing_tags:
            if not stack:
                return tag
            else:
                o_tag = stack.pop()
                if not opening_tags.index(o_tag) == closing_tags.index(tag):
                    return o_tag

    return True if not stack else stack.pop()


if __name__ == '__main__':
    print(is_correct_html('<div><div><b></b></div><p/>'))
    print(is_correct_html('<div>abc</div><p><em><i>test test test</b></em></p>'))
