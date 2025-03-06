# Cifra de cesar

A ideia desse projeto é representar uma biblioteca capaz de executar a cifra de cesar (ROT13)

## Exemplos de uso

### Encriptação

```python
from cesar import encripta

encripta('victor')  # ivpgbe
```

### Decriptação
```python
from cesar import decripta

decripta('ivpgbe')  # victor
```

### Rotações diferentes de 13
```python
from cesar import decripta, encripta

encripta('victor')  # jwqhcf
decripta('jwqhcf', 14)  # victor
```