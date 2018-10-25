'''
@task_link: https://py.checkio.org/en/mission/non-unique-elements/

@task_description
If you have 50 different plug types, appliances wouldn't be available and would be very expensive.
But once an electric outlet becomes standardized,
	many companies can design appliances,
	and competition ensues,
	creating variety and better prices for consumers. 
-- Bill Gates

You are given a non-empty list of integers (X).
For this task, you should return a list consisting of only the non-unique elements in this list.
To do so you will need to remove all unique elements (elements which are contained in a given list only once).
When solving this task, do not change the order of the list.
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].

@input: A list of integers.

@output: An iterable of integers.

@how_it_is_used: This mission will help you to understand how to manipulate arrays,
	something that is the basis for solving more complex tasks.
The concept can be easily generalized for real world tasks.
For example: if you need to clarify statistics by removing low frequency elements (noise).

'''


def create_frequency_dict(data):
	'''
	This function will create a dict of frequency of given list elements.
	'''
	frequency_dict = {}
	for letter in data:
		if letter not in frequency_dict:
			frequency_dict[letter] = data.count(letter)

	return frequency_dict

def checkio(data):
	'''
	This function will return list of non-unique elements.
	'''

	frequency_dict = create_frequency_dict(data)
	for key, value in frequency_dict.items():
		if value == 1:
			# remove element from list with '1' frequency
			data = list(filter(lambda a: a != key, data))

	return data

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")