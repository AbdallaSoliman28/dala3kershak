# ======== dependencies ========
from predefined_data import intent
import text_processing as tp
import time
from responses import response
import random
import inventory_res
 
# ======== statements ========

print("welome to dala3 kershak")
print("I am Nour your virtual food assistant")
print("what may I call you")
print()
name = input("--> ")
time.sleep(1)
prom = ""

prompts = [f"\nhello {name} breakfast lunch or dinner ? \n (you can exit by typing quit)",
f"\nhello {name} would you like breakfast lunch or dinner? \n (you can exit by typing quit)",
f"\nhello {name} which course do you want breakfast lunch or dinner ? \n (you can exit by typing quit)"
]
 #========== main loop ==========
while prom != "quit":
    intent_found = False
    intent = ""
    prom = input(random.choice(prompts))

    lowered = tp.normalize(prompts)
    punc_removed_str = tp.remove_punc(lowered)
    tokenized = tp.tokenize(punc_removed_str)
    cleaned = tp.remove_stop_words(tokenized)
    print(cleaned)

    for elems in intent:
        for word in cleaned:
            for string in elems[1]:
                if word in string:
                    intent = elems[0]
                intent_found = True
                
                break
            if intent_found:
                break
        if intent_found:
            break
    print(intent)
    print(response(intent))
    print()
    time.sleep(0.5)





