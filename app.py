from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "🎯 YXNGBOITORRES-EA is working! Go to /dashboard"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/signals')
def get_signals():
    symbols = ['EURUSD', 'GBPUSD', 'USDJPY', 'XAUUSD']
    signals = []
    
    for symbol in symbols:
        price = round(random.uniform(1.0800, 1.0900), 5) if 'USD' in symbol else round(random.uniform(140, 150), 2)
        change = round(random.uniform(-0.01, 0.01), 4)
        
        signals.append({
            'symbol': symbol,
            'price': price,
            'change': change,
            'change_percent': round(change * 100, 2),
            'rsi': round(random.uniform(20, 80), 2),
            'signal': random.choice(['STRONG_BUY', 'BUY', 'NEUTRAL', 'SELL', 'STRONG_SELL']),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    
    return jsonify(signals)

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'time': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
