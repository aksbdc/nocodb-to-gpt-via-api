BIN_NAME=nocodb-to-gpt-via-api
BIN_VERSION=0.0.3
BIN_DATE=$(shell date +%FT%T%z)

# Advisor Tooling @ Alaska SBDC

eligibility:
	uv run main.py

publish:
	echo "This step will typically happen on an approx. ~3 month interval cadence."

subscribe:
	echo "End users, who are advisors, want information on a daily basis."

update:
	echo "[OPERATIONS] Batch process every week (via GitHub Actions)."
	
debug:
	ping aksbdc.org

test:
	pytest



