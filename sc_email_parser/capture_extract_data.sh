#!/bin/sh
# syntax: bash ./capture_extract_data "Generic email script (App Exchange v2.3.0)" "Process email message v2.3.0"
resilient-sdk extract --script "$1"
mv export-*.res ScriptAlone.res

resilient-sdk extract --script "$1" --rule "$2"
mv export-*.res RuleAndScript.res
