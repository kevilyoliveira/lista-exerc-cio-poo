# Lista de Exercícios II – Parte 1
## Descrição

Os projetos foram desenvolvidos em Python utilizando conceitos de:

* Programação Orientada a Objetos (POO)
* Herança
* Polimorfismo
* Classes Abstratas (ABC)
* Protocol (Protocolos Estruturais)
* Sobrescrita de Métodos

---

## Tecnologias Utilizadas

* Python 3.11+
* Biblioteca `abc`
* Biblioteca `typing`

---

## Estrutura do Projeto

```text
lista-exercicios-poo-python/
│
├── sistema_midias_edu/
├── sistema2_funcionarios/
├── sistema3_notificacoes_abc/
├── sistema4_impressao_protocol/
├── sistema5_armazenamento/
│
├── README.md
└── link_repositorio.txt
```
---

# Sistema 1 – Mídias Educacionais
Implementação de uma plataforma educacional capaz de armazenar diferentes tipos de mídias.

### Classes Implementadas
* Midia (Classe Abstrata)
* Video
* Podcast
* TextoNarrado
* Plataforma

### Conceitos Aplicados
* Herança
* Classe Abstrata (ABC)
* Polimorfismo

### Executar
```bash
cd sistema_midias_edu
python main.py
```

---

# Sistema 2 – Funcionários de uma Empresa
Implementação de uma empresa que gerencia diferentes tipos de funcionários e gera uma folha de pagamento utilizando polimorfismo.

### Classes Implementadas
* Funcionario (Classe Abstrata)
* FuncionarioAssalariado
* FuncionarioHorista
* FuncionarioComissionado
* Empresa

### Conceitos Aplicados
* Herança
* Sobrescrita de métodos
* Polimorfismo
* Classe Abstrata (ABC)

### Executar
```bash
cd sistema2_funcionarios
python main.py
```

---

# Sistema 3 – Notificações com ABC
Sistema de envio de notificações utilizando contrato formal por herança.

### Classes Implementadas
* Notificador (Classe Abstrata)
* NotificadorEmail
* NotificadorSMS
* NotificadorApp
* CentralNotificacoes

### Conceitos Aplicados
* ABC
* Contrato formal
* Polimorfismo

### Executar
```bash
cd sistema3_notificacoes_abc
python main.py
```

---

# Sistema 4 – Impressão com Protocol
Sistema de impressão utilizando Protocol para definir compatibilidade estrutural entre objetos.

### Classes Implementadas
* Imprimivel (Protocol)
* Boleto
* Etiqueta
* RelatorioSimples

### Função Implementada
* processar_impressao(item)

### Conceitos Aplicados
* Protocol
* Duck Typing
* Polimorfismo Estrutural

### Executar
```bash
cd sistema4_impressao_protocol
python main.py
```

---

# Sistema 5 – Armazenamento com ABC e Protocol
Sistema desenvolvido para comparar o uso de Classes Abstratas (ABC) e Protocol no mesmo problema.

### Classes Implementadas
#### Parte A – ABC
* Armazenador
* ArmazenadorArquivo
* ArmazenadorBanco

#### Parte B – Protocol
* Salvavel
* ArmazenadorNuvem

#### Parte C – Funções
* executar_salvamento_formal()
* executar_salvamento_flexivel()

### Conceitos Aplicados
* ABC
* Protocol
* Contrato por Herança
* Contrato Estrutural
* Comparação entre abordagens

### Executar
```bash
cd sistema5_armazenamento
python main.py
```

## Como Executar os Projetos
1. Clone o repositório:

```bash
git clone https://github.com/kevilyoliveira/lista-exerc-cio-poo.git
```

2. Entre na pasta desejada:

```bash
cd sistema1_midias_educacionais
```

3. Execute o arquivo principal:

```bash
python main.py
```
---
## Aluna

Kevily Oliveira

Universidade Federal do Amazonas – UFAM

Curso: Sistemas de Informação
