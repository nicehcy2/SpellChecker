from django.shortcuts import render, redirect
from urllib.parse import quote
import requests
import json

# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'main/index.html')

def wrongTocorrect(input_text, corrections):
    corrected_text = input_text

    for correction in corrections:
        org_str = correction.get('orgStr', '')
        cand_word = correction.get('candWord', '')

        if org_str and cand_word:
            corrected_text = corrected_text.replace(org_str, cand_word)

    return corrected_text

def spellcheck(request):
    result_text = ""
    error_count = 0

    if request.method == 'POST':
        try:
            input_text = request.POST.get('input_text', '')
            response = requests.post('http://164.125.7.61/speller/results', data={'text1': input_text})

            # 3. 응답에서 필요한 내용 추출 (html 파싱)
            data_start = response.text.find('data = [')
            data_end = response.text.rfind('];', data_start)
            if data_start != -1 and data_end != -1:
                data = response.text[data_start + len('data = ['):data_end]
            
                # 4. 파이썬 딕셔너리 형식으로 변환
                data = json.loads(data)
                if 'errInfo' in data:
                    input_text = wrongTocorrect(input_text, data['errInfo'])
                    for err in data['errInfo']:
                        result_text += f"입력 내용 : {err['orgStr']}\n"
                        result_text += f"대치어 : {err['candWord']}\n"
                        result_text += f"도움말 : {err['help']}\n\n"
                else:
                    result_text = "맞춤법 오류 정보가 없습니다."
            else:
                result_text = "맞춤법 오류 정보가 없습니다."
        except requests.RequestException as e:
            print(f"오류 발생: {e}")
        except json.JSONDecodeError as e:
            print(f"JSON 디코딩 오류: {e}")
        except Exception as e:
            print(f"알 수 없는 오류: {e}")
        return redirect('main:result_page', input_text = input_text, result_text=result_text, error_count=error_count)

    return render(request, 'main/index.html')

def result_page(request, input_text, result_text, error_count):
    return render(request, 'main/result.html', {'input_text': input_text, 'result_text': result_text, 'error_count': error_count})