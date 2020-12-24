from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

### DIMENSIONAL ANALYSIS

class Lecture3_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Three')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{Dimensional Analysis}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture3_scene1(Scene):
    def construct(self):
        ### Lecture notes 04 pgs. NA
        ### video 03, 6:30

        ## What is it?
        # makes eqns easier to rationalize
        # helps scale eqns
        # skips solution set up (apprimation)
        # basis of experimentation
        
        why = TextMobject('Why Use Dimensional Analysis?')
        why.scale(1.5)
        why.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(why))

class Lecture3_scene2(Scene):
    def construct(self):
        ### Lecture notes 04 pgs. 1
        ### video 03, 12:00

        ## Bomb example!
        # we are a spy, lots of bomb exploding pics
        # what do we have? length scale, time scale
        # How powerful? measure energy
        # dE/dt = 0, consv. energy
        # solve for energy as a function of known parameters: E = f(t, R, ...)
        # also know density of air might matter
        # unit of energy: [M^2 L^2 / T^2]
        # combine time (t), density (rho), length (R) to get parameter with same units
        # E ~ (rho R^5)/t^2
        # take R to be a function of time, R(t) ~ (t^2 E/rho)^1/5
        # R(t) = Const.(t^2 E/rho)^1/5

        taylor_bomb = TextMobject('Taylor and the Trinity Bomb')
        taylor_bomb.scale(1.5)
        taylor_bomb.set_color_by_gradient(RED, YELLOW)

        self.play(Write(taylor_bomb))

class Lecture3_scene3(Scene):
    def construct(self):
        ### Lecture notes 04 pgs. 2
        ### video 03, 25:10

        ## Blood spatter example
        # want to determine if someone was struck based off the shape of the blood splatter
        # we have pictures of blood splatters, length scale included
        # some have a bunch of splines, # of splines (N) is something we can use
        # small drops few splines, large drops many splines
        # want to solve for N as a function of parameters
        # params: length scale, velocity (dropping), mu, rho, sigma (surf tension)
        # N has no units
        # write out units of all params
        # rho = [M/L^3], sigma = [M/T^2], mu = [M/T L], d = [M], V = [M/T]
        # chose d as length scale, divide all params by d. Goal is to eliminate the primary dimension of length
        # further non-dimensionalize blah blah
        # N ~ f(Re, We) Reynolds and Webber bby!
        # run experiments (3D plot?), conclude Re doesn't matter  
        # N = We^0.5. remove fluidic constants and make only a function of velocity
        # plug in numbers, become sherlock
        # find paper to reference

        blood = TextMobject('The Blood Splatter Calamity')
        blood.scale(1.5)
        blood.set_color_by_gradient(RED, YELLOW)

        self.play(Write(blood))

class Lecture3_scene4(Scene):
    def construct(self):
        ### Lecture notes 04 pgs. 4
        ### video 03, 55:00

        ### Buggy boy example!
        # do bugs with more legs swim faster?
        # balance, more legs more mass
        # important parameters: number of legs (N), density of fluid, bug length, weight of each leg, velocity, weight of body, power of 1 leg
        # weight of bug = # legs (leg weight + body unit weight)
        # power = F*V = A*P*V 
        # power per leg ~ (rho L^2 V^3)/N
        # forece scales ~ rho L^2 V^2 = mg (weight) = rho L^3 g (beuyoncy)
        # length ~ L, time ~ L/V, mass ~ rho l^3
        # N = f( [N*P/rho L^2 V^3], [N*(Wb + Wl)/rho L^3 g], [Re^-1 Fr^-2] )
        # divide through by N, consider coefficient of drag: Cd = f(Re, Fr)
        # after dividing through we see each term must be effectively a constant
        # a0 ~ (N*P)/rho L^2 V^3, a1 ~ (N*(Wb + Wl)/ rho L^3 g)
        # turns out, V ~ Co*N^(1/9)
        # cons: doesn't work well for normal bugs
        # cons: tons of physical arguments, hand wavey, neglect Re, Fr, why were inputs constant

        bug = TextMobject('Buoyant Bugs')
        bug.scale(1.5)
        bug.set_color_by_gradient(RED, YELLOW)

        self.play(Write(bug))

class Lecture3_scene5(Scene):
    def construct(self):
        ### Lecture notes 04 pgs. 7
        ### video 03, 1:23:12

        ### Viscosity
        # sigma = mu*grad(V), where does mu come from, when does this stop being true
        # [m/T^2 L] = mu [u/L], m = [rho L^3]
        # rho [L^2/T^2] = mu [u/L] --> nu = [mu/rho] = [u*L]
        # moving to NVS
        # non-linearity comes from material verivative of V
        # rho DV/Dt = rho {part V/part t = (V*grad)*V}, nonlinear term is (V*grad)*V
        # if incomporessible then (grad*V) = 0
        # follow math in notes from here, pages 8-9
        # Kolomogorove scales
        # nondsimensionalize the incompressible NVS
        # ADD HT PROBLEM FROM NOTES??

        visc = TextMobject('Viscosity')
        visc.scale(1.5)
        visc.set_color_by_gradient(RED, YELLOW)

        self.play(Write(visc))



