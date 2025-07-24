#imports random module
import random

History = "history.txt"

def show_history():
    data = open("history.txt","r")
    lines = data.readlines()
    if(len(lines)==0):
        print("No history available............................")
    else:
        for line in reversed(lines) :
            print(line)
            
    data.close()

def save_history(msg):
    with open("history.txt","a") as file:
        file.write(f"Fake News : {msg} \n ")
    file.close()

def clear():
    with open("history.txt","w") as file:
        file.write("")
    print("history cleared...............................")

# create a list of subjects or names 
subjects = [
    "Narendra Modi", "Rahul Gandhi", "Amit Shah", "Arvind Kejriwal", "Yogi Adityanath",
    "Mamata Banerjee", "KCR", "Pinarayi Vijayan", "MK Stalin", "Uddhav Thackeray",
    "Shah Rukh Khan", "Salman Khan", "Aamir Khan", "Akshay Kumar", "Ranbir Kapoor",
    "Ranveer Singh", "Allu Arjun", "Prabhas", "Yash", "Vijay Deverakonda",
    "Rajinikanth", "Kamal Haasan", "Pawan Kalyan", "Chiranjeevi", "NTR Jr.",
    "Alia Bhatt", "Deepika Padukone", "Katrina Kaif", "Kangana Ranaut", "Rashmika Mandanna",
    "Samantha Ruth Prabhu", "Keerthy Suresh", "Tamannaah", "Anushka Shetty", "Trisha Krishnan",
    "IPL", "Bollywood", "Tollywood", "Election 2024", "Indian Economy",
    "Cricket World Cup", "Space Mission", "Stock Market", "NEET Scam", "CBI Raid",
      "Celebrity Wedding", "OTT Release", "Political Scandal", "Startup Fraud", "Tech Layoffs"
]

# create a list of places or events

places = [
    # India places
    "Taj Mahal", "Red Fort", "Qutub Minar", "Gateway of India", "Charminar",
    "India Gate", "Mysore Palace", "Meenakshi Temple", "Golden Temple", "Lotus Temple",
    "Hawa Mahal", "Victoria Memorial", "Statue of Unity", "Ajanta Caves", "Sun Temple Konark",
    "Ranthambore National Park", "Kaziranga National Park", "Dal Lake", "Backwaters of Kerala", "Thar Desert",

    # Global places
    "Eiffel Tower", "Statue of Liberty", "Great Wall of China", "Machu Picchu", "Colosseum",
    "Christ the Redeemer", "Big Ben", "Sydney Opera House", "Mount Fuji", "Petra",
    "Niagara Falls", "Grand Canyon", "Burj Khalifa", "Mount Everest", "Pyramids of Giza",
    "Stonehenge", "Acropolis of Athens", "Sagrada Familia", "Angkor Wat", "Blue Lagoon Iceland",
    "Times Square", "Santorini", "Louvre Museum", "Tower Bridge", "Brandenburg Gate",
    "Great Barrier Reef", "Amazon Rainforest", "Antelope Canyon", "Salar de Uyuni", "Banff National Park"
]

# create a list of actions or events

events = [
    "Politician lost in own rally", "Actor mistaken for delivery guy", "Minister opens fridge factory",
    "Cricketer forgets match day", "Dog wins local election", "Parrot speaks five languages",
    "Man sues ghost", "Robot joins gym", "Cat becomes Instagram CEO", "Cow enters classroom",
    "Fake alien spotted in mall", "Tea seller opens stock market", "Actor adopts talking plant",
    "Student builds rocket from junk", "Village declares Monday as holiday", "Chicken lays square egg",
    "Man marries smartphone", "Fish found wearing glasses", "UFO lands in wedding",
    "Baba starts tech startup", "AI joins as government advisor", "Auto driver invents flying rickshaw",
    "Goat becomes mayor", "Politician caught sleepwalking in parliament", "Fan proposes to statue",
    "Rickshaw races go viral", "Dog becomes cricket team mascot", "Crowd waits for invisible bus",
    "Magician disappears at award show", "Police chase over stolen mangoes", "Man finds treasure in dustbin",
    "Online class hacked by parrot", "Student tops exam by mistake", "Scientist claims moon is a hologram",
    "Monkey drives police jeep", "Groom loses bride over meme", "Cow selfie breaks internet",
    "News anchor laughs 10 mins live", "Cart vendor launches e-commerce app", "Squirrel causes power outage",
    "Turtle blocks highway", "Man wins lottery thrice in one day", "Bride dances with drone",
    "Vegetable vendor writes bestseller", "Pet goat gives TED talk", "Baby names dad", "Fan wears 100 badges",
    "Old man outruns sprinters", "Robot opens tea stall", "Lost suitcase returns with pizza"
]


# generate a random fake news headline
while True:
    user = input("Do you want to see history or clear history or exit from the fake news generator : ").strip()

    if user.lower() == "history":
        show_history()

    elif user.lower() == "clear":
        clear()
    elif user.lower() == "exit":
        break
    else: 
        subject = random.choice(subjects)
        place = random.choice(places)
        event = random.choice(events)

        headline = f"{subject} {event} at {place}!"
        print(f"BREAKING NEWS : ",headline)

        # Wait for user input to generate the next headline
        user_input = input(f"\n Do you want to generate another fake news headline ?(yes/no): ").strip()
        if user_input.lower() == "no":
            break

        save_history(headline)

print("Thank you for using the Fake news generator!\n Have a fun day!")