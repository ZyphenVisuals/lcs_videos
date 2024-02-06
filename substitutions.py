from manim import *

class Thumbnail(Scene):
    def construct(self):
        title = Title("Logic for Computer Science")
        text = Text("Substitutions").scale(1.5)
        self.add(title, text)

class Disclaimer(Scene):
    def construct(self):
        # https://stackoverflow.com/a/76195562
        myBaseTemplate = TexTemplate(
            documentclass="\documentclass[preview]{standalone}"
        )
        myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        disclaimer = Tex(
            "\\justifying{This is an abridged explanation from a student that might not accurately depict all of the nuances of the topic discussed, intended only to get an intuitive idea for the topic. For a better understanding, please check lecture notes from a professor.}",
            tex_template=myBaseTemplate,
        ).scale(0.6)        

        title = Title("Disclaimer")

        self.play(AnimationGroup(Write(disclaimer), Write(title)))
        self.wait(7)
        self.play(FadeOut(disclaimer), FadeOut(title))

class Credit(Scene):
    def construct(self):
        text = Text("Based on the lecture notes of Associate Prof. Adrian Crăciun.").scale(0.5)

        self.play(Write(text))
        self.wait(1)
        self.play(Unwrite(text),reverse=False)

class Intro(Scene):
    def construct(self):
        title = Text("Substitutions")

        self.play(Write(title))
        self.wait(1)
        self.play(Unwrite(title),reverse=False)

class Substitution(Scene):
    def construct(self):
        s = MathTex(r"\sigma = \{",r"x_1",r"\leftarrow ",r"t_1",r",\dots,",r"x_n",r" \leftarrow ",r"t_n",r" \}")
        self.play(Write(s))
        self.wait(1)
        # indicate the variables x
        self.play(AnimationGroup(
            Indicate(s[1]),
            Indicate(s[5])
        ))
        # indicate the terms t
        self.play(AnimationGroup(
            Indicate(s[3]),
            Indicate(s[7])
        ))
        self.wait(1)
        self.play(Unwrite(s),reverse=False)

class ApplyingSubstitutions(Scene):
    def construct(self):
        cosntants = MathTex(r"c_\sigma = c")
        self.play(Write(cosntants))
        self.wait(1)
        self.play(Unwrite(cosntants),reverse=False)
        variables = MathTex(r"x_\sigma = \left\lbrace\begin{aligned}&x&\text{if }\underset{1\le i\le n}\forall (x\ne x_i)\\&t_i&\text{if }\exists i(x=x_i)\end{aligned}\right.")
        self.play(Write(variables))
        self.wait(1)
        self.play(Unwrite(variables),reverse=False)
        functions = MathTex(r"f(s_1,\dots,s_m)_\sigma = f((s_1)_\sigma,\dots,(s_m)_\sigma)")
        self.play(Write(functions))
        self.wait(1)
        self.play(Unwrite(functions),reverse=False)
        predicates = MathTex(r"P(s_1,\dots,s_m)_\sigma = P((s_1)_\sigma,\dots,(s_m)_\sigma)")
        self.play(Write(predicates))
        self.wait(1)
        self.play(Unwrite(predicates),reverse=False)
        logical_connectives = MathTex(r"(\lnot F)_\sigma &=(\lnot F_\sigma)\\(F\land G)_\sigma &= (F_\sigma \land G_\sigma)\\(F\lor G)_\sigma &= (F_\sigma \lor G_\sigma)\\(F\implies G)_\sigma &= (F_\sigma \implies G_\sigma)\\(F\iff G)_\sigma &= (F_\sigma \iff G_\sigma)\\")
        self.play(Write(logical_connectives))
        self.wait(1)
        self.play(Unwrite(logical_connectives),reverse=False)
        quantified_formulas = MathTex(r"(\forall xF)_\sigma &= \forall x(F_{\sigma \setminus \{x\leftarrow t\}})\\(\exists xF)_\sigma &= \exists x(F_{\sigma \setminus \{x\leftarrow t\}})\\")
        self.play(Write(quantified_formulas))
        self.wait(1)
        self.play(Unwrite(quantified_formulas),reverse=False)

class SubstitutionExample(Scene):
    def construct(self):
        MathTemplate = TexTemplate(
            documentclass="\documentclass[preview]{standalone}"
        )
        MathTemplate.add_to_preamble(r"\usepackage{braket}")
        title = Title(r"$\sigma=\set{x\leftarrow f(y,z),y\leftarrow z,z\leftarrow a}$", tex_template=MathTemplate)
        self.play(Write(title))
        self.wait(1)
        ex1_1 = MathTex("f(", "x", "+", "y", ",", "z", ")", "_\sigma")
        self.play(Write(ex1_1))
        self.wait(1)
        ex1_2 = MathTex("f(", "(", "x", "+", "y", ")", "_\sigma", ",", "z", "_\sigma" , ")")
        self.play(TransformMatchingTex(ex1_1,ex1_2))
        self.wait(1)
        ex1_3 = MathTex("f(", "x", "_\sigma" , "+", "y", "_\sigma", ",", "z", "_\sigma", ")")
        self.play(TransformMatchingTex(ex1_2,ex1_3))
        self.wait(1)
        ex1_4 = MathTex("f(", "f(y,z)", "+", "z" ",", "a", ")")
        self.play(Transform(ex1_3,ex1_4))
        self.wait(1)
        self.clear() # clear the screen to unwrite properly
        self.add(ex1_4) # add the final result to the screen
        self.add(title) # add the title to the screen
        self.play(Unwrite(ex1_4),reverse=False)
        ex2_1 = MathTex("(P(", "x", ",", "y", ")", "\implies", "(", "\\forall x(", "P(", "x", ",", "y", ")", "\land", "Q(", "z", ")",")",")",")","_\sigma")
        self.play(Write(ex2_1))
        self.wait(1)
        ex2_2 = MathTex("(P(", "x", ",", "y", ")","_\sigma", "\implies", "(", "\\forall x(", "P(", "x", ",", "y", ")", "\land", "Q(", "z", ")",")",")","_\sigma",")")
        self.play(TransformMatchingTex(ex2_1, ex2_2))
        self.wait(1)
        ex2_3 = MathTex("(P(", "x","_\sigma", ",", "y","_\sigma", ")", "\implies", "(", "\\forall x(", "P(", "x", ",", "y", ")", "\land", "Q(", "z", ")",")",")","_\sigma",")")
        self.play(TransformMatchingTex(ex2_2, ex2_3))
        self.wait(1)
        ex2_4 = MathTex("(P(", "x","_\sigma", ",", "y","_\sigma", ")", "\implies", "\\forall x(", "P(", "x", ",", "y", ")", "\land", "Q(", "z", ")",")","_{\sigma\setminus\{x\leftarrow f(y,z)\}}",")")
        self.play(TransformMatchingTex(ex2_3, ex2_4))
        self.wait(1)
        ex2_5 = MathTex("(P(", "x","_\sigma", ",", "y","_\sigma", ")", "\implies", "\\forall x(", "P(", "x", ",", "y", ")","_{\sigma\setminus\{x\leftarrow f(y,z)\}}", "\land", "Q(", "z", ")","_{\sigma\setminus\{x\leftarrow f(y,z)\}}",")",")")
        self.play(TransformMatchingTex(ex2_4, ex2_5))
        self.wait(1)
        ex2_6 = MathTex("(P(", "x","_\sigma", ",", "y","_\sigma", ")", "\implies", "\\forall x(", "P(", "x","_{\sigma\setminus\{x\leftarrow f(y,z)\}}", ",", "y","_{\sigma\setminus\{x\leftarrow f(y,z)\}}", ")", "\land", "Q(", "z","_{\sigma\setminus\{x\leftarrow f(y,z)\}}", ")",")",")")
        self.play(TransformMatchingTex(ex2_5, ex2_6.scale(0.8)))
        self.wait(1)
        ex2_7 = MathTex("(P(", "f(y,z)", ",", "z", ")", "\implies", "\\forall x(", "P(", "x", ",", "z", ")", "\land", "Q(", "a", ")",")",")")
        self.play(TransformMatchingTex(ex2_6, ex2_7))
        self.wait(1)
        self.play(FadeIn(ex2_1.shift(DOWN)))
        self.wait(1)
        self.play(AnimationGroup(
            Indicate(ex2_1[1]), # indicate the variable x   
            Indicate(ex2_7[1]) # indicate the transformed variable x
        ))
        self.wait(1)
        self.play(AnimationGroup(
            Indicate(ex2_1[9]), # indicate the variable x   
            Indicate(ex2_7[8]) # indicate the unchanged variable x
        ))
        self.wait(1)
        self.play(FadeOut(ex2_1))
        self.wait(1)
        self.play(
            Unwrite(ex2_7,reverse=False),
            Unwrite(title,reverse=False)
            )
    
class CompositionsIntro(Scene):
    def construct(self):
        title = Text("Compositions of substitutions")
        self.play(Write(title))
        self.wait(1)
        self.play(Unwrite(title),reverse=False)

class CompositionsDefinition(Scene):
    def construct(self):
        substitutions = MathTex(r"&\theta=\{x_1\leftarrow t_1,\dots,x_n\leftarrow t_n\}&X:variables\\&\sigma=\{y_1\leftarrow s_1,\dots,y_m\leftarrow s_m\}&Y:variables").shift(UP)
        composition = MathTex(r"\theta\sigma=\{x_1\leftarrow (t_1)_\sigma | x_i \in X, x_i \ne (t_i)_\sigma\} \cup \{y_j\leftarrow s_j | y_j \in Y, y_j \ne X\}").shift(DOWN).scale(0.9)
        self.play(Write(substitutions))
        self.wait(1)
        self.play(Write(composition))
        self.wait(1)
        self.play(Unwrite(substitutions,reverse=False),Unwrite(composition,reverse=False))

class CompositionsExample(Scene):
    def construct(self):
        substitutions = MathTex(r"&\theta=\{x\leftarrow f(y),y\leftarrow f(a),z\leftarrow u\}\\&\sigma=\{y\leftarrow g(a),u\leftarrow z,v\leftarrow f(f(a))\}").shift(UP)
        self.play(Write(substitutions))
        self.wait(1)
        composition = MathTex("\{x\leftarrow ","f(y)",",y\leftarrow ","f(a)",",z\leftarrow ","u","\}\cup\{","y\leftarrow g(a),","u\leftarrow z,v\leftarrow f(f(a))","\}").shift(DOWN).scale(0.9)
        self.play(Write(composition))
        self.wait(1)
        composition_2 = MathTex("\{x\leftarrow ","f(y)","_\sigma",",y\leftarrow ","f(a)","_\sigma",",z\leftarrow ","u","_\sigma","\}\cup\{","y\leftarrow g(a),","u\leftarrow z,v\leftarrow f(f(a))","\}").shift(DOWN).scale(0.9)
        self.play(TransformMatchingTex(composition,composition_2))
        self.wait(1)
        composition_3 = MathTex("\{x\leftarrow ","f(y)","_\sigma",",y\leftarrow ","f(a)","_\sigma",",z\leftarrow ","u","_\sigma","\}\cup\{","u\leftarrow z,v\leftarrow f(f(a))","\}").shift(DOWN).scale(0.9)
        self.play(TransformMatchingTex(composition_2,composition_3))
        self.wait(1)
        composition_4 = MathTex("\{x\leftarrow ","f(g(a))",",y\leftarrow ","f(a)",",z\leftarrow ","z","\}\cup\{","u\leftarrow z,v\leftarrow f(f(a))","\}").shift(DOWN).scale(0.9)
        self.play(TransformMatchingTex(composition_3,composition_4))
        self.wait(1)
        composition_5 = MathTex("\{x\leftarrow ","f(g(a))",",y\leftarrow ","f(a)","\}\cup\{","u\leftarrow z,v\leftarrow f(f(a))","\}").shift(DOWN).scale(0.9)
        self.play(TransformMatchingTex(composition_4,composition_5))
        self.wait(1)
        composition_6 = MathTex("\{x\leftarrow ","f(g(a))",",y\leftarrow ","f(a)",",","u\leftarrow z,v\leftarrow f(f(a))""\}").shift(DOWN).scale(0.9)
        self.play(TransformMatchingTex(composition_5,composition_6))
        self.wait(1)
        self.play(Unwrite(substitutions,reverse=False),Unwrite(composition_6,reverse=False))

class SubstitutabilityTeaser(Scene):
    def construct(self):
        exp = MathTex("P",":\exists y(","x","=2y)")
        self.play(Write(exp))
        self.wait(1)
        exp_2 = MathTex("P","_{\{x\leftarrow y+1\}}",":\exists y(","y+1","=2y)")
        self.play(TransformMatchingTex(exp,exp_2))
        self.wait(1)
        self.play(Unwrite(exp_2),reverse=False)

class SubstitutabilityIntro(Scene):
    def construct(self):
        title = Text("Substitutability")
        self.play(Write(title))
        self.wait(1)
        self.play(Unwrite(title),reverse=False)

class SubstitutabilityRules(Scene):
    def construct(self):
        title = Title("The term $t$ is substitutable for the variable $x$ in...")
        self.play(Write(title))
        self.wait(1)
        rules = MathTex(
            r"&\text{terms, atomic formulas} &\text{always}\\",
            r"&(\lnot F) &\text{iff. subs. in } F\\",
            r"&(F\square G) &\text{iff. subs. in } F \text{ and } G\\",
            r"&\forall xF,\exists xF &\text{always, no effect}\\",
            r"&\forall yF,\exists yF &\text{iff. subs. in } F \text{ and } y \text{ not in } t\\"
        )
        self.play(Write(rules[0]))
        self.wait(1)
        self.play(Write(rules[1]))
        self.wait(1)
        self.play(Write(rules[2]))
        self.wait(1)
        self.play(Write(rules[3]))
        self.wait(1)
        self.play(Write(rules[4]))
        self.wait(1)
        self.play(Unwrite(title,reverse=False),Unwrite(rules,reverse=False))