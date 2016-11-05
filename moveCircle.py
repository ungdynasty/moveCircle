import simplegui

frame = simplegui.create_frame("Home", 500, 500)

class ShapeAttributes:
    
    def __init__(self):
        self.line_width = 5
        self.line_color = "Blue"
        self.fill_color = "Orange"

class Circle:
    
    def __init__(self):
        self.radius = 50
        self.center_point = (100, 100)

class Character:

    key_map = {
        37: "left",
        38: "up",
        39: "right",
        40: "down"
    }

    def __init__(self):
        self.circle_shape = Circle()
        self.shape_attributes = ShapeAttributes()
        
    def draw_me(self, canvas):
        canvas.draw_circle(
            self.circle_shape.center_point,
            self.circle_shape.radius,
            self.shape_attributes.line_width,
            self.shape_attributes.line_color,
            self.shape_attributes.fill_color
        )
        
    def move(self, key):
        if key in Character.key_map.keys():
            print Character.key_map[key]
        

cliq = Character()




def draw(canvas):
    cliq.draw_me(canvas)

frame.set_draw_handler(draw)
frame.set_keydown_handler(cliq.move)
frame.start()
