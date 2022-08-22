from fpdf import FPDF
import json
from index_price import get_index_price_chart

WIDTH = 210
HEIGHT = 297
MARGIN = 10
LOGO_SCALE = 60

class PDF(FPDF):

    def make_page(self):
        # Make generic page with constant properties
        self.add_page()
        self.add_font(
            family='Lato',
            fname='resources\Lato-Regular.ttf',
            uni=True
        )
        self.add_font(
            family='Lato_b',
            fname='resources\Lato-Bold.ttf',
            uni=True
        )
        self.set_font(family='Lato', size=16)
        self.image(
            name=r'resources\big.jpg',
            x=140,
            y=3,
            w=3466/LOGO_SCALE,
            h=420/LOGO_SCALE
        )

        self.set_draw_color(0, 214, 101)
        self.set_line_width(0.5)


    def make_title_div(self, index):
    
        # Name
        self.set_font(family='Lato_b', size=16)
        self.cell(
            w=0, h=15, txt=mapping[index]['long_name'], border=0
        )
        self.set_font(family='Lato', size=11)
        self.line(MARGIN, 21, WIDTH-MARGIN, 21)

        # Description
        self.set_y(23)
        self.set_font(family='Lato', size=9)
        self.multi_cell(
            w=185, h=4, txt=mapping[index]['description']
        )

        return

    def make_key_feature_div(self, index):

        self.set_xy(MARGIN, 38.5)
        self.set_font(family='Lato_b', size=16)
        self.cell(
            w=0, h=0, txt='Key Features', border=0
        )
        self.line(MARGIN, 41.5, WIDTH-MARGIN, 41.5)

        # Chart
        get_index_price_chart(index, 180)
        self.image(
            name=fr'resources\{index}_price.jpg', x=5, y=43, w=120, h=60
        )

        # Text
        self.set_font(family='Lato_b', size=9)
        self.set_xy(120, 44)
        self.cell(
            w=0, h=0, txt='Size Requirements', border=0
        )
        self.set_font(family='Lato', size=9)
        self.set_xy(120, 46)
        self.multi_cell(
            w=(WIDTH/2)-3*MARGIN,
            h=4,
            txt=mapping[index]['size_requirements']
        )

        self.set_font(family='Lato_b', size=9)
        self.set_xy(120, 58)
        self.cell(
            w=0, h=0, txt='Review', border=0
        )
        self.set_font(family='Lato', size=9)
        self.set_xy(120, 60)
        self.multi_cell(
            w=(WIDTH/2)-3*MARGIN,
            h=4,
            txt=mapping[index]['review']
        )
        

        return


    def save_pdf(self):
        self.output('mvda_factsheet.pdf', 'F')
        return


    def compile_pdf(self, index):
        self.make_page()
        self.make_title_div('MVDA')
        self.make_key_feature_div('MVDA')
        self.save_pdf()
        return

if __name__ == '__main__':
    f = open('index_mappings.json')
    mapping = json.load(f)
    mvda = PDF()
    mvda.compile_pdf('MVDA')