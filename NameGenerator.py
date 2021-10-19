import random

# General lists to follow of syllables, prefixes, suffixes, races, characteristics, and plot hooks to pull from. Can be expanded
# or items removed as preferred.

# Syllables that names are constructed from
syllables = ['Arc', 'Bar', 'Can', 'Caz', 'Cha', 'Ale', 'Bor', 'Ben', 'Dar', 'Dag', 'Del', 'Dyn', 'Een', 'Est', 'Fan',
             'Fay', 'Fly', 'Ga', 'Gre', 'Gri', 'Sha', 'Kha', 'Vor', 'Var', 'Kaz', 'Par', 'Zen', 'Zish', 'Kol', 'Phy',
             'Pin', 'Pal', 'Tar', 'Get', 'For', 'Spa', 'Shi', 'Sho', 'Ken', 'Tay', '\'Ik', '\'Cha', 'Zar', 'Ry', 'As',
             'co', 'sa', 'an', 'le', 'ta', 'sa', 'se', 'sey', 'lie', 'las', 'or', 'chi', 'kay', 'er', 'tey', 'no', 'na',
             'ram', 'ro', 'sh', 'ich', 'yi', 'quo', 'wri', 'wro', 'ooo', 'ash', 'kie', 'ie', 'po', 'win', 'ter', 'sky',
             'ha', 'mi', 'che', 'elle', 'hea', 'thea', '\'Xor', 'by', 'big', 'sal', 'uh', 'ju', 'wer', 'wren', 'lyn',
             'a', 'tor', 'bjorn', 'mald', 'vald', 'tyn', 'er', 're', 'col', 'cur', 'cho', 'try', 'raja', 'weed', 'que',
             'fios', 'stal', 'gro', 'op', '\'Za', 'puri', 'yus', 'Wel', 'Wes', 'bile', 'ste', 'ven', 'ash', 'Bre',
             'net', 'Ian', 'Jen', 'Kev', 'in', 'Rach', 'Sara', 'Kel', 'Pow', 'acha', 'sas', 'ex', 'al', 'bi', 'lo', 'li',
             'ti', 'to', 'ri', 'aes', 'de', 'di', 'ley', 'ren', 'tare', 'lee', 'hai', 'beau', 'chad', 'cain', 'rose',
             'dean', 'jack', 'daw', 'jude', 'mar', 'rex', 'ajax', 'pa', 'par', 'pan', 'anne', 'blue', 'eve', 'hope',
             'live', 'fern', 'Rae']

# An increased chance for surnames to start with one of these syllables
surname_prefixes = ['De', 'Von ', 'Vos', 'Der', 'Del', 'Abu', 'Du ', 'Fitz', 'A', 'Le ', 'La', 'Ost', 'Ter', 'Van',
                    'Mala', 'zu', 'war', 'vest', 'Oz', 'Opp', 'Stor', 'Bet', 'Bar', 'Aust', 'Al', 'Ap', 'Ab', 'Vas']

# Name prefixes and titles
prefixes = ['Doctor', 'Sergent', 'Captain', 'Lieutenant', 'Elder', 'professor', 'Earl', 'Duke', 'Sir', 'Squire',
            'Blacksmith', 'Seven fingers', 'One-eye', 'Poor', 'Tyrannical', 'Scribe', 'Bear fucker', 'Elder', 'Sultan',
            'Lady', 'Lord', 'Your Grace', 'His Excellency', 'Goodman', 'Goodwife', 'Midwife', 'Bishop', 'Cardinal',
            'Father', 'Pastor', 'Master', 'Chairman', 'Mage', 'Wizard', 'Fellow', 'Minister', 'Constable', 'Herald',
            'Secretary', 'Madam', 'Monsignor', 'Despot', 'Centurion', 'Dame', 'Councillor', 'Nephew', 'Saint', 'Nasty',
            'Foul-mouthed', 'Kind', 'Ol\'', 'Old', 'Young', 'Little', 'Big', 'Shy', 'Timid', 'Senor', 'Complainin\'',
            'Toasty', 'Badger-catcher', 'Tiny-hands', 'Immortal', 'Guardian', 'monk', 'druid', 'Thief',
            'Lord of Outlaws', 'King of Thieves', 'Sourfaced', 'Angry', 'Sleepy']

# Name suffixes and titles
suffixes = ['the strange', 'the lost', 'the shepherd', 'the blessed', 'the holy', 'the ungodly', 'the golden',
            'the corrupt', 'the dirty', 'the vile', 'the kind', 'the courageous', 'the righteous', 'the sane',
            'the insane', 'the fury', 'the pale', 'the victorious', 'the farmer', 'the clean', 'Senior', 'junior',
            'of the golden shoes', 'the beauty', 'the consort', 'the handsome', 'the cagey', 'the swift', 'piss-pants',
            'the sweet', 'of the travellers', 'the wanderer', 'the fool', 'the heirophant', 'the sun', 'the moon',
            'the magician', 'the devil', 'the tall', 'the short', 'the nine toed', 'strangler', 'the rider', 'the ogre',
            'the weak', 'the strong', 'the pasty', 'of the night', 'of the north', 'of the south', 'of the east',
            'of the west', 'the outsider', 'the champion', 'of Fate', 'the tender lover', 'who got lost for five days',
            'of the swamp', 'of the forests', 'Mossbeard', 'Terror-fist', 'the Coward', 'the gentle', 'the boring'
            'the baker', 'the alchemist', 'the merchant', 'the Invisible', 'Cowardsbane', 'Orcbane', 'Trollbane',
            'Dragonlover', 'Swiftfoot', 'Highjumper', 'Smith', 'the Cobbler', 'The Cooper', 'the stableboy', 'the bad',
            'The radish', 'the corpse', 'the Tasty', 'the cook', 'the Innkeeper', 'the wise', 'the powerhungry',
            'one-sock', 'of mud', 'the bastard', 'the wealthy', 'the ignoble', 'the wicked', 'the petrified',
            'the hungry', 'slippery fingers', 'pickpocket', 'King of Dirt', 'the Headsman', '"Sniff-my-fingers"',
            'the mad mage', 'the paladin', 'the bard', 'the warlock', 'the barbarian', 'the sorcerer', 'the painter',
            'the one-day lich', 'the scam artist', 'chicken legs', 'McCoy', 'the terrified']

# Races, with an increased chance of human, elf, and dwarf. To generate only humans, simply remove all other items.
races = ['human', 'elf', "dwarf", "human", "elf", 'dwarf', 'half-elf', 'half-orc', 'gnome', 'half-giant', "goblin",
         "minotaur", "lizardfolk", "talking animal", "unknown", "shapeshifter", "halfling", "tiefling", "ghost",
         "half-elf", "half-dwarf", "dragonborn", "satyr", "fairy", "genasi", "goliath", "tortle", "centaur",
         "kobold", "orc", "tabaxi"]

# Physical characteristics that would be noticed on first glance or interaction
characteristics_physical = ['tall', 'short', 'blue eyes', 'green eyes', 'brown eyes', 'tanned skin', 'long black cloak',
                            'twitchy', 'one-handed', 'limping', 'smiling', 'missing teeth', 'eye-patch', 'kind eyes',
                            'knee high boots', 'wearing a sword', 'hunched over', 'hood pulled up', 'barefoot', 'blind',
                            'poor', 'rich', 'noble', 'beggar', 'merchant', 'worker', 'slave', 'commoner', 'farmer',
                            'big smile', 'wearing blue', 'wearing red', 'drinking tea', 'drinking beer', 'eating',
                            'pale', 'bleeding', 'diseased', 'in a loincloth', 'carrying tools', 'holding gold coins',
                            'has a talking crow', 'strong accent', 'dark skin', 'squinting at you', 'unblinking']

# Personality traits that would learn upon further interaction with the character
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

# Verbs used to generate plot hooks
plot_verbs = ['deliver', 'retrieve', 'save', 'find', 'catch', 'destroy', 'steal/kidnap', 'hide', 'protect', 'betray',
              'bartender for', 'trade', 'teach', 'bribe', 'blackmail', 'spy on', 'sell [to]', 'adjudicate for',
              'create a fake of', 'gamble against', 'eating contest with', 'pass a secret message to',
              'get information on', 'protect', 'escort', 'track down', 'exploit', 'investigate']

# Nouns used to generate plot hooks
plot_nouns = ['sister', 'father', 'child', 'pet', 'dinner', 'pair of pants', 'heirloom', 'weapon', 'enemy', 'jester',
              'cart', 'melon', 'bear', 'tree', 'ghost', 'monster', 'grandmother', 'wizard', 'skeleton', 'monster',
              'bartender', 'mimic', 'trapped citizen', 'farmer', 'tinker', 'shipwreck', 'knight', 'wild animal',
              'local noble', 'goblin tribe', 'thief', 'beautiful woman', 'cursed artifact', 'sailor', 'merchant',
              'environmental disaster', 'adventuring party', 'musician', 'pair of twins', 'sheet of music', 'wolf pack',
              'angry mob', 'family', 'cult', 'religious group', 'demon', 'beggar', 'town guard', 'werewolf',
              'demi-lich', 'group of bandits', 'meteor', 'handsome stranger']

# Additional clauses that can add intrigue, challenge, or flavour to generated plot hooks
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
    """
    Character class that holds information about a specific generated character.
    """
    def __init__(self, syllable_count_first=2, syllable_count_last=3, prefix=None, name=None, suffix=None, race=None,
                 traits=None, personality=None, plot_hook=None):
        """
        init method that calls for creation of the specific details.
        :param syllable_count_first: how many syllables go into the first name
        :param syllable_count_last: how many syllables go into the last name
        :param prefix: a prefix for the name
        :param name: a first and last name, with specified syllable counts in each
        :param suffix: a suffix for the name
        :param race: a randomly chosen race
        :param traits: two physical traits
        :param personality: a personality trait
        :param plot_hook: a potential plot line with a verb, noun, and additional clause formatted into a sentence
        """
        self.name = make_name(syllable_count_first, syllable_count_last)
        self.prefix = random.choice(prefixes)
        self.suffix = random.choice(suffixes)
        self.race = random.choice(races)
        self.traits = random.sample(characteristics_physical, 2)
        self.personality = random.choice(characteristic_personality)
        self.plot_hook = generate_plot_hook()

    def character_output(self):
        """
        Outputs a formatted string containing all important character details
        :return: A formatted string
        """
        print("%-20s %-25s %-30s %-15s %-20s %-20s %-20s %-50s" % (
            self.prefix.title(), self.name.title(), self.suffix.title(), self.race.title(), self.traits[0].title(),
            self.traits[1].title(), self.personality.title(), self.plot_hook.title()))


def generate_plot_hook():
    """
    Creates a plot hook using a verb, noun, and additional clause.
    Generates simple sentences with the structure "[verb] a[n] [noun] [additional clause]
    :return: a string containing the plot hook
    """
    plot_hook = random.choice(plot_verbs)
    plot_noun = random.choice(plot_nouns)
    plot_addition = random.choice(plot_additions)
    if plot_noun[0] in ('a', 'e', 'i', 'o', 'u', 'y'):
        plot_hook += " an " + plot_noun + " " + plot_addition
    else:
        plot_hook += " a " + plot_noun + " " + plot_addition
    return plot_hook


def make_name(syllable_count_first=3, syllable_count_last=3):
    """
    Creates a first and last name using random syllables.
    Syllable counts can be specified when calling the method. Defaults to 2 and 3 respectively.
    Increased chance of starting the last name with a surname prefix, for more natural sounding names
    :param syllable_count_first:
    :param syllable_count_last:
    :return: A string containing the name.
    """
    name = ""
    name += ''.join(random.sample(syllables, syllable_count_first))
    name += " "
    if random.randint(0, 4) == 0:
        name += random.choice(surname_prefixes)
        syllable_count_last -= 1
    name += ''.join(random.sample(syllables, syllable_count_last))
    return name


def user_interface():
    """
    A user interface loop that takes some basic inputs for character generation,
    and then calls for creation and printing of those characters in a formatted table.
    """
    while True:  # loop forever until user exits
        syllable_count_first = 2
        syllable_count_last = 3
        character_count = 10
        try:
            # Syllables per name
            print('How many syllables would you like in the first name? (Default 2):')
            i = input()
            if int(i) >= 1:
                syllable_count_first = int(i)

            print('How many syllables would you like in the last name? (Default 3):')
            i = input()
            if int(i) >= 0:
                syllable_count_last = int(i)

            # How many characters to create
            print('How many characters would you like? (Default 10):')
            i = input()
            if int(i) >= 1:
                character_count = int(i)

            # generating and printing the characters
            create_characters(character_count, syllable_count_first, syllable_count_last)

        except ValueError as e:
            print('No custom input. Defaults used.')
            create_characters(character_count, syllable_count_first, syllable_count_last)

        print('\nWould you like to continue? (Enter "Y" or "1" to continue) :')
        repeat = input()
        if repeat not in ('Y', 'y', 'yes', 'YES', 'Yes', '1'):
            break


def create_characters(character_count, syllable_count_first, syllable_count_last):
    """
    Creates a table of generated characters, based on a set of parameters.
    Formats with spacing, column headers, and separators every 10 rows.
    :param character_count: how many characters to generate
    :param syllable_count_first: how many syllables the first names should be
    :param syllable_count_last:  how many syllables the last names should be
    """
    # Column Headers
    print(
        "\n\n%-20s %-25s %-30s %-15s %-20s %-20s %-20s %-50s" % ("Prefix", "Name", "Suffix", "Race", "Trait 1",
                                                                 "Trait 2", "Personality", "Plot Hook"))
    # Creating the parameterized characters
    for idx in range(character_count):
        if idx % 10 == 0:
            print("-" * 200)
        c = Character(syllable_count_first, syllable_count_last)
        c.character_output()



user_interface()
