<# - - - - - Equipo PowerTNTShell - - - - -
                  Integrantes
              1.- Edgar Sandoval
              2.- Sergio Torres
              3.- Aidan Rodriguez             
   - - - - - - - - - - - - - - - - - - - - -
Objetivo
El principal propósito de este script es el uso
del módulo de Microsoft Teams, donde se han creado
funciones donde será posible realizar acciones en
tu perfil de inicio de sesión. Como agregar un equipo,
agregar/eliminar gente o bien, revisar en qué equipos
estamos agregados.

*****Módulos a instalar*****
Para que haya conexión con MicrosoftTeams, será necesario
ejecutar los comandos siguientes para instalar los módulos:
Install-Module -Name PowerShellGet -Force 
Install-Module -Name MicrosoftTeams -Force 

******ADVERTENCIA****** 
1. Antes de ejecutar el script principal
MicrosoftTeamsSettings.ps1 será necesario iniciar sesión
en Teams a través de la linea de comandos
haciendo uso del comando "Connect-MicrosoftTeams", seguido de esto,
será posible ejecutar correctamente el programa. 
2. A causa de la conexión con la aplicación y módulos de MicrosoftTeams,
podría darse un error en el primer intento al realizar una acción usando
el script.
#>
cls
$flag = $true
Write-Host "BIENVENIDO - INICIAR SESION"
#Connect-MicrosoftTeams

do{
    
    cls
    Write-Host "= = = = = = = = = = MENU = = = = = = = = = =`n
    [1] Ver equipos/info 
    [2] Agregar un equipo 
    [3] Eliminar un Equipo 
    [4] Ver miembros de un equipo 
    [5] Agregar una persona a un equipo
    [6] Eliminar una persona de un equipo
    [7] Salir de la aplicacion"
    Write-Host "= = = = = = = = = = = = = = = = = = = = = = `n"

    $UserOp = Read-Host -Prompt "Que desea hacer?"

    switch($UserOp)
    {
        1{
            Write-Host "`n= = = = = = = = = Ver equipos/info = = = = = = = = =`n"
            do
            {
            [int]$op_user = Read-Host -Prompt "[1]Id_Grupo | [2]Por Correo del Usuario`nComo desea buscar el equipo?"
            }while($op_user -ne 1 -and $op_user -ne 2)
            View-MicrosoftTeams -op $op_user
        }
        2{
            Write-Host "`n= = = = = = = = = Agregar un equipo = = = = = = = = =`n"
            Add-MicrosoftTeams
        }
        3{
            Write-Host "`n= = = = = = = = = Eliminar un Equipo = = = = = = = = =`n"
            Delete-MicrosoftTeams
        }
        4{
            Write-Host "`n= = = = = = = = = Ver miembros de un equipo = = = = = = = = =`n"
            Get-UsersOnTeam
        }
        5{
            Write-Host "`n= = = = = = = = = Agregar una persona a un equipo = = = = = = = = =`n"
            Add-MembersOnTeam
        }
        6{
            Write-Host "`n= = = = = = = = = Eliminar una persona de un equipo = = = = = = = = =`n"
            Remove-MembersOnTeam
        }
        7{
            $flag = $false
        }
        default{
            Write-Host "Opcion no valida, intenta de nuevo..."
        }
    }

}while($flag -eq $true)
Write-Host "Adios!!"