from inventory_res import lists
from predefined_data import intent
def response(intent):
    if intent == "recommendation":
        res == "we have all sort of resturants"
    elif intent == "location_info":
        res == "the resturant is in the 5th settlement "
    elif intent == "hours_info":
        res == "from 8 to 11"
    elif intent == "greetings":
        res == "hey"
    elif intent == "breakfast":
        res == "great would you like to have bakery or barista?"
    elif intent == "Barista":
        res == (f("{name},we have a bunch of choices you can choose from \n {baristas}"))
    elif intent == "bakery":
        res == (f("you {name}, you can choose from these resturants \n {bakery}"))
    elif intent == "lunch":
        res == (f("so {name} which cusine would you like to choose from these \n {cuisines} "))
    elif intent == "italian":
        res == (f("excellent choice {name} here is a list of all the possible italian resturants \n {italian}"))
    elif intent == "american":
        res == (f("alrighhtyyyyy {name} here are some all american resturants \n {american}"))
    elif intent == "french"
        res == (f("exquisite choice Monsieur {name} and the fine french resturants are \n {french}"))
    elif intent == "asian"
        res == (f("you're going to feel the spices with our collection of asian food which are \n {asian}"))
    elif intent == "mexican"
        res == (f("you will be delighted with a fine taste of south america with these resturant \n {mexican}"))
    elif intent == "seafood"
        res == (f("have a taste of the ocean \n {seafood}"))
    elif intent == "arabic"
        res == (f("mafeesh agda3 mn keda \n {arabic}"))
    else:
        res == "I didn't quite get that could you repeat"
