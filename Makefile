BIN_NAME=nocodb-to-gpt-via-api
BIN_VERSION=0.1.1
BIN_DATE=$(shell date +%FT%T%z)

# Advisor Tooling @ Alaska SBDC

eligibility:
	uv run main.py

subscribe:
	echo "End users, who are advisors, want information on a daily basis."
	
publish:
	echo "This step will typically happen on an approx. ~3 month interval cadence."

update:
	echo "[OPERATIONS] Batch process every week (via GitHub Actions)."
	
debug:
	ping aksbdc.org

local:
	llm -m llama3.2:latest 'What are the main jurisdictional funding sources in Alaska?'

test:
	cat data/response.json | llm -s "What loans do you have available for startups?"
