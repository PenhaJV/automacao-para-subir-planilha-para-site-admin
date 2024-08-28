# Automação de Carregamento de Planilhas para Site

Este projeto é uma automação simples para carregar uma planilha de preços em um site específico, utilizando Python com Selenium e PyAutoGUI. A automação acessa o site, carrega mais produtos na página, seleciona e envia uma planilha de preços, e, finalmente, atualiza os preços no site.

## Pré-requisitos

Antes de executar o código, você precisará instalar as seguintes bibliotecas Python:

- **Selenium**: Para controlar o navegador e interagir com a página web.
- **PyAutoGUI**: Para automatizar o preenchimento do caminho do arquivo e a interação com a interface gráfica.
  
Você pode instalar as bibliotecas necessárias usando pip:

```bash
pip install selenium pyautogui
```

## Configuração

1. **Escolha do Navegador**: No código, substitua `webdriver.Edge()` pelo navegador de sua escolha, como `webdriver.Chrome()` ou `webdriver.Firefox()`. Certifique-se de ter o WebDriver correspondente instalado e configurado no seu PATH.

2. **Caminho do Arquivo**: No trecho `pg.write(r'C:\Projects\automacao-para-subir-planilha-para-site-admin\data\precos-produtos-atualizados.xlsx')`, substitua o caminho pelo caminho do arquivo em sua própria máquina.

3. **Ajuste de Tempo**: O tempo de espera configurado com `sleep()` pode ser ajustado conforme necessário, dependendo da velocidade de carregamento da página ou da interação com os elementos da interface.

## Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Execute o script Python:

```bash
python nome-do-arquivo.py
```

O script abrirá o navegador, acessará o site, carregará mais produtos na página, subirá a planilha especificada, e atualizará os preços.

## Contribuição

Este é um repositório público, e você está convidado a contribuir! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE). Você pode utilizá-lo livremente em seus próprios projetos, desde que mantenha a atribuição devida.

---

**Nota**: Este projeto foi criado como um exemplo simples de automação. Certifique-se de adaptar o código às suas necessidades específicas e testar cuidadosamente em um ambiente seguro antes de usá-lo em produção.