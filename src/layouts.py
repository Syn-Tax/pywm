import win32gui
import re
import window


class MonadTall:
    def __init__(self, border_window_classes=[], border_window_ignore=[], switched=False, scale=0, margin=0):
        self.border_window_classes = border_window_classes
        self.border_window_ignore = border_window_ignore
        self.switched = switched
        self.scale = scale
        self.config_margin = margin
        self.margin = margin

    def arrange(self, stack, screen, workspaces, window_ignore=[]):
        if len(stack) < 1:
            return
        elif len(stack) == 1:
            if re.findall("|".join(self.border_window_classes), str(win32gui.GetClassName(stack[0].hwnd))) and not any(re.findall("|".join(self.border_window_ignore), stack[0].title)):

                pos_x = self.margin
                pos_y = screen.bar.height+self.margin
                width = screen.resolution[0]-(self.margin*2)
                height = screen.resolution[1]-(self.margin*2)

                print(f"{stack[0].title}: [{pos_x}, {pos_y}, {width}, {height}]")

                stack[0].place(pos_x, pos_y, width, height)
            else:
                pos_x = self.margin-screen.border[0]
                pos_y = screen.bar.height + self.margin #-screen.border[1]
                width = screen.resolution[0]-((self.margin-screen.border[0]) *2)
                height = screen.resolution[1]-((self.margin))

                print(f"{stack[0].title}: [{pos_x}, {pos_y}, {width}, {height}]")

                stack[0].place(pos_x, pos_y, width, height)
                return

        if not self.switched:
            if re.findall("|".join(self.border_window_classes), str(win32gui.GetClassName(stack[0].hwnd))) and not any(re.findall("|".join(self.border_window_ignore), stack[0].title)):
                # these windows are drawing in the borders
                pos_x = self.margin
                pos_y = screen.bar.height+self.margin
                width = int(screen.resolution[0]/2)+self.scale-(self.margin *2)
                height = int(screen.resolution[1])-(self.margin*2)
                stack[0].place(pos_x, pos_y, width, height)
            else:
                # these ones are not
                pos_x = -screen.border[0]+self.margin
                pos_y = screen.bar.height+self.margin
                width = int((screen.resolution[0]/2)+((screen.border[0]-self.margin)*2)+self.scale)
                height = int(screen.resolution[1]-(self.margin*2)-screen.border[1]+2)
                stack[0].place(pos_x, pos_y, width, height)

            for i in range(1, len(stack)):
                if re.findall("|".join(self.border_window_classes), win32gui.GetClassName(stack[i].hwnd)) and not any(re.findall("|".join(self.border_window_ignore), stack[i].title)):
                    # these are drawing in borders
                    x_pos = int(screen.resolution[0]/2)+self.scale+self.margin
                    y_pos = int((i-1)*(screen.resolution[1]/(len(stack)-1)))+screen.bar.height+(self.margin)
                    width = int(screen.resolution[0]/2) - self.scale-(self.margin*2)
                    height = int(screen.resolution[1]/(len(stack)-1))-(self.margin*2)

                    print(f"{stack[i].title}: [{pos_x}, {pos_y}, {width}, {height}]")
                    stack[i].place(x_pos, y_pos, width, height)
                else:
                    # these are not
                    x_pos = int(screen.resolution[0]/2) - screen.border[0]+self.scale+self.margin
                    y_pos = int((i-1)*(screen.resolution[1]/(len(stack)-1)))-1+screen.bar.height+(self.margin)
                    width = int(screen.resolution[0]/2)+(screen.border[0]*2)-self.scale-(self.margin*2)
                    height = int(screen.resolution[1]/(len(stack)-1) -(self.margin*2))-(screen.border[1]-1)

                    print(f"{stack[i].title}: [{pos_x}, {pos_y}, {width}, {height}]")
                    stack[i].place(x_pos, y_pos, width, height)

        else:
            if re.findall("|".join(self.border_window_classes), str(win32gui.GetClassName(stack[0].hwnd))) and not any(re.findall("|".join(self.border_window_ignore), stack[0].title)):
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

    def arrange(self, stack, screen, workspaces, window_ignore=[]):
        w = window.get_active_window(workspaces, window_ignore)
        for w in stack:
            if not any(re.findall("|".join(window_ignore), w.title)):
                w.maximize()
        w.focus()

    def switch():
        pass
