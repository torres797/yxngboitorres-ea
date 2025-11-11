from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
import requests
from datetime import datetime
import os

app = Flask(__name__)

class TradingAnalyzer:
    def __init__(self):
        self.symbols = ['EURUSD', 'GBPUSD', 'USDJPY', 'XAUUSD']
    
    def get_mock_data(self, symbol):
        """Generate mock market data (replace with real API)"""
        np.random.seed(hash(symbol) % 10000)
        
        # Simulate price data
        base_price = {
            'EURUSD': 1.0850,
            'GBPUSD': 1.2700,
            'USDJPY': 148.00,
            'XAUUSD': 1980.00
        }
        
        current_price = base_price.get(symbol, 1.0) + np.random.uniform(-0.01, 0.01)
        change = np.random.uniform(-0.005, 0.005)
        
        return {
            'symbol': symbol,
            'price': round(current_price, 5),
            'change': round(change, 4),
            'change_percent': round(change * 100, 2),
            'rsi': round(np.random.uniform(20, 80), 2),
            'signal': np.random.choice(['STRONG_BUY', 'BUY', 'NEUTRAL', 'SELL', 'STRONG_SELL']),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def analyze_market(self):
        """Analyze all symbols and generate signals"""
        analysis = []
        for symbol in self.symbols:
            data = self.get_mock_data(symbol)
            analysis.append(data)
        return analysis

analyzer = TradingAnalyzer()

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/signals')
def get_signals():
    signals = analyzer.analyze_market()
    return jsonify(signals)

@app.route('/api/analysis/<symbol>')
def get_analysis(symbol):
    analysis = analyzer.get_mock_data(symbol.upper())
    return jsonify(analysis)

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
