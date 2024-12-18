import os.path
from arguments import Arguments
import util

def count_words(file: str):
    count = 0
    word = False
    for ch in file:
        if not ch.isspace():
            if not word:
                word = True
                count += 1
        else:
            word = False
    return count

def count_characters(file):
    return len(file)

def count_lines(file):
    count = 0
    for ch in file:
        if ch == "\n":
            count += 1
    if file and file[-1] != "\n":
        count += 1
    return count

def count_bytes(path):
    return os.path.getsize(path)

def get_size(unit: str, path):
    size_in_bytes = count_bytes(path)
    units = {
        "KB": size_in_bytes / 1024,
        "MB": size_in_bytes / (1024 ** 2),
        "GB": size_in_bytes / (1024 ** 3)
    }
    return f"{units[unit]:.2f} {unit}"

def main():
    args = Arguments()
    args.parse()

    if args.word_count:
        file = util.read_file(args.file_path)
        count = count_words(file)
        print(count)

    if args.line_count:
        file = util.read_file(args.file_path)
        count = count_lines(file)
        print(count)

    if args.char_count:
        file = util.read_file(args.file_path)
        count = count_characters(file)
        print(count)

    if args.byte_count:
        count = count_bytes(args.file_path)
        print(count)

    if args.size_unit:
        size = get_size(args.size_unit, args.file_path)
        print(size)

if __name__ == "__main__":
    main()
