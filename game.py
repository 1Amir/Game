from random import random
print '--------- Let\'s play text version of Fallout game ---------'


#Short intro
def intro():
	print ("You live in Vault 13, one of few human's shelters after nuclear war. The Water Chip, a "
			"computer chip responsible for the water recycling and pumping machinery of the vault, was broken "
			"and you need to find another one and save all in the Vault. So you go out to Waste Land")
	print '--------------------------------------------------------------------------------'

intro()
#Visited or not places
visit_15, visit_shady, visit_junktown, visit_12, visit_necropolis, save_game = [], [], [], [], [], ['no']

#Main choice where to go and what to do
def serch_for_places():
	random_place = random()
	map_check = raw_input("Check the map? (y/n) ").lower()
	print '--------------------------------------------------------------------------------'
	map_of = {
	'Vault 15': '     3.5 km on south',
	'Shady Sands': '  2 km on east',
	'Junktown': '     1.5 km on north east',
	'Vault 12': '     4 km on south east',
	'Necropolis': '   2.5 kn on north'
	}

	if map_check == 'y' or map_check == 'yes':
		for key in map_of:
			print key, map_of[key]
		decided_to_go = raw_input("where you decided to go?: ").lower()
		print '---'
		print '--'
		print '-'
		if 0 <= random_place < 0.1:
			if decided_to_go == ('Vault 15').lower():
				print 'In some time you find a Vault 15'
				return 1
			elif decided_to_go == ('Shady Sands').lower():
				print 'In some time you find a Shady Sands'
				return 2
			elif decided_to_go == ('Junktown').lower():
				print 'In some time you find a Junktown'
				return 3
			elif decided_to_go == ('Vault 12').lower():
				print 'In some time you find a Vault 12'
				return 4
			elif decided_to_go == ('Necropolis').lower():
				print 'In some time you find a Necropolis'
				return 5
		elif 0.1 <= random_place < 0.3:
			print ('Walked around in Waste Land you find a lemontree.. Here almost everything is dead, abandoned houses, '
					'skeletons everywhere, but lemontree looks prety fresh. Strange...')
			return serch_for_places()
		elif 0.3 <= random_place < 0.5:
			print 'You meet lonely walked lady about 25-27 years old. Suddenly she asks to play a game?? "stone, scissors & papper" for few times'
			play_girl = raw_input('Will you play? (y/n) ').lower()
			
			if play_girl == 'y' or play_girl == 'yes':
				print '--------------------------------------------------------------------------------'
				return more()
			else:
				print "Okey, see you later... I hope"
				return serch_for_places()
		elif 0.5 <= random_place < 0.7:
			print 'Just find another one lonely skeleton...'
			return serch_for_places()
		elif 0.7 <= random_place < 0.8:
			print 'You are tired... Just need to sleep or rest'
			return serch_for_places()
		elif 0.8 <= random_place < 1:
			print 'You meet a couple of raders and they decided to attac you'
			fight_run = raw_input('What will you do, fight or run? (f/r) ').lower()
			combat = random()
			if fight_run == 'f' or fight_run == 'fight':
				if combat < 0.4:
					print 'They are stronger and you loose.. They take everything you had'
					return serch_for_places()
				else:
					print 'You beat them and get some weapons and money. Heh, they use cokes caps like a money))). Such a strange world)))'
					return serch_for_places()
			else:
				if combat < 0.2:
					print 'You tried to run, but they cach you, beat you and take everything you had'
					return serch_for_places()
				else:
					print 'Wow, they almost cach you, but you always run fast'
					return serch_for_places()	
								
	else:
		print 'You decided to walk around'
		print '---'
		print '--'
		print '-'
		if 0 <= random_place < 0.1:
			print 'In some time you suddenly find a Vault 15'
			return 1
		elif 0.1 <= random_place < 0.2:
			print 'In some time you suddenly find a Shady Sands'
			return 2
		elif 0.2 <= random_place < 0.3:
			print 'In some time you suddenly find a Junktown'
			return 3
		elif 0.3 <= random_place < 0.4:
			print 'In some time you suddenly find a Vault 12'
			return 4
		elif 0.4 <= random_place < 0.5:
			print 'In some time you suddenly find a Necropolis'
			return 5
		elif 0.5 <= random_place < 0.65:
			print ('Walked around in Waste Land you suddenly meet strange man who looked just like '
					'postman so you tried to talk to him, but he just run away. Strange...')
			return serch_for_places()
		elif 0.65 <= random_place < 0.8:
			print 'You find some lonely abandoned house. Look like no one lives here for long time.'
			enter_the_door = raw_input('Do you like to check are there something interesting inside? (y/n)').lower()
			gun_food = random()
			if enter_the_door == 'y' or enter_the_door == 'yes' and 0 <= gun_food < 0.3:
				print ("Oh, you're fucking lucky, you find good one shotgun laying under the table. Seems like someone "
						"hide it here. Howewer now it has a new owner:)")
				return serch_for_places()
			elif enter_the_door == 'y' or enter_the_door == 'yes' and 0.3 <= gun_food < 0.6:
				print ("Inside small room, beside the stuff you just noticed some strange box. You're opening and BINGO! "
						"Some food and water here, seem like this house is not abandoned like for first looks")
				return serch_for_places()
			elif enter_the_door == 'y' or enter_the_door == 'yes' and 0.6 <= gun_food < 1:
				print "You enter the house and find realy nothing interesting inside"
				return serch_for_places()
			else:
				return serch_for_places()
		elif 0.8 <= random_place < 1:
			print 'Just find another one lonely skeleton...'
			return serch_for_places()


#Game with the girl
def game():
	girl_choice = random()
	player_choice = raw_input('Choose one of stone, scissors or papper: ').lower()
	#If girl choose stone
	if 0 <= girl_choice < 0.33:
		print "Girl choice is stone."
		if player_choice == "stone":
			print "Your choice is stone too, it's draw!"
		elif player_choice == "scissors":
			print "Your choice is scirrors, you loose!"
		elif player_choice == "papper":
			print "Your choice is papper, you win!"
		else:
			print "You can choose stone, scissors or papper only!!!"
	#If girl choose scissors
	elif 0.33 <= girl_choice < 0.66:
		print "Girl choice is scissors."
		if player_choice == "scissors":
			print "Your choice is scissors too, it's draw!"
		elif player_choice == "papper":
			print "Your choice is papper, you loose!"
		elif player_choice == "stone":
			print "Your choice is stone, you win!"
		else:
			print "You can choose stone, scissors or papper only!!!"
	#If girl choose papper
	else:
		print "Girl choice is papper."
		if player_choice == "papper":
			print "Your choice is papper too, it's draw!"
		elif player_choice == "stone":
			print "Your choice is stone, you loose!"
		elif player_choice == "scissors":
			print "Your choice is scissors, you win!"
		else:
			print "You can choose stone, scissors or papper only!!!"


#If you want to play "stone, scissors and papper" one more time
def more():
	game()
	once_more = raw_input('--------- Wanna some more??? (y/n) ').lower()
	if once_more == 'y' or once_more == 'yes':
		more()
	else:
		print "Good bye!"
		print '--------------------------------------------------------------------------------'
		return serch_for_places()

#Review of founded place
def place_founded(place):
	print '--------------------------'
	if place == 1:
		if not visit_15:
			print ("Vault 15 is another one vault of Vaut Tec Web, and here has to be a "
					"water chip you need. Unfortunatly it looks abandoned for a long "
					"time... There's nothing useful or interesting here")
			visit_15.append('visited')
		return place_founded(serch_for_places())
	elif place == 2:
		if not visit_shady:
			print ('Shady Sands is a small willage, founded by former Vault 15 members.. Now they are farmers, in majority. '
					'No signs of high technologies for a first look.')
			visit_shady.append('visited')
		return place_founded(serch_for_places())
	elif place == 3:
		if not visit_junktown:
			print ("Junktown is a big city, with casino and bordels. Also here are a lot of stores, including "
					"gun stores. Let's walk around and watch what can we find")
			visit_junktown.append('visited')
		return place_founded(serch_for_places())
	elif place == 4:
		if not visit_12:
			print ('Vault 12 is abandoned... It seems like everything in nowadays world is lost.. Where do I have to '
					'find what I look for? Wait, I heat some noise there, inside. What a FU.. MUTANTS!!!')
			visit_12.append('visited')
		go_in = raw_input('It seems there must be something important inside. Should I try to get in? (y/n) ').lower()
		if go_in == 'y' or go_in == 'yes':
			save_game[0] = raw_input('Do you want to save game before go inside? (y/n) ')
			return explore_place()
		else:
			return place_founded(serch_for_places())
	else:
		print 'Necropolis is a ... "village" populated with a zombies.. They have Vault 12 closes. What the hell was done to them???.'
		return place_founded(serch_for_places())


#Explore the Vault 12 to find Water chip
def explore_place():
	print ("At the entrance into the vault you can see a big strong mutant Gregore. He looks very strong but not very smart. Oh, he just "
			"noticed you and order you to come slowly or he'll shoot you. Lets try to talk to him")
	print "Gregore - Who are you? I don't like you!"
	lst = ['1. Mutant', '2. Zombie', '3. Robot', '4. Alien', '5. Man', '6. School-girl', '7. Boy-scout', '8. Cow', '9. Tree'] 
	for var in lst:
		print var
	mut_talk = int(raw_input('Choose number: '))
	print lst[mut_talk - 1][3:]
	print '--------------------------'
	luck = random()
	if mut_talk == 1:
		if 0 <= luck < 0.5:
			print "Hm, you look strange for mutant but okey, you can go inside"
			print '---'
			print '--'
			print '-'
			print "You find the Water Chip inside!!! Your vault is saved!!!"
		elif 0.5 <= luck < 0.7:
			print "Oh, sorry dude, never seen you here before, come in!"
			print '---'
			print '--'
			print '-'
			print "You find the Water Chip inside!!! Your vault is saved!!!"
		else:
			print "You tried to fool Gregore, that was bad idea.. Gregore start shooting and you die!"
	elif mut_talk == 2:
		if 0 <= luck < 0.3:
			print "I don't like zombies, go away"
			return place_founded(serch_for_places())
		elif 0.3 <= luck < 0.6:
			print "Realy? Okey, anyway there is nothing you to do here. Go away"
			return place_founded(serch_for_places())
		else:
			print "Ha-Ha-Ha, die you maggot!!!  Gregore start shooting and you die!"
	elif mut_talk == 3:
		if  0 <= luck < 0.4:
			print "Hm, okey. You go inside"
			print '---'
			print '--'
			print '-'
			print "You find the water chip inside!!! Your vault is saved!!!"
		else:
			print "What a??? You tried to fool Gregore, that was bad idea..  Gregore start shooting and you die!"
	elif mut_talk == 4:
		if 0 <= luck < 0.2:
			print "Gregore run away and leave his minigun.  You take it and go inside the vault"
			print '---'
			print '--'
			print '-'
			print "You find the Water Chip inside!!! Your vault is saved!!!"
		else:
			print "What a??? You tried to fool Gregore, that was bad idea..  Gregore start shooting and you die!"
	elif mut_talk == 5:
		print "Ha-Ha-Ha, die you maggot!!!  Gregore start shooting and you die!"
	elif mut_talk == 6:
		print "What a??? You tried to fool Gregore, that was bad idea..  Gregore start shooting and you die!"
	elif mut_talk == 7:
		print "What a??? You tried to fool Gregore, that was bad idea..  Gregore start shooting and you die!"
	elif mut_talk == 8:
		print "What a??? You tried to fool Gregore, that was bad idea..  Gregore start shooting and you die!"
	elif mut_talk == 9:
		if 0 <= luck < 0.4:
			print "Gregore are baffled, but can't say nothing. You just go inside very slowly)))"
			print '---'
			print '--'
			print '-'
			print "You find the Water Chip inside!!! Your vault is saved!!!"
		else:
			print "What a??? You tried to fool Gregore, that was bad idea..  Gregore start shooting and you die!"
	else:
		print "Gregore start shooting and you die!"

	if save_game[0] == 'y' or save_game[0] == 'yes':
		load_save_game = raw_input('Do you want to load saved game? (y/n): ').lower()
		if load_save_game == 'y' or load_save_game == 'yes':
			print '--------------------------'
			print 'loading...'
			print '--------------------------'
			explore_place()
		else:
			print '--------------The End--------------'

place_founded(serch_for_places())

