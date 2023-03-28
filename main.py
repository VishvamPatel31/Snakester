# Snakester: Python Code from CMU-CS-Academy

# Fill me in!
#Creates score counter and gameOver Tracker
app.score = 0
app.paused = True
app.gameOver = True

# Background
# app.url= 'https://wallpaperaccess.com/full/741514.jpg'
app.background = 'black'

#Background grid
Line(40,0,40,400,fill='white',opacity=30)
Line(80,0,80,400,fill='white',opacity=30)
Line(120,0,120,400,fill='white',opacity=30)
Line(160,0,160,400,fill='white',opacity=30)
Line(200,0,200,400,fill='white',opacity=30)
Line(240,0,240,400,fill='white',opacity=30)
Line(280,0,280,400,fill='white',opacity=30)
Line(320,0,320,400,fill='white',opacity=30)
Line(360,0,360,400,fill='white',opacity=30)
Line(400,0,400,400,fill='white',opacity=30)

Line(0,40,400,40,fill='white',opacity=30)
Line(0,80,400,80,fill='white',opacity=30)
Line(0,120,400,120,fill='white',opacity=30)
Line(0,160,400,160,fill='white',opacity=30)
Line(0,200,400,200,fill='white',opacity=30)
Line(0,240,400,240,fill='white',opacity=30)
Line(0,280,400,280,fill='white',opacity=30)
Line(0,320,400,320,fill='white',opacity=30)
Line(0,360,400,360,fill='white',opacity=30)
Line(0,400,400,400,fill='white',opacity=30)

Rect(0,0,40,40,fill='black',opacity =50)
Rect(80,0,40,40,fill='black',opacity =50)
Rect(160,0,40,40,fill='black',opacity =50)
Rect(240,0,40,40,fill='black',opacity =50)
Rect(320,0,40,40,fill='black',opacity =50)

Rect(40,40,40,40,fill='black',opacity =50)
Rect(120,40,40,40,fill='black',opacity =50)
Rect(200,40,40,40,fill='black',opacity =50)
Rect(280,40,40,40,fill='black',opacity =50)
Rect(360,40,40,40,fill='black',opacity =50)

Rect(0,80,40,40,fill='black',opacity =50)
Rect(80,80,40,40,fill='black',opacity =50)
Rect(160,80,40,40,fill='black',opacity =50)
Rect(240,80,40,40,fill='black',opacity =50)
Rect(320,80,40,40,fill='black',opacity =50)

Rect(40,120,40,40,fill='black',opacity =50)
Rect(120,120,40,40,fill='black',opacity =50)
Rect(200,120,40,40,fill='black',opacity =50)
Rect(280,120,40,40,fill='black',opacity =50)
Rect(360,120,40,40,fill='black',opacity =50)

Rect(0,160,40,40,fill='black',opacity =50)
Rect(80,160,40,40,fill='black',opacity =50)
Rect(160,160,40,40,fill='black',opacity =50)
Rect(240,160,40,40,fill='black',opacity =50)
Rect(320,160,40,40,fill='black',opacity =50)

Rect(40,200,40,40,fill='black',opacity =50)
Rect(120,200,40,40,fill='black',opacity =50)
Rect(200,200,40,40,fill='black',opacity =50)
Rect(280,200,40,40,fill='black',opacity =50)
Rect(360,200,40,40,fill='black',opacity =50)

Rect(0,240,40,40,fill='black',opacity =50)
Rect(80,240,40,40,fill='black',opacity =50)
Rect(160,240,40,40,fill='black',opacity =50)
Rect(240,240,40,40,fill='black',opacity =50)
Rect(320,240,40,40,fill='black',opacity =50)

Rect(40,280,40,40,fill='black',opacity =50)
Rect(120,280,40,40,fill='black',opacity =50)
Rect(200,280,40,40,fill='black',opacity =50)
Rect(280,280,40,40,fill='black',opacity =50)
Rect(360,280,40,40,fill='black',opacity =50)

Rect(0,320,40,40,fill='black',opacity =50)
Rect(80,320,40,40,fill='black',opacity =50)
Rect(160,320,40,40,fill='black',opacity =50)
Rect(240,320,40,40,fill='black',opacity =50)
Rect(320,320,40,40,fill='black',opacity =50)

Rect(40,360,40,40,fill='black',opacity =50)
Rect(120,360,40,40,fill='black',opacity =50)
Rect(200,360,40,40,fill='black',opacity =50)
Rect(280,360,40,40,fill='black',opacity =50)
Rect(360,360,40,40,fill='black',opacity =50)

#Level Label
rl = Rect(17,8,80,28,fill=gradient('yellow','orange'))
level = Label('Level 1',58,20,fill='black',size =20)

#Instructions for how to play the game
newGameScreen = Group(
    Rect(25,50,350,60,fill='lightSeaGreen'),
    Label('The New Snake!',200,80,size=40, font='arial',bold=True),
    Rect(5,120,390,275,fill='midnightblue'),
    Rect(10,130,377,35,fill='paleTurquoise'),
    Label('Use the arrow keys to move the snake.', 200, 148, size = 20,bold=True),
    Rect(5,172,386,33,fill = 'paleTurquoise'),
    Label('The snake head shoud not touch barriers!', 196, 190, size = 19,bold=True),
    Rect(45,213,310,40,fill='paleTurquoise'),
    Label('Press Space to Start', 200, 233, size = 30,bold=True),
    Rect(61,262,280,35,fill='lightSalmon'),
    Label('Eat the food to gain points!', 200, 280, size = 20,bold=True),
    Rect(31,310,150,80,fill='lightSeaGreen'),
    Circle(48.5,335,12,fill=gradient('yellow','slateBlue')),
    Label('= +10 points',120,333,size=20),
    Label('= +20 points',120,370,size=20),
    Star(48.5,370,12,7,fill=gradient('lightSalmon','Aqua')),
    Rect(220,310,153,80,fill='lightSeaGreen'),
    Circle(240,332,12,fill=gradient('mediumVioletRed','yellow',start='left')),
    Star(240,371,12,7,fill=gradient('mediumVioletRed','lightSalmon')),
    Label('= -10 points',313,333,size=20),
    Label('= -15 points',313,370,size=20)
    )
            
#Game Over Labels
gameOverBa = Rect (90,45,200,30,fill='paleTurquoise',visible = False)
gameOverLab = Label ('You hit the barrier!',190,60,size=20,bold=True,visible=False)
gameOverMBack = Rect(18,78,363,180,fill='white',visible = False);
gameOverBack1 = Rect(52,90,300,60,fill='aqua',visible = False)
gameOverLabel1 = Label('Game Over!',200, 120, size = 50,visible = False)
gameOverBack2 = Rect(115,156,170,48,fill='aqua',visible = False)
gameOverLabel2 = Label( 'Score is: ' + str(app.score),200, 180, size = 20,visible = False)
gameOverBack3 = Rect(36,215,330,30,fill='aqua',visible = False)
gameOverLabel3 = Label('Press Space to Start a New Game', 200, 225, size = 20,visible = False)
GameOverBack4 = Rect(35,270,330,130,fill='white',visible = False)
gameOverLabel4 = Label('BE AWARE!',197,297,fill='red',size = 33,bold=True,visible = False)
gameOverLabel5 = Label('Your snake will start from ',203,335,fill='red',size = 27,visible = False)
gameOverLabel6 = Label('where it hit the barrier.',197,367,fill='red',size = 27,visible = False)

#Snake Body Group
player = Group ()

#Snake body components
c1 = Circle(180,20,10,fill=gradient('grey','lime',start='left'))

#Snake Eye
c0 = Circle(180,18,3,fill='black')

##SnakeBody Cont.
c2 = Circle(180,20,10,fill=gradient('grey','lime',start='left'))
c3 = Circle(180,20,9,fill=gradient('grey','lime',start='left'))
c4 = Circle(180,20,8,fill=gradient('grey','lime',start='left'))
c5 = Circle(180,20,7,fill=gradient('grey','lime',start='left'))
c6 = Circle(180,20,6,fill=gradient('grey','lime',start='left'))
c7 = Circle(180,20,5,fill=gradient('grey','lime',start='left'))
c8 = Circle(180,20,4,fill=gradient('grey','lime',start='left'))

#Adding snake components to player group
player.add (c1,c0,c2,c3,c4,c5,c6,c7,c8)

#Steps per second
app.stepsPerSecond= 25

#Initial destination values for snake ( c3.destinationX is defined here)
c3.destinationX = 40
c3.destinationY = 150

#Creates Score Label
r2 = Rect(260,8,120,30,fill=gradient('yellow','orange'))
scoreLabel = Label ('score: ' + str(app.score), 320, 20,fill='black', size = 20)

# Food with 10 points
food = Group()

#creates counters to determine when new food (10 points ) will be created randomly
food.count = 0
food.new = randrange(30,50)

#Creats group for food with 20 points  
food1 = Group ()

##creates counters to determine when new food (20 points ) will be created randomly
food1.count = 0 
food1.new = randrange (30,50)

# poisonous food group0 
foodp = Group()

# creates counters to determine when new food (-10 points ) will be created randomly
foodp.count = 0 
foodp.new = randrange(30,50)

# poisonous food group1
foodp1 = Group()

# creates counters to determine when new food (-15points ) will be created randomly
foodp1.count = 0 
foodp1.new = randrange(30,50)

#Creates a group which contains all the barriers (coming left to right)
barriers = Group()

#Creates counters to determine when a new barrier will be created randomly
barriers.count = 0
barriers.new = randrange(30,50)

#Resets the game using the space bar when the game is over 
def onKeyPress(key):
    if (app.gameOver == True and key == 'space'):
        barriers.clear()
        food.clear()
        food1.clear()
        foodp.clear()
        foodp1.clear()
        player.centerX = 40
        player.centerY = 150
        app.score = 0
        scoreLabel.value = 'Score:  ' + str(app.score)
        newGameScreen.visible = False 
        gameOverLabel1.visible = False
        gameOverLabel2.visible = False
        gameOverLabel3.visible = False
        gameOverLabel4.visible = False
        gameOverLabel5.visible = False
        gameOverLabel6.visible = False
        gameOverBack1.visible = False
        gameOverBack2.visible = False
        gameOverBack3.visible = False
        GameOverBack4.visible = False 
        gameOverMBack.visible = False
        gameOverBa.visible = False
        gameOverLab.visible = False
        barriers.count = 0
        barriers.new = 1
        food.count = 0
        food.new = 1
        food1.count= 0
        food1.new = 1
        foodp.count = 0
        foodp.new = 1
        foodp1.count = 0
        foodp1.new = 1
        app.paused = False
        app.gameOver = False
        app.background ='black'
        level.value = 'Level 1'
        
    # Makes the snake move with up,down,right and left keys.
    if (key=='up'):
        c3.destinationY -=31
    
    elif(key=='down'):
        c3.destinationY +=31
        
    elif(key=='left'):
        c3.destinationX -=31
        
    elif(key=='right'):
        c3.destinationX +=31

def onStep():
    
    #Adds barriers, food, food 1, foodp and foodp1.
    barriers.count += 1
    food.count += 1
    food1.count += 1
    foodp.count += 1
    foodp1.count += 1
    
    #moves the snake ( The snake body follows the head)
    c1.centerX += (c3.destinationX - c1.centerX)/2
    c1.centerY += (c3.destinationY - c1.centerY)/2
    
    c0.centerX += (c3.destinationX - c0.centerX)/2
    c0.centerY += (c3.destinationY - c0.centerY)/2
    
    c2.centerX += (c3.destinationX - c2.centerX)/3.25
    c2.centerY += (c3.destinationY - c2.centerY)/3.25

    c3.centerX += (c3.destinationX - c3.centerX)/4.5
    c3.centerY += (c3.destinationY - c3.centerY)/4.5
    
    c4.centerX += (c3.destinationX - c4.centerX)/5.75
    c4.centerY += (c3.destinationY - c4.centerY)/5.75

    c5.centerX += (c3.destinationX - c5.centerX)/7
    c5.centerY += (c3.destinationY - c5.centerY)/7
    
    c6.centerX += (c3.destinationX - c6.centerX)/8.25
    c6.centerY += (c3.destinationY - c6.centerY)/8.25
    
    c7.centerX += (c3.destinationX - c7.centerX)/9.50
    c7.centerY += (c3.destinationY - c7.centerY)/9.50
    
    c8.centerX += (c3.destinationX - c8.centerX)/10.75
    c8.centerY += (c3.destinationY - c8.centerY)/10.75
    
    #Keeps the snake within the canvas(right of the canvas)
    if (player.right  > 400):
        c1.centerX = 390
        c2.centerX = 390
        c3.centerX = 390
        c4.centerX = 390
        c5.centerX = 390
        c6.centerX = 390
        c7.centerX = 390
        c8.centerX = 390
        c3.destinationX = 390
        
    #Keeps the snake within the canvas(left of the canvas)    
    if (player.left  < 0):
        c1.centerX = 10
        c2.centerX = 10
        c3.centerX = 10
        c4.centerX = 10
        c5.centerX = 10
        c6.centerX = 10
        c7.centerX = 10
        c8.centerX = 10
        c3.destinationX = 10
    
    #Keeps the snake within the canvas(bottom of the canvas)     
    if (player.bottom > 400):
        c1.centerY = 390
        c2.centerY = 390
        c3.centerY = 390
        c4.centerY = 390
        c5.centerY = 390
        c6.centerY = 390
        c7.centerY = 390
        c8.centerY = 390
        c3.destinationY = 390
        
    #Keeps the snake within the canvas(top of the canvas)     
    if (player.top < 0):
        c1.centerY = 10
        c2.centerY = 10
        c3.centerY = 10
        c4.centerY = 10
        c5.centerY = 10
        c6.centerY = 10
        c7.centerY = 10
        c8.centerY = 10
        c3.destinationY = 10
        
    #Controls the speed, the food comes from the top of the canvas (circle)
    for f in food.children:
        f.centerY += 2.75
        if (f.centerY > 380):
            food.remove (f)
            
        # Increases the score by 10 each time the snake eats food (circle:10 points)
        if (player.hitsShape(f)==True):
            app.score += 10
            scoreLabel.value = 'Score:   ' + str(app.score)
            food.remove(f)

    #Controls the distance between each food (circle)
    if (food.count == food.new): 
        food.count = 0
        food.new = randrange (120,225 )
        
        #Random values for food
        RandomX1 = randrange(10,150)
        RandomX2 = randrange(100,380)
        RandomX3 = randrange(30,310)
        RandomX4 = randrange(120,280)
        RandomY1 = randrange(1,75)
        RandomY2 = randrange(-250,300)
        RandomY3 = randrange(-100,200)
        RandomY4 = randrange(-150,50)
        
        #Defined variables to food
        cf1 = Circle(RandomX1,RandomY1,12,fill=gradient('yellow','slateBlue'))
        cf2 = Circle(RandomX2,RandomY2,12,fill=gradient('yellow','slateBlue'))
        cf3 = Circle(RandomX3,RandomY3,12,fill=gradient('yellow','slateBlue'))
        cf4 = Circle(RandomX4,RandomY4,12,fill=gradient('yellow','slateBlue'))
        
        # Adds food to food group
        food.add (
            cf1,cf2,cf3,cf4
            )
    
    #Controls the speed food 1 comes from the bottom of the canvas(star)
    for f1 in food1.children:
        f1.centerY -= 2.75
        if (f1.centerY < 0 ):
            food1.remove (f1)
            
        # Increases the score by 20 each time the snake eats food (star: 20 points)    
        if player.hitsShape(f1):
            app.score += 20
            scoreLabel.value = 'Score:   ' + str(app.score)
            food1.remove(f1)
    
    # Controls the distance between each food1 (star)
    if (food1.count == food1.new):
        food1.count = 0 
        food1.new = randrange (120,250)
        
        #Random values for food1
        RandX1 = randrange(1,200)
        RandX2 = randrange(200,400)
        RandY1 = randrange(350,450)
        RandY2 = randrange(375,425)
        RandX3 = randrange(20,380)
        RandY3 = randrange(350,425)
        
        # defines variables food1's
        sf1 = Star(RandX1,RandY1,12,7,fill=gradient('lightSalmon','Aqua'))
        sf2 = Star(RandX2,RandY2,12,7,fill=gradient('lightSalmon','Aqua'))
        sf3 = Star(RandX3,RandY3,12,7,fill=gradient('lightSalmon','Aqua'))
        
        # adds food to food1 group
        food1.add (
            sf1,sf2,sf3
            )
    
    #Controls the speed foodp comes from the bottom of the canvas (circle)
    for fp in foodp.children:
        fp.centerY -= 2.75
        if (fp.centerY < 0 ):
            foodp.remove (fp)
            
        # Decreases the score by 10 each time the snake eats food (circle:-10points)    
        if player.hitsShape(fp):
            app.score -= 10
            scoreLabel.value = 'Score:   ' + str(app.score)
            foodp.remove(fp)
    
    # Controls the distance between each foodp (circle)
    if (foodp.count == foodp.new):
        foodp.count = 0 
        foodp.new = randrange (120,290)
        
        #Random values for foodp
        RandiX1 = randrange(1,200)
        RandiX2 = randrange(200,400)
        RandiY1 = randrange(350,450)
        RandiY2 = randrange(375,425)
        RandiX3 = randrange(30,310)
        RandiY3 = randrange(350,500)
        
        # defines variables foodp's
        cp1 = Circle(RandiX1,RandiY1,12,fill=gradient('mediumVioletRed','yellow',start='left'))
        cp2 = Circle(RandiX2,RandiY2,12,fill=gradient('mediumVioletRed','yellow',start='left'))
        cp3 = Circle(RandiX3,RandiY3,12,fill=gradient('mediumVioletRed','yellow',start='left'))
        
        # adds badfood(circle) to foodp group
        foodp.add (
            cp1,cp2,cp3
            )
            
    #Controls the speed foodp1 comes from the bottom of the canvas (star)
    for fp1 in foodp1.children:
        fp1.centerY += 2.75
        if (fp1.centerY > 400 ):
            foodp1.remove (fp1)
            
        # Decreases the score by 15 each time the snake eats food (star: -15 points)    
        if player.hitsShape(fp1):
            app.score -= 15
            scoreLabel.value = 'Score:   ' + str(app.score)
            foodp1.remove(fp1)
    
    # Controls the distance between each foodp1 (star)
    if (foodp1.count == foodp1.new):
        foodp1.count = 0 
        foodp1.new = randrange (200,275)
        
        #Random values for foodp1
        RandieX1 = randrange(1,200)
        RandieX2 = randrange(200,400)
        RandieX3 = randrange(35,389)
        RandieY1 = randrange(-250,50)
        RandieY2 = randrange(-75,125)
        RandieY3 = randrange (-250,125)
        
        # defines variables foodp1's
        sfp1 = Star(RandieX1,RandieY1,12,7,fill=gradient('mediumVioletRed','lightSalmon'))
        sfp2 = Star(RandieX2,RandieY2,12,7,fill=gradient('mediumVioletRed','lightSalmon'))
        sfp3 = Star(RandieX3,RandieY3,12,7,fill=gradient('mediumVioletRed','lightSalmon'))
        sfp4 = Star(RandieX2 - 30, RandieY3 +40,12,7,fill=gradient('mediumVioletRed','lightSalmon'))
        
        # adds food to foodp1 group
        foodp1.add (
            sfp1,sfp2,sfp3,sfp4
            )
    
    #This section controls how fast the barriers come at the snake
    for b in barriers.children:
        b.x1 -= 1.5
        b.x2 -= 1.5
        if (b.centerX < -20):
            barriers.remove (b)
            
    #Controls the distance between each barrier 
    if (barriers.count == barriers.new):
        barriers.count = 0
        barriers.new = randrange (110,210 )
        
        #These are assigned variables to the randrange for the x and y values of the barriers.
        RandeX1 = randrange(500,600)
        RandeX2 = randrange(125,200)
        RandeX3 = randrange(50,75)
        RandeY1 = randrange(36,130)
        RandeY2 = randrange(160,260)
        RandeY3 = randrange(290,390)
        
        #Defines variables for  barriers
        b1 = Line(400,RandeY1,RandeX1,RandeY1,lineWidth=4.5,fill=gradient('orange','yellow','crimson'))
        b2 = Line(RandeX1 + RandeX3 + 50,RandeY1, RandeX1 + 400, RandeY1,lineWidth=4.5,fill=gradient('crimson','yellow','orange'))
        
        b3 = Line(450,RandeY2,RandeX1+100,RandeY2,lineWidth=4.5,fill=gradient('orange','yellow','crimson'))
        b4 = Line(RandeX1 + RandeX2 +90,RandeY2, RandeX1 + 350, RandeY2,lineWidth=4.5,fill=gradient('crimson','yellow','orange'))
        
        b5 = Line(425,RandeY3,RandeX1+50,RandeY3,lineWidth=4.5,fill=gradient('orange','yellow','crimson'))
        b6 = Line(RandeX1 + RandeX2 + 35,RandeY3, RandeX1 + 450,RandeY3,lineWidth=4.5,fill=gradient('orange','yellow','crimson'))
        
        #This generates random barriers from the top of the screen
        #adds barriers to barrier group
        barriers.add (
            b1,b2,b3,b4,b5,b6
            )
        
        #Chnages the baarier type after they reach the specified score(increases difficulty)    
        if (app.score >= 70):
            b1.y1 += randrange(1,50)
            b2.y2 -= randrange(15,35)
            
        if (app.score >= 120):
            b3.y2 += randrange (10,30)
            b4.y1 += randrange (20,40)
            
        if (app.score >= 175):
            b5.y1 -= RandeY1
            b6.y1 += randrange (5,25)
            
    #changes barriers speed for different levels.
    #changes level labels when the user reaches a certain score.
    for b in barriers.children:
        #after user reaches the score of 5
        if (app.score >= 5):
            b.x1 -= 2.25
            b.x2 -= 2.25

        #after user reaches the score of 10
        if (app.score >= 10):
            b.x1 -= 2.75
            b.x2 -= 2.75
            
        #after user reaches the score of 25
        if (app.score >= 25):
            b.x1 -= 3.25
            b.x2 -= 3.25
            
        #after user reaches the score of 45
        if (app.score >= 45):
            b.x1 -= 3.50
            b.x2 -= 3.50
            
        #after user reaches the score of 70
        if (app.score >= 70):
            b.x1 -= 0.5
            b.x2 -= 0.5
        
        #after user reaches the score of 100
        if (app.score >= 100):
            b.x1 -= 0.65
            b.x2 -= 0.65
         
        #after user reaches the score of 135
        if (app.score >= 135):
            b.x1 -= 0.75
            b.x2 -= 0.75
        
        #after user reaches the score of 175
        if (app.score >= 175):
            b.x1 -= 0.85
            b.x2 -= 0.85
        
        #after user reaches the score of 200
        if (app.score >= 200):
            b.x1 -= 1
            b.x2 -= 1
            
        #after user reaches the score of 240
        if (app.score >= 240):
            b.x1 -= 1.25
            b.x2 -= 1.25
            
        #after user reaches the score of 200
        if (app.score >= 300):
            b.x1 -= 1.5
            b.x2 -= 1.5
            
        if (app.score >= 380):
            b.x1 -= 1.75
            b.x2 -= 1.75
        
    #creates different backgrouds for different levels at certain score.        
    #after user reaches the score of 5
    if (app.score >= 5):
        app.background = 'midnightblue'
        level.value = 'Level 2'
        
    #after user reaches the score of 10    
    if (app.score >= 10):
        app.background ='navy'
        level.value = 'Level 3'
        
    #after user reaches the score of 25    
    if (app.score >= 25):
        app.background ='purple'
        level.value = 'Level 4'
    
    #after user reaches the score of 45    
    if (app.score >= 45):
        app.background ='indigo'
        level.value = 'Level 5'
        
    #after user reaches the score of 70     
    if (app.score >= 70):
        app.background ='maroon'
        level.value = 'Level 6'
        
    #after user reaches the score of 100        
    if (app.score >= 100):
        app.background ='darkSlategrey'
        level.value = 'Level 7'
    
    #after user reaches the score of 135    
    if (app.score >= 135):
        app.background = 'mediumBlue'
        level.value = 'Level 8 '
        
    #after user reaches the score of 175        
    if (app.score >= 175):
        app.background = 'saddleBrown'
        level.value = 'Level 9'
        
    #after user reaches the score of 200        
    if (app.score >= 200):
        app.background = 'darkGreen'
        level.value = 'Level 10'
        
    #after user reaches the score of 240        
    if (app.score >= 240):
        app.backgground = 'olive'
        level.value = 'Level 11'
        
    #after user reaches the score of 300    
    if (app.score >= 300):
        app.background = 'peru'
        level.value = 'Level 12'
        
    if (app.score >= 380):
        app.background = 'mediumBlue'
        level.value ='Level 13'
        
    #This makes the game stop if it hits any part of the snake and makes game over labels visible
    if (c1.hitsShape(barriers) == True):
        gameOverLabel1.visible = True
        gameOverLabel2.visible = True
        gameOverLabel2.value = 'Score:  ' + str(app.score)
        gameOverLabel3.visible = True 
        gameOverLabel4.visible = True
        gameOverLabel5.visible = True
        gameOverLabel6.visible = True
        GameOverBack4.visible = True
        gameOverBack1.visible = True
        gameOverBack2.visible = True
        gameOverBack3.visible = True
        gameOverMBack.visible = True
        gameOverBa.visible = True
        gameOverLab.visible = True
        barriers.clear()
        food.clear()
        food1.clear()
        foodp.clear()
        foodp1.clear()
        
        # Makes the user rate the game so in a real world the ratings could be used to improve the game.
        a = app.getTextInput('Rate this game from 1 to 10')
        while a.isnumeric()==False:
            a = app.getTextInput('Rating must be a number. Please enter a number')
        print (a)
        
        # Pauses the game and makes the game over
        app.gameOver = True
        app.paused = True
        
    
