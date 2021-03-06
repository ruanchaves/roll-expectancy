# expectation.py

Programa feito para ilustrar a esperança matemática dos lançamentos de um dado honesto.

![](https://i.imgur.com/JkV1asn.gif)

# Dependências

Matplotlib.

    sudo apt-get install python3-matplotlib

ou

    sudo -H pip3 install matplotlib

E caso queira fazer GIFs:

    sudo apt-get install imagemagick

# Uso

    python3 expectation.py n b

* **n** : Número de imagens a serem geradas.

* **b** : Informe 0 para sobrepor com gráficos anteriores, 1 para não sobrepor.

As imagens geradas serão criadas na mesma pasta onde o script é executado. 

# Exemplos

O eixo y vai de 1 a 6 ( as faces do dado ) e o eixo x está em escala de log10.

    python3 expectation.py 30 0

Depois rodamos:

    convert -resize 768x576 -delay 20 -loop 0 `ls -tr expectation_*` animacao.gif

E essa é a animação das 30 imagens geradas:

![](https://i.imgur.com/yhlNqzh.gif)

Ou então, sem sobreposição:

    python3 expectation.py 30 1
    convert -resize 768x576 -delay 200 -loop 0 `ls -tr expectation_*` animacao.gif

E temos:

![](https://i.imgur.com/JkV1asn.gif)

# Detalhes

* O método de geração dos números aleatórios, a quantidade de faces do dado, a altura da assíntota e outras configurações podem ser alteradas ao começo do arquivo.

Exemplo: Dado de 20 faces, de 1 até 10^100 lançamentos, com esperança em 10.5, 5 gráficos de lançamento por imagem:

![](https://i.imgur.com/F4Odjt6.png)

# hipster-expectation

![](https://i.imgur.com/jmSl7UX.png)

Existe também uma versão que pode ser executada puramente na linha de comando e usa [hipsterplot](https://github.com/imh/hipsterplot) ao invés de pyplot.

Ela está disponível no repl.it e pode ser executada de qualquer dispositivo com acesso a internet.

[Executar hipster-expectation](https://repl.it/@ruanchaves/hipster-expectation)
