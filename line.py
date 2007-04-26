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
        leer=0
        dlugo=0
        #tu trzeba sie dopyta� Grzesia o funkcje zwracaj�ce wielko�� obiektu
        #tj. wysoko�ci i szeroko�ci i dopisa� to ni�ej
        while (position < dlugo and self.hLineHistogram(position)==0):
            position+=1
            leer+=1
        if position == dlugosclini: # sprawdamy czy nie mamy przypadkiem do czynienia ze spacja lub enterem
            return position, "Enter"
        elif leer>=spaceLength:
            return position, "Space"
        else:
            pass

def findSpaceLength(Histogram): #znajduje d�ugo�� spacji
    pass


        
