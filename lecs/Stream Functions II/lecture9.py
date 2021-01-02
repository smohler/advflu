from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

class Lecture9_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Nine')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{Stream Functions, pt.2}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture9_scene1(Scene):
    def construct(self):
        ### Lecture notes 09 pgs. 1
        ### video 09, 0:00

        ### recap
        # streamfunction (lagrangian view)
        # consider flow as a bunch of paths
        # 4th order PDE for psi
        # NVS eqns (eularian)
        # 2nd order system of PDE's
        # both can handle viscous flows
        # all we want to do is figure out u,v,w
        # figure out psi (streamfunction) or phi (potential flow)
        # streamfunctions can handle viscous flows, potential flows cannot
        # can only use potential flows if flows is irrotational (curl-free velocity field)
        # today we're going to be gonig into potential flows

        recap = TextMobject('Recap')
        recap.scale(1.5)
        recap.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(recap))

class Lecture9_scene2(Scene):
    def construct(self):
        ### Lecture notes 09 pgs. 1
        ### video 09, 10:30

        ### what exactly is 2D flow?
        # means that one dimension just doesn't matter
        # slot flow --> z --> infty, w = 0
        # effectively gives us that one momentum equation is trivial (0 = 0)
        # also have some symmetry about some axis
        # cone flows, radially symmetric
        ### how can we define irrotational
        # grad X v = 0 |--> v = grad(phi) [gradient of a scale field]
        # this does not go the other way
        # evaluating in continuity we get, grad^2(phi) = 0
        # any phi must conserve mass
        # streamfunctions automatically satisfy continuity. potential flowsare not gaurenteed to do so
        ### picture of aerofoil in 2D flow w/ streamlines
        # if we disperse small boxes within the flow we do not see any deformation
        # regarless of free stream flow no slip must hold, always
        # zooming out, the dynamics of the aerofoil fade out. everything smoothes out
        ### flow is irrotational when?
        # 1) no net viscous shear forces. grad X v = picture. large value means very rotational flows. small values mean non-rotating flows
        # 2) viscosity = 0
        # 3) L--> infty and there are no comparable obstructions around 
        # we are also assuming steady flows

        PF = TextMobject('Potential Flows')
        PF.scale(1.5)
        PF.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(PF))

class Lecture9_scene3(Scene):
    def construct(self):
        ### Lecture notes 09 pgs. 3
        ### video 09, 40:15

        ### complex numbers
        # draw 2D cartesian plane
        # R = ssqrt(x^2 + y^2)
        # P = (R*cos(theta), R*sin(theta))
        ### draw a complex 2D plane
        # complex value, z, is just a single value unlike real numbers where there are two
        # z = x + iy = r*e^(i theta) [euleiar eqn]
        # ideal flow: V = grad phi
        # complex potential flow: F(z) = phi(x,y) + i psi(x,y). involves a streamfunction
        # streamfunction can capture viscid and inviscid flows while the potential function can only describe inviscid
        ### complex velocity
        # write down complex velocity eqn here. dF/dz = ...
        # symmetric statement
        # call complex velocity some w(z) = u - iv = q*e^(-i alpha) [cartesian, polar]
        ### draw diagram of flow in complex plane
        # using w(z) transforms us to a new plane where axes are now (u, -iv)
        # q = sqrt(w*w_conjugate). w = a + ib, w_conjugate = a - ib, w*w_conjugate = a^2 + b^2
        
        CN = TextMobject('Complex Numbers')
        CN.scale(1.5)
        CN.set_color_by_gradient(RED, ORANGE)

        self.play(Write(CN))

class Lecture9_scene4(Scene):
    def construct(self):
        ### Lecture notes 09 pgs. 4
        ### video 09, 55:40

        ### what does this look like
        # F(z) = i*z^2 = i*(z+iy)*(z+iy)
        # expand out, break up into imaginary and real
        # calculate dF/fz
        ### anotha one
        # F(z) = U_o*e^(-i alpha)*z
        # w = dF/dz = U_o*cos(alpha) - i*U_o*sin(alpha) = u - i*v
        # plot this solution in cartesian
        ### anotha anotha one
        # F(z) = A*z^n
        # w = n*A*z^(n-1)
        # since we have powers polar notation is superior: z = r*e^(i theta), z^n = r^n*e^(i n theta)
        # follow math
        # side thingy: if we change to polar notation then things look like, w = (v_r - i*v_theta)*e^(-i theta)
        # show what streamfunctions come out to be
        # where are stagnation points? wherever streamfunction = 0
        # psi = 0, stagnation point. will happen when theta = (k*pi)/2 for integers K, for all r
        # plug this in to rewrite V_r
        # plot/draw for different k, n
        # 1) k = 1, n = 1
        # 2) k = 1, n = 2
        # 3) k = 1, n = 1/2
        # different values of n model a very large array of different flows
        ### one more
        # F(z) = (m/2pi)*ln(z - zo), zo = 0
        # F(z) = (m/2pi)*ln(r*e^(i theta)) = (m/2pi)*(ln(r) + i theta)
        # write stream and potential functions
        # looks almost like a vortex but with radial flow, not tangential
        # sink/source flow
        ### issues
        # for example, source/sink when r = 0
        # we did not say velocity potentials always satisfy continuity, they satisfy the lapalcian eqns. very diff
        # calculate flow rate
        # have an issue where grad V =/= 0, continuity thrown out near singularities
        ### anotha one
        # F(z) = -i*(J/2pi)*ln(z - zo), circulation theory
        # v_r = 0, v_theta = J/(2pi r)
        
        W = TextMobject('What Does This Look Like')
        W.scale(1.5)
        W.set_color_by_gradient(PURPLE, BLUE)

        self.play(Write(W))

class Lecture9_scene5(Scene):
    def construct(self):
        ### Lecture notes 09 pgs. 9
        ### video 09, 1:36:00

        ### potential flows add up to new potential flows
        # final example
        # F(z) = U_o + (m/2pi)ln(z) + i*c
        # first term: plug flow at alpha = 0, second term: source flow at zo = 0, third term: allows us to move zo
        # solve velocity field: w(z) = u + (m/2pi z)
        # find where stagnation occurs
        # for streamfunction  = 0, c = -m/2
        # psi = U_o + (m/2pi)*theta + c
        # this is a model of a blunt body moving in plug flow
        # talk about generalized velocity (q^2)
        # follow math
        # plug into insteady bernoulli. q is the speed at the surface
        # follow math
        # pressure coefficient
        # plot ideal inviscid pressure coefficent curve
        # this works well for the front portion of the blunt body
        # curves don't diverge until later
        # essentially. IF IDEAL WRITE F(z).
        
        PPF = TextMobject('Properties of Potential Flows')
        PPF.scale(1.5)
        PPF.set_color_by_gradient(GREEN, BLUE)

        self.play(Write(PPF))