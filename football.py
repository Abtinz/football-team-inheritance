class footballteam() :
    def __init__(self,name,league) :
        self.name=name
        self.league=league

    def teamPrint(self) :
        print(f"Club Name : {self.name}")
        print(f"Club League : {self.league}")

class players(footballteam) :
    def __init__(self, name, league,playerName,age,value) :
        super().__init__(name, league)
        self.playerName=playerName
        self.age=age
        self.value=value

class post(players) :
    def __init__(self, name, league, playerName, age, value,roll,goals,assist,cleansheets,match) :
        super().__init__(name, league, playerName, age, value)
        self.roll=roll
        self.goals=goals
        self.cleansheets=cleansheets
        self.assist=assist
        self.match=match

    def goalkeeperPrint(self) :
        print(f"Name : {self.playerName}")
        print(f"age : {self.age}")
        print(f"Value : {self.value}")
        print(f"post : {self.roll}")
        print(f"Matches : {self.match}")
        print(f"Clean Sheets : {self.cleansheets}")

    def defenderPrint(self) :
        print(f"Name : {self.playerName}")
        print(f"age : {self.age}")
        print(f"Value : {self.value}")
        print(f"post : {self.roll}")
        print(f"Matches : {self.match}")
        print(f"Clean Sheets : {self.cleansheets}")
        print(f"Goals : {self.goals}")
        print(f"Assists : {self.match}")

    def midfielderAndForwardPrint(self) :
        print(f"Name : {self.playerName}")
        print(f"age : {self.age}")
        print(f"Value : {self.value}")
        print(f"post : {self.roll}")
        print(f"Matches : {self.match}")
        print(f"Goals : {self.goals}")
        print(f"Assists : {self.match}")      

class stadium(footballteam) :
    def __init__(self, name, league,stdName,Capacity,ticketPrice) :
        super().__init__(name, league)
        self.stdName=stdName
        self.Capacity=Capacity
        self.ticketPrice=ticketPrice
    
    def stadiumPrint(self) :
        print(f"Stadium name : {self.stdName}")
        print(f"Capcity : {self.Capacity} (person)")
        print(f"Ticket Price {self.ticketPrice} $ per match")

class locatoin(footballteam) :
    def __init__(self, name, league,country,city):
        super().__init__(name, league)
        self.country=country
        self.city=city

    def locatoinPrint(self) :
        print(f"Country : {self.country}")
        print(f"City : {self.city}")

class date(footballteam) :
    def __init__(self, name, league,year,month,day):
        super().__init__(name, league)
        self.year=year
        self.month=month
        self.day=day

    def datePrint(self) :
        super().teamPrint()
        print(f"founding date : {self.year}/{self.month}/{self.day}")

def difultDitails() :
   ### football team
   name = "Manchester United"
   league="Primier League"
   ### date 
   year=1902
   month="march"
   day=23
   foundDate=date(name,league,year,month,day)
   ### stadium
   stdName = "Old Trafford"
   Capacity = 	74140
   ticketPrice =70
   stdDetail=stadium(name, league,stdName,Capacity,ticketPrice)
   ### locatoin
   country = "England"
   city = "Manchester"
   locatoinDetails=locatoin(name, league,country,city)
   playersDetail=[]
   ### post 1
   playerName="De Gea"
   age=30
   value=19000000
   roll="GK"
   cleansheets=20
   match=35
   playersDetail.append(post(name, league, playerName, age, value,roll,0,0,cleansheets,match))
   ### post 2
   playerName="Maguire"
   age=28
   value=58000000
   roll="DF"
   cleansheets=24
   assist=2
   goals=7
   match=45
   playersDetail.append(post(name, league, playerName, age, value,roll,goals,assist,cleansheets,match))
   ### post 3
   playerName="Fernandes"
   age=26
   value=70000000
   roll="MF"
   assist=25
   goals=19
   match=34
   playersDetail.append(post(name, league, playerName, age, value,roll,goals,assist,cleansheets,match))
   ### post4
   playerName="Rashford"
   age=23
   value=60000000
   roll="ST"
   assist=16
   goals=17
   match=30
   playersDetail.append(post(name, league, playerName, age, value,roll,goals,assist,cleansheets,match))
   
   ### lets print details :
   print("------------------------------")
   foundDate.datePrint()
   stdDetail.stadiumPrint()
   locatoinDetails.locatoinPrint()
   for item in playersDetail :
       print("------------------------")
       if item.roll == "GK": item.goalkeeperPrint()
       elif item.roll == "DF" : item.defenderPrint()
       else : item.midfielderAndForwardPrint()
   print("Press any Keys to Main Menu : ")
   choice = input()
   if choice.isalpha() : mainmnue()

def manulDitails() :
    name = input("Club Name : ")
    league=input("Club League : ") 
    ### date
    print("------------------------") 
    print("Foundation Date : ")
    year=int(input("Year of foundation : "))
    month=int(input("Month of foundation : "))
    day=int(input("Day of foundation : "))
    foundDate=date(name,league,year,month,day)
    ### stadium
    print("------------------------") 
    print("Stadium Details : ")
    stdName = input("Stadium Name : ")
    Capacity = 	int(input(f"Capacity of {stdName} : "))
    ticketPrice = int(input("Ticket Cost (per mathch) : "))
    stdDetail=stadium(name, league,stdName,Capacity,ticketPrice)
    ### locatoin
    print("------------------------") 
    print("locatoin Details : ")
    country = input("Country Name : ")
    city = input("City Name : ")
    locatoinDetails=locatoin(name, league,country,city)
    playersDetail=[]
    while 1 == 1 :
       print("------------------------") 
       print("player Details : ")
       playerName=input("Player Name : ")
       age= int(input("Age of Player : "))
       value=int(input("Value of Player : "))
       roll=input("Player Roll : ")
       assist=int(input("Assists of Player : "))
       goals=int(input("Goals of Player : "))
       cleansheets=int(input("Cleansheets of Player : "))
       match=int(input("Match of Player : "))
       playersDetail.append(post(name, league, playerName, age, value,roll,goals,assist,cleansheets,match))
       print("1) new player")
       print("2) Exit")
       choice = int(input())
       if choice != 1 : break
    
    ### print details
    print("Club Details : ")
    print("------------------------------")
    foundDate.datePrint()
    stdDetail.stadiumPrint()
    locatoinDetails.locatoinPrint()
    for item in playersDetail :
       print("------------------------")
       if item.roll == "GK": item.goalkeeperPrint()
       elif item.roll == "DF" : item.defenderPrint()
       else : item.midfielderAndForwardPrint()
    
    print("Press any Keys to Main Menu : ")
    choice = input()
    if choice.isalpha() : mainmnue()

def manulDifult() :
 
    print("NEW TEAM :")
    name = input("Club Name : ")
    league=input("Club League : ") 
    ### date
    print("------------------------") 
    print("Foundation Date : ")
    year=int(input("Year of foundation : "))
    month=int(input("Month of foundation : "))
    day=int(input("Day of foundation : "))
    foundDate=date(name,league,year,month,day)
    ### stadium
    print("------------------------") 
    print("Stadium Details : ")
    stdName = input("Stadium Name : ")
    Capacity = 	int(input(f"Capacity of {stdName} : "))
    ticketPrice = int(input("Ticket Cost (per mathch) : "))
    stdDetail=stadium(name, league,stdName,Capacity,ticketPrice)
    ### locatoin
    print("------------------------") 
    print("locatoin Details : ")
    country = input("Country Name : ")
    city = input("City Name : ")
    locatoinDetails=locatoin(name, league,country,city)
    playersDetail=[]
    while 1 == 1 :
       print("------------------------") 
       print("player Details : ")
       playerName=input("Player Name : ")
       age= int(input("Age of Player : "))
       value=int(input("Value of Player : "))
       roll=input("Player Roll : ")
       assist=int(input("Assists of Player : "))
       goals=int(input("Goals of Player : "))
       cleansheets=int(input("Cleansheets of Player : "))
       match=int(input("Match of Player : "))
       playersDetail.append(post(name, league, playerName, age, value,roll,goals,assist,cleansheets,match))
       print("1) new player")
       print("2) Exit")
       choice = int(input())
       if choice != 1 : break
    
    ### print details
    print("Club Details : ")
    print("------------------------------")
    foundDate.datePrint()
    stdDetail.stadiumPrint()
    locatoinDetails.locatoinPrint()
    for item in playersDetail :
       print("------------------------")
       if item.roll == "GK": item.goalkeeperPrint()
       elif item.roll == "DF" : item.defenderPrint()
       else : item.midfielderAndForwardPrint()
   ### Difault MAN UTD
    print("------------------------------")
    print("------------------------------")
    print("------------------------------")
    print("------------------------------")
    ### football team
    name = "Manchester United"
    league="Primier League"
    ### date 
    year=1902
    month="march"
    day=23
    foundDate=date(name,league,year,month,day)
    ### stadium
    stdName = "Old Trafford"
    Capacity = 	74140
    ticketPrice =70
    stdDetail=stadium(name, league,stdName,Capacity,ticketPrice)
    ### locatoin
    country = "England"
    city = "Manchester"
    locatoinDetails=locatoin(name, league,country,city)
    playersDetail=[]
    ### post 1
    playerName="De Gea"
    age=30
    value=19000000
    roll="GK"
    cleansheets=20
    match=35
    playersDetail.append(post(name, league, playerName, age, value,roll,0,0,cleansheets,match))
    ### post 2
    playerName="Maguire"
    age=28
    value=58000000
    roll="DF"
    cleansheets=24
    assist=2
    goals=7
    match=45
    playersDetail.append(post(name, league, playerName, age, value,roll,goals,assist,cleansheets,match))
    ### post 3
    playerName="Fernandes"
    age=26
    value=70000000
    roll="MF"
    assist=25
    goals=19
    match=34
    playersDetail.append(post(name, league, playerName, age, value,roll,goals,assist,cleansheets,match))
    ### post4
    playerName="Rashford"
    age=23
    value=60000000
    roll="ST"
    assist=16
    goals=17
    match=30
    playersDetail.append(post(name, league, playerName, age, value,roll,goals,assist,cleansheets,match))
   
    ### lets print details :
    print("------------------------------")
    foundDate.datePrint()
    stdDetail.stadiumPrint()
    locatoinDetails.locatoinPrint()
    for item in playersDetail :
       print("------------------------")
       if item.roll == "GK": item.goalkeeperPrint()
       elif item.roll == "DF" : item.defenderPrint()
       else : item.midfielderAndForwardPrint()
    print("Press any Keys to Main Menu : ")
    choice = input()
    if choice.isalpha() : mainmnue()


def mainmnue() :
    while 1 == 1:
          print("1) defualt Team(MAN UTD)")
          print("2) New team")
          print("3) New team and defualt Team")
          print("4) Exit")
          cohise = int(input())
          if cohise == 1: difultDitails()
          elif cohise == 2: manulDitails()
          elif cohise == 3: manulDifult()
          elif cohise == 4 : break
    print("See you next time ^ _ ^")
mainmnue()
