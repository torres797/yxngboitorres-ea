from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/signals')
def get_signals():
    symbols = ['EURUSD', 'GBPUSD', 'USDJPY', 'XAUUSD']
    signals = []
    
    for symbol in symbols:
        # Generate realistic price data
        if symbol == 'EURUSD':
            price = round(random.uniform(1.0800, 1.0900), 5)
        elif symbol == 'GBPUSD':
            price = round(random.uniform(1.2600, 1.2800), 5)
        elif symbol == 'USDJPY':
            price = round(random.uniform(147.00, 149.00), 2)
        else:  # XAUUSD
            price = round(random.uniform(1970.00, 1990.00), 2)
            
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
