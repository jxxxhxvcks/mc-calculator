# Conversor de Coordenadas Minecraft

## Descrição
Este programa em Python calcula as coordenadas equivalentes entre o **Nether** e o **Overworld** no jogo Minecraft. No Minecraft, as coordenadas no Nether são escaladas por um fator de 8 em relação ao Overworld. O programa permite que o usuário:
- Converta coordenadas do Nether para o Overworld (multiplica por 8).
- Converta coordenadas do Overworld para o Nether (divide por 8).
- Insira coordenadas X e Z, receba os resultados formatados e escolha realizar novos cálculos ou encerrar o programa.

A interface usa códigos de cores ANSI para destacar informações no terminal, tornando a interação mais visual e amigável.

## Funcionalidades
- **Conversão de coordenadas**:
  - Nether → Overworld: multiplica as coordenadas X e Z por 8.
  - Overworld → Nether: divide as coordenadas X e Z por 8 (usando divisão inteira).
- **Validação de entrada**:
  - Garante que o usuário escolha uma opção válida (0 ou 1) para o tipo de conversão.
  - Valida que as coordenadas sejam números inteiros (positivos ou negativos).
- **Interface colorida**:
  - Usa códigos ANSI para destacar mundos, coordenadas e mensagens de erro.
- **Repetição de cálculos**:
  - Permite realizar múltiplos cálculos sem encerrar o programa.
- **Saída formatada**:
  - Exibe coordenadas com separadores de milhares (ex.: `1.000` em vez de `1000`).

## Requisitos
- **Python**: Versão 3.x.
- **Terminal compatível com códigos ANSI**:
  - Funciona bem em sistemas Unix/Linux (como Ubuntu, macOS) e terminais Windows modernos (como Windows Terminal).
  - Em prompts de comando clássicos do Windows, as cores podem não ser exibidas corretamente. Para compatibilidade, instale o módulo `colorama`:
    ```bash
    pip install colorama
    ```
    E adicione ao início do código:
    ```python
    from colorama import init
    init()
    ```

## Como Usar
1. **Execute o programa**:
   - Salve o código em um arquivo (ex.: `conversor.py`).
   - Execute no terminal com:
     ```bash
     python conversor.py
     ```
2. **Escolha o tipo de conversão**:
   - Digite `0` para converter do Nether para o Overworld.
   - Digite `1` para converter do Overworld para o Nether.
   - Se a entrada for inválida (não for 0 ou 1), o programa pedirá uma nova escolha.
3. **Insira as coordenadas**:
   - Digite as coordenadas X e Z (números inteiros, positivos ou negativos).
   - Se a entrada não for um número inteiro, uma mensagem de erro será exibida e o programa pedirá novas coordenadas.
4. **Visualize o resultado**:
   - As coordenadas convertidas serão exibidas com formatação (ex.: `X: 1.000`, `Z: -2.400`).
5. **Continuar ou encerrar**:
   - Digite `Sim` (ou `S`) para fazer outro cálculo.
   - Digite `Não` (ou `N`) para encerrar o programa.
   - Entradas inválidas serão rejeitadas, e o programa pedirá novamente.

## Exemplo de Uso
```plaintext
Você deseja calcular as coordenadas de qual mundo?
 [ 0 ] NETHER para o OVERWORLD
 [ 1 ] OVERWORLD para o NETHER
>> Faça sua escolha: 0
  Ok. Vamos calcular as coordenadas do NETHER para o OVERWORLD
Digite a primeira coordenada: (X) 100
Digite a segunda coordenada: (Z) -50
X: 800
Z: -400
Deseja fazer outro cálculo? [Sim/Não] S

 [ 0 ] NETHER para o OVERWORLD
 [ 1 ] OVERWORLD para o NETHER
>> Faça sua escolha: 1
  Ok. Vamos calcular as coordenadas do OVERWORLD para o NETHER
Digite a primeira coordenada: (X) 800
Digite a segunda coordenada: (Z) -400
X: 100
Z: -50
Deseja fazer outro cálculo? [Sim/Não] N
Programa encerrado.
```

## Estrutura do Código
- **Dicionário `cores`**: Define códigos ANSI para formatação de texto no terminal (ex.: negrito, vermelho, verde).
- **Menu inicial**: Exibe as opções de conversão (Nether → Overworld ou Overworld → Nether).
- **Validação de entrada**:
  - Usa um loop `while` para garantir que a escolha seja `0` ou `1`.
  - Usa `try-except` para capturar entradas inválidas nas coordenadas.
- **Cálculo**:
  - Para Nether → Overworld: multiplica X e Z por 8.
  - Para Overworld → Nether: divide X e Z por 8 (divisão inteira com `//`).
- **Loop principal**:
  - Permite múltiplos cálculos até o usuário escolher encerrar (`N`).
- **Saída formatada**:
  - Usa `.replace(",", ".")` para formatar números com separadores de milhares no padrão português.

## Limitações
- **Compatibilidade de cores**: Sem o módulo `colorama`, as cores podem não funcionar em terminais Windows antigos.
- **Entradas vazias**: Entradas vazias no `input` (pressionar Enter sem digitar) causam erro (`ValueError`). Considere adicionar tratamento adicional.
- **Interrupção do usuário**: Pressionar Ctrl+C não é tratado e pode encerrar o programa abruptamente.

## Melhorias Futuras
- Adicionar suporte ao módulo `colorama` para maior compatibilidade com Windows.
- Tratar entradas vazias e interrupções do usuário (ex.: `KeyboardInterrupt`).
- Refatorar o código para reduzir duplicação (ex.: criar uma função para o menu).
- Adicionar suporte para coordenadas Y (embora não sejam afetadas pela conversão).
- Incluir uma mensagem informando que coordenadas negativas são válidas.

## Licença
Este projeto é de código aberto e pode ser usado livremente para fins educacionais ou pessoais.
