import os

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if skip:
        skip = False
        continue
        
    # Look for the price container block
    # We expect:
    # <div class="price-container">
    #     <!-- <span class="price-old">R$ 97,00</span> -->
    #     <div class="price-tag">R$14,90</div>
    # </div>
    
    if '<div class="price-tag">R$14,90</div>' in line:
        # We found the inner tag. We need to replace the surrounding block.
        # The block starts 2 lines back (index i-2) and ends 1 line forward (index i+1)
        # But we are iterating.
        # Let's find the start of the block.
        pass

# Let's try a simpler approach: replace the specific lines we know from view_file
# Lines 1293-1296 (1-based) -> indices 1292-1295 (0-based)

start_idx = 1292
end_idx = 1295 # Inclusive of the closing div

# Verify content matches roughly what we expect to avoid destroying wrong things
if 'price-container' in lines[start_idx] and 'price-tag' in lines[start_idx+2]:
    print("Found target block at expected lines.")
    
    new_block = [
        '                    <div class="price-container" style="justify-content: center; margin-bottom: 20px;">\n',
        '                        <div style="border: 2px solid var(--accent-color); padding: 15px 40px; border-radius: 50px; display: inline-block; background-color: rgba(255, 187, 0, 0.05);">\n',
        '                            <div class="price-tag" style="margin-bottom: 0; line-height: 1;">R$14,90</div>\n',
        '                        </div>\n',
        '                    </div>\n'
    ]
    
    # Replace lines
    lines[start_idx:end_idx+1] = new_block
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Successfully updated pricing style.")
else:
    print("Target block not found at expected lines. Searching...")
    # Fallback search
    found = False
    for i in range(len(lines)):
        if '<div class="price-container">' in lines[i] and '<div class="price-tag">R$14,90</div>' in lines[i+2]:
            print(f"Found block starting at line {i+1}")
            lines[i:i+4] = new_block
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            print("Successfully updated pricing style via search.")
            found = True
            break
    if not found:
        print("Could not find target block.")
