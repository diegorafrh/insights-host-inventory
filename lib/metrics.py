from prometheus_client import start_http_server, Counter, Summary

host_dedup_processing_time = Summary("inventory_dedup_processing_seconds",
                                     "Time spent looking for existing host (dedup logic)")
new_host_commit_processing_time = Summary("inventory_new_host_commit_seconds",
                                          "Time spent committing a new host to the database")
update_host_commit_processing_time = Summary("inventory_update_host_commit_seconds",
                                             "Time spent committing a update host to the database")
ingress_message_parsing_time = Summary("ingress_message_parsing_seconds",
                                                "Time spent parsing a message from the ingress queue")
create_host_count = Counter("inventory_create_host_count",
                            "The total amount of hosts created")
update_host_count = Counter("inventory_update_host_count",
                            "The total amount of hosts updated")