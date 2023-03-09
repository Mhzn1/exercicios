print("Ana Maria recebeu seu salário e precisa pagar 2 contas que já venceram. \nComo as contas estão atrasadas, Ana Maria terá que pagar multa de 3% sobre cada conta!")
print("Insira seu salário")
salario = float(input())
print("Qual o valor da sua primeira conta")
conta = float(input())
print("Qual o valor da sua segunda conta")
conta2 = float(input())
print("O valor total das suas contas é de", conta+conta2," \ncomo elas estão atrasadas, acumularam juros de 3% em cada uma!")
print("Na primeira conta, os juros acumulados são de", conta * 3 / 100)
print("Resultando em", conta + conta*3/100)
print("Na segunda conta, os juros são de", conta2 *3 / 100)
print("Resultando em", conta2 + conta2*3/100)
contajuros = conta+ (conta*3/100)
conta2juros = conta2+ (conta2*3/100)
print("Ou seja, utilizando seu salário de", salario,"para pagar suas duas contas com juros, restará", (salario - contajuros) - conta2juros)




