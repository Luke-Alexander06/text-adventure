mc = input ("hva er navnet dit?")

print ("|du er i byen å har med deg 300 kr]")
print ("|du har løst til å kjøpe noe. men du har en sum på deg!] ")
print ("|du har valget om 2 ting lego Mario eller Burger King hva vellger du " + mc +"?]")
asking = True
while asking == True:
    valg = input ("|A: du kjøper lego mario,| B:Burger King --> ")

if valg == "A":
     asking = False
     print("|du kjøpte lego mario]")
     print("|og du ble glad]")
     print("|men venene dine ble sur og begyner å angrype deg]")
     print("|Bad ending :(]")

     valgsecret = input()
     if valgsecret == "L":
        print("du blir teleportert til lego luigi dimensonen og blir glad men venene dine er der og du blir banket op")
        print("kul endin?")
     else:
        exit()

elif valg == "B":
    asking = False
    print("|du kjøpte burger og venene dine bled glad]")
    print("|men du fikk diabetes og dødet]")
    print("|bad ending:(]")
else:
    print("du svrte ikke en av alternativene", valg)
    
    valgsecret2 = input()
    if valgsecret2 == "G":
        print("du vokner i en lys verden du ser en stor shyge foran deg hva gjør du " + mc + "?")
valg = input ("A?: du løper vekk, | B?:du se va den mystiske store sygen er --> ")

if valg == "A?":
    print("du løpte vek men når du løpte vek")
    print("fant du ut av du hvar i kyene")
    print("du løpte og løpte til du falt ned")
    print("bad ending")
else:
    exit()

if valg == "B?":
    print("du står å ser på sygen")
    print("den blir mer synelig du begyner å se det og det er")
    print("Gud!!!")
    print("gud sier til deg du har 1 ønske som du kan bruke")
    print("så bruk den klokt " + mc + "?")