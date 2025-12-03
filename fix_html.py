import re

file_path = r'c:\Users\João\Documents\receitasaudavel\receitazero\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Pricing Section
# Remove the wrapper div with the border
# Pattern: <div\s+style="border: 2px solid var\(--accent-color\);[^>]+>\s*<div class="price-tag"
# We want to keep the inner div class="price-tag"

# Let's try to replace the specific style string first, effectively removing the border
style_str = 'border: 2px solid var(--accent-color); padding: 15px 40px; border-radius: 50px; display: inline-block; background-color: rgba(255, 187, 0, 0.05);'
if style_str in content:
    print("Found pricing style string")
    # We can just remove the style attribute content or the whole div wrapper.
    # Replacing the style string with empty string might leave an empty div wrapper which is fine-ish, but better to remove the wrapper.
    # But removing the wrapper is harder with simple replace.
    # Let's just remove the border and background from the style.
    # Or replace the whole block.
    
    # Let's try regex to match the block
    pattern = r'(<div\s+style="border: 2px solid var\(--accent-color\);[^"]+">)(\s*<div class="price-tag"[^>]+>.*?</div>)(\s*</div>)'
    # This is risky with regex on HTML.
    
    # Simpler: Replace the specific line with the style attribute with a simple <div> or nothing if we can.
    # The line is:
    # <div style="border: 2px solid var(--accent-color); padding: 15px 40px; border-radius: 50px; display: inline-block; background-color: rgba(255, 187, 0, 0.05);">
    
    # We can replace this line with nothing (start of wrapper) and the closing </div> (end of wrapper) with nothing?
    # No, that's hard to match the closing div.
    
    # Let's just remove the border styles from the string.
    new_style = '' # Remove all styles
    content = content.replace(style_str, new_style)
    
    # Now we have <div style=""> ... </div>
    # That removes the border.
    
else:
    print("Pricing style string NOT found")
    # Try to find it with flexible whitespace
    # This script is running in the same environment, so it should read the file exactly as it is.

# Fix Guarantee Card
# <div class="guarantee-card reveal" style="background-color: #4a2c25; border: none; box-shadow: none; flex-direction: column; text-align: center;">
guarantee_old = '<div class="guarantee-card reveal"\n                style="background-color: #4a2c25; border: none; box-shadow: none; flex-direction: column; text-align: center;">'
guarantee_new = '<div class="guarantee-card reveal card-dark"\n                style="border: none; box-shadow: none; flex-direction: column; text-align: center;">'

# We need to be careful with newlines.
# Let's try to match the style attribute part only.
guarantee_style_old = 'style="background-color: #4a2c25; border: none; box-shadow: none; flex-direction: column; text-align: center;"'
guarantee_style_new = 'style="border: none; box-shadow: none; flex-direction: column; text-align: center;"'

if guarantee_style_old in content:
    print("Found Guarantee style")
    content = content.replace(guarantee_style_old, guarantee_style_new)
    # And add the class
    content = content.replace('class="guarantee-card reveal"', 'class="guarantee-card reveal card-dark"')
else:
    print("Guarantee style NOT found")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
