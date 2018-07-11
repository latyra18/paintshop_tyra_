def setup():
    size(400,400)
    background(128, 128, 128)
    
    fill (255,0,0)
    rect(0, 0, 50, 50)
    
    fill (0,0,255)
    rect(0, 51, 50, 50) 
    
    fill (0,255,0)
    rect(0, 102, 50, 50)
    
    fill (255,255,0)
    rect(0, 153, 50, 50)
    
    fill (199, 21, 133)
    rect(0, 204, 50, 50)
    
    fill (255)
    rect(0, 255, 50, 50)
    
    fill (255, 128, 0)
    rect(0, 306, 50, 50)                                                                                                                                                                            
    
    fill (0)
    text("Random", 3, 234)                                                                                                                                               
    text("Yellow", 5, 180) 
    text("Green", 5, 130) 
    text("Red", 8, 28)
    text("Blue", 5, 80)                                                                                                   
    text("Eraser", 5, 283)
    text("Circle M", 3, 333)
                                                                                                                                                                                                                                                                                                                  
def draw():
    if mousePressed and mouseX >= 150:
       line(pmouseX, pmouseY, mouseX, mouseY)
       
    if mousePressed and (mouseX >= 0 and mouseX <= 50) and (mouseY >= 306 and mouseY <= 356) and mouseX >= 150:
       ellipse(pmouseX, pmouseY, 100, 100)
       
    if mousePressed and (mouseX >= 0 and mouseX <= 50) and (mouseY >= 0 and mouseY <= 50):
       stroke (255, 0, 0)
       
    if mousePressed and (mouseX >= 0 and mouseX <= 50) and (mouseY >= 51 and mouseY <= 100):
       stroke (0, 0, 255)
    
    if mousePressed and (mouseX >= 0 and mouseX <= 50) and (mouseY >= 102 and mouseY <= 152):
       stroke (0, 255, 0)
       
    if mousePressed and (mouseX >= 0 and mouseX <= 50) and (mouseY >= 153 and mouseY <= 203):
       stroke (255, 255, 0)
       
    if mousePressed and (mouseX >= 0 and mouseX <= 50) and (mouseY >= 204 and mouseY <= 254):
       stroke(random(255), random(255), random(255))
       
    if mousePressed and (mouseX >= 0 and mouseX <= 50) and (mouseY >= 255 and mouseY <= 305):
       stroke(128, 128, 128)

    if mousePressed and (mouseX >= 0 and mouseX <= 50) and (mouseY >= 306 and mouseY <= 356):
       stroke(random(255), random(255), random(255))
       

    
