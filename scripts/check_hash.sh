#!/bin/bash
set -e

VERIFICATION_HASH="VERIFICACAO: 9b12b6f7-4c91-421e-b5a5-ef1a14"

FILES_TO_CHECK=(
  "README.md"
  "backend/core/models.py"
  "frontend/src/App.vue"
  "backend/core/tests/test_ingest.py"
)

missing_in=()

echo "Checking for verification hash '${VERIFICATION_HASH}'..."

for file in "${FILES_TO_CHECK[@]}"; do
  if [ -f "$file" ]; then
    if grep -qF "$VERIFICATION_HASH" "$file"; then
      echo "OK: Found hash in $file"
    else
      echo "ERROR: Hash NOT FOUND in $file"
      missing_in+=("$file")
    fi
  else
    echo "ERROR: File not found: $file"
    missing_in+=("$file (not found)")
  fi
done

if [ ${#missing_in[@]} -ne 0 ]; then
  echo "Hash check FAILED. Missing in: ${missing_in[*]}"
  exit 1
fi

echo "Verification hash check PASSED."
exit 0 