# -*- coding: cp1250 -*-

import picture.py
import cPickle
 
class LineFrame(Frame): #Klasa linijka dziedzicz�ca po klasie obraz

    def extractCharacters(self): #g��wna metoda wywo�ujaca pozosta�e
        hHisto = self.hLinesHistogram()
        spaceLength = findSpaceLength(hHisto)
        position = 0
        Line={}
        Word={}
        End = False
        while not end: #dopuki nie doszli�my do ko�ca linijki wyszukujemy znak�w
            position, char, correction = self.findChar(position, spaceLength+correction)
            if type(char) == str: #sprawdzenie czy nadano komunikat, czy zwr�cono obiekt
                if char == Space:
                    Line.append(Word)
                    Word={}
                elif char == Enter:
                    Line.append(Word)
                    return Line
            else: # zwr�cono obiekt typu znak
                Word.append(char)

    def findChar(self, position, spaceLength, ): 
        leer=0 # int, licznik pustych kolumn
        Queue=[] #kolejka, bedzie s�uzy� do wyszukiwania i przechowywania s�siad�w
        PiksList=[] #lista bedzie zawirea�a wynikow� liste pikseli.
        
        #tu trzeba sie dopyta� Grzesia o funkcje zwracaj�ce wielko�� obiektu
        #tj. wysoko�ci i szeroko�ci i dopisa� to ni�ej
        
        while (position < length and self.hLineHistogram(position,high)==0):
            position+=1
            leer+=1
        if position == length: # sprawdamy czy nie mamy przypadkiem do czynienia ze spacja lub enterem
            return position, "Enter", 0
        elif leer>=spaceLength:
            return position, "Space", 0
        else:
            for i in range(0,High-1): #wpisujemy wszystkie piksele z pierwszej czarnej linijki do kolejki
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
            position1,High1=PiksList[0]
            position2,High2=PiksList[len(PiksList)-1]  # wten spos�b uzyskamy numery skrajnych kolumn
            charLength=position2-position1
            
            if charLength<=High: #sprawdzamy czy nie wykryli�my sklejki d�u�szej ni� d�ugo�� kafelki
                newPositon= position+(charLength/2) #nowa pozycja w �rodku wykrytego znaku by wyeliminowa� przypadek gdy jeden znak nakryje drugi
                Char=CharFrame() #tworzymy obiekt typu Charframe, ale jeszcze nie wiem jak go wywo�a�
                
                for el in PiksList: #je�li nie wymy�limy efektywniejszego sposobu
                    Char.putPiksel(position-el[0],el[1])
                    self.makeWhite(el[0],el[1])
                    
                Char.reScale(20,20)
                return position, Char, charLength/2

            else: #czyli gdy wykryto za d�ug� sklejke
                PiksList, Char = reconChar(Pikslist)
                position1,High1=PiksList[0]
                position2,High2=PiksList[len(PiksList)-1]  # wten spos�b uzyskamy numery skrajnych kolumn
                charLength=position2-position1
                newPositon= position+(charLength/2) #nowa pozycja w �rodku wykrytego znaku by wyeliminowa� przypadek gdy jeden znak nakryje drugi

                return position, Char, charLength/2

            
#pisze t� metode bo chyba mi sie przyda, a nie ma jej w projekcie.
#ma ona za zadanie doda� do PiksList piksele nad tymi ju� wybranymi
#na razie zak�adam �e najwy�szy wiersz ma numer 0, dopuki mi Grze� nie odpisze

    def addHigherPiks(PiksList):
        position1,High1=PiksList[0]
        position2,High2=PiksList[len(PiksList)-1]
        for kol in range(position1, position2): #dla ka�edj kolumnt sprawdzamy piksele nad znalezionymi
            line=0
            while ((kol, line) in PiksList):
                if self.getPiksel(kol,line): #je�eli czarne, to dodajemy je do listy
                    PiksList.append((kol,line))
                line+=1
        PiksList.sort()# na koniec sortujemy liste ponownie by mia�a taki sam format jak na wejsciu, przyda sie to zaraz w findChar
        return PiksList

#######################################################################################################################

def reconChar(PiksList, high):
    position, h=PiksList[0]
    for piks in PiksList: #us�wamy wszystkie piksele kt�re nie mieszcz� sie w kafelce
        if piks[0]>=position+high-1:
            PiksList.remove(piks)
            
    Char=CharFrame() #tworzymy obiekt typu Charframe, ale jeszcze nie wiem jak go wywo�a�      
    for el in PiksList: #je�li nie wymy�limy efektywniejszego sposobu
        Char.putPiksel(position-el[0],el[1])

    CharScaled=copy.deepcopy(Char)    
    CharScaled.reScale(20,20)
    if CharScaled.getOutput():
        return PiksList, CharScaled
    else:
        prop=[[],[],[]]
        histo=Char.hLinesHistogram()
        for i in range(0, len(histo):
            if histo[i]<=3:
                prop[histo[i]-1].append(i)
        for proposition in prop:
            proposition.reverse()
            CharPro=copy.deepcopy(Char)
            PiksListPro=copy.deepcopy(PiksList)
            for kolumn in proposition:
                for el in PiksList: #je�li nie wymy�limy efektywniejszego sposobu
                    if el[1]>=proposition:
                        CharPro.makeWhite(position-el[0],el[1])
                        PiksListPro.remove(el)
                CharProScaled=copy.deepcopy(CharPro)
                CharProScaled.reScale(20,20)
                if CharProScaled.getOutput():
                    return PiksListPro, CharProSlaled
        return PiksList, Char # gdyby to ni� nie da�o by zwr�ci� cokolwiek
                
                            
def findSpaceLength(Histogram, High): #znajduje d�ugo�� spacji
    summ=0
    length=0
    number=0
    for kol in Histogram:
        if kol==0:
            length+=1
        elif kol>0 and length>0:
            if length<High:
                summ+=length
                length=0
                number+=1
            else:length=0
    return summ/number      
