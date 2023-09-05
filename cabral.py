#Vitor Nicoletti, Eduardo Silva Contin, Fabricio Goes Pinterich
def main():
    file = open("input.txt", "r")
    line = file.readlines()

    quantidadeOperacoes = int(line[0].replace("\n", ""))

    for i in range(1, ((quantidadeOperacoes * 3) + 1), 3):

        operacao = line[i].replace("\n", "").replace(",", "")
        conjA = set(line[i + 1].replace("\n", "").replace(" ", "").split(","))
        conjB = set(line[i + 2].replace("\n", "").replace(" ", "").split(","))

        if operacao == "I":
            print(f"\nInterseção: conjunto 1 {conjA}, conjunto 2 {conjB}. Resultado: ", conjA.intersection_update(conjB))
        elif operacao == "U":
            print(f"\nUnião: conjunto 1 {conjA}, conjunto 2 {conjB}. Resultado: ", conjA.union(conjB))
        elif operacao == "D":
            print(f"\nDiferença: conjunto 1 {conjA}, conjunto 2 {conjB}. Resultado: ", conjA.difference(conjB))
        elif operacao == "C":
            print(f"\nProduto Cartesiano: conjunto 1 {conjA}, conjunto 2 {conjB}. Resultado: ", end="")
            
            for i in conjA:
                for j in conjB:
                    print(f"({i.replace(' ', '')},{j.replace(' ', '')}), ", end="")

if __name__ == "__main__":
    main()
