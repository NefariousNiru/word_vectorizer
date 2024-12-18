from argparse import ArgumentParser

class Arguments(ArgumentParser):
    def __init__(self):
        super().__init__(description="Word Count Clone")
        self.file_path = None
        self.char_count = False
        self.word_count = False
        self.line_count = False
        self.byte_count = False
        self.size_unit = None

    def parse(self):
        self.add_argument('-f', '--file-path', help='Specify file path', required=True)
        self.add_argument('-c', '--char-count', action='store_true', help='Count characters')
        self.add_argument('-w', '--word-count', action='store_true', help='Count words')
        self.add_argument('-l', '--line-count', action='store_true', help='Count lines')
        self.add_argument('-b', '--byte-count', action='store_true', help='Count bytes')
        self.add_argument('-k', '--kilobyte', action='store_true', help='Measure in kilobytes')
        self.add_argument('-m', '--megabyte', action='store_true', help='Measure in megabytes')
        self.add_argument('-g', '--gigabyte', action='store_true', help='Measure in gigabytes')

        args = self.parse_args()

        self.file_path = args.file_path
        self.char_count = args.char_count
        self.word_count = args.word_count
        self.line_count = args.line_count
        self.byte_count = args.byte_count

        if args.kilobyte:
            self.size_unit = 'KB'
        elif args.megabyte:
            self.size_unit = 'MB'
        elif args.gigabyte:
            self.size_unit = 'GB'

        self._validate()

    def _validate(self):
        if not (self.char_count or self.word_count or self.line_count or self.byte_count or self.size_unit):
            self.error("At least one count option must be specified.")

        if self.size_unit and [self.size_unit].count(True) > 1:
            self.error("You can only specify one of --kilobyte, --megabyte, or --gigabyte.")

    def error(self, message):
        print(f"Error: {message}")
        self.print_help()
        exit(1)

    def __str__(self):
        return (
            f"File Path: {self.file_path}\n"
            f"Character Count: {self.char_count}\n"
            f"Word Count: {self.word_count}\n"
            f"Line Count: {self.line_count}\n"
            f"Byte Count: {self.byte_count}\n"
            f"Size Unit: {self.size_unit or 'None'}"
        )
