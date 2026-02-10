# Space Guardian Remake 🚀

HTML5 Canvas와 Phaser 3를 사용하여 제작된 **Space Guardian**의 리메이크 버전입니다.
고전적인 슈팅 게임의 재미에 성장 요소(상점, 업그레이드)와 현대적인 비주얼 이펙트를 더했습니다.

## 🎮 게임 특징

### 1. **향상된 비주얼 & 사운드**
- **Starfield 배경**: 다중 레이어 스크롤링으로 우주 공간의 깊이감을 구현했습니다.
- **사운드 이펙트**: 발사, 폭발, 아이템 획득 등 상황별 효과음이 적용되었습니다.
- **다양한 적**: 일반 운석뿐만 아니라 빠른 **Red Meteor**, 맷집이 강한 **Big Meteor**, 그리고 강력한 **Boss**가 등장합니다.

### 2. **성장 시스템 (Shop & Upgrade)**
- **Keys**: 게임 플레이 중 열쇠를 획득하여 화폐로 사용합니다. (브라우저 `localStorage`에 자동 저장)
- **Shop**: 메인 메뉴에서 상점을 이용할 수 있습니다.
    - **Damage Upgrade**: 탄환의 공격력을 강화하여 적을 더 빠르게 처치하세요.
    - **Duration Upgrade**: 든든한 아군 '가디언'의 소환 지속 시간을 늘리세요.

### 3. **다양한 아이템 & 스킬**
- **Shield**: 적의 공격을 한 번 막아주는 보호막을 생성합니다.
- **Rapid Fire**: 일정 시간 동안 공격 속도가 빨라집니다.
- **Guardian Summon**: Space Bar 또는 소환 버튼을 눌러 보조 기체를 소환합니다. (5 Keys 소모)

### 4. **모바일 최적화**
- **터치 컨트롤**: 화면 좌우 터치로 이동, 버튼 터치로 가디언을 소환할 수 있습니다.
- **반응형 UI**: 모바일 화면 비율에 맞춰 UI가 최적화되었습니다.

## 🕹️ 조작 방법

| 동작 | PC (Keyboard) | Mobile (Touch) |
|---|---|---|
| **이동** | 방향키 `←`, `→` | 화면 좌/우 터치 |
| **가디언 소환** | `Space Bar` | `SUMMON` 버튼 터치 |
| **상점/시작** | 마우스 클릭 | 화면 터치 |

## 🛠️ 기술 스택
- **Engine**: Phaser 3
- **Language**: JavaScript (ES6+)
- **Storage**: localStorage (데이터 영구 저장)

## 🚀 설치 및 실행
1. 저장소 클론: `git clone [Repository URL]`
2. `index.html` 파일을 웹 브라우저로 실행
3. 게임 즐기기!

## 🔄 최근 업데이트 (2026-02-10)
- **Asset Restoration**: 플레이어 기체 디자인을 오리지널 'Earth' 스타일로 복구했습니다.
- **Visual Improvements**: 모든 게임 에셋(플레이어, 적, 아이템 등)의 배경 투명도(Chroma Key) 처리를 완료하여 그래픽 품질을 개선했습니다.
- **Bug Fixes**:
    - **Rapid Fire**: 아이템 획득 시 공격 속도가 정상적으로 증가하도록 로직을 수정했습니다.
    - **HUD Bug**: 게임 오버 또는 재시작 시 점수 및 키 텍스트가 올바르게 초기화되도록 수정했습니다.
    - **Asset Injection**: 에셋 주입 스크립트를 개선하여 브라우저 호환성을 높였습니다.

## 🐛 Issue Tracker & Resovled Bugs
프로젝트 진행 중 발생한 주요 이슈와 해결 내역입니다.

- [x] **Asset Mismatch**: 플레이어 기체가 의도한 'Earth' 이미지가 아닌 다른 아이콘으로 출력되는 문제 방지 (Resolved)
- [x] **Transparency Issue**: 게임 내 모든 비트맵 이미지(플레이어, 적, 아이템)의 배경색(Magenta/Black)이 투명하게 처리되지 않던 문제 해결 (Resolved via `processChromaKey`)
- [x] **Rapid Fire Bug**: 'Rapid Fire' 아이템 습득 시 발사 속도가 빨라지지 않던 로직 오류 수정 (Resolved)
- [x] **Runtime Error**: 게임 오버/재시작 시 `scoreText` 초기화 누락으로 인한 콘솔 에러 수정 (Resolved)
- [x] **Browser Compatibility**: `innerHTML`을 사용한 스크립트 주입 시 브라우저 멈춤 현상 해결 (Resolved via `createElement('script')`)
- [ ] **Code Refactoring**: 단일 `index.html` 파일에 모든 로직이 포함되어 있어 유지보수가 어려움. 모듈 분리 필요 (Backlog)
- [ ] **Mobile Optimization**: 모바일 터치 조작감 개선 및 가로 모드 강제 지원 필요 (Backlog)

---
*이 게임은 제4회 인디사이드 게임대회 출품작을 리메이크한 프로젝트입니다.*
