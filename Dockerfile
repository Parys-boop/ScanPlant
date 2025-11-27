FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Copiar apenas o .csproj primeiro para cache de dependências
COPY ["ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.csproj", "ScanPlantAPI/ScanPlantAPI/"]
RUN dotnet restore "ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.csproj"

# Copiar todo o código fonte
COPY ScanPlantAPI/ScanPlantAPI/ ScanPlantAPI/ScanPlantAPI/

# Build e publish
WORKDIR "/src/ScanPlantAPI/ScanPlantAPI"
RUN dotnet build "ScanPlantAPI.csproj" -c Release -o /app/build
RUN dotnet publish "ScanPlantAPI.csproj" -c Release -o /app/publish /p:UseAppHost=false

# Runtime
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app/publish .

# Railway define a variável PORT automaticamente
ENV ASPNETCORE_URLS=http://+:$PORT

ENTRYPOINT ["dotnet", "ScanPlantAPI.dll"]
