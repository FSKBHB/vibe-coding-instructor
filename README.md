# Vibe Coding Instructor — Landing Page

AI Vibe Coding 강사 소개 페이지의 **3가지 디자인 시안**을 비교·선택할 수 있는 FastAPI 웹 애플리케이션입니다.

---

## 디자인 시안

| 시안 | 스타일 | 특징 |
|------|--------|------|
| **Design A** | Editorial Luxury | 딥 네이비 + 골드 포인트, 권위 있는 학술적 분위기 |
| **Design B** | Intimate Split-Panel | 스티키 사이드바, 1:1 코칭 분위기의 따뜻한 레이아웃 |
| **Design C** | Bold Dashboard / Bento Grid | 베토 카드 그리드, 모던 SaaS 감성의 대담한 레이아웃 |

---

## 기술 스택

| 항목 | 기술 |
|------|------|
| Language | Python 3.11+ |
| Package Manager | [uv](https://github.com/astral-sh/uv) |
| Web Framework | FastAPI |
| ASGI Server | Uvicorn |
| Template Engine | Jinja2 |
| Data Storage | JSON 파일 (DB 미사용) |

---

## 시작하기

### 1. 의존성 설치

```bash
uv sync
```

### 2. 개발 서버 실행

```bash
uv run uvicorn src.main:app --reload --port 8000
```

### 3. 브라우저에서 확인

| URL | 설명 |
|-----|------|
| `http://localhost:8000/` | 디자인 선택 페이지 |
| `http://localhost:8000/design-a` | Design A — Editorial Luxury |
| `http://localhost:8000/design-b` | Design B — Intimate Split-Panel |
| `http://localhost:8000/design-c` | Design C — Bold Dashboard |

---

## 프로젝트 구조

```
vibe-coding-instructor/
├── src/
│   ├── main.py              # FastAPI 앱 엔트리포인트
│   ├── api/                 # API 라우터 (확장용)
│   ├── templates/
│   │   ├── base.html        # 베이스 템플릿
│   │   ├── index.html       # 디자인 선택 페이지
│   │   └── pages/
│   │       ├── design_a.html
│   │       ├── design_b.html
│   │       └── design_c.html
│   └── static/
│       └── css/
│           ├── design_a.css
│           ├── design_b.css
│           └── design_c.css
├── pyproject.toml
├── uv.lock
└── CLAUDE.md
```

---

## 개발 명령어

```bash
# 린팅
uv run ruff check src/

# 포맷팅
uv run ruff format src/

# 테스트
uv run pytest
```

---

## 라이선스

MIT
