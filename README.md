# Documentação Notion
### ***Classes criadas e suas responsabilidades e a** visibilidade dos atributos e métodos e o motivo dessas escolhas*

### ***—Classe banco (concreta)—***

Essa classe representa o banco é a gestão de seus clientes. 

Sua responsabilidade é cadastrar os clientes e gerenciá-los.

***Métodos —***

**get_nome e get_endereço :** tem a função de retornar o nome e o endereço de cada cliente.

**cadastrar_Cliente :** tem a função de cadastrar novos clientes.

**get_clientes :** Mostra a lista de clientes cadastrados.

***Atributos —***

**__nome** = nome do banco 

**__endereço** = endereço do banco

**__clientes** = lista de clientes (objetos). 

---

### **—Classe cliente (concreta)—**

Essa classe representa um cliente do banco e seu próprio gerenciamento.

Ou seja, um cliente tem uma ou mais contas e tem a capacidade de gerenciá-las seguindo os métodos abaixo. 

***Métodos —***

**add_conta :** Cria uma conta de cliente. 

**remover_conta :** Exclui uma conta de cliente. 

**listar_contas :** Faz uma lista das contas, contendo o número e o saldo.

**Getters/Setters :** Acesso de dados pessoais de um cliente.

***Atributos —*** 
**__nome , __sobrenome , __cpf , __idade , __endereco** = São os dados pessoais dos clientes.

---

### **—Classe OperacoesFinaceiras (abstrata)—**

Tem a responsabilidade de definir operações básicas que todas os tipos de conta devem ter.

***Métodos —***  

sacar (quantidade) 

depositar (quantidade)

transferir (quantidade)

Isso garante que todos os tipos de conta (poupança e corrente) tenham esses métodos. 

---

### —Classe conta (abstrata)—

É o modelo para os diferentes tipos de conta. 

Define o que toda conta bancária deve ter e fazer, mas não implementa diretamente.

Herda **OperacoesFinanceiras,** que define os métodos sacar, depositar e transferir. 

***Métodos —*** 

**Gets :** Precisam ser implementados por subclasses. 

**sacar, depositar, saldo :** são definidos pela classe herdada (OperacoesFinanceiras).

***Atributos —*** 

**__numero :** Representa o número da conta 

**__senha :** A senha para acesso

**__saldo :** O saldo disponível.

---

### **—Classe corrente (concreta)—**

Representa uma conta corrente, que faz operações simples. 

Herda da classe **conta.**

**Métodos —** 

**depositar -** adiciona um valor ao saldo.

**sacar -** permite o saque de uma valor, caso seja o suficiente.

**transferir -** permite a transferência de valor, se houver suficiente. 

---

### **—Classe poupança (concreta)—**

Herda da classe **conta.**

Representa uma conta poupança, com os métodos abaixo:

***Métodos —*** 

**depositar -** adiciona um valor ao saldo.

**sacar -** permite o saque de uma valor, caso seja maior ou igual a 100.

**transferir -** permite a transferência de valor, se houver saldo maior ou igual a 100.

### *A justificativa de cada relacionamento (associação, agregação, composição)*

### **Banco / cliente → Agregação**

O banco agrega vários clientes, porém não é dono de nenhum deles. 

Ou seja, o cliente existe independentemente do banco. 

O banco armazena os clientes, sem poder modifica-los. 

---

### Cliente / conta → Composição

O cliente é dono de suas contas, então se o cliente for apagado as contas relacionadas a ele também são apagadas. 

Ou seja, as contas dependem da existência dos clientes. 

---

### **Conta / OperacoesFinaceiras → Herança**

A classe OperaçõesFinanceiras define os métodos que devem estar presente em qualquer tipo de conta, seja ela corrente ou poupança. 

A classe conta herda os métodos de OperacoesFinanceiras, isso garante que todos os tipos de conta possuam tais métodos. 

---

### Conta / Corrente e Poupança → Herança

A Corrente e Poupança herdam os métodos da conta, sendo assim, ambas se fazem diferentes tipos de conta, ambas com os métodos da classe conta. Entretanto, cada uma possui específicações, que as tornam diferentes.

### *A aplicação dos conceitos de POO e as razões de cada implementação.*

### Abstração —

***Aplicação-***

A abstração são as classes banco, cliente e conta que representam elementos do mundo real. 

A Classe OperacoesFinanceiras serve de modelo genérico para os tipos de contas possíveis.

***Por que a abstração foi utilizada?***

O motivo do uso da abstração foi para que novas contas possam ser criadas utilizando este mesmo padrão, mantendo uma constância no funcionamento do código. 

---

### Encapsulamento —

***Aplicação-***

O (__) declara a privação dos atributos, que podem ser alterados apenas por métodos gets e setters

Ex: 

self.__saldo → pode ser alterado por get_Saldo

***Por que o encapsulamento foi utilizado?***

Foi utilizado com o intuito de proteger os dados de cada cliente, de modo a impedir que informações pessoais fossem alteradas por outras partes do código. 

---

### Herança —

***Aplicação***-

A classe conta herda os métodos de OperacoesFinanceiras, fazendo com que todas as contas repliquem o mesmo comportamento. 

As classes Corrente e Poupança herdam da classe conta, isso permite que contas poupança e corrente tenham certos comportamentos padronizados. 

***Por que a herança foi utilizada?***

A herança serve como um reaproveitamento de código, fazendo com que não seja necessário a repetição de um mesmo padrão várias vezes. 

---

### Polimorfismo—

***Aplicação-***

O polimorfismo faz com que classes filhas, no caso Poupança e Corrente, implementem os mesmos métodos, mas de formas diferentes. 

Ambas possuem métodos de saque, depósito e transferência. A diferença é que cada um aplica esses métodos com suas próprias condições. 

***Por que usar o polimorfismo?***

Permite que o sistema leia as contas de forma padronizada, mas cada uma com suas particularidades.
