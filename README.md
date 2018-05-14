Programa feito para ilustrar a esperança matemática dos lançamentos de um dado honesto.

# Dependências

Matplotlib.

> sudo apt-get install python3-matplotlib

ou

> sudo -H pip3 install matplotlib

# Uso

> python3 expectancy.py n b

* **n** : Número de imagens a serem geradas.

* **b** : Informe 0 para sobrepor com gráficos anteriores, 1 para não sobrepor.

As imagens geradas serão criadas na mesma pasta onde o script é executado. 

# Exemplos

O eixo y vai de 1 a 6 ( as faces do dado ) e o eixo x está em escala de log10.

> python3 convergence.py 30 0

Depois rodamos:

>convert -resize 768x576 -delay 20 -loop 0 `ls -tr expectancy_*` animacao.gif

E essa é a animação das 30 imagens geradas:

![](https://i.imgur.com/yhlNqzh.gif)
