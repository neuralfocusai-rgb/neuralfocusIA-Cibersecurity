# Scripts: Automated Windows Security Audit ⚙️🔍

This PowerShell script allows hospital IT administrators to quickly verify if basic security policies (like active Firewalls and Screen Lock configurations) are enforced on a medical workstation.

## 🚀 How to use
1. Open Windows PowerShell as Administrator on the clinical workstation.
2. Copy and paste the script below.
3. Press Enter to see the security status report.

```powershell
Write-Host "🏥 neuralFocusAI - Medical Workstation Security Audit" -ForegroundColor Cyan
Write-Host "--------------------------------------------------------"

# 1. Check Windows Firewall Status
Write-Host "🛡️ 1. Checking Windows Firewall Status..." -ForegroundColor Yellow
$Firewall = Get-NetFirewallProfile -Profile Domain,Public,Private | Select-Object Name, Enabled
$Firewall | Format-Table

# 2. Check Screen Lock Configuration
Write-Host "🔒 2. Checking Screen Auto-Lock Policy..." -ForegroundColor Yellow
$ScreenLock = Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "InactivityTimeoutSecs" -ErrorAction SilentlyContinue

if ($ScreenLock) {
    Write-Host "[OK] Screen Lock Timeout is configured." -ForegroundColor Green
} else {
    Write-Host "[WARNING] Screen Lock is NOT configured. This is a critical privacy risk!" -ForegroundColor Red
}

Write-Host "--------------------------------------------------------"
Write-Host "Audit Complete. Please remediate any warnings." -ForegroundColor Cyan
