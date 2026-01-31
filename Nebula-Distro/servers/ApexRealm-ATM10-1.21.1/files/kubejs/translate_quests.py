import os
import re
import json

# Paths
# Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
# Quests are usually in config/ftbquests/quests/chapters based on server root
# Script is in kubejs/translate_quests.py
# So we need to go up one level to server root (kubejs/.. = root), then config/ftbquests...
# root = ..
server_root = os.path.join(script_dir, "..")
quests_dir = os.path.join(server_root, "config", "ftbquests", "quests", "chapters")

# Translation Dictionaries (To be populated)
# Simple dictionary mapping English text -> (Russian, Ukrainian)
# In a real scenario, this could be loaded from an external file.
translations = {
    "Welcome": ("Добро пожаловать", "Ласкаво просимо"),
    "Join the Discord!": ("Присоединяйтесь к Discord!", "Приєднуйтесь до Discord!"),
    "First steps into the world of Allthemodium, required to progress.": ("Первые шаги в мире Аллземодиума, необходимые для прогресса.", "Перші кроки у світі Аллземодіуму, необхідні для прогресу."),
    # Add more translations here as discovered
}

def translate_text(text, lang):
    """
    Translates text. Returns the translation if found, otherwise returns title-cased or original text 
    marked with TODO if strictly needed, but here we will return the original if unknown 
    to avoid breaking things, or maybe a marked version.
    """
    if text in translations:
        if lang == 'ru':
            return translations[text][0]
        elif lang == 'uk':
            return translations[text][1]
    
    # Heuristic for unknown text: 
    # If we want to verify coverage, we could mark it. 
    # For now, let's keep it as English if unknown, but formatted in the JSON structure 
    # so the user can see it needs translation.
    return text 

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Pattern to find keys: title, subtitle
    # Regex for title: "Some Text"
    # We want to match: title: "Text" BUT NOT title: "{...}"
    # So we look for a quote that is NOT followed by a curly brace (escaped or not).
    # Since checking the content of the string is hard with regex, we can match the string 
    # and then check if it looks like JSON.
    
    def replacer(match):
        key = match.group(1) # title, subtitle, or plain text in description
        val = match.group(2) # The text content inside quotes
        
        # Check if already localized
        if val.strip().startswith('{') and '\"en\"' in val:
            return match.group(0) # Already localized
            
        # It's a raw string. Localize it.
        ru_val = translate_text(val, 'ru')
        uk_val = translate_text(val, 'uk')
        
        # Escape quotes in the inner strings if necessary (the regex captured the content *inside* quotes)
        # We need to construct the new JSON string.
        # The target format is: "{ \"en\": \"VAL\", \"ru\": \"RU_VAL\", \"uk\": \"UK_VAL\" }"
        # We need to escape double quotes inside VAL, RU_VAL, UK_VAL because they will be inside a string.
        
        def escape(s):
            return s.replace('"', '\\"')
            
        new_val = '{ \\"en\\": \\"' + escape(val) + '\\", \\"ru\\": \\"' + escape(ru_val) + '\\", \\"uk\\": \\"' + escape(uk_val) + '\\" }'
        
        return f'{key}: "{new_val}"'

    # Replace titles and subtitles
    # title: "Something"
    # subtitle: "Description"
    content = re.sub(r'(title|subtitle):\s*"(.*?)"', replacer, content)
    
    # Descriptions are trickier: description: [ "Line 1", "Line 2" ]
    # We can try to match the list content. 
    # Or just generic string matching? No, that's dangerous for IDs.
    # Let's target lines inside description: [...]
    # This involves a more complex parser or a specific regex for description blocks.
    # Simple approach: Find `description: [` and process lines until `]`.
    
    lines = content.split('\n')
    new_lines = []
    in_description = False
    
    for line in lines:
        stripped = line.strip()
        if 'description: [' in line:
            in_description = True
            new_lines.append(line)
            continue
            
        if in_description:
            if ']' in stripped:
                in_description = False
                new_lines.append(line)
                continue
            
            # Inside description, usually strings like: "Line text"
            # match: "Text"
            desc_match = re.match(r'^(\s*)"(.*)"(\s*)$', line)
            if desc_match:
                indent = desc_match.group(1)
                val = desc_match.group(2)
                
                if val.strip().startswith('{') and '\"en\"' in val:
                    new_lines.append(line)
                else:
                    # Localize
                    ru_val = translate_text(val, 'ru')
                    uk_val = translate_text(val, 'uk')
                    
                    def escape(s):
                        return s.replace('"', '\\"')
                    
                    new_val = '{ \\"en\\": \\"' + escape(val) + '\\", \\"ru\\": \\"' + escape(ru_val) + '\\", \\"uk\\": \\"' + escape(uk_val) + '\\" }'
                    new_lines.append(f'{indent}"{new_val}"')
            else:
                new_lines.append(line)
        else:
            # We already ran the regex on the whole content for title/subtitle? 
            # Actually, splitting lines invalidates the previous regex replace if we did it on `content`.
            # Let's do the title/subtitle replace on the *line* level too for simplicity.
            
            # Title/Subtitle regex on line
            ts_match = re.match(r'^(\s*)(title|subtitle):\s*"(.*?)"(\s*)$', line)
            if ts_match:
                indent = ts_match.group(1)
                key = ts_match.group(2)
                val = ts_match.group(3)
                
                if val.strip().startswith('{') and '\"en\"' in val:
                    new_lines.append(line)
                else:
                    ru_val = translate_text(val, 'ru')
                    uk_val = translate_text(val, 'uk')
                    
                    def escape(s):
                        return s.replace('"', '\\"')
                        
                    new_val = '{ \\"en\\": \\"' + escape(val) + '\\", \\"ru\\": \\"' + escape(ru_val) + '\\", \\"uk\\": \\"' + escape(uk_val) + '\\" }'
                    new_lines.append(f'{indent}{key}: "{new_val}"')
            else:
                new_lines.append(line)

    final_content = '\n'.join(new_lines)
    
    if final_content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Updated: {filepath}")
    else:
        # print(f"No changes: {filepath}")
        pass

def main():
    if not os.path.exists(quests_dir):
        print(f"Directory not found: {quests_dir}")
        return

    print("Starting translation...")
    count = 0
    for root, dirs, files in os.walk(quests_dir):
        for file in files:
            if file.endswith(".snbt"):
                process_file(os.path.join(root, file))
                count += 1
    print(f"Processed {count} files.")

if __name__ == "__main__":
    main()
