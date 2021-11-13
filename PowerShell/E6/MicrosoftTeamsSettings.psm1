function View-MicrosoftTeams {
    [CmdletBinding()] param([Parameter(Mandatory)] [int] $op)

    switch($op){
        1 {
            try{
                [string]$Gid = Read-Host -Prompt "Ingrese el ID del grupo a buscar" 
                Get-Team -GroupId $Gid -ErrorAction Stop
                Read-Host "`nPresione enter para continuar..."
            }
            catch{
                $_.Exception.Message
                Read-Host "`nPresione una enter para continuar..."
            }
        }
        2{
            try{
                [string]$Mail_User = Read-Host -Prompt "Ingresa tu correo electrónico"
                Get-Team -User $Mail_User -ErrorAction Stop
                Read-Host "`nPresione enter para continuar..."

            }
            catch{
                $_.Exception.Message
                Read-Host "`nPresione enter para continuar..."
            }
        }
        default{
            Read-Host "Opcion no valida, intente de nuevo..."

        }
    }
}

function Add-MicrosoftTeams {
    try{
        [string]$Team_name = Read-Host -Prompt "Ingrese el nombre del grupo"
        [string]$Team_info = Read-Host -Prompt "Ingrese la descripcion del grupo"
        do
        {
        [int] $op_view = Read-Host -Prompt "El grupo sera [1]Publico o [2]Privado?" -ErrorAction Stop
        }while($op_view -ne 1 -and $op_view -ne 2)

        if ($op_view -eq 1){
            $Team_view = "Public"
        }
        elseif ($op_view -eq 2){
            $Team_view = "Private"
        }
        else{
            $Team_view = "Public"
        }

        [string]$Team_admin = Read-Host -Prompt "Ingrese el correo propietario del grupo (deberá ser el tuyo por ser creador)"

        New-Team -DisplayName $Team_name -Description $Team_info -Visibility $Team_view -Owner $Team_admin -ErrorAction Stop
        Write-Host "`nEquipo creado correctamente"
        Read-Host "`nPresione enter para continuar..."
    }
    catch{
        $_.Exception.Message
        Read-Host "`nPresione enter para continuar..."
    }
    
}

function Delete-MicrosoftTeams {
    try{
        [string]$Gid_Del = Read-Host -Prompt "Ingrese el ID del grupo a eliminar"
        Remove-Team -GroupId $Gid_Del -ErrorAction Stop
        Write-Host "`nEquipo eliminado correctamente"
        Read-Host "`nPresione enter para continuar..."
    }
    catch{
        $_.Exception.Message
        Read-Host "`nPresione enter para continuar..."
    }
}

function Get-UsersOnTeam {
    try{
        [string]$Gid_getUsr = Read-Host -Prompt "Ingrese el ID del grupo"
        do
        {
        [int]$User_mode = Read-Host -Prompt "Quiere buscar [1]Propietarios [2]Miembros?" -ErrorAction Stop
        }while($User_mode -ne 1 -and $User_mode -ne 2)
        if ($User_mode -eq 1){
            $Srch_UserMode = "Owner"
        }
        elseif ($User_mode -eq 2){
            $Srch_UserMode = "Member"
        }
        else{
            $Srch_UserMode = "Member"
        }

        Get-TeamUser -GroupId $Gid_getUsr -Role $Srch_UserMode
        Read-Host "`nPresione enter para continuar..."
    }
    catch{
        $_.Exception.Message
        Read-Host "`nPresione enter para continuar..."
    }
}

function Remove-MembersOnTeam {
    try{
        [string]$Gid_getUsr = Read-Host -Prompt "Ingrese el ID del grupo"
        do
        {
        [int]$User_mode = Read-Host -Prompt "Qué tipo de usuario desea eliminar?[1]Miembro [2]Propietario" -ErrorAction Stop
        }while($User_mode -ne 1 -and $User_mode -ne 2)
        if ($User_mode -eq 1){
            Write-Host "La eliminación del miembro en el equipo se verá reflejado en la aplicación Microsoft Teams en un tiempo más tardado" 
        }
        elseif ($User_mode -eq 2){
            Write-Host "La eliminación de un miembro propietario solo le quita el puesto y lo cambia a ser un miembro más del equipo"
            Write-Host "`nPara eliminar completamente al miembro, vuelva a eliminarlo con la opción de eliminar usuario tipo miembro" 
        }
        [string]$email_User = Read-Host -Prompt "Ingrese correo de usuario"
        if ($User_mode -eq 1){
            Remove-TeamUser -GroupId $Gid_getUsr -User $email_User
            Write-Host "`nMiembro eliminado correctamente"
        }
        elseif ($User_mode -eq 2){
            Remove-TeamUser -GroupId $Gid_getUsr -User $email_User -Role Owner
            Write-Host "`nUsuario eliminado como propietario correctamente"
        }
        Read-Host "`nPresione enter para continuar..."
    }
    catch{
        $_.Exception.Message
        Read-Host "`nPresione enter para continuar..."
    }
}

function Add-MembersOnTeam {
    try{
        [string]$Gid_getUsr = Read-Host -Prompt "Ingrese el ID del grupo"
        do
        {
        [int]$User_mode = Read-Host -Prompt "Qué tipo de usuario desea agregar?[1]Miembro [2]Propietario" -ErrorAction Stop
        }while($User_mode -ne 1 -and $User_mode -ne 2)
        [string]$email_User = Read-Host -Prompt "Ingrese correo de usuario"
        if ($User_mode -eq 1){
            Add-TeamUser -GroupId $Gid_getUsr -User $email_User
        }
        elseif ($User_mode -eq 2){
            Add-TeamUser -GroupId $Gid_getUsr -User $email_User -Role Owner
        }
        Write-Host "`nMiembro agregado correctamente"
        Read-Host "`nPresione enter para continuar..."
    }
    catch{
        $_.Exception.Message
        Read-Host "`nPresione enter para continuar..."
    }
}