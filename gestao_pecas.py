from dataclasses import dataclass, field

CAPACIDADE_CAIXA = 10

@dataclass
class Peca:
    identificador: str
    peso: float
    cor: str
    comprimento: float
    aprovada: bool
    motivos: list[str] = field(default_factory=list)

pecas: list[Peca] = []
caixas_fechadas: list[list[str]] = []
caixa_atual: list[str] = []

def avaliar_peca(peso: float, cor: str, comprimento: float) -> list[str]:
    motivos = []
    if not 95 <= peso <= 105:
        motivos.append("peso fora do intervalo de 95g a 105g")
    if cor not in ("azul", "verde"):
        motivos.append("cor diferente de azul ou verde")
    if not 10 <= comprimento <= 20:
        motivos.append("comprimento fora do intervalo de 10cm a 20cm")
    return motivos

def reorganizar_caixas() -> None:
    """Reconstrói caixas após remoção, mantendo a ordem de cadastro."""
    global caixas_fechadas, caixa_atual
    aprovadas = [p.identificador for p in pecas if p.aprovada]
    caixas_fechadas = [aprovadas[i:i + CAPACIDADE_CAIXA]
                       for i in range(0, len(aprovadas) // CAPACIDADE_CAIXA * CAPACIDADE_CAIXA, CAPACIDADE_CAIXA)]
    caixa_atual = aprovadas[len(caixas_fechadas) * CAPACIDADE_CAIXA:]

def ler_numero(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Digite um número válido (ex.: 100 ou 12,5).")

def cadastrar_peca() -> None:
    identificador = input("ID da peça: ").strip()
    if not identificador:
        print("O ID não pode ficar vazio.")
        return
    if any(p.identificador.casefold() == identificador.casefold() for p in pecas):
        print("Esse ID já está cadastrado.")
        return
    peso = ler_numero("Peso em gramas: ")
    cor = input("Cor (azul/verde): ").strip().casefold()
    comprimento = ler_numero("Comprimento em centímetros: ")
    motivos = avaliar_peca(peso, cor, comprimento)
    peca = Peca(identificador, peso, cor, comprimento, not motivos, motivos)
    pecas.append(peca)
    if peca.aprovada:
        caixa_atual.append(identificador)
        if len(caixa_atual) == CAPACIDADE_CAIXA:
            caixas_fechadas.append(caixa_atual.copy())
            caixa_atual.clear()
            print("Peça aprovada. Caixa fechada (10 peças); uma nova caixa será iniciada.")
        else:
            print(f"Peça aprovada e armazenada. Caixa atual: {len(caixa_atual)}/{CAPACIDADE_CAIXA}.")
    else:
        print("Peça reprovada: " + "; ".join(motivos) + ".")

def listar_pecas() -> None:
    if not pecas:
        print("Nenhuma peça cadastrada.")
        return
    for aprovada in (True, False):
        grupo = [p for p in pecas if p.aprovada == aprovada]
        print("\nAPROVADAS" if aprovada else "\nREPROVADAS")
        if not grupo:
            print("  Nenhuma.")
        for p in grupo:
            dados = f"ID {p.identificador} | {p.peso:g}g | {p.cor} | {p.comprimento:g}cm"
            print(f"  {dados}" + ("" if aprovada else " | Motivo: " + "; ".join(p.motivos)))

def remover_peca() -> None:
    identificador = input("ID da peça a remover: ").strip()
    peca = next((p for p in pecas if p.identificador.casefold() == identificador.casefold()), None)
    if peca is None:
        print("Peça não encontrada.")
        return
    pecas.remove(peca)
    reorganizar_caixas()
    print(f"Peça {peca.identificador} removida. As caixas foram reorganizadas.")

def listar_caixas() -> None:
    if not caixas_fechadas:
        print("Nenhuma caixa fechada.")
    for numero, caixa in enumerate(caixas_fechadas, start=1):
        print(f"Caixa {numero} ({len(caixa)}/{CAPACIDADE_CAIXA}): " + ", ".join(caixa))

def gerar_relatorio() -> None:
    aprovadas = [p for p in pecas if p.aprovada]
    reprovadas = [p for p in pecas if not p.aprovada]
    print("\n=== RELATÓRIO FINAL ===")
    print(f"Peças aprovadas: {len(aprovadas)}")
    print(f"Peças reprovadas: {len(reprovadas)}")
    if reprovadas:
        print("Motivos por peça:")
        for p in reprovadas:
            print(f"  {p.identificador}: " + "; ".join(p.motivos))
    print(f"Caixas utilizadas: {len(caixas_fechadas) + (1 if caixa_atual else 0)}")
    print(f"Caixas fechadas: {len(caixas_fechadas)}")
    if caixa_atual:
        print(f"Peças na caixa em preenchimento: {len(caixa_atual)}/{CAPACIDADE_CAIXA}")

def main() -> None:
    opcoes = {
        "1": cadastrar_peca,
        "2": listar_pecas,
        "3": remover_peca,
        "4": listar_caixas,
        "5": gerar_relatorio,
    }
    while True:
        print("\n=== GESTÃO DE PEÇAS ===")
        print("1. Cadastrar nova peça")
        print("2. Listar peças aprovadas/reprovadas")
        print("3. Remover peça cadastrada")
        print("4. Listar caixas fechadas")
        print("5. Gerar relatório final")
        print("0. Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "0":
            print("Programa encerrado.")
            break
        acao = opcoes.get(opcao)
        if acao:
            acao()
        else:
            print("Opção inválida. Escolha de 0 a 5.")

if __name__ == "__main__":
    main()


