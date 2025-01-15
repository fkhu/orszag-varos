function Start-Countdown {
    param(
        $seconds,
        $message
    )
    foreach ( $count in (1..$seconds) ) {
        Write-Progress -Id 1 -Activity $Message -Status "Visszaszámlálás: $($seconds - $count) másodperc" -PercentComplete ( ($Count / $Seconds) * 100 )
        [console]::CursorVisible = $false
        Start-Sleep -Seconds 1
        if (($seconds - $count) -le 6 -and ($seconds - $count) -ne 0) {say -v Bells "bip"}
    }
    Write-Progress -Id 1 -Activity $Message -Status "Completed" -PercentComplete 100 -Completed
    say -v Bells "beeeeeep"; afplay ./vege.mp3
}

function Start-Game {
    Clear-Host
    $letter = Get-RandomLetter
    Write-Host "A következő betű a(z): - $letter -"
    if (Get-UserInput "Jó lesz? Mehet? (i|n)") {
        Clear-Host
        Start-Countdown -Seconds 120 -Message "Mehet a játék! A jelenlegi betű: - $letter -"
        if (Get-UserInput "Lejárt az idő. Mégegy játék? (i|n)") {
            Start-Game
        } else {
            Write-Host "`nVége`n"
        }
    } else {
        Start-Game
    }
}

function Get-UserInput {
    param(
        [string]$message
    )
    while ($true) {
        $char = Read-CharacterInput $message
        if ($char -match '(^|,)(i|n)') {
            return $char -eq "i"
        } else {
            Write-Host $message
        }
    }
}

function Get-RandomLetter {
    $alph = @('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','Z')
    $letter = $alph | Get-Random
    if ($letter -in "Q", "W", "Y", "X") { 
        return Get-RandomLetter
    }
    else {
        switch ($letter) {
            "A" { return "A,Á" }
            "C" { return "C,CS" }
            "D" { return "D,DZ,DZS" }
            "E" { return "E,É" }
            "G" { return "G,GY" }
            "I" { return "I,Í" }
            "J" { return "J,LY" }
            "N" { return "N,NY" }
            "O" { return "O,Ó,Ö,Ő" }
            "S" { return "S,SZ" }
            "T" { return "T,TY" }
            "U" { return "U,Ú,Ü,Ű" }
            "Z" { return "Z,ZS" }
            Default { return $letter }
        }
    }
}

function Read-CharacterInput {
    param(
        [string]$prompt
    )
    Write-Host $prompt
    while ($true) {
        $key = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
        $char = $key.Character
        if (!($char -match '(^|,)(i|n)')) {
            Write-Host $prompt
        }
        else { return $char }
    }
}

# Main:
Start-Game