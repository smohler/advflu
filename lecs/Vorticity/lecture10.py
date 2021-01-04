from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

class Lecture10_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Ten')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{Vorticity}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

### skipped review of what has been covered in class (videos) so far. Can add in if wanted
### started when vorticity had begun being discussed

class Lecture10_scene1(Scene):
    def construct(self):
        ### Lecture notes 10 pgs. 1
        ### video 10, 0:00

        ### what is vorticity
        # w = grad X v, curl of velocity field gives the vorticity field
        # w = vorticity, v = velocity
        # material derivative of v: Dv/Dt ~ inertia, grad P ~ pressure, mu grad^2 V ~ viscous force, rho g ~ body force
        # rewrite function to include some hydraulic head
        # define new derivative operator
        # essentially forces prescribe motion. reworked linear momentum
        ### what about angular momentum?
        # 2 BIG BALLS TOUCHING
        # can't store energy in intersecting surfaces
        # L = r X P (angular momentum = radius cross linear momentum)
        # how do we measure r? doesn't really matter since we are interested in differences
        # shrinking volume the rotational vector shouldn't vanish
        # L = 1/2 *I*||w||, ||*|| = vector norm = sqrt(wx^2+wy^2+wz^2)
        ### vorticity from angular momentum 
        # w = grad X v, L = r X mV. there is a mismatch
        # m = rho*volume
        # recalling cross product rules, (a X ib) = (ia X b) = i(a X b). we can move around scalars
        # L = rho*vol(r X v), L/vol = rho(r X v)
        # must be independent of coordinate system. If placed at enter of mass it will always work
        ### Rigid body rotation
        # R is an anitisymmetric linear tensor
        # grad X () ~ R(x,y,z,t)
        # gradient and velocity define a vorticity plane which is perpendicular to both
        # grad X NVS = characterize the spiny bois = the vorticity eqn
        
        WV = TextMobject('What is Vorticity')
        WV.scale(1.5)
        WV.set_color_by_gradient(GREEN, BLUE)

        self.play(Write(WV))

class Lecture10_scene2(Scene):
    def construct(self):
        ### Lecture notes 10 pgs. 7
        ### video 10, 1:02:00

        ### the vorticity eqn
        # vorticity eqn goes here ...
        # there is no pressure term. since coord is placed at COM pressure cannot cause a rotation
        # DeRham case or something
        # Dw/Dt ~ the transport of spiny bois, w*grad(V) ~ rotational straining term, nu*grad^2*w ~ viscous shear imbalance, measure net imbalance of shear forces
        ### consider a bunch of balls on a surface. must obey no-slip but can still 'produce' vorticity
        # linear velocity at a wall must be zero, but this does not exclude it from having angular velocity
        # THINK OF A BUNCH OF PING PONG BALLZ
        ### pressure indirectly affects w
        # pressure -> velocity -> vorticity
        ### scaling vorticity eqn for small v
        # part w/part t ~ nu*grad^2*w (looks like heat eqn)
        # length scale (delta) ~ sqrt(nu t), viscous diffusion length
        # for small velocity fields, vorticity diffuses
        # d delta/dt ~ sqrt(nu/t) = nu/deta, viscous diffusion velocity
        # delta ~ nu/U_o, viscous length in suction flows
        ### vorticity straining
        # math goes here ...
        # (grad X V)(grad(V)) = ...
        # length of vorticity vector, stretching of lines, turning of lines
        # picture of ballz with a line connecting them
        
        VE = TextMobject('The Vorticity Equation')
        VE.scale(1.5)
        VE.set_color_by_gradient(RED, BLUE)

        self.play(Write(VE))

class Lecture10_scene3(Scene):
    def construct(self):
        ### Lecture notes 10 pgs. 11
        ### video 10, 1:32:00

        ### vorticity at walls
        # write vorticity eqn
        # diagram of flow near a body with vorticity field, place 'camera' near the wall and zoom in
        # expand and scale, as we zoomed in L became smalll
        # at the wall, vorticity diffuses: part w/part t = nu*grad^2*w
        # back to NVS
        # 1) (1/rho)grad P ~ nu grad^2 V = nu grad X (grad X V)
        # follow math
        # marbles spinning in plane
        # pressure assigns the boundary condition for the vorticy equation at the wall
        # grad w_wall ~ grad P along any surface
        # 
        
        VAW = TextMobject('Vorticity at Walls')
        VAW.scale(1.5)
        VAW.set_color_by_gradient(RED, WHITE)

        self.play(Write(VAW))

class Lecture10_scene4(Scene):
    def construct(self):
        ### Lecture notes 10 pgs. 17
        ### video 10, 1:53:00

        ### wing example
        # draw aerofoil, 2D flow. 
        # x, y flow only causes vorticity in the z direction
        # include plot of top/bottom vorticity along wing
        ### top half
        # have negative dP/ds portion (accelerating flow)
        # then positive dP/ds portion (deaccelerating flow)
        # dumping negative vortivity lol
        ### bottom half
        # same thing but flow accelerates for longer
        # dumping positive vorticity
        # difference between change in signs between top and bottom is a proprty of airfoil geometry
        # goal is to have net, positive vorticity on bottom of the wing
        # 2D flow becomes 3D in the wake of the flow
        
        wing = TextMobject('Vortex in the Wake of a Wing')
        wing.scale(1.5)
        wing.set_color_by_gradient(BLUE, WHITE)

        self.play(Write(wing))

class Lecture10_scene5(Scene):
    def construct(self):
        ### Lecture notes 10 pgs. 15
        ### video 10, 2:07:00

        ### Helmholtz and Kelvin
        # Helmholtz laws for inviscid flows
        # def of invs=iscid flow: grad x V = 0
        # 1) particles without vorticity stays without vorticity
        # 2) Elements of one vortex line/loop stay on it
        # 3) A vortex line/loop must be a closed curve or meet the boundary at both ends
        ### Kelvins theorem
        # come closed curve in flow
        # circulation  = eqn goes here ...
        # follow math
        # Kelvins theorem talks about the circulation that happens inside some closed curve C
        # write better in math 
        # circulation is constant for inviscid flow
        ### bath tub wing example?

        HK = TextMobject('Helmholtz and Kelvin')
        HK.scale(1.5)
        HK.set_color_by_gradient(GREEN, BLUE)

        self.play(Write(HK))