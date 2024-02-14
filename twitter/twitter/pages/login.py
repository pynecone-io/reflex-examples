"""Login page. Uses auth_layout to render UI shared with the sign up page."""
import reflex as rx
from twitter.layouts import auth_layout
from twitter.state.auth import AuthState


def login():
    """The login page."""
    return auth_layout(
        rx.box(
            rx.vstack(
                rx.input(placeholder="Username", on_blur=AuthState.set_username, margin_bottom="12px",),
                rx.input(
                    type_="password",
                    placeholder="Password",
                    on_blur=AuthState.set_password,
                    margin_bottom="12px",
                ),
                rx.button(
                    "Log in",
                    on_click=AuthState.login,
                    color="white",
                    size="3",
                ),
                spacing="3",
            ),
            align_items="left",
            background="white",
            border="1px solid #eaeaea",
            padding="16px",
            max_width="400px",
            border_radius="8px",
        ),
        rx.text(
            "Don't have an account yet? ",
            rx.link("Sign up here.", href="/signup"),
            color="gray",
        ),
    )