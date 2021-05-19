def WordSplit(strArr):
    phrase = strArr[0]
    refs = strArr[1].replace(' ', '').split(',')

    matches = len(refs) * ['']
    for ref in refs:
        if ref in phrase:
            matches.insert(phrase.index(ref), ref)

    return ', '.join([match for match in matches if match]) if matches else 'Not Possible'


if __name__ == '__main__':
    print(WordSplit(["hellocat", "apple, bat ,cat,goodbye,hello,yellow,why"]))
