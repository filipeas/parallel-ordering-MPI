# trabalho de ordenação de vetor usando biblioteca mpi.
#
# exec: mpiexec -np 4 --hostfile maqs.txt python sort_parallel.py
#
# obs: caso mude o numero de processos, observar o tamanho do array TAM_ARRAY,
# eles devem ser divisíveis.
#
# obs2: não consegui executar nas maquinas 3 e 4 (me refiro as maquinas de 1 a 4)
# fornecidas pelo SIGAA. Só consigo executar nas maquinas 1 e 2. Elas até rodam
# mas quando eu altero a quantidade de processos a maquina 3 ou a 4 nunca respondem,
# ai o processo de rank 0 fica travado esperando a resposta e o programa fica em loop.
# por isso, considerei os testes somente nas maquinas 1 e 2.
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

TAM_ARRAY = 32

unsorted_array = np.zeros(TAM_ARRAY, dtype="int")
# final_sorted = np.zeros(TAM_ARRAY, dtype="int") apagar
local_a = np.zeros(int(TAM_ARRAY / size), dtype="int")
local_b = np.zeros(int(TAM_ARRAY / size), dtype="int")
array_merge = np.zeros(2 * int(TAM_ARRAY / size), dtype="int")

if rank == 0:
	unsorted_array = np.random.randint(low=0,high=TAM_ARRAY,size=TAM_ARRAY)
	print("Vetor de ", TAM_ARRAY," posicoes iniciais criado pelo Rank 0: \n", unsorted_array)

comm.Scatter(unsorted_array, local_a, root = 0)

local_a.sort()

# print("Rank: ", rank)
etapa = size / 2
while(etapa >= 1):
	if(rank >= etapa and rank < etapa * 2):
		# print("local_a do rank",rank," (vetor ja ordenado e enviando para o processo [", rank - etapa, "]):", local_a)
		comm.Send(local_a, rank - etapa, tag = 0)
	elif(rank < etapa):
		local_b = np.zeros(local_a.size, dtype="int")
		array_merge = np.zeros(2 * local_a.size, dtype="int")
		comm.Recv(local_b, rank + etapa, tag = 0)

		i = 0
		j = 0
		for k in range(0, 2 * local_a.size):
			if(i >= local_a.size):
				array_merge[k] = local_b[j]
				j += 1
			elif(j >= local_a.size):
				array_merge[k] = local_a[i]
				i += 1
			elif(local_a[i] > local_b[j]):
				array_merge[k] = local_b[j]
				j += 1
			else:
				array_merge[k] = local_a[i]
				i += 1
		#print("etapa: ", etapa)
		# print("local_a do rank", rank, " ordenado: ", local_a)
		# print("recepcao para local_b do rank", rank, " ordenado: ", local_b)
		# print("ordenacao final do rank", rank, ": ", array_merge)
		local_a = array_merge
	etapa = etapa / 2

if(rank == 0):
	print("**Resposta final**: ", local_a)
