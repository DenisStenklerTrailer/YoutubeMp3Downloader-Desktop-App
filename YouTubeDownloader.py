import PySimpleGUI as sg
import pytube as YouTube
import os
import errno

# row 1:
label1 = sg.Text("Enter a download link: ")
input1 = sg.Input(key="link")
# row 2:
label2 = sg.Text("Enter a dist directory: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose",key="folder")

compress_button = sg.Button("Download")
exit_button = sg.Button("Exit")

complete_label = sg.Text("", key="output")

window = sg.Window("YouTube MP3 downloader", layout=[[label1, input1],[label2, input2, choose_button2],[compress_button, complete_label],[exit_button]], element_justification="center")


while True:

    event, values = window.read()

    if event == "Download":
        link = str(values["link"])

        folder = values["folder"]

        yt = YouTube.YouTube(link)

        t = yt.streams.filter(only_audio=True).first()

        out_file = t.download(output_path=folder)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'

        try:
            os.rename(out_file, new_file)
            window["output"].update(f"{t.title} has been downloaded sucessfully!")
        except FileExistsError:
            window["output"].update("File already exists!")

    if event == "Exit":
        break
    elif sg.WIN_CLOSED == event:
        # print(event)
        break

window.close()