from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/linear-search', methods=['POST'])
def linear_search():
    data = request.json
    arr = data.get('array', [10, 23, 5, 12, 44, 3])
    target = data.get('target', 12)
    
    steps = []
    found_index = -1
    
    # 선형 검색 수행 및 단계별 기록 (자세한 주석 포함)
    for i in range(len(arr)):
        steps.append({"index": i, "value": arr[i], "checked": True})
        if arr[i] == target:
            found_index = i
            break
            
    return jsonify({
        "status": "success",
        "complexity": "O(N)",
        "target": target,
        "foundIndex": found_index,
        "steps": steps
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
