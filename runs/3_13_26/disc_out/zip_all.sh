for d in */; do tar -czf "${d%/}.tar.gz" "$d"; done &
