# [Space Guardian #1] AI와 짝코딩으로 죽은 게임 심폐소생술하기 (Vibe Coding)

안녕하세요! 이번 시리즈에서는 제4회 인디사이드 게임대회 출품작이었던 **Space Guardian**을, 최신 웹 기술(Phaser 3)과 **AI 코딩 어시스턴트(Antigravity)**를 활용해 리메이크한 과정을 공유하려 합니다.

특히 이번 프로젝트는 **"Vibe Coding"** 방식으로 진행되었습니다. 제가 기획 의도와 원하는 "느낌(Vibe)"을 말하면, AI가 이를 구체적인 코드로 구현해주는 방식이죠. 개발 속도가 얼마나 빨라졌는지, 그리고 어떤 프롬프트를 사용했는지 자세히 공개합니다.

## 1. 프로젝트 목표
- **Legacy 청산**: 오래된 코드 구조를 최신 엔진(Phaser 3) 기반으로 리팩토링
- **Fun 요소 추가**: 단순 슈팅을 넘어선 성장(상점) 및 비주얼 업그레이드
- **멀티 플랫폼**: PC와 모바일 어디서든 즐길 수 있도록 반응형 웹으로 제작

## 2. 초기 환경 설정 및 분석
가장 먼저 레거시 프로젝트의 구조를 파악하고, 필요한 에셋을 관리하기 쉽게 만드는 작업부터 시작했습니다.

### 🤖 Vibe Coding Prompt #1
> "현재 프로젝트 폴더(`space_guardian`)를 분석해주고, 리메이크를 위한 작업 목록(`task.md`)을 작성해줘. 우선순위는 '게임 루프 복원' -> '비주얼 개선' -> '콘텐츠 확장' 순서야."

AI는 즉시 `task.md`를 생성하여 체계적인 개발 로드맵을 제안해 주었습니다. 덕분에 개발 중간에 길을 잃지 않을 수 있었죠.

### 🤖 Vibe Coding Prompt #2
> "기존 `index.html`에 하드코딩된 Base64 이미지들이 너무 길어서 코드를 읽기가 힘들어. 이걸 별도의 파이썬 스크립트(`inject_assets.py`)로 관리하거나 분리하는 방법을 제안해줘."

이 요청을 통해 코드의 가독성이 획기적으로 좋아졌습니다. 에셋 주입 로직이 자동화되어, 저는 오로지 게임 로직에만 집중할 수 있게 되었습니다.

## 3. 첫 결과물
단 10분 만에 플레이 가능한 프로토타입이 완성되었습니다.

**(Before: 2017년 원작)**
![Original Game Title](https://postfiles.pstatic.net/MjAxNzEyMDZfODYg/MDAxNTEyNTU5OTE1ODI3.Hz0cU38Gx_lAWXJ6wjy1Lcovo_wv8sdBsMqAeXIUP7Qg.PojAsMMHt4V6nIjl1haQc5PvrcHg9QmCSN1wxhT0FVEg.JPEG.gpejddk/image_6982089981512559173253.jpg)

**(After: 2026년 리메이크)**
![Remake Menu](/Users/muaco/.gemini/antigravity/brain/104825de-5f95-4705-8e36-dcd59b673877/screenshot_menu_1770194548294.png)

다음 편에서는 밋밋한 우주 배경을 **화려한 Starfield**로 바꾸고, 타격감을 더해주는 **사운드 효과**를 적용한 과정을 다룹니다.

---
**[Space Guardian 리메이크 시리즈]**
1. **AI와 짝코딩으로 죽은 게임 심폐소생술하기** 👈
2. 밋밋한 우주에 생기를! 비주얼 & 사운드 이펙트 대수술
3. 게임의 재미는 '성장'에서 온다: 상점과 데이터 저장
4. PC 게임을 모바일 앱처럼? 터치 컨트롤과 반응형 UI 최적화
5. 프로젝트 배포와 회고: AI가 코딩의 미래일까?
