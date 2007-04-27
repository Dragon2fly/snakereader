# -*- coding: cp1250 -*-

import picture.py
 
class LineFrame(Frame): #Klasa linijka dziedzicz�ca po klasie obraz

    def extractCharacters(self): #g��wna metoda wywo�ujaca pozosta�e
        hHisto = self.hLinesHistogram()
        spaceLength = findSpaceLength(hHisto)
        position = 0
        Line={}
        Word={}
        End = False
        while not end: #dopuki nie doszli�my do ko�ca linijki wyszukujemy znak�w
            Position, char = self.findChar(position, spaceLength)
            if type(char) == str: #sprawdzenie czy nadano komunikat, czy zwr�cono obiekt
                if char == Space:
                    Line.append(Word)
                    Word={}
                elif char == Enter:
                    Line.append(Word)
                    return Line
            else: # zwr�cono obiekt typu znak
                char.reScale(20,20)
                Word.append(char)

    def findChar(self, position, spaceLength):
        leer=0 # int, licznik pustych kolumn
        Queue=[] #kolejka, bedzie s�uzy� do wyszukiwania i przechowywania s�siad�w
        PiksList=[] #lista bedzie zawirea�a wynikow� liste pikseli.
        
        #tu trzeba sie dopyta� Grzesia o funkcje zwracaj�ce wielko�� obiektu
        #tj. wysoko�ci i szeroko�ci i dopisa� to ni�ej
        
        while (position < Length and self.hLineHistogram(position)==0):
            position+=1
            leer+=1
        if position == length: # sprawdamy czy nie mamy przypadkiem do czynienia ze spacja lub enterem
            return position, "Enter"
        elif leer>=spaceLength:
            return position, "Space"
        else:
            for i in range(0, wysokosc-1): #wpisujemy wszystkie piksele z pierwszej czarnej linijki do kolejki
                if self.getPiksel(positon, i)==1: #sprawdzi� czy na pewno taka kolejno�� wsp��dnych
                    Queue.append((position, i))
                    PiksList.append((position, i))
            while len(Queue)>0:
                Piksel=Queue.pop(0) #krotka zawieraj�ca wsp�rz�dne piksela
                neighbourhood=[(Piksel[0]-1, Piksel[1]+1),(Piksel[0]-1, Piksel[1]),(Piksel[0]-1, Piksel[1]-1),(Piksel[0], Piksel[1]+1),(Piksel[0], Piksel[1]-1),(Piksel[0]+1, Piksel[1]+1),(Piksel[0]+1, Piksel[1]),(Piksel[0]+1, Piksel[1]-1)]
                #to co wyzej to lista wsp�rz�dnych s�siad�w Piksela
                for neighbour in neighbourhood: #sprawdzamy s�siedztwo
                    if not(neighbour in PiksList) and self.getPiksel(neighbour[0],neighbour[1])==1:
                        Queue.append(neighbour)
                        PiksList.append(neighbour)
            PiksList.sort() # soruje liste w ten spos�b, �e najpierw piksele z pierwszej kolumny potem z drugiej itd
            PiksList=self.addHigherPiks(PiksList) #dodajemy wszystkie piksele nad grup�
            

            
#pisze t� metode bo chyba mi sie przyda, a nie ma jej w projekcie.
#ma ona za zadanie doda� do PiksList piksele nad tymi ju� wybranymi
#na razie zak�adam �e najwy�szy wiersz ma numer 0, dopuki mi Grze� nie odpisze
    def addHigherPiks(PiksList):
        position1,High1=PiksList[0]
        position2,High2=PiksList[len(PiksList)-1]
        for kol in range(position1, position2):
            line=0
            while ((kol, line) in PiksList):
                if self.getPiksel(kol,line):
                    PiksList.append((kol,line))
                line+=1
        PiksList.sort()
        return PiksList
                
                            
def findSpaceLength(Histogram, High): #znajduje d�ugo�� spacji
    pass



        
