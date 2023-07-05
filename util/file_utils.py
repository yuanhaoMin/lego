def load_text(file_path, by_lines=False):
    with open(file=file_path, mode="r") as fp:
        if by_lines:
            return fp.readlines()
        else:
            return fp.read()


def dump_text(text, file_path):
    with open(file=file_path, mode="w", encoding="utf-8") as fp:
        fp.write(text)
