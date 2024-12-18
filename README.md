
# Word Vectorizer

A command-line utility that acts as a clone of the `wc` (word count) command with additional support for counting characters, words, lines, and bytes, as well as converting byte counts to kilobytes, megabytes, or gigabytes.

## Features

- Count the number of **characters** in a file.
- Count the number of **words** in a file.
- Count the number of **lines** in a file.
- Count the number of **bytes** in a file.
- Display the result in **kilobytes (KB)**, **megabytes (MB)**, or **gigabytes (GB)**.

## Requirements

- Python 3.x
- `argparse` library (included with Python standard library)

## Installation

To use this tool, you can either install it as a package or run it directly from the source.

### **Installing via `setup.py`**

1. Clone or download this repository to your local machine.
2. Navigate to the project directory where `setup.py` is located.
3. Install the project in **editable mode** using the following command:

   ```bash
   pip install --editable .
   ```
   And then use this directly -
   ```bash
   wcc [-f file_path] [-<other flags>]
   ```
   This installs the package locally and links it to your current working directory, so changes to the code are immediately reflected when you run the tool.

### **Direct Execution (Without Installation)**

Alternatively, you can run the `word_vectorizer.py` script directly:
```bash
   python word_vectorizer.py [-f file_path] [-<other flags>]
```

## Usage

You can run the utility from the command line by providing the appropriate flags:

### **Flags:**

- **`-f` or `--file-path`**: Specify the path to the file you want to analyze. (Required)
- **`-w` or `--word-count`**: Count words in the file.
- **`-l` or `--line-count`**: Count lines in the file.
- **`-b` or `--byte-count`**: Count bytes in the file.
- **`-k` or `--kilobyte`**: Display the byte count in kilobytes (KB).
- **`-m` or `--megabyte`**: Display the byte count in megabytes (MB).
- **`-g` or `--gigabyte`**: Display the byte count in gigabytes (GB).

### **Examples:**

1. **Word count in a file**:
   ```bash
   python word_vectorizer.py -f example.txt -w
   ```

2. **Count the number of lines and bytes in a file**:
   ```bash
   python word_vectorizer.py -f example.txt -l -b
   ```

3. **Display byte count in kilobytes**:
   ```bash
   python word_vectorizer.py -f example.txt -b -k
   ```

4. **Display byte count in megabytes**:
   ```bash
   python word_vectorizer.py -f example.txt -b -m
   ```

## Setup.py

If you want to install this tool and make it available for use across your system, you can use the `setup.py` file. 

### **Steps:**

1. Ensure that `setup.py` is correctly set up to define your package (this should already be done in the project).
2. Run the following command in the project directory:

   ```bash
   pip install --editable .
   ```

   This command will install the package in editable mode, meaning that any changes to the code will be reflected immediately in your environment without needing to reinstall the package.

3. After installation, you can use the tool by running the following command from anywhere:

   ```bash
   word_vectorizer -f example.txt -w -l -b
   ```

## License

This project is open-source and available under the MIT License.
