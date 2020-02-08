#This program displays the active roster of a football team sorted by position. The program displays team statistics
#such as the number of players on the active roster, the current team salary, the teams's cap space, the average age of each player
#The program also includes options to give raises to players, cut players or add players to the roster

import statistics

salarycap = 188200000

class Football:

    def __init__(self,player,pos,salary,age):

        self.player = player
        self.pos = pos
        self.salary = salary
        self.age = age

        result = sum(p.salary for p in players)
        assert result < salarycap, 'You have exceeded the salary cap. Please offer a lower salary to stay under the salary cap.'
        assert len(players) <= 53, 'You cannot have more than 53 players on the active roster. You must cut another player if you would like to add this player'

    def playerdescription(self):
        return '{0:s} is {1:d} years old and plays {2:s} and makes ${3:,d} per year'.format(self.player,self.age,self.pos,self.salary)
    def lastname(self):
        return self.player.split()[-1]
    def giveRaise(self,percent):
        self.salary = int(self.salary * (1 + percent))
        convert = percent * 100
        result = sum(p.salary for p in players)
        assert result < salarycap, 'You have exceeded the salary cap. Please offer a lower salary to stay under the salary cap.'
        print('{0:s} has been given a {1:d}% raise and his new salary is ${2:,d}'.format(self.player,int(convert),self.salary))


    def cutplayer(name):
        for p in players:
            if name == p.player:
                players.remove(p)
        print('{0:s} has been released from the Mud Dogs.'.format(name))

    def addplayer(name,pos,salary,age):
        players.append(Football(name,pos,salary,age))
        print('{0:s} has been signed to the Mud Dogs active roster'.format(name))
        assert len(players) <= 53, 'You cannot have more than 53 players on the active roster. You must cut another player if you would like to add this player'


players = []
players.append(Football('John Smith','RB',749912,23))
players.append(Football('Ron Ward', 'TE', 7000000, 26))
players.append(Football('Matt Abrams', 'QB',2525000, 30))
players.append(Football('Anthony Atlee', 'OL', 11050000,30))
players.append(Football('Chad Jalen', 'WR', 880000,32))
players.append(Football('Terry Wells', 'CB', 2000000, 35))
players.append(Football('Wyatt Reynolds', 'LB', 8500000,39))
players.append(Football('Isaac Johnson','DE',4894000,22))
players.append(Football('Terrence Thompson', 'S', 4500000,27))
players.append(Football('Eric Rollins', 'QB',17000000,25))
players.append(Football('Lonnie Bowers', 'RB', 2500000,28))
players.append(Football('Stephen Whitworth', 'DT',5700000,32))
players.append(Football('Barry Lions','TE',3450000,30))
players.append(Football('Chad Linder', 'CB', 2900000,35))
players.append(Football('Clarence Connor','DE',5400000,24))
players.append(Football('Johnny Dorchester', 'DT',2750000,22))
players.append(Football('Eric Everman','S',950000,22))
players.append(Football('Monty Morgan', 'LB', 6200000,27))
players.append(Football('A.J. Wiley','WR', 2500000,26))
players.append(Football('Mike Mulasky', 'OL',3000000,31))
players.append(Football('Jeff Hanover', 'WR', 4000000,29))
players.append(Football('Brandon Roberts','TE',700000,22))
players.append(Football('Randy Reynolds','CB',2300000,28))
players.append(Football('Earnest Edwards','DE',1800000,25))
players.append(Football('Jake Lambo','OL',3400000,23))
players.append(Football('Cam Cook', 'DT', 1900000,25))
players.append(Football('Rick Sonnan','CB',1100000,30))
players.append(Football('Mickey Thomas','LB',2300000,32))
players.append(Football('Tommy Tolchinsky','OL', 850000,29))
players.append(Football('Louis Lanna','OL',2000000,23))
players.append(Football('Aaron Franklin','LB',1400000,25))
players.append(Football('Sheldon Tomlinson','RB',3000000,27))
players.append(Football('Arnold Jones','LB',1700000,31))
players.append(Football('Jarrod Ponderman','S',850000,22))
players.append(Football('Roger Rickman','OL',2200000,25))
players.append(Football('Willie Walls', 'WR',1200000,29))
players.append(Football('Mark Monolon', 'DE', 7800000,29))
players.append(Football('Bart Simmons','OL', 5200000,25))
players.append(Football('David Erickson','OL',2700000,34))
players.append(Football('Sam Dollansky', 'S', 4500000,24))
players.append(Football('Burt Blanchard','DT',2300000,25))
players.append(Football('Rufus Langley','LB', 1500000,22))
players.append(Football('Zane Cochran','OL', 1500000,21))
players.append(Football('Larry Isom','OL',3200000,23))
players.append(Football('Sean Strahan','S', 2300000,25))
players.append(Football('Nick Dominguez','TE',1220000,29))
players.append(Football('Alex Monocan', 'CB',1000000,30))
players.append(Football('Bradley Chilowski','K',700000,37))
players.append(Football('Bob Trent','LS',700000,34))
players.append(Football('Pat York','P',2500000,30))


maximum = max(p.salary for p in players)
result = sum(p.salary for p in players)

salaryrem = 188200000 - result
avgage = statistics.mean(p.age for p in players)

poscount=[]
for p in players:
    poscount.append(p.pos)

rb = poscount.count('RB')
te = poscount.count('TE')
qb = poscount.count('QB')
ol = poscount.count('OL')
wr = poscount.count('WR')
cb = poscount.count('CB')
lb = poscount.count('LB')
de = poscount.count('DE')
s = poscount.count('S')
dt = poscount.count('DT')
ls = poscount.count('LS')
p = poscount.count('P')
k = poscount.count('K')

print('\n')

posname={players[i].player:players[i].pos for i in range(len(players))}

rbname = []
for key, value in posname.items():
    if value == 'RB':
        rbname.append(key)

tename = []
for key, value in posname.items():
    if value == 'TE':
        tename.append(key)

qbname = []
for key, value in posname.items():
    if value == 'QB':
        qbname.append(key)

olname = []
for key, value in posname.items():
    if value == 'OL':
        olname.append(key)

wrname = []
for key, value in posname.items():
    if value == 'WR':
        wrname.append(key)

cbname = []
for key, value in posname.items():
    if value == 'CB':
        cbname.append(key)

lbname = []
for key, value in posname.items():
    if value == 'LB':
        lbname.append(key)

dename = []
for key, value in posname.items():
    if value == 'DE':
        dename.append(key)

sname = []
for key, value in posname.items():
    if value == 'S':
        sname.append(key)

dtname = []
for key, value in posname.items():
    if value == 'DT':
        dtname.append(key)

lsname = []
for key, value in posname.items():
    if value == 'LS':
        lsname.append(key)

kname = []
for key, value in posname.items():
    if value == 'K':
        kname.append(key)

pname = []
for key, value in posname.items():
    if value == 'P':
        pname.append(key)

print('There are currently {} players on the Mud Dogs roster'.format(len(players)))
print('The Mud Dogs current team salary is ${0:,d}'.format(result))
print('The highest paid player on the Mud Dogs has a salary of ${0:,d}'.format(maximum))
print('The Mud Dogs have ${0:,d} remaining to spend until they are over the salary cap'.format(int(salaryrem)))
print('The average age of the Mud Dogs roster is {0:.2f} years.'.format(avgage))
print('\n')
print('------NUMBER OF PLAYERS ON ACTIVE ROSTER AT EACH POSITION--------')
print('\n')

print('{0:d} running backs - {1:s}'.format(rb,', '.join(rbname)))
print('{0:d} tight ends - {1:s}'.format(te,', '.join(tename)))
print('{0:d} quarterbacks - {1:s}'.format(qb, ', '.join(qbname)))
print('{0:d} offensive lineman - {1:s}'.format(ol, ', '.join(olname)))
print('{0:d} wide receivers - {1:s}'.format(wr, ', '.join(wrname)))
print('{0:d} cornerbacks - {1:s}'.format(cb,', '.join(cbname)))
print('{0:d} linebackers - {1:s}'.format(lb, ', '.join(lbname)))
print('{0:d} defensive ends - {1:s}'.format(de, ', '.join(dename)))
print('{0:d} safeties - {1:s}'.format(s, ', '.join(sname)))
print('{0:d} defensive tackles - {1:s}'.format(dt, ', '.join(dtname)))
print('{0:d} punter - {1:s}'.format(p, ', '.join(pname)))
print('{0:d} kicker - {1:s}'.format(k, ', '.join(kname)))
print('{0:d} long snapper - {1:s}'.format(ls, ', '.join(lsname)))

print('\n')

#Gives a raise to John Smith and gives his new salary

players[0].giveRaise(.2)

print('\n')

#Recalculates the total salary of entire team after raise given to John Smith

result = sum(p.salary for p in players)
print(result)

#Removes Chad Jalen from roster and prints statement showing his release

Football.cutplayer('Chad Jalen')

#Shows updated total number of players on roster after Chad Jalen's release

print(len(players))

#Adds Rod Allen to the roster and prints statement showing he has been signed

Football.addplayer('Rod Allen', 'LB',1500000,32)








