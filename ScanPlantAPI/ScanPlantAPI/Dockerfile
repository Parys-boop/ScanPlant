FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

COPY ["ScanPlantAPI.csproj", "./"]
RUN dotnet restore "ScanPlantAPI.csproj"

COPY . .
RUN dotnet build "ScanPlantAPI.csproj" -c Release -o /app/build
RUN dotnet publish "ScanPlantAPI.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app/publish .

ENV ASPNETCORE_URLS=http://+:$PORT

ENTRYPOINT ["dotnet", "ScanPlantAPI.dll"]
