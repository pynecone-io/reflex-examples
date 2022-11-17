"""Welcome to Pynecone! This file create a counter app."""
import pynecone as pc
import random


class State(pc.State):
    """The app state."""
    count = 0

    def increment(self):
        """Increment the count."""
        self.count += 1

    def decrement(self):
        """Decrement the count."""
        self.count -= 1
    
    def random(self):
        """Randomize the count."""
        self.count = random.randint(0, 100)
    
def index():
    """The main view."""
    return pc.center(
        pc.vstack(
            pc.heading(State.count),
            pc.hstack(
                pc.button("Increment", on_click=State.increment, color_scheme = "green"),
                pc.button(
                    "Randomize", 
                    on_click=State.random, 
                    background_image="linear-gradient(90deg, rgba(0,176,34,1) 0%, rgba(255,0,0,1) 100%)",
                    color="white"
                ),
                pc.button("Decrement", on_click=State.decrement, color_scheme = "red"), 
            ),
            padding = "1em",
            bg = "#ededed",
            border_radius = "1em",
            box_shadow = "lg"
        ),
        padding_y="5em",
        font_size="2em",
        text_align="center",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, title="Counter")
app.compile()
api = app.api
