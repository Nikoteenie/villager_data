"""Functions to parse a file containing villager data."""

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    filename = open(filename)
    species = set()

    # TODO: replace this with your code
    
    for line in filename:
        words = line.split("|")
        species.add(words[1])
    print(species)
    return species

all_species("villagers.csv")

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    filename = open(filename)
    villagers = []
    species = []

    # TODO: replace this with your code
    for name in filename:
        words = name.split("|")
        villagers.append([words[0], words[1]])
     
          
    print(villagers)
    return sorted(villagers)
get_villagers_by_species("villagers.csv")

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    fitness= []
    nature = []
    play = []
    fashion = []
    education = []
    music = []
    # TODO: replace this with your code
    filename = open(filename)
    for hobby in filename:
        words = hobby.split("|")
       
        if words[3] == "Fitness":
            
            fitness.append(words[0])

        elif words[3] == "Nature":

            nature.append(words[0])

        elif words[3] == "Play":
            play.append(words[0])
        
        elif words[3] == "Fashion":
            fashion.append(words[0])

        elif words[3] == "Education":
            education.append(words[0])

        elif words[3] == "Music":
            music.append(words[0])

    

    print([fitness, nature, play, fashion, education, music])
   
    return [fitness, nature, play, fashion, education, music]
all_names_by_hobby("villagers.csv")

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    # lines = ()
    # TODO: replace this with your code
    filename = open(filename)

    for line in filename:
        words = line.rstrip().split("|")
        lines = tuple(words)
        all_data.append(lines)
        
    print(all_data)
    return all_data
all_data("villagers.csv")
def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
   
    # TODO: replace this with your code
    filename = open(filename)
    for line in filename:
        words = line.strip().split("|")
        if(words[0] == villager_name):
            return words[4]        
    print(find_motto("villagers.csv"))
    return None
    
find_motto("villagers.csv", "Pudge")

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file   
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    names = set([])
    # TODO: replace this with your code
    filename = open(filename)
    for line in filename:
        words = line.strip().split("|")
      
        if(words[0] == villager_name):
            personality = words[2]
            while(personality):
                names.add(words[0])
    print(names)
    return names
find_likeminded_villagers("villagers.csv","Knox")