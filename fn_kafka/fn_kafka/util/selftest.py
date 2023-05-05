# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn-kafka
"""
import logging
from fn_kafka.lib.kafka_common import create_producer

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


def selftest_function(opts):
   """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
   """
   options = opts.get("fn_kafka", {})
   selftest_broker = options.get("selftest_broker")

   if not selftest_broker:
      return {"state": "unimplemented"}
   else:
      # get the a producer for testing
      state = "success"
      try:
         producer = create_producer(opts, selftest_broker)
         producer.close()
      except:
         state = "failure"      

      return {"state": state}
