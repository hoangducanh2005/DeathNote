from nicegui import ui
from datetime import datetime
import time
from uuid import uuid4

from app.storage import load_notes, save_notes
from app.styles import DEATHNOTE_CSS


class DeathNotePage:
    def __init__(self):
        self.notes = load_notes()
        self.ensure_note_timestamps()

        self.note_input = None
        self.counter_label = None
        self.notes_container = None
        self.delete_dialog = None

        self.selected_note_id = None

    def ensure_note_timestamps(self):
        changed = False
        now_ts = time.time()
        for note in self.notes:
            if "created_at_ts" not in note:
                note["created_at_ts"] = now_ts
                changed = True
        if changed:
            save_notes(self.notes)

    def create(self):
        ui.page_title("DeathNote")
        ui.add_head_html(DEATHNOTE_CSS)

        self.create_delete_dialog()

        with ui.column().classes("w-full min-h-screen items-center px-6 py-8"):
            ui.label("DeathNote").classes("death-title")
            ui.label("A dark notebook for your thoughts").classes("death-subtitle mb-6")

            with ui.card().classes("main-book w-full max-w-5xl p-6"):
                with ui.row().classes("w-full gap-6"):
                    with ui.column().classes("flex-1 gap-4"):
                        ui.label("Write a new page").classes("text-2xl font-bold text-red-700")

                        self.note_input = ui.textarea(
                            label="Your note",
                            placeholder="Write something here..."
                        ).props(
                            "outlined autogrow clearable autofocus"
                        ).classes(
                            "death-input w-full"
                        )

                        with ui.row().classes("items-center gap-4"):
                            ui.button(
                                "Add to DeathNote",
                                icon="edit_note",
                                on_click=self.add_note
                            ).props("unelevated").classes("bg-red-900 text-white")

                            self.counter_label = ui.label("").classes("text-gray-400")

                    with ui.column().classes("rule-box w-full md:w-80 p-4 rounded-xl"):
                        ui.label("Rules").classes("text-xl font-bold text-red-700")
                        ui.label("1. Every written page is saved.").classes("text-sm")
                        ui.label("2. Deleted pages cannot be restored.").classes("text-sm")
                        ui.label("3. This is only a note-taking app.").classes("text-sm")
                        ui.label("4. Do not write anything you may regret.").classes("text-sm")

            self.notes_container = ui.column().classes("w-full max-w-3xl gap-4 mt-6")

        self.update_counter()
        self.render_notes()
        ui.timer(1.0, self.render_notes)

    def update_counter(self):
        self.counter_label.set_text(f"{len(self.notes)} page(s) written")

    def add_note(self):
        content = self.note_input.value

        if content is None:
            content = ""

        content = content.strip()

        if content == "":
            ui.notify("You must write something first.", color="warning")
            return

        new_note = {
            "id": str(uuid4()),
            "content": content,
            "created_at": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "created_at_ts": time.time(),
        }

        self.notes.insert(0, new_note)
        save_notes(self.notes)

        self.note_input.set_value("")
        self.update_counter()
        self.render_notes()

        ui.notify("A new page has been written.", color="positive")

    def render_notes(self):
        self.notes_container.clear()

        with self.notes_container:
            if len(self.notes) == 0:
                with ui.card().classes("empty-card w-full p-6"):
                    ui.label("The notebook is empty...").classes("text-xl")
                    ui.label("Write your first note above.").classes("text-gray-400")
                return

            for note in self.notes:
                with ui.card().classes("note-card w-full p-5"):
                    with ui.row().classes("w-full justify-between items-start"):
                        with ui.column().classes("gap-1"):
                            ui.label("DEATH NOTE PAGE").classes("page-title")
                            ui.label(note["created_at"]).classes("text-xs text-gray-400")

                        ui.button(
                            "Delete",
                            icon="delete",
                            color="red",
                            on_click=lambda note_id=note["id"]: self.request_delete(note_id)
                        ).props("flat")

                    ui.separator().classes("my-3")

                    ui.label(note["content"]).classes("note-content")

                    if self.is_dead(note):
                        with ui.row().classes("gap-2 mt-3"):
                            ui.label("đã chết").classes("text-white bg-red-800 px-2 py-1 rounded text-xs")
                            ui.label("heart attack").classes("text-white bg-black px-2 py-1 rounded text-xs")

    def is_dead(self, note):
        created_at_ts = note.get("created_at_ts")
        if created_at_ts is None:
            return False
        return (time.time() - float(created_at_ts)) >= 40

    def request_delete(self, note_id):
        self.selected_note_id = note_id
        self.delete_dialog.open()

    def create_delete_dialog(self):
        with ui.dialog() as dialog:
            with ui.card().classes("p-6 bg-black text-white"):
                ui.label("Delete this page?").classes("text-2xl font-bold text-red-600")
                ui.label("This action cannot be undone.").classes("text-gray-400 mt-2")

                with ui.row().classes("w-full justify-end mt-4"):
                    ui.button("Cancel", on_click=dialog.close).props("flat")
                    ui.button("Delete", color="red", on_click=self.confirm_delete)

        self.delete_dialog = dialog

    def confirm_delete(self):
        if self.selected_note_id is None:
            return

        self.notes = [
            note for note in self.notes
            if note["id"] != self.selected_note_id
        ]

        save_notes(self.notes)

        self.selected_note_id = None
        self.delete_dialog.close()

        self.update_counter()
        self.render_notes()

        ui.notify("The page has been deleted.", color="negative")