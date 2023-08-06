@echo off
mypy --strict zxgraphs
pylint zxgraphs
python -m readme_renderer README.rst -o README-PROOF.html
pytest test --cov=./zxgraphs
coverage html
@pause
