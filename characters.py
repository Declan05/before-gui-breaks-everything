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
        description = f"""
          Class: {self.__class__.__name__}
          ----------------
          Name: {self.name}
          Health: {self.health}
          Full Damage: {self.full_damage}
        """
        return description
      
    # ATTACKS
    def conservative_attack(self, attack_name):
        # NO DAMAGE DEALT TO SELF
        damage = self.full_damage * uniform(0.5, 0.6)
        damage = round(damage)
        return damage

    def balanced_attack(self, attack_name):
        # MINOR DAMAGE DEALT TO SELF
        damage = self.full_damage * uniform(0.3, 0.8)
        damage = round(damage)
        return damage

    def aggressive_attack(self, attack_name):
        # MEDIUM DAMAGE DEALT TO SELF
        damage = self.full_damage * uniform(0.1, 1.0)
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

    def get_aggro_attack(self):
        return "Skateboard Smash"

    def get_bal_attack(self):
        return "Jumpkick"
    
    def get_con_attack(self):
        return "Sling Shot"

    
    #SETTER
    def set_damage_multi(self,damage_multi):
        self.damage_multi = damage_multi  

    def attack(self, opponent, button_selected):
        damage = 0
        if button_selected == 1:
            damage = self.conservative_attack("Sling Shot")
            print(f"{self.name} used Sling Shot...")
        elif button_selected == 2:
            damage = self.balanced_attack("Jumpkick")
            print(f"{self.name} used... placeholder")
        elif button_selected == 3:
            damage = self.aggressive_attack("Skateboard Smash")
            print(f"{self.name} used Skateboard Smash...")
        opponent.take_damage(round(damage * 1.1))

            
    
class Health(Character):
    def __init__(self, name, full_damage, health, speech):
        super().__init__(name, full_damage, health,speech)
    
    # GETTER
    # def get_regenerate(self):
    #     return self.regenerate

    def get_aggro_attack(self):
        return "Hammer Time"

    def get_bal_attack(self):
        return "Flying Kick"
    
    def get_con_attack(self):
        return "Sling Shot"
    # # SETTER   
    # def set_regenerate(self, regenerate):
    #     self.regenerate = regenerate

    def regenerate(self):
        self.set_health = self.get_health() * 1.1
    
    def attack(self, opponent, attack_type):
        damage = 0
        if attack_type == 1:
            damage = self.conservative_attack("Sling Shot")
            print(f"{self.name} used Sling Shot...")
        elif attack_type == 2:
            damage = self.balanced_attack("Flying Kick")
            print(f"{self.name} used Flying Kick...")
        elif attack_type == 3:
            damage = self.aggressive_attack("Sling Shot")
            print(f"{self.name} used Sling Shot...")
            
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

    def get_aggro_attack(self):
        return "Skipping Rope Whip"

    def get_bal_attack(self):
        return "Broom attack"
    
    def get_con_attack(self):
        return "Sling Shot"
    # SETTER    
    def set_block_damage(self, block_damage):
        self.block_damage = block_damage
    
    def attack(self, opponent, attack_type):
        damage = 0
        if attack_type == 1:
            damage = self.conservative_attack("Sling Shot")
            print(f"{self.name} used Sling Shot...")
        elif attack_type == 2:
            damage = self.balanced_attack("Broom attack")
            print(f"{self.name} used Broom attack...")
        elif attack_type == 3:
            damage = self.aggressive_attack("Skipping Rope Whip")
            print(f"{self.name} used Skipping Rope Whip...")
            
        opponent.take_damage(damage)

