from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

class Lecture7_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Seven')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{Advanced Flows, pt.2}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture7_scene1(Scene):
    def construct(self):
        ### Lecture notes 07 pgs. NA
        ### video 07, 0:00

        ### Recap?
        # go over key parts from advanced flows pt.1
        
        R = TextMobject('Recap')
        R.scale(1.5)
        R.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(R))

class Lecture7_scene2(Scene):
    def construct(self):
        ### Lecture notes 06 pgs. 1
        ### video 06, 15:40

        ### viscous coupling
        # include schematic (tilted viscometer thing)
        # define all variables
        # only considering swirl velocity, simplifying radial NVS and scaling we get ... [gov eqn]
        # epsilon = h/R < 1
        # chosen scales, r ~ R, z ~ h, v ~ R*w
        # BC's: v*(r*,0) = 0, v*(r*,1) = r*, v*(1, z*) = 0
        # First case (simple case): epsilon --> 0
        # v* = r*(z*), but this doesn't satisfy no-slip
        # Second case: breaking up r
        # R = r + eta, eta = R - r = R(1 - r*)
        # scale eta by h since it is smaller, eta* = R(1 - r*)/h = (1 - r*)/epsilon
        # r*(eta*) = 1 - epsilon(eta*), dr*/d eta* = -epsilon. coordinate transformation from bulk flow to viscous flow near the wall
        # gong to replace part / part r with (part / part r)(part r / part eta)
        # transformed eqn here ...
        # BC's: v*(eta*,0) = 0, v*(eta*,1) = 1, v*(0,z*) = 0
        # v*(eta* --> infty, z*) = z* = limit of first case solution with r*-->1, we get z*. symmetry/continuous kind of argument thing. Mathcing condition
        # solution goes here ... infinite sum.
        # how can we consider both inner and outer solutions?? we can't just sum
        # introduce the common part, is a part of the matching condition
        # full solution here ... (uniformly valid solution)
        
        VC = TextMobject('Viscous Coupling')
        VC.scale(1.5)
        VC.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(VC))

class Lecture7_scene3(Scene):
    def construct(self):
        ### Lecture notes 06 pgs. 6
        ### video 06, 55:30

        ### stagnation flow
        # include diagram and paramaters. blunt body in flow, steady
        # Hiemenz flow
        # lim y --> infty u(x,y) = ax
        # lim x --> infty u(x,y) = -ax + b
        # from NVS we get the gov eqution. goes here ...
        # we are looking for 2 eqns, u(x,y), v(x,y) 
        # from continuity, part u /part x = -(part v / part y)
        # integrate both sides (dx), we get u = x f'(y)
        # continuity gives us what u will LOOK like
        # we get v(x,y) = x f(y) for free
        # plug into gov eqn, goes here ... 4 BC's
        # 3rd order ODE means we need 4 BC's
        # follow math
        # move on to y-momentum
        # concude for consistancey, H(y) = -a^2
        # shown by enforcing BC
        # consider statement on H(y) to solve for f
        # non-dimensionalizing: y ~ sqrt(nu/a), F ~ sqrt(nu*a), F' ~ U_o, a ~ U_o/L
        # turns out we can't solve for F(eta) but if we could it would be applicable
        # show plots of different derivative curves of F
        # explain what we have done and how good it is. epic
        
        HF = TextMobject('Hiemenz Flow')
        HF.scale(1.5)
        HF.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(HF))

class Lecture7_scene4(Scene):
    def construct(self):
        ### Lecture notes 06 pgs. 12
        ### video 06, 1:37:00

        ### Von Karmen Pump
        # include diagram
        # draw different vlocity profiles
        # work energy theorem
        # centrifugal forces creates radial velocity
        # write equations
        # scaling to set terms to zero
        # u ~ rw, v ~ rw, W ~ sqrt(nu*w), p ~ rho w nu
        # transform in to eta* = z/sqrt(nu/w). show G, F, H, P nondimensionalizatinos
        # write 4 ODE's
        # ^^^ this is the von karmen viscous pump
        # talk about everything we can learn from this: flowrate, shear stress, ...
        # how we get these constants, 5.5, 0.886

        VKP = TextMobject('Von Karmen Pump')
        VKP.scale(1.5)
        VKP.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(VKP))