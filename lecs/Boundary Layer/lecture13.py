from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

class Lecture13_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Thirteen')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{The Boundary Layer}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture13_scene1(Scene):
    def construct(self):
        ### Lecture notes 13 pgs. 1
        ### video 13, 0:00

        ### the bundary layer
        # entrence regions
        # imagine with potential flow
        # can appear in different places: entry flow (pipe), flat plate, wing
        # include figures
        # boundary layer ends at seperation
        # inside BL grad X V =/= 0
        ### what to know
        # 1) boundary layer happens close to a surface
        # 2) delta(x) has to do with intertial/viscous battle delta = f(Re)
        # 3) boundary layer matches the inviscid and viscous flows
        ### inviscid mathing principle
        # write NVS, normalize pressure by dynamics pressure, steady flow
        # nondim gov eqn, Re = (U_o L)/nu
        # scales chosen to make Re large, 1/Re --> 0
        # rescale for inner equations (asymptotics)
        # eta/sqrt(Re) = y
        ### external inviscid flow (aerofoil)
        # include diagram
        # write continuity and NVS eqns (2D)
        # scales: P ~ rho U_o^2, x ~ L, y ~ delta, u ~ U_o
        # use dynamic pressure scale since we are assuming large Re (be consistent)
        # find u, v, p
        # use continuity to find perpendicular velocity scale, V_o ~ (delta/L)*U_o
        # during boundary layer seperation, delta --> infty. V_o scale breaks down
        # useing scales to nondim, write out term coeffs (x-mom, y-mom)
        # write the orders of the terms, O-notation
        # inertial, pressure, viscous: how to balance inertial and viscous
        # inertia is order one, viscous terms has 1/Re as Re-->infty. problem
        # rescale second term to avoid this (x-mom). 1/Re = (delta/L)^2
        # can achieve an order one term if we get this to hold (delta/L) ~ 1/sqrt(Re)
        # carry this scale to the y-mom eqn, divide by 1/sqrt(Re)
        # as Re -> infty everything checks out
        # write down simplified expressions ...
        ### What is delta, we must find it agrr
        # BC's u(x,0) = v(x,0) = 0, u(x,infty) = U_o
        # IC's u(0,y) = g(y) *some function, incoming velocity profile*
        # what do we know
        # i. steady state, ii. delta << L, iii. Re^(-1/2) << 1, iiii. smooth surface, iiiii. g(y) can't have zero shear
        ### outter flow solution
        # write expression here, only function of x
        # do some math thing to rewrite: f*f' = 1/2 *f''
        # changes in speed are attributed to changes in pressure
        # dP/dx < 0, accel flow 
        # dP/dx > 0, decel flow
        ### seperation
        # draw figure to show seperation
        # after seperation is the wake
        # backflow occurs then (rotational wake)
        # curve has zero first derivative at surface
        # zero shear at wall at point of seperation
        # stuff stops working past here

        BL = TextMobject('The Boundary Layer')
        BL.scale(1.5)
        BL.set_color_by_gradient(RED, YELLOW)

        self.play(Write(BL))

class Lecture13_scene2(Scene):
    def construct(self):
        ### Lecture notes 13 pgs. 10
        ### video 13, 1:29:00

        ### streamfunction approach
        # write u, v stream function definition
        # write gov streamfunctino eqn here ...
        # scales: x~ L, y ~ delta, psi ~ u(x)*delta(x)
        # follow math ...
        # need to keep simplifying, we have yet to eliminate a coordinate
        # f(eta) IF alpha and beta are constants
        # more math, get eqn for delta
        # say 2*alpha - beta = 1. get multiple cases
        # beta = -+ stuff...
        # write down conditionals
        # full f(eta) eqn with BC's
        # m = 0, blasius flat plate
        # m < 1 flow on wedge
        # m = 1 heimenz
        # 1 < m < 2 flow in corner
        # m < -1 Jeffery Hamel Re -> -infty w/ BL on walls

        SA = TextMobject('Streamfunction Approach')
        SA.scale(1.5)
        SA.set_color_by_gradient(GREEN, BLUE)

        self.play(Write(SA))



