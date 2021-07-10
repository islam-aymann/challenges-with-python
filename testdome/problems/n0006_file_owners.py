from collections import defaultdict


def group_by_owners(files):
    result = defaultdict(list)

    for file, name in files.items():
        result[name].append(file)

    return result


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))
