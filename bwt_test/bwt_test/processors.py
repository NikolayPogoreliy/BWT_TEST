import re


class SplitNumbers:
    def __call__(self, value):
        return int(re.match(r'(\d+) \w+', ' '.join(value)).group(1))
