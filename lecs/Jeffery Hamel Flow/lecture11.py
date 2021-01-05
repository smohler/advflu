from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

class Lecture11_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Eleven')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{Jeffery-Hamel Flow}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture11_scene1(Scene):
    def construct(self):
        ### Lecture notes 11 pgs. 1
        ### video 11, 0:00

        ### what dies jeffery-hamel flow (JHF) have
        # great scaling arguments
        # radial problem
        # non-linear ODE
        # great analytical methods
        # Elliptic integral
        # assymptotic solutions
        # boundary layer problem
        # integral boundary condition
        # great analysis of integral methods
        
        WSG = TextMobject('Jeffery-Hamel Flow: Why so Cool')
        WSG.scale(1.5)
        WSG.set_color_by_gradient(BLUE, PURPLE)

        self.play(Write(WSG))

class Lecture11_scene2(Scene):
    def construct(self):
        ### Lecture notes 10 pgs. 1
        ### video 10, 9:30

        ### what does JHF look like
        # draw schematic of wedge flow
        # flow going into or out of a wadge, inflow ~ negative, outflow ~ positive
        # apply symmetry
        # alpha ~ half wedge angle, L ~ length of plate, W ~ width into and out of the board, W --> infty
        # assume steady state
        # moving to continuity, look up radial gradient operator
        # theta ~ alpha, r ~ L, z ~ W (goes to 0)
        # nondimensional gradient operator
        # we can show that flow will be purely radial. use continuity
        # "continuity solves for velocity relations"
        # write radial continuity with V_z = 0 
        # scale eqn with V_r ~ U_o, V_theta ~ V_o, r ~ L, theta ~ alpha
        # V_o ~ alpha U_o
        # alpha, [0, pi)
        # is alpha is small then, for example, we could say " V_o is 10% of U_o"
        # V = (V_r, 0, 0) with small alpha
        ### more nondimensionalization
        # schematic showing purely radial flow vectors
        # V_r ~ U_o. We are searching for U_o
        # from continuity, (part/part r)*(r V_r) = 0
        # this means that r*V_r = f(theta), V_r = f(theta)/r
        # the furthest away we can be from the wall is at theta = 0, choose our scale to be: U_o ~ f(0)/r = Co/r
        # V* = V_r/U_o = f(theta)/Co. V* = F(eta), eta = theta/alpha
        ### using momentum
        # write out term by term
        # write out full eqns (radial, swirl momentum eqns)
        # to eliminate pressure, use streamfunctions babay!
        # partial of theta mom, theta. partial of swirtl mom, r
        # follow math
        # inertial and viscous terms
        # nondimensionalize this eqn
        # Re = (U_o r alpha)/nu = (alpha Co)/mu
        # get the JHF gov eqn
        # technically this is a solution, just need to solve
        # BC's: F(0) = 1, F(+-1) = 0, 
        # can also pose symmetry boundary conditions. F'(0) = 0, F(1) = 0
        # can make a flow rate BC: Q = int_{-alpha}_{alpha}(V_r * r d_theta)
        # do math
        # different ways to solve: 1)numerical soln, 2)Analytical [elliptic integral], 3)Approximate soln [assymptotic soln]
        # explain what the pros/cons of each method are
        # going with an analytical soln
        
        look = TextMobject('What Does JHF Look Like?')
        look.scale(1.5)
        look.set_color_by_gradient(YELLOW, RED)

        self.play(Write(look))

class Lecture11_scene2(Scene):
    def construct(self):
        ### Lecture notes 10 pgs. 8
        ### video 10, 1:11:00

        ### solving analytically
        # for terms like, F(x)*F'(x) = (1/2)(dF^2/dx)
        # drop the order of the eqn with fancy substitution
        # new eqn must be equal to a constant
        # multiply by F' to drop order once again
        # integrate using symmmetry BC's
        # obtain implicit solution, solve for C using BC's
        # from here NOW transition to numerical integrations
        # plotting C as a function of Re. There is a limit for positive Re
        # no solutions for alpha*Re > 10.31
        ### what did we learn
        # 1) for pi/2<alpha<pi and Re > 0 there are NO SOLUTIONS
        # 2) for pi/2<alpha<pi and Re < 0 there are SOME soultions
        # 3) for alpha<pi/2 and Re < 0 there are ALL SOLUTIONS
        # 4) for alpha<pi/2 and Re > 0 there are SOME solutions if alpha*Re < 10.31
        
        A = TextMobject('Analytic Solution')
        A.scale(1.5)
        A.set_color_by_gradient(BLUE, GREEN)

        self.play(Write(A))

class Lecture11_scene3(Scene):
    def construct(self):
        ### Lecture notes 10 pgs. 17
        ### video 10, 1:50:30

        ### approximate solution
        # Write initial non-linear gov eqn here ...
        # as Re -->0. Say it looks like some easy problem plus a correction term
        # F ~ sum_{k=1}_{infty} F_k *Re^k, for when Re<1
        # follow math
        # lots o math
        # we break up into orders, O(1), O(Re), (Re^2)
        # must also expand BC's
        ### solving zeroth order term.
        # write down here ...
        # solve for O(Re) term
        # explain basics of asympototics
        
        B = TextMobject('Approximate Solution')
        B.scale(1.5)
        B.set_color_by_gradient(GREEN, BLUE)

        self.play(Write(B))

class Lecture11_scene4(Scene):
    def construct(self):
        ### Lecture notes 10 pgs. 20
        ### video 10, 2:09:30

        ### what about Re --> -infty
        # dividing gov eqn by Re. replace (1/Re) with epsilon
        # we now have the smallest number on the highest order term
        # show polynomial example: singular, non-singular
        # we must rescale to remove this
        # durign fast flow it looks like plug flow but there is a small viscous regieme
        # utilize the viscous length scale. show how we zoom in using tsi scale
        # show math
        # tsi = sqrt(Re*alpha)(1 - eta)
        # we now have a new independent variable. rescale
        # we still have no slip and limit terms, matching conditions
        # also derivative conditions
        # bust out the hyperbolics
        # F_out + F_inner - F_common = F_uniform
        # big issues if Re becomes positive

        C = TextMobject('What Happens as Reynolds Increases for Inflow')
        C.scale(1.2)
        C.set_color_by_gradient(PURPLE, BLUE)
        
        self.play(Write(C))