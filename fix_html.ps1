$filePath = ".\index.html"
$content = Get-Content -Path $filePath -Raw -Encoding UTF8

# Fix Pricing Section
$styleStr = 'border: 2px solid var(--accent-color); padding: 15px 40px; border-radius: 50px; display: inline-block; background-color: rgba(255, 187, 0, 0.05);'
if ($content.Contains($styleStr)) {
    Write-Host "Found pricing style string"
    $content = $content.Replace($styleStr, "")
}
else {
    Write-Host "Pricing style string NOT found"
}

# Fix Guarantee Card
$guaranteeStyleOld = 'style="background-color: #4a2c25; border: none; box-shadow: none; flex-direction: column; text-align: center;"'
$guaranteeStyleNew = 'style="border: none; box-shadow: none; flex-direction: column; text-align: center;"'

if ($content.Contains($guaranteeStyleOld)) {
    Write-Host "Found Guarantee style"
    $content = $content.Replace($guaranteeStyleOld, $guaranteeStyleNew)
    $content = $content.Replace('class="guarantee-card reveal"', 'class="guarantee-card reveal card-dark"')
}
else {
    Write-Host "Guarantee style NOT found"
}

Set-Content -Path $filePath -Value $content -Encoding UTF8
Write-Host "Done"
