$perfilRed = Get-NetConnectionProfile  
Write-Host "Nombre de red:" $perfilRed.Name  
Write-Host "Perfil de red:" $perfilRed.NetworkCategory
Write-Host "Conectividad IPv4:" $perfilRed.IPv4Connectivity
Write-Host "Conectividad IPv6:" $perfilRed.IPv6Connectivity