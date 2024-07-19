def main():
    kata = "kos"
    tebakan= "_" * len(kata)
    huruf_benar =[]

    print ("hangman harus di tembak ", len(kata), "huruf")

    while True:
        huruf_tebakan = input("Masukkan huruf tebakan kamu:").lower()

        if len(huruf_tebakan) != 1 or not huruf_tebakan.isalpha():
            print("Masukkan huruf dan hanya 1 aja yaa")
            continue
        elif huruf_tebakan not in kata:
            print ("tebakan salah")
            continue
        else:
            huruf_benar.append (huruf_tebakan)
            tebakan_baru = ""
            for i in range (len(kata)):
                if kata [i] == huruf_tebakan:
                    tebakan_baru += huruf_tebakan
                else :
                    tebakan_baru += tebakan[i]
            tebakan = tebakan_baru
            print("tebakanmu benar")
            if "_" not in tebakan:
                print("selesai")
                break


main()
    