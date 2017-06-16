from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import random
from kivy.clock import Clock
from kivy.uix.widget import Widget

class GameFloatLayout(FloatLayout):
    def on_touch_down(self, touch):
        if self.ids.cuswid.collide_point(touch.x,touch.y):
            print(self.ids.cuswid.pos)
            pos = self.ids.cuswid.pos
            lblscore = self.ids.lblscore.text
            highscore = int(lblscore.split(' : ')[1])
            print highscore
            pressscore = abs(pos[1]-pos[0])
            print 'press at',pressscore
            if pressscore < highscore:
                if pressscore < 10 and pressscore > 0:
                    self.ids.hint.text = 'getting close!!'
                elif pressscore == 0:
                    self.ids.hint.text = 'you win!!! giwh'
                lblscore = lblscore.split(' : ')[0]+' : '+str(pressscore)
                print('out',lblscore)
                self.ids.lblscore.text = lblscore
    def movewid(self, *args):
        lblequal = self.ids.lblequal
        lblequal.color = [random.random(),random.random(),random.random(),1]
        pos = self.ids.cuswid.pos
        pos[0] += 1
        self.ids.lblx.text = 'x ='+str(pos[0])
        self.ids.lbly.text = 'y ='+str(pos[1])
        if pos[0] > self.width:
            pos[0] = 0

class Ball(Widget):
    pass

class BallGame(Widget):
    pass
            

class UnamedApp(App):
    def on_pause(self):
        return True
    def build(self):
        game = GameFloatLayout()
        Clock.schedule_interval(game.movewid, 1.0/60.0)
        return game

if __name__ == '__main__':
    UnamedApp().run()
