#!/usr/bin/env bash

countdown(){
    declare desc="Countdown timer. \$\"\{1\}\": time in seconds"
    local arg1="${1}"
    local i="${arg1}"
    while [[ "${i}" -gt 0 ]];
    do
        echo -ne "Time remaining: ${i} seconds\033[0K\r"
        sleep 1
        i=$((i-1))
    done
    echo -e "Time remaining: 0 seconds\033[0K\r"
}