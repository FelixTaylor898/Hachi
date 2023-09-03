import sys #for terminating the program
import random #for generating random numbers

"""
Introduction:
This program generates the profile of a user based on their input, and some random elements.
The results are portrayed as though the user is a vampire in a fictional story I have written.

@author Felix Taylor
@version 11.28.18
Programmed in 3.5.2
"""



"""               PHASE 1 - Setting things up               """

#Initial Print - introduction for the user
print("Within the two isolated northern towns of Lunarville and Sunnytown, there exist 8 different types of what are known as Hachi vampires. This short quiz will help determine which type of Hachi you are, and which of the various flocks you belong to.")
print("")

#Declaring arrays of text for the profile
#The name of each type, preceded by a or an, for grammatical correctness
atypes = ["a Reger", "a Kota", "a Paran", "a Rashi", "a Calana", "a Suyo", "a Forma", "an Avere"]
#The color eyes they have, depending on their type
eyestypes = ["a red-eyed Reger", "an orange-eyed Kota", "a yellow-eyed Paran", "a green-eyed Rashi", "a blue-eyed Calana", "a purple-eyed Suyo", "a pink-eyed Forma", "a white-eyed Avere"]
#A description of their gift/power
gifts = ["that you have the power to control the minds of humans",
         "that you can teleport anywhere in the world",
         "that you can turn yourself and others invisible",
         "that you have the power to read minds, and communicate with others telepathically",
         "that you are able to move objects with your mind",
         "that you can absorb and distribute energy to and from living things",
         "that you can shape-shift into any animal",
         "that you can turn your body into a spirit form, and use it to possess humans"]
#A description of their curse
curses = ["that no humans will trust you ever again",
          "that you have to be invited in before entering certain places, or risk death",
          "that you have no reflection, and no longer show up in pictures or on video",
          "that you are deathly allergic to various spices and herbs, such as garlic",
          "that you have a highly compulsive personality now, having to continuously count things and obsessively keep everything tidy",
          "that your body is no longer alive, and it will begin to rot if you do not absorb energy",
          "that you now have a lethal sun allergy, that causes severe burns and possibly death if you are in a human form",
          "that you are repelled and possibly hurt by religious/spiritual objects or places, regardless of origin"]
#Additional information on the types
infotypes = ["\nThe power to control others may have slightly gone to your head, causing you to think very highly of yourself. If you're not looking down on humans for being weak, you're unhappy that no humans trust you anymore, and how they all give you weird looks even when you're doing nothing. The only way for you to get used to that is by seeing them as lesser, because you're the one with the mind-control powers, and they're just there for you to use.",
             "\nYour teleportation powers have caused you to develop an unquenchable wanderlust: you always seek to go new places and experience new adventures. You're never content with staying in one place for too long: you always have to teleport to far-away places to sight-see and explore. However, you're still very much attached to your home and your flock, so you always come back after a trip.",
             "\nAs with most Parans, you've become a fairly shy person since Turning. You don't particularly enjoy being in the spotlight at all, and you'd prefer if people didn't notice you. Your power lets you go unseen whenever you want, which is fortunate for you, but you find it unfortunate that you can't show up in mirrors or film anymore. Sometimes you turn invisible so people won't notice you, while other times you do it so people won't notice how you don't show up anywhere. You know that the only reason you're so shy now is because you're a Paran, but that's something that all Parans must learn to accept.",
             "\nThe ability to search through the minds of others has given you a deep fascination for learning about people and their lives, along with seeking new information from all different points of view. Your curiosity for knowledge can only be sated by direct information from a person's mind. Books and lessons hardly seem to cut it for you now, but you still enjoy them anyway, as you will forever love to learn. Sometimes, though, you feel guilt over your power. Is it right for someone to listen to another person's thoughts without permission? To find their darkest secrets on a whim, without them even knowing? You figure that since you became a Rashi, it must be fine for you to do it, though sometimes you are unsure. Your allergy to certain things never seems to affects you, since vampires don't eat food anyway. You know that Rashi is the type with the least severe curse by far, and you're glad that's the one you became.",
             "\nIt's not the easiest thing in the world to be a Calana. Your highly compulsive nature makes you lose control and have to spend countless hours obsessing over keepings things cleaned and organized. If you're not doing that, you're having to count things around you. It takes so much of your time and attention that sometimes entire days can go by without you even knowing. Calanas have to learn the best ways to cope with their compulsive natures, finding ways to keep relaxed so that they can stay in control. Telekinesis is definitely a very nice power to have: you can move heavy objects freely with your mind alone. It definitely comes in handy for easily re-ordering books on shelves, or making your bed, or anything else you want to to easily and quickly.",
             "\nSuyos are perhaps the least human of the eight types, since their bodies are dead. Their hearts don't beat, and they don't breathe. Their skin is cold to the touch, and none of their organs function anymore. As a Suyo, you are deeply connected to nature, and love to be outside, feeling the air on your cold skin, hearing the sounds around you, and feeling the energy from all the living things pulsing through the atmosphere. Energy from plants can be good enough to keep your body from rotting sometimes, but other times you have to absorb energy from animals or humans to keep yourself going. You are always careful to not take too much from any living thing, as you do not wish to cause death, since you very much know what it's like to be dead.",
             "\nAs a Forma, you've developed a need for people to give you attention and adoration. You want to be popular and well-liked, and you get frustrated if you go too long without being paid attention to by others. Looks are very much important to you. The ability to shape-shift means you can make your body and face look however you want, so you strive to look as good as possible. Besides that, you can shape-shift into animals as well. Turning into a bird and flying through the sky is the greatest feeling in the world to you. Each animal you become brings you a different, amazing experience. You've developed a deep connection to animals, and can communicate with them now. Being in an animal form is the only way you can travel in day time without getting burned or killed, otherwise you're constricted to the night.",
             "\nAveres are very mysterious, quiet vampires. They spend a lot of time by themselves, finding it much more fulfilling to be alone with their own thoughts, than be surrounded by others who can't really understand them. Their need to be alone is an almost spiritual thing, and they find it difficult to describe to others why they are this way. Averes don't even spend much time with each other, but all in all they are still loyal members to their flock. Their spirit form can move through solid matter, and can't be seen by human eyes, but isn't very good for seeing or hearing, and it can't interact with physical objects, so it isn't very practical. Some Averes find it difficult to accept their power of possession, thinking it's immoral to take a physical body from somebody else. Usually humans won't remember the Avere taking control if it's for a short enough amount of time, so you see it as justifiable in that way. You only use your possession power if you have to, as do most other Averes."]

#Random first names for the generated leader
#Courtesy of http://random-name-generator.info/
firstnames = ["Patrick","Ronald","Mark","Jeffrey","Kenneth","Randy","Lawrence","Terry","Howard","Robert","Ernest","Gregory","Bobby","Joseph","Joshua","Edward","Roger","Roy","Shawn","Jesse","Mike","Eric","Carl","Keith","George","Billy","Jonathan","Wayne","Gerald","Jimmy","Arthur","Christopher","Henry","Sean","Albert","Philip","Harold","Jerry","Eugene","Kevin","Dennis","Justin","James","Taylor""Jose","Joe","Earl","Larry","Donald","Peter","Scott","Matthew","Steven","Anthony","John","Victor","David","Samuel","Douglas","Brian","Jason","Raymond","Steve","Timothy","Ralph","Carlos","Willie","Juan","Brandon","Nicholas","Frank","Fred","Aaron","Adam","Daniel","Alfonzo","Russell","Gary","Harry","Clarence","Chris","Walter","Ryan","William",	"Jack","Paul","Bruce","Andy","Richard",
"Benjamin","Jeremy","Craig","Louis","Martin","Stephen","Charles","Thomas","Phillip","Johnny","Blair","Phyllis","Kathleen","Michelle","Mary","Dorothy","Marie","Joyce","Diane","Mildred","Amber","Sharon","Anna","Diana","Rose","Amy","Ruth","Cynthia","Rebecca","Patricia","Jacqueline","Alice","Bonnie","Christine","Beverly","Jennifer","Samantha","Nicole","Lisa","Lois","Nancy","Sara","Carolyn","Betty","Katherine","Christina","Susan","Tammy","Denise","Wanda","Maria","Paula","Judy","Kathryn","Stephanie","Virginia","Carol","Debra","Louise","Kathy","Joan","Theresa","Pamela","Bonnie","Elizabeth","Janet","Shirley","Terri","Margaret","Julie","Melissa","Karen","Kelly","Cheryl","Lillian","Linda","Norma","Evelyn","Ashley","Heather","Marilyn","Julia","Jean","Deborah","Frances","Helen",
"Emily","Tina","Donna","Kelsey","Angela","Brenda","Sandra","Irene","Judith","Martha","Laura","Jane","Rachel","Lori","Ruby","Gloria","Kit","Andrea","Barbara","Kimberly","Doris","Jessica","Janice","Amanda","Darla"]

#Random last names for the generated leader
#Courtesy of https://www.randomlists.com/
lastnames = ["Mora","Flower","Larson","Conrad","Benjie","Holloway","May","Dennis","Buchanan","Pineda","Richards","Gray","Morris","Flynn","Eaton","Werner","Howell","Waller","Alvarado","Summers","Dodson","Hooper","Moses","White","Jordan","Lozano","Barrera","Woodard","Chapman","Byrd","Boone","Owen","King","Terry","Fry","Hull","Price","McCullough","Dillon","Buck","Bray","Massey","Short","Charles","Donovan","Lynn","Payne","Pacheco","Nixon","Crosby","Keith","Sheppard","Hubbard","McCoy","Zimmerman","Potter","Bartlett","Rosario","Mack","Hicks","Boyle","Travis","Woods","Ruiz","Mays","Taylor","Park","Benson","Jacobson","Carey","Douglas","Aguilar","Arroyo","Glover","Stanton","Bentley","Gilmore","Mendez","Myers","McGee","Acosta","McCall","Grimes","Deleon","Hogan","Serrano","Crawford","Cohen","Moran","Duffy","McIntosh","Silva","Cho","Dickson","Alvarez","Monroe","Gaines","Ming","Hoffman","Shepard","Warren","Cross","Reid","Mercado","Arnold","Harris",
"Shields","Prince","Gonzales","Davis","Kramer","Gibbs","Wilkinson","Blankenship","Riley","Alexander","Chen","Sharp","Little","Wade","Carson","Barron","Simon","French","Huerta","Weeks","Huynh","Lam","McMillan","Holder","McCann","Hendricks","Solomon","Hall","Esparza","Avila","Duncan","Wyatt","Paul","Petty","Houston","Hayden","Bryan","Jensen","Avery","Murphy","Rojas","McClain","Carr","Compton","Snyder","Roach","Shannon","Blackburn","Carroll","Harding","Carpenter","Patterson","Phelps","Han","Logan","Pugh","Walker","Stafford","Lambert","Navarro","Schultz","Joseph",
"Lee","Shepherd","Liu","Ryan","Blair","Curry","Kaiser","Frazier","Rivera","Stokes","Hurley","Ramsey","Cunningham","Cline","Williams","Villarreal","Farmer","Pennington","Graham","Hobbs","Robles","Atkins","Landry","Bush","Reeves","Hudson","Marks","Valencia","Howe","Valdez","Patton","Lara"]

#Array of integers that will determine which "type" the user is.
#The index of the highest score will be used as the index when other arrays are called.
scores = [0,0,0,0,0,0,0,0]

#End of Phase 1




"""             PHASE 2 - First batch of questions for the user           """

#Taking the year. Can be any year after 1960.
yearint = False
while yearint == False:
    current = input("Enter the current year: ")
    if current.isdigit():
        current = int(current)
        if current < 1961: #Hachi vampires weren't around in Lunarville and Sunnytown before this year
            print ("That's too early of a year.")
        else:
            yearint = True
    else:
        print("Please enter an integer.")

#Taking their age.
agebool = False
while agebool == False:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        if age > 50:
            print("Unfortunately (or fortunately, depending on how you look at it), because you are over the age of 50, it is physically impossible for you to become a Hachi vampire. The venom of Hachi vampires has no effect on people who aren't within the age range of 13-50. Sorry, but you're stuck as a human.")
            sys.exit() #Program terminates, as they are old young to be a vampire.
        elif age < 13:
            print("You are too young to be a Hachi vampire. Only people aged 13 or older are able to Turn. Sorry, give it a while longer and perhaps you'll Turn.")
            sys.exit() #Program terminates, as they are too young to be a vampire.
        else:
            agebool = True
    else:
        print("Please enter an integer.")

#Simple strings for the profile
name = input("Enter your name: ")
friendname = input("Enter the name of a friend: ")

#Determining which town they belong to out of the two options, Lunarville or Sunnytown
nord = False
while nord == False:
    daynight = input("Are you a night-person, or a day-person? Enter n or d. ")
    if daynight == "n":
        towntype = 0 #this variable is for reference in the creation of the profile
        nord = True
    elif daynight == "d":
        towntype = 1
        nord = True
    else:
        print("Please enter a suitable response.")

#End of Phase 2



"""             PHASE 3 - Quiz for the user with 12 questions             """

#Function for converting the user's answer to an integer for use as an array index
def question():
    typeinput = False
    while typeinput == False:
        userinput = input("Your response: ")
        if (userinput.isdigit()):
            userinput = int(userinput)
            if userinput < 0 or userinput > 7:
                print("Please choose an integer 0-7") #Arrays will only be 8 values long
            else:
                return userinput
        else:
            print("Please enter an integer")

#The personality quiz. Some questions are worth more than others because they have been subjectively determined to be better indicators of type.
#Each answer corresponds to one type, and is written to have to do with some typical trait of the type.
#For example, Regers (index 0) are typically power-hungry, and Formas (index 6) are typically fame-seeking.
print("\nThe following quiz will determine which type you are.")
print("01. What do you value?\na. Power (enter 0)\nb. Freedom (enter 1)\nc. Stealth (enter 2)\nd. Intelligence (enter 3)\ne. Order (enter 4)\nf. Peacfulness (enter 5)\ng. Popularity (enter 6)\nh. Thoughtfulness (enter 7)")
temp = question()
scores[temp] = scores[temp] + 1
print("\n02. Where would you like to go?\na. Anywhere but here (enter 0)\nb. Anywhere in the world! (enter 1)\nc. Anywhere I can go unnoticed (enter 2)\nd. Somewhere with interesting people (enter 3)\ne. Somewhere clean and tidy (enter 4)\nf. Anywhere outside in nature (enter 5)\ng. Anywhere as long as it’s night time (enter 6)\nh. Anywhere as long as I’m alone (enter 7)")
temp = question()
scores[temp] = scores[temp] + 1
print("\n03. Where would you NOT like to go?\na. A human gathering (enter 0)\nb. Someone else's house (enter 1)\nc. Somewhere full of cameras (enter 2)\nd. An Italian restaurant (enter 3)\ne. A marble factory (enter 4)\nf. A dead forest (enter 5)\ng. A beach (enter 6)\nh. A church (enter 7)")
temp = question()
scores[temp] = scores[temp] + 1
print("\n04. What do you like?\na. Having control over others (enter 0)\nb. Being able to go places (enter 1)\nc. Blending in (enter 2)\nd. Learning new things (enter 3)\ne. Mathematics (enter 4)\nf. Nature (enter 5)\ng. Animals! (enter 6)\nh. The quiet (enter 7)")
temp = question()
scores[temp] = scores[temp] + 1
print("\n05. What do you dislike?\na. Humans (enter 0)\nb. Restrictions (enter 1)\nc. Being stared at (enter 2)\nd. Stupid people (enter 3)\ne. Unorganized things (enter 4)\nf. Being inside (enter 5)\ng. Being ignored (enter 6)\nh. Crowds (enter 7)")
temp = question()
scores[temp] = scores[temp] + 1
print(" \n06. You would describe yourself as a(n)...\na. Strong person (enter 0)\nb. Free spirit (enter 1)\nc. Shy person (enter 2)\nd. Smart person (enter 3)\ne. Compulsive person (enter 4)\nf. Very zen person (enter 5)\ng. Animal-lover (enter 6)\nh. Reserved person (enter 7)")
temp = question()
scores[temp] = scores[temp] + 1
print("\n07. You like to…\na. Show off your abilities (enter 0)\nb. Sight-see (enter 1)\nc. Hide from others (enter 2)\nd. Absorb information (enter 3)\ne. Keep track of numbers (enter 4)\nf. Relax in nature (enter 5)\ng. Get attention from others (enter 6)\nh. Think while alone (enter 7)")
temp = question()
scores[temp] = scores[temp] + 1
print("\n08. You don't like to…\na. Feel ostracized (enter 0)\nb. Be stuck in one place (enter 1)\nc. Be talked to by strangers (enter 2)\nd. Be bored by people (enter 3)\ne. Lose control of yourself (enter 4)\nf. Kill anything (enter 5)\ng. Be in sunlight (enter 6)\nh. Be confronted by guilt (enter 7)")
temp = question()
scores[temp] = scores[temp] + 1
print("\n09. You are a(n)…\na. King/queen (enter 0)\nb. Adventurer (enter 1)\nc. Wallflower (enter 2)\nd. Nerd (enter 3)\ne. Neat-freak (enter 4)\nf. Tree-hugger (enter 5)\ng. Celebrity (enter 6)\nh. Loner (enter 7)")
temp = question()
scores[temp] = scores[temp] + 1
print("\n10. Your favorite horror character(s) is/are…\na. Vampires or witches (enter 0)\nb. Pinhead (Hellraiser) or Michael Myers (enter 1)\nc. The Invisible Man (enter 2)\nd. Freddy Krueger or Jigsaw (enter 3)\ne. Carrie (Stephen King) or Eleven (Stranger Things) (enter 4)\nf. Zombies or skeletons (enter 5)\ng. Werewolves or cat-people (enter 6)\nh. Ghosts, spirits, or demons (enter 7)")
temp = question()
scores[temp] = scores[temp] + 1
print("\n11. If you could have any power, it would be…\na. Mind-control (enter 0)\nb. Teleportation (enter 1)\nc. Invisibility (enter 2)\nd. Telepathy/mind-reading (enter 3)\ne. Telekinesis (enter 4)\nf. Energy control (enter 5)\ng. Shape-shifting (enter 6)\nh. Possession (enter 7)")
temp = question()
scores[temp] = scores[temp] + 1
print("\n12. What's your favorite color?\na. Red (enter 0)\nb. Orange (enter 1)\nc. Yellow (enter 2)\nd. Green (enter 3)\ne. Blue (enter 4)\nf. Purple (enter 5)\ng. Pink (enter 6)\nh. White (enter 7)")
temp = question()
scores[temp] = scores[temp] + 1

#Displays the quiz scores for the user's curiosity
print("\nHere are the results of the quiz")
print("Reger: " + str(scores[0]))
print("Kota: " + str(scores[1]))
print("Paran: " + str(scores[2]))
print("Rashi: " + str(scores[3]))
print("Calana: " + str(scores[4]))
print("Suyo: " + str(scores[5]))
print("Forma: " + str(scores[6]))
print("Avere: " + str(scores[7]))

#Separating the questions from the results
print("\n---------------------------------------------")

#End of Phase 3



"""               PHASE 4 - Setting up profile results               """

#Determines which type they belong to based on the highest score
value = scores[0]
types = 0 #Used as an index for the arrays
i = 1
while i < 8:
    if value < scores[i]:
        value = scores[i]
        types = i
    elif value == scores[i]: #If they are equal, randomly chooses which value to proceed with
        temp = random.randint(0,1)
        #50% chance of this proceeding
        if (temp == 0):
            value = scores[i]
            types = i
    i = i + 1

#Determines how long ago they became a vampire.
sample = random.randint(0,9)
if sample == 0: #An initial 10% change of them Turning recently
    tier = 3 #This determines the text that will print at the end of the profile
    number = "a few days ago" #Quantitative indicator of time
elif sample == 1: #An initial 10% change of them Turning weeks ago
    tier = 2
    number = str(random.randint(2,7)) + " weeks ago"
    yearturned = ""
elif sample < 4: #20% chance of them Turning months ago
    tier = 1
    number = str(random.randint(2,11)) + " months ago" #2 months is the minimum for them to no longer be a fledgeling vampire. 
else: #60% chance of it being one year or more since Turning
    tier = 0
    yearturned = random.randint(1961,current) #A random year generated between 1961 and the current year
    difference = current - yearturned #How many years since then
    number = str(difference) + " years ago, in " + str(yearturned) #Specifies the year they Turned
    if difference == 0: #If it hasn't been over a year, it converts it to months ago instead
        tier = 1
        number = str(random.randint(2,11)) + " months ago"
    if difference == 1:
        number = str(difference) + " year ago, in " + str(yearturned)

#Randomly generated information for the friend in the profile
friendturnedyear = random.randint(1961,current)
friendturned = current - friendturnedyear

#Array info on which flock they belong to, depending on their age and town
flockinfo = random.randint(0,4) #Randomly generated index.
#Names of flocks for teens in Lunarville
lunarteen = ["Redmoon", "Starlight", "Piano Star", "Umbra Eternal" , "Gemini"]
#Information for the flocks of the Lunarville teens
lunarteeninfo = ["the oldest and biggest teen flock in both of the two towns",
                     "a well-sized, unified flock", "a relatively peaceful, content flock",
                     "a flock made of many passionate, powerful vampires", "a flock for the more intellectual-type vampires"]
#Names for the adult flocks in Lunarville
lunaradult = ["Night Sky", "Moondust", "Evening Breeze", "Nocturna", "Afterglow"]
#Information for the flocks for adults in Lunarville
lunaradultinfo = ["the oldest and biggest adult flock in both of the two towns",
                      "a fairly musical, joyous flock", "a quiet, whimsical flock made up of thoughtful vampires",
                      "a flock made up of those who wish to protect all vampires in the two towns",
                      "a small, but thriving flock, full of wonderful people"]
#Names for the teen flocks in Sunnytown
sunnyteen = ["Lightfall", "Sunset Wind", "Sunshine", "Brightbeam", "Indigo Blue"]
#Information for the teen flocks in Sunnytown
sunnyteeninfo = ["the biggest teen flock in Sunnytown", "a flock made up of many creatively-minded people",
                     "a flock geared mostly towards younger teens, who grow to become experienced vampires",
                     "a very laid-back, easy-going flock", "a flock full of a lot of bubbly, outgoing people"]
#Names for the adult flocks in Sunnytown
sunnyadult = ["Solarflare", "Daybreak", "Rising Sun", "Morning Light", "Apollo Fire"]
#Information for the adult flocks in Sunnytown
sunnyadultinfo = ["the biggest adult flock in Sunnytown", "a flock that seems to have no trouble bending rules to have a good time",
                      "a flock for mostly older vampires to congregate, and take others under their wings",
                      "a flock where people strive to live as normal a life as possible",
                      "an invite-only flock, for those who prove themselves to be valiant, intelligent people"]

#Sets the information for the profile based on the random number and user inputs
if towntype == 0:
    yourtown = "Lunarville"
    if age < 20:
        yourstatus = "a teenager"
        yourflock = lunarteen[flockinfo]
        flockstatus = "a teenage-only"
        flockdesc = lunarteeninfo[flockinfo]
    else:
        yourstatus = "an adult"
        yourflock = lunaradult[flockinfo]
        flockstatus = "an adult-only"
        flockdesc = lunaradultinfo[flockinfo]
else:
    yourtown = "Sunnytown"
    if age < 20:
        yourstatus = "a teenager"
        flockstatus = "a teenage-only"
        yourflock = sunnyteen[flockinfo]
        flockdesc = sunnyteeninfo[flockinfo]
    else:
        yourstatus = "an adult"
        flockstatus = "an adult-only"
        yourflock = sunnyadult[flockinfo]
        flockdesc = sunnyadultinfo[flockinfo]

#Randomly generated type for your friend
friendtype = random.randint(0,7)
#Randomly generated type for the leader
leadertype = random.randint(0,7)

#End of Phase 4



"""               PHASE 5 - Printing the profile               """

#Name and age information
print("\nYour name is " + name + ". The year is " + str(current) + ". You Turned into " +
      eyestypes[types] + " vampire "
      + number + ". You were trapped as a " + str(age) + "-year-old when you Turned, and you'll remain that way forever.")
#Type information
print("\nAs " + atypes[types] + ", your Gift is " + gifts[types] + ". However, your Curse is " + curses[types] + ".")
print(infotypes[types])
#Location and flock information
print("\nYou live in " + yourtown + ", and because you are " + yourstatus +
          ", you belong to " + flockstatus + " flock. Yours is the " + yourflock + " Flock: " + flockdesc + ". The Leader of this flock is " + atypes[leadertype] + " vampire named " + firstnames[random.randint(0,199)] + " " + lastnames[random.randint(0,199)] + ".")
#Friend information
print("\nYour best friend in the " + yourflock + " Flock is named " + friendname + ". Your friend is " + atypes[friendtype] + " vampire, and has been for " + str(friendturned) + " years, after being Turned in " + str(friendturnedyear) + ".")

#Additional information based on how long user has been a vampire
if tier == 3:
    print("\nAs you were only recently Turned, you are very new to the world of Hachi vampires, and all that it entails. It might feel intimidating, but you'll learn to love it soon enough. You have a long road ahead of you. Don't feel ashamed to seek guidance from those more experienced than you.")
elif tier == 2:
    print("\nSince it's only been a few weeks since you Turned, you're still a fledgeling. You still have plenty of learning and growing to do, even after you become a full vampire. Don't worry: your flock is there to guide you, and help you on your long journey as a vampire.")
elif tier == 1:
    print("\nYou're no longer a fledgeling, but you know you're not fully accustomed to vampire life just yet. Everything is a learning process: growing used to your Curse, learning to use your powers, and overall adjusting to your life being different. With your flock by your side, however, you know you're not alone. They'll be there to help you, and some day you'll be capable of helping new vampires too.")
elif tier == 0:
    if difference < 6:
        print("\nWhile it feels like a long time since you've Turned, you're still not qualified for being considered an old vampire yet. While some of the younger vampires may look to you for guidance as they adjust to their own lives, you know you still have a long way to go. Eternity is a long time, after all.")
    elif difference < 10:
        print("\nYou're definitely at the age where you're more mature than a lot of the newer vampires in the flock. Passing the 5-year mark always seems like a huge milestone for a lot of people as vampires. It's at this point when they really seem to realize just how much the humans in their lives have changed, while they've stayed the same age since Turning, all those years ago. You know that despite your body being the same, your mind and heart have both grown greatly as time has gone on, and you look forward for them to continue to do so. What more can one hope for when they have an eternity's worth of life to live?")
    elif difference < 20:
        print("\nYour old life as a human seems like forever ago by now, but you've long since accepted it. You look back on those days with nostalgia, but know that your life as a vampire is very important to you. Your flock is like your family, and vampires are the only people who can understand you. As a result, you prefer to spend time with them, rather than humans. While you still take care of human friends and family, the thought that they'll grow old and die someday saddens you. You may be a powerful Hachi vampire, but you're still human at heart. You know that you need to learn to accept it: your life will go on without them, and it's just the way it is.")
    elif difference < 30:
        print("\nBy this point, all the humans in your life have grown up or gotten older, while you've been the same age since that fateful day when you were Turned, all those years ago. You've been a vampire for a decently long time now, so you're very well-respected in your flock. You surround yourself with them, knowing they're the only people you won't have to watch grow and age without you. They are your family, and while it's different from having a normal human family, you find it equally if not more special. You teach and aid the other vampires around you, all the while knowing that they'll have to watch people in their lives grow and die too, and they'll be left needing the flock to fill that hole just as much as you do.")
    elif difference < 50:
        print("\nYou're at an age where you no longer bother trying to keep up with humans, or at least not many of them. You just can't stand the pain of watching them grow while you stay the same, and you don't like to say goodbye when they die. You wonder how different your life might have been if you had never Turned, but you know that you prefer vampire life to human life. It's been a long time since you've been human, but you still have the rest of forever to get through, and you consider that a gift more than anything. You have so much more opportunity as a vampire with a limitless lifespan than you would have had as an aging, powerless human who would eventually die. You've been through a lot, and it's not going to stop. You embrace that.")
    elif difference > 49:
        print("\nYou are very much considered an old vampire. You've reached your maximum potential with all of your powers, as age and experience brings a greater amount of ability to any Hachi vampire, but it also brings a more powerful Curse. You've learned to deal with it of course, but it only makes you slightly reminiscent on your days as an unsuspecting human, so long ago. Back when you had plenty of humans in your life, who are likely by now all dead. No matter: you still have the flock that you've always had since you Turned, and while it's grown and changed over the years, it's somewhere where everyone supports and accepts each other. In that regard, vampires are perhaps more capable than humans, despite many humans viewing them as evil monsters. Of course vampires aren't evil: they're just people whose lives went in a different direction than most, and they work together to learn how to work through it. They're a family, and they're perhaps more important to you than any of your powers or abilities: they're all you could ever ask for.")

#End of Phase 5
