# Sistema de Cálculo de Fretes

Projeto desenvolvido em Python com foco na aplicação de Programação Orientada a Objetos (POO), utilizando abstração, herança e polimorfismo para calcular o valor de 
fretes de diferentes meios de transporte. A aplicação recebe a distância informada pelo usuário, realiza validações de entrada e calcula automaticamente o valor do 
frete de acordo com as regras de negócio definidas para cada tipo de transporte.

## Funcionalidades

- Cálculo de fretes para diferentes meios de transporte
- Validação de entrada de dados
- Tratamento de exceções para valores inválidos
- Aplicação de regras específicas para cada transporte
- Interface em terminal utilizando a biblioteca Rich
- Exibição dos resultados em tabelas formatadas

## Tecnologias Utilizadas

- Python 3
- Rich
- ABC (Abstract Base Classes)

## Conceitos Aplicados

- Programação Orientada a Objetos (POO)
- Abstração
- Classes Abstratas
- Herança
- Polimorfismo
- Sobrescrita de métodos
- Encapsulamento
- Type Hints
- Tratamento de Exceções (`try/except`)
- Estruturas de Repetição
- Interface de terminal com Rich

## Estrutura do Projeto

```
FreightSystem/
│
├── freights/
│   ├── __main__.py
│   └── transports.py
│
├── .gitignore
└── README.md
```

## Regras de Negócio

- O sistema aceita apenas valores numéricos para a distância.
- A distância deve ser maior que zero.
- Cada meio de transporte possui um fator de cálculo próprio.
- Caminhões realizam entregas apenas para distâncias iguais ou superiores a **50 km**.
- Drones realizam entregas apenas para distâncias iguais ou superiores a **10 km**.
- Caso a distância mínima não seja atendida, o sistema informa o motivo ao usuário.

## Soluções Implementadas

- Utilização de uma **classe abstrata (`Transport`)** para definir um contrato comum entre todos os transportes.
- Implementação do método abstrato `freight_calc()` por meio de polimorfismo.
- Especialização das classes `Motorcycle`, `Truck` e `Drone`, cada uma contendo sua própria regra de cálculo.
- Validação robusta da entrada utilizando `try/except`, impedindo que valores inválidos interrompam a execução da aplicação.
- Organização da interface utilizando **Rich**, com tabelas e painéis para melhorar a visualização das informações no terminal.
- Separação da lógica de negócio da interface, tornando o código mais organizado e de fácil manutenção.
