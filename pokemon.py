class Pokemon:
  def __init__(self, name, typeP, level):
    self.ko = False
    self.name = name
    self.level = level
    self.typeP = typeP
    self.max_health = level
    self.cur_health = self.max_health

  def lose_health(self, num):
    self.cur_health -= num
    if self.cur_health <= 0:
      self.ko = True
  
  def gain_health(self,num):
    self.cur_health += num

  def knock_out(self):
      self.cur_health = 0
      self.ko = True

  def revive(self):
    if knock_out():
      self.cur_health = self.max_health

  def attack(self, nameT):
    if nameT.cur_health <= 0:
      nameT.knock_out()
    else:
      if self.typeP == "Grass":
        if nameT.typeP == "Fire":
          nameT.lose_health(nameT.level / 2)
        if nameT.typeP == " Water":
          nameT.lose_health(nameT.level * 2)
      if self.typeP == "Fire":
        if nameT.typeP == "Water":
          nameT.lose_health(nameT.level / 2)
        if nameT.typeP == " Water":
          nameT.lose_health(nameT.level * 2)
      if self.typeP == "Water":
        if nameT.typeP == "Grass":
          nameT.lose_health(nameT.level / 2)
        if nameT.typeP == " Fire":
          nameT.lose_health(nameT.level * 2)

class Trainer:
  def __init__(self, namePs, pokes, potions):
    self.namePs = namePs
    self.pokes = pokes[:6] if len(pokes) > 6 else pokes
    self.active = self.pokes[0]
    self.potions = potions

  def use_potion(self):
    if self.potions > 0 and self.active.cur_health <= self.active.max_health - 5:
      if self.active.ko == False:
        self.active.gain_health(5)
        print(f'Potion used! {self.active.name} now has {self.active.cur_health} health')
      else:
        self.active.revive()
        self.active.gain_health(5)
        print(f'Potion used! {self.active.name} was revived and now has {self.active.cur_health} health')
    else:
      print("No potion left!")
  
  def attackTrainer(self, trainerT):
    if trainerT.active.ko == False:
      self.active.attack(trainerT.active)
      print(f'Attack! {trainerT.active.name} of {trainerT.namePs} now has {trainerT.active.cur_health} health.')
    else:
      print(f'Cannot attack! {trainerT.active.name} of {trainerT.namePs} was knocked out!')

  def switch(self, num):
    if num <= 6:
      if self.pokes[num] == self.active:
        print("Pokemon is already in use")
      elif self.pokes[num].ko == True:
        print("Pokemon is knocked out. Please use potion!")
      else:
        self.active = self.pokes[num]
        print(f'Pokemon swapped to {self.active.name}')
    else:
      print("Pokemon is invalid!")

Venusaur = Pokemon('Venusaur', 'Grass', 5)
Charizard = Pokemon('Charizard', 'Fire', 5)
Blastoise = Pokemon('Blastoise', 'Water', 5)

Ash = Trainer('Ash Kectup', [Venusaur, Charizard, Blastoise], 0)

User = Trainer('Lynh Mochi', [Blastoise, Charizard, Venusaur], 1000)

User.attackTrainer(Ash)
Ash.attackTrainer(User)
User.switch(0)
User.switch(1)
User.use_potion()
User.attackTrainer(Ash)
Ash.switch(2)
User.attackTrainer(Ash)
Ash.attackTrainer(User)
User.attackTrainer(Ash)