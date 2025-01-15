#!/usr/bin/env python3

import random
import time
import os
import sys
import subprocess

	
def start_countdown(seconds, message):
	for count in range(1, seconds + 1):
		percent_complete = (count / seconds) * 100
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f"{message} Visszaszámlálás: {seconds - count} másodperc")
		sys.stdout.write(f"[{'#' * (count * 100 // seconds):<100}] {percent_complete:.2f}%\r")
		sys.stdout.flush()
		time.sleep(1)
			
	sys.stdout.write("\n")
	print(f"Lejárt az idő")
	os.system("afplay ./vege.mp3")
	
def start_game():
	clear_console()
	letter = get_random_letter()
	print(f"A következő betű a(z): - {letter} -")
	if get_user_input("Jó lesz? Mehet? (i|n)"):
		clear_console()
		start_countdown(120, f"Mehet a játék! A jelenlegi betű: - {letter} -")
		if get_user_input("Mégegy játék? (i|n)"):
			start_game()
		else:
			print("\nVége\n")
	else:
		start_game()
		
def get_user_input(message):
	while True:
		char = read_character_input(message)
		if char in ['i', 'n']:
			return char == 'i'
		else:
			print(message)
			
def get_random_letter():
	alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Z']
	letter = random.choice(alph)
	if letter in ["Q", "W", "Y", "X"]:
		return get_random_letter()
	else:
		return transform_letter(letter)
	
def transform_letter(letter):
	transformations = {
		"A": "A,Á",
		"C": "C,CS",
		"D": "D,DZ,DZS",
		"E": "E,É",
		"G": "G,GY",
		"I": "I,Í",
		"J": "J,LY",
		"N": "N,NY",
		"O": "O,Ó,Ö,Ő",
		"S": "S,SZ",
		"T": "T,TY",
		"U": "U,Ú,Ü,Ű",
		"Z": "Z,ZS"
	}
	return transformations.get(letter, letter)

def read_character_input(prompt):
	print(prompt)
	while True:
		char = input().strip().lower()
		if char in ['i', 'n']:
			return char
		else:
			print(prompt)
			
def clear_console():
	os.system('cls' if os.name == 'nt' else 'clear')
	
# Main:
start_game()
