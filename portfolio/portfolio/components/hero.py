import reflex as rx

def hero() -> rx.Component:
    return rx.vstack(
        rx.heading("John Doe", size="2xl", margin_bottom="4"),
        rx.text(
            "Full Stack Developer & Software Engineer",
            color=rx.color_mode.current.text,
            margin_bottom="6",
        ),
        rx.hstack(
            rx.link(
                rx.button("View Projects", size="lg"),
                href="#projects",
            ),
            rx.link(
                rx.button("Contact Me", size="lg", variant="outline"),
                href="#contact",
            ),
            spacing="4",
        ),
        padding_y="20",
        spacing="4",
        align_items="center",
    )
