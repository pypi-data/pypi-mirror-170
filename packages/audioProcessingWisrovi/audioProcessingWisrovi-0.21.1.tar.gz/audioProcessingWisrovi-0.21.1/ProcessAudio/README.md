# ProcessAudio
 Libreria python para extraer caracteristicas a audios

## Initialization

```bash
pip install audioProcessingWisrovi
```

A `ProcessAudio` object should be created and use its attributes.

```python
from audioProcessingWisrovi import ProcessAudio
processAudio = ProcessAudio()
processAudio.set_data("audio_file.wav")
caracteristicas = processAudio.get_all()  # Extrayendo caracteristicas audios, salen 26 caracteristicas
```

### ProcessAudio methods

* `get_all()`: returns all featuresconfigured folder, returns the new filename.

