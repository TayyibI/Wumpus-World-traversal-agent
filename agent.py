import random
import numpy as np
class Agent:
    def __init__(self):
        self.wump=[['A' for i in range(50)] for j in range(50)]
        self.kb=[['A' for i in range(50)] for j in range(50)]
        self.moves=[]
        self.move=1
        self.tb=False                      #top to bottom
        self.unsafe=[]
        self.border=False
        self.prev=[]
        self.f=False
        self.exp_t=False
        self.shoot=""
        self.arrow_fired=False
        self.a=False
        self.last_move='null'
        self.step_back=False
        self.counter=0
        self.move_p=""
        
    def get_action(self):
        actions = ['MOVE_UP', 'MOVE_DOWN', 'MOVE_LEFT', 'MOVE_RIGHT']
        extras = ['SHOOT_UP', 'SHOOT_DOWN', 'SHOOT_LEFT', 'SHOOT_RIGHT']
        self.counter+=1
        if self.counter>999:                        # the counter of 1000
            return "QUIT"
        if self.shoot in extras and self.arrow_fired==False:        #check if shoot action has been given and if has taken place if not then shoot
            if self.move_p==actions[0]:
                self.last_move=actions[1]
            if self.move_p==actions[1]:
                self.last_move=actions[0]
            if self.move_p==actions[2]:
                self.last_move=actions[3]
            if self.move_p==actions[3]:
                self.last_move=actions[2]
            self.step_back=True
            self.arrow_fired=True
            return self.shoot
        
        if self.step_back==True:                                    #step back if shot in previous move
            self.step_back=False
            return self.last_move
            
        if self.f==False:                                           #is a flag for if the 4 up down left right is safe
            if self.exp_t==True:                                    #if the up down left right exploration moves have been made 
                #self.unsafe=[
                self.exp_t=False
                self.f=True
            else:
                return(self.explore_world())
        
        if self.f==True:                                            #moves are made 
            t=self.make_move()
            self.f=False
            return t

    def explore_world(self):
        actions = ['MOVE_UP', 'MOVE_DOWN', 'MOVE_LEFT', 'MOVE_RIGHT']
        if self.move==1 and self.tb==False:                 #go up
            self.tb=True
            self.moves.append(actions[0])
            self.move_p=actions[0]
            return actions[0]
        if self.move==1 and self.tb==True:                  #if not border then go up else go down 
            self.tb=False
            self.move=2
            if self.border==False:
                return actions[1]
            else:
                return actions[0]
                
        
        if self.move==2 and self.tb==False:                 #go down 
            self.tb=True
            self.moves.append(actions[1])
            self.move_p=actions[1]
            return actions[1]
        if self.move==2 and self.tb==True:                  #if not border then down else go up
            self.tb=False
            self.move=3
            if self.border==False:
                return actions[0]
            else:
                return actions[1]
                
        
        if self.move==3 and self.tb==False:                  #go left
            self.tb=True
            self.moves.append(actions[2])
            self.move_p=actions[2]
            return actions[2]
        if self.move==3 and self.tb==True:                   #if not border then left else go right
            self.tb=False
            self.move=4
            if self.border==False:
                return actions[3]
            else:
                return actions[2]
                self.move=4
        
        if self.move==4 and self.tb==False:                 #go right
            self.tb=True
            self.moves.append(actions[3])
            self.move_p=actions[3]
            return actions[3]
        if self.move==4 and self.tb==True:                   #if not border then right else go left
            self.tb=False
            self.move=1
            self.moves=[]
            self.exp_t=True
            if self.border==False:
                return actions[2]
            else :
                return actions[3]
                

    
    def make_move(self):
        self.f=False
        actions = ['MOVE_UP', 'MOVE_DOWN', 'MOVE_LEFT', 'MOVE_RIGHT']
        temp=[]                                         #safe moves
        t=self.check_pit(self.prev)                     #check if pit, number tell which move is pit
        if isinstance(t,int):                           #check if number
            if actions[t] in self.unsafe:               #if in unsafe
                if len(self.unsafe)!=1:                 #if lenght of unsafe is not equal to 1
                    for item in self.unsafe:            
                        if item==actions[t]:
                            self.unsafe.remove(item)    #remove from unsafe so that for next coordinate 
                                                        #old unsafes are not confused

        for item in actions:                            
            if item not in self.unsafe:                 #safe moves
                temp.append(item)
        self.unsafe=[]
        self.a=True
        if temp:
            return (random.choice(temp))                #random move
        
    def give_senses(self, location, breeze, stench):
        actions = ['MOVE_UP', 'MOVE_DOWN', 'MOVE_LEFT', 'MOVE_RIGHT']
        extras = ['SHOOT_UP', 'SHOOT_DOWN', 'SHOOT_LEFT', 'SHOOT_RIGHT']
        x=location[0]
        y=location[1]
        
        if stench==True:
            self.wump[x][y]='s'
        if breeze==True:
            self.kb[x][y]='b'
            self.locate_pit(location)
        if breeze==False and stench==False:
            self.kb[x][y]='o'
            self.wump[x][y]='o'            
        if self.prev==location:
            self.border=True
        else:
            self.prev=location
            self.border=False
        if (breeze==True):
            self.unsafe.append(self.move_p)
        if stench==True:
            if self.arrow_fired==False:
                self.unsafe.append(self.move_p)
            c=self.killed_wumpus()
            if c in extras:
                self.shoot=c 

        #print (np.matrix(self.kb[-1::-1]))                  prints knowledge bases
        #print ('\n')
        #print (np.matrix(self.wump[-1::-1]))
        
    def killed_wumpus(self):
        c=(0,0)                 #ur location
        v=(0,0)                 #location of wumpus
        x=0
        y=0                 
        l=[]
        l=self.prev
        for i,lst in enumerate(self.wump):          #checking for stench
            for j,k in enumerate(lst):
                if k == "s":
                     c=(i, j)
        
        if c:
            x,y=c
        
            if self.wump[x+2][y]=='s':
                self.wump[x+1][y]='w'
            if self.wump[x-2][y]=='s':
                self.wump[x-1][y]='w'
            if self.wump[x+1][y+1]=='s':
                self.wump[x+1][y]='w'
            if self.wump[x+1][y-1]=='s':
                self.wump[x+1][y]='w'
            if self.wump[x-1][y+1]=='s':
                self.wump[x][y+1]='w'
            if self.wump[x-1][y-1]=='s':
                self.wump[x][y-1]='w'

        extras = ['SHOOT_UP', 'SHOOT_DOWN', 'SHOOT_LEFT', 'SHOOT_RIGHT']
        for i,lst in enumerate(self.wump):          #checking for wumpus
            for j,k in enumerate(lst):
                if k == "w":
                     v=(i, j)
                     
        if l[0]==v[0]:                              #checking if in same row
            if l[1]>v[1]:                           #checking if above or below agent
                return (extras[1])
            else:
                return (extras[0])
        if l[1]==v[1]:                              #checking if in same column
            if l[0]>v[0]:
                return (extras[2])
            else:
                return (extras[3])

    
    def locate_pit(self,location):
        
        
        x=location[0]
        y=location[1]
        if self.kb[x+2][y]=='b' and self.kb[x+1][y+1]=='b':         #check and put in knowledge base if breeze
            self.kb[x+1][y]='p'
        if self.kb[x+2][y]=='b' and self.kb[x+1][y-1]=='b':
            self.kb[x+1][y]='p'
        if self.kb[x-2][y]=='b' and self.kb[x-1][y+1]=='b':
            self.kb[x-1][y]='p'
        if self.kb[x-2][y]=='b' and self.kb[x-1][y-1]=='b':
            self.kb[x+1][y]='p'
        if self.kb[x][y+2]=='b' and self.kb[x+1][y+1]=='b':
            self.kb[x][y+1]='p'
        if self.kb[x][y+2]=='b' and self.kb[x-1][y+1]=='b':
            self.kb[x][y+1]='p'
        if self.kb[x][y-2]=='b' and self.kb[x+1][y-1]=='b':
            self.kb[x][y-1]='p'
        if self.kb[x][y-2]=='b' and self.kb[x-1][y-1]=='b':
            self.kb[x][y-1]='p'
        
    
    def check_pit(self,l):
        x=l[0]
        y=l[1]
        if self.kb[x+1][y]=='p':                #checks if there is put and returns the action's index where it is
            return 3
        if self.kb[x-1][y]=='p':
            return 2
        if self.kb[x][y+1]=='p':
            return 0
        if self.kb[x][y-1]=='p':
            return 1