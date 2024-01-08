import asyncio
import os
from typing import List

import reflex as rx


class State(rx.State):
    """The app state."""

    # Whether we are currently uploading files.
    is_uploading: bool

    @rx.var
    def file_str(self) -> str:
        """Get the string representation of the uploaded files."""
        return "\n".join(os.listdir(rx.get_asset_path()))

    async def handle_upload(self, files: List[rx.UploadFile]):
        """Handle the file upload."""
        self.is_uploading = True

        # Iterate through the uploaded files.
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_asset_path(file.filename)
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

        # Stop the upload.
        return State.stop_upload

    async def stop_upload(self):
        """Stop the file upload."""
        await asyncio.sleep(1)
        self.is_uploading = False


color = "rgb(107,99,246)"


def index():
    return rx.vstack(
        rx.upload(
            rx.button(
                "Select File(s)",
                height="70px",
                width="200px",
                color=color,
                bg="white",
                border=f"1px solid {color}",
            ),
            rx.text(
                "Drag and drop files here or click to select files",
                height="100px",
                width="200px",
            ),
            border="1px dotted black",
            padding="2em",
        ),
        rx.hstack(
            rx.button(
                "Upload",
                on_click=State.handle_upload(rx.upload_files()),
            ),
        ),
        rx.heading("Files:"),
        rx.cond(
            State.is_uploading,
            rx.progress(is_indeterminate=True, color="blue", width="100%"),
            rx.progress(value=0, width="100%"),
        ),
        rx.text_area(
            is_disabled=True,
            value=State.file_str,
            width="100%",
            height="100%",
            bg="white",
            color="black",
            placeholder="No File",
            min_height="20em",
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index, title="Upload")
