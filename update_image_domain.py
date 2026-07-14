import sys
import os

if len(sys.argv) < 2:
    print("Usage: python update_image_domain.py <new_domain_url>")
    print("Example: python update_image_domain.py https://mywebsite.com/flight-images/")
    sys.exit(1)

new_domain = sys.argv[1].rstrip('/') + '/'
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "catalog_flight.csv")

if not os.path.exists(csv_path):
    print(f"Error: {csv_path} not found.")
    sys.exit(1)

with open(csv_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Replace the placeholder URL with the user's actual hosting URL
    new_line = line.replace("https://yourdomain.com/flight-images/", new_domain)
    new_lines.append(new_line)

with open(csv_path, 'w', encoding='utf-8', newline='') as f:
    f.writelines(new_lines)

print(f"SUCCESS: Replaced image domain in catalog_flight.csv with: {new_domain}")
