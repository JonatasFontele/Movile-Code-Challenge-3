[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

# **Movile Code Challenge 3**

## [**Challenges**](https://www.hackerrank.com/contests/movile-code-challenge-3/challenges)

Desafio online de programação do Grupo Movile.

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

* [promobomb_movilepay_e_ifood.py](https://github.com/JonatasFontele/movile-code-challenge-3/blob/main/senha_forte_movilepay.py)
  
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
