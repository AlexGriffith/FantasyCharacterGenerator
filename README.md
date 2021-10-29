# NPC_Generator

An ultralight character generator for NPC's, with names, nicknames, races, traits, and plot hooks
Just enter how many syllables you'd like names to be, and how many characters to generate, it does the rest. 
  [2-3 syllables are recommended for most names, but don't let me tell you how to run your games]

The code starts with a set of lists that are drawn from to generate everything,
you can simply make changes to those lists to alter the end results. 

syllables                   - the syllables that generate names, add to or remove from this to alter the sounds in the names for more/less common/foreign names

prefixes                    - a list of titles or descriptors that appear before the name

suffixes                    - a list of titles or nicknames that appear after the name

races                       - for games like Dungeons & Dragons, this will generate character races, weighted slightly towards human/elf/dwarf. 
                                Feel free to change or simply ignore it if it doesn't apply to your needs.

characteristics_physical    - physical characteristics or things that may be noticed upon first glance. 

characteristic_personality  - a personality trait of the character that may be noticed upon further interaction

plot_verbs                  - a list of verbs used to generate plot hooks

plot_nouns                  - a list of nouns used to generate plot hooks

plot_additions              - a list of further additions to add challenge, intrigue, or a potential reward to a plot hook
