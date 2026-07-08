import os
import urllib.request
import hashlib
from urllib.parse import urlparse

image_urls = [
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=futuristic%20AI%20chatbot%20interface%20with%20green%20accent%20color%2C%20digital%20customer%20service%20dashboard%2C%20tech%20style%2C%20professional%20enterprise%20software&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=modern%20ecommerce%20website%20dashboard%20with%20world%20map%2C%20global%20trade%20analytics%2C%20green%20technology%20theme%2C%20professional%20business%20style&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=mobile%20app%20shopping%20mall%20interface%2C%20mini%20program%20design%2C%20green%20accent%20color%2C%20modern%20ecommerce%20UI%2C%20professional%20style&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=enterprise%20AI%20agent%20management%20platform%2C%20multiple%20AI%20bots%20dashboard%2C%20green%20tech%20theme%2C%20futuristic%20interface%2C%20professional&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=agricultural%20IoT%20monitoring%20system%2C%20smart%20farming%20dashboard%2C%20green%20plants%20and%20technology%2C%20data%20visualization%2C%20modern%20UI&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=cryptographic%20security%20monitoring%20dashboard%2C%20cybersecurity%20protection%20interface%2C%20green%20shield%20icon%2C%20professional%20tech%20style&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=advanced%20AI%20model%20neural%20network%20visualization%2C%20deep%20learning%20technology%2C%20green%20glow%2C%20futuristic%20digital%20brain%2C%20professional%20tech%20style&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=restaurant%20management%20system%2C%20POS%20dashboard%2C%20food%20service%20analytics%2C%20green%20technology%20theme%2C%20professional%20business&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=government%20AI%20service%20platform%2C%20public%20service%20chatbot%2C%20official%20blue%20and%20green%20theme%2C%20professional%20interface&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=cross-border%20distribution%20network%20system%2C%20Southeast%20Asia%20trade%20map%2C%20multi-language%20dashboard%2C%20green%20tech%20theme&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=AI%20artificial%20intelligence%20technology%20concept%2C%20neural%20network%2C%20green%20tech%20theme%2C%20futuristic%20digital%20brain%2C%20professional%20enterprise&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=software%20application%20development%2C%20mobile%20app%20and%20web%20development%2C%20green%20technology%20theme%2C%20professional%20tech%20style&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=global%20cross-border%20ecommerce%2C%20international%20trade%20network%2C%20world%20map%2C%20green%20tech%20theme%2C%20modern%20business&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=cybersecurity%20protection%20system%2C%20digital%20shield%2C%20encrypted%20data%2C%20green%20security%20theme%2C%20professional%20tech&image_size=landscape_16_9',
]

name_mapping = [
    'ai-chatbot.png',
    'ecommerce-dashboard.png',
    'mini-program.png',
    'ai-agent-platform.png',
    'agri-iot.png',
    'cybersecurity.png',
    'ai-neural-network.png',
    'restaurant-pos.png',
    'government-service.png',
    'cross-border.png',
    'ai-technology.png',
    'app-development.png',
    'global-trade.png',
    'security-shield.png',
]

public_dir = '/Users/richard/project/5.website-all/zkzn365.github.io/public'

os.makedirs(public_dir, exist_ok=True)

url_to_filename = {}

for i, url in enumerate(image_urls):
    filename = name_mapping[i]
    filepath = os.path.join(public_dir, filename)
    
    if os.path.exists(filepath):
        print(f'✓ {filename} already exists, skipping')
        url_to_filename[url] = f'/{filename}'
        continue
    
    try:
        print(f'Downloading {filename}...')
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url, filepath)
        
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f'✓ Downloaded {filename} ({size} bytes)')
            url_to_filename[url] = f'/{filename}'
        else:
            print(f'✗ Failed to download {filename}')
    except Exception as e:
        print(f'✗ Error downloading {filename}: {e}')

print('\nURL to filename mapping:')
for url, path in url_to_filename.items():
    print(f'  "{url}" -> "{path}"')

print(f'\nDownloaded {len(url_to_filename)} images to {public_dir}')