from random import uniform

class Character(object):
    def __init__(self, name, full_damage, health, speech):
        self.name = name
        self.full_damage = full_damage
        self.health = health
        self.speech = speech
    
    # GETTERS
    def get_name(self):
        return self.name

    def get_full_damage(self):
        return self.full_damage
          
    def get_health(self):
        return self.health
    
    #SETTERS
    def set_name(self,name):
        self.name = name

    def set_full_damage(self,full_damage):
        self.full_damage = full_damage

    def set_health(self,health):
        self.health = health

    
    def describe(self):
		# type(self).__name__ ?
        print(f"""
          Class: {self.__class__.__name__}
          ----------------
          Name: {self.name}
          Health: {self.health}
          Full Damage: {self.full_damage}
        """)
    
    # RECOIL DAMAGE TO SELF
    def attack_self(self, damage):
        pass
        

    # ATTACKS
    def conservative_attack(self, attack_name):
        # NO DAMAGE DEALT TO SELF
        damage = self.full_damage * uniform(0.4, 0.6)
        damage = round(damage)
        return damage

    def balanced_attack(self, attack_name):
        # MINOR DAMAGE DEALT TO SELF
        damage = self.full_damage * uniform(0.6, 0.8)
        damage = round(damage)
        return damage

    def aggressive_attack(self, attack_name):
        # MEDIUM DAMAGE DEALT TO SELF
        damage = self.full_damage * uniform(0.8, 1.0)
        damage = round(damage)
        return damage
        
    #METHODS
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 1:
            self.health = 0
        print(f"\033[31m{self.name} has taken {damage} damage.\033[0mTheir health is now \033[32m{self.health}.\033[0m\n")    


# CHARACTER SUBCLASSES
class Assault(Character):
    def __init__(self, name, full_damage, health, speech, damage_multi):
        super().__init__(name, full_damage, health, speech)
        self.damage_multi = damage_multi
    
    #GETTER
    def get_damage_multi(self):
        return self.damage_multi
    #SETTER
    def set_damage_multi(self,damage_multi):
        self.damage_multi = damage_multi  

    def attack(self, opponent):
        print("""
        1. Conservative
        2. Balanced
        3. Aggressive
        """)
        attack_type = input("Choose your attack! ").lower()
        damage = 0
        if "con" in attack_type or "1" in attack_type:
            damage = self.conservative_attack("Bottle Squirt")
            print(f"{self.name} used Bottle Squirt...")
        elif "bal" in attack_type or "2" in attack_type:
            damage = self.balanced_attack("Wail")
            print(f"{self.name} used Wail...")
        elif "ag" in attack_type or "3" in attack_type:
            damage = self.aggressive_attack("Hammer Smash")
            print(f"{self.name} used Hammer Smash...")
        opponent.take_damage(round(damage * 1.1))

            
    
class Health(Character):
    def __init__(self, name, full_damage, health, speech):
        super().__init__(name, full_damage, health,speech)
    
    # GETTER
    # def get_regenerate(self):
    #     return self.regenerate
    # # SETTER   
    # def set_regenerate(self, regenerate):
    #     self.regenerate = regenerate

    def regenerate(self):
        self.set_health = self.get_health() * 1.1
    
    def attack(self, opponent):
        print("""
        1. Conservative
        2. Balanced
        3. Aggressive
        """)
        self.get_health()
        attack_type = input("Choose your attack! ")
        damage = 0
        if "1" in attack_type or "con" in attack_type:
            damage = self.conservative_attack("Belch")
            print(f"{self.name} used Belch...")
        elif "2" in attack_type or "bal" in attack_type:
            damage = self.balanced_attack("Doughnut Throw")
            print(f"{self.name} used Doughnut Throw...")
        elif "3" in attack_type or "ag" in attack_type:
            damage = self.aggressive_attack("Strangle")
            print(f"{self.name} used Strangle...")
            
        opponent.take_damage(damage)
        self.regenerate()
        self.get_health()
    

class Defence(Character):
    def __init__(self, name, full_damage, health, speech, block_damage):
        super().__init__(name, full_damage, health, speech)
        self.block_damage = block_damage
        
    def take_damage(self, damage):
        damage -= 0.1
        damage = round(damage)
        self.health -= damage
        if self.health < 1:
            self.health = 0
        print(f"\033[31m{self.name} has taken {damage} damage.\033[0mTheir health is now \033[32m{self.health}.\033[0m\n")    
    # GETTER
    def get_block_damage(self):
        return self.block_damage 
    # SETTER    
    def set_block_damage(self, block_damage):
        self.block_damage = block_damage
    
    def attack(self, opponent):
        print("""
        1. Conservative
        2. Balanced
        3. Aggressive
        """)
        attack_type = input("Choose your attack! ")
        damage = 0
        if "1" in attack_type or "con" in attack_type:
            damage = self.conservative_attack("Slam Poetry")
            print(f"{self.name} used Slam Poetry...")
        elif "2" in attack_type or "bal" in attack_type:
            damage = self.balanced_attack("Saxophone Screech")
            print(f"{self.name} used Saxophone Screech...")
        elif "3" in attack_type or "ag" in attack_type:
            damage = self.aggressive_attack("Book Throw")
            print(f"{self.name} used ...")
            
        opponent.take_damage(damage)

