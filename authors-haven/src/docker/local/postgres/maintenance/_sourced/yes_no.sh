#!/usr/bin/env bash

yes_no(){
    declare desc="Prompt for confirmation. \$\"\{1\}\": confirmation message"
    local arg1="${1}"
    local response= read -r -p "${arg1} [y/N]? " response

    if [[ "${response}" =~ ^([yY][eE][sS]|[yY])$ ]];
    then
        exit 0
    else
        return 1
    fi
}