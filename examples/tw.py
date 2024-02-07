from py import ButtonStylesTW, Button

cool_style = ButtonStylesTW(
    buttonColor={"Red": 500},
    fontColor="Offwhite",
    size="Md"
)

button = Button(text="Click me!", onclick="""alert('IT WORKED')""", styles=cool_style)

button.write_to_file(method="w")