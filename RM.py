import os
import requests
import json
import random

current_page = 1
current_characters = []

def showCharacterInfo(char_id):
	print("Name: " + current_characters[char_id]['name'])
	print("Status: " + current_characters[char_id]['status'])
	print("Species: " + current_characters[char_id]['species'])
	print("Type: " + current_characters[char_id]['type'])
	print("Gender: " + current_characters[char_id]['gender'])

def showPageCharacters(page):

	# Fetching data for a certain page of characters
	global current_characters
	response_API = requests.get('https://rickandmortyapi.com/api/character/?page='+str(page))
	data = response_API.text
	parse_json = json.loads(data)
	characters = parse_json['results']
	current_characters = characters

	print("Current Page: " + str(page))

	# Showing the list of characters
	print("\nSelect a character: ")
	for x in range(len(characters)):
		name = characters[x]['name']
		print(str(x+1)+" - ", end="", flush=True)
		print(name)
	print("21 - Random")

	# Showing options related to changing pages or ending execution
	print("\nSelect a menu option: ")
	print("22 - Next Page")
	print("23 - Previous Page")
	print("24 - Exit\n")

def showMainMenu():

	# Initial introduction explaining how the program works
	print("\nWelcome to the Rick and Morty character selector!")
	print("Please select the character you want to learn more about.")
	print("If you select the 'Random' option, a random character will be presented.")
	print("To see more characters, select one of the page changing option.")
	print("To exit the character selector press the 'Exit' option.\n")

# Start by showing the 'Main Menu' and showing the characters of the first page
showMainMenu()
showPageCharacters(current_page)

# Continually wait for user input to select options from the menus
while True:
	selection = int(input())

	# Show random character
	if selection == 21:
		number = random.randint(0,19)
		showCharacterInfo(number)
		print('\n')

	# Show next page
	elif selection == 22:

		# Check if you reached the last page available
		if(current_page < 42):
			showPageCharacters(current_page+1)
			current_page += 1
		else:
			print("\nYou are already at the last page.\n")
			showPageCharacters(current_page)

	# Show previous page
	elif selection == 23:

		# Check if you reached the first page available
		if(current_page > 1):
			showPageCharacters(current_page-1)
			current_page -= 1
		else:
			print("\nYou are already at the first page.\n")
			showPageCharacters(current_page)

	# Exit
	elif selection == 24:
		print("\nGoodbye!")
		exit()

	# Checking for a valid input
	elif selection > 24 or selection < 0:
		print("\nPlease insert a valid number.\n")
		showPageCharacters(current_page)

	# Show selected character
	else:
		showCharacterInfo(selection-1)
		print('\n')

