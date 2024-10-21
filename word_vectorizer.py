import argparse
import concurrent.futures
import multiprocessing


def read_chunks(path, chunk_size=8192):
    with open(path, 'rb') as file:
        while chunk := file.read(chunk_size):
            yield chunk

def process_chunk(chunk, leftover_parts):
    chunk = chunk.decode()

    words = chunk.split()
        
    # Separated at the end of a complete word
    if not chunk[-1].isspace():
        leftover_parts.append(words.pop())

    return len(words)

def parallel_calculation(args, core_thread_multiplier=1):
    total_word_count = 0
    leftover_parts = []

    cores = multiprocessing.cpu_count()
    threads = cores * core_thread_multiplier

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for chunk in read_chunks(args.file_path):
            futures.append(executor.submit(process_chunk, chunk, leftover_parts))

        for future in concurrent.futures.as_completed(futures):
            total_word_count += future.result()

    print(leftover_parts)
    if leftover_parts:
        total_word_count += len(leftover_parts)

    return total_word_count

def parse_arguments(args):
    path = args.file_path
    wc = parallel_calculation(args, 1)
    print(wc)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file-path', help='Specify file path')
    parser.add_argument('-c', '--char-count', action='store_true', help='Count characters')
    parser.add_argument('-w', '--word-count', action='store_true', help='Count words')
    parser.add_argument('-l', '--line-count', action='store_true', help='Count lines')
    parser.add_argument('-b', '--byte-count', action='store_true', help='Count bytes')
    parser.add_argument('-k', '--kilobyte', action='store_true', help='Measure in kilobytes')
    parser.add_argument('-m', '--megabyte', action='store_true', help='Measure in megabytes')
    parser.add_argument('-g', '--gigabyte', action='store_true', help='Measure in gigabytes')

    args = parser.parse_args()
    parse_arguments(args)


if __name__ == "__main__":
    main()
