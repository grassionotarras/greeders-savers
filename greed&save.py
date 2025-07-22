import random
import time


# <oasis> is the enviroment

# there will be 4 kinds of Bobs, greeders, savers, guardians, gangsters.
# Savers will share the food they find and have 50% chance to reproduce.
# greeders are greedy and will steal the food, making it so that they have 100% chance to reproduce.
# if a guardian is paired with a greeder it will remove the greeded and have a 33% chance to die, can evolve from a saver.
# if a guardian is paired with a saver it will act like a saver.
# gangsters are greeders but stronger. They have a 100% chance to reproduce if they steal and put up a good fight with guards.
# if 2 greeders meet then there will be 0-25% chance of reproducing.



class Bob:

    def __init__(self, g_amount, s_amount, tries, gu_amount=0, ga_amount=0):
        self.g_amount = g_amount
        self.s_amount = s_amount
        self.gu_amount = gu_amount
        self.ga_amount = ga_amount
        self.tries = tries

    def oasis_s(self):
        start = time.time()

        for _ in range(self.tries):

           types = (
               [1] * self.s_amount +
               [2] * self.g_amount +
               [3] * self.gu_amount +
               [4] * self.ga_amount
           )

           if len(types) < 2:
               break

           rs = random.randint(1, 2)
           rg = random.randint(1, 2)

           

           

           if rs == 1 and rg == 1:

                y = random.randint(1, 2)

                
                if y == 1:
                    if random.random() < 0.1:
                        self.gu_amount += 1
                    else:
                        self.s_amount += 1
                else:
                    x = random.randint(1, 3)

                    if x == 1 or x == 2:
                        self.s_amount -= 1
                    
           # greeder/saver
           elif rs == 1 or rg == 1 and rs == 2 or rg == 2:

               if random.random() < 0.5:
                   if random.random() < 0.1:
                        self.ga_amount += 1
                   else:
                        self.g_amount += 1

           # greeder/greeded
           elif rs == 2 and rg == 2:

                self.g_amount -= 2

           # guardian/saver
           elif (rs == 3 and rg == 1) or (rs == 1 and rg == 3):
                
                if random.random() < 0.5:
                    self.s_amount += 1

           # gangster/saver
           elif rs == 1 or rg == 1 and rs == 4 or rg == 4:
              
                if random.random() < 0.1:
                    self.ga_amount += 1
                else:
                    self.g_amount += 1

                if random.random() < 0.33:
                    self.s_amount -= 1


           # gangster/guardian
           elif (rs == 3 and rg == 4) or (rs == 4 and rg == 3):
                self.ga_amount -= 1  
                self.gu_amount -= 1

           

           # guardian/guardian
           elif rs == 3 and rg == 3:
                pass
           
           # gangster/gangster
           elif rs == 4 and rg == 4:
               pass
           
           #guardian/greeder
           elif (rs == 3 and rg == 2) or (rs == 2 and rg == 3):
                self.g_amount -= 1  
                if random.random() < 0.33:
                    self.gu_amount -= 1

           # power sc
           if self.s_amount > self.g_amount:

               if random.random() < 0.1:
                   self.gu_amount += 1
               else:
                   self.s_amount += 1

           # greed burnout
           if random.random() < 0.01:
                self.g_amount - 1



           print(f'{self.s_amount} savers remain, {self.gu_amount} of guardians remain, {self.ga_amount} of gangsters remain while {self.g_amount} greeders remain.')

        end = time.time()
        elapsed = end - start

        print(f'Elapsed: {elapsed}s SUCCESS.')





        

oasis = Bob(100, 100, 10000)
oasis.oasis_s()