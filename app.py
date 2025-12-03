from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
import os
from io import BytesIO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_meme():
    if 'image' not in request.files:
        return "Ni slike!", 400
    
    file = request.files['image']
    top_text = request.form.get('top_text', '').upper()
    bottom_text = request.form.get('bottom_text', '').upper()
    
    if file.filename == '':
        return "Ni izbrane datoteke!", 400
    
    img = Image.open(file.stream)
    
    draw = ImageDraw.Draw(img)
    
    width, height = img.size
    font_size = int(height/16)
    
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()

    def draw_text_with_outline(draw, text, position, font):
        x, y = position
        for adj_x in range(-5, 6):
            for adj_y in range(-5, 6):
                draw.text((x+adj_x, y+adj_y), text, font=font, fill="black")
        draw.text(position, text, font=font, fill="white")

    if top_text:
        bbox = draw.textbbox((0, 0), top_text, font=font)
        text_width = bbox[2] - bbox[0]
        draw_text_with_outline(draw, top_text, ((width - text_width) / 2, 10), font)

    if bottom_text:
        bbox = draw.textbbox((0, 0), bottom_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        draw_text_with_outline(draw, bottom_text, ((width - text_width) / 2, height - text_height - 20), font)

    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='meme.png')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
