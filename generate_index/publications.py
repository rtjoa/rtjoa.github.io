from publication import Author, Publication

AmyZhu = Author("Amy", "Zhu", "https://amy.zhucchini.ca/")
AnjaliPal = Author("Anjali", "Pal", "https://ajpal.github.io/")
BenjaminPierce = Author("Benjamin", "Pierce", "https://www.cis.upenn.edu/~bcpierce/")
BrettSaiki = Author("Brett", "Saiki", "https://bsaiki.com/")
ChandrakanaNandi = Author("Chandrakana", "Nandi", "https://cnandi.com/")
ChrisCasinghino = Author("Chris", "Casinghino", "https://tyconmismatch.com/")
CynthiaRichey = Author("Cynthia", "Richey", "https://thia.codes/")
GuyVandenBroeck = Author("Guy", "Van den Broeck", "https://web.cs.ucla.edu/~guyvdb/")
HarrisonGoldstein = Author("Harrison", "Goldstein", "https://harrisongoldste.in/")
MaxWillsey = Author("Max", "Willsey", "https://www.mwillsey.com/")
OliverFlatt = Author("Oliver", "Flatt", "https://www.oflatt.com/")
PoorvaGarg = Author("Poorva", "Garg", "https://web.cs.ucla.edu/~poorvagarg/")
RyanTjoa = Author("Ryan", "Tjoa", is_me=True)
StevenHoltzen = Author(
    "Steven", "Holtzen", "https://www.khoury.northeastern.edu/home/sholtzen/"
)
ToddMillstein = Author("Todd", "Millstein", "https://web.cs.ucla.edu/~todd/")
WilliamXCao = Author("William X.", "Cao", "https://www.linkedin.com/in/williamxcao/")
ZacharyTatlock = Author("Zachary", "Tatlock", "https://ztatlock.net/")

publications = [
    # Publication(
    #     # title="Tuning Random Generators with <span class='small-caps'>Loaded Dice</span>",
    #     # title="Tuning Random Generators with Loaded Dice",
    #     # title="Random Testing with Loaded Dice",
    #     title="Random Testing with Loaded Dice",
    #     authors=[
    #         RyanTjoa,
    #         PoorvaGarg,
    #         HarrisonGoldstein,
    #         ToddMillstein,
    #         BenjaminPierce,
    #         GuyVandenBroeck,
    #     ],
    #     venue="In Submission",
    #     pdf="",
    # ),
    # Publication(
    #     title="Labeled Tuples (Informed Position)",
    #     authors=[ChrisCasinghino, RyanTjoa],
    #     venue="Higher-order, Typed, Inferred, Strict: ML Family Workshop 2024",
    #     venue_short="ML Family Workshop 2024",
    #     venue_table="ML 2024",
    #     venue_url="https://icfp24.sigplan.org/home/mlworkshop-2024",
    #     pdf="",
    # ),
    Publication(
        title="Equality Saturation Theory Exploration à la Carte",
        authors=[
            AnjaliPal,
            BrettSaiki,
            RyanTjoa,
            CynthiaRichey,
            AmyZhu,
            OliverFlatt,
            MaxWillsey,
            ZacharyTatlock,
            ChandrakanaNandi,
        ],
        venue="Object-Oriented Programming, Systems, Languages & Applications (OOPSLA) 2023",
        venue_short="OOPSLA 2023",
        pdf="pubs/oopsla23-enumo.pdf",
        doi="https://dl.acm.org/doi/10.1145/3622834",
        venue_url="https://2023.splashcon.org/track/splash-2023-oopsla",
        asterisk=[2, 3],
    ),
    Publication(
        title="Scaling Integer Arithmetic in Probabilistic Programs",
        authors=[
            WilliamXCao,
            PoorvaGarg,
            RyanTjoa,
            StevenHoltzen,
            ToddMillstein,
            GuyVandenBroeck,
        ],
        venue="Uncertainty in Artificial Intelligence (UAI) 2023",
        venue_short="UAI 2023",
        pdf="pubs/uai23-arith.pdf",
        doi="https://proceedings.mlr.press/v216/cao23b.html",
        venue_url="https://www.auai.org/uai2023/",
        asterisk=[1, 2],
    ),
]
