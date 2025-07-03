# Code cleanup analysis

## Tools run
- `ruff check ferum_customs`
- `isort --check-only ferum_customs`
- `vulture ferum_customs --min-confidence 80 --exclude ferum_customs/tests`

## Results
- Ruff reported no unused imports or variables.
- isort confirmed import order is correct.
- vulture was not available in the environment, so dead code detection could not run.
