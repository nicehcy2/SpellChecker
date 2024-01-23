# SpellChecker

<br/>

![image](https://github.com/nicehcy2/SpellChecker/assets/105339362/8644d1d8-84e3-474b-9daa-d4ad316944e9)

## 1. 개요

<br/>

사용자가 입력한 텍스트나 파일을 읽어 맞춤법과 글자수를 검사하는 페이지이다. <br/><br/>

## 2. 문제 정의와 과제의 필요성 

<br/>

최근에 자기소개서를 작성하는 일이 매우 많았다. 자소서 초안을 작성하고 맞춤법을 검사하기 위해 맞춤법 검사 사이트를 찾았는데 글자수 제한이 있고 광고도 매우 많았다. 그리고 돈을 지불해야 되는 경우도 있었고 무료 버전일 경우 디자인 요소가 사용하기 좋지도 않았다. 그래서 내가 직접 페이지를 제작하여 글자수 제한도 없고 무료로 자소서 맞춤법 검사와 글자수를 검사 받고 싶다. 

**파이썬 기초 프로그래밍 수업 과제이며 django를 사용해보기 위해 이 웹 페이지를 제작했다.** (README 역시 과제 보고서 위주로 작성되었다.) <br/><br/>

## 3. 개발 개요

<br/>

웹 어플리케이션은 Django를 사용하여 개발할 것이다. 우선은 AWS를 사용하여 직접 서버 개발을 하지 않고 로컬(127.0.0.1)에서만 실행될 수 있도록 할 것이다. 그리고 맞춤법, 글자수 확인 기능은 pyhunspell 라이브러리를 사용하여 구현할 것이다. HunSpell()을 호출해서 HunSpell 객체를 생성하고 spell() 함수를 호출하여 맞춤법 오류가 있는 단어를 찾아 집합 단위로 저장한다. 그리고 suggest() 함수를 호출하여 맞춤법 오류가 있는 단어를 올바르게 수정한 뒤 저장한다. 이러한 방식으로 맞춤법 검사 페이지를 구현해볼 것이다. <br/><br/>

## 4. 개발 내용

<br/>

**Spell Checker 웹 어플리케이션 구성**: Django 웹 프레임워크와 Bootstrap을 사용하여 Spell Checker 기능을 제공하는 웹 어플리케이션을 개발하였습니다. 사용자는 웹 페이지에서 텍스트를 입력하고, 맞춤법을 검사하는 기능을 사용할 수 있습니다.

![image](https://github.com/nicehcy2/SpellChecker/assets/105339362/2892045e-fcc1-4346-995f-2a84ca1ec12f)

Django로 구현한 핵심적인 기능을 설명하면 urls.py에서 urlpatterns를 정의하여 URL 패턴을 정의했습니다. 빈 문자열(‘’)은 기본 URL이며, main.urls로 라우팅됩니다. Main.urls는 main 애플리케이션 내에 있는 URL 패턴을 정의한 파일입니다.

![image](https://github.com/nicehcy2/SpellChecker/assets/105339362/e1410f79-9a74-43f3-a2e3-2e965d3b83cd)

위의 코드는 Django에서 URL을 처리하기 위한 main 애플리케이션의 urls.py 파일입니다. Urlpatterns로 기본 URL로 들어온 요청은 spellcheck 뷰 함수에 연결합니다. <br/><br/>

**서버와의 통신**: 사용자가 입력한 텍스트를 서버(로컬 서버)로 전송하고, 서버에서는 외부 API를 이용하여 맞춤법 검사를 수행합니다. 서버는 API의 응답을 받아와서 웹 페이지에 결과를 표시합니다.

![image](https://github.com/nicehcy2/SpellChecker/assets/105339362/5edd040c-6fcd-406f-a17f-ff714154aed5)

오류를 고쳐 올바른 text로 출력하는 함수입니다.

![image](https://github.com/nicehcy2/SpellChecker/assets/105339362/0f9a3aee-cded-46d3-bac9-bcb88ab0b4bd)

맞춤법을 교정하는 코드입니다. Index.html에서 구현한 버튼을 누르면 POST 요청이 들어오고 해당 form에 있던 데이터를 읽어 input_text에 string 형태로 저장합니다. 그리고 부산대 맞춤법 검사기 서버에 POST 방식으로 input_text 데이터를 보냅니다. 서버에서 클라이언트로 보낸 응답 텍스트를 파싱하여 JSON 형식으로 변환합니다. 그리고 JSON 형식의 데이터를 딕셔너리 형식으로 변환하여 data에 저장합니다. 오류 정보가 있으면 data에 정보가 있기 때문에 문제가 된 부분들을 wrongTocorrect() 함수로 올바르게 수정하고 해설을 result_text에 저장합니다. 만약 오류가 없으면 기본 설정 텍스트를 출력하도록 합니다. 

![image](https://github.com/nicehcy2/SpellChecker/assets/105339362/f647eac3-2c59-4b64-8155-dca664be9742)

POST 요청이 있어 코드가 정상적으로 작동하면 result.html에 정보를 보내면서 렌더링 시킵니다. POST 요청이 아닌 GET 요청(로컬 서버에 접속하는 경우)일 경우 index.html을 렌더링 시킵니다. 
(글자수 세기와 버튼 기능 등은 html로 구현했기에 생략하겠습니다.) <br/><br/>

## 5. 결과

<br/>

- 사용자는 웹 페이지를 통해 텍스트를 입력하고 맞춤법을 간편하게 검사할 수 있습니다.
- 맞춤법 오류가 발견되면 해당 부분이 강조되어 표시되며, 대치어와 도움말을 통해 오류를 이해하고 수정할 수 있습니다.
- 수정된 텍스트를 얻어 원본 텍스트를 교정할 수 있습니다.

![image](https://github.com/nicehcy2/SpellChecker/assets/105339362/273c0b51-43db-4c06-ad49-13fbded5690a)

index.html

<br/>

![image](https://github.com/nicehcy2/SpellChecker/assets/105339362/5cb48bab-d24c-4a0c-9acf-c5299aa3303d)

result.html
