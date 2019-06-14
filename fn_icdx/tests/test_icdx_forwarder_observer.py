
from __future__ import print_function
import pytest

from fn_icdx.util.helper import ICDXHelper
from fn_icdx.util.amqp_async_consumer import AMQPAsyncConsumer
from resilient import SimpleClient

class TestIcdxForwarder:
    """Test cases for the ICDx forwarder"""



class TestAsyncConsumer:
    """Test cases for the Consumer class"""

    def test_no_value(self):
        """Should raise an exception when AMQPAsyncConsumer is instantiated without params"""
        with pytest.raises(Exception) as e_info:
            obj = AMQPAsyncConsumer()

    def test_partial_value(self):
        """Should raise an exception when AMQPAsyncConsumer is instantiated without enough params"""
        with pytest.raises(Exception) as e_info:
            obj = AMQPAsyncConsumer(
                host="192.168.1.254",
                port=1
            )

    def test_full_unsuccessful_instantiation(self):
        """Should raise an exception when AMQPAsyncConsumer is instantiated with malformed params"""
        with pytest.raises(Exception) as e_info:
            obj = AMQPAsyncConsumer(
                host="192.168.1.254",
                port=1,
                virtual_host="dx",
                username="test",
                amqp_password="pass",
                rest_client=SimpleClient(),
                helper=ICDXHelper()
            )
    def test_successful_instantiation(self):
        """Should not raise an exception when AMQPAsyncConsumer is instantiated with correct params"""

        obj = AMQPAsyncConsumer(
            host="192.168.1.254",
            port=1,
            virtual_host="dx",
            username="test",
            amqp_password="pass",
            rest_client=SimpleClient(),
            helper=ICDXHelper(options={})
        )

    def test_restclient_validation(self):
        """Should raise an exception when AMQPAsyncConsumer is instantiated without params"""

        obj = AMQPAsyncConsumer(
            host="192.168.1.254",
            port=1,
            virtual_host="dx",
            username="test",
            amqp_password="pass",
            rest_client=SimpleClient(),
            helper=ICDXHelper(options={})
        )

        assert isinstance(getattr(obj, "_client"), SimpleClient)

        obj_with_no_client = AMQPAsyncConsumer(
            host="192.168.1.254",
            port=1,
            virtual_host="dx",
            username="test",
            amqp_password="pass",
            rest_client=123,
            helper=ICDXHelper(options={})
        )
        assert isinstance(getattr(obj_with_no_client, "_client"), type(None))

    def test_helper_validation(self):
        """Should raise an exception when AMQPAsyncConsumer is instantiated without params"""

        obj = AMQPAsyncConsumer(
            host="192.168.1.254",
            port=1,
            virtual_host="dx",
            username="test",
            amqp_password="pass",
            rest_client=SimpleClient(),
            helper=ICDXHelper(options={})
        )

        assert isinstance(getattr(obj, "_helper"), ICDXHelper)

        obj_with_no_client = AMQPAsyncConsumer(
            host="192.168.1.254",
            port=1,
            virtual_host="dx",
            username="test",
            amqp_password="pass",
            rest_client=SimpleClient(),
            helper=123
        )
        assert isinstance(getattr(obj_with_no_client, "_helper"), type(None))

    def test_default_port_usage(self):
        """Should raise an exception when AMQPAsyncConsumer is instantiated without params"""

        obj = AMQPAsyncConsumer(
            host="192.168.1.254",
            port=1,
            virtual_host="dx",
            username="test",
            amqp_password="pass",
            rest_client=SimpleClient(),
            helper=ICDXHelper(options={})
        )

        assert isinstance(getattr(obj, "_port"), int)
        assert getattr(obj, "_port") == 1

        obj_with_no_client = AMQPAsyncConsumer(
            host="192.168.1.254",
            port="notaPort",
            virtual_host="dx",
            username="test",
            amqp_password="pass",
            rest_client=SimpleClient(),
            helper=123
        )
        assert isinstance(getattr(obj_with_no_client, "_port"), int)
        assert getattr(obj_with_no_client, "_port") == 5672