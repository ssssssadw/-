from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/linear-search', methods=['POST'])
def linear_search_api():
    """
    클라이언트로부터 배열(array)과 찾을 값(target)을 전달받아
    선형 검색(Linear Search)을 수행하고, 단계별 탐색 과정과 시간 복잡도를 JSON으로 반환하는 API
    """
    try:
        # 클라이언트 요청 데이터 파싱 (기본값 설정)
        req_data = request.get_json() or {}
        arr = req_data.get('array', [10, 25, 3, 42, 18, 7])
        target = req_data.get('target', 42)
        
        steps = []
        found_index = -1
        
        # 선형 검색 알고리즘 수행 (O(N) 시간 복잡도)
        for i in range(len(arr)):
            current_value = arr[i]
            is_match = (current_value == target)
            
            # 각 단계별 탐색 상태를 기록
            steps.append({
                "index": i,
                "value": current_value,
                "checked": True,
                "matched": is_match
            })
            
            # 값을 찾았을 경우 검색 중단
            if is_match:
                found_index = i
                break
                
        # 서버 응답 데이터 구성
        response_data = {
            "status": "정상 동작 중 (Running)",
            "complexity": "시간 복잡도: O(N) (선형 탐색)",
            "target": target,
            "foundIndex": found_index,
            "steps": steps
        }
        
        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Cloud Run에서 할당하는 PORT 환경 변수를 사용하며, 기본값은 8080
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
