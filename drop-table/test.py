string = 'HANGMAN_GAME_145'
string1 = 'HANGMAN_GAME_ok'
string2 = 'HANGMAN_GAME_14'
string3 = 'HANGMAN_GAME_5'

def convertStr(str):

	if any(char.isdigit() for char in str):
		return None
	new_str = str.lower().replace('_', ' ')
	res = [str.capitalize() for str in new_str.split()]

	return ' '.join(res)


convertStr(string)
convertStr(string1)
convertStr(string2)
convertStr(string3)