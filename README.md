[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

# **Movile Code Challenge 3**

## [**Challenges**](https://www.hackerrank.com/contests/movile-code-challenge-3/challenges)

Desafio online de programação do Grupo Movile.

> ## [**Senha Forte Movilepay**](https://www.hackerrank.com/contests/movile-code-challenge-3/challenges/senha-forte-movile-pay)

* senha_forte_movilepay.py
  * This algorithm only got 7 out of 8 cases.
  * Used [Regex](https://docs.python.org/3/library/re.html) to solve it.

  Na Movile Pay, assim como na maioria das empresas que estão na web, precisamos garantir que as senhas informadas sejam fortes e difíceis de quebrar.

  Podemos consideramos uma senha forte aquela que atenda os seguintes requisitos:
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
