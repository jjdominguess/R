
#Tendo em vista o uso dos insumos do arquivo AtividadeFase01.py, segue o código em R para cálculo de médias e desvio padrão

plantInput <- data.frame(potassiumInput = c(0.05, 0.06, 0.07, 0.08, 0.09), 
                         phosphorusInput = c(0.08, 0.09, 0.10, 0.11, 0.12))

mean(plantInput$potassiumInput)
mean(plantInput$phosphorusInput)

sd(plantInput$phosphorusInput)
sd(plantInput$potassiumInput)

print("Média de Potássio")
mean(plantInput$potassiumInput)

print("Média de Fósforo")
mean(plantInput$phosphorusInput)

print("Desvio Padrão de Potássio")
sd(plantInput$potassiumInput)

print("Desvio Padrão de Fósforo")
sd(plantInput$phosphorusInput)



#programa da API

# Instalando os pacotes
if (!require(httr)) install.packages("httr", dependencies = TRUE)
if (!require(jsonlite)) install.packages("jsonlite", dependencies = TRUE)

#Iniciar as bibliotecas
library(httr)
library(jsonlite)

#URL da API
url <- "https://api.weatherapi.com/v1/current.json?q=S%C3%A3o%20Paulo&lang=Pt-BR&key=b451680b05f2425b8dd00420252003"

# API kEY
api_key <- "b451680b05f2425b8dd00420252003"  

# Linha para fazer a requisicao - Passei o Token no Authorization
response <- GET(url, add_headers(Authorization = paste("Bearer", api_key)))

# Fiz a requisição GET para a API
response <- GET(url)

# Se for 200 deu sucesso
if (status_code(response) == 200) {
  # converti para JSON e listei
  dados <- fromJSON(content(response, "text"))
  print(dados)
} else {
  print(paste("Erro: Código", status_code(response)))
}


