FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /app

# Copiar arquivos do projeto
COPY ScanPlantAPI/ScanPlantAPI/*.csproj ./ScanPlantAPI/ScanPlantAPI/
RUN dotnet restore ./ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.csproj

# Copiar todo o código
COPY ScanPlantAPI/ScanPlantAPI/. ./ScanPlantAPI/ScanPlantAPI/

# Build
WORKDIR /app/ScanPlantAPI/ScanPlantAPI
RUN dotnet publish -c Release -o /app/publish

# Runtime
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app/publish .

# Expor porta
EXPOSE 5041

# Comando de início
ENTRYPOINT ["dotnet", "ScanPlantAPI.dll"]
