import threading
import time
from tqdm import tqdm
from time import sleep

import PySimpleGUI as Gui
from components import mainFunctions as mF

Gui.theme('SystemDefault')  # window theme
Gui.set_options(font=("Copper", 11))  # default font

THREAD_EVENT = '-THREAD-'

selection_layout = [  # second position argument for button type, cannot use 'center'
    [Gui.Text('Source Folder', size=(50, 1)), Gui.FolderBrowse(size=(10, 1), key="INPUT_FOLDER")],
    [Gui.Text('Destination Folder', size=(50, 1)),
     Gui.FolderBrowse(size=(10, 1), key="OUTPUT_FOLDER")]]

box = [Gui.Multiline('  ', size=(60, 10), background_color='black', text_color='White', pad=(5, 5), key='SCREEN',
                     autoscroll=True,
                     reroute_stdout=True, write_only=True)]

selection = [[Gui.Text('Format'),
              Gui.Combo([name for name in mF.support_formats], key="FORMAT", pad=(10, 0),
                        default_value=mF.support_formats[0]),
              Gui.Text('  Max Width'), Gui.InputText('1920', size=(5, 1), key="MAX_WIDTH"), Gui.Text('Pixel')]]

buttons_layout = [  # second position argument for button type, cannot use 'center'
    [Gui.Button('Start'), Gui.Cancel()]]

layout = [[Gui.Column(selection_layout, element_justification='left', expand_x=True)],
          [Gui.Column(selection), Gui.Column([[Gui.Text('Quality')]], element_justification='right', expand_x=True)],
          [Gui.Column([box]),
           Gui.Slider(range=(1, 100), default_value=100, key="QUALITY", tooltip="Image Quality by %", orientation='v',
                      size=(8, 20))],
          [Gui.Column(buttons_layout, element_justification='right', expand_x=True)]]

# [Gui.Text('Source for Folders', size=(15, 1)), Gui.InputText(), Gui.FolderBrowse()]

window = Gui.Window('Python Bulk Image Compressor', layout, size=(600, 360),
                    margins=(5, 5), finalize=True)  # icon='media/079.ico'


def screen_updater(set_time_end, set_time_start):
    window['SCREEN'].update(
        window['SCREEN'].get() + f"\nFinished in: {round(set_time_end - set_time_start, 2)} Seconds")


while True:
    event, values = window.read()
    start = window['Start']
    # folder_path, file_path = values[0], values[1]
    # check_box = values[2], values[3]
    if event == 'Cancel' or event is None:
        break
    elif event == 'Start':

        text = ""
        for char in tqdm(["a", "b", "c", "d"]):
            sleep(0.25)
            text = text + char
            window['SCREEN'].update(window['SCREEN'].get() + f"\n {text}")
        # start.update(disabled=True)
        time_start = time.time()
        print("")
        isEmptyOutput = "./Data/Out/" if values["OUTPUT_FOLDER"] == '' else values["OUTPUT_FOLDER"]

        # mF.start_command(str(values["INPUT_FOLDER"]), str(isEmptyOutput),
        #                  str(values["FORMAT"]).replace('.', ""),
        #                  int(values["MAX_WIDTH"]), int(values["QUALITY"]))

        time_end = time.time()
        threading.Thread(target=screen_updater(time_end, time_start), daemon=True).start()

    elif event == 'End':
        start.update(disabled=False)

window.close()
