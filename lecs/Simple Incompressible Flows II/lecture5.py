from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

class Lecture5_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Five')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{Simple Incompressible Flows, pt.2}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture5_scene1(Scene):
    def construct(self):
        ### Lecture notes 05 pgs. 9
        ### video 05, 0:00

        ### From last time
        # we posed paralll flow, applied scales, 
        # partial P*/ partial x* = partial^2 u*/ partial y*^2 (non-dimensional)
        # u*(o) = 0, u*(1) = u/U
        # where to get cetain scales (velocity, pressure)
        # from last time, writing out x-momentum get expression with bunch of epsilons
        # end up with H/L ~ 1/Re, l_entrance ~ D_h Re
        # want to examin large Re, but we have problems
        # big Re --> log(Re), to still be able to examine it. or even Re^(1/p)
        ### Solving the parallel flow problem
        # end up with, u*(y*) = (u/U)y* + 0.5*(dP/dx)(y*^2 - y*)
        
        review = TextMobject("Let's review")
        review.scale(1.5)
        review.set_color_by_gradeint(BLUE, YELLOW)

        self.play(Write(review))

class Lecture5_scene2(Scene):
    def construct(self):
        ### Lecture notes 05 pgs. 9
        ### video 05, 22:00

        ### Where can we find velocity scales?
        # if we had no-slip on both surfaces we could not use the BC's to find scales, uh oh
        # balance terms and non-dimensionalize and we get, u ~ (h^2/mu)*(dP/dx) (internal veloity)
        # if we have a free surface then we could also just scale by U (boundary velocity)
        # show alternate math where you get the internal velocity scale w/ lubrication approximation
        # pressure gradient has to be negative
        # substitute in scale, define as something simple (good tricks) 1/(1+phi) where phi is something
        # harp on how general this is, good stuff
        ### Quantities of interest
        # shear at a wall: tau = mu du/dy if newtonian
        # flowrate: Q = VA but if we have the field Q = int u dA
        # one we have the velocity profile we usually end up solving for these
        
        scales = TextMobject('How Can we Find Scales?')
        scales.scale(1.5)
        scales.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(scales))

class Lecture5_scene3(Scene):
    def construct(self):
        ### Lecture notes 05 pgs. 12
        ### video 05, 44:55

        ### Same problem but NOT STEADY HAHA
        # Raleigh's Probelm
        # allow y to go to infinity, plate applies impulse
        # IC: u(y,0), for t>0 u(y,t) = Uo
        # no pressure gradient
        # governing equation is rho (part u/ part t) = mu (part^2 u/ part y^2) similar to first problem
        # still liquid, no pressure gradient
        # part u/ part x = 0
        ### Where do we get out scales???
        # given the scale of the problem we are looking for a time scale that analyzes the viscous response of the fish moving through water
        # BC's IC's: u(y,0) = 0, u(y,t) = Uo, u(infty, t) = 0
        # looking for scales: u ~ Uo
        # set up scaling of two terms to obtain similarity variable
        # get, y ~ sqrt(nu * T); 1 ~ y/sqrt(nu * T)
        # we have found our new similarity variable. eta(y,t) this is the similarity variable
        # this comes from lack of a natural scale
        # we are essentially converting a PDE into an ODE. must rewrite our BC's and IC's in term of eta
        # now rewrite expression in terms of eta, ex. part/ part t = (part/ part eta)*(part eta/ part t)
        # NEW ODE: f'' + Co*eta*f' = 0, where ()' = d/d eta and f(eta) = u/Uo
        # f(0) = 1,f(infty) = 0
        # we now have 2 solutions
        # solving for f(eta), f(eta) = 1 - erf(y/(2*sqrt(nu*t)))
        
        RP = TextMobject("Raleigh's Problem")
        RP.scale(1.5)
        RP.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(RP))

class Lecture5_scene4(Scene):
    def construct(self):
        ### Lecture notes 05 pgs. 14
        ### video 05, 1:17:00

        ### Let's shake things up
        # same problem as before but lets allow the plate to SHAKE
        # bottom plate shakes like Uo*sin(wt)
        # same set up as before but different BC, u(0,t) = Uo*sin(wt) 
        # go through process for finding scales: t ~ 1/w, u ~ Uo, y* ~ y/sqrt(nu/omega)
        # non-dimensinalize
        # to solve this end up using eulers identity. look for solution like, u*(y*,t*) = f(y)*exp(i t*)
        # get form apply BC's solution goes here ---> :) 
        # viscous diffuino length can be estimated from exp() term in solution
        # explain how this can be useful

        shake = TextMobject('Shaking Things Up') 
        shake.scale(1.5)
        shake.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(shake))

class Lecture5_scene5(Scene):
    def construct(self):
        ### Lecture notes 05 pgs. 15
        ### video 05, 1:37:22

        ### Radial Vortex Flow
        # show diagram
        # near the top is the ideal flow for solution, then transitional, then a scale where viscous effects begin
        # for ideal case, v_theta = J/(2 pi r), J is a circulation value
        # as r --> 0 we have infinite velocity
        # from continuity, part v_theta / part theta = 0, swirl is not dependent on theta
        # there is no deformation of a control volume!! cool stuff
        # equation goes here -->
        # BC's: v(0, t) = 0, v(infty, t) = J/(2 pi r) ideal case 
        # IC's: v(t,0) = J/(2 pi r)
        # scale equation, balance terms, obtain similarity variable
        # 1 ~ r/sqrt(nu t), velocoty scale (comes from IC/BC): v = J/(2 pi r)
        # f'' + (eta/2 + 1/eta)*f' = 0, f(0) = 0, f(infty) = 1
        # LOOK UP SOLUTION: f(eta) = 1 - exp(-eta^2/4)
        # write down complete solution: OCEAN VORTEX BBY!!

        rvf = TextMobject('Radial Vortex FLow')
        rvf.scale(1.5)
        rvf.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(rvf))