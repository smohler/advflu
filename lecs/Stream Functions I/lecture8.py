from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

class Lecture8_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Eight')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{Stream Functions, pt.1}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture8_scene1(Scene):
    def construct(self):
        ### Lecture notes 08 pgs. 1
        ### video 08, 0:00

        ### what is it?
        # we have been using the eulerian view point up til here. given space and time, we can supply a velocity vecotor. system of PDE's
        # now switching to a lagrangian view point. can focus on far field
        # can now regard inflow and entry regions we previously ignored
        # we are simply changing our perspective
        ### what does 'far' mean?
        # rho, mu are medium properties. do not change based on eularian or largarangian
        # we have control over u, L scales. (in regards to Re)
        # if we go far enough out our lenth scale would blow up
        ### irrotational flows/ideal flows/potential flows
        # Doesn't mean mu = 0. it means there are no imbalance in shear flows
        # unit cell of fluid does not deform
        # no net imbalance becuase the shear stress is proportional to a velocity gradient
        # boxes stay boxes

        VP = TextMobject('Viewpoints')
        VP.scale(1.5)
        VP.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(VP))

class Lecture8_scene2(Scene):
    def construct(self):
        ### Lecture notes 08 pgs. 3
        ### video 08, 31:15

        ### path stuff
        # draw body in fluid with streamlines
        # define coordinate system
        # show stagnation point, even on rear of body
        # "lagrangian paths for fluid particle"
        # consider each path as, S(x,y) = a where a is some constant. similar to eqn for a circle
        # the paths have information about the velocity.
        # draw segment of path, find slope, come to: dy = v dt, dx = u dt
        # take derivative of path: dS = 0 = (part S/part x)dx + (part S/part y)dy
        # dS/dt = da/dt = 0 = (part S/part x)dx/dt + (part S/part y)dy/dt, divide out dt
        # dy/dx = (-part S/part x)/(part S/part y) = (v dt)/(u dt)
        # we now have the relation: u = part S/part y, v = -(part S/part y) 
        # propose some stream function: phi(x,y) = a for a in all real numbers
        # very key: u = part phi/part y, v = -(part phi/ part x)
        # find one functino so give us both u, v
        # this argument breaksdown at stagnation points, there are kinks. just say v=0 at that point
        # write things in matrix form. column matrix of derivative ops defined as grad*dagger
        # grad(V) = 0. automatically satisfy continuity
        
        PS = TextMobject('Path Stuff')
        PS.scale(1.5)
        PS.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(PS))

class Lecture8_scene3(Scene):
    def construct(self):
        ### Lecture notes 08 pgs. 5
        ### video 08, 1:01:00

        ### moving on to the momentum equations
        # follow math from notes
        # transform momentum eqn interms of psi now
        # say we know psi(x,y). V = grad*dagger(psi(x,y))
        # move velocities to one side. left with pressure gradient
        # dot everything with new dagger gradient
        # write big eqn here. momentum in regars to psi
        # unsteady, convective, and viscous terms
        # units of psi are, [L^2/T]
        # big picture: we've put together a new way to describe velocties
        
        M = TextMobject('Momentum')
        M.scale(1.5)
        M.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(M))

class Lecture8_scene4(Scene):
    def construct(self):
        ### Lecture notes 08 pgs. 7
        ### video 08, 1:15:20

        ### viscous suction flow example
        # include schematic. have flow in both v and u
        # 2D, steady slot flow. fully developed
        # from continuity dP/dx = constant
        # scales: u ~ U_o, v ~ U_o, x ~ h, y ~ h, psi ~ U_o*h, v_o ~ U_o, alpha ~ v_o*Re
        # looking for psi(x,y)
        # introuce a gauge function: psi(x,y) - psi(0,0) = int(-v_0)dx + int(u)dy = -v_o*x + F(y)
        # d_psi = -v dx + u dy
        # going over a lot of math we end up with: alpha*F''' = F''''
        # solving for F(y) = soln goes here ...
        # alpha was defined as, alpha = (v_o*h)/nu, [porous flow/viscous diffusion]
        # calculating pressure gradient
        
        VSF = TextMobject('Viscous Suction Flow')
        VSF.scale(1.5)
        VSF.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(VSF))

class Lecture8_scene5(Scene):
    def construct(self):
        ### Lecture notes 08 pgs. 12
        ### video 08, 1:43:00

        ### irrotational (inviscid/potential flow/ideal flow)
        # if grad X v = 0, then v = grad of a potential function (phi)
        # this is NOT the streamfuntion definiton
        # u = part phi/part x, v = part phi/part y (no swap, no negative)
        # phi = potential function
        # from continuity, grad^2 phi = 0
        # phi is a 'harmonic' function. phi solved the laplacian eqn
        # w/ vector identities we can rewrite NVS eqns. includes cross products so we can zero stuff
        # plug in phi definition, we have assumed phi(x,y,z,t)
        # unsteady bernoulli
        ### expanding bubble problem
        # want to solve for radius as a functino of time
        # say velocity field is diverging, grad X v = 0
        # BC's: grad^2 phi = 0, (part phi)/(part r) (infty, t) = 0, (part phi)/(part r) (R, t) = R dot
        # rewrite in spherical coords
        # determine what phi must look like. write here ...
        # intigrate phi and we get gov eqn for expanding bubble
        
        PF = TextMobject('Potential Flows')
        PF.scale(1.5)
        PF.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(PF))