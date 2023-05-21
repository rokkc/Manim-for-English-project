from manim import *

class QuoteFade(Scene):
    def construct(self):
        quote_text = "The difference between a successful person and others is not a lack of\n strength, not a lack of knowledge, but rather a lack in will. - Vince Lombardi"

        quote = Text(quote_text, font="Times New Roman", font_size=30)
        quote.set_color_by_gradient(BLUE, GREEN, BLUE, GREEN)

        self.play(AnimationGroup(*[Write(quote)]), run_time=4.5)
        self.wait(2.5)
        self.play(FadeOut(quote))
        self.wait()


class RotateAndArrange(MovingCameraScene):
    def construct(self):


        plane = NumberPlane()
        plane.add_coordinates()
        #self.add(plane)

        # Define the images
        image_paths = [
            "/Users/yash/Desktop/New Folder With Items/THOMS.jpg",
            "/Users/yash/Desktop/New Folder With Items/TKAM.jpg",
            "/Users/yash/Desktop/New Folder With Items/OD.jpg",
            "/Users/yash/Desktop/New Folder With Items/RNJ.jpg",
            "/Users/yash/Desktop/New Folder With Items/OMAM.jpg"
            ]

        image_paths = [ImageMobject(image) for image in image_paths]
        for image in image_paths:
            image.height = 2

        group = Group(image_paths[0], image_paths[1], image_paths[2], image_paths[3], image_paths[4])
        group.arrange(RIGHT)
        self.add(group)

        for _ in range(5):
            self.play(CyclicReplace(*group), run_time=1.25)

        self.play(
            image_paths[0].animate.shift(UP*1.5+RIGHT*0.2).scale(1.2),
            image_paths[1].animate.shift(UP*1.5+RIGHT*4.4).scale(1.2),
            image_paths[2].animate.shift(DOWN * 2+LEFT*4).scale(1.2),
            image_paths[3].animate.shift(DOWN * 2+LEFT*1.5).scale(1.2),
            image_paths[4].animate.shift(DOWN * 2+RIGHT).scale(1.2),
        )

        self.wait()

        text_1 = Text("The House on Mango Street", font_size=20)
        text_1.next_to(image_paths[0], UP*1)

        text_2 = Text("To Kill a Mockingbird", font_size=20)
        text_2.next_to(image_paths[1], UP*1)

        text_3 = Text("The Odyssey", font_size=20)
        text_3.next_to(image_paths[2], UP)

        text_4 = Text("Romeo & Juliet", font_size=20)
        text_4.next_to(image_paths[3], UP)

        text_5 = Text("Of Mice and Men", font_size=20)
        text_5.next_to(image_paths[4], UP)

        self.play(
            Write(text_1),
            Write(text_2),
            Write(text_3),
            Write(text_4),
            Write(text_5),
        )

        self.wait(4)

        self.play(
            image_paths[0].animate.shift(UP*0.55 + LEFT * 2.75).scale(1.2),
            FadeOut(image_paths[1]),
            FadeOut(image_paths[2]),
            FadeOut(image_paths[3]),
            FadeOut(image_paths[4]),
            FadeOut(text_1),
            FadeOut(text_2),
            FadeOut(text_3),
            FadeOut(text_4),
            FadeOut(text_5),
        )

        self.wait(2)

class TitleScene(MovingCameraScene):
    def construct(self):
        # Create a title
        title = Text("A Difference in Will", font_size=48)
        title.align_to(ORIGIN, direction=UP)
        title.shift(UP*0.5)

        # Add the title to the scene
        self.add(title)

        attribution = Text("by: Yash Pattekar", font_size=24)

        # Position the attribution below the title
        attribution.next_to(title, DOWN*1.5)

        # Add the attribution to the scene
        self.add(attribution)

        self.play(self.camera.frame.animate.move_to(title).set(width=title.width * 1.35))
        self.wait(1)
        self.play(self.camera.frame.animate.move_to(attribution).set(width=attribution.width * 1.35))
        self.wait(1)
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))
        self.wait(1)
        self.play(
            FadeOut(title),
            FadeOut(attribution),
        )

class THOMS(Scene):
    def construct(self):
        book_image = ImageMobject("/Users/yash/Desktop/New Folder With Items/THOMS.jpg").shift(UP*2.05 + RIGHT * -5.64565627).scale(1.44)
        self.add(book_image)


        bullet_symbol = Text("•", font_size=35)

        # Create the text content
        text_content1 = Text("Be yourself", font_size=24)
        text_content1.next_to(book_image, RIGHT*4).shift(UP*0.9)

        text_content2 = Text("Follow your passions, whatever they are", font_size=24)
        text_content2.next_to(book_image, RIGHT*4).shift(UP*0)

        # Group the bullet symbol and text content
        bullet_point1 = Group(bullet_symbol.copy().next_to(text_content1, LEFT, buff=0.15), text_content1)
        bullet_point2 = Group(bullet_symbol.copy().next_to(text_content2, LEFT, buff=0.15), text_content2)

        self.wait(4.5)

        # Fade in the bullet point
        self.play(FadeIn(bullet_point1))

        self.wait(4.5)

        self.play(FadeIn(bullet_point2))

        self.wait(2.5)

        image = ImageMobject("/Users/yash/Desktop/New Folder With Items/typewriter.png").scale(0.65).shift(DOWN*1.75+RIGHT*4)
        image_text = Text("Sandra Cisneros' past writing", font_size=20).next_to(image, UP*1)



        self.play(FadeIn(image))
        self.play(Write(image_text))

        self.wait()

        self.play(
            FadeTransform(book_image, ImageMobject("/Users/yash/Desktop/New Folder With Items/TKAM.jpg").shift(UP*2.05 + RIGHT * -5.64565627).scale(1.44)),
            FadeOut(bullet_point1),
            FadeOut(bullet_point2),
            FadeOut(image),
            FadeOut(image_text),
        )

class TKAM(MovingCameraScene):
    def construct(self):
        book_image = ImageMobject("/Users/yash/Desktop/New Folder With Items/TKAM.jpg").shift(UP*2.05 + RIGHT * -5.64565627).scale(1.44)
        self.add(book_image)


        bullet_symbol = Text("•", font_size=35)

        # Create the text content
        text_content1 = Text("Atticus had a passion for being a lawyer and defending his clients", font_size=24)
        text_content1.next_to(book_image, RIGHT*4).shift(UP*0.9)

        text_content2 = Text("He knew he was fighting a losing battle", font_size=24)
        text_content2.next_to(book_image, RIGHT*4).shift(UP*0)

        text_content3= Text("Persevere in our passions no matter which obstacles are in our paths", font_size=24)
        text_content3.next_to(book_image, RIGHT*4).shift(DOWN*0.9)

        # Group the bullet symbol and text content
        bullet_point1 = Group(bullet_symbol.copy().next_to(text_content1, LEFT, buff=0.15), text_content1)
        bullet_point2 = Group(bullet_symbol.copy().next_to(text_content2, LEFT, buff=0.15), text_content2)
        bullet_point3 = Group(bullet_symbol.copy().next_to(text_content3, LEFT, buff=0.15), text_content3)

        quote_text = '"Real courage is when you know you\'re licked before you begin,\n but you begin anyway and see it through no matter what." (Lee 149)'


        quote = Text(quote_text, font="Times New Roman", font_size=30)
        quote.set_color_by_gradient(BLUE, GREEN, BLUE, GREEN).shift(DOWN*0.5)


        # Fade in the bullet point
        self.wait(1.3)

        self.play(FadeIn(bullet_point1))

        self.wait(5)

        self.play(FadeIn(bullet_point2))

        self.wait(3)

        self.play(AnimationGroup(*[Write(quote)]), run_time=4.5)
        self.wait(6)

        self.play(FadeIn(bullet_point3))

        self.wait()

        self.play(
            FadeOut(quote),
            FadeOut(bullet_point1),
            FadeOut(bullet_point2),
            FadeOut(bullet_point3),
        )

        self.wait()


        self.play(self.camera.frame.animate.move_to(book_image).set(width=book_image.width * 0.25), FadeOut(book_image), run_time=2)

        self.wait(0.5)


class OD(Scene):
    def construct(self):
        book_image = ImageMobject("/Users/yash/Desktop/New Folder With Items/OD.jpg").shift(UP*2.05 + RIGHT * -5.64565627).scale(1.44)
        self.play(FadeIn(book_image))


        bullet_symbol = Text("•", font_size=35)

        # Create the text content
        text_content1 = Text("Faced many obstacles", font_size=24)
        text_content1.next_to(book_image, RIGHT*4).shift(UP*0.9)

        text_content2 = Text("Resisted temptations", font_size=24)
        text_content2.next_to(book_image, RIGHT*4).shift(UP*0)

        text_content3= Text("Didn't succumb to temptations and faced obstacles head on", font_size=24)
        text_content3.next_to(book_image, RIGHT*4).shift(DOWN*0.9)

        # Group the bullet symbol and text content
        bullet_point1 = Group(bullet_symbol.copy().next_to(text_content1, LEFT, buff=0.15), text_content1)
        bullet_point2 = Group(bullet_symbol.copy().next_to(text_content2, LEFT, buff=0.15), text_content2)
        bullet_point3 = Group(bullet_symbol.copy().next_to(text_content3, LEFT, buff=0.15), text_content3)

        quote_text = '"In my grief I thought that I should cast myself overboard and drown,\n rather than face such a tragedy. But my spirit held me, made me\n cling to the rail and endure it all." (Homer 113)'



        quote = Text(quote_text, font="Times New Roman", font_size=30)
        quote.set_color_by_gradient(BLUE, GREEN, BLUE, GREEN).shift(DOWN*0.5)


        # Fade in the bullet point
        self.wait(7)
        self.play(FadeIn(bullet_point1))

        self.wait(5)



        image1 = ImageMobject("/Users/yash/Desktop/New Folder With Items/header-10-1024x559.png").shift(DOWN*1.5)
        image2 = ImageMobject("/Users/yash/Desktop/New Folder With Items/Odysseusand-thesirensbywaterhouse-56aab07c5f9b58b7d008dc0e.jpg").shift(DOWN*1.5)
        image3 = ImageMobject("/Users/yash/Desktop/New Folder With Items/The-waves-crashed-between-the-towering-cliff-of-Scylla-and-the-jagged-rocks-of-Charybdis.png").shift(DOWN*1.5)
        image4 = ImageMobject("/Users/yash/Desktop/New Folder With Items/317496_orig.png").shift(DOWN*1.5)
        image5 = ImageMobject("/Users/yash/Desktop/New Folder With Items/lotus.jpg").shift(DOWN*1.5)

        self.play(FadeIn(image1))

        self.wait(5)

        self.play(FadeOut(image1))

        self.wait(2)

        self.play(FadeIn(image2))

        self.wait(7)

        self.play(FadeOut(image2))

        self.wait(0.5)

        self.play(FadeIn(image3))

        self.wait(0.5)

        self.play(FadeOut(image3))


        self.play(FadeIn(image4))

        self.wait(0.5)

        self.play(FadeOut(image4))

        self.wait(0.5)

        self.play(FadeIn(image5))

        self.wait()

        self.play(FadeOut(image5))

        self.wait(3)

        self.play(FadeIn(bullet_point2))

        self.wait()

        self.play(FadeIn(bullet_point3))

        self.wait(9)

        self.play(AnimationGroup(*[Write(quote)]), run_time=4.5)
        self.wait(15)

        self.play(
            FadeOut(book_image),
            FadeOut(quote),
            FadeOut(bullet_point1),
            FadeOut(bullet_point2),
            FadeOut(bullet_point3),
        )

        self.wait()


class RNJ(Scene):
    def construct(self):
        book_image = ImageMobject("/Users/yash/Desktop/New Folder With Items/RNJ.jpg").shift(UP*2.05 + RIGHT * -5.64565627).scale(1.44)
        self.play(FadeIn(book_image))


        bullet_symbol = Text("•", font_size=35)

        # Create the text content
        text_content1 = Text("We should avoid people who don't believe in our goals", font_size=24)
        text_content1.next_to(book_image, RIGHT*4).shift(UP*0.9)



        # Group the bullet symbol and text content
        bullet_point1 = Group(bullet_symbol.copy().next_to(text_content1, LEFT, buff=0.15), text_content1)


        quote_text = '“Henceforth I will never be Romeo.” (Shakespeare 2.2.51)'



        quote = Text(quote_text, font="Times New Roman", font_size=30)
        quote.set_color_by_gradient(BLUE, GREEN, BLUE, GREEN).shift(DOWN*0.5)


        # Fade in the bullet point
        self.wait(1)

        self.play(FadeIn(bullet_point1))

        self.wait(6.5)

        self.play(AnimationGroup(*[Write(quote)]))
        self.wait(2)

        self.play(
            FadeOut(book_image),
            FadeOut(quote),
            FadeOut(bullet_point1),
        )

        self.wait(4)


class OMAM(Scene):
    def construct(self):
        book_image = ImageMobject("/Users/yash/Desktop/New Folder With Items/OMAM.jpg").shift(UP*2.05 + RIGHT * -5.64565627).scale(1.44)
        self.play(FadeIn(book_image))


        bullet_symbol = Text("•", font_size=35)

        # Create the text content
        text_content1 = Text("We should work towards our goals", font_size=24)
        text_content1.next_to(book_image, RIGHT*4).shift(UP*0.9)

        text_content2 = Text("Use your passions as a purpose", font_size=24)
        text_content2.next_to(book_image, RIGHT*4).shift(UP*0)



        # Group the bullet symbol and text content
        bullet_point1 = Group(bullet_symbol.copy().next_to(text_content1, LEFT, buff=0.15), text_content1)
        bullet_point2 = Group(bullet_symbol.copy().next_to(text_content2, LEFT, buff=0.15), text_content2)

        image1 = ImageMobject("/Users/yash/Desktop/New Folder With Items/5098736.jpg").shift(DOWN * 1.5).scale(1.725)


        # Fade in the bullet point

        self.wait(4)

        self.play(FadeIn(bullet_point1), FadeIn(image1), run_time = 1.25)

        self.wait(4)


        self.play(FadeIn(bullet_point2))

        self.wait(7)



        self.play(
            FadeOut(book_image),
            FadeOut(bullet_point1),
            FadeOut(bullet_point2),
            FadeOut(image1),

        )

        self.wait(1.5)




class LineGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 11, 1],
            y_range=[0, 6, 1],
            x_length=10,
            y_length=5,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": range(1, 11)},
            y_axis_config={"numbers_to_include": range(1, 6)},
        )

        x_label = Text("Grade in English Class (5 is average)", font_size=20).next_to(axes.x_axis, DOWN)
        y_label = Text("Interest in English Class", font_size=20).rotate(90 * DEGREES).shift(LEFT*6)
        chart_label = Text("Correlation between interest and grades", font_size=30).next_to(axes, UP)

        data = [(4, 3), (6, 3.5), (7, 3), (8, 4), (9, 4.5), (10, 5)]
        points = VGroup(*[Dot(axes.c2p(x, y), color=BLUE) for x, y in data])

        lines = VGroup()
        for i in range(len(points) - 1):
            line = Line(points[i].get_center(), points[i + 1].get_center(), color=BLUE, stroke_width=2)
            lines.add(line)

        self.play(Create(axes), run_time=2)
        self.play(Write(x_label), Write(y_label), Write(chart_label), run_time=2)
        self.play(Create(points), run_time=2)
        self.play(Create(lines), run_time=2)

        self.wait(12)

        graph_group = VGroup(axes, x_label, y_label, chart_label, points, lines)


        self.play(graph_group.animate.scale(0.4).shift(UP*2.4+LEFT*3.75), run_time=2)

        white_border = SurroundingRectangle(graph_group, buff=0.1)
        white_border.set_color(WHITE)

        self.play(Create(white_border))

        self.wait()

        text1 = Text("Passion can be found in anything", font_size=22).shift(UP*3+RIGHT*2)
        text2 = Text("We should persevere in our passions no matter which obstacles are in our paths", font_size=22).shift(DOWN*3+LEFT*1.5)
        text3 = Text("We should never succumb to distractions and face obstacles head on", font_size=22).shift(DOWN*2+RIGHT)
        text4 = Text("Don't be around people who don't believe in your goals and dreams", font_size=22)
        text5 = Text("Use your passions to find purpose", font_size=22).shift(RIGHT+UP)

        self.play(
            Write(text1),
            Write(text2),
            Write(text3),
            Write(text4),
            Write(text5),
            )

        self.wait(2)

        text6 = Text("Success can be found in any goal, as long as we are passionate,\n perseverant and we don't let our obstacles stop us.", font_size=22)



        self.play(
            FadeOut(white_border),
            ReplacementTransform(graph_group, text6),
            ReplacementTransform(text1, text6),
            ReplacementTransform(text2, text6),
            ReplacementTransform(text3, text6),
            ReplacementTransform(text4, text6),
            ReplacementTransform(text5, text6),
            runtime = 1.5
        )

        self.add(text6)

        self.play(
            FadeOut(text1),
            FadeOut(text2),
            FadeOut(text3),
            FadeOut(text4),
            FadeOut(text5),
            runtime = 1.5
        )

        self.wait()

        self.play(text6.animate.scale(1.25))

        self.wait(3)

        self.play(FadeOut(text6))


class RollingCredits(MovingCameraScene):
    def construct(self):
        title = Text("Works Cited", font_size=52).shift(UP*2.5)
        self.add(title)
        names = [
            '“FROM WHAT PLANT DID THE LOTUS EATERS EAT THE FRUIT AND FLOWERS?”\n        The Garden of Eaden,\n        https://gardenofeaden.blogspot.com/2017/01/from-what-plant-did-lotus-eaters-ea\n       t.html. Accessed 20 May 2023. ',
            'Bos. “Odysseus and the Sirens.” AwesomeStories.Com,\n        https://www.awesomestories.com/asset/view/Odysseus-and-the-Sirens.\n        Accessed 20 May 2023. ',
            "“The Witch Circe.” The Odyssey by Homer,\n        https://theodysseyperla2.weebly.com/the-witch-circe.html. Accessed 20 May\n        2023. ",
            "“The Odyssey.” Every Day Original, 5 June 2019,\n        https://everydayoriginal.com/product/the-odyssey/. Accessed 20 May 2023. ",
            "The Great Courses. “How Odysseus Fooled a Cyclops.” Wondrium Daily, 19 Dec. 2016,\n        https://www.wondriumdaily.com/odysseus-fooled-cyclops/. Accessed 20 May\n        2023. ",
            "Landsman, Klaas. “Fig. 11.1 The Waves Crashed between the Towering Cliff of Scylla\n        And...” ResearchGate,\n        https://www.researchgate.net/figure/The-waves-crashed-between-the-towering-cli\n       ff-of-Scylla-and-the-jagged-rocks-of-Charybdis_fig1_317172062. Accessed 20\n        May 2023. ",
            "“Steinbeck’s ‘Of Mice and Men’: Plot Analysis.” Scraps from the Loft, 11 Mar. 2019,\n        https://scrapsfromtheloft.com/books/steinbeck-of-mice-and-men-plot-analysis/.\n        Accessed 20 May 2023. ",
            "Store, Getty Museum. “The Odyssey.” Getty Museum Store,\n        https://shop.getty.edu/products/the-odyssey?variant=32716926124109.\n               Accessed 20 May 2023. ",
            "Foca, Anna, and Laura Fine. “To Kill a Mockingbird.” Encyclopedia Britannica, 28 Oct.\n        2011, https://www.britannica.com/topic/To-Kill-a-Mockingbird. Accessed 20 May\n        2023. ",
            "“The House on Mango Street.” National Endowment for the Arts,\n        https://www.arts.gov/initiatives/nea-big-read/house-mango-street. Accessed 20\n        May 2023. ",
            "Lamb, Joyce. “Lauren Kate Casts the Movie Version of ‘Fallen.’” USATODAY, 21 Feb.\n        2013, https://www.usatoday.com/story/happyeverafter/2013/02/20/lauren-kate-fallen-mo\n       vie-dream-cast/1933973/. Accessed 20 May 2023. ",
            "“Of Mice and Men.” Julianne’s Literature Blog,\n        https://julianneslitblog.weebly.com/of-mice-and-men.html. Accessed 20 May\n        2023. ",
            "Intern, Communications. “Sandra Cisneros on Looking Through Her Past Writing.” PEN\n        America, 19 Feb. 2019,\n        https://pen.org/sandra-cisneros-looking-through-past-writing/. Accessed 20 May\n        2023. ",
        ]
        credit_objs = [Text(name, font_size=40).scale(0.5) for name in names]
        for ind, cred in enumerate(credit_objs):
            cred.shift(DOWN*ind*3)
            self.add(cred)

        self.play(
            self.camera.frame.animate.shift(DOWN*50),
            run_time=10,
            rate_func=linear
        )

