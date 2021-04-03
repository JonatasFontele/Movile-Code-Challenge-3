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
  
  
> ## [**Saldo Promocional Movilepay**](https://www.hackerrank.com/contests/movile-code-challenge-3/challenges/saldo-promocional-movilepay)

* saldo_promocional_movilepay.py

  Uma das atividades da MovilePay é a disponibilização de saldos promocionais para seus usuários. Os saldos promocionais podem ser disponibilizados em uma carteira digital através de depósitos e possuem um período de validade para serem consumidos.

  Para ser justo na hora de uma compra utilizando esses saldos promocionais, considere a seguinte regra para o consumo dos saldos:

  * Os saldos devem ser consumidos com a prioridade por **menor quantidade de dias para a expiração**.
  * Em caso de empate no primeiro critério, **deve ser considerado como prioridade o item de menor valor de depósito**.
  * Caso o saldo disponível somando todos os depósitos seja menor do que o valor da compra, a compra não deve ser efetuada e o saldo não deve ser consumido.
  
  Dado uma lista composta por D inteiros representando depósitos, e uma lista composta por C quantidade de compras, imprima uma lista com o estado final dos valores de cada um dos depósitos.

  **Input Format**

  A primeira linha contém um inteiro D que representa a quantidade de depósitos de uma determinada carteira.

  As DV linhas subsequentes representam um depósito no formato DV E - DV: representando o valor do depósito. - E: representando a quantidade de dias até a expiração do depósito.

  Em seguida temos um valor C representando a quantidade de compras. As C linhas subsequentes representam tentativas de compras no formato CV - CV: representando um valor de uma compra.

  **Constraints**

  1 ≤ DV ≤ 5000

  0 ≤ E ≤ 5000

  1 ≤ C ≤ 5000

  1 ≤ CV ≤ 5000

  **Output Format**

  Imprima a lista de depósitos contendo o valor final de todos os D depósitos após o consumo de saldo pelas C compras, ordenados na ordem de consumo proposta no exericicio.

  **Sample Input 0**
  ```
  4
  30 1
  43 1
  1 3
  123 2
  2
  40
  30
  ```
  **Sample Output 0**
  ```
  0
  3 
  123
  1
  ```
  **Explanation 0**

  **4 depósitos**:

  1. valor: 30, 1 dia para expirar
  2. valor: 43, 1 dia para expirar
  3. valor: 1, 3 dias para expirar
  4. valor: 123, 2 dias para expirar
  
  **após a ordenação**:

  1. valor: 30, 1 dia para expirar
  2. valor: 43, 1 dia para expirar
  3. valor: 123, 2 dias para expirar
  4. valor: 1, 3 dias para expirar
 
  **2 compras**:

  1. valor 40
  2. valor 30
  
  **Depósitos após primeira compra**:

  1. valor: 0, 1 dia para expirar
  2. valor: 33, 1 dia para expirar
  3. valor: 123, 2 dias para expirar
  4. valor: 1, 3 dias para expirar
  
  **Depósitos após segunda compra**:

  1. valor: 0, 1 dia para expirar
  2. valor: 3, 1 dia para expirar
  3. valor: 123, 2 dias para expirar
  4. valor: 1, 3 dias para expirar
  
  **Sample Input 1**
  ```
  7
  1 15
  20 1
  1 1
  100 15
  35 0
  3 100
  5 2
  3
  5000
  100
  20
  ```
  **Sample Output 1**
  ```
  0
  0
  0
  0
  0
  42
  3
  ```
  **Explanation 1**

  **7 depósitos**:

  1. valor: 1, 15 dia para expirar
  2. valor: 20, 1 dias para expirar
  3. valor: 1, 1 dia para expirar
  4. valor: 100, 15 dias para expirar
  5. valor: 35, 0 dias para expirar
  6. valor: 3, 100 dias para expirar
  7. valor: 5, 2 dias para expirar
  
  **após a ordenação**:

  1. valor: 35, 0 dias para expirar
  2. valor: 1, 1 dia para expirar
  3. valor: 20, 1 dias para expirar
  4. valor: 5, 2 dias para expirar
  5. valor: 1, 15 dia para expirar
  6. valor: 100, 15 dias para expirar
  7. valor: 3, 100 dias para expirar
  
  **3 compras**:

  1. valor 5000 - Rejeitada pois não há valor suficiente
  2. valor 100
  3. valor 20
  
  **Depósitos após segunda compra**:

  1. valor: 0, 0 dias para expirar
  2. valor: 0, 1 dia para expirar
  3. valor: 0, 1 dias para expirar
  4. valor: 0, 2 dias para expirar
  5. valor: 0, 15 dia para expirar
  6. valor: 62, 15 dias para expirar
  7. valor: 3, 100 dias para expirar
  
  **Depósitos após terceira compra**:

  1. valor: 0, 0 dias para expirar
  2. valor: 0, 1 dia para expirar
  3. valor: 0, 1 dias para expirar
  4. valor: 0, 2 dias para expirar
  5. valor: 0, 15 dia para expirar
  6. valor: 42, 15 dias para expirar
  7. valor: 3, 100 dias para expirar
  
  
> ## [**Quantidade possível de saques Movilepay**](https://www.hackerrank.com/contests/movile-code-challenge-3/challenges/quantidade-possivel-de-saques-movilepay)

* quantidade_possivel_de_saques_movilepay.py
  
  Em instituições financeiras, como a **MovilePay**, é comum existir a opção de **saque** de dinheiro em terminais bancários (ATM), para isso, é calculada uma combinação possível de notas para que o saque possa ser efetuado dado um montante desejado.

  Escreva uma função que retorne as diferentes maneiras de mostrar quantas combinações de saque pode ser feito a partir de um valor informado.

  Por exemplo, existem **3** combinações possíveis para sacar o valor de **4** com as cédulas de **1** e **2**:

  1. 1+1+1+1
  2. 1+1+2
  3. 2+2
  
  **Input Format**

  Você deverá ler um número que representa o valor desejado para o saque (**N**, com 0 < **N** <= 1000) e um array de números inteiros separados por espaço informando as cédulas existentes no ATM (**C**, sendo **C** um número inteiro menor que o máximo de **N**)

  **Constraints**

  * A ordem das combinações de saque não importam: 1+1+2 == 2+1+1;
  * Assuma também, que temos um limite infinito de cédulas/moedas para o saque;
  * Sua função deve receber o montante total para o saque e uma lista de inteiros que equivalem às cédulas/moedas únicas;
  * O valor do saque deve ser um número entre 0 e 1000;
  * A lista de cédulas disponíveis deve ser de valores inteiros separados por espaço;
  
  **Output Format**

  A saída do código deve ser o número da quantidade de maneiras possíveis para se sacar o dinheiro informado.

  Se o valor não corresponder aos limites informados, deverá retornar: -1.

  **Sample Input 0**
  ```
  4
  1 2
  ```
  **Sample Output 0**
  ```
  3
  ```
  **Sample Input 1**
  ```
  10
  2 5
  ```
  **Sample Output 1**
  ```
  2
  ```
  **Sample Input 2**
  ```
  -100
  1
  ```
  **Sample Output 2**
  ```
  -1
  ```
  **Sample Input 3**
  ```
  1234
  1 2 3 4
  ```
  **Sample Output 3**
  ```
  -1
  ```


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
  
  
> ## [**Conectividade entre datacenters Movile**](https://www.hackerrank.com/contests/movile-code-challenge-3/challenges/conectividade-entre-datacenters-movile)

* conectividade_entre_datacenters_movile.py

  A Movile como uma holding é uma empresa que preza para interação entre as empresas do grupo, tanto que um serviço de uma das empresas pode e deve ser utilizado por outras empresas do grupo sempre que necessário.

  As integrações entre os serviços são feitas através da rede de computadores. Para garantir que os serviços prestados ao usuário final seja rápido e de qualidade, é necessário que a conectividade entre os clientes e os servidores seja impecável.

  Desse modo, a Movile montou um plano juntamente com os administradores dos datacenters das empresas do grupo com objetivo de implantar uma tecnologia nova de rotas para conectar todos os datacenters do grupo Movile.

  Os administradores dos datacenters fornecerão uma lista de rotas entre os servidores da Movile e seus custos de implantação.

  Todos os datacenters devem estar dentro dessa nova rede e todos devem estar conectados entre si, mas não necessariamente via conexões diretas.

  Assim, sua função é analisar a tabela de rotas e custos e reportar quanto será o custo mínimo para garantir a implantação dessa nova tecnologia de conectividade.

  A figura a seguir mostra um exmeplo de rede otimizada, as rota em vermelho são as rotas que devem ser implantadas:

  [![alt text](https://s3.amazonaws.com/hr-assets/0/1533449015-1b07ea5ea6-grafo.png "Grafo movile")](https://s3.amazonaws.com/hr-assets/0/1533449015-1b07ea5ea6-grafo.png)

  **Input Format**

  A primeira linha conterá um número D que representa quantos datacenters das empresas do grupo Movile existe (os datacenters são representados por um número de identificação que começa do 1 e vai até D). Na linha seguinte haverá um número R que representa a quantidade de rotas existentes. Cada um das seguintes R linhas conterá 3 números (A B C) onde A e B representam identificadores de datacenter e C é o custo para criar aquela conexão entre os datacenters A e B. EX:
  4
  4
  1 2 3
  2 3 1
  2 4 7
  3 4 1

  **Constraints**

  Os valores dados são todos inteiros positivos
  1 < D < 70
  C < 50

  **Output Format**

  A saída deve conter um número que representa o custo mínimo possível para fazer a melhoria na rede. EX:
  5

  **Sample Input 0**
  ```
  4
  4
  1 2 3
  2 3 1
  2 4 7
  3 4 1
  ```
  **Sample Output 0**
  ```
  5
  ```
