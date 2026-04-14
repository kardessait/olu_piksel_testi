from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Tespit edilen pikselleri burada tutuyoruz
detected_pixels = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def report():
    data = request.get_json()
    detected_pixels.append(data)
    
    # Konsola detaylı bilgi yazdırır
    print(f"--- Yeni Ölü Piksel Raporu ---")
    print(f"Koordinat: X={data['x']}, Y={data['y']}")
    print(f"Ekran Rengi: {data['color']}")
    print(f"----------------------------")
    
    return jsonify({'status': 'ok', 'message': 'Veri kaydedildi'})

if __name__ == '__main__':
    # debug=True sayesinde hata alırsan tarayıcıda detayını görebilirsin
    app.run(debug=True)
