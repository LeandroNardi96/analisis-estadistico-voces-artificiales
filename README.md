# Análisis Estadistico Test de Voces Artificiales

<img src="https://edsurge.imgix.net/uploads/post/image/11432/AWS_Amazon_Transcribe-1537508848.jpg?auto=compress%2Cformat&w=640&h=259&fit=crop" width="710">

[![Python](https://img.shields.io/badge/python-3.11.2-blue)](https://www.python.org/)
[![Papermill](https://img.shields.io/badge/papermill-2.4.0-green)](https://papermill.readthedocs.io/en/latest/)
[![Pandas](https://img.shields.io/badge/pandas-1.5.3-yellow)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.2.2-orange)](https://scikit-learn.org/)
[![Seaborn](https://img.shields.io/badge/seaborn-0.12-red)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/plotly-5.14.1-brightgreen)](https://plotly.com/)
[![Statsmodels](https://img.shields.io/badge/statsmodels-0.14.0-blueviolet)](https://www.statsmodels.org/)


## Índice

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [test-result](#test-result)
- [Contribución](#contribución)

## Descripción

Este proyecto consiste en analizar si el género es un factor de influencia a la hora de calificar los parámetros subjetivos de voces artificiales, como también realizar regresiones entre los parámetros objetivos y subjetivos, con el fin de estudiar relaciones entre ellos y comprender mejor como estos se vinculan entre sí. Las notebooks que permiten realizar estos análisis son:

- sample_population.ipynb: analiza como se distribuye la muestra estadística tomada.
- mann_whitney_test.ipynb: realiza el test de Mann Whitney para saber si el género es factor de influencia.
- preprocess_regression.ipynb: etapa de preprocesamiento para poder realizar las regresiones (aquí se aplica el MOS).
- parametric_regression.ipynb: realiza las regresiones lineales paramétricas.
- no_parametric_regression.ipynb: realiza las regresiones lineales no paramétricas.

## Instalación

Para ejecutar este proyecto se necesita tener instalado Python 3.6 o superior y las siguientes librerías:

- papermill 2.X o superior
- pandas 1.X
- numpy 1.X
- scikit-learn 1.X
- seaborn 0.X o superior
- statsmodels 0.X o superior
- plotly 5.X o superior

Se recomienda usar un ambiente virtual para instalar las librerías y evitar conflictos con otras versiones. Se puede crear un ambiente virtual **(para Windows)** usando los comandos:

Crea un ambiente virtual llamado venv
```bash
python -m venv venv
```
Activa el ambiente virtual
```bash
venv/scripts/activate
```
Instala las librerías y las actualiza si es necesario
```bash
pip install -r requirements.txt --upgrade
```

En caso de usar Linux o Mac, los comandos cambian un poco su sintaxis. Se recomenda revisar como crear ambientes virtuales en dichos OS si se desea ejecutar el código en alguna distribución de Linux o Mac.

## Uso
Para usar este proyecto, se deben seguir los siguientes pasos:

1. Se deberán crear las siguientes carpetas para evitar problemas (ya que el script, no contempla que no existan las carpetas y que el mismo las cree):
    - aux_file
    - notebook-output
    - test-result

Esta última tiene una estructura similar, la se detallará en un propio apartado. Todas las carpetas, deben estar en el mismo directorio donde se encuentran los archivos .ipynb.

2. Ejecutar el notebook `main.ipynb` o `main.py`. Ambos files se encargan de llamar a los otros notebooks con los parámetros adecuados mediante papermill. Los resultados de cada notebook se guardan en archivos con el sufijo _output.ipynb en la carpeta `notebook-output`. Los archivos auxiliares que se van creando asociados a cada flujo de ejecución, se guardan en la carpeta `aux_file`

Se pueden ejecutar cada notebook por separado, siguiendo el orden de ejecución. Aunque se recomienda que la primera vez, se ejecute desde los orquestadores para que se cree todo junto y si se quiere analizar una notebook en particular, ejecutarla esa misma, sin problema. Aunque si se quiere ver los resultados de las notebooks, pueden verse en la carpeta `notebook-output`

## test-result

Esta carpeta tiene una estructura muy particular, la cual es la siguiente:

```bash
test-result/
    back-up-muestra/
    mann-whitney/
    regressions/
        no-parametric/
            Acentuacion/
                femenino/
                masculino/
            Cadencia/
                femenino/
                masculino/
            Inteligibilidad/
                femenino/
                masculino/
            Naturalidad/
                femenino/
                masculino/
            Pronunciacion/
                femenino/
                masculino/
        parametric/
            Acentuacion/
                femenino/
                masculino/
            Cadencia/
                femenino/
                masculino/
            Inteligibilidad/
                femenino/
                masculino/
            Naturalidad/
                femenino/
                masculino/
            Pronunciacion/
                femenino/
                masculino/
    sample-population/
```

Se deberá crear a mano todas las carpetas y subcarpetas como se muestra en el árbol de directorios, y además en la carpeta `test-result`, se deberá los siguientes 2 archivos (los cuales, enviaré por mail):

- caso_mati.csv
- Test_Subjetivo_Analisis_de_voces_artificiales_Submissions.csv

Una vez ejecutado todas las notebooks (a mano o con el orquestador), el arbol de directorios completo quedará:

```bash
test-result/
    ├── Test_Subjetivo_Analisis_de_voces_artificiales_Submissions.csv
    back-up-muestra/
        ├── Test_Subjetivo_Analisis_de_voces_artificiales_Submissions.csv
    ├── caso_mati.csv
    mann-whitney/
        ├── df_output_mannwhitney.xlsx
    regressions/
        no-parametric/
            Acentuacion/
                femenino/
                    ├── regresiones_acentuacion_female.png
                masculino/
                    ├── regresiones_acentuacion_male.png
            Cadencia/
                femenino/
                    ├── regresiones_cadencia_female.png
                masculino/
                    ├── regresion_cadencia_multivariable_male.html
                    ├── regresiones_cadencia_male.png
            Inteligibilidad/
                femenino/
                    ├── regresion_inteligibilidad_multivariable_female.html
                    ├── regresiones_inteligibilidad_female.png
                masculino/
                    ├── regresiones_inteligibilidad_male.png
            Naturalidad/
                femenino/
                    ├── regresion_naturalidad_multivariable_female.html
                    ├── regresiones_naturalidad_female.png
                masculino/
                    ├── regresion_naturalidad_multivariable_male.html
                    ├── regresiones_naturalidad_male.png
            Pronunciacion/
                femenino/
                    ├── regresion_pronunciacion_multivariable_female.html
                    ├── regresiones_pronunciacion_female.png
                masculino/
                    ├── regresiones_pronunciacion_male.png
            ├── output_p_values_no_parametric_regressions.xlsx
        parametric/
            Acentuacion/
                femenino/
                    ├── regresion_acentuacion_multivariable_female.html
                    ├── regresiones_acentuacion_female.png
                masculino/
                    ├── regresiones_acentuacion_male.png
            Cadencia/
                femenino/
                    ├── regresiones_cadencia_female.png
                masculino/
                    ├── regresiones_cadencia_male.png
            Inteligibilidad/
                femenino/
                    ├── regresion_inteligibilidad_multivariable_female.html
                    ├── regresiones_inteligibilidad_female.png
                masculino/
                    ├── regresiones_inteligibilidad_male.png
            Naturalidad/
                femenino/
                    ├── regresion_naturalidad_multivariable_female.html
                    ├── regresiones_naturalidad_female.png
                masculino/
                    ├── regresiones_naturalidad_male.png
            Pronunciacion/
                femenino/
                    ├── regresion_pronunciacion_multivariable_female.html
                    ├── regresiones_pronunciacion_female.png
                masculino/
                    ├── regresion_pronunciacion_multivariable_male.html
                    ├── regresiones_pronunciacion_male.png
            ├── output_p_values_parametric_regressions.xlsx
    sample-population/
        ├── distribucion_muestra_estadistica.png
        ├── edad.png
        ├── experiencia_TTS.png
        ├── genero.png
        ├── lugar_geografico.png
```
**IMPORTANTE**: El repo consta de varios otros archivos, como por ejemplo `plot_features_v3.py`, los cuales se usaron para obtener las visualizaciones de los audios de las voces artificiales, como también archivos para crear un orden aleatoreo de las voces (para el test) y demás. En este README **no esta contemplado** la explicación de creación de carpetas y subcarpetas para que los mismos funcionen, como tampoco los audios de las voces. De querer ejecutar otra cosa que no sean los archivos detallados en este escrito, se deberá consultarle al creador o bien debbuguear los files para poder crear las carpetas y subcarpetas mecesarias. Dato no menor, también se le deberá pedir al dev que envíe los audios de las voces artificiales creadas.

## Contribución

Este proyecto consta para la finalización de mi tesis de grado y no tiene fines comerciales. Si quieres contribuir a mejorar el código o la documentación, puedes hacer un fork del repositorio y enviar un pull request con tus cambios.

<br>

### <p align="center"> Made with &#x2764; for Everyone</p>
