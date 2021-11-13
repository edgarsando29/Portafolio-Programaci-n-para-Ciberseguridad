#Rodríguez Bautista Aidan Eduardo || Juárez Torres Sergio Javier || Sandoval Salazar Edgar Omar
do
{
cls
$opc = Read-Host -Prompt "*****MENÚ*****
[1] Ver StatusPerfil
[2] Cambiar-StatusPerfil
[3] Ver-PerfilRedActual
[4] Cambiar-PerfilRedActual
[5] Ver-ReglasBloqueo
[6] Agregar-ReglasBloqueo
[7] Eliminar-ReglasBloqueo

Qué desea hacer?"

switch($opc){
    1 {
        Write-Host "`n= = = = = = = = = Ver-StatusPerfil = = = = = = = = ="
        do
        {
        $op_perfil = Read-Host -Prompt "Que Perfil quieres ver? (Public, Private): "
        }while($op_perfil -ne "Public" -and $op_perfil -ne "Private") 
        write-host "`n"
        Ver-StatusPerfil -perfil $op_perfil
            
    }
    2 {
        Write-Host "`n= = = = = = = = = Cambiar-StatusPerfil = = = = = = = = ="
        do
        {
        $op_perfil = Read-Host -Prompt "Que Perfil quieres cambiar? (Public, Private): "
        }while($op_perfil -ne "Public" -and $op_perfil -ne "Private")
        write-host "`n"
        Cambiar-StatusPerfil -perfil $op_perfil
    }
    3{
        Write-Host "`n= = = = = = = = = Ver-PerfilRedActual = = = = = = = = ="
        Ver-PerfilRedActual
    }
    
    4 {
        Write-Host "`n= = = = = = = = = Cambiar-PerfilRedActual = = = = = = = = ="
        Cambiar-PerfilRedActual
    }
    5{
        Write-Host "`n= = = = = = = = = Ver-ReglasBloqueo = = = = = = = = ="
        Ver-ReglasBloqueo
    }
    6{
        Write-Host "`n= = = = = = = = = Agregar-ReglasBloqueo = = = = = = = = ="
        Agregar-ReglasBloqueo
    }
    7{
        Write-Host "`n= = = = = = = = = Eliminar-ReglasBloqueo = = = = = = = = ="
        Eliminar-ReglasBloqueo
    }
      
    default{
        Write-Host "Opción no válida, intente de nuevo"
    }
    }
$flag = $false
while ($flag -eq $false)
{
    $continue = Read-Host -Prompt "`nDesea continuar usando el programa? Si[Y] / No[N]: "

    if ($continue -eq "Y" -or $continue -eq "N"){
        $flag = $True
    }
    else{
        Write-Host "Opcional no valida..."
    }
}

}while ($continue -eq "Y")
Write-Host "Adios!!"