# parallel-ordering-MPI
Trabalho de Sistemas Distribuídos para ordenar um vetor aleatório usando a biblioteca MPI

# Descrição do trabalho
Usando a biblioteca MPI, desenvolva um programa que ordene um vetor em paralelo. O vetor deverá ser dividido e distribuído entres os processos. Cada processo deve ordenar localmente seu vetor. A seguir, o processor 0 deverá reunir esses valores e imprimir o resultado.

# Análise do trabalho
Após pesquisa, percebeu-se que o mecanismo de divisão dos vetores e envio para outros processos é semelhante ao processo de divisão dos vetores nos diferentes métodos de ordenação. Então, por facilidade de implementação, decidiu-se usar o método Merge Sort, mas é possível usar qualquer outro, como Bubble Sort, Quick Sort, etc.

# Modo de uso
Após configurar as máquinas com SSH, NFS, configurar a montagem da pasta de compartilhamento, execute o comando: ``` mpiexec -np 4 --hostfile maqs.txt python sort_parallel.py ```. Não esqueça de criar um arquivo chamado maqs.txt contendo o nome de todas as máquinas que rodarão os processos em paralelo.