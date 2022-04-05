
    #
import random
import time
playing = 'yes'
approach = 'I dont know man what you want from me bro just chill for a sec'
cave = '37'
fren = '4'
turn = '16'
pocket = '500000000'
while playing == 'yes' :

    approach = 'I dont know man what you want from me bro just chill for a sec'
    cave = '37'
    fren = 4
    turn = '16'
    pocket = 500000000
    import random

    print('yo. you are a great royal knight, you serve the king and have made a holy oath to protect the people of this kingdom.')
    print('today is your day off, so you naturally decided to go hunting dragons in order to relax.')
    print('as you wander through the wilderness on the kingdoms outskirts, you come across 2 dark caves.')
    print('the first cave, gives off a nice breeze, but as you approach, the breeze becomes moist and uncomfortably warm.')
    print('the second cave, emits an ominous stench that lines the ground like an evil bog, the feeling lessens as you approach the cave, taunting you.')
    while approach != 'yes' and approach != 'no' :
        print('do you want to enter a cave (yes or no)')
        approach = input()
    print('haha, your choice doesent actually matter, of  course you would approach! you are a royal knight afterall.')
    while cave != '1' and cave != '2' :
        print('which cave do you enter(1 or 2)')
        cave = input()
    if cave == '1' :
        print('you enter the moist cave, bearing the heat.')
    else :
        print('you enter the ominous cave, gving in to temptation')
    print('its dark and hard to navigate, but you eventually reach the end, only to be greated with a horde of gold, and a monstrous dragon.')
    fren = random.randrange(1, 3)
    if fren == 1 :
        print('the dragon looks to you and says,"yo whats up dawg, you came all the way here just for me? here, take like 56,300 dollers."')
        print('*you gained 56,300 dollers')
        print('"so, you want to stay for dinner?"')
        if approach == 'no' :
            print('you recall how you did not want to enter the cave in the first place and decide to politly decline the dragons offer.')
            print('as you return to the kingdom with newfound riches, you wonder if visiting that dragon again would be a good idea...')
            print('but perhaps its best a knight not associate with such a beast, as nice as the beast may be.')
            print('THE END')
        else :
            print('you recall how willing you were to enter the cave in the first place, and decide to oblige the dragons humble request.')
            print('over the course of the dinner, you forge a new bond with the dragon, and vow to return soon, perhaps with more company...')
            print('the king and other knights would surely approve of a dragon such as this one.')
            print('THE END(the best one)')
    else :
        print('the dragon looks at you with a burning fury, it is sure to attack!')
        if approach == 'no' :
            print('you recall not wanting to enter the cave in the first place, so you run away as fast as you can.')
            print('as you return to the kingdom, you contemplate your actions...')
            print('you may have lived to tell the tale of a dragon, but your honour will surely suffer.')
            print('THE END')
        else :
            print('you recall the courage you had to enter this cave in the first place, and decide to fight the dragon...')
            print('your turn (choose 1,2 or 3):')
            print('ATTACK (1) ')
            print('DEFEND (2) ')
            print('ITEM   (3) ')
            turn = input()
            if turn == '1' :
                print('in one swift motion, you draw your sword, striking the dragon, but the blade does not pierce the dragons skin.')
                print('the dragon fights back with fiery breath.')
                print('YOU DIED')
            else:
                if turn == '2' :
                    print('the dragon readys its flaming breath, but you stand your ground, shield at the ready.')
                    print('the fire doesent care about your shield and...')
                    print('YOU DIED')
                else :
                    print('you reach into your pocket, trying to find anyhting that may be useful.')
                    pocket = random.randrange(1, 4)
                    if pocket == 1 :
                        print('the first thing you find in your pocket is an assortment of seasonings.')
                        print('you throw the seasonings at the dragon, and they explode into a puff of flavour, the smell is strong.')
                        print('the dragon starts to melt. it turns out pepper is the weakness of all dragons.')
                        print('the dragon is defeated.')
                        print('after rounding up the riches of the dragon, you begin to head back to the kingdom, with a new tale to tell.')
                        print('THE END')
                    else :
                        if pocket == 2 :
                            print('the first thing you find in your pocket is an M16 assault rifle, modified to chamber rounds of extremely high caliber.')
                            print('you shoot the dragon, and it dies.')
                            print('the e n d')
                        else :
                            print('the first thing you find in your pocket is an action figure of the dragons favourite character, discontinued by the manufacturer')
                            print('the dragon spares you, impressed by the collectable')
                            print('you sell it for like at least 17 euros and take your leave')
                            print('THE END')
    print('wowowow its over')
    print('wanna play again? (yes or no)')
    playing = input()
                                
