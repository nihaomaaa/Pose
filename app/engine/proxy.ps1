$p=Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings'
if($p.ProxyEnable -eq 1){$p.ProxyServer}
