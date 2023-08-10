import gradio as gr
from gradio import components
from pathlib import Path
import os
#@markdown #Seperation
#@markdown *Run this cell to sperate your audio*
def process_data(input_path, output_path, ChunkSize, vocalsOnly):

    folder_path = input_path.name
    output_folder = output_path



    filename =  Path(folder_path).stem
    Path(output_folder,filename).mkdir(parents=True, exist_ok=True)
    os.system(f'python inference.py --large_gpu --chunk_size {ChunkSize} --input_audio "{folder_path}" --vocals_only "{vocalsOnly}" --output_folder "{output_folder}"/"{filename}"')
    return f"Your audio has been seperated, and saved to {output_folder}/{filename}."

input_path = components.File()
output_path = gr.Textbox(label="Output Path", value = "/content/drive/MyDrive/output")

chunk_size = components.Slider(minimum=-100000, maximum=500000, label="Chunk Size",info = "Use a lower Chunk Size if you are having memory issues.", value = 500000)
vocalsOnly = components.Checkbox(label="Vocals Only", info = "Check this to only Split the Vocals and Instrumental. This may speed up processing.", show_label=True)

interface = gr.Interface(
    fn=process_data,
    inputs=[input_path, output_path, chunk_size, vocalsOnly],
    outputs="text",
    allow_flagging='never'
)

interface.queue().launch(share = True, debug = True)
