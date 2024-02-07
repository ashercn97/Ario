from py import Text, TextDefaults, Grid, Card, Modal, ButtonModal, Button, ButtonStyles

header = TextDefaults(variant="Header").get()
header_text = Text(content="Hi, I'm Asher.", styles=header)
paragraph = TextDefaults(variant="Paragraph").get()

my_card = Card(
    title="Asher's Card!",
    title_style=header,
    content=Text(content="This is so much fun!", styles=paragraph),
    filepath="./simpleexample.html"
)

my_modal = Modal(
    id="myModal",
    title="Asher is so cool",
    title_style=header,
    content=Text(content="OMG im so awesome", styles=paragraph),
)

open_modal_code = ButtonModal(id=my_modal.id).get()

open_modal_button = Button(
    text="open modal",
    onclick=open_modal_code,
    styles=ButtonStyles(backgroundColor="Secondary", size="Large", borderRadius="Rounded-LG"),
)

my_grid = Grid(rows=4, cols=4, gap=15)

my_grid.add_item(header_text, row_start=1, col_start=1)
my_grid.add_item(my_card, row_start=2, col_start=3)
my_grid.add_item(my_modal, row_start=1, row_end=2, col_start=1, col_end=2)
my_grid.add_item(open_modal_button, row_start=2, col_start=2)

my_grid.write_to_file(method="w")