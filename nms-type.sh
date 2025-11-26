#!/bin/bash
echo Enter a command:
read command
$command > nms.tmp
clear
while IFS= read -r line; do
    printf '%s\n' "$line" | nms -a
done < nms.tmp
rm nms.tmp