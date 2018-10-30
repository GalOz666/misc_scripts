def bracket_push(phrase):
	memory_str = []
	closure_dict = {"(" : ")", "[" : "]", "{" : "}"}
	for letter in phrase:
		if letter in "([{":
			memory_str.append(letter)
		elif letter in ")]}":
			try:
				a = memory_str.pop()
				if closure_dict[a] == letter:
					continue
				else:
					return False
			except IndexError:
				return False
	return memory_str == []
