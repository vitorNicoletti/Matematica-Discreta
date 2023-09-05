arquivo = open("arquivo2.txt", "r")
texto = arquivo.readlines()

quantidadeOperacoes = int(texto[0].replace("\n", ""))

for i in range(1, ((quantidadeOperacoes * 3) + 1), 3):
  operacao = texto[i].replace("\n", "").replace(",", "")
  conjuntoA = set(texto[i + 1].replace("\n", "").split(","))
  conjuntoB = set(texto[i + 2].replace("\n", "").split(","))
  if operacao == "I":
    print(
        f"\nInterseção: Conjunto 1 {conjuntoA}, Conjunto 2 {conjuntoB}. Resultado: ",
        conjuntoA.intersection(conjuntoB))
  elif operacao == "U":
    print(
        f"\nUnião: Conjunto 1 {conjuntoA}, Conjunto 2 {conjuntoB}. Resultado: ",
        conjuntoA.union(conjuntoB))
  elif operacao == "D":
    print(
        f"\nDiferença: Conjunto 1 {conjuntoA}, Conjunto 2 {conjuntoB}. Resultado: ",
        conjuntoA.difference(conjuntoB))
  elif operacao == "C":
    print(
        f"\nProduto Cartesiano: Conjunto 1 {conjuntoA}, Conjunto 2 {conjuntoB}. Resultado: ",
        end="")
    for i in conjuntoA:
      for j in conjuntoB:
        print(f"({i},{j}), ", end="")
