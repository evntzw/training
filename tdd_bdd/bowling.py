class Game():
    def __init__(self):
        self.scoreboard = Scoreboard()
    
    def roll(self, pins: int):
        self.scoreboard.putScore(pins)
    
    def score(self):
        return self.scoreboard.totalScore()

class Frame():
    def __init__(self):
        self.roll_one = -1
        self.roll_two = -1
    
    def putScore(self, pins):
        if self.roll_one == -1:
            self.roll_one = pins
        elif self.roll_two == -1:
            self.roll_two = pins
    
    def frameScore(self):
        if self.isRolled():
            return self.roll_one + self.roll_two
        else:
            return None
    
    def isRolled(self):
        return self.roll_one != -1 and self.roll_two != -1
    
    def isSpare(self):
        return self.roll_one + self.roll_two == 10
    
    def isStrike(self):
        if self.roll_one == 10:
            self.roll_two = 0
            return True
        else:
            return False
           
class Scoreboard():
    def __init__(self):
        self.frames = [Frame() for _ in range(10)]        
        self.current_frame = 0
        
    def putScore(self, pins):
        if self.frames[self.current_frame].isRolled():
            self.current_frame += 1
            
        self.frames[self.current_frame].putScore(pins)
        
    def totalScore(self):
        score = 0
        for frame in range(self.current_frame+1):
            print("\n For loop-frame no: %s", frame)
            if self.frames[frame].frameScore() != None:
                if self.frames[frame].isSpare():
                    score += self.frames[frame].frameScore() + self.frames[frame+1].roll_one
                elif self.frames[frame].isStrike():
                    score += self.frames[frame].frameScore() + self.frames[frame+1].frameScore()
                else:
                    score += self.frames[frame].frameScore()
            else:
                score = None
        
        return score
