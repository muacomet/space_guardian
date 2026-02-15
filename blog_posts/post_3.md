# [Space Guardian #3] 게임의 재미는 '성장'에서 온다: 상점과 데이터 저장

아무리 재미있는 게임도 보상이 없으면 금방 질리기 마련입니다. 플레이어가 계속 게임을 즐길 동기를 부여하기 위해 **재화(Key) 수집**과 **능력치 업그레이드(Shop)** 시스템을 도입했습니다.

## 1. Shop Scene 구현
기존의 `Intro` -> `Game` 흐름 사이에 `Menu`와 `Shop` 씬을 추가하여 게임의 볼륨을 키웠습니다.

### 🤖 Vibe Coding Prompt
> "**상점(ShopScene)을 만들어줘.** 인트로 화면에 [SHOP] 버튼을 추가하고, 누르면 상점으로 이동하게 해. 상점에서는 **공격력(Damage)**과 **가디언 지속시간(Duration)**을 업그레이드할 수 있어야 해."

AI는 Phaser의 `Scene` 클래스를 상속받아 `ShopScene`을 뚝딱 만들어냈습니다. UI 구성부터 버튼 이벤트 처리까지 한 번에 구현되었죠.

![Shop Interface](/Users/muaco/.gemini/antigravity/brain/104825de-5f95-4705-8e36-dcd59b673877/screenshot_shop_1770195202999.png)

## 2. 데이터 영구 저장 (localStorage)
웹 게임의 단점은 '새로고침하면 데이터가 날아간다'는 점입니다. 이를 해결하기 위해 브라우저의 `localStorage`를 활용했습니다.

### 🤖 Vibe Coding Prompt
> "열심히 모은 열쇠(Keys)와 업그레이드 레벨이 사라지지 않게 **localStorage에 저장하고 싶어.** 게임 시작 시(`create`) 데이터를 불러오고, 게임 오버 시(`hitMeteor`) 데이터를 저장하도록 로직을 수정해줘."

이제 플레이어는 브라우저를 껐다 켜도 자신의 강화 상태를 그대로 유지할 수 있습니다.

```javascript
// 데이터 로드 예시
this.keys = parseInt(localStorage.getItem('sg_keys') || '0');
this.damageLevel = parseInt(localStorage.getItem('sg_damage_level') || '1');
```

## 3. 성장 체감 설계
업그레이드를 하면 확실히 강해졌다는 느낌을 주어야 합니다.
- **Damage**: 1 -> 2 -> 3 (강한 운석도 한 방!)
- **Duration**: 5초 -> 6초 -> 7초 (가디언이 더 오래 지원사격!)

이러한 수치 밸런싱도 AI에게 초기 값을 제안받고, 테스트하며 조정해 나갔습니다.

다음 편에서는 PC뿐만 아니라 지하철에서도 즐길 수 있도록 **모바일 터치 컨트롤**을 구현한 이야기를 들려드립니다.

---
**[Space Guardian 리메이크 시리즈]**
1. AI와 짝코딩으로 죽은 게임 심폐소생술하기
2. 밋밋한 우주에 생기를! 비주얼 & 사운드 이펙트 대수술
3. **게임의 재미는 '성장'에서 온다: 상점과 데이터 저장** 👈
4. PC 게임을 모바일 앱처럼? 터치 컨트롤과 반응형 UI 최적화
5. 프로젝트 배포와 회고: AI가 코딩의 미래일까?
