import os

# Define the mapping from filename to placeholder
MAPPING = {
    'earth.png': 'PLACEHOLDER_EARTH_BASE64',
    'meteor.png': 'PLACEHOLDER_METEOR_BASE64',
    'key.png': 'PLACEHOLDER_KEY_BASE64',
    'guardian.png': 'PLACEHOLDER_GUARDIAN_BASE64',
    'bullet.png': 'PLACEHOLDER_BULLET_BASE64',
    'intro.jpg': 'PLACEHOLDER_INTRO_BASE64',
    'PauseButton.png': 'PLACEHOLDER_PAUSE_BTN_BASE64',
    'boss.png': 'PLACEHOLDER_BOSS_BASE64',
    'explosion.png': 'PLACEHOLDER_EXPLOSION_BASE64',
    'EarthExplosion.wav': 'PLACEHOLDER_EARTH_EXPLOSION_BASE64',
    'KeyGet.wav': 'PLACEHOLDER_KEY_GET_BASE64',
    'MeteorExplosion.wav': 'PLACEHOLDER_METEOR_EXPLOSION_BASE64'
}

ASSETS_FILE = 'assets.txt'
HTML_FILE = 'index.html'

def main():
    # Read the assets file
    assets_data = {}
    with open(ASSETS_FILE, 'r') as f:
        for line in f:
            if '|' in line:
                filename, data = line.strip().split('|', 1)
                assets_data[filename] = data

    # Read the HTML file
    with open(HTML_FILE, 'r') as f:
        html_content = f.read()

    # Replace placeholders
    for filename, placeholder in MAPPING.items():
        if filename in assets_data:
            print(f"Injecting {filename} into {placeholder}...")
            html_content = html_content.replace(placeholder, assets_data[filename])
        else:
            print(f"Warning: {filename} not found in {ASSETS_FILE}")

    # Write the modified HTML back
    with open(HTML_FILE, 'w') as f:
        f.write(html_content)

    print("Injection complete!")

if __name__ == '__main__':
    main()
