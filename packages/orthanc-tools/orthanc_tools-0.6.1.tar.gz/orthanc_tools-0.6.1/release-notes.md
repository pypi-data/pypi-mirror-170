v 0.6.1
=======

- uses orthanc-api-client v 0.7.1 to fix `OrthancCloner` with reverse-proxies

v 0.6.0
=======

- added a scheduler for `OrthancCloner` to allow running at night and weekends.
- BREAKING_CHANGE: `OrthancCloner` constructor: renamed `workers_count` into `worker_threads_count`

v 0.5.1
=======

- added 'mode' for OrthancCloner: `ClonerMode.DEFAULT, ClonerMode.PEERING, ClonerMode.TRANSFER`

v 0.4.9
=======

- uses orthanc-api-client v 0.5.8

v 0.4.7
=======
-  pacs_migrator - added retry for transfer from modality to aet

v 0.4.7
=======
- uses orthanc-api-client v 0.5.0