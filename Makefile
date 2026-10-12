.PHONY: check
check:
	python3 scripts/check_package.py
	PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py'
	node --experimental-strip-types --test tests/test_waiting.mjs
	git diff --check
