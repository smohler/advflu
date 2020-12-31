from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

class Lecture6_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Six')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{Advanced Flows, pt.1}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture6_scene1(Scene):
    def construct(self):
        ### Lecture notes 06 pgs. 1
        ### video 06, 0:00

        ### Breakdown
        # going to be doing 3 problems
        # 1) elliptic cross-section pipe [solving PDE's]
        # 2) Rectangular pipe [power of educated guess]
        # 3) pressure oscillations in a pipe [make math pretty]
        
        ps = TextMobject('3 Problems')
        p1 = TextMobject('Elliptic Cross-Section Pipe')
        p2 = TextMobject('Rectangular Pipe Flow')
        p3 = TextMobject('Pressure Oscillations in a Pipe')
        
        ps.shift(2*UP)
        p1.shift(UP)
        p3.shift(DOWN)

        p = VGroup(ps, p1, p2, p3)
        (p[0]).scale(1.5)
        (p[1:]).set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(p))

class Lecture6_scene2(Scene):
    def construct(self):
        ### Lecture notes 06 pgs. 1
        ### video 06, 7:11

        ### elliptic cross-section pipe
        # draw flow schematc
        # assume we are past the entrace length
        # boundary is defined by (x/a)^2 + (y/b)^2 = 1, consider z to be infinite
        # simplifying the NVS we get: 0 = (part P/ part z) + mu grad^2 (w)
        # 0 = -(part P/ part y) + rho g
        # 0 = -(part P/ part x)
        # 0 = (part u/ part x) + (part v/ part y)
        # expand out main equation, how to apply no slip?
        # w @ boundary set = 0
        # nondimensionalie: w ~ (L^2/mu)*(-dp/dz), x ~ L, y ~ L
        # we can have different length scales
        # L = {a, b, ab/(a+b), sqrt(ab), (a+b)/2}
        # we will scale Length by L = a
        # nondim equation is now: grad*^2 (w*) = -1, w* @ boundary = 0, x* + (a/b)^2 y* = 1
        # redefine (a/b) = phi
        # we have a linear PDE. the sum of two solutions is the solution of that sum: w* = w1 + w2
        # grad*^2 w* = grad*^2 w1 + grad*^2 w2
        # where w1 and w2 are simpler functions
        # we will break it up like: w* = w~ - B, grad*^2 w* = grad*^2 w~ - grad*^2 B
        # plugging in what we know: -1 = grad*^2 w~ - grad*^2 B
        # if we assume  grad*^2 B = 1, then grad*^2 w~ = 0
        # now what is actually B? it's been found, B(x,y) = c1(x*^2) + c2(y*^2)
        # grad*^2 B = 2 c1 + 2 c2, set equal to 1 like we assumed, 1 = 2 c1 + 2 c2
        # now considering how to handle the boundary: B @ wall = w~ @ wall
        # subbing in B and rearranging we get, w~ @ wall = c1(x*^2 + (c2/c1)y*^2)
        # we can now claim that (c2/c1) = (a/b)^2. we have 2 eqns and 2 unknowns and we can solve for c1/c2
        # c1 = 1/2(1 + phi), c2 = phi/2(1 + phi)
        # w* = homogenious + forcing. now solving for the homogenious solution (w~)
        # insert cool elliptical fig here. boundary is a constant value with zero curvature
        # pictures showing what the independent w~, B solutions look like, solution is,
        # w* = (1/2(1+phi))(1-x*^2-phi y*^2)
        # redimensionalize. breakdown what we can learn from this. solve for flowrate
        
        ECS = TextMobject('Elliptic Cross-Section Pipe')
        ECS.scale(1.5)
        ECS.set_color_by_gradient(BLUE, YELLOW)
        
        self.play(Write(ECS))

class Lecture6_scene3(Scene):
    def construct(self):
        ### Lecture notes 06 pgs. 6
        ### video 06, 51:00

        ### Rectangular Pipe Flow
        # include flow schematic
        # as (x/a)^n + (y/b)^n = 1 as n->infty begins to look like a square
        # we have the same gov eqn as the elliptic pipe. since duct is symmetric, we only solve one quadratic
        # apply no slip at boundarys inside quadrant one, and additional symmetry conditions
        # scales: x ~ L, y ~ L, w ~ (L^2/mu)(-dP/dz)
        # same eqns as before but with more BC's
        # w* = w~ + f(x,y) where grad*^2 (f) = -1
        # lots of different possible functions, f(x,y). show examples
        # regardless of choice, w~ will correct
        # choose, f(x,y) = (a^2/2)(1 - (y*/a)^2). now solve for w~
        # solving grad*^2 (w~) = 0, ...
        # educated guess, w~ = f(x)*g(y) search for solution of this form
        # we can also say, g''/g = -f''/f, LHS is func of y RHS is function of x
        # this is only possible if they are equal to a constant value, +- lambda^2
        # now have 2 ODEs: g'' = - lambda^2 * g, f'' = - lambda^2 * f
        # w~ = solution goes here...
        # we need to consider all the 'eigenvalues' for when this is true, 
        # w* = solution goes here, (has the sum in it), can say B = 0
        # lambda = pi*(2n - 1)/2a, n = 1,2,3,4...
        # apply BC, using fourier series --> An = big integral
        # end up with An = (2*(-1)^n)/(a*lambda^3*(1+e^(-2*lambda)))
        # we have all the parts defined to pose the solution as an infinite series
        # re-write in a hyberbolic
        # solve for flow rate,
        # explain what we can learn from this
        
        RPF = TextMobject('Rectangular Pipe Flow')
        RPF.scale(1.5)
        RPF.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(RPF))

class Lecture6_scene4(Scene):
    def construct(self):
        ### Lecture notes 06 pgs. 12
        ### video 06, 1:36:00

        ### pressure oscillations in a pipe
        # show schematic
        # ex. human heart, pumps, under-current flows
        # we have: inster gov eqn here...
        # BC's: no slip, symmetry
        # use same technique where we make use of the sum of two solutions
        # have one solution solve the steady flow, and have the other solve the time varying component
        # scales: t ~ 1/w, y ~ h
        # velocity scale? find internal scales. discuss pros and cons of either. use u ~ G/w
        # breakdown velocity scale as ratio of viscous diffusion length and slot length. sqrt(nu/w) = viscous diffusion length
        # rewrite as 1/(2*V^2), where V = H/sqrt(2 nu/w)
        # Look for a function that has the form: u*(y,t) = Re{exp(it)F(y)}
        # follow math
        # F(y) = solution...
        # take real part to get actual solution. simplify from mathematica output. redine stuff
        # see how we can limit lambda. get new solution for lambda --> 0 (small slot, fully viscous regieme)
        # see what happens as lambda blows up, just a wiggle vertical line. coool but violates no slip
        # rewrite y* as eta* to resolve in order to obey no slip: h = y + eta
        # would like to find a uniformly valid solution across the range of parameters 
        
        POP = TextMobject('Pressure Oscillations in a Pipe')
        POP.scale(1.5)
        POP.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(POP))
