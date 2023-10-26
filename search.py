import requests
import string

valids = list("qweyuipfhjkzxm")
base = "ie"
answer = base

for i in valids:
    s4 = i
    for j in valids:
        s5 = j
        answer = s4 + answer + s5 + "l"
        re = requests.post("https://words.dev-apis.com/validate-word",json={"word": answer}, timeout=0.8)
        if(re.json()["validWord"]):
            print(f"VALID WORD FOUND: {answer}")
            answer = base #Reset and start over
        else:
            print(f"{answer} tried.. Not a valid word!")
            answer = base #Reset and start over
            
print("Finished!")
