# Learning

#OOP
class Hero:
	
	def __init__(self, name, hp, defense, hit_chance, items, speed, resistences)
		self.name = name
		self.hp = hp
		self.defense = defense 
		self.hit_chance = hit_chance
		self.items = items
		self.speed = speed
		self.resistences = resistences
	
	def attk(self, opposing_character):
		print(chance to hit of character)
		print(defense of opposing character)
		print(print hit or miss)
		if attack_hit = True:
			print(attack dmg of character)
			print(defene of opposing character)
			print(total dmg done)
		else:
			print(your attack missed)
		

def hero(name):
	print(name)
	print(hp)
	print(defense)
	print(to hit chance)
	print(items)
	print(speed)
	print(resistences) 

def monster(name):
	print(name)
	print(hp)
	print(defense)
	print(to hit chance)
	print(items)
	print(speed)
	print(resistences)
	

hero()
monster()
attk(goblin, hero)
