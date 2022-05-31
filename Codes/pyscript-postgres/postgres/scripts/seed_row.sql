INSERT INTO note (rowid, username, body)
    VALUES (1, 'SYSTEM', 'Auto Generated Note!!!')
ON CONFLICT
    DO NOTHING;

SELECT
    setval('note_rowid_seq', (
            SELECT
                MAX(rowid)
            FROM note));

