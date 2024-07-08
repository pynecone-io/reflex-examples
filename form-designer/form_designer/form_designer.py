import reflex as rx

import reflex_local_auth

from . import constants, routes, utils
from .components import (
    FieldEditorState,
    FormEditorState,
    field_edit_title,
    form_edit_title,
)
from .pages import (
    FormEntryState,
    ResponsesState,
    form_editor_page,
    home_page,
    form_entry_page,
    form_entry_success,
    responses_page,
    responses_title,
)


# Add these dynamic route vars early, so they can be referenced in the titles.
if "form_id" not in rx.State.__fields__:
    rx.State.add_var("form_id", str, "")
if "field_id" not in rx.State.__fields__:
    rx.State.add_var("field_id", str, "")

app = rx.App(theme=rx.theme(accent_color="blue"))
app.add_page(home_page, route="/", title=constants.TITLE)

# Authentication via reflex-local-auth
app.add_page(
    reflex_local_auth.pages.login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)
app.add_page(
    reflex_local_auth.pages.register_page,
    route=reflex_local_auth.routes.REGISTER_ROUTE,
    title="Register",
)

# Field editing routes
app.add_page(
    form_editor_page,
    route=routes.FIELD_EDIT_ID,
    title=field_edit_title(),
    on_load=[FormEditorState.load_form, FieldEditorState.load_field],
)
app.add_page(
    form_editor_page,
    route=routes.FIELD_EDIT_NEW,
    title=field_edit_title(),
    on_load=[FormEditorState.load_form, FieldEditorState.load_field],
)

# Form editing routes
app.add_page(
    form_editor_page,
    route=routes.FORM_EDIT_ID,
    title=form_edit_title(),
    on_load=FormEditorState.load_form,
)
app.add_page(
    form_editor_page,
    route=routes.FORM_EDIT_NEW,
    title=form_edit_title(),
    on_load=FormEditorState.load_form,
)

# Form entry routes
app.add_page(
    form_entry_page,
    route=routes.FORM_ENTRY,
    title=rx.cond(
        rx.State.form_id == "",
        utils.quoted_var("Unknown Form"),
        FormEntryState.form.name,
    ),
    on_load=FormEntryState.load_form,
)
app.add_page(
    form_entry_success,
    route=routes.FORM_ENTRY_SUCCESS,
    title="Form Response Saved",
)

# Response viewing routes
app.add_page(
    responses_page,
    route=routes.RESPONSES,
    title=responses_title(),
    on_load=ResponsesState.load_responses,
)

# Create the database if it does not exist (hosting service does not migrate automatically)
rx.Model.migrate()