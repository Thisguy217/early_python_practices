import tkinter as tk
import random
quotes = [
    "See! They aren\'t so tough, I think a saw some of them wearing skrits.",
    "I just wet myself.",
    "Looks like I picked the wrong day to quit smoking.",
    "One down, 50 billion to go!",
    "No running!",
    "I am on fire baby!",
    "Notify his next of kin cause they\'re next!",
    "Who\'s your daddy!",
    "You\'re almost a man.",
    "The thing on the left is the brake!",
    "Well, that\'s one way to save ammo.",
    "Shoot me too, I don\'t want the aliens to get me!",
    "Please stop being human.",
    "If got issues with me performance, prefer we have rational adult conversation.",
    "Zug zug.",
    "Don\'t worry, me already resigned early death.",
    "You see nipple! Me thirsty!",
    "Nap?",
    "Shh...me hunting hewatics!",
    "I stare at you. You stare at me. I faile to see the point.",
    "Hang on, I\'m gonna read your mind...uhh..aaand I\'m getting nothin\'.",
    "Didn\'t I give you this for Christmas?",
    "I know this is a great game, but don\'t you think it\'s time you changed your underpants?",
    "You got a sandwhich in there?",
    "We are wearing the same uniform, sir.",
    "I am sorry, did you really mean to suck?",
    "You have got to be sucking on purpose.",
    "Hey I am sorry to say, but I just don\'t feel the same way about you.",
    "Hey, don\'t make me teabag you!",
    "I don\'t normally date giant, armored, killing machines. Sorry.",
    "Enough dude. Brrrb...brrrb...brrrb.",
    "This means so much to me!",
    "Shooting friendlies, is not friendly, is it?",
    "He was breathing just fine through the hole in his FACE!",
    "You got a lot of pockets, one of them holding a sandwhich?",
    "Because of you, ''my'' kids can\'t get enough gas. Or ''nipple''! How does that make you ''feeeeeeeel''?!",
    "I\'m trying new contacts, now stop dripping!",
    "That is going to hurt tomorrow.",
    "Could we just not kill each other?",
    "I am going to write you up!",
    "You have some brains. On your face.",
    "You know I can read your mind, and I gotta say, what you are thinking about right now is...uh...is just '''not''' ok.",
    "It\'s the former command! We\'ve got new ones now! And they\'re actually very nice. Though big. And furry. And kind of petite. And angry.",
    "Taunting the demon definitely qualifies for a rukting!",
    "Ding dong the demon is dead!"
    ]
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 1000, height = 400)
canvas1.pack()
label1 = tk.Label(root, text='', fg='black', font=('helvetica', 12, 'bold'), wraplength=950,justify='center')

def hello():  
    label1.config(text= random.choice(quotes))
    canvas1.create_window(500, 100, window=label1)

button1 = tk.Button(text='Click Me',command=hello, bg='brown',fg='white')
canvas1.create_window(500, 50, window=button1)

root.mainloop()