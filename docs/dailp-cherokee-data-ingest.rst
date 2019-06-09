================================================================================
  Ingest DAILP Cherokee Data
================================================================================

--------------------------------------------------------------------------------
 Joel Dunham — June 7, 2019
--------------------------------------------------------------------------------

.. image:: images/old-logo.png
   :width: 25%
   :alt: OLD (DativeBase) logo image
   :align: right

In the context of the DAILP Cherokee project, we can ingest the DAILP Cherokee
language data into our local OLD using the
`DAILP Ingest tool dailp-ingest-clj`_.

First, clone the ``dailp-ingest-clj`` source, checkout out the master
branch, and ensure you are at the commit indicated below:

.. code:: console

   $ git clone https://github.com/dativebase/dailp-ingest-clj.git
   $ cd dailp-ingest-clj
   $ git status
   On branch master
   $ git log -1
   commit 0ff8529bff4e2581d1913f8aad789cd26c4e7909

Making sure you have Leiningen_ installed, use ``lein`` to create a JAR file.

.. code:: console

   $ lein uberjar

Run the ingest script to ingest the DAILP cherokee data to your local OLD:

.. code:: console

  $ java -jar target/uberjar/dailp-ingest-clj-0.1.0-SNAPSHOT-standalone.jar \
        http://127.0.0.1:61001/old/ \
        admin \
        adminA_1

The above will take some time to run. It took approximately 20 minutes on my
machine. By navigating through the forms browse page at
`http://127.0.0.1:61000/#forms` you can watch as the forms are ingested. When
the ingest completes, you should have the following counts of OLD resources:

- forms:                6,932
- tags:                 19
- syntactic categories: 8
