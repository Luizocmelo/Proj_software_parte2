# Disciplina: Projeto de Software - Prof: Baldoino Fonseca
###ALUNO: Luiz Antonio Omena Cabral de Melo
-------------------------------------------------------------------------------
### Sistema de Folha de Pagamento Empresarial

O projeto é implementar um sistema de folha de pagamento. O sistema consiste no
gerenciamento de pagamentos dos empregados de uma empresa fictícia.

Algumas definições com relação ao funcionamento:

• Alguns empregados são horistas. Eles recebem um salário por hora trabalhada. Eles
submetem "cartões de ponto" todo dia para informar o número de horas trabalhadas naquele dia. Se um empregado trabalhar mais do que 8 horas, deve receber 1.5 a taxa normal Durante as horas extras. Eles são pagos toda sexta-feira.

• Alguns empregados recebem um salário fixo mensal. São pagos no último dia útil do mês. São chamados de "assalariados".

• Alguns empregados assalariados são comissionados e portanto recebem uma comissão, um
percentual das vendas que realizam. Eles submetem resultados de vendas que informam a data e valor da venda. O percentual de comissão varia de empregado para empregado. Eles são pagos a cada 2 sextas-feiras; neste momento, devem receber o equivalente de 2 semanas de salário fixo mais as comissões do período.

• O empregados que informa o método de pagamento:
Podem receber um cheque pelos correios ou um cheque em mãos ou depósito em conta bancária

• Alguns empregados pertencem ao sindicato:
O sindicato cobra uma taxa mensal do empregado e essa taxa pode variar entre
empregados, é deduzida do salário. Também, o sindicato pode ocasionalmente 
cobrar taxas de serviços adicionais a um empregado. A identificação do empregado no sindicato não é a mesma da
identificação no sistema de folha de pagamento.

• A folha de pagamento é rodada todo dia e deve pagar os empregados cujos salários vencem naquele dia. 
O sistema receberá a data até a qual o pagamento deve ser feito e calculará o pagamento para cada empregado desde a última vez em que este foi pago.


-------------------------------------------------------------------------------
### Code Small

•1. Large Class
Foi segmentado as classes que possuiam excesso de funções e atributos. A classe 
Employee possuia 10 atributos, alem das varias funções, com a segmentação, passou a 
possuir apenas 4 atributos e herdando mais 3 da classe BankData, diminuindo a 
quantidade de codigo e o deixando-o mais limpo. Os outros atributos da classe foram
redirencionando para outras classes, como Deparetaments.

•2. Data Class:
Foi criada uma funçaõ para imprimir os dados, motivo: Anteriormente a classe Employee
abrigava uma quantidade significativa de codigo, logo, centralizando o codigo, com
a segmentação da classe foi-se necessario a criação de uma função "repre" para imprimir
dados, evitando assim reescrever o codigo para varias funções e classes que herdaram
os atributos de Employee.


•3 .Shotgun Surgery
Tambem voltado para mudança na classe emplooyye, como ele concentrava muitos atributos,
todo e qualquer alteração gerava uma grande serie de modificações no codigo, com a redução
da mesmo, foi-se minimizado essa necessidade.

•4. Long Method
Houve a dinimuição de rotinas condicionais IF_ELSE nas classes, devido a diminuição
de atributos nas classes, essas rotinas foram segmentadas em outras classes, 
tornando assim o codigo mais limpo e legivel.
  
