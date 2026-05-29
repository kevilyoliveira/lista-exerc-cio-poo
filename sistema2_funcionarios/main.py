from funcionario_assalariado import FuncionarioAssalariado
from funcionario_horista import FuncionarioHorista
from funcionario_comissionado import FuncionarioComissionado
from empresa import Empresa

empresa = Empresa("Tech Solutions")

f1 = FuncionarioAssalariado("Ana", "111.111.111-11", 5000)
f2 = FuncionarioHorista("Bruno", "222.222.222-22", 160, 25)
f3 = FuncionarioComissionado("Carla", "333.333.333-33", 20000, 5)

empresa.adicionar_funcionario(f1)
empresa.adicionar_funcionario(f2)
empresa.adicionar_funcionario(f3)

empresa.listar_funcionarios()
empresa.mostrar_folha_pagamento()
