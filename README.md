# Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento

## Objetivo
Protótipo em Python para cadastrar peças, avaliar requisitos de qualidade, armazenar aprovadas em caixas de até 10 unidades e consultar resultados.

## Regras implementadas
- Peso aprovado: de 95 g a 105 g, inclusive.
- Cor aprovada: azul ou verde (maiúsculas/minúsculas são aceitas).
- Comprimento aprovado: de 10 cm a 20 cm, inclusive.
- Basta falhar em um critério para reprovar; o sistema informa todos os motivos.
- IDs não podem se repetir. A remoção reorganiza as caixas mantendo a ordem das peças aprovadas restantes.
- Caixas completas são fechadas automaticamente. A opção 4 lista apenas caixas fechadas. A caixa incompleta, quando houver, também conta como utilizada no relatório, que informa quantas peças estão nela.
- Os dados ficam na memória durante a execução e são perdidos ao sair.

## Como executar
1. Instale Python 3, se ainda não estiver instalado: https://www.python.org/downloads/
2. Salve `gestao_pecas.py` e `README.md` na mesma pasta.
3. Abra o terminal nessa pasta.
4. Execute `python gestao_pecas.py` (em alguns sistemas, use `python3 gestao_pecas.py`).
5. Use as opções do menu. Digite `0` para encerrar.

Não são necessárias bibliotecas externas.

## Exemplo de uso
Entrada para uma peça aprovada:

```text
Escolha uma opção: 1
ID da peça: P001
Peso em gramas: 100
Cor (azul/verde): azul
Comprimento em centímetros: 15
Peça aprovada e armazenada. Caixa atual: 1/10.
```

Entrada para uma peça reprovada em dois critérios:

```text
Escolha uma opção: 1
ID da peça: P002
Peso em gramas: 110
Cor (azul/verde): vermelho
Comprimento em centímetros: 18
Peça reprovada: peso fora do intervalo de 95g a 105g; cor diferente de azul ou verde.
```

Exemplo resumido do relatório:

```text
=== RELATÓRIO FINAL ===
Peças aprovadas: 1
Peças reprovadas: 1
Motivos por peça:
  P002: peso fora do intervalo de 95g a 105g; cor diferente de azul ou verde.
Caixas utilizadas: 1
Caixas fechadas: 0
Peças na caixa em preenchimento: 1/10
```

Com 10 peças aprovadas, o programa fecha a caixa automaticamente. O menu de listagem permite conferir aprovadas, reprovadas, dados e motivos.

## Estrutura lógica
- `avaliar_peca`: verifica os três critérios.
- `cadastrar_peca`: coleta dados, evita IDs duplicados e armazena o resultado.
- `reorganizar_caixas`: atualiza o armazenamento após remoção.
- Funções de listagem e relatório apresentam os registros.
- `main`: repete o menu até a opção de saída.
- Condições `if` decidem aprovação, fechamento de caixa e opção do menu; o laço `while` mantém o sistema ativo e `for` percorre os registros.

## Limites do protótipo
É uma demonstração local, com dados temporários e entrada manual. Não controla sensores nem equipamentos industriais.

