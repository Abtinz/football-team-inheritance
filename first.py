class footballteam() :
    def __init__(self,name,league) :
        self.name=name
        self.league=league

    def teamPrint() :
        print(f"Club Name : {self.name}")
        print(f"Club Name : {self.league}")

class players(footballteam) :
    def __init__(self, name, league,playerName,age,value) :
        super().__init__(name, league)
        self.playerName=playerName
        self.age=age
        self.value=value

class post(players) :
    def __init__(self, name, league, playerName, age, value,post,goals,assist,cleansheets,match) :
        super.__init__(name, league, playerName, age, value)
        self.post=post
        self.goals=goals
        self.cleansheets=cleansheets
        self.assist=assist
        self.match=match

    def goalkeeperPrint() :
        print(f"Name : {self.name}")
        print(f"age : {self.age}")
        print(f"Value : {self.value}")
        print(f"post : {self.post}")
        print(f"Matches : {self.match}")
        print(f"Clean Sheets : {self.cleansheets}")

    def defenderPrint() :
        print(f"Name : {self.name}")
        print(f"age : {self.age}")
        print(f"Value : {self.value}")
        print(f"post : {self.post}")
        print(f"Matches : {self.match}")
        print(f"Clean Sheets : {self.cleansheets}")
        print(f"Goals : {self.goals}")
        print(f"Assists : {self.match}")

    def midfielderAndForwardPrint() :
        print(f"Name : {self.name}")
        print(f"age : {self.age}")
        print(f"Value : {self.value}")
        print(f"post : {self.post}")
        print(f"Matches : {self.match}")
        print(f"Goals : {self.goals}")
        print(f"Assists : {self.match}")        

def stadium(footballteam) :
    def __init__(self, name, league,stdName,Capacity,ticketPrice) :
        super(selfself, name, league)
        self.stdName=stdName
        self.Capacity=Capacity
        self.ticketPrice=ticketPrice
    
    def stadiumPrint() :
        print(f"Stadium name : {self.stdName}")
        print(f"Capcity : {self.Capacity} (person)")
        print(f"Ticket Price {self.ticketPrice} $ per match")

def locatoin(footballteam) :
    def __init__(self, name, league,country,city):
        super(selfself, name, league)
        self.country=country
        self.city=city

    def locatoinPrint() :
        super().teamPrint()
        print(f"Country : {self.country}")
        print(f"City : {self.city}")

def date(footballteam) :
    def __init__(self, name, league,year,month,day):
        super(selfself, name, league)
        self.year=year
        self.month=day
        self.day=day

    def datePrint() :
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
   locatoinDetails=location(name, league,country,city)
   playersDetail=[]
   ### post 1
   playerName="De Gea"
   age=30
   value=19000000
   post="GK"
   cleansheets=20
   match=35
   playersDetail.append(post(name, league, playerName, age, value,post,0,0,cleansheets,match))
   ### post 2
   playerName="Maguire"
   age=28
   value=58000000
   post="DF"
   cleansheets=24
   assists=2
   goals=7
   match=45
   playersDetail.append(post(name, league, playerName, age, value,post,goals,assist,cleansheets,match))
   ### post 3
   playerName="Fernandes"
   age=26
   value=70000000
   post="MF"
   assists=25
   goals=19
   match=34
   playersDetail.append(post(name, league, playerName, age, value,post,goals,assist,cleansheets,match))
   ### post4
   playerName="Rashford"
   age=23
   value=60000000
   post="ST"
   assists=16
   goals=17
   match=30
   playersDetail.append(post(name, league, playerName, age, value,post,goals,assist,cleansheets,match))
   
   ### lets print details :
   foundDate.datePrint()
   stdDetail.stadiumPrint()
   locatoinDetails.locatoinPrint()
   for item in playersDetail :
       if item.roll == "GK": item.goalkeeperPrint()
       elif item.roll == "DF" : item.defenderPrint()
       else : item.midfielderAndForwardPrint()
difultDitails()

def mainmnue() :
    post(playerName, age, value,post,goals,assist,cleansheets,match)
