from turtle import position
from unicodedata import name
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image(
            name="./src/img/header.jpg",
            x=0,
            y=0,
            w=215.9
        )
        self.image(
            name="./src/img/logoJamar.jpg",
            x=10,
            y=30,
            w=60
        )
        self.set_font("helvetica", "B", 15)
        self.cell(80)
        self.cell(w=30, h=10, txt="PAZ Y SALVO", align="C")

    # def body(self):
    #     self.multi_cell(
    #         txt=""
    #         )

    # def footer(self):
    #     self.image(
    #         name="./src/img/footer.jpg"
    #     )

pdf = PDF(
    orientation="P",
    unit="mm",
    format="A4"
    )

pdf.add_page()
pdf.set_font(family="Times", size=12)
pdf.output("./src/tests/test1.pdf")