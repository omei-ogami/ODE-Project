from manim import *

class Graph2(Scene):

    def func(A, x):
        return (A-x)**(3/2) / (3 * np.sqrt(A)) - np.sqrt(A) * np.sqrt(A-x) + 2 * A / 3
    
    def construct(self):

        A1 = 1
        A2 = 3
        A3 = 5
        X = ValueTracker(0)
        k = ValueTracker(0)

        plane = (
            Axes(
                x_range = [-1,7,1], y_range = [-1,5,1], x_length=10.
            )
            .add_coordinates()
        )

        
        #man1 = always_redraw(lambda: Dot(color=BLUE).move_to(plane.c2p(A1, k.get_value())))
        #man2 = always_redraw(lambda: Dot(color=DARK_BLUE).move_to(plane.c2p(A2, k.get_value())))
        man3 = always_redraw(lambda: Dot(color=PURE_BLUE).move_to(plane.c2p(A3, k.get_value())))

        #dog1 = always_redraw(lambda: Dot(color=YELLOW).move_to(plane.c2p(X.get_value(), Graph2.func(A1, X.get_value()))))
        #dog2 = always_redraw(lambda: Dot(color=YELLOW_B).move_to(plane.c2p(X.get_value(), Graph2.func(A2, X.get_value()))))
        dog3 = always_redraw(lambda: Dot(color=YELLOW_D).move_to(plane.c2p(X.get_value(), Graph2.func(A3, X.get_value()))))

        #track_dog1 = TracedPath(dog1.get_center)
        #track_dog2 = TracedPath(dog2.get_center)
        track_dog3 = TracedPath(dog3.get_center)

        #track_dog1.color = YELLOW
        #track_dog2.color = YELLOW_B
        track_dog3.color = YELLOW_D

        #track_man1 = TracedPath(man1.get_center)
        #track_man2 = TracedPath(man2.get_center)
        track_man3 = TracedPath(man3.get_center)

        #track_man1.color = BLUE
        #track_man2.color = DARK_BLUE
        track_man3.color = PURE_BLUE

        
        self.add(plane, man3, dog3, track_dog3, track_man3)
        self.play(
            X.animate.set_value(5),
            ChangeSpeed(
                k.animate.set_value(10/3),
                speedinfo = {0 : 0.84}
            )
        )
        #self.wait()

    

