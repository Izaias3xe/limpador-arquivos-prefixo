# 🧹 Limpador de Arquivos por Prefixo

Script em **Python** que localiza e remove automaticamente **arquivos ou pastas que começam com um prefixo específico** dentro de um diretório no Linux.

Este projeto foi criado para automatizar tarefas simples de organização e limpeza de arquivos no sistema.

---

# 🚀 Funcionalidades

* 🔎 Busca arquivos que começam com um prefixo específico
* 📁 Pode incluir **pastas** na remoção
* ⚠️ Confirmação antes de excluir qualquer coisa
* 🧾 Lista todos os arquivos encontrados antes da remoção
* 🐧 Funciona em sistemas **Linux / Unix**

---

# 📂 Exemplo de funcionamento

Imagine que uma pasta possui os seguintes arquivos:

```
teste1.txt
teste_backup.log
teste_pasta/
foto.png
documento.pdf
```

Se o prefixo definido for:

```
teste
```

O script irá localizar:

```
teste1.txt
teste_backup.log
teste_pasta/
```

E perguntará se você deseja removê-los.

---

# ⚙️ Requisitos

* Python 3
* Sistema Linux ou Unix

---

# ▶️ Como executar

Clone o repositório:

```
git clone https://github.com/Izaias3xe/limpador-arquivos-prefixo.git
```

Entre na pasta do projeto:

```
cd limpador-arquivos-prefixo
```

Execute o script:

```
python3 script.py
```

---

# 📁 Alterando a pasta que será analisada

Dentro do código existe uma variável chamada:

```python
pasta = "/home/izaias"
```

Essa variável define **qual pasta o script irá analisar**.

Se você quiser usar o script em outro local do seu computador, basta **alterar o caminho da pasta**.

### Exemplo:

Se quiser analisar a pasta **Downloads**, altere para:

```python
pasta = "/home/seu_usuario/Downloads"
```

Se quiser analisar a pasta **Documentos**:

```python
pasta = "/home/seu_usuario/Documentos"
```

Ou qualquer outro diretório do seu sistema.

---

# ⚠️ Aviso Importante

Este script **remove arquivos e pastas permanentemente** do sistema.

Arquivos removidos utilizando `rm` ou funções equivalentes **não vão para a lixeira**.

Sempre verifique:

* o **prefixo definido**
* a **pasta selecionada**
* a **confirmação de exclusão**

antes de executar a remoção.

---

# 🏷️ Tecnologias utilizadas

* Python
* Linux
* Automação de arquivos
* Manipulação de sistema de arquivos

---

# 👨‍💻 Autor

**Izaias Gabriel©**

Projeto desenvolvido para estudo de:

* automação com Python
* manipulação de arquivos no Linux
* criação de scripts CLI simples

---

⭐ Se este projeto te ajudou ou você achou interessante, considere deixar uma **estrela no repositório**.
