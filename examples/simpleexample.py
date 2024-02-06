from py import Text, TextDefaults, Grid

header = TextDefaults(variant="Header").get()
header_text = Text(content="Hi, I'm Asher.", styles=header, output="./simpleexample.html")


my_grid = Grid(rows=4, cols=4, gap=15)

my_grid.add_item(header_text, row_start=1, col_start=1)

my_grid.write_to_file("./simpleexample.html")