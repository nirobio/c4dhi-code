# c4dhi-code
Niro Yogendran
10th Dec 2021
---

Brief:

Take 2-3 days to write a small Android application which classifies singing vs speaking vs silence of the last 2 seconds based on microphone sensor data. Your solution should utilize at least one machine learning approach. You are welcome to make use of third party libraries as long as they are not pre-trained on the specific task at hand. The classification results should be displayed on the screen.


In case you accept this challenge, provide us with a small set of slides describing your approach, the commented source code, and a compiled .apk supporting Android 6.0+.

---

**This is a brief overview of my approach to the problem**

- Develop simple mobile application with Flutter & Dart, which is to be compiled into an .apk file. Interface should have one Elevated Button with a microphone icon and text reading "Start". On pressing, the button state will switch and the text will read "Stop". Consider using Flutter-Sounds-Lite library for ease. Audio file will be saved in .mp3 format to local device (user must permit microphone and write access on button press (permission_handler package)). 

- File will be trimmed so only last 2s is available for analysis. It is possible to convert file 16kHz and mono channel to match model input data, but uncertain whether this is a necessary step.

- To simplify the problem, use Root Mean Square (RMS) to detect unvoiced/silent segments from the speech signal using a power threshold. This should enable detection of true silence but would not correctly detect background noise, for example, which could also be considered silence.

- Based on the previous step, the trimmed audio file should be classified as silence or sound. If silence, display this result on screen. If not, move to next step.

- This is now a binary classification problem of speech and singing. For speech detection, the Librispeech (train-clean-100) dataset and the LJSpeech dataset are used. These are entirely English language speak with a strong bias for American English. The data vary from 1s - 5s sample lengths and include male and female speakers.

- For singing detection, a corpus of music with lyrics is used from the Free Music Archive (FMA) and GTZAN database which provide ~30s segments. Most data contain background instrumental music + voice, but some are a capella only. Speech + singing =~40GB data.

- Convert .mp3, .flac and .wav files to WAV-PCM format which is readily accepted by the Wavfile (scipy.io) using ffmpeg unix script.

- Define a threshold envelope and remove data outwith. Downsample all files and convert to mono channel. Resample at 16kHz. Save samples in 1s segments.

- At this point, consider whether any class imbalances are evident. I suspect the speech class will emerge as the majority class and may require downsampling or the minority singing class may be upscaled, or both using imbalanced-learn.

- Generate mel-spectrograms and mel-frequency cepstral coefficients (MFCCs) to be used as the input layer.

- Split each class into 80:20 train-test-split by speaker/singer.

- Train data on CNNs (Conv1d; Conv2d) and RNN (LSTM) for ~50 epochs to begin, and consider early stopping if necessary.

- generate model files and csv files with train/validation accuracy and loss per epoch. Matplotlib graph the latter. 

- Generate confusion matrices and ROC-AUC curves.

- Predict classes (predict.py) on unseen mel-spectrograms/MFCCs files.

- If models display sufficient accuracy, convert into TFLite Flatbuffer format for mobile deployment and load into Flutter using flutter-tflite. 

- load locally saved audio files if classified as sound, convert to spectral domain and classify. Display class label and confidence once result available.

- compile as .apk
