score = 0
def add_score():
    global score
    score += 10
    
def show_score():
    print(f"Score du joueur : {score}")

def get_score():
    return score