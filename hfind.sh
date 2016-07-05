echo '#include <'"$1"'>' | cpp -H -o /dev/null 2>&1 | head -n1 | sed 's/^\. //g'
