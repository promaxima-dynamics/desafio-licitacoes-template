#!/bin/bash
set -e

# Argumentos: 1=Branch atual, 2=Branch base (ex: develop main)
CURRENT_BRANCH=${1:-develop}
BASE_BRANCH=${2:-main}

# Commits obrigatórios definidos no README
# IMPORTANTE: Mantenha sincronizado com o README.md!
REQUIRED_PREFIXES=(
  "feat(models):"
  "feat(ingest):"
  "feat(api):"
  "feat(ui):"
  "feat(export):"
  # "refactor:" ou "test:" são opcionais para o último, verificamos pelo menos um
)
REFACTOR_OR_TEST_PREFIXES=("refactor:" "test:")

echo "Checking required commit prefixes on branch '${CURRENT_BRANCH}' against '${BASE_BRANCH}'..."

# Lista commits na branch atual que não estão na base
# Usa --no-merges para ignorar merges que podem poluir
COMMIT_LOG=$(git log --no-merges --pretty=format:"%s" ${BASE_BRANCH}..${CURRENT_BRANCH})

if [ -z "$COMMIT_LOG" ]; then
  echo "WARNING: No commits found between ${BASE_BRANCH} and ${CURRENT_BRANCH}. Skipping check."
  # Decide if this should be an error or just a warning depending on the flow
  # exit 1
  exit 0
fi

missing_prefixes=()
found_refactor_or_test=false

# Checa prefixos obrigatórios
for prefix in "${REQUIRED_PREFIXES[@]}"; do
  if ! echo "$COMMIT_LOG" | grep -qF "$prefix"; then
    missing_prefixes+=("$prefix")
  else
    echo "OK: Found commit with prefix '$prefix'"
  fi
done

# Checa se pelo menos um de refactor/test existe
for prefix in "${REFACTOR_OR_TEST_PREFIXES[@]}"; do
  if echo "$COMMIT_LOG" | grep -qF "$prefix"; then
    echo "OK: Found commit with prefix '$prefix'"
    found_refactor_or_test=true
    break
  fi
done

if ! $found_refactor_or_test; then
  rt_prefixes=$(IFS=, ; echo "${REFACTOR_OR_TEST_PREFIXES[*]}")
  missing_prefixes+=("one of [${rt_prefixes}]")
  echo "ERROR: Missing commit with prefix 'refactor:' or 'test:'"
fi


if [ ${#missing_prefixes[@]} -ne 0 ]; then
  echo "Commit check FAILED. Missing prefixes: ${missing_prefixes[*]}"
  exit 1
fi

echo "Required commit prefixes check PASSED."
exit 0 