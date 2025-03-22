
#programa para calcular


dados <- data.frame(dadosA = c(12,13,14,15,16,16))

mean(dados$dadosA)

median(dados$dadosA)

Mode(dados$dadosA)

sd(dados$dadosA)




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


