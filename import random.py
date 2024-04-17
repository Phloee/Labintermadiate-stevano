import random


def text(tebakn, display, tebak):
    text = ""
    for i in range(len(tebakn)):
        if tebakn[i].lower() == tebak.lower():
            text += tebak.lower()
        else:
            text += display[i]
    return text



def hangman(tebakn):
    nyawa = 6
    used  = ""
    display="_" * len(tebakn)

    print ("welcome to hangman")
    print ("tebak kata")
    print (display)

    while  tebakn != " " and nyawa > 0:
        tebak = input("tebak kata di garisnya  ")

        if len(tebak) != 1:
            print("hanya masukan hanya SATU kata saja")
        elif not tebak.isalpha():
            print ("hanya tebak menggunakan huruf saja")
        elif tebak.lower() in used:
            print("kmau telah menggunka huruf ini")
        else:
            used += tebak.lower()

            if tebak.lower() in tebakn.lower():
                print("kamu telah berhasil menebak satu kata")
                display= text(tebakn,display,tebak)
                print (display)
            else:
                    nyawa -= 1
                    print("maaf tebakan mau salah")
                    print(display)

        if "_" not in display:
            print("selamat anda telah berhasil",tebakn)
        
    
    if nyawa == 0:
        print("maaf anda kalah",tebakn)



tebakn ="indonesia"
hangman(tebakn)
