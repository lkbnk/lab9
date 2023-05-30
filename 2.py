from PIL import Image, ImageFilter
from pathlib import Path

current_dir = ""
image = Path(current_dir).glob('*')
Path('newfile').mkdir(parents=True, exist_ok=True)
for i in image:
    if i.suffix in ['.jpg', '.png']:
        with Image.open(image) as img:
            img.load()
            new_img = img.filter(ImageFilter.EDGE_ENHANCE)
            new_img.save(Path('newfile/NEW_' + i))