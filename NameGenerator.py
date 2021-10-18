import random

# General lists of syllables, prefixes, suffixes, races, characteristics, and plot hooks to pull from. Can be expanded
# or items removed as preferred.
syllables = ['Arc', 'Bar', 'Can', 'Caz', 'Cha', 'Ale', 'Bor', 'Ben', 'Dar', 'Dag', 'Del', 'Dyn', 'Een', 'Est', 'Fan',
             'Fes', 'Fly', 'Gha', 'Gre', 'Gri', 'Sha', 'Kha', 'Vor', 'Var', 'Kaz', 'Par', 'Zen', 'Zish', 'Kol', 'Phy',
             'Pin', 'Pal', 'Tar', 'Get', 'For', 'Spa', 'Shi', 'Sho', 'Ken', 'Tay', '\'Ik', '\'Cha', 'Zar', 'Ry', 'As',
             'co', 'sa', 'an', 'le', 'ta', 'sa', 'se', 'sey', 'lie', 'las', 'or', 'chi', 'kay', 'er', 'tey', 'no', 'na',
             'ram', 'ro', 'sh', 'ich', 'vos', 'yi', 'quo', 'wri', 'wro', 'ooo', 'ash', 'kie', 'ie', 'po', '\'Ka',
             '\'ii', ' vas', 'ha', 'mi', 'che', 'elle', 'hea', 'thea', '\'Xor', 'by', 'big', 'sal', 'uh', 'ju', 'wer',
             'a', 'tor', 'bjorn', 'mald', 'vald', 'tyn', 'er', 're', 'col', 'cur', 'choo', 'try', 'raja', 'weed', 'que',
             'fios', 'stal', 'gro', 'op', '\'Za', 'puri', 'yus', 'Wel', 'Wes', 'bile', 'ste', 'ven', 'ash', 'Bre',
             'nt', 'Ian', 'Jen', 'Kev', 'in', 'Rach', 'Sara', 'Kel', 'Pow', 'acha', 'sas', 'ex', 'al', 'bi', 'lo', 'li',
             'ti', 'to', 'ri', 'aes', 'de', 'di', ' von ', 'ley', 'ren', 'tare', 'lee', 'hai']

prefixes = ['Doctor', 'Sergent', 'Captain', 'Lieutenant', 'Elder', 'professor', 'Earl', 'Duke', 'Sir', 'Squire',
            'Blacksmith', 'Seven fingers', 'One-eye', 'Poor', 'Tyrannical', 'Scribe', 'Bear fucker', 'Elder', 'Sultan',
            'Lady', 'Lord', 'Your Grace', 'His Excellency', 'Goodman', 'Goodwife', 'Midwife', 'Bishop', 'Cardinal',
            'Father', 'Pastor', 'Master', 'Chairman', 'Mage', 'Wizard', 'Fellow', 'Minister', 'Constable', 'Herald',
            'Secretary', 'Madam', 'Monsignor', 'Despot', 'Centurion', 'Dame', 'Councillor', 'Nephew', 'Saint', 'Nasty',
            'Foul-mouthed', 'Kind', 'Ol\'', 'Old', 'Young', 'Little', 'Big', 'Shy', 'Timid', 'Senor', 'Complainin\'',
            'Toasty', 'Badger-catcher', 'Tiny-hands', 'Immortal', 'Guardian', 'monk', 'druid', 'Thief',
            'Lord of Outlaws', 'King of Thieves', 'Sourfaced', 'Angry', 'Sleepy']

suffixes = ['the strange', 'the lost', 'the shepherd', 'the blessed', 'the holy', 'the ungodly', 'the golden',
            'the corrupt', 'the dirty', 'the vile', 'the kind', 'the courageous', 'the righteous', 'the sane',
            'the insane', 'the fury', 'the pale', 'the victorious', 'the farmer', 'the clean', 'Senior', 'junior',
            'of the golden shoes', 'the beauty', 'the consort', 'the handsome',
            'the sweet', 'of the travellers', 'the wanderer', 'the fool', 'the heirophant', 'the sun', 'the moon',
            'the magician', 'the devil', 'the tall', 'the short', 'the nine toed', 'the dwarf', 'the elf',
            'the halfling', 'the half-orc', 'the ogre', 'piss-pants', 'the rider', 'the swift', 'the cagey',
            'strangler',
            'the weak', 'the strong', 'the pasty', 'of the night', 'of the north', 'of the south', 'of the east',
            'of the west', 'the outsider', 'the champion', 'of Fate',
            'of the swamp', 'of the forests', 'Mossbeard', 'Terror-fist', 'the Coward', 'the gentle',
            'the tender lover',
            'the baker', 'the alchemist', 'the merchant', 'the Invisible', 'Cowardsbane', 'Orcbane', 'Trollbane',
            'Dragonlover', 'Swiftfoot', 'Highjumper', 'Smith', 'the Cobbler', 'The Cooper', 'the stableboy', 'the bad',
            'The radish', 'the corpse', 'the Tasty', 'the cook', 'the Innkeeper', 'the wise', 'the powerhungry',
            'one-sock', 'of mud', 'the bastard', 'the wealthy', 'the ignoble', 'the wicked',
            'who got lost for five days',
            'the hungry', 'slippery fingers', 'pickpocket', 'King of Dirt', 'the Headsman', '"Sniff-my-fingers"',
            'the mad mage', 'the paladin', 'the bard', 'the warlock', 'the barbarian', 'the sorcerer', 'the painter',
            'the one-day lich', 'the scam artist', 'chicken legs', 'McCoy', 'the terrified', 'the petrified',
            'the boring']

races = ['human', 'elf', 'dwarf', 'half-elf', 'half-orc', 'gnome', 'half-giant', "goblin", "ghost",
         "minotaur", "lizardfolk", "talking animal", "unknown", "shapeshifter", "halfling", "tiefling",
         "human", "elf", "dwarf", "half-elf", "half-dwarf", "dragonborn", "satyr", "fairy", "genasi", "goliath",
         "human", "elf", "dwarf", "human", "half-elf", "kobold", "orc", "tabaxi", "tortle", "centaur"]

characteristics_physical = ['tall', 'short', 'blue eyes', 'green eyes', 'brown eyes', 'tanned skin', 'long black cloak',
                            'twitchy', 'one-handed', 'limping', 'smiling', 'missing teeth', 'eye-patch', 'kind eyes',
                            'knee high boots', 'wearing a sword', 'hunched over', 'hood pulled up', 'barefoot', 'blind',
                            'poor', 'rich', 'noble', 'beggar', 'merchant', 'worker', 'slave', 'commoner', 'farmer',
                            'big smile', 'wearing blue', 'wearing red', 'drinking tea', 'drinking beer', 'eating',
                            'pale', 'bleeding', 'diseased', 'in a loincloth', 'carrying tools', 'holding gold coins',
                            'has a talking crow', 'strong accent', 'dark skin', 'squinting at you', 'unblinking']

characteristic_personality = ['happy', 'sad', 'angry', 'nervous', 'joyous', 'quick temper', 'forgiving', 'friendly',
                              'alcoholic', 'pacifist', 'aggressive', 'scared', 'terrified', 'fearless', 'alert',
                              'active', 'agreeable', 'caring', 'confident', 'daring', 'curious', 'creative', 'decisive',
                              'brilliant', 'wise', 'fair', 'fun-loving', 'generous', 'heroic', 'hearty', 'honest',
                              'liar', 'healthy', 'unhealthy', 'humble', 'educated', 'dramatic', 'loyal', 'musical',
                              'neat', 'organized', 'passionate', 'patient', 'observant', 'playful', 'rational', 'sage',
                              'sane', 'selfless', 'self-critical', 'scholarly', 'prudent', 'protective', 'persuasive',
                              'patriotic', 'sensitive', 'sexy', 'teacherly', 'unfoolable', 'foolish', 'trusting',
                              'boring', 'plain', 'warm', 'well-rounded', 'sweet', 'subtle', 'stoic', 'sober',
                              'sociable',
                              'zealous', 'youthful', 'sweet', 'understanding', 'suave', 'spontaneous', 'tidy']

plot_verbs = ['deliver', 'retrieve', 'save', 'find', 'catch', 'destroy', 'steal/kidnap', 'hide', 'protect', 'betray',
              'bartender for', 'trade', 'teach', 'bribe', 'blackmail', 'spy on', 'sell [to]', 'adjudicate for',
              'create a fake of', 'gamble against', 'eating contest with', 'pass a secret message to', 'get information on',
              'protect', 'escort', 'track down', 'exploit', 'investigate']

plot_nouns = ['sister', 'father', 'child', 'pet', 'dinner', 'pants', 'heirloom', 'weapon', 'enemy', 'cursed artifact',
              'cart', 'melon', 'bear', 'tree', 'ghost', 'monster', 'grandmother', 'wizard', 'skeleton', 'monster',
              'bartender', 'mimic', 'trapped citizen', 'farmer', 'tinker', 'shipwreck', 'knight', 'wild animal',
              'local noble', 'goblin tribe', 'thief', 'beautiful woman', 'jester', 'sailor', 'merchant',
              'environmental disaster', 'adventuring party', 'musician', 'pair of twins', 'sheet of music', 'wolf pack',
              'angry mob', 'family', 'cult', 'religious group', 'demon', 'beggar', 'town guard', 'werewolf', 'demi-lich',
              'bandits', 'union', 'meteor', 'handsome stranger']

plot_additions = ['before midnight', 'in the dark', 'in public', 'in disguise', 'from a jail', 'while under attack',
                  'tomorrow', 'with my help', 'without your weapons', 'underwater', 'with an alchemist\'s help',
                  'without magic', 'while being pursued', 'stealthily', 'lawfully', 'during a fancy ball',
                  'during a festival', 'in another town', 'on the roof of the castle', 'in a dungeon', 'in a storm',
                  'during thick fog', 'to prevent a disease outbreak', 'as fast as possible', 'in a graveyard',
                  'to stop the nightmares', 'with a curse of silence', 'to receive a magic item', 'before next dawn',
                  'against the wishes of the thieves guild', 'on behalf of a dragon', 'to earn my trust',
                  'to prevent my public shame', 'twice', 'to fulfill a prophecy', 'while poisoned', '50 miles away',
                  'with expenses paid for', 'in a cave', 'on a mountain', 'in a barn', 'in a tavern', 'in an alley',
                  'before guards arrive']


class Character:
    def __init__(self, syllable_count=2, prefix=None, name=None, suffix=None, race=None, traits=None, plot_hook=None):
        self.name = make_name(syllable_count)
        self.prefix = random.choice(prefixes)
        self.suffix = random.choice(suffixes)
        self.race = random.choice(races)
        self.traits = random.sample(characteristics_physical, 2)
        self.personality = random.choice(characteristic_personality)
        self.plot_hook = generate_plot_hook()

    def character_output(self):
        print("%-20s %-20s %-30s %-15s %-20s %-20s %-20s %-50s" % (
            self.prefix.title(), self.name.title(), self.suffix.title(), self.race.title(), self.traits[0].title(),
            self.traits[1].title(), self.personality.title(), self.plot_hook.title()))


def generate_plot_hook():
    plot_hook = random.choice(plot_verbs)
    plot_noun = random.choice(plot_nouns)
    plot_addition = random.choice(plot_additions)
    if plot_noun[0] in ('a', 'e', 'i', 'o', 'u', 'y'):
        plot_hook += " an " + plot_noun + " " + plot_addition
    else:
        plot_hook += " a " + plot_noun + " " + plot_addition
    return plot_hook


def make_name(syllable_count):
    name = ""
    for i in range(syllable_count):
        name += random.choice(syllables)
    return name


def user_interface():
    while True:  # loop forever until user exits
        try:
            # Syllables per name
            print('How many syllables would you like? :')
            syllable_count = int(input())

            # How many characters to create
            print('How many characters would you like? :')
            character_count = int(input())

            # Column Headers
            print(
                "\n\n%-20s %-20s %-30s %-15s %-20s %-20s %-20s %-50s" % ("Prefix", "Name", "Suffix", "Race", "Trait 1",
                                                                         "Trait 2", "Personality", "Plot Hook"))
            print("-" * 195)
            # Creating the parameterized characters
            for i in range(character_count):
                c = Character(syllable_count)
                c.character_output()

        except ValueError as e:
            print('Uh oh! Try entering only positive integers when prompted for a number.')

        print('\nWould you like to continue? (Enter "Y" or "1" to continue) :')
        repeat = input()
        if repeat not in ('Y', 'y', 'yes', 'YES', 'Yes', '1'):
            break


user_interface()
