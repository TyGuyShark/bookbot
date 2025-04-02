# takes book text string, splits and counts words at whitespace
def word_count(book_text):
        words = book_text.split()
        return len(words)

# takes text as string, returns dictionary with each character as key
# and the count as value (i.e. char->count)
def char_count(book_text):
	char_count = {}

	for char in book_text:
		char_l = char.lower()
		if char_l in char_count:
			char_count[char_l] += 1
		else:
			char_count[char_l] = 1
	return char_count

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["count"]

# takes dictionary of characters->counts, returns sorted list
#  of dictionaries
def dict_sort(dict):
	dict_list = []
	for char in dict:
		char_dict = {}
		char_dict["char"] = char
		char_dict["count"] = dict[char]
		dict_list.append(char_dict)
	dict_list.sort(reverse=True, key=sort_on)
	return dict_list
