$path = "index.html"
$lines = Get-Content $path
$startIdx = 1292
$endIdx = 1295

# Verify content roughly
if ($lines[$startIdx] -match "price-container" -and $lines[$startIdx + 2] -match "price-tag") {
    Write-Host "Found target block at expected lines."
    
    $newBlock = @(
        '                    <div class="price-container" style="justify-content: center; margin-bottom: 20px;">',
        '                        <div style="border: 2px solid var(--accent-color); padding: 15px 40px; border-radius: 50px; display: inline-block; background-color: rgba(255, 187, 0, 0.05);">',
        '                            <div class="price-tag" style="margin-bottom: 0; line-height: 1;">R$14,90</div>',
        '                        </div>',
        '                    </div>'
    )
    
    # Replace
    # We construct new array
    $newContent = $lines[0..($startIdx - 1)] + $newBlock + $lines[($endIdx + 1)..($lines.Count - 1)]
    $newContent | Set-Content $path -Encoding UTF8
    Write-Host "Successfully updated pricing style."
}
else {
    Write-Host "Target block not found at expected lines. Searching..."
    # Search
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -match '<div class="price-container">' -and $lines[$i + 2] -match '<div class="price-tag">R\$14,90</div>') {
            Write-Host "Found block starting at line $($i+1)"
            $newBlock = @(
                '                    <div class="price-container" style="justify-content: center; margin-bottom: 20px;">',
                '                        <div style="border: 2px solid var(--accent-color); padding: 15px 40px; border-radius: 50px; display: inline-block; background-color: rgba(255, 187, 0, 0.05);">',
                '                            <div class="price-tag" style="margin-bottom: 0; line-height: 1;">R$14,90</div>',
                '                        </div>',
                '                    </div>'
            )
            $newContent = $lines[0..($i - 1)] + $newBlock + $lines[($i + 4)..($lines.Count - 1)]
            $newContent | Set-Content $path -Encoding UTF8
            Write-Host "Successfully updated pricing style via search."
            break
        }
    }
}
