class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Retornar la cantidad de dias que hay que esperar para tener un dia mas calido
        # Iterar sobre temperatures y para cada variable, metemos otro ciclo que cuente los dias hasta que 
            # llegue uno mas calido
        # Si meto todo a un stack, checar las temperaturas mayores, es sencillo?

        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            acc = 0
            
            for j in range(i,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    break
                else:
                    acc += 1
                    if j == len(temperatures)-1:
                        acc = 0
                        break
                
            res[i] = acc

        return res