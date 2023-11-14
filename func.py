from manim import *

class Graph2(Scene):

    def func(A, x):
        return (A-x)**(3/2) / (3 * np.sqrt(A)) - np.sqrt(A) * np.sqrt(A-x) + 2 * A / 3
    
    def construct(self):

        A1 = 1
        A2 = 3
        A3 = 5
        X1 = ValueTracker(0)
        k1 = ValueTracker(0)
        X2 = ValueTracker(0)
        k2 = ValueTracker(0)
        X3 = ValueTracker(0)
        k3 = ValueTracker(0)

        plane = (
            Axes(
                x_range = [-1,7,1], y_range = [-1,5,1], x_length=10.
            )
            .add_coordinates()
        )

        
        man1 = always_redraw(lambda: Dot(color=BLUE).move_to(plane.c2p(A1, k1.get_value())))
        man2 = always_redraw(lambda: Dot(color=DARK_BLUE).move_to(plane.c2p(A2, k2.get_value())))
        man3 = always_redraw(lambda: Dot(color=PURE_BLUE).move_to(plane.c2p(A3, k3.get_value())))

        dog1 = always_redraw(lambda: Dot(color=YELLOW).move_to(plane.c2p(X1.get_value(), Graph2.func(A1, X1.get_value()))))
        dog2 = always_redraw(lambda: Dot(color=YELLOW_B).move_to(plane.c2p(X2.get_value(), Graph2.func(A2, X2.get_value()))))
        dog3 = always_redraw(lambda: Dot(color=YELLOW_D).move_to(plane.c2p(X3.get_value(), Graph2.func(A3, X3.get_value()))))

        track_dog1 = TracedPath(dog1.get_center)
        track_dog2 = TracedPath(dog2.get_center)
        track_dog3 = TracedPath(dog3.get_center)

        track_dog1.color = YELLOW
        track_dog2.color = YELLOW_B
        track_dog3.color = YELLOW_D

        track_man1 = TracedPath(man1.get_center)
        track_man2 = TracedPath(man2.get_center)
        track_man3 = TracedPath(man3.get_center)

        track_man1.color = BLUE
        track_man2.color = DARK_BLUE
        track_man3.color = PURE_BLUE


        g1 = VGroup(man1, dog1, track_dog1, track_man1)
        g2 = VGroup(man2, dog2, track_dog2, track_man2)
        g3 = VGroup(man3, dog3, track_dog3, track_man3)

        self.add(plane)
        self.add(g1, g2, g3)
        curve1 = g1.copy()
        self.play(
            X1.animate.set_value(1),
            X2.animate.set_value(3),
            X3.animate.set_value(5),
            ChangeSpeed(
                AnimationGroup(
                    k1.animate.set_value(2/3),
                    k2.animate.set_value(2),
                    k3.animate.set_value(10/3),
                ),
                speedinfo = {0 : 0.84}
            ),
            subcaption_duration = 12
        )
        '''
        self.add(curve1, g2)
        self.play(
            
            X2.animate.set_value(3),
            ChangeSpeed(
                k2.animate.set_value(2),
                speedinfo = {0 : 0.84}
            )
        )
        self.add(       man1, dog1, track_dog1, track_man1, 
                        man2, dog2, track_dog2, track_man2,
                        man3, dog3, track_dog3, track_man3
                )
        self.play(
            X3.animate.set_value(5),
            ChangeSpeed(
                k3.animate.set_value(10/3),
                speedinfo = {0 : 0.84}
            )
        )
        '''
        self.wait()
        self.add(curve1)
        #self.wait()

    

