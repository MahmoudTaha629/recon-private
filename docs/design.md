# Module contracts

| Module      | Reads from table | Writes to table | Depends on |
|-------------|------------------|-----------------|------------|
| scope       | -                | scope_rules     | -          |
| subdomains  | scope_rules      | subdomains      | scope      |
| resolve     | subdomains       | dns_records     | subdomains |
| probe       | dns_records      | hosts           | resolve    |
| urls        | hosts            | urls            | probe      |

# Naming rules
- tables and columns: snake_case
- every table has: id, scan_id, created_at
- a module writes only to its own tables

# MVP (must work even if time runs out)
scope + subdomains + resolve + probe + urls + db + cli

# Team split
- Member 1: core (config, scope, clients, pipeline, CLI)
- Member 2: recon modules
- Member 3: analysis, dashboard, reports
