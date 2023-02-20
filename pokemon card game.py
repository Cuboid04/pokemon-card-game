from tkinter import *
root=Tk()
from PIL import ImageTk, Image
import random
root.title("Endless Dice Game")
root.geometry("700x700")
root.configure(background="orange")

pl1=Label(root, text="Player 1", bg="red", fg="white")
pl2=Label(root, text="Player 2", bg="red", fg="white")
p1score=Label(root, bg="green")
p2score=Label(root, bg="green")
mainlbl=Label(root, bg="white")
pl1.place(relx=0.1, rely=0.3, anchor=CENTER)
pl2.place(relx=0.9, rely=0.3, anchor=CENTER)
p1score.place(relx=0.1, rely=0.4,anchor=CENTER)
p2score.place(relx=0.9, rely=0.4,anchor=CENTER)
mainlbl.place(relx=0.5, rely=0.5, anchor=CENTER)

squirtle=ImageTk.PhotoImage(Image.open("squirtle.jpg"))
rattata=ImageTk.PhotoImage(Image.open("ratata.jpg"))
pikachu=ImageTk.PhotoImage(Image.open("pikachu.jpg"))
persian=ImageTk.PhotoImage(Image.open("persion.jpg"))
paras=ImageTk.PhotoImage(Image.open("paras.jpg"))
nidoking=ImageTk.PhotoImage(Image.open("nidoking.jpg"))
meowth=ImageTk.PhotoImage(Image.open("meowth.jpg"))
kadabra=ImageTk.PhotoImage(Image.open("kadabra.jpg"))
jigglypuff=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
ivysaur=ImageTk.PhotoImage(Image.open("iyvasour.jpg"))
charmander=ImageTk.PhotoImage(Image.open("charmender.jpg"))
bulbasaur=ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
abra=ImageTk.PhotoImage(Image.open("abra.jpg"))
btn=ImageTk.PhotoImage(Image.open("button.jpg"))

pokemonimage_list=[pikachu, squirtle, rattata, persian, paras, nidoking, meowth, kadabra, jigglypuff, ivysaur, charmander, bulbasaur, abra]
pokemonhp_list=[200, 50, 40, 70, 40, 90, 60, 70, 70, 100, 50, 60, 30]
player1score=0
player2score=0
def randompokemon1():
    global player1score
    pokemon_no1=random.randint(1,13)
    randompokemon=pokemonimage_list[pokemon_no1]
    mainlbl["image"]=randompokemon
    randompower=pokemonhp_list[pokemon_no1]
    player1score=player1score+randompower
    p1score["text"]=str(player1score)

def randompokemon2():
    global player2score
    pokemon_no2=random.randint(1,13)
    randompokemon=pokemonimage_list[pokemon_no2]
    mainlbl["image"]=randompokemon
    randompower=pokemonhp_list[pokemon_no2]
    player2score=player2score+randompower
    p2score["text"]=str(player2score)

btn1=Button(root, image=btn, command=randompokemon1)
btn1.place(relx=0.1, rely=0.5, anchor=CENTER)
btn2=Button(root, image=btn, command=randompokemon2)
btn2.place(relx=0.9, rely=0.5, anchor=CENTER)
root.mainloop()