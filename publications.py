from publication import Publication

publications = [
    Publication(
        title="Tuning Random Generators",
        authors=[("<span class='author'>Ryan","Tjoa</span>"),("Poorva","Garg"),("Harrison", "Goldstein"), ("Todd", "Millstein"), ("Benjamin", "Pierce"), ("Guy", "Van den Broeck")],
        venue="In Submission",
    ),
    Publication(
        title="Labeled Tuples (Informed Position)",
        authors=[("Chris","Casinghino"), ("<span class='author'>Ryan","Tjoa</span>")],
        venue="Higher-order, Typed, Inferred, Strict: ML Family Workshop 2024",
        venue_short="ML Family Workshop 2024",
        venue_table="ML 2024",
        venue_url="https://icfp24.sigplan.org/home/mlworkshop-2024",
    ),
    Publication(
       title="Equality Saturation Theory Exploration à la Carte",
       authors=[("Anjali","Pal"), ("Brett","Saiki"), ("<span class='author'>Ryan","Tjoa</span>*"), ("Cynthia","Richey*"),("Amy","Zhu"), ("Oliver","Flatt"), ("Max","Willsey"),("Zachary","Tatlock"), ("Chandrakana","Nandi")],
       venue="Object-Oriented Programming, Systems, Languages & Applications (OOPSLA) 2023",
       venue_short="OOPSLA 2023",
       pdf="pubs/oopsla23-enumo.pdf",
       doi="https://dl.acm.org/doi/10.1145/3622834",
       venue_url="https://2023.splashcon.org/track/splash-2023-oopsla",
    ),
    Publication(
        title="Scaling Integer Arithmetic in Probabilistic Programs",
        authors=[("William X.","Cao"),("Poorva","Garg*"),("<span class='author'>Ryan","Tjoa</span>*"), ("Steven", "Holtzen"), ("Todd","Millstein"), ("Guy","Van den Broeck")],
        venue="Uncertainty in Artificial Intelligence (UAI) 2023",
        venue_short="UAI 2023",
        pdf="pubs/uai23-arith.pdf",
        doi="https://proceedings.mlr.press/v216/cao23b.html",
        venue_url="https://www.auai.org/uai2023/",
    )
]
