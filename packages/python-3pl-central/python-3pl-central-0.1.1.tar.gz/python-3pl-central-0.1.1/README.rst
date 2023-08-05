TPL Python API
==============

A Python wrapper for the 3PL Central REST API

Usage
-----

set up a `.env` file in the root of the project:

.. code-block:: python

    BASE_URL="https://secure-wms.com" 
    AUTH_PATH="AuthServer/api/Token"
    CLIENT_ID="your-id"
    CLIENT_SECRET="your-secret"
    FACILITY_ID=99
    TPL_KEY="your-tpl-key"
    GRANT_TYPE="client_credentials"
    USER_LOGIN_ID="name-this-whatever-you-want"
    ROUTING_INFO_ACCOUNT_NUMBER="ups-account-number"

Verify that you can access the api by running 

.. code-block:: python
    
    python3 -m verify_credentials



Then, run the following get a list of methods you can try out, with a handy run-in-place CLI:


.. code-block:: shell
    
    python3 -m examples


.. code-block::

    Which endpoint do you want to try?
    1) cancel_test_order

    2) create_test_item

    3) create_test_order

    4) get_carriers_list

    5) get_order

    Enter a number:



License
-------

MIT

See LICENSE for more details
