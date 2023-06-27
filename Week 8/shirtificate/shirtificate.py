from fpdf import FPDF

def main():
    shirtify(input("Name: "))


def shirtify(name):
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica", size=60)
    pdf.cell(190, 30, txt="CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png", x=10, y=60, w=190)
    pdf.set_font("Helvetica", size=25)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(-190, 240, txt=f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()