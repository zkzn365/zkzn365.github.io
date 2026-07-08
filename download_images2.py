import os
import urllib.request
import urllib.parse

image_defs = [
    {'name': 'ai-chatbot', 'prompt': 'futuristic AI chatbot interface with green accent color, digital customer service dashboard, tech style, professional enterprise software'},
    {'name': 'ecommerce-dashboard', 'prompt': 'modern ecommerce website dashboard with world map, global trade analytics, green technology theme, professional business style'},
    {'name': 'mini-program', 'prompt': 'mobile app shopping mall interface, mini program design, green accent color, modern ecommerce UI, professional style'},
    {'name': 'ai-agent-platform', 'prompt': 'enterprise AI agent management platform, multiple AI bots dashboard, green tech theme, futuristic interface, professional'},
    {'name': 'agri-iot', 'prompt': 'agricultural IoT monitoring system, smart farming dashboard, green plants and technology, data visualization, modern UI'},
    {'name': 'cybersecurity', 'prompt': 'cryptographic security monitoring dashboard, cybersecurity protection interface, green shield icon, professional tech style'},
    {'name': 'ai-neural-network', 'prompt': 'advanced AI model neural network visualization, deep learning technology, green glow, futuristic digital brain, professional tech style'},
    {'name': 'restaurant-pos', 'prompt': 'restaurant management system, POS dashboard, food service analytics, green technology theme, professional business'},
    {'name': 'government-service', 'prompt': 'government AI service platform, public service chatbot, official blue and green theme, professional interface'},
    {'name': 'cross-border', 'prompt': 'cross-border distribution network system, Southeast Asia trade map, multi-language dashboard, green tech theme'},
    {'name': 'ai-technology', 'prompt': 'AI artificial intelligence technology concept, neural network, green tech theme, futuristic digital brain, professional enterprise'},
    {'name': 'app-development', 'prompt': 'software application development, mobile app and web development, green technology theme, professional tech style'},
    {'name': 'global-trade', 'prompt': 'global cross-border ecommerce, international trade network, world map, green tech theme, modern business'},
    {'name': 'security-shield', 'prompt': 'cybersecurity protection system, digital shield, encrypted data, green security theme, professional tech'},
]

base_url = 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image'
public_dir = '/Users/richard/project/5.website-all/zkzn365.github.io/public'

os.makedirs(public_dir, exist_ok=True)

def detect_image_type(filepath):
    with open(filepath, 'rb') as f:
        header = f.read(12)
    if header[:8] == b'\x89PNG\r\n\x1a\n':
        return 'png'
    elif header[:3] == b'\xff\xd8\xff':
        return 'jpg'
    elif header[:4] == b'RIFF' and header[8:12] == b'WEBP':
        return 'webp'
    return 'jpg'

for item in image_defs:
    encoded_prompt = urllib.parse.quote(item['prompt'])
    url = f'{base_url}?prompt={encoded_prompt}&image_size=landscape_16_9'
    
    temp_path = os.path.join(public_dir, f"{item['name']}_temp")
    
    try:
        print(f"Downloading {item['name']}...")
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url, temp_path)
        
        if os.path.exists(temp_path):
            ext = detect_image_type(temp_path)
            final_path = os.path.join(public_dir, f"{item['name']}.{ext}")
            
            if os.path.exists(final_path):
                os.remove(final_path)
            
            os.rename(temp_path, final_path)
            
            size = os.path.getsize(final_path)
            print(f"✓ Saved {final_path} ({size} bytes, type: {ext})")
        else:
            print(f"✗ Failed to download {item['name']}")
    except Exception as e:
        print(f"✗ Error downloading {item['name']}: {e}")
        if os.path.exists(temp_path):
            os.remove(temp_path)

print(f"\nDownload complete!")