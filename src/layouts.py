import win32gui
import re

class MonadTall:
    def __init__(self, border_window_classes=[], border_window_ignore=[], switched=False, scale=0, margin=0):
        self.border_window_classes = border_window_classes
        self.border_window_ignore = border_window_ignore
        self.switched = switched
        self.scale = scale
        self.config_margin = margin
        self.margin = margin

    def arrange(self, stack, screen):
        if len(stack) == 1:
            if re.findall("|".join(self.border_window_classes), str(win32gui.GetClassName(stack[0].hwnd))) and not re.findall("|".join(self.border_window_ignore), stack[0].title):
                stack[0].place(
                    self.margin, screen.bar.height+self.margin,
                    screen.resolution[0]-(self.margin*2), screen.resolution[1]-(self.margin*2)
                )
            else:
                stack[0].place(
                    self.margin-screen.border[0], screen.bar.height+self.margin-screen.border[1],
                    screen.resolution[0]-((self.margin-screen.border[0])*2), screen.resolution[1]-((self.margin-screen.border[1])*2)
                )
            return

        if not self.switched:
            if re.findall("|".join(self.border_window_classes), str(win32gui.GetClassName(stack[0].hwnd))) and not re.findall("|".join(self.border_window_ignore), stack[0].title):
                # these windows are drawing in the borders
                stack[0].place(
                    self.margin, screen.bar.height+self.margin,
                    int(screen.resolution[0]/2)+self.scale-(self.margin*2), int(screen.resolution[1])-(self.margin*2)
                )
            else:
                # these ones are not
                stack[0].place(
                    -screen.border[0]+self.margin, -1+screen.bar.height+self.margin,
                    int((screen.resolution[0]/2)+(screen.border[0]*2)+self.scale-(self.margin*2)), int(screen.resolution[1]+(screen.border[1])-(self.margin*2))
                )

            for i in range(1, len(stack)):
                if re.findall("|".join(self.border_window_classes), win32gui.GetClassName(stack[i].hwnd)) and not re.findall("|".join(self.border_window_ignore), stack[i].title):
                    # these are drawing in borders
                    x_pos = int(screen.resolution[0]/2)+self.scale+self.margin
                    y_pos = int((i-1)*(screen.resolution[1]/(len(stack)-1)))+screen.bar.height+(self.margin*2)
                    width = int(screen.resolution[0]/2)-self.scale-(self.margin*2)
                    height = int(screen.resolution[1]/(len(stack)-1))-(self.margin*2)
                    stack[i].place(x_pos, y_pos, width, height)
                else:
                    # these are not
                    x_pos = int(screen.resolution[0]/2)-screen.border[0]+self.scale+self.margin
                    y_pos = int((i-1)*(screen.resolution[1]/(len(stack)-1)))-1+screen.bar.height+(self.margin)
                    width = int(screen.resolution[0]/2)+(screen.border[0]*2)-self.scale-(self.margin*2)
                    height = int(screen.resolution[1]/(len(stack)-1) + (screen.border[1]+1))-(self.margin*2)
                    stack[i].place(x_pos, y_pos, width, height)
            
        else:
            if re.findall("|".join(self.border_window_classes), str(win32gui.GetClassName(stack[0].hwnd))) and not re.findall("|".join(self.border_window_ignore), stack[0].title):
                stack[0].place(int(screen.resolution[0]/2)-self.scale, 0, int(screen.resolution[0]/2)-self.scale, int(screen.resolution[1]))
            else:
                stack[0].place(int(screen.resolution[0]/2)-screen.border[0]+self.scale, -1, int(screen.resolution[0]/2)+(screen.border[0]*2)-self.scale, int(screen.resolution[1]+screen.border[1]))

            for i in range(1, len(stack)):
                if re.findall("|".join(self.border_window_classes), win32gui.GetClassName(stack[i].hwnd)) and not re.findall("|".join(self.border_window_ignore), stack[i].title):
                    x_pos = 0
                    y_pos = int((i-1)*(screen.resolution[1]/(len(stack)-1)))
                    width = int(screen.resolution[0]/2)+self.scale
                    height = int(screen.resolution[1]/(len(stack)-1))
                    stack[i].place(x_pos, y_pos, width, height)
                else:
                    x_pos = -screen.border[0]
                    y_pos = int((i-1)*(screen.resolution[1]/(len(stack)-1)))-1
                    width = int((screen.resolution[0]/2)+(screen.border[0]*2)+self.scale)
                    height = int(screen.resolution[1]/(len(stack)-1) + (screen.border[1]+1))
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