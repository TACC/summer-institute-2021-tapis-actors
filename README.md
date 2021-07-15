# tapis_hello_world_actor

Install the CLI
===============

The Tapis CLI is available as a Python package. We highly recommend using
Python 3.7+ as the Python runtime behind the Tapis CLI.

Install with Pip
----------------

.. code-block:: bash

   $ pip3 install tapis-cli


Initialize a Session
====================

You must set up a Tapis session on each host where you will use the Tapis CLI.
This is a scripted process implemented by the command :code:`tapis auth init`.

.. code-block:: text

   $ tapis auth init

   +---------------+--------------------------------------+----------------------------------------+
   |      Name     |             Description              |                  URL                   |
   +---------------+--------------------------------------+----------------------------------------+
   |      3dem     |             3dem Tenant              |         https://api.3dem.org/          |
   |     a2cps     |   Acute to Chronic Pain Signatures   |         https://api.a2cps.org/         |
   |   agave.prod  |         Agave Public Tenant          |      https://public.agaveapi.co/       |
   |  araport.org  |               Araport                |        https://api.araport.org/        |
   |     bridge    |                Bridge                |     https://api.bridge.tacc.cloud/     |
   |   designsafe  |              DesignSafe              |    https://agave.designsafe-ci.org/    |
   |  iplantc.org  |         CyVerse Science APIs         |       https://agave.iplantc.org/       |
   |      irec     |              iReceptor               | https://irec.tenants.prod.tacc.cloud/  |
   |    portals    |            Portals Tenant            |  https://portals-api.tacc.utexas.edu/  |
   |      sd2e     |             SD2E Tenant              |         https://api.sd2e.org/          |
   |      sgci     | Science Gateways Community Institute |        https://sgci.tacc.cloud/        |
   |   tacc.prod   |                 TACC                 |      https://api.tacc.utexas.edu/      |
   | vdjserver.org |              VDJ Server              | https://vdj-agave-api.tacc.utexas.edu/ |
   +---------------+--------------------------------------+----------------------------------------+

   Enter a tenant name [tacc.prod]:

   Container registry access:
   --------------------------
   Registry Url [e]:
   Registry Username [docker_username]:
   Registry Password:
   Registry Namespace [docker_namespace]:
   +--------------------+----------------------------------+
   | Field              | Value                            |
   +--------------------+----------------------------------+
   | tenant_id          | tacc.prod                        |
   | username           | sgopal                           |
   | api_key            | $API_KEY                         |
   | access_token       | $ACCESS_TOKEN                    |
   | expires_at         | Thu Jul 15 13:11:02 2021         |
   | verify             | True                             |
   | registry_url       | e                                |
   | registry_username  | docker_username                  |
   | registry_password  |                                  |
   | registry_namespace | docker_namespace                 |
   +--------------------|-----------------------------------

Work with Actors
================

In Tapis, **actors** are container-based functions-as-a-service that follow the
actor model of concurrent computation. An actor responds to messages it receives
by changing its state, performing an action, sending out response messages, or
all of the above.

The function an actor performs is exposed as the default command in a container.
It is typically quick and requires little processing power - i.e. an app may be
configured to
`run FastQC <../advanced-api/create_a_custom_app.html>`__,
and an actor may trigger a job using that app.

The guide below is a brief introduction to interacting with actors on the Tapis
platform. For a full reference guide to actors, see the
`Abaco Documentation <https://tacc-cloud.readthedocs.io/projects/abaco/en/latest/index.html>`_.

Create a New Actor
------------------

The function of an actor is exposed as the default command in a Docker
container. Here, we will create an actor from an existing Docker container image
called **tacc/hello-world:latest** available on
`Docker Hub <https://hub.docker.com/repository/docker/tacc/hello-world>`__.
The default command for this container simply prints the message "Hello, World" or
the message sent to it, which will be captured in the actor logs.

Create the actor as:

.. code-block:: bash

   $ tapis actors create --repo tacc/hello-world:latest \
                         -n example-actor \
                         -d "Test actor that says Hello, World"
   +----------------+-----------------------------+
   | Field          | Value                       |
   +----------------+-----------------------------+
   | id             | NN5N0kGDvZQpA               |
   | name           | example-actor               |
   | owner          | taccuser                    |
   | image          | tacc/hello-world:latest     |
   | lastUpdateTime | 2021-07-14T22:25:06.171534  |
   | status         | SUBMITTED                   |
   | cronOn         | False                       |
   +----------------+-----------------------------+

The ``--repo`` flag points to the Docker Hub repo on which this actor is based,
the ``-n`` flag and ``-d`` flag attach a human-readable name and description to
the actor.

The resulting actor is assigned an id: ``NN5N0kGDvZQpA``. The actor id can be
queried by:

.. code-block:: bash

   $ tapis actors show -v NN5N0kGDvZQpA
   {
    "id": "NN5N0kGDvZQpA",
    "name": "example-actor",
    "description": "Test actor that says Hello, World",
    "owner": "sgopal",
    "image": "tacc/hello-world:latest",
    "createTime": "2021-07-14T22:25:06.171Z",
    "lastUpdateTime": "2021-07-14T22:25:06.171Z",
    "defaultEnvironment": {},
    "gid": 862347,
    "hints": [],
    "link": "",
    "mounts": [],
    "privileged": false,
    "queue": "default",
    "stateless": true,
    "status": "READY",
    "statusMessage": " ",
    "token": true,
    "uid": 862347,
    "useContainerUid": false,
    "webhook": "",
    "cronOn": false,
    "cronSchedule": null,
    "cronNextEx": null,
    "_links": {
      "executions": "https://api.tacc.utexas.edu/actors/v2/NN5N0kGDvZQpA/executions",
      "owner": "https://api.tacc.utexas.edu/profiles/v2/sgopal",
      "self": "https://api.tacc.utexas.edu/actors/v2/NN5N0kGDvZQpA"
      }
    }


Above, you can see the plain text name, description that were passed on the command line. In addition, you can see the
"status" of the actor is "READY", meaning it is ready to receive and act on
messages. Finally, you can list all actors visible to you with:

.. code-block:: bash

   $ tapis actors list
   +---------------+---------------+----------+-----------------------------+----------------------------+--------+-------+
   | id            | name          | owner    | image                       | lastUpdateTime             | status | cronOn|
   +---------------+---------------+----------+-----------------------------+----------------------------+--------+-------+
   | NN5N0kGDvZQpA | example-actor | taccuser | tacc/hello-world:latest     | 2021-07-14T22:25:06.171Z   | READY  | False |
   +---------------+---------------+----------+-----------------------------+----------------------------+--------+-------+


Submit a Message to the Actor
-----------------------------

Next, let's craft a simple message to send to the reactor. Messages can be plain
text or in JSON format. When using the python actor libraries as in the example
above, JSON-formatted messages are made available as python dictionaries.

.. code-block:: bash

   # Write a message
   $ export MESSAGE='Hello, World'
   $ echo $MESSAGE
   Hello, World

   $ Submit the message to the actor
   $ tapis actors submit -m "$MESSAGE" NN5N0kGDvZQpA
   +-------------+---------------+
   |  Field      | Value         |
   +-------------+---------------+
   | executionId | N4xQ5WM5Np1X0 |
   | msg         | Hello, World  |
   +-------------+---------------+

The id of the actor (``N4xQ5WM5Np1X0``) was used on the command line to specify
which actor should receive the message. In response, an "execution id"
(``N4xQ5WM5Np1X0``) is returned. An execution is a specific instance of an actor.
List all the executions for a given actor as:

.. code-block::bash

   $ tapis actors execs list NN5N0kGDvZQpA
   +---------------+----------+
   | executionId   | status   |
   +---------------+----------+
   | N4xQ5WM5Np1X0 | COMPLETE |
   +---------------+----------+

The above execution has already completed. Show detailed information for the
execution with:

.. code-block:: bash

   $ tapis actors execs show -v NN5N0kGDvZQpA N4xQ5WM5Np1X0
   {
      "actorId": "NN5N0kGDvZQpA",
      "apiServer": "https://api.tacc.utexas.edu",
      "cpu": 121748743,
      "exitCode": 0,
      "finalState": {
        "Dead": false,
        "Error": "",
        "ExitCode": 0,
        "FinishedAt": "2021-07-14T22:32:45.602Z",
        "OOMKilled": false,
        "Paused": false,
        "Pid": 0,
        "Restarting": false,
        "Running": false,
        "StartedAt": "2021-07-14T22:32:45.223Z",
        "Status": "exited"
      },
      "id": "N4xQ5WM5Np1X0",
      "io": 176,
      "messageReceivedTime": "2021-07-14T22:32:37.051Z",
      "runtime": 1,
      "startTime": "2021-07-14T22:32:44.752Z",
      "status": "COMPLETE",
      "workerId": "JABKl4BeDwXJD",
      "_links": {
        "logs": "https://api.tacc.utexas.edu/actors/v2/NN5N0kGDvZQpA/executions/N4xQ5WM5Np1X0/logs",
        "owner": "https://api.tacc.utexas.edu/profiles/v2/sgopal",
        "self": "https://api.tacc.utexas.edu/actors/v2/NN5N0kGDvZQpA/executions/N4xQ5WM5Np1X0"
      }
   }


Check the Logs for an Execution
-------------------------------

An execution's logs will contain whatever was printed to STDOUT / STDERR by the
actor. In our demo actor, we just expect the actor to print the message passed to it.

.. code-block:: bash

   $ tapis actors execs logs NN5N0kGDvZQpA N4xQ5WM5Np1X0
   Logs for execution N4xQ5WM5Np1X0
    Actor received message: Hello, World


In a normal scenario, the actor would then act on the contents of a message to, e.g.,
kick off a job, perform some data management, send messages to other actors, or
more.


Run Synchronously
-----------------

The previous message submission (with ``tapis actors submit``) was an
*asynchronous* run, meaning the command prompt detached from the process after
it was submitted to the actor. In that case, it was up to us to check the execution
to see if it had completed and manually print the logs.

There is also a mode to run actors *synchronously* using ``tapis actors run``,
meaning the command line stays attached to the process awaiting a response after
sending a message to the actor. For example:

.. code-block:: bash

   $ tapis actors run -m "$MESSAGE" NN5N0kGDvZQpA
   FULL CONTEXT:
   {
     "username": "taccuser",
     "HOSTNAME": "33d4dd334ef9",
     "_abaco_worker_id": "X5xGkZ0lol0D3",
     "raw_message": "{\"key1\":\"value1\", \"key2\":\"value2\"}",
     "actor_dbid": "TACC-PROD_boEg3mEvrKO5w",
     "_abaco_container_repo": "jturcino/abaco-trial:latest",
     "content_type": null,
     "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
     "MSG": "{\"key1\":\"value1\", \"key2\":\"value2\"}",
     "HOME": "/",
     "_abaco_actor_state": "{}",
     "_abaco_actor_name": "example-actor",
     "_abaco_Content_Type": "str",
     "execution_id": "jP3RExQW108wM",
     "_abaco_synchronous": "True",
     "_abaco_access_token": "de6d11bdbb5a16bdd85beec692b1b283",
     "_abaco_api_server": "https://api.tacc.utexas.edu",
     "_abaco_actor_dbid": "TACC-PROD_boEg3mEvrKO5w",
     "_abaco_jwt_header_name": "X-Jwt-Assertion-Tacc-Prod",
     "_abaco_actor_id": "NN5N0kGDvZQpA",
     "_abaco_execution_id": "jP3RExQW108wM",
     "state": "{}",
     "_abaco_username": "taccuser",
     "actor_id": "NN5N0kGDvZQpA"
   }
   ...

The output above is truncated because it is mostly the same response as our
first execution of the actor. This time, however, we did not need to query the
logs for this execution for them to print to screen - that was done
automatically.

