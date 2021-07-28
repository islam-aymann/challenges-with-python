from collections import Counter
from typing import List


def matchingStrings(strings: List[str], queries: List[str]) -> List[int]:
    counter = Counter(strings)
    return [counter[query] for query in queries]


if __name__ == "__main__":
    print(
        matchingStrings(
            ["ab", "ab", "abc"],
            ["ab", "abc", "bc"],
        )
    )
