[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

# **Movile Code Challenge 3**

## [**Challenges**](https://www.hackerrank.com/contests/movile-code-challenge-3/challenges)

Desafio online de programação do Grupo Movile.

> ## [**Reuniões Movilepay**](https://www.hackerrank.com/contests/movile-code-challenge-3/challenges/reunioes-movilepay)

* reunioes_movilepay.py
  
  Na MovilePay, assim como provavelmente na maioria das empresas, são necessárias reuniões, apresentações e encontros entre mais de uma pessoa para que alinhamentos e decisões sejam tomados.

  Nos dias atuais e, dado todo o contexto global que estamos vivendo, no qual as pessoas estão tendo que se reinventar por conta da pandemia que esta terrível doença que é o COVID-19 acarretou, as reuniões e uma boa organização para tal têm um papel ainda mais fundamental.

  No entanto, apesar de termos nos adaptado a esse novo contexto, onde reuniões são cada vez mais necessárias, gostaríamos da sua ajuda para melhorar ainda mais nosso dia a dia, construindo uma ferramenta capaz de prever o melhor horário de uma reunião dado um grupo de pessoas e suas respectivas agendas para um determinado dia.

  **Input Format**

  Você vai receber como entrada o número de pessoas (**N**, com 0 < **N** <= 1000), a quantidade de horas que a reunião que desejamos marcar vai durar (**T**, com 0 < **T** < 24), e a agenda de cada pessoa em um determinado dia da semana, com cada uma das suas reuniões (**a**,**b**), que será no formato:

  a1,b1 a2,b2 a3,b3 … aX,bY

  Por exemplo: "0,2 6,7 12,14 20,22 13,15", onde 0,2 significa que a reunião inicia as 0h e se encerra as 2h.

  Onde: **aJ**: É a hora em que uma reunião **J** inicia na agenda da pessoa **a** 
  **bJ**: É a hora em que uma reunião **J** se encerra na agenda da pessoa **a**

  **Constraints**
  * A agenda de uma pessoa pode ter um número qualquer de reuniões nesse dia.
  * Não irão existir nessa entrada valores concorrentes para uma agenda de uma pessoa (como por exemplo 1,3 2,4), em que reuniões possuam intervalos de horários concomitantes.
  * Os horários das reuniões não estarão necessariamente ordenados para uma determinada pessoa. Por exemplo, 5,6 por vir antes de 1,2.
  * Os valores das horas de cada reunião são inteiros que variam de **0 até 23**, representando todas as horas de um dia.
  * Os valores de cada reunião serão ordenados, ou seja, **a < b** para **a,b**.
  
  **Output Format**

  Você deverá imprimir o primeiro horário possível em que todas as N pessoas na entrada conseguem participar da reunião de T horas, onde X é a hora de início e Y a hora de fim:

  **O primeiro horario possivel para a reuniao eh das Xh00 as Yh00**

  Caso não seja possível nenhum horário que contemple a agenda de todos, deverá imprimir a mensagem:

  **Nao existe horario no dia para marcar a reuniao**

  **Sample Input 0**
  ```
  2
  3
  1,4 12,14 6,8 10,12
  2,3 5,6 20,22
  ```
  **Sample Output 0**
  ```
  O primeiro horario possivel para a reuniao eh das 14h00 as 17h00
  ```
  **Sample Input 1**
  ```
  3
  5
  12,14 20,23
  0,20
  1,2 3,4
  ```
  **Sample Output 1**
  ```
  Nao existe horario no dia para marcar a reuniao
  ```

> ## [**Senha Forte Movilepay**](https://www.hackerrank.com/contests/movile-code-challenge-3/challenges/senha-forte-movile-pay)

* [senha_forte_movilepay.py](https://github.com/JonatasFontele/movile-code-challenge-3/blob/main/senha_forte_movilepay.py)
  * Used [Regex](https://docs.python.org/3/library/re.html) to solve it.

  Na Movile Pay, assim como na maioria das empresas que estão na web, precisamos garantir que as senhas informadas sejam fortes e difíceis de quebrar.

  Podemos considerar uma senha forte aquela que atenda os seguintes requisitos:
  * Tamanho mínimo de 6 caracteres.
  * Deve conter pelo menos um dígito numérico [0-9]
  * Deve conter pelo menos um caractere minúsculo [a-z]
  * Deve conter pelo menos um caractere maiúsculo [A-Z]
  * Deve conter ao menos um caractere especial [!@#$%^&*()-+]
  * Para não deixar um cliente informar uma senha fraca precisamos informá-lo qual o valor mínimo de caracteres que precisam ser informados para que a senha seja considerada forte.

  **Input Format**
  
  O programa precisa receber dois parâmetros:
  * Int n = Tamanho da senha para ser validada
  * String password = Senha para ser testada.
 
  **Constraints**
  * 1 <= n <= 100
  * Todos os caracteres de password devem respeitar [a-z], [A-Z], [0-9] e [!@#$%^&*()-+]
  
  **Output Format**
  * O programa deverá imprimir um inteiro que representa qual o valor mínimo de caracteres que precisam ser adicionados nessa senha para ela ser considerada segura.
  * Para o caso em que a senha não precisa de nenhum caracter para ser considerada segura, imprimir o valor zero (0).
  
  **Sample Input 0**
  ```
  6
  qwe
  ```
  **Sample Output 0**
  ```
  3
  ```
  **Explanation 0**
  
  Essa senha pode ficar forte adicionando 3 caracteres a mais. Eu posso adicionar "2#A", nesse caso ela ficaria qwe2#A, tonando assim uma senha forte.

  **Sample Input 1**
  ```
  7
  tesaA
  ```
  **Sample Output 1**
  ```
  2
  ```
  **Explanation 1**
  
  Essa senha pode ficar forte adicionando um número e um caractere especial.
  
  **Sample Input 2**
  ```
  8
  am4n$aB2
  ```
  **Sample Output 2**
  ```
  0
  ```
  **Explanation 2**
  
  Senha atende todas as condições acima, portanto pode ser considerada uma senha forte.

> ## [**Promobomb Movilepay & iFood**](https://www.hackerrank.com/contests/movile-code-challenge-3/challenges/promobomb-movilepay-ifood)

* promobomb_movilepay_e_ifood.py
  
  O ifood está engajado diariamente a atrair novos clientes. Um dos meios de atingir esse objetivo é criando as promo-bombs, uma oferta relâmpago, com algum tipo de desconto ao cliente.

  Você foi escolhido para ajudar a Movilepay a criar uma plataforma que maximize o lucro das ações para o iFood. Tendo em mente todas as ações possíveis planejadas pelo time de comercial do iFood, você precisará selecionar as **três ações que gerem um maior lucro, de acordo com as duas respectivas funções abaixo**:
  * R(x) = 4x²
  * C(x) = 100x

  **R(x)** é a função da receita obtida pelo iFood, em função do número de pessoas x da ação.

  **C(x)** é a função do custo necessário em função do número de pessoas x da ação.

  **Input Format**

  Você vai receber como entrada o número de ações **N**, e em sequência N linhas, onde cada linha representa uma ação **A**, que terá o formato:

  **A: 'a' x**

  Onde:
  * **a**: Nome da ação, que estará entre aspas simples.
  * **x**: Número de pessoas que serão impactadas.
 
  Por exemplo:

  'Acao do comercial' 2000

  **Constraints**
  * 3 <= N <= 1000
  * 0 < x <= 1000000
  * Em caso de empate entre duas ou mais ações, selecioná-las pela ordem de entrada, na ordem em que aparecem primeiro.
  
  **Output Format**

  Você deverá imprimir a posição de entrada das três ações que maximizem o lucro em função do número de pessoas.

  **Sample Input 0**
  ```
  5
  'Acao maluca' 3000
  'Acao ifood' 5000
  'Acao movilepay' 5005
  'Acao simpla' 10
  'Acao movile' 50
  ```
  **Sample Output 0**
  ```
  3
  2
  1
  ```
