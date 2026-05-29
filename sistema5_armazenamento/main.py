from armazenador_arquivo import ArmazenadorArquivo
from armazenador_banco import ArmazenadorBanco
from armazenador_nuvem import ArmazenadorNuvem
from funcoes import executar_salvamento_formal, executar_salvamento_flexivel

arquivo = ArmazenadorArquivo()
banco = ArmazenadorBanco()
nuvem = ArmazenadorNuvem()

print("\n--- Salvamento Formal (ABC) ---")
executar_salvamento_formal(arquivo, "dados.txt")
executar_salvamento_formal(banco, "clientes")

print("\n--- Salvamento Flexível (Protocol) ---")
executar_salvamento_flexivel(arquivo, "dados.txt")
executar_salvamento_flexivel(banco, "clientes")
executar_salvamento_flexivel(nuvem, "backup.zip")
