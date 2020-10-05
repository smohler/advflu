from manimlib.imports import *

class Lecture1_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture One')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{The Navier Stokes Equations, pt.1}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture1_scene1(Scene):
    def construct(self):
        ## this scene will lead us into study, body, motion, fluid
        question = TextMobject('Consider a ', 'of ')
        blob = TexMobject(r'\textit{Blob }')
        blob.set_color(YELLOW)
        fluid = TexMobject(r'\textit{Fluid}')
        fluid.set_color(BLUE)
        ## set order
        blob.next_to(question[0], RIGHT)
        question[1].next_to(blob, RIGHT)
        fluid.next_to(question[1], RIGHT)
        phrase = VGroup(question[0], blob, question[1], fluid)
        phrase.center()
        phrase.to_edge(UP)
        ## illustrate blob
        circle = Circle(radius = 1.5, fill_color = BLUE, color = YELLOW, fill_opacity = 0.3)
        eli1 = Ellipse(width = 2, height = 3, fill_color = BLUE, color = YELLOW)
        eli2 = Ellipse(width = 1, height = 3, fill_color = BLUE, color = YELLOW)
        eli3 = Ellipse(width = 3, height = 1, fill_color = BLUE, color = YELLOW)
        sphere = VGroup(circle, eli1, eli2, eli3)
        ## how does it move
        phrase2 = TextMobject('Say we are tasked with answering a simple queston:')
        phrase2.shift(UP)
        question3 = TexMobject(r'\textit{How does it move?}')
        question3.set_color_by_gradient(YELLOW, BLUE)
        question3.scale(2)
        # play
        self.play(Write(phrase))
        self.play(ShowCreation(sphere))
        self.wait(1)
        self.play(FadeOut(phrase), ReplacementTransform(sphere, phrase2))
        self.wait(1)
        self.play(Write(question3))
        self.wait(1)
        self.play(FadeOut(phrase2), FadeOut(question3))

class Lecture1_scene2(Scene):
    def construct(self):
        ## introduce study, body, motion, fluid
        intro = TextMobject('We must define the following topics')
        intro.to_edge(UP)
        study = TexMobject(r'\textit{Study}')
        study.scale(2)
        study.set_color_by_gradient(RED, ORANGE)
        body = TexMobject(r'\textit{Body}')
        body.scale(2)
        body.set_color_by_gradient(ORANGE, YELLOW)
        motion = TexMobject(r'\textit{Motion}')
        motion.scale(2)
        motion.set_color_by_gradient(YELLOW, GREEN)
        fluid = TexMobject(r'\textit{Fluid}')
        fluid.scale(2)
        fluid.set_color_by_gradient(GREEN, BLUE_C)
        ## positioning
        study.shift(1.5*UP)
        body.next_to(study, 2*DOWN)
        motion.next_to(body, 2*DOWN)
        fluid.next_to(motion, 2*DOWN)
        chapters = VGroup(study, body, motion, fluid)
        chapters.center()

        # play
        self.play(FadeIn(intro))
        self.wait(1)
        self.play(Write(chapters))
        self.wait(3)
        self.play(FadeOut(chapters), FadeOut(intro))

class Lecture1_study(Scene):
    def construct(self):
        ## scene describing study
        study = TexMobject(r'\textit{Study}')
        study.scale(3)
        study.set_color_by_gradient(RED, ORANGE)
        study.center()
        ## have 'study' go from center to corner
        studyA = TexMobject(r'\textit{Study}')
        studyA.set_color_by_gradient(RED, ORANGE)
        studyA.scale(1.5)
        studyA.to_corner(UP + LEFT)
        ##

        # inculde animations describing what we mean by 'study' as in video

        ##
        # play
        self.play(FadeIn(study))
        self.wait(1)
        self.play(Transform(study, studyA))
        self.wait(2)



class Lecture1_body(Scene):
    def construct(self):
        ## scene describing study
        body = TexMobject(r'\textit{Body}')
        body.scale(3)
        body.set_color_by_gradient(ORANGE, YELLOW)
        body.center()
        ## have 'study' go from center to corner
        bodyA = TexMobject(r'\textit{Body}')
        bodyA.set_color_by_gradient(ORANGE, YELLOW)
        bodyA.scale(1.5)
        bodyA.to_corner(UP + LEFT)
        ##

        # inculde animations describing what we mean by 'body' as in video

        ##
        # play
        self.play(FadeIn(body))
        self.wait(1)
        self.play(Transform(body, bodyA))
        self.wait(2)


class Lecture1_motion(Scene):
    def construct(self):
        ## scene describing study
        motion = TexMobject(r'\textit{Motion}')
        motion.scale(3)
        motion.set_color_by_gradient(YELLOW, GREEN)
        motion.center()
        ## have 'study' go from center to corner
        motionA = TexMobject(r'\textit{Motion}')
        motionA.set_color_by_gradient(YELLOW, GREEN)
        motionA.scale(1.5)
        motionA.to_corner(UP + LEFT)
        ##

        # inculde animations describing what we mean by 'body' as in video

        ##
        # play
        self.play(FadeIn(motion))
        self.wait(1)
        self.play(Transform(motion, motionA))
        self.wait(2)


class Lecture1_fluid(Scene):
    def construct(self):
        ## scene describing study
        fluid = TexMobject(r'\textit{Fluid}')
        fluid.scale(3)
        fluid.set_color_by_gradient(GREEN, BLUE_C)
        fluid.center()
        ## have 'study' go from center to corner
        fluidA = TexMobject(r'\textit{Fluid}')
        fluidA.set_color_by_gradient(GREEN, BLUE_C)
        fluidA.scale(1.5)
        fluidA.to_corner(UP + LEFT)
        ##

        # inculde animations describing what we mean by 'body' as in video

        ##
        # play
        self.play(FadeIn(fluid))
        self.wait(1)
        self.play(Transform(fluid, fluidA))
        self.wait(2)