
# scripts/log_analysis.ps1
```powershell
# PowerShell Script: Analyze Windows Security Logs
Write-Host "Starting Security Log Analysis..."

# Define log path
$logFilePath = "C:\\Windows\\System32\\winevt\\Logs\\Security.evtx"

# Check for log file
if (!(Test-Path $logFilePath)) {
    Write-Error "Log file not found: $logFilePath"
    exit
}

# Import logs
$events = Get-WinEvent -Path $logFilePath -FilterHashtable @{LogName="Security"}

# Analyze logs for unauthorized access
$unauthorizedLogins = $events | Where-Object {
    $_.Id -eq 4625 -or $_.Id -eq 4648
}

if ($unauthorizedLogins) {
    Write-Host "Potential unauthorized access detected:"
    $unauthorizedLogins | Format-Table -AutoSize
} else {
    Write-Host "No unauthorized access detected."
}

Write-Host "Analysis Complete."
```
