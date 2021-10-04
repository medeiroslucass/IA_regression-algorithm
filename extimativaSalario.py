from sklearn.linear_model import LinearRegression



#cargos
gerente = 1
programador = 2
designer = 3

#nivel
junior = 1
pleno = 2
senior = 3

atribuitos = [
    [20,gerente, senior, 52],
    [15,programador, senior, 43],
    [10,programador, pleno, 28],
    [4,gerente, junior, 32],
    [8,designer, senior, 40],
    [5,designer, pleno, 35],
    [6,designer, pleno, 29],
    [10,programador, junior, 30],
    [2, programador, junior, 22],
]

salarios = [14534, 10437.41,5333.07, 3587.23, 8983.43, 6467.40, 6183.58, 2853.52, 1849.53]

#Criar Modelo
modelo = LinearRegression()
modelo.fit(atribuitos, salarios)

# predicao
novosFuncionarios = [
    [12, gerente,pleno,38],
    [1, programador, junior, 19],
    [5, designer, senior, 32]

]

novosSalarios = modelo.predict(novosFuncionarios)
print(novosSalarios)