import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

import customtkinter as ctk
import os
import torch
#import torchaudio
#from transformers import AutoModelForCausalLM, AutoTokenizer
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voice
import vlc
from tkVideoPlayer import TkinterVideo


app =tk.TK()
app.geometry("700x700")
app.title("Justris")
ctk.set_appearance_mode("dark")








app.mainloop()
