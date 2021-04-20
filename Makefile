tests:
	shellspec
	pytest --verbose

.PHONY: \
		check \
		clean \
		coverage \
		format \
		install \
		linter \
		mutants \
		tests

module = common_task_framework
codecov_token = 69abd834-7dd6-4667-8a12-42505381624d

define lint
	pylint \
        --disable=bad-continuation \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        ${1}
endef

check:
	black --check --line-length 100 ${module}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 tests

clean:
	rm --force --recursive ${module}.egg-info
	rm --force --recursive ${module}/__pycache__
	rm --force --recursive tests/__pycache__
	rm --force .mutmut-cache
	rm --force coverage.xml
	rm --force tests/example_submission.csv
	rm --force tests/test_data/example_submission.csv
	rm --force tests/test_data/test.csv
	rm --force tests/test_data/train.csv
	rm --force tests/test_data/XXexample_submission.csvXX
	rm --force tests/test_data/XXtest.csvXX
	rm --force tests/test_data/XXtrain.csvXX
	rm --force tests/test.csv
	rm --force tests/train.csv

coverage: install
	pytest --cov=${module} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}

format:
	black --line-length 100 ${module}
	black --line-length 100 tests

install:
	pip install --editable .

linter:
	$(call lint, ${module})
	$(call lint, tests)

mutants: install
	mutmut run --paths-to-mutate ${module} --runner "make tests"
