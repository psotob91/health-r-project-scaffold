# Project Memory

Project ID: `minimal_mirror_with_simulated_metadata`.

Decision path: `offline_with_online_mirror + code_data_split + extended + simulated`.

Standing decisions:

- `server_payload/` is the only server-transferable unit.
- Agent context stays outside `server_payload/`.
- Future production scripts go under `server_payload/scripts/`.
- Raw data are not included in this public example.
- Any real project ID, date, postal, facility, member, claim, or join-key fields must be treated as sensitive by design.
