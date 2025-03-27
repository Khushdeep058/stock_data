from flask import Flask, jsonify
import pandas as pd
from strategy_service import load_data, generate_signals

app = Flask(__name__)


file_path = "HINDALCO_1D.xlsx"
df = load_data(file_path)

@app.route('/strategy/performance', methods=['GET'])
def strategy_performance():
    results = generate_signals(df.copy())
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
