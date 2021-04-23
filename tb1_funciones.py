#Función recursiva para hallar las combinaciones
def comb(n, m, info, nr, vec, ans):
    if (n-1==nr):
        aux = [None]*n
        for e in range(n):
            aux[e] = vec[info[e]]
        ans.append(aux)
        return

    for j in range(info[nr]+1, m):
        info[nr+1] = j
        comb(n, m, info, nr+1, vec, ans)

#Obtener todas las combinaciones posibles sin repetición
def get_comb(n, m):
    ans = []
    vec = [i for i in range(m)]
    info = [None]*(n+1) #El ultimo None no se usa pero es para evitar error
    for i in range(m):
        info[0] = i
        comb(n, m, info, 0, vec, ans)
    return ans

def get_states(m):
	aux = []
	for i in range(1, m+1):
		aux.extend(get_comb(i, m))
	return aux