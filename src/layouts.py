class MonadTall:
    def __init__(self, switched=False, scale=0):
        self.switched = switched
        self.scale = 0

    def arrange(self, stack, screen):
        if len(stack) == 1:
            stack[0].maximise()
            return

        if not self.switched:
            stack[0].place(-8, -1, int(screen.resolution[0]/2+12)+self.scale, int(screen.resolution[1]+8))

            for i in range(1, len(stack)):
                x_pos = int(screen.resolution[0]/2-12)+self.scale
                y_pos = int((i-1)*(screen.resolution[1]/(len(stack)-1))-1)
                width = int(screen.resolution[0]/2+20)-self.scale
                height = int(screen.resolution[1]/(len(stack)-1)+9)
                stack[i].place(x_pos, y_pos, width, height)
        
        else:
            stack[0].place(int(screen.resolution[0]/2-12)-self.scale, -1, int(screen.resolution[0]/2+12)-self.scale, int(screen.resolution[1]+8))

            for i in range(1, len(stack)):
                x_pos = -8
                y_pos = int((i-1)*(screen.resolution[1]/(len(stack)-1))-1)
                width = int(screen.resolution[0]/2+20)+self.scale
                height = int(screen.resolution[1]/(len(stack)-1)+9)
                stack[i].place(x_pos, y_pos, width, height)

    def switch(self, stack, screen):
        self.switched = not self.switched
        self.arrange(stack, screen)

class Monacle:
    def __init__(self):
        pass

    def arrange(self, stack, screen):
        for w in stack:
            w.maximize()

    def switch():
        pass