from gi.repository import Gtk, Gdk, GObject
import cairo

from point3d import Point3D

class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()
        
        self.init_ui()
        self.width = self.get_size()[0]
        self.height = self.get_size()[1]
        self.angleX, self.angleY, self.angleZ = 0, 0, 0
        
    def init_ui(self):    

        self.darea = Gtk.DrawingArea()
        self.darea.connect("draw", self.on_expose)
        #self.darea.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)        
        self.add(self.darea)
        self.coords = []
        self.xy = []
        
        self.vert = [[1,1,1],[-1,1,1],[1,-1,1],[1,1,-1],[-1,-1,1],[-1,1,-1],[1,-1,-1],[-1,-1,-1]]
        for i in self.vert:
            self.coords.append(Point3D(i[0],i[1],i[2]))
        
        #self.darea.connect("button-press-event", self.on_button_press)

        self.set_title("Lines")
        self.resize(640, 480)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        
    
    def on_expose(self, widget, event):

        cr = widget.get_property('window').cairo_create()
        rect = self.darea.get_allocation()

        cr.set_source_rgb(0, 0, 0)
        cr.set_line_width(0.5)
        
        for v in self.coords:
            r = v.rotateX(self.angleX).rotateY(self.angleY).rotateZ(self.angleZ)
            p = r.project(self.width, self.height, 256, 4)
            x, y = p.x, p.y
            self.xy.append([x,y])
        
        cr.move_to(self.xy[0][0], self.xy[0][1])
        cr.line_to(self.xy[1][0], self.xy[1][1])
        cr.stroke()
        cr.move_to(self.xy[0][0], self.xy[0][1])
        cr.line_to(self.xy[2][0], self.xy[2][1])
        cr.stroke()
        cr.move_to(self.xy[0][0], self.xy[0][1])
        cr.line_to(self.xy[3][0], self.xy[3][1])
        cr.stroke()
        cr.move_to(self.xy[5][0], self.xy[5][1])
        cr.line_to(self.xy[1][0], self.xy[1][1])
        cr.stroke()
        cr.move_to(self.xy[5][0], self.xy[5][1])
        cr.line_to(self.xy[3][0], self.xy[3][1])
        cr.stroke()
        cr.move_to(self.xy[5][0], self.xy[5][1])
        cr.line_to(self.xy[7][0], self.xy[7][1])
        cr.stroke()
        cr.move_to(self.xy[4][0], self.xy[4][1])
        cr.line_to(self.xy[1][0], self.xy[1][1])
        cr.stroke()
        cr.move_to(self.xy[4][0], self.xy[4][1])
        cr.line_to(self.xy[2][0], self.xy[2][1])
        cr.stroke()
        cr.move_to(self.xy[4][0], self.xy[4][1])
        cr.line_to(self.xy[7][0], self.xy[7][1])
        cr.stroke()
        cr.move_to(self.xy[6][0], self.xy[6][1])
        cr.line_to(self.xy[2][0], self.xy[2][1])
        cr.stroke()
        cr.move_to(self.xy[6][0], self.xy[6][1])
        cr.line_to(self.xy[3][0], self.xy[3][1])
        cr.stroke()
        cr.move_to(self.xy[6][0], self.xy[6][1])
        cr.line_to(self.xy[7][0], self.xy[7][1])
        cr.stroke()

        self.xy = []
                         
    def change(self):
                
        self.angleX +=1
        self.angleY +=1
        self.angleZ +=1
        self.queue_draw()
        return True
        #self.on_draw()
            
    def animate(self):
        GObject.timeout_add(10, self.change)
                                                        
    
def main():
    
    app = Example()
    app.animate()
    Gtk.main()
        
        
if __name__ == "__main__":    
    main()
