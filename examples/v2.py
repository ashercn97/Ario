from py import write_to_file, EventHandler, TextStyles, StatefulText, StatefulButton, ButtonStyles
from pydantic import BaseModel
from typing import Optional



initial_state = {
    "text": "true",
    "styles": ButtonStyles(backgroundColor="Primary", borderRadius="Rounded", size="Medium").get()
}

click_handler = EventHandler(event="click", action="text = !text")

stateful_button = StatefulButton(
    initial_state=initial_state,
    event_handlers={"click": click_handler}
)

stateful_button.write_to_file(method='w')