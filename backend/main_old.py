"""
So our expert system would initially have rules no facts at all
when the user choses GOALS we tell our knowledge Base of the new facts we provided through the 

we do a forward chain and get the list of themes back
after that backend take cares of querying Books based from the database based on the themes the updated KB provided return to the Front end
Clean up the KB [ remove facts for the next request (scope of the KB is a one func call  short lifecycle ]

OUR GOALS can look something like : 
- make more money
- better leadership
- more productive
- healthier lifestyle
- better carreer
- stronger relations
- Get Shores Done
- articulate

OUR THEMES can look something like : 
- enterpren
- finance
- self improvment
- excercise and health
- poetry
- Cooking
- Networking
- psychologie
- 

OUR KB can look something like this : 
1st part : 
-------------------------
makemoney(x) & leadership(x) == > Enterpren
makemoney(x) & productivity(x) == > finance
healthy(x) & stronger relatios(x) == > Networking
healthy(x) & stronger relatios(x) == > exercise and health


2nd part :
-----------------------

Enterpren ==> Book(jamayka1)
Enterpren ==> Book(jamayka3)
finance ==> Book(rich dad poor dad)

 

questions :
- what do we follow when we create a knowledge base  [ par exemple database kayen normalization how about in KB ]

"""

from aima3.logic import *

data = [
        "makemoney(x) & leadership(x) == > THEMES(Enterpren)",
        "makemoney(x) & productivity(x) == > THEMES(finance)",
        "healthy(x) & stronger relatios(x) == > THEMES(Networking)",
        "healthy(x) & stronger relatios(x) == > THEMES(exerciseAndHealth)",
        
    ]

fc = FolKB()

def KnowldgeBase():
    for i in data:
        fc.tell(expr(i))
    return

KnowldgeBase()