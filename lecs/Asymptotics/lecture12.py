from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

class Lecture12_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Twelve')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{Asymptotic Methods}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture12_scene1(Scene):
    def construct(self):
        ### Lecture notes 12 pgs. 1
        ### video 12, 00:00

        ### history
        # algebra -> calculus -> computation -> repeat
        # from calculus cam asmptotics
        # "calculus of approximation"
        # asymptotics <-> computation
        # supply further motivation
        ### aries function
        # say y = sum_{n=0}_{infty} A_n*x^n
        # A(n) = ?
        # come to, y = C1 Ai(x) + C2 Bi(x)
        # relate it to (d^2y/dx^2) - y = 0 having clean soultion
        # Ai(x) = sum_{n=0}_{infty} A_n*x^n
        # Bi(x) = sum_{n=0}_{infty} B_n*x^n
        # how many terms do we need?
        # we can say Ai ~ (mathy thingy) as x->infty, Bi ~ (mathy thingy) as x->infty
        # show plot to show accuracy
        # we get an idea of the form of these expressions
        # asymptotics come with qualifiers
        ### bessel functions
        # write diff eqn
        # make same assumption about infinite sum
        # write out what we get ...
        # take alpha = 0, show asymptotic expansion for x->infty
        # we need 10 terms of the infinite series to get <10% for x = 5
        # 1 term of asymptotic series to get 0.001% for x > 5
        
        H = TextMobject('A Brief History')
        H.scale(1.5)
        H.set_color_by_gradient(ORANGE, WHITE)

        self.play(Write(H))

class Lecture12_scene2(Scene):
    def construct(self):
        ### Lecture notes 12 pgs. 1
        ### video 12, 44:50

        ### background
        ### compare two functions f(x), g(x) for x in D
        ### big O
        # write out in fancy math but, for K less than infty, |f(x)|<=|g(x)| for 0 <|x-x_o|<delta
        # f(x) = O(g(x)), saying that both functinos are of the same order
        ### lil o
        # we say f(x) = o(g(x)) if for anuy epsilon > 0
        # |f(x)| <= epsilon|g(x)| for 0<|x-x_o|<delta
        # f(x) = o(1) = o(500) = o(10^10)
        # lim x->x_o f(x) = 0
        # big Oand lil o are different base off how they are bounded
        # big O is saying lim x->x_o f(x)/g(x) = K
        # lil o is saying lim x->x_o f(x)/g(x) = 0
        # if k=1, f(x) ~ g(x), can't say anything if k-> infty
        ### example
        # sin(epsilon*x) = O(1) as -> infty
        # but d/d_epsilon sin(epsilon*x) = x*cos(epsilon*x)
        # follow math but essentially, = O(0)
        # x*sin(1/x) = o(x) as x->0
        # take derivative with respect to x, = O(dx/dx) = O(1)
        # f(x) = O(g(x))
        # in genreral ... int f(x) dx =/= O(int g(x) dx)
        # ln(z) = O(z^p) as z->infty for p>0
        # |ln(z)| <= k|z^p| for z-> infty
        # Big Oh --> lil o (big O implies lil o, not the other way around)
        ### transitivity
        # O() is transitive (big oh)
        # if g = O(g)and g = O(h) then f = O(h)
        
        B = TextMobject('Background')
        B.scale(1.5)
        B.set_color_by_gradient(GREEN, BLUE)

        self.play(Write(B))

class Lecture12_scene3(Scene):
    def construct(self):
        ### Lecture notes 12 pgs. 3
        ### video 12, 1:04:00

        ### gauge functions
        # {f_i(x)}^{infty}_i = 0 = {f1(x), f2(x), ..., fn(x)}
        # Assymptotic sequence {delta_i(epsilon)}^{infty}_i = 0
        # called gauge functions if (write math form) but the next one goes to zero faster then the previous
        # write in lil o notation
        # write list of gauge functions here ...
        # they all need qualifiers
        # we have many infty lists of functions that satisfy this def
        ### using them
        # assymptotic sum, take list of some functino and multiply them by a set of coefficients
        # write in mathy way here
        # say f(x) = asymptotic sum plus lil o notation of next term
        # f(x) ~ sum an*delta_n(x) as epsilon -> epsilon_o
        # expanssions are NOT unique, coefficients ARE
        # how to find coefficients? come from limit definitions for each term
        ### multivariable issue 
        # f(x, epsilon) ~ new form. coefficients become functions. now use BIG O
        ### convergent series vs asymptotic series
        # convergent: every term after N is smaller than the pervious
        # asymptotic: sum CAN be divergent, closeness of approx is controlled by delta_n and x -> x_o
        # every convergent is an asymptotic series but not every asymptotic series is a convergent series
        # write down fundamental theorm/conjecture
        
        GF = TextMobject('Gauge Functions')
        GF.scale(1.5)
        GF.set_color_by_gradient(RED, BLUE)

        self.play(Write(GF))

class Lecture12_scene4(Scene):
    def construct(self):
        ### Lecture notes 12 pgs. 9
        ### video 12, 1:27:10

        ### root finding
        # x^3+3x-3*epsilon = 0, find x
        # we're finding x(epsilon)
        # refer to quadratic eqn with c = epsilon
        # pick gauge function x_n*epsilon^n
        # missing qualifier haha. as epsilon -> 0
        # x(epsilon) = x_o + epsilon*x_1
        # plug this into eqn
        # plug in x(epsilon) = x_o + epsilon*x_1 into polynomial for x
        # write out substituted form, collect terms. will check out on my end to show actual math
        # to be true both terms must be equal to zero
        # solve roots from these equations (for x_o = 0)
        ### naive expansion
        # delta_n(epsilon) = epsilon^n as epsilon -> 0
        
        RF = TextMobject("Root Finding")
        RF.scale(1.5)
        RF.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(RF))

class Lecture12_scene5(Scene):
    def construct(self):
        ### Lecture notes 12 pgs. 10
        ### video 12, 1:48:30

        ### differential equations
        # We can always say (mathy here) ...
        # solve eqn: f'' + epsilon*f' + f^4 = 0 for epsilon <<1
        # or: epsilon*f' + (f^4)'' = 0 as epsilon -> infty
        # or: f''' - f^2 - epsilon*f'' = 0 as epsilon->1 (delta(x) = (1-epsilon)^n)
        # These are all REGULAR
        ### singular
        # epsilon*f'' + ff' = 0, epsilon ->0
        # or: (1-epsilon)(f')^2 - f^3 = 0, epsilon ->1
        # write other examples here ...
        # SINGULAR: small term kills highest order term
        ### polynomial example
        # what if we had, epsilon*x^3 +x^2-1 = 0, as epsilon->0
        # we are going to lose a root
        # how to fix? rescale the problem
        # Y = M*x, M is magnification term. y/M = x
        # substitute this new expression for x
        # becomes balancing act. Decide which terms to balance
        # say first and third balance get, m  = epsilon^-1/3
        # write rebalanced eqn. didn't work balance other 2 scales
        # we get epsilon ~ M, rewrite. divide through by epsilon^2
        ### another singular example
        # linear ODE, write down eqn...
        # use naive series
        # zeroth order eqn easy (evaluate as epsilon->0)
        # solution for zeroth order term singularity blows up. we get u(0) = 1.whaaaaaat
        # rescale the problem: u(y,epsilon) = u_o(y) + u_i(eta) - f_o + O(epsilon)
        # break solution off into inner, outer, and common parts
        # eta = y/M, substitute in, multiply through by M. want order one so epsilon = m
        # new problem becomes ...
        # surprise variable pops up from matching condition, solve with limits
        # write final zeroth order soln
        
        DE = TextMobject('Differential Equations')
        DE.scale(1.5)
        DE.set_color_by_gradient(RED, ORANGE)

        self.play(Write(DE))