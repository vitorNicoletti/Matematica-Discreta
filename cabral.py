def main():
  file = open("input2.txt", "r")
  line = file.readlines()

  quantidadeOperacoes = int(line[0].replace("\n", ""))

  for i in range(1, ((quantidadeOperacoes * 3) + 1), 3):

    operacao = line[i].replace("\n", "").replace(",", "")
    conjA = set(line[i + 1].replace("\n", "").split(","))
    conjB = set(line[i + 2].replace("\n", "").split(","))

    if operacao == "I":
      print(
          f"\nInterseção: Conjunto 1 {conjA}, Conjunto 2 {conjB}. Resultado: ",
          conjA.intersection_update(conjB))
    elif operacao == "U":
      print(f"\nUnião: Conjunto 1 {conjA}, Conjunto 2 {conjB}. Resultado: ",
            conjA.union(conjB))

    elif operacao == "D":
      print(
          f"\nDiferença: Conjunto 1 {conjA}, Conjunto 2 {conjB}. Resultado: ",
          conjA.difference(conjB))
    elif operacao == "C":
      print(
          f"\nProduto Cartesiano: Conjunto 1 {conjA}, Conjunto 2 {conjB}. Resultado: ",
          end="")
      for i in conjA:
        for j in conjB:
          print(f"({i},{j}), ", end="")


if __name__ == "__main__":
  main()
