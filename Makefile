BIN_NAME=nocodb-to-gpt-via-api
BIN_VERSION=0.1.1
BIN_DATE=$(shell date +%FT%T%z)

# Advisor Tooling @ Alaska SBDC

eligibility:
	uv run main.py

subscribe:
	echo "End users, who are small business advisors, want information on a daily basis."
	
publish:
	echo "This step will typically happen on an approx. ~3 month interval cadence."

update:
	echo "[OPS] Batch process data collection every week (via GitHub Actions)."
	
debug:
	ping aksbdc.org

local:
	llm -m llama3.2:latest 'What are the main jurisdictional funding sources in Alaska?'

test:
	cat data/response.json | llm -s "What loans do you have available for startups?"

# Aliases (a.k.a. shortened versions)

eli: eligibility
e: eligibility

sub: subscribe
s: subscribe

pub: publish
p: publish

up: update
u: update

de: debug
d: debug

loc: local
l: local

te: test
t: test
