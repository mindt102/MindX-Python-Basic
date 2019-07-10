districts = ["ST","BD","BTL","CG","DD","HBT"]
population = [150.300,247.100,333.300,266.800,420.900,318.000]
area = [117.43,9.224,43.35,12.04,9.96,10.09]

max_i = population.index(max(population))
min_i = population.index(min(population))

print("Quan co dan so dong nhat:",districts[max_i])
print("Quan co dan so it nhat:",districts[min_i])

density = []
for i in range(len(population)):
    density.append(population[i]/area[i])

avg_dens = round(sum(density)/(len(density)+1),4)
print("Mat do dan cu trung binh:",avg_dens)

