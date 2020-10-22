from tkinter import *
prozor = Tk()
prozor.geometry("510x510+500+200")
prozor.title("Križić-kružić")
m = [["-","-","-"],["-","-","-"],["-","-","-"]]
cX = cO = 0
def gumbSubmitAkcija(event):
    def izj():
        def gumbNAkcija(event):
            global k1, k2, k3, k4, k5, k6, k7, k8, k9
            prozor2.destroy()
            k1 = k2 = k3 = k4 = k5 = k6 = k7 = k8 = k9 = True
            gumb1.config(text = "")
            gumb2.config(text = "")
            gumb3.config(text = "")
            gumb4.config(text = "")
            gumb5.config(text = "")
            gumb6.config(text = "")
            gumb7.config(text = "")
            gumb8.config(text = "")
            gumb9.config(text = "")
            global m
            m = [["-","-","-"],["-","-","-"],["-","-","-"]]
        def gumbIAkcija(event):
            prozor2.destroy()
            prozor.destroy()
        global k1, k2, k3, k4, k5, k6, k7, k8, k9, cX, cO
        k1 = k2 = k3 = k4 = k5 = k6 = k7 = k8 = k9 = False
        prozor2 = Toplevel(prozor)
        prozor2.geometry("300x350+605+305")
        prozor2.title("")
        labelPob = Label(prozor2, text = "Izjednačeno", font=(200))
        labelPob.pack()
        gumbN = Button(prozor2, text = "Nastavi igru", font=(200))
        gumbI = Button(prozor2, text = "Izađi", font=(200))
        gumbN.bind("<Button>", gumbNAkcija)
        gumbI.bind("<Button>", gumbIAkcija)
        gumbN.pack()
        gumbI.pack()
        TT = PhotoImage(file = "ttt.png")
        imgTT = Label(prozor2, image = TTT)
        label = Label(prozor2, text = "")
        label.pack()
        imgTT.pack()
    def pob():
        def gumbNAkcija(event):
            global k1, k2, k3, k4, k5, k6, k7, k8, k9
            prozor2.destroy()
            k1 = k2 = k3 = k4 = k5 = k6 = k7 = k8 = k9 = True
            gumb1.config(text = "")
            gumb2.config(text = "")
            gumb3.config(text = "")
            gumb4.config(text = "")
            gumb5.config(text = "")
            gumb6.config(text = "")
            gumb7.config(text = "")
            gumb8.config(text = "")
            gumb9.config(text = "")
            global m
            m = [["-","-","-"],["-","-","-"],["-","-","-"]]
        def gumbIAkcija(event):
            prozor2.destroy()
            prozor.destroy()
        global k1, k2, k3, k4, k5, k6, k7, k8, k9, cX, cO
        k1 = k2 = k3 = k4 = k5 = k6 = k7 = k8 = k9 = False
        prozor2 = Toplevel(prozor)
        prozor2.geometry("300x350+605+305")
        prozor2.title("")
        labelPob = Label(prozor2, text = "Pobjedio je " + Prvi if kontrola == 2 else "Pobjedio je " + Drugi, font=(200))
        labelPob.pack()
        gumbN = Button(prozor2, text = "Nastavi igru", font=(200))
        gumbI = Button(prozor2, text = "Izađi", font=(200))
        gumbN.bind("<Button>", gumbNAkcija)
        gumbI.bind("<Button>", gumbIAkcija)
        gumbN.pack()
        gumbI.pack()
        TT = PhotoImage(file = "ttt.png")
        imgTT = Label(prozor2, image = TTT)
        label = Label(prozor2, text = "")
        label.pack()
        imgTT.pack()
        if kontrola == 2:
            cX += 1
            labelcX.config(text = Prvi + ": " + str(cX))
        else:
            cO += 1
            labelcO.config(text = Drugi + ": " + str(cO))
    def gumb1Akcija(event):
        global kontrola
        global k1, k2, k3, k4, k5, k6, k7, k8, k9
        if k1:
            if kontrola == 1:
                gumb1.config(text = "X", fg = 'red')
                kontrola = 2
                Igrac = Drugi
                labelRed.config(text = "Na redu je " + Igrac)
                m[0][0] = "X"
                a = m[0].count("X") == 3
                b = m[1].count("X") == 3
                c = m[2].count("X") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "XXX"
                e = m[0][1] + m[1][1] + m[2][1] == "XXX"
                f = m[0][2] + m[1][2] + m[2][2] == "XXX"
                g = m[0][0] + m[1][1] + m[2][2] == "XXX"
                h = m[0][2] + m[1][1] + m[2][0] == "XXX"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            else:
                gumb1.config(text = "O", fg = 'blue')
                kontrola = 1
                Igrac = Prvi
                labelRed.config(text = "Na redu je " + Igrac)
                m[0][0] = "O"
                a = m[0].count("O") == 3
                b = m[1].count("O") == 3
                c = m[2].count("O") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "OOO"
                e = m[0][1] + m[1][1] + m[2][1] == "OOO"
                f = m[0][2] + m[1][2] + m[2][2] == "OOO"
                g = m[0][0] + m[1][1] + m[2][2] == "OOO"
                h = m[0][2] + m[1][1] + m[2][0] == "OOO"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            k1 = False
        else:
            return
        if (k1 or k2 or k3 or k4 or k5 or k6 or k7 or k8 or k9) == False:
            izj()
    def gumb2Akcija(event):
        global kontrola
        global k1, k2, k3, k4, k5, k6, k7, k8, k9
        if k2:
            if kontrola == 1:
                gumb2.config(text = "X", fg = 'red')
                kontrola = 2
                Igrac = Drugi
                labelRed.config(text = "Na redu je " + Igrac)
                m[0][1] = "X"
                a = m[0].count("X") == 3
                b = m[1].count("X") == 3
                c = m[2].count("X") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "XXX"
                e = m[0][1] + m[1][1] + m[2][1] == "XXX"
                f = m[0][2] + m[1][2] + m[2][2] == "XXX"
                g = m[0][0] + m[1][1] + m[2][2] == "XXX"
                h = m[0][2] + m[1][1] + m[2][0] == "XXX"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            else:
                gumb2.config(text = "O", fg = 'blue')
                kontrola = 1
                Igrac = Prvi
                labelRed.config(text = "Na redu je " + Igrac)
                m[0][1] = "O"
                a = m[0].count("O") == 3
                b = m[1].count("O") == 3
                c = m[2].count("O") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "OOO"
                e = m[0][1] + m[1][1] + m[2][1] == "OOO"
                f = m[0][2] + m[1][2] + m[2][2] == "OOO"
                g = m[0][0] + m[1][1] + m[2][2] == "OOO"
                h = m[0][2] + m[1][1] + m[2][0] == "OOO"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            k2 = False
        else:
            return
        if (k1 or k2 or k3 or k4 or k5 or k6 or k7 or k8 or k9) == False:
            izj()
    def gumb3Akcija(event):
        global kontrola
        global k1, k2, k3, k4, k5, k6, k7, k8, k9
        if k3:
            if kontrola == 1:
                gumb3.config(text = "X", fg = 'red')
                kontrola = 2
                Igrac = Drugi
                labelRed.config(text = "Na redu je " + Igrac)
                m[0][2] = "X"
                a = m[0].count("X") == 3
                b = m[1].count("X") == 3
                c = m[2].count("X") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "XXX"
                e = m[0][1] + m[1][1] + m[2][1] == "XXX"
                f = m[0][2] + m[1][2] + m[2][2] == "XXX"
                g = m[0][0] + m[1][1] + m[2][2] == "XXX"
                h = m[0][2] + m[1][1] + m[2][0] == "XXX"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            else:
                gumb3.config(text = "O", fg = 'blue')
                kontrola = 1
                Igrac = Prvi
                labelRed.config(text = "Na redu je " + Igrac)
                m[0][2] = "O"
                a = m[0].count("O") == 3
                b = m[1].count("O") == 3
                c = m[2].count("O") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "OOO"
                e = m[0][1] + m[1][1] + m[2][1] == "OOO"
                f = m[0][2] + m[1][2] + m[2][2] == "OOO"
                g = m[0][0] + m[1][1] + m[2][2] == "OOO"
                h = m[0][2] + m[1][1] + m[2][0] == "OOO"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            k3 = False
        else:
            return
        if (k1 or k2 or k3 or k4 or k5 or k6 or k7 or k8 or k9) == False:
            izj()
    def gumb4Akcija(event):
        global kontrola
        global k1, k2, k3, k4, k5, k6, k7, k8, k9
        if k4:
            if kontrola == 1:
                gumb4.config(text = "X", fg = 'red')
                kontrola = 2
                Igrac = Drugi
                labelRed.config(text = "Na redu je " + Igrac)
                m[1][0] = "X"
                a = m[0].count("X") == 3
                b = m[1].count("X") == 3
                c = m[2].count("X") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "XXX"
                e = m[0][1] + m[1][1] + m[2][1] == "XXX"
                f = m[0][2] + m[1][2] + m[2][2] == "XXX"
                g = m[0][0] + m[1][1] + m[2][2] == "XXX"
                h = m[0][2] + m[1][1] + m[2][0] == "XXX"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            else:
                gumb4.config(text = "O", fg = 'blue')
                kontrola = 1
                Igrac = Prvi
                labelRed.config(text = "Na redu je " + Igrac)
                m[1][0] = "O"
                a = m[0].count("O") == 3
                b = m[1].count("O") == 3
                c = m[2].count("O") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "OOO"
                e = m[0][1] + m[1][1] + m[2][1] == "OOO"
                f = m[0][2] + m[1][2] + m[2][2] == "OOO"
                g = m[0][0] + m[1][1] + m[2][2] == "OOO"
                h = m[0][2] + m[1][1] + m[2][0] == "OOO"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            k4 = False
        else:
            return
        if (k1 or k2 or k3 or k4 or k5 or k6 or k7 or k8 or k9) == False:
            izj()
    def gumb5Akcija(event):
        global kontrola
        global k1, k2, k3, k4, k5, k6, k7, k8, k9
        if k5:
            if kontrola == 1:
                gumb5.config(text = "X", fg = 'red')
                kontrola = 2
                Igrac = Drugi
                labelRed.config(text = "Na redu je " + Igrac)
                m[1][1] = "X"
                a = m[0].count("X") == 3
                b = m[1].count("X") == 3
                c = m[2].count("X") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "XXX"
                e = m[0][1] + m[1][1] + m[2][1] == "XXX"
                f = m[0][2] + m[1][2] + m[2][2] == "XXX"
                g = m[0][0] + m[1][1] + m[2][2] == "XXX"
                h = m[0][2] + m[1][1] + m[2][0] == "XXX"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            else:
                gumb5.config(text = "O", fg = 'blue')
                kontrola = 1
                Igrac = Prvi
                labelRed.config(text = "Na redu je " + Igrac)
                m[1][1] = "O"
                a = m[0].count("O") == 3
                b = m[1].count("O") == 3
                c = m[2].count("O") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "OOO"
                e = m[0][1] + m[1][1] + m[2][1] == "OOO"
                f = m[0][2] + m[1][2] + m[2][2] == "OOO"
                g = m[0][0] + m[1][1] + m[2][2] == "OOO"
                h = m[0][2] + m[1][1] + m[2][0] == "OOO"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            k5 = False
        else:
            return
        if (k1 or k2 or k3 or k4 or k5 or k6 or k7 or k8 or k9) == False:
            izj()
    def gumb6Akcija(event):
        global kontrola
        global k1, k2, k3, k4, k5, k6, k7, k8, k9
        if k6:
            if kontrola == 1:
                gumb6.config(text = "X", fg = 'red')
                kontrola = 2
                Igrac = Drugi
                labelRed.config(text = "Na redu je " + Igrac)
                m[1][2] = "X"
                a = m[0].count("X") == 3
                b = m[1].count("X") == 3
                c = m[2].count("X") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "XXX"
                e = m[0][1] + m[1][1] + m[2][1] == "XXX"
                f = m[0][2] + m[1][2] + m[2][2] == "XXX"
                g = m[0][0] + m[1][1] + m[2][2] == "XXX"
                h = m[0][2] + m[1][1] + m[2][0] == "XXX"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            else:
                gumb6.config(text = "O", fg = 'blue')
                kontrola = 1
                Igrac = Prvi
                labelRed.config(text = "Na redu je " + Igrac)
                m[1][2] = "O"
                a = m[0].count("O") == 3
                b = m[1].count("O") == 3
                c = m[2].count("O") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "OOO"
                e = m[0][1] + m[1][1] + m[2][1] == "OOO"
                f = m[0][2] + m[1][2] + m[2][2] == "OOO"
                g = m[0][0] + m[1][1] + m[2][2] == "OOO"
                h = m[0][2] + m[1][1] + m[2][0] == "OOO"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            k6 = False
        else:
            return
        if (k1 or k2 or k3 or k4 or k5 or k6 or k7 or k8 or k9) == False:
            izj()
    def gumb7Akcija(event):
        global kontrola
        global k1, k2, k3, k4, k5, k6, k7, k8, k9
        if k7:
            if kontrola == 1:
                gumb7.config(text = "X", fg = 'red')
                kontrola = 2
                Igrac = Drugi
                labelRed.config(text = "Na redu je " + Igrac)
                m[2][0] = "X"
                a = m[0].count("X") == 3
                b = m[1].count("X") == 3
                c = m[2].count("X") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "XXX"
                e = m[0][1] + m[1][1] + m[2][1] == "XXX"
                f = m[0][2] + m[1][2] + m[2][2] == "XXX"
                g = m[0][0] + m[1][1] + m[2][2] == "XXX"
                h = m[0][2] + m[1][1] + m[2][0] == "XXX"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            else:
                gumb7.config(text = "O", fg = 'blue')
                kontrola = 1
                Igrac = Prvi
                labelRed.config(text = "Na redu je " + Igrac)
                m[2][0] = "O"
                a = m[0].count("O") == 3
                b = m[1].count("O") == 3
                c = m[2].count("O") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "OOO"
                e = m[0][1] + m[1][1] + m[2][1] == "OOO"
                f = m[0][2] + m[1][2] + m[2][2] == "OOO"
                g = m[0][0] + m[1][1] + m[2][2] == "OOO"
                h = m[0][2] + m[1][1] + m[2][0] == "OOO"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            k7 = False
        else:
            return
        if (k1 or k2 or k3 or k4 or k5 or k6 or k7 or k8 or k9) == False:
            izj()
    def gumb8Akcija(event):
        global kontrola
        global k1, k2, k3, k4, k5, k6, k7, k8, k9
        if k8:
            if kontrola == 1:
                gumb8.config(text = "X", fg = 'red')
                kontrola = 2
                Igrac = Drugi
                labelRed.config(text = "Na redu je " + Igrac)
                m[2][1] = "X"
                a = m[0].count("X") == 3
                b = m[1].count("X") == 3
                c = m[2].count("X") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "XXX"
                e = m[0][1] + m[1][1] + m[2][1] == "XXX"
                f = m[0][2] + m[1][2] + m[2][2] == "XXX"
                g = m[0][0] + m[1][1] + m[2][2] == "XXX"
                h = m[0][2] + m[1][1] + m[2][0] == "XXX"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            else:
                gumb8.config(text = "O", fg = 'blue')
                kontrola = 1
                Igrac = Prvi
                labelRed.config(text = "Na redu je " + Igrac)
                m[2][1] = "O"
                a = m[0].count("O") == 3
                b = m[1].count("O") == 3
                c = m[2].count("O") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "OOO"
                e = m[0][1] + m[1][1] + m[2][1] == "OOO"
                f = m[0][2] + m[1][2] + m[2][2] == "OOO"
                g = m[0][0] + m[1][1] + m[2][2] == "OOO"
                h = m[0][2] + m[1][1] + m[2][0] == "OOO"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            k8 = False
        else:
            return
        if (k1 or k2 or k3 or k4 or k5 or k6 or k7 or k8 or k9) == False:
            izj()
    def gumb9Akcija(event):
        global kontrola
        global k1, k2, k3, k4, k5, k6, k7, k8, k9
        if k9:
            if kontrola == 1:
                gumb9.config(text = "X", fg = 'red')
                kontrola = 2
                Igrac = Drugi
                labelRed.config(text = "Na redu je " + Igrac)
                m[2][2] = "X"
                a = m[0].count("X") == 3
                b = m[1].count("X") == 3
                c = m[2].count("X") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "XXX"
                e = m[0][1] + m[1][1] + m[2][1] == "XXX"
                f = m[0][2] + m[1][2] + m[2][2] == "XXX"
                g = m[0][0] + m[1][1] + m[2][2] == "XXX"
                h = m[0][2] + m[1][1] + m[2][0] == "XXX"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return    
            else:
                gumb9.config(text = "O", fg = 'blue')
                kontrola = 1
                Igrac = Prvi
                labelRed.config(text = "Na redu je " + Igrac)
                m[2][2] = "O"
                a = m[0].count("O") == 3
                b = m[1].count("O") == 3
                c = m[2].count("O") == 3
                d = m[0][0] + m[1][0] + m[2][0] == "OOO"
                e = m[0][1] + m[1][1] + m[2][1] == "OOO"
                f = m[0][2] + m[1][2] + m[2][2] == "OOO"
                g = m[0][0] + m[1][1] + m[2][2] == "OOO"
                h = m[0][2] + m[1][1] + m[2][0] == "OOO"
                if a or b or c or d or e or f or g or h:
                    pob()
                    return
            k9 = False
        else:
            return
        if (k1 or k2 or k3 or k4 or k5 or k6 or k7 or k8 or k9) == False:
            izj()
    global cX, cO
    Prvi = entryPrvi.get()
    if Prvi == "":
        Prvi = "X"
    Drugi = entryDrugi.get()
    if Drugi == "":
        Drugi = "O"
    Igrac = Prvi
    labelImena.pack_forget()
    labelPrvi.pack_forget()
    entryPrvi.pack_forget()
    labelDrugi.pack_forget()
    entryDrugi.pack_forget()
    gumbSubmit.pack_forget()
    labe.pack_forget()
    imgTTT.pack_forget()
    gumb1 = Button(prozor, text = "", height = 1, width = 3, font=('Ariel',50))
    gumb2 = Button(prozor, text = "", height = 1, width = 3, font=('Ariel',50))
    gumb3 = Button(prozor, text = "", height = 1, width = 3, font=('Ariel',50))
    gumb4 = Button(prozor, text = "", height = 1, width = 3, font=('Ariel',50))
    gumb5 = Button(prozor, text = "", height = 1, width = 3, font=('Ariel',50))
    gumb6 = Button(prozor, text = "", height = 1, width = 3, font=('Ariel',50))
    gumb7 = Button(prozor, text = "", height = 1, width = 3, font=('Ariel',50))
    gumb8 = Button(prozor, text = "", height = 1, width = 3, font=('Ariel',50))
    gumb9 = Button(prozor, text = "", height = 1, width = 3, font=('Ariel',50))
    labelRed = Label(prozor, text = "Na redu je " + Igrac)
    labelRed.grid(row = 0, column = 0)
    gumb1.grid(row = 1, column = 0)
    gumb2.grid(row = 1, column = 1)
    gumb3.grid(row = 1, column = 2)
    gumb4.grid(row = 2, column = 0)
    gumb5.grid(row = 2, column = 1)
    gumb6.grid(row = 2, column = 2)
    gumb7.grid(row = 3, column = 0)
    gumb8.grid(row = 3, column = 1)
    gumb9.grid(row = 3, column = 2)
    gumb1.bind("<Button>", gumb1Akcija)
    gumb2.bind("<Button>", gumb2Akcija)
    gumb3.bind("<Button>", gumb3Akcija)
    gumb4.bind("<Button>", gumb4Akcija)
    gumb5.bind("<Button>", gumb5Akcija)
    gumb6.bind("<Button>", gumb6Akcija)
    gumb7.bind("<Button>", gumb7Akcija)
    gumb8.bind("<Button>", gumb8Akcija)
    gumb9.bind("<Button>", gumb9Akcija)
    labelcX = Label(prozor, text = Prvi + ": " + str(cX), font=(30))
    labelcO = Label(prozor, text = Drugi + ": " + str(cO), font=(30))
    labelcX.grid(row = 1, column = 3)
    labelcO.grid(row = 2, column = 3)
labelImena = Label(prozor, text = "Unesite imena igrača!")
labelPrvi = Label(prozor, text = "Prvi igrač:")
labelDrugi = Label(prozor, text = "Drugi igrač:")
entryPrvi = Entry(prozor)
entryDrugi = Entry(prozor)
gumbSubmit = Button(prozor, text = "Unesi")
labelImena.pack()
labelPrvi.pack()
entryPrvi.pack()
labelDrugi.pack()
entryDrugi.pack()
gumbSubmit.pack()
gumbSubmit.bind("<Button>", gumbSubmitAkcija)
TTT = PhotoImage(file = "ttt.png")
imgTTT = Label(prozor, image = TTT)
labe = Label(prozor, text = "")
labe.pack()
imgTTT.pack()
kontrola = 1
k1 = k2 = k3 = k4 = k5 = k6 = k7 = k8 = k9 = True
prozor.mainloop()
