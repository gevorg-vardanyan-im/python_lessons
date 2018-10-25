'''
@task_link: https://py.checkio.org/en/mission/most-wanted-letter/

@task_description:
You are given a text, which contains different english letters and punctuation symbols.
You should find the most frequent letter in the text.
The letter returned must be in lower case.
While checking for the most wanted letter,
	casing does not matter,
	so for the purpose of your search,
	"A" == "a".
Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
If you have two or more letters with the same frequency,
	then return the letter which comes first in the latin alphabet.
	For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

@input: A text for analysis as a string.

@output: The most frequent letter in lower case as a string.

'''


def checkio(text):
	'''
	This function finds the most frequent letter in the text.
	'''

	text_list = []
	for character in text:
		text_list.append(character)

	frequency_dict = {}
	# convert list to lowercase due to task requirement
	text_list = [li.lower() for li in text_list]
	# remove non alphabetic values from the list
	text_list = list(filter(lambda a: a.isalpha(), text_list))

	for letter in text_list:
		if letter not in frequency_dict:
			frequency_dict[letter] = text_list.count(letter)

	maximum = max(sorted(frequency_dict), key = frequency_dict.get)
	return maximum

if __name__ == '__main__':
	print("Example:")
	print(checkio("Hello Worlddddddd!"))

	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio("Hello World!") == "l", "Hello test"
	assert checkio("How do you do?") == "o", "O is most wanted"
	assert checkio("One") == "e", "All letter only once."
	assert checkio("Oops!") == "o", "Don't forget about lower case."
	assert checkio("AAaooo!!!!") == "a", "Only letters."
	assert checkio("abe") == "a", "The First."
	print("Start the long test")
	assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
	print("The local tests are done.")
