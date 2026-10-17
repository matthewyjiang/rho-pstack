#!/usr/bin/env bash
# Append a well-formed row to a show-me-your-work decision log (TSV).
# Usage: log.sh <logfile> <phase> <decision> <why> <evidence> <result>
set -euo pipefail

if [ "$#" -ne 6 ]; then
	printf 'usage: log.sh <logfile> <phase> <decision> <why> <evidence> <result>\n' >&2
	exit 1
fi

logfile="$1"
shift

logdir="$(dirname "$logfile")"
if [ -n "$logdir" ] && [ "$logdir" != "." ] && [ ! -d "$logdir" ]; then
	mkdir -p "$logdir"
fi

# Use `>>` here, never `>`. A network mount can fail this test for a log
# that exists. Then the cost is one stray header line, not the rows.
if [ ! -s "$logfile" ]; then
	printf 'ts\tphase\tdecision\twhy\tevidence\tresult\n' >> "$logfile"
fi

ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
# Keep cells single-line, neutralize spreadsheet formulas (including after
# whitespace), and quote/escape TSV fields so a reader cannot reinterpret
# user-supplied double quotes as delimiters and expose a hidden formula.
clean() {
	local v leading_trimmed
	v=$(printf '%s' "$1" | tr '\t\n\r' '   ')
	leading_trimmed="${v#"${v%%[![:space:]]*}"}"
	case "$leading_trimmed" in
		=*|+*|-*|@*) v="'$v" ;;
	esac
	v="${v//\"/\"\"}"
	printf '"%s"' "$v"
}
printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
	"$ts" "$(clean "$1")" "$(clean "$2")" "$(clean "$3")" "$(clean "$4")" "$(clean "$5")" \
	>> "$logfile"
