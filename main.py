# takes file path and returns file contents as string
def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
		return file_contents

# prints contents of frankenstein.txt
def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	book_text = get_book_text(book_path)
	book_num = word_count(book_text)
	book_count = char_count(book_text)
	book_sort = dict_sort(book_count)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {book_num} total words")
	print("--------- Character Count -------")

	for num_dict in book_sort:
		if num_dict["char"].isalpha():
			nd_char = num_dict["char"]
			nd_count = num_dict["count"]
			print(f"{nd_char}: {nd_count}")

from stats import word_count, char_count, dict_sort
import sys

main()
