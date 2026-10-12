#!/bin/sh
now=`date '+%Y%m%d_%H%M'`
mv Data_Breach_Best_Practices_for_Resilient.zip Data_Breach_Best_Practices_for_Resilient_$now.zip
zip -r Data_Breach_Best_Practices_for_Resilient.zip Data_Breach_Best_Practices_for_Resilient.md data_breach_best_practices_playbook.res doc
