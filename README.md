# Space Guardian Remake (Earth Edition) 🌍🚀

HTML5 Canvas와 Phaser 3를 사용하여 제작된 **Space Guardian**의 리메이크 버전입니다.
지구를 직접 조종하여 우주의 위협으로부터 살아남으세요!

## 🎮 게임 특징

### 1. **새로운 플레이어: 지구 (Earth)**
- **Earth Player**: 기존의 우주선 대신 **지구**가 플레이어 캐릭터가 됩니다.
- **Refined Hitbox**: 지구의 원형 형태에 맞춘 정교한 충돌 박스를 적용하여 더욱 직관적인 플레이가 가능합니다.

### 2. **향상된 가디언 (Guardian)**
- **Invincibility**: 가디언 소환 시 **3초간 무적** 상태가 되며, 반짝이는 효과로 상태를 확인할 수 있습니다.
- **Collision Attack**: 무적 상태에서 운석과 충돌하면 가디언은 파괴되지 않고 **운석만 파괴**됩니다. 위기 상황에서 적극적으로 활용하세요!
- **Guardian Summon**: Space Bar 또는 소환 버튼을 눌러 보조 기체를 소환합니다. (5 Keys 소모)

### 3. **다양한 아이템 & 스킬**
- **Shield**: 적의 공격을 한 번 막아주는 보호막을 생성합니다.
- **Rapid Fire**: 일정 시간 동안 공격 속도가 빨라집니다.
- **Double Shot**: 탄환이 2발씩 발사됩니다.
- **Magnet**: 주변의 아이템을 자동으로 끌어당깁니다.
- **Bomb (Red Key)**: 화면 내의 모든 적(Meteor)을 파괴하고 보스에게 큰 데미지를 입힙니다.

### 4. **성장 시스템 (Shop & Upgrade)**
- **Keys**: 게임 플레이 중 열쇠를 획득하여 화폐로 사용합니다. (브라우저 `localStorage`에 자동 저장)
- **Shop**: 메인 메뉴에서 상점을 이용할 수 있습니다.
    - **Damage Upgrade**: 탄환의 공격력을 강화하여 적을 더 빠르게 처치하세요.
    - **Duration Upgrade**: 든든한 아군 '가디언'의 소환 지속 시간을 늘리세요.

## 🕹️ 조작 방법

| 동작 | PC (Keyboard) | Mobile (Touch) |
|---|---|---|
| **이동** | 방향키 `←`, `→` | 화면 좌/우 터치 |
| **가디언 소환** | `Space Bar` | `SUMMON` 버튼 터치 |
| **일시정지** | `ESC`, `P` | - |
| **상점/시작** | 마우스 클릭 | 화면 터치 |

## 🛠️ 기술 스택
- **Engine**: Phaser 3
- **Language**: JavaScript (ES6+)
- **Storage**: localStorage (데이터 영구 저장)

## 🚀 설치 및 실행
1. 저장소 클론: `git clone [Repository URL]`
2. `index.html` 파일을 웹 브라우저로 실행
3. 게임 즐기기!

## 🔄 최근 업데이트 (2026-02-15)
- **Earth as Player**: 플레이어 캐릭터를 지구로 변경하고 충돌 박스를 최적화했습니다.
- **Guardian Invincibility**: 가디언 소환 시 3초 무적 및 충돌 공격 기능을 추가했습니다.
- **Item Balance**: 아이템 생성 주기 및 확률을 조정하여 게임 템포를 개선했습니다.
- **Bug Fixes**:
    - **Screenshot**: 스크린샷 캡처 시 화면이 검게 나오는 오류를 수정했습니다.
    - **Premature Game Over**: 지구와 운석의 충돌 판정 범위를 수정하여 불합리한 게임 오버를 방지했습니다.

## 🐛 Issue Tracker & Resolved Bugs
프로젝트 진행 중 발생한 주요 이슈와 해결 내역입니다.

- [x] **Asset Mismatch**: 플레이어 기체 오류 수정 (Resolved)
- [x] **Transparency Issue**: 배경 투명도(Chroma Key) 처리 (Resolved)
- [x] **Rapid Fire Bug**: 공속 증가 로직 수정 (Resolved)
- [x] **Item Spawn Issue**: 아이템 생성 타이머 미작동 및 0.5초 단축 (Resolved)
- [x] **Bomb Item Crash**: 폭탄 이펙트 미초기화로 인한 멈춤 현상 수정 (Resolved)
- [x] **Black Screenshot**: 캔버스 설정 변경으로 스크린샷 오류 수정 (Resolved)
- [x] **Premature Game Over**: 지구 충돌 박스 축소로 해결 (Resolved)
- [x] **Guardian Vulnerability**: 소환 직후 무적 시간 추가로 해결 (Resolved)

---
*이 게임은 제4회 인디사이드 게임대회 출품작을 리메이크한 프로젝트입니다.*
