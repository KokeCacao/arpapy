# arpapy

Multilingual text/IPA to ARPAbet G2P for text2speech generation.

## Installation
```bash
sudo apt install espeak-ng
pip install arpapy
```

## Quick Start
```python
from arpapy import get_arpa

s: str = '"Marron glacé is in my DNA." adiós'
print(get_arpa(s)) # ['M', 'AA1', 'R', 'AX0', 'N', '/', 'G', 'L', 'AA0', 'S', 'EY1', '/', 'IH0', 'Z', '/', 'IH0', 'N', '/', 'M', 'AY0', '/', 'D', 'IY2', 'EH2', 'N', 'EY1', '-', 'EY1', 'D', 'IH0', 'AX2', 'UH0', 'Z']
```

## Citation

See [CREADITS.md](CREDITS.md) for all credits.

```
@misc{arpapy,
  title={arpapy: Multilingual text/IPA to ARPAbet G2P for text2speech generation.},
  author={Koke_Cacao},
  year={2025},
  howpublished={\url{https://github.com/KokeCacao/arpapy}},
  note={Open-source software}
}
```
