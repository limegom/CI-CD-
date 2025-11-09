# tests/conftest.py
import os
# 빈 값이면 로키 핸들러가 등록되지 않음
os.environ.setdefault("LOKI_ENDPOINT", "")