# Zodiaco


Com este pacote voçê pode descobrir o signo de qualquer pessoa com base na sua data de nascimento.
Métodos disponiveis:

	- getSigno()
	- getCor()
	- getNumeroSorte()

## Instalação

Use o gerenciador de instalação de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar zodiaco

```bash
pip install zodiaco
```

## Exemplo de uso

```python
from zodiaco.signos import getSignos
signo = getSignos.getSigno('1980-04-27')
print(signo)
print(getSignos.getCor(signo))
print(getSignos.getNumeroSorte(signo))
```

## Author
Julio Cesar Bueno de Oliveira

## License
[MIT](https://choosealicense.com/licenses/mit/)