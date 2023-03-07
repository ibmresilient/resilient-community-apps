#!/bin/sh
# syntax: bash ./capture_extract_data.sh "Generic email script (App Exchange v2.3.2)" "Process email message v2.3.2"
resilient-sdk extract --script "$1"
mv export-*.res ScriptAlone.res

resilient-sdk extract --script "$1" --rule "$2"
mv export-*.res RuleAndScript.res
