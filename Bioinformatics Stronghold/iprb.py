k = 25.0
m = 17.0
n = 18.0

population = m+n+k

p = (k/population)*(1.0) + (m/population)*((k+(0.75*(m-1))+(0.5)*n)/(population-1)) + ((n/population)*(k+(0.5*m))/(population-1))
print(p)