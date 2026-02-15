# [Space Guardian #2] 밋밋한 우주에 생기를! 비주얼 & 사운드 이펙트 대수술

단순한 검은 화면에 흰 점 몇 개... 초기 버전의 우주는 너무나 적막했습니다. 이번 편에서는 게임의 몰입감을 높여줄 **Starfield(별 배경)**와 **사운드 효과**를 적용한 과정을 소개합니다.

## 1. 우주를 더 깊게: Parallax Starfield 구현
정적인 배경 대신, 플레이어의 움직임이나 시간에 따라 흐르는 별 배경을 만들고 싶었습니다. 특히 원근감(Parallax)을 주기 위해 3개의 레이어로 별을 구성했습니다.

### 🤖 Vibe Coding Prompt
> "**지루한 검은 배경 대신, 뒤로 흘러가는 별 배경(Starfield)을 추가하고 싶어.** 원근감을 위해 3개의 레이어(원경, 중경, 근경)로 나누고 속도를 다르게 설정해줘. 게임이 멈추면 배경도 멈쳐야 해."

AI가 작성해준 `Starfield` 클래스는 `Phaser.GameObjects.Graphics`를 활용해 수백 개의 별을 효율적으로 그려냈습니다. `update()` 문에서 각 레이어의 속도를 다르게 조절하는 코드가 핵심이었죠.

```javascript
// AI가 작성한 코드 일부
createLayer(count, speed, color) {
    for (let i = 0; i < count; i++) {
        const star = this.scene.add.rectangle(x, y, 2, 2, color).setDepth(-10);
        star.speed = speed;
        this.stars.push(star);
    }
}
```

## 2. 귀를 즐겁게: 사운드 시스템 추가
게임의 타격감은 소리가 80%를 차지한다고 해도 과언이 아닙니다. 외부 파일 로딩 없이 단일 HTML 파일로 구동되길 원했기에, 사운드 파일도 Base64로 인코딩하여 포함시켰습니다.

### 🤖 Vibe Coding Prompt
> "**효과음(발사, 폭발, 아이템 획득)을 추가해줘.** 에셋은 Base64 문자열로 코드 내에 포함시키고, `AudioContext`나 Phaser의 사운드 매니저를 통해 재생되도록 구현해."

## 3. 적 다양화 (Enemy Variety)
단조로움을 피하기 위해 적의 패턴도 다양화했습니다.
- **Red Meteor**: 작고 빠르며 점수가 높음
- **Big Meteor**: 느리지만 체력이 높아 2번 맞춰야 함

### 🤖 Vibe Coding Prompt
> "적의 종류를 늘리고 싶어. **빠르게 떨어지는 붉은 운석**과 **체력이 높은 거대 운석**을 추가하고, 각각 다른 점수와 속도를 부여해줘."

결과적으로 화면은 훨씬 다채로워졌고, 플레이어는 상황에 맞춰 전략적으로 움직여야 하는 재미가 생겼습니다.

**(Before: 단조로운 배경)**
![Original Gameplay](https://postfiles.pstatic.net/MjAxNzEyMTNfMTYy/MDAxNTEzMTYzOTk5MzIw.CmR8HHMxWFg0L9TFS5TkahFt1ligQV2UzQ3B3KGixisg.flIBrlCP3ho0a-0MODYWCjoLzocbBHFuipjVVNNlwS8g.JPEG.gpejddk/1.jpg)

**(After: Parallax Starfield 적용)**
![Remake Gameplay](/Users/muaco/.gemini/antigravity/brain/104825de-5f95-4705-8e36-dcd59b673877/screenshot_gameplay_countdown_1770195543281.png)

---
**[Space Guardian 리메이크 시리즈]**
1. AI와 짝코딩으로 죽은 게임 심폐소생술하기
2. **밋밋한 우주에 생기를! 비주얼 & 사운드 이펙트 대수술** 👈
3. 게임의 재미는 '성장'에서 온다: 상점과 데이터 저장
4. PC 게임을 모바일 앱처럼? 터치 컨트롤과 반응형 UI 최적화
5. 프로젝트 배포와 회고: AI가 코딩의 미래일까?
