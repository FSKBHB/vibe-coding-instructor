import sys
from pathlib import Path

# Vercel 서버리스 환경에서 src 모듈을 찾을 수 있도록 경로 추가
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.main import app  # noqa: F401, E402
