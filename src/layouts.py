class MonadTall:
    def __init__(self, switched=False):
        self.switched = switched

    def arrange(self, stack, screen):
        if len(stack) == 1:
            stack[0].maximise()
            return

        if not self.switched:
            stack[0].place(-8, -1, int(screen.resolution[0]/2+12), int(screen.resolution[1]+8))

            for i in range(1, len(stack)):
                x_pos = int(screen.resolution[0]/2-12)
                y_pos = int((i-1)*(screen.resolution[1]/(len(stack)-1))-1)
                width = int(screen.resolution[0]/2+20)
                height = int(screen.resolution[1]/(len(stack)-1)+9)
                stack[i].place(x_pos, y_pos, width, height)

    def switch(self):
        self.switched = not self.switched