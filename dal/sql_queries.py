__author__ = 'mshankar@slac.stanford.edu'

# Add all your SQL queries (if any) in this file.

QUERY_SELECT_EXPERIMENT_ID_FOR_NAME = """
SELECT id FROM regdb.experiment WHERE name = %(experiment_name)s
;
"""


QUERY_SELECT_JOB_HASHES_FOR_EXPERIMENT = """
SELECT
    hash AS hash,
    executable AS executable,
    parameters AS parameters,
    auto_run AS autorun,
    auto_run_user AS auto_run_user,
    location AS location
FROM batch_hash
WHERE
    experiment_id = %(experiment_id)s
ORDER BY hash
;
"""

QUERY_INSERT_JOB_HASH_FOR_EXPERIMENT = """
INSERT INTO batch_hash (experiment_id, hash, executable, parameters, auto_run, auto_run_user, location)
VALUES (
  %(experiment_id)s,
  %(hash)s,
  %(executable)s,
  %(parameters)s,
  %(auto_run)s,
  %(auto_run_user)s,
  %(location)s
  )
;
"""


QUERY_SELECT_NAME_ID_FOR_NEW_EXPERIMENTS = """
SELECT id, name
FROM
    regdb.experiment
WHERE id > %(last_known_experiment_id)s
ORDER BY id
;
"""
