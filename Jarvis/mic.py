import speech_recognition as sr
import whisper
import queue
import os
import threading
import click
import torch
import numpy as np


@click.command()
@click.option("--model", default="tiny", help="Model to use", type=click.Choice(["tiny", "base", "small", "medium", "large"]))
@click.option("--energy", default=300, help="Energy level for mic to detect", type=int)
@click.option("--dynamic_energy", default=False, is_flag=True, help="Flag to enable dynamic energy", type=bool)
@click.option("--pause", default=0.8, help="Pause time before entry ends", type=float)
def main(model, energy, pause, dynamic_energy):
    model = model + ".en"
    audio_model = whisper.load_model(
        model, download_root=f"{os.path.dirname(os.path.abspath(__file__))}/models")
    audio_queue = queue.Queue()
    result_queue = queue.Queue()

    threading.Thread(target=record_audio,
                     args=(audio_queue, energy, pause, dynamic_energy)).start()
    threading.Thread(target=transcribe_forever,
                     args=(audio_queue, result_queue, audio_model)).start()

    while True:
        print(result_queue.get())


def record_audio(audio_queue, energy, pause, dynamic_energy):
    # load the speech recognizer and set the initial energy threshold and pause threshold
    r = sr.Recognizer()
    r.energy_threshold = energy
    r.pause_threshold = pause
    r.dynamic_energy_threshold = dynamic_energy

    with sr.Microphone(sample_rate=16000) as source:
        while True:
            audio = r.listen(source)

            torch_audio = torch.from_numpy(np.frombuffer(
                audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)
            audio_data = torch_audio

            audio_queue.put_nowait(audio_data)


def transcribe_forever(audio_queue, result_queue, audio_model):
    while True:
        audio_data = audio_queue.get()
        result = audio_model.transcribe(audio_data, language='english')
        result_queue.put_nowait(result["text"])


main()
