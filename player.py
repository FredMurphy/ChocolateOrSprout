from buildhat import Motor, ColorDistanceSensor

class Player:
    
    def __init__(self, sensor_port, motor_port, chocolate_direction):
        self.sensor = ColorDistanceSensor(sensor_port)
        self.motor = Motor(motor_port)
        self.chocolate_direction = chocolate_direction
        self.score = 0
        
    def zero(self):
        self.score = 0
    
    def add_point(self):
        self.score = self.score + 1
        #print('Score now', self.score)
    
    def get_score(self):
        return self.score
    
    def get_color(self):
        distance = self.sensor.get_distance()
        if (distance > 1):
            # too far away
            return ""
        color = self.sensor.get_color_rgb()
        min_val = min(color)
        max_val = max(color)
        # print('Color',color, min_val, max_val)

        if (max_val < 30 or (max_val-min_val)< 5):
            # not enough contrast
            return ""

        lower = (min_val+min_val+max_val)/3
        upper = (min_val+max_val+max_val)/3
        red = color[0]
        green = color[1]
        blue = color[2]

        if (red > lower and red < upper) or (green > lower and green < upper) or (blue > lower and blue < upper):
            # unclear
            return ""

        if (red > upper and green < lower and blue < lower):
            return "red"
        if (red < lower and green > upper and blue < lower):
            return "green"
        # more like cyan, but that's what we're using and we'll call it blue
        if (red < lower and green > upper and blue > upper):
            return "blue"
        if (red > upper and green > upper and blue < lower):
            return "yellow"

        # some other colour
        return ""
