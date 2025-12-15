# WhatsApp Bulk Sender

Um sistema automatizado para envio de mensagens em massa via WhatsApp Web usando Selenium e Python.

## 📋 Pré-requisitos

- Python 3.6 ou superior
- Google Chrome instalado
- Conta WhatsApp

## 🚀 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd whatsapp-bulk-messenger
```

### 2. Criar e ativar ambiente virtual (venv)

**No macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**No Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

## 📝 Como usar

### Passo 1: Abrir navegador em modo debug

Execute o script `open.py` para abrir o Chrome em modo debug:

```bash
python open.py
```

Este script irá:
- Detectar automaticamente seu sistema operacional (macOS, Windows ou Linux)
- Abrir o Google Chrome com configurações especiais para debug
- Criar um perfil temporário em `/tmp/chrome-whatsapp-bulk-sender`
- Habilitar a porta 9222 para comunicação com o Selenium

### Passo 2: Configurar mensagem

Edite o arquivo `message.txt` com a mensagem que deseja enviar:

```
Hello World,

This is my *text* to you from automated messaging system.

*Thank You!*
```

**Dicas para formatação:**
- Use `*texto*` para deixar o texto em negrito
- Use `_texto_` para deixar o texto em itálico
- Use quebras de linha normalmente

### Passo 3: Configurar números

Edite o arquivo `numbers.txt` com os números de telefone (um por linha):

```
5531983176539
5531987654321
5531999888777
```

**Formato dos números:**
- Use o código do país + código da área + número
- Exemplo Brasil: 55 (país) + 31 (área) + 983176539 (número)
- Não use espaços, parênteses ou hífens

### Passo 4: Executar o envio

Execute o script principal para iniciar o envio:

```bash
python send_messages.py
```

O script irá:

1. **Conectar ao Chrome em debug** - Se conecta à instância do Chrome aberta pelo `open.py`
2. **Abrir WhatsApp Web** - Navega automaticamente para web.whatsapp.com
3. **Aguardar login** - Você precisará fazer login manualmente escaneando o QR Code
4. **Confirmar início** - Pressione ENTER após fazer login e visualizar seus chats
5. **Enviar mensagens** - O script enviará as mensagens automaticamente para todos os números

## ⚙️ Configurações Avançadas

### Intervalos entre mensagens

No arquivo `send_messages.py`, você pode ajustar os intervalos:

```python
min_between_messages = 10  # Mínimo 10 segundos
max_between_messages = 25  # Máximo 25 segundos
```

### Tempo de espera

```python
delay = 40  # Tempo máximo de espera para elementos carregarem
```

## 🔧 Funcionalidades

- ✅ **Multi-plataforma**: Funciona em macOS, Windows e Linux
- ✅ **Detecção anti-bot**: Usa técnicas para evitar detecção como bot
- ✅ **Intervalos humanizados**: Adiciona delays aleatórios entre ações
- ✅ **Retry automático**: Tenta novamente em caso de falha (até 3 tentativas por número)
- ✅ **Logs coloridos**: Interface visual clara com status de cada envio
- ✅ **Cliques humanizados**: Simula movimentos humanos do mouse

## 📊 Como funciona

1. **open.py**: Abre uma instância do Chrome em modo debug na porta 9222
2. **send_messages.py**: Se conecta ao Chrome via Selenium usando a porta de debug
3. O script navega para WhatsApp Web e aguarda seu login manual
4. Para cada número na lista, o script:
   - Abre a URL de envio direto do WhatsApp
   - Aguarda o botão "Enviar" ficar disponível
   - Clica no botão de forma humanizada
   - Aguarda um intervalo aleatório antes do próximo envio

## ⚠️ Avisos Importantes

- **Use com responsabilidade**: Este script é apenas para fins educacionais
- **Respeite os termos do WhatsApp**: O uso pode violar os termos de serviço
- **Limite de envios**: WhatsApp pode bloquear contas que enviam muitas mensagens
- **Teste primeiro**: Sempre teste com poucos números antes de envios em massa
- **Mantenha intervalos**: Não diminua muito o tempo entre mensagens

## 🛠️ Solução de Problemas

### Chrome não encontrado
Certifique-se de que o Google Chrome está instalado no caminho padrão:
- **macOS**: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
- **Windows**: `C:\Program Files\Google\Chrome\Application\chrome.exe`
- **Linux**: `google-chrome` (deve estar no PATH)

### Erro de conexão
- Certifique-se de que executou o `open.py` primeiro
- Verifique se não há outra instância do Chrome rodando
- Feche todos os Chromes e tente novamente

### Mensagem não enviada
- Verifique se os números estão no formato correto
- Certifique-se de que tem internet estável
- Confirme que está logado no WhatsApp Web

### Elemento não encontrado
- O script procura pelo botão "Enviar" em português
- Se seu WhatsApp estiver em outro idioma, altere a linha 118 em `send_messages.py`:
```python
# Português
EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Enviar']"))

# Inglês
EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send']"))

# Espanhol
EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Enviar']"))
```

## 📄 Estrutura dos Arquivos

```
whatsapp-bulk-messenger/
├── open.py              # Script para abrir Chrome em debug
├── send_messages.py     # Script principal de envio
├── message.txt          # Arquivo com a mensagem a ser enviada
├── numbers.txt          # Arquivo com lista de números
├── requirements.txt     # Dependências do Python
└── README.md           # Este arquivo
```

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests

## 📝 Licença

Este projeto é apenas para fins educacionais. Use por sua própria conta e risco.