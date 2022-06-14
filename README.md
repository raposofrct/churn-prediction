# Churn Ranking Problem

Qual empresa nunca se viu na necessidade de diminuir seu nível de churn? 

Perder clientes é sempre uma métrica negativa, independente do modelo de negócio, significa essencialmente menor faturamento e lucros!

Assim, prever quando o seu cliente entrará em churn é essencial, pois dá a possibilidade de manobra para a empresa reverter tal situação.

## Entendimento do Problema
A TopBank é uma grande empresa de serviços bancários. Ela atua principalmente nos países da Europa oferecendo produtos financeiros, desde contas bancárias até investimentos, passando por alguns tipos de seguros e produto de investimento.

O principal produto da empresa é uma conta bancária, na qual o cliente pode depositar seu salário, fazer saques, depósitos e transferência para outras contas.

Segundo a TopBank, cada cliente que possui essa conta bancária retorna um valor monetário de 1% do valor do seu saldo ao ano.

Nos últimos meses, percebeu-se que a taxa de clientes cancelando suas contas e deixando o banco, atingiu números inéditos na empresa. Preocupados com o aumento dessa taxa, o time de negócios estimou que o custo necessário para reter o cliente por mais um ano é de 0.5% do saldo dele, pois seria necessário aumentar os rendimentos do cliente nesse período.

**O grande problema, então, é o fato de que o time de negócio não sabe previamente quem dará churn!.**

Isso faz com que eles não saibam a quem oferecer essa promoção de rendimentos melhores, pois se for oferecido a um cliente que não daria churn, a empresa estaria tendo um custo desnecessário, o que reduziria os lucros no final do ano, com um Return Over Investiment (ROI) negativo!

## Solução
Para solucionar o problema de negócio se faz necessário o uso de **algoritmos de Machine Learning (Classification - Learning to Rank)**
Esse algoritmo irá rankear os clientes de acordo com sua probabilidade de entrar em churn, o que diminuiria as incertezas enfrentadas pelo time de negócio, possibilitando uma diminuição do churn e um ROI positivo.

Esse algoritmo foi colocado **em produção na cloud através de uma API**. 

**Tecnologias Utilizadas:** 
* Python, Git e Github
* Bibliotecas de manipulação de dados (Pandas, Numpy..)
* Bibliotecas de visualização de dados (Seaborn e Matplotlib)
* Bibliotecas de machine learning (Sklearn, LightGBM,XGboost...)
* Bibliotecas para deploy e criação da API (Flask, Pickle...)
* Heroku para hospedar nossa API na cloud.

## Data Description


Os dados são compostos pelas características de 10.000 clientes e a target: 'Exited', que indicará se o cliente entrou ou não em churn.
 
```
RowNumber - O número da linha

CustomerID - Identificador único do cliente

Surname - Sobrenome do cliente.

CreditScore - A pontuação de Crédito do cliente para o mercado de consumo.

Geography - O país onde o cliente reside.

Gender - O gênero do cliente.

Age - A idade do cliente.

Tenure - Número de anos que o cliente permaneceu ativo.

Balance - Saldo monetário do cliente.

NumOfProducts - O número de produtos comprado pelo cliente no banco.

HasCrCard - Indica se o cliente possui ou não cartão de crédito.

IsActiveMember - Indica se o cliente faz movimentações no banco.

EstimateSalary - Estimativa do salário mensal do cliente.

Exited - Indica se o cliente está ou não em Churn.
```

## Model Performance (in Business Terms)

#### Modelo com AI (LGBMClassifier)
 
|       Model Name          |        Média ROI          |      Min ROI      |        Max ROI        |
|:-------------------------:|:-------------------:|:--------------:|:------------------:|
| LGBM Classifier                  |  €18039          | €15332       |       €21196        |

#### Modelo sem AI (Random)

|       Model Name          |        Média ROI          |      Min ROI      |        Max ROI        |
|:-------------------------:|:-------------------:|:--------------:|:------------------:|
| Random                  |  €-0.437          | €-0.828      |       €0.0047        |

Vemos que **a empresa sem utilizar o modelo não teria a menor possibilidade de ganhos, o ROI é basicamente zero!**

**Com esse modelo de machine learning, a TopBank poderá embolsar quase até €22 mil! O que se traduz em mais de 100 mil reais!**

<img src="https://i.imgur.com/8XEOlir.png"/>

Esse modelo está disponível na cloud, podendo ser acessado <a href=https://reqbin.com/4puvvq1c target="_blank">aqui</a>
(É só mudar as variáveis na aba 'Content')

## Conclusão

Esse projeto nos **rendeu diversos insights valiosos para o negócio, que vão possibilitar a TopBank tomar decisões mais acertadas** para evitar o churn, e assim aumentar seu faturamento, além de **possibilitar que a empresa conseguisse ter mais segurança na previsão de churn dos clientes, o que traria um ROI de até mais de 100 mil reais para a empresa por ano.

Ainda há muito que pode ser feito: Coletar mais dados, formular novas hipóteses, gerar novos insights na EDA, criar novas features, testar outras formas de data preparation, testar outros algoritmos, utilizar um Hyperparameter Fine Tuning exaustivo como o GridSearchCV, dentre outras milhões de possibilidades! 

Apesar desse mar de coisas novas para fazer, considero que o que temos atualmente supre a necessidade da empresa no curto prazo. Dessa forma **conseguimos entregar valor de forma rápida à empresa** e vamos aperfeiçoando o projeto até onde for necessário para o negócio.
