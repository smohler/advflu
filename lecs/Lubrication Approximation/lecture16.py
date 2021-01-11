from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

class Lecture16_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Sixteen')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{The Lubrication Approximation}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture16_scene1(Scene):
    def construct(self):
        ### Lecture notes 16 pgs. 1
        ### video 16, 0:00

        ### Scales
        # Is all about length scale being scale
        # when Nu really big, stokes flow
        # if U slow, creeping flow
        # lubrication is a statement about small length scale
        ### thin slots
        # draw thin slot, but we have a surface function
        # bottom plate is moving, gap height is a function of position
        # if constant then couette flow
        # h(x) ~ h_o
        # or this to work we need, h_o/L = epsilon -> 0 and Re is moderate
        # Re = inertia/viscous = write in differential form oooh fancy
        # y ~ h_o, x ~ L, sub in scales
        # augmented Re, Re*epsilon^2
        # epsilon can make high Re 'moderate'
        ### irl example
        # give values and show math
        ### assumptions
        # 2D, SS
        # mini schematic, write out eqns
        # x ~ L, y ~ h_o
        # u, v, P ~ ???
        # u ~ U_o (sliding of plate)
        # use continuity to solve for v scale
        # solve for pressure scale
        # since flow is viscous dominated we can choose to scale by (mu*U_o)/(epsilon*L)
        # epsilon i spressure sale causes problems
        # v ~ epsilon*U_o
        # term by term we get ... (x,y mom)
        # let epsilon ->0 as Re < infty, pressure scale comes from forcing to be order one
        # comes about because something has to be driving the motion in limit
        # write gov, 2D eqns
        # write dp/dx since (part p/part y) = 0
        # h(x) makes theory different
        # draw schematic w/ flowrate
        # show how to consider h(x)
        # Q = int_{0}_{h(x)} u dy = const at any x
        # write u(y)
        # show flowrate, Q, now solve for dp/dx
        # this tells us some critical pressure exists
        # find pressure through integration
        # P(L) = P_o, solve for flowrate again. gives us characteristic height
        # dp/dx (x) = new expression ...
        #  dp/dx (x_crit) = 0 when h(c_crit) = H
        # pressure graph
        # have made no assumptions on h(x), dope
        # now to make an assumption lol
        # make h(x) = delta*(x - a) [linear]
        # show schematic
        # more math
        ### how to write a line
        # h(x) eqn in terms of inlet and outlet heights
        # sub into pressure eqn
        # net pressure. integrate pressure from 0 to L
        # big expression
        # everything expressed in terms of this K = h1/h2
        # do same thing for shear force
        # tangential forces to parallel forces (shear/pressure ratio)
        # coefficient of friction
        #  x_crit = more math ...
        # tells us where max pressur occurs
        # explain
        ### journal bearing
        # diagram
        # u = r*omega
        # what is the load bearing capacity of this with the fluid in there
        ### going 3D babay
        #diagram
        # write 3 scaled eqns
        # h(x) is replaced with some surface. this top surface is solid. RIGID BODY
        # doesn't dance or wiggle or do anthing cool
        # can use to supply boundary conditions
        # can integrate continuity
        # integration stuff
        # show outcome
        # lotso math, not somuch concepts but application/analysis
        # what is this solving for? pressure field
        ### viscous adhesion
        # if we have a flat plates, solve for delta*P
        # scales tell us pressure gradient is ~ to one over gap length CUBED
        # diagram
        # beer pong hehe
        # Re ~ large because of U_o
        # epsilon^2*Re <<1 if epsilon <<1
        # issue of heat!!
        # energy ~ work done by friction (viscous) + heat
        # viscoisity becomes a function of temperature which is a function of time
        # all we have to account for this in the eqn is simply plug it in
        ### redoing same problem 
        # constant viscosity
        # ramped (linear) gap
        # follow math
        # non-dim pressure function
        
        S = TexMobject('Scales')
        S.scale(1.5)
        S.set_color_by_gradient(RED, PURPLE)

        self.play(Write(S))