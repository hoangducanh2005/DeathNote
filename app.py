from nicegui import ui

notes = []


def add_note():
    text = note_input.value.strip()

    if text == '':
        ui.notify('Vui lòng nhập nội dung note!', color='warning')
        return

    notes.append(text)
    note_input.value = ''
    note_list.refresh()


def delete_note(index):
    notes.pop(index)
    note_list.refresh()


@ui.refreshable
def note_list():
    if len(notes) == 0:
        ui.label('Chưa có note nào.').classes('text-gray-500 mt-4')
        return

    with ui.column().classes('w-full gap-3 mt-4'):
        for index, note in enumerate(notes):
            with ui.card().classes('w-full p-4'):
                with ui.row().classes('w-full items-center justify-between'):
                    ui.label(note).classes('text-lg')
                    ui.button(
                        'Delete',
                        color='red',
                        on_click=lambda i=index: delete_note(i)
                    )


ui.label('DeathNote').classes('text-3xl font-bold text-red-700')

with ui.card().classes('w-full max-w-xl p-6'):
    note_input = ui.input(
        label='Write your note',
        placeholder='Nhập note ở đây...'
    ).classes('w-full')

    ui.button('Add', on_click=add_note).classes('mt-2')

    note_list()

ui.run(title='DeathNote')