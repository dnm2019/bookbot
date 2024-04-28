def main ():
	book_path = "books/frankenstein.txt"
	print(f"--- Begin report of {book_path} ---")
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	print(f"{num_words} words found in the document")
	char_dict = get_chars_dict(text)
	char_lst = dict_to_list(char_dict)
	for item in char_lst:
		if not item["char"].isalpha():
			continue
		print(f"The '{item["char"]}' character was found {item["num"]} times")
	print("--- End report ---")

def sort_on(dict):
	return dict["num"]

def dict_to_list(char):
	char_lst = []
	for c in char:
		char_lst.append({
		"char": c,
		"num": char[c] 
		})
	char_lst.sort(reverse=True,key=sort_on)
	return char_lst

def lower_words(text):
	lowered_string = text.lower()
	return lowered_string

def get_chars_dict(text):
	chars = {}
	for c in text:
		lowered = c.lower()
		if lowered in chars:
			chars[lowered] += 1
		else:
			chars[lowered] = 1
	return chars

def get_num_words(text):
	words = text.split()
	return len(words)

def get_book_text(path):
	with open(path) as f:
		return f.read()

if __name__ == '__main__':
    main()