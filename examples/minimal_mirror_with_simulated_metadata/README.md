# Minimal Mirror With Simulated Metadata

This example shows the intended shape of an offline-with-online-mirror scaffold without including raw data, private metadata, machine package inventories, or generated bulky outputs.

Decision path:

```text
offline_with_online_mirror + code_data_split + extended + simulated
```

Important rule:

```text
Only project-mirror/server_payload/ is copied to the offline code server.
```

Agent files stay in the online mirror. Real raw data and private metadata belong in the protected server root.
