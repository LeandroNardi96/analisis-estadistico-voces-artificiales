import librosa
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


def create_path_to_plot(path, folder):
    """
    Dado un path y una carpeta, devuelve un nuevo path con la
    carpeta añadida como subdirectorio.

    :param path: str
        El path original del archivo.
    :param folder: str
        La carpeta a añadir como subdirectorio.
    :return: str
        El nuevo path con la carpeta añadida como subdirectorio.
    """
    # Crear el nuevo directorio
    new_path = os.path.join(path, folder)

    if not os.path.exists(new_path):
        os.mkdir(new_path)

    return new_path


def extract_features(audio_path):
    """
    Extrae características de un archivo de audio.

    Args:
        audio_path (str): Ruta del archivo de audio.

    Returns:
        dict: Un diccionario que contiene las características extraídas:
            - 'zero_crossing_rate': Tasa de cruce por cero promedio.
            - 'rms': Valor RMS promedio.
            - 'mfcc': Coeficientes cepstrales de frecuencia promedio.
            - 'pitch': Valor de pitch promedio.
    """
    y, sr = librosa.load(audio_path, sr=None)
    zcr = librosa.feature.zero_crossing_rate(y)
    rms = librosa.feature.rms(y=y)
    rms_avg = np.mean(rms)
    rms_avg_np = np.array([rms_avg])
    rms_db = librosa.amplitude_to_db(rms_avg_np)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    f0, voiced_flag, voiced_probs = librosa.pyin(
            y,
            fmin=librosa.note_to_hz('C2'),
            fmax=librosa.note_to_hz('C7')
        )
    pitch = f0[voiced_flag > 0]

    features = {
        'zero_crossing_rate': np.mean(zcr),
        'rms': rms_db[0],
        'mfcc': np.mean(mfcc, axis=1),
        'pitch': pitch.mean()
    }

    return features, y, sr


def plot_mel_spectrogram(
    y,
    sr,
    fig,
    ax,
    n_mels=128,
    cmap='magma'
):
    """
    Genera y visualiza un Mel Spectrogram a partir de una señal de audio.

    Args:
        - y: ndarray de 1 dimensión
            Señal de audio.
        - sr: int
            Tasa de muestreo de la señal de audio.
        - n_mels: int, opcional (default=128)
            Número de coeficientes Mel a calcular.
        - figsize: tuple, opcional (default=(10, 6))
            Tamaño de la figura del gráfico.
        - cmap: str, opcional (default='coolwarm')
            Colormap a utilizar para la visualización.

    Returns:
        None
    """
    # Calcular Mel Spectrogram
    mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels)

    # Convertir a decibeles
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)

    # Visualizar el Mel Spectrogram
    img = librosa.display.specshow(
        mel_spectrogram_db,
        y_axis='mel',
        x_axis='time',
        sr=sr,
        hop_length=512,
        cmap=cmap,
        ax=ax
    )
    fig.colorbar(img, format='%+2.0f dB', aspect=5, pad=0.01)
    plt.title('Espectrograma de Mel', fontsize=14, pad=15)
    plt.xlabel('Tiempo [s]', fontsize=12, labelpad=10)
    plt.ylabel('Frecuencia [Hz]', fontsize=12, labelpad=10)
    plt.tick_params(axis='both', labelsize=10)
    plt.tight_layout()


def plot_pitch(y, sr):
    """
    Genera un gráfico de la frecuencia fundamental (pitch)
    de un archivo de audio.

    Args:
        y (array): Señal de audio.
        sr (int): Tasa de muestreo de la señal de audio.
        pathname (str): Ruta de archivo para guardar el gráfico.
        figsize (tuple, opcional): Tamaño de la figura del gráfico.

    Returns:
        None
    """
    # Grafico el Pitch
    f0, voiced_flag, voiced_probs = librosa.pyin(
            y,
            sr=sr,
            fmin=librosa.note_to_hz('C2'),
            fmax=librosa.note_to_hz('C7')
        )
    pitch = f0[voiced_flag > 0]
    plt.plot(
        librosa.frames_to_time(np.arange(len(pitch))),
        pitch,
        alpha=1,
        color='black',
        linewidth=2
    )
    plt.title('Frecuencia Fundamental', fontsize=14, pad=15)
    plt.xlabel('Tiempo [s]', fontsize=12, labelpad=10)
    plt.xlim(0, len(y)/sr)
    plt.ylabel('Frecuencia [Hz]', fontsize=12, labelpad=10)
    plt.ylim(bottom=0)  # Fijo el límite inferior del eje y en 0
    plt.grid()  # Oculto las líneas de la cuadrícula
    plt.tick_params(axis='both', labelsize=10)
    plt.tight_layout()


def plot_zcr(y, sr):
    """
    Genera un gráfico de la tasa de cruce por cero (Zero Crossing Rate)
    de un archivo de audio.

    Args:
        y (array): Señal de audio.
        sr (int): Tasa de muestreo de la señal de audio.
        pathname (str): Ruta de archivo para guardar el gráfico.
        figsize (tuple, opcional): Tamaño de la figura del gráfico.

    Returns:
        None
    """
    # Grafico el ZCR
    zcr = librosa.feature.zero_crossing_rate(y)
    times = librosa.times_like(zcr)
    plt.plot(times, zcr[0], alpha=1, color='black', linewidth=2)
    plt.xlabel('Tiempo [s]', fontsize=12, labelpad=10)
    plt.ylabel('ZCR', fontsize=12, labelpad=10)
    plt.title('Tasa de Cruce por Cero', fontsize=14, pad=15)
    plt.xlim(0, len(y)/sr)
    plt.ylim(bottom=0)  # Fijo el límite inferior del eje y en 0
    plt.grid()  # Oculto las líneas de la cuadrícula
    plt.tick_params(axis='both', labelsize=10)
    plt.tight_layout()


def plot_rms(y, sr):
    """
    Genera un gráfico de la Energía de una Señal (Root Mean Square) en dB.

    Args:
        y (array): Señal de audio.
        sr (int): Tasa de muestreo de la señal de audio.
        figsize (tuple, opcional): Tamaño de la figura del gráfico.

    Returns:
        None
    """
    # Grafico el RMS
    rms = librosa.feature.rms(y=y)
    rms_db = librosa.amplitude_to_db(rms, ref=np.max)  # Convertir RMS a dB
    times = librosa.times_like(rms)
    plt.plot(times, rms_db[0], alpha=1, color='black', linewidth=2)
    plt.xlabel('Tiempo [s]', fontsize=12, labelpad=10)
    plt.ylabel('RMS [dBFS]', fontsize=12, labelpad=10)
    plt.title('Energía (RMS)', fontsize=14, pad=15)
    plt.xlim(0, len(y)/sr)
    plt.ylim(bottom=None)
    plt.grid()
    plt.tick_params(axis='both', labelsize=10)
    plt.tight_layout()


def plot_audio_features(y, sr, path, filename, figsize=(12, 12)):
    """
    Crea un gráfico con cuatro subplots, uno debajo del otro, con las
    siguientes características de audio: pitch, zero crossing rate,
    root mean square y mel spectrogram.

    Args:
        y (array): Señal de audio.
        sr (int): Tasa de muestreo de la señal de audio.
        figsize (tuple, opcional): Tamaño de la figura del gráfico.

    Returns:
        fig, ax (tuple): Objetos de figura y subplots creados.
    """
    fig = plt.figure(figsize=figsize)

    # Subplot 1: Mel Spectrogram
    ax1 = plt.subplot(4, 1, 1)
    plot_mel_spectrogram(y, sr, fig, ax1)

    # Subplot 2: Pitch
    plt.subplot(4, 1, 2)
    plot_pitch(y, sr)

    # Subplot 3: Zero Crossing Rate
    plt.subplot(4, 1, 3)
    plot_zcr(y, sr)

    # Subplot 4: Root Mean Square
    plt.subplot(4, 1, 4)
    plot_rms(y, sr)

    plt.tight_layout()
    plt.savefig(os.path.join(path, filename))
    plt.close()


PATH = os.getcwd()
GRAPHIC_FOLDER = 'graficos'
AUDIO_FOLDER = 'voces'
VOCES_RMS = 'voces_rms'
SUBFOLDERS = ['masculino', 'femenino']
OUTPUT_FOLDER = 'features'
FEATURES_FILE = 'features.xlsx'
features_list = []

if not os.path.exists(os.path.join(PATH, GRAPHIC_FOLDER)):
    os.mkdir(GRAPHIC_FOLDER)

if not os.path.exists(os.path.join(PATH, OUTPUT_FOLDER)):
    os.mkdir(OUTPUT_FOLDER)

for subfolder in SUBFOLDERS:

    graphic_path = os.path.join(PATH, GRAPHIC_FOLDER, subfolder)

    if not os.path.exists(graphic_path):
        os.mkdir(graphic_path)

    audio_folder_path = os.path.join(PATH, AUDIO_FOLDER, subfolder, VOCES_RMS)
    files = os.listdir(audio_folder_path)

    for file in files:

        if not file.endswith('.wav'):
            continue

        audio_file_path = os.path.join(audio_folder_path, file)
        features, y, sr = extract_features(audio_file_path)
        features = {key: [value] for key, value in features.items()}
        features.update({'genero': [subfolder]})
        features_list.append(features)
        # graphic_folder = file.replace('.wav', '')
        graphic_filename = file.replace('.wav', '.png')
        # graphic_file_path = create_path_to_plot(graphic_path, graphic_folder)
        plot_audio_features(
            y=y,
            sr=sr,
            path=graphic_path,
            filename=graphic_filename
        )

dataset_features = pd.DataFrame()

for features in features_list:
    df_features = pd.DataFrame.from_dict(features, orient='columns')
    dataset_features = pd.concat([dataset_features, df_features], axis=0)
    dataset_features = dataset_features.sort_values('zero_crossing_rate')

dataset_features.to_excel(
    os.path.join(PATH, OUTPUT_FOLDER, FEATURES_FILE),
    index=False
)
