# Copilot library render — per-library regression reports

One report per library in `Library_regression_report/`. Each was produced by a dedicated agent that read the
upstream source at the pinned tag, the compiler-plugin source, the exact-version bala, the
Ballerina Central metadata, and both renders plus both JSON models.

## What is being compared

| side | repo | branch | commit |
|---|---|---|---|
| `old` | `ballerina-platform/ballerina-vscode` | `main` | `eb5d81b3` |
| `new` | local `Check-PR-s/ballerina-vscode` | `L1_json_and_annotations_with_spec_v2` | `412ba01e` |

The library and its version are identical on both sides (all 162 `PIN_OK`), so every
difference is attributable to the extractor/renderer change, not to library drift.

## Verdicts

| Verdict | Libraries |
|---|---|
| **MINOR REGRESSION** | 2 |
| **IMPROVEMENT ONLY** | 195 |
| **NO REGRESSION** | 9 |
| **total** | **206** |

## Repo-wide render signals (counted directly from the render files)

| Signal | `old` | `new` |
|---|---|---|
| Total rendered lines | 314,618 | 344,545 |
| `// Unknown type:` lines | 2,656 | 0 |
| Libraries containing any `// Unknown type:` | 141 | 0 |

## Libraries needing attention

| Library | Version | Verdict | Report |
|---|---|---|---|
| `ballerina/ftp` | `2.20.1` | **MINOR REGRESSION** | [ftp.md](ftp.md) |
| `ballerinax/mssql` | `1.19.0` | **MINOR REGRESSION** | [mssql.md](mssql.md) |

## All libraries

| Library | Version | Tag reviewed | old | new | Δ | Verdict | Report |
|---|---|---|---:|---:|---:|---|---|
| `ballerina/ftp` | `2.20.1` | `v2.20.1` | 1564 | 1703 | +139 | MINOR REGRESSION | [ftp.md](ftp.md) |
| `ballerinax/mssql` | `1.19.0` | `v1.19.0` | 837 | 899 | +62 | MINOR REGRESSION | [mssql.md](mssql.md) |
| `ballerinax/github` | `6.0.0` | `v6.0.0` | 22880 | 26408 | +3528 | IMPROVEMENT ONLY | [github.md](github.md) |
| `ballerinax/shopify.admin` | `3.0.0` | `v3.0.0` | 11780 | 15280 | +3500 | IMPROVEMENT ONLY | [shopify.admin.md](shopify.admin.md) |
| `ballerinax/mailchimp.marketing` | `1.0.2` | `v1.0.2` | 11579 | 13811 | +2232 | IMPROVEMENT ONLY | [mailchimp.marketing.md](mailchimp.marketing.md) |
| `ballerinax/stripe` | `2.0.1` | `v2.0.1` | 31426 | 33448 | +2022 | IMPROVEMENT ONLY | [stripe.md](stripe.md) |
| `ballerinax/zoom.meetings` | `1.0.2` | `v1.0.2` | 12144 | 14104 | +1960 | IMPROVEMENT ONLY | [zoom.meetings.md](zoom.meetings.md) |
| `ballerinax/discord` | `2.0.1` | `v2.0.1` | 5779 | 7142 | +1363 | IMPROVEMENT ONLY | [discord.md](discord.md) |
| `ballerina/http` | `2.16.6` | `v2.16.6` | 3532 | 4669 | +1137 | IMPROVEMENT ONLY | [http.md](http.md) |
| `ballerinax/twitter` | `5.0.1` | `v5.0.1` | 4045 | 4965 | +920 | IMPROVEMENT ONLY | [twitter.md](twitter.md) |
| `ballerinax/asana` | `3.0.1` | `v3.0.1` | 7484 | 8270 | +786 | IMPROVEMENT ONLY | [asana.md](asana.md) |
| `ballerinax/slack` | `5.0.1` | `v5.0.1` | 5041 | 5754 | +713 | IMPROVEMENT ONLY | [slack.md](slack.md) |
| `ballerinax/elastic.elasticcloud` | `1.0.1` | `v1.0.1` | 4976 | 5668 | +692 | IMPROVEMENT ONLY | [elastic.elasticcloud.md](elastic.elasticcloud.md) |
| `ballerina/sql` | `1.19.0` | `v1.19.0` | 1027 | 1551 | +524 | IMPROVEMENT ONLY | [sql.md](sql.md) |
| `ballerina/io` | `1.8.1` | `v1.8.1` | 356 | 879 | +523 | IMPROVEMENT ONLY | [io.md](io.md) |
| `ballerina/ai` | `1.13.0` | `v1.13.0` | 2683 | 3172 | +489 | IMPROVEMENT ONLY | [ai.md](ai.md) |
| `ballerinax/postgresql` | `1.19.0` | `v1.19.0` | 1393 | 1864 | +471 | IMPROVEMENT ONLY | [postgresql.md](postgresql.md) |
| `ballerinax/mailchimp.transactional` | `1.0.2` | `v1.0.2` | 3688 | 4155 | +467 | IMPROVEMENT ONLY | [mailchimp.transactional.md](mailchimp.transactional.md) |
| `ballerinax/smartsheet` | `1.0.2` | `v1.0.2` | 10516 | 10940 | +424 | IMPROVEMENT ONLY | [smartsheet.md](smartsheet.md) |
| `ballerinax/sap.s4hana.ce_salesorder_0001` | `2.1.0` | `ce_salesorder_0001-v2.1.0` | 2070 | 2419 | +349 | IMPROVEMENT ONLY | [sap.s4hana.ce_salesorder_0001.md](sap.s4hana.ce_salesorder_0001.md) |
| `ballerinax/asb` | `3.10.0` | `v3.10.0` | 1368 | 1699 | +331 | IMPROVEMENT ONLY | [asb.md](asb.md) |
| `ballerinax/openai.audio` | `3.0.0` | `v3.0.0` | 2991 | 3286 | +295 | IMPROVEMENT ONLY | [openai.audio.md](openai.audio.md) |
| `ballerinax/openai.finetunes` | `3.0.0` | `v3.0.0` | 3035 | 3330 | +295 | IMPROVEMENT ONLY | [openai.finetunes.md](openai.finetunes.md) |
| `ballerina/mime` | `2.12.2` | `v2.12.2` | 210 | 490 | +280 | IMPROVEMENT ONLY | [mime.md](mime.md) |
| `ballerinax/zoom.scheduler` | `1.0.2` | `v1.0.2` | 1419 | 1673 | +254 | IMPROVEMENT ONLY | [zoom.scheduler.md](zoom.scheduler.md) |
| `ballerina/xlsx` | `1.0.1` | `v1.0.1` | 638 | 891 | +253 | IMPROVEMENT ONLY | [xlsx.md](xlsx.md) |
| `ballerinax/salesforce` | `8.7.0` | `v8.7.0` | 1769 | 1985 | +216 | IMPROVEMENT ONLY | [salesforce.md](salesforce.md) |
| `ballerina/mcp` | `1.2.0` | `v1.2.0` | 1058 | 1258 | +200 | IMPROVEMENT ONLY | [mcp.md](mcp.md) |
| `ballerinax/paypal.orders` | `2.0.2` | `v2.0.2` | 2219 | 2410 | +191 | IMPROVEMENT ONLY | [paypal.orders.md](paypal.orders.md) |
| `ballerinax/ai.agent` | `0.9.2` | `v0.9.2` | 2128 | 2315 | +187 | IMPROVEMENT ONLY | [ai.agent.md](ai.agent.md) |
| `ballerinax/microsoft.onedrive` | `3.0.2` | `v3.0.2` | 10879 | 11055 | +176 | IMPROVEMENT ONLY | [microsoft.onedrive.md](microsoft.onedrive.md) |
| `ballerina/smb` | `2.0.1` | `v2.0.1` | 973 | 1148 | +175 | IMPROVEMENT ONLY | [smb.md](smb.md) |
| `ballerina/grpc` | `1.14.7` | `v1.14.7` | 1239 | 1406 | +167 | IMPROVEMENT ONLY | [grpc.md](grpc.md) |
| `ballerinax/mistral` | `1.0.2` | `v1.0.2` | 1248 | 1409 | +161 | IMPROVEMENT ONLY | [mistral.md](mistral.md) |
| `ballerina/websocket` | `2.15.5` | `v2.15.5` | 831 | 988 | +157 | IMPROVEMENT ONLY | [websocket.md](websocket.md) |
| `ballerina/graphql` | `1.17.0` | `v1.17.0` | 1578 | 1722 | +144 | IMPROVEMENT ONLY | [graphql.md](graphql.md) |
| `ballerinax/redis` | `3.4.1` | `v3.4.1` | 695 | 838 | +143 | IMPROVEMENT ONLY | [redis.md](redis.md) |
| `ballerinax/googleapis.sheets` | `4.0.0` | `v4.0.0` | 754 | 881 | +127 | IMPROVEMENT ONLY | [googleapis.sheets.md](googleapis.sheets.md) |
| `ballerinax/trello` | `2.0.1` | `v2.0.1` | 4379 | 4499 | +120 | IMPROVEMENT ONLY | [trello.md](trello.md) |
| `ballerinax/paypal.subscriptions` | `1.0.2` | `v1.0.2` | 1154 | 1272 | +118 | IMPROVEMENT ONLY | [paypal.subscriptions.md](paypal.subscriptions.md) |
| `ballerinax/azure.functions` | `4.2.0` | `v4.2.0` | 231 | 338 | +107 | IMPROVEMENT ONLY | [azure.functions.md](azure.functions.md) |
| `ballerina/cache` | `3.10.0` | `v3.10.0` | 78 | 180 | +102 | IMPROVEMENT ONLY | [cache.md](cache.md) |
| `ballerinax/jira` | `2.0.2` | `v2.0.2` | 16649 | 16749 | +100 | IMPROVEMENT ONLY | [jira.md](jira.md) |
| `ballerinax/mongodb` | `5.2.4` | `v5.2.4` | 608 | 707 | +99 | IMPROVEMENT ONLY | [mongodb.md](mongodb.md) |
| `ballerinax/paypal.invoices` | `1.0.2` | `v1.0.2` | 1153 | 1251 | +98 | IMPROVEMENT ONLY | [paypal.invoices.md](paypal.invoices.md) |
| `ballerinax/nats` | `3.3.1` | `v3.3.1` | 552 | 646 | +94 | IMPROVEMENT ONLY | [nats.md](nats.md) |
| `ballerina/websub` | `2.15.0` | `v2.15.0` | 445 | 539 | +94 | IMPROVEMENT ONLY | [websub.md](websub.md) |
| `ballerina/email` | `2.14.0` | `v2.14.0` | 718 | 811 | +93 | IMPROVEMENT ONLY | [email.md](email.md) |
| `ballerinax/sap.s4hana.api_sales_order_srv` | `2.1.0` | `api_sales_order_srv-v2.1.0` | 5398 | 5487 | +89 | IMPROVEMENT ONLY | [sap.s4hana.api_sales_order_srv.md](sap.s4hana.api_sales_order_srv.md) |
| `ballerinax/alfresco` | `2.0.2` | `v2.0.2` | 4567 | 4654 | +87 | IMPROVEMENT ONLY | [alfresco.md](alfresco.md) |
| `ballerinax/ai.aws.dynamodb` | `1.0.0` | `v1.0.0` | 143 | 225 | +82 | IMPROVEMENT ONLY | [ai.aws.dynamodb.md](ai.aws.dynamodb.md) |
| `ballerina/workflow` | `0.8.3` | `v0.8.3` | 638 | 714 | +76 | IMPROVEMENT ONLY | [workflow.md](workflow.md) |
| `ballerinax/kafka` | `4.6.5` | `v4.6.5` | 936 | 1011 | +75 | IMPROVEMENT ONLY | [kafka.md](kafka.md) |
| `ballerina/websubhub` | `1.16.0` | `v1.16.0` | 512 | 587 | +75 | IMPROVEMENT ONLY | [websubhub.md](websubhub.md) |
| `ballerinax/googleapis.calendar` | `3.2.1` | `no` | 804 | 878 | +74 | IMPROVEMENT ONLY | [googleapis.calendar.md](googleapis.calendar.md) |
| `ballerinax/rabbitmq` | `3.6.0` | `v3.6.0` | 622 | 695 | +73 | IMPROVEMENT ONLY | [rabbitmq.md](rabbitmq.md) |
| `ballerinax/ai.sqlite` | `1.0.0` | `v1.0.0` | 162 | 234 | +72 | IMPROVEMENT ONLY | [ai.sqlite.md](ai.sqlite.md) |
| `ballerinax/ai.memory.postgresql` | `1.0.0` | `v1.0.0` | 133 | 203 | +70 | IMPROVEMENT ONLY | [ai.memory.postgresql.md](ai.memory.postgresql.md) |
| `ballerina/time` | `2.8.1` | `v2.8.1` | 429 | 494 | +65 | IMPROVEMENT ONLY | [time.md](time.md) |
| `ballerinax/ai.memory.redis` | `1.1.0` | `v1.1.0` | 85 | 149 | +64 | IMPROVEMENT ONLY | [ai.memory.redis.md](ai.memory.redis.md) |
| `ballerinax/ai.memory.mssql` | `1.3.0` | `v1.3.0` | 108 | 171 | +63 | IMPROVEMENT ONLY | [ai.memory.mssql.md](ai.memory.mssql.md) |
| `ballerina/observe` | `1.7.1` | `v1.7.1` | 508 | 570 | +62 | IMPROVEMENT ONLY | [observe.md](observe.md) |
| `ballerinax/oracledb` | `1.17.0` | `v1.17.0` | 1091 | 1151 | +60 | IMPROVEMENT ONLY | [oracledb.md](oracledb.md) |
| `ballerinax/twilio` | `5.0.2` | `v5.0.2` | 6220 | 6278 | +58 | IMPROVEMENT ONLY | [twilio.md](twilio.md) |
| `ballerinax/sap.s4hana.api_sales_quotation_srv` | `2.1.0` | `api_sales_quotation_srv-v2.1.0` | 3176 | 3232 | +56 | IMPROVEMENT ONLY | [sap.s4hana.api_sales_quotation_srv.md](sap.s4hana.api_sales_quotation_srv.md) |
| `ballerinax/ibm.ibmmq` | `1.4.4` | `v1.4.4` | 979 | 1033 | +54 | IMPROVEMENT ONLY | [ibm.ibmmq.md](ibm.ibmmq.md) |
| `ballerinax/java.jms` | `1.2.1` | `v1.2.1` | 505 | 558 | +53 | IMPROVEMENT ONLY | [java.jms.md](java.jms.md) |
| `ballerina/log` | `2.17.0` | `v2.17.0` | 628 | 676 | +48 | IMPROVEMENT ONLY | [log.md](log.md) |
| `ballerinax/mysql` | `1.19.0` | `v1.19.0` | 886 | 934 | +48 | IMPROVEMENT ONLY | [mysql.md](mysql.md) |
| `ballerinax/gcloud.pubsub` | `0.1.1` | `v0.1.1` | 347 | 394 | +47 | IMPROVEMENT ONLY | [gcloud.pubsub.md](gcloud.pubsub.md) |
| `ballerina/messaging` | `1.0.0` | `v1.0.0` | 219 | 264 | +45 | IMPROVEMENT ONLY | [messaging.md](messaging.md) |
| `ballerinax/solace` | `0.4.0` | `v0.4.0` | 796 | 840 | +44 | IMPROVEMENT ONLY | [solace.md](solace.md) |
| `ballerina/mqtt` | `1.4.1` | `v1.4.1` | 308 | 351 | +43 | IMPROVEMENT ONLY | [mqtt.md](mqtt.md) |
| `ballerinax/ai.ollama` | `1.2.4` | `v1.2.4` | 155 | 197 | +42 | IMPROVEMENT ONLY | [ai.ollama.md](ai.ollama.md) |
| `ballerina/auth` | `2.14.0` | `v2.14.0` | 142 | 182 | +40 | IMPROVEMENT ONLY | [auth.md](auth.md) |
| `ballerina/file` | `1.13.0` | `v1.13.0` | 416 | 456 | +40 | IMPROVEMENT ONLY | [file.md](file.md) |
| `ballerinax/sap.s4hana.api_sales_order_simulation_srv` | `2.1.0` | `api_sales_order_simulation_srv-v2.1.0` | 1062 | 1102 | +40 | IMPROVEMENT ONLY | [sap.s4hana.api_sales_order_simulation_srv.md](sap.s4hana.api_sales_order_simulation_srv.md) |
| `ballerina/data.xmldata` | `1.6.3` | `v1.6.3` | 626 | 665 | +39 | IMPROVEMENT ONLY | [data.xmldata.md](data.xmldata.md) |
| `ballerinax/salesforce.marketingcloud` | `1.0.2` | `v1.0.2` | 1636 | 1675 | +39 | IMPROVEMENT ONLY | [salesforce.marketingcloud.md](salesforce.marketingcloud.md) |
| `ballerinax/ai.azure` | `1.5.0` | `v1.5.0` | 262 | 297 | +35 | IMPROVEMENT ONLY | [ai.azure.md](ai.azure.md) |
| `ballerinax/paypal.payments` | `2.0.2` | `v2.0.2` | 716 | 750 | +34 | IMPROVEMENT ONLY | [paypal.payments.md](paypal.payments.md) |
| `ballerina/tcp` | `1.13.8` | `v1.13.8` | 251 | 285 | +34 | IMPROVEMENT ONLY | [tcp.md](tcp.md) |
| `ballerina/udp` | `1.13.6` | `v1.13.6` | 205 | 239 | +34 | IMPROVEMENT ONLY | [udp.md](udp.md) |
| `ballerina/constraint` | `1.7.0` | `v1.7.0` | 257 | 290 | +33 | IMPROVEMENT ONLY | [constraint.md](constraint.md) |
| `ballerina/ai.eval` | `0.9.0` | `v0.9.0` | 470 | 502 | +32 | IMPROVEMENT ONLY | [ai.eval.md](ai.eval.md) |
| `ballerina/avro` | `1.2.2` | `v1.2.2` | 61 | 90 | +29 | IMPROVEMENT ONLY | [avro.md](avro.md) |
| `ballerinax/cdc` | `1.4.0` | `v1.4.0` | 1310 | 1339 | +29 | IMPROVEMENT ONLY | [cdc.md](cdc.md) |
| `ballerinax/peoplehr` | `2.2.1` | `v2.2.1` | 1345 | 1374 | +29 | IMPROVEMENT ONLY | [peoplehr.md](peoplehr.md) |
| `ballerina/task` | `2.11.2` | `v2.11.2` | 448 | 477 | +29 | IMPROVEMENT ONLY | [task.md](task.md) |
| `ballerinax/aws.s3` | `4.0.0` | `v4.0.0` | 650 | 677 | +27 | IMPROVEMENT ONLY | [aws.s3.md](aws.s3.md) |
| `ballerina/os` | `1.10.1` | `v1.10.1` | 102 | 129 | +27 | IMPROVEMENT ONLY | [os.md](os.md) |
| `ballerinax/aws.sqs` | `5.0.0` | `v5.0.0` | 885 | 911 | +26 | IMPROVEMENT ONLY | [aws.sqs.md](aws.sqs.md) |
| `ballerina/jwt` | `2.15.1` | `v2.15.1` | 274 | 298 | +24 | IMPROVEMENT ONLY | [jwt.md](jwt.md) |
| `ballerina/oauth2` | `2.15.0` | `v2.15.0` | 283 | 307 | +24 | IMPROVEMENT ONLY | [oauth2.md](oauth2.md) |
| `ballerinax/wso2.apim.catalog` | `1.3.0` | `v1.3.0` | 449 | 473 | +24 | IMPROVEMENT ONLY | [wso2.apim.catalog.md](wso2.apim.catalog.md) |
| `ballerinax/ai.openai` | `1.4.0` | `v1.4.0` | 370 | 393 | +23 | IMPROVEMENT ONLY | [ai.openai.md](ai.openai.md) |
| `ballerinax/aws.lambda` | `3.3.0` | `v3.3.0` | 343 | 365 | +22 | IMPROVEMENT ONLY | [aws.lambda.md](aws.lambda.md) |
| `ballerinax/ai.mistral` | `1.2.4` | `v1.2.4` | 211 | 232 | +21 | IMPROVEMENT ONLY | [ai.mistral.md](ai.mistral.md) |
| `ballerinax/ai.anthropic` | `1.3.4` | `v1.3.4` | 168 | 188 | +20 | IMPROVEMENT ONLY | [ai.anthropic.md](ai.anthropic.md) |
| `ballerinax/ai.googleapis.vertex` | `1.0.2` | `v1.0.2` | 257 | 277 | +20 | IMPROVEMENT ONLY | [ai.googleapis.vertex.md](ai.googleapis.vertex.md) |
| `ballerinax/ai.deepseek` | `1.1.4` | `v1.1.4` | 125 | 144 | +19 | IMPROVEMENT ONLY | [ai.deepseek.md](ai.deepseek.md) |
| `ballerina/xmldata` | `2.9.2` | `v2.9.2` | 125 | 144 | +19 | IMPROVEMENT ONLY | [xmldata.md](xmldata.md) |
| `ballerinax/sap.s4hana.api_sales_inquiry_srv` | `2.1.0` | `default branch` | 1131 | 1149 | +18 | IMPROVEMENT ONLY | [sap.s4hana.api_sales_inquiry_srv.md](sap.s4hana.api_sales_inquiry_srv.md) |
| `ballerinax/ai.openrouter` | `1.0.2` | `v1.0.2` | 148 | 165 | +17 | IMPROVEMENT ONLY | [ai.openrouter.md](ai.openrouter.md) |
| `ballerina/serdes` | `0.2.0` | `v0.2.0` | 132 | 149 | +17 | IMPROVEMENT ONLY | [serdes.md](serdes.md) |
| `ballerinax/ai.milvus` | `1.0.4` | `v1.0.4` | 130 | 146 | +16 | IMPROVEMENT ONLY | [ai.milvus.md](ai.milvus.md) |
| `ballerinax/ai.pgvector` | `1.0.5` | `v1.0.5` | 120 | 136 | +16 | IMPROVEMENT ONLY | [ai.pgvector.md](ai.pgvector.md) |
| `ballerinax/ai.pinecone` | `1.1.5` | `v1.1.5` | 73 | 89 | +16 | IMPROVEMENT ONLY | [ai.pinecone.md](ai.pinecone.md) |
| `ballerinax/ai.weaviate` | `1.0.5` | `v1.0.5` | 160 | 176 | +16 | IMPROVEMENT ONLY | [ai.weaviate.md](ai.weaviate.md) |
| `ballerinax/ai.devant` | `1.0.4` | `v1.0.4` | 79 | 94 | +15 | IMPROVEMENT ONLY | [ai.devant.md](ai.devant.md) |
| `ballerinax/aws.marketplace.mpm` | `1.0.0` | `v1.0.0` | 295 | 307 | +12 | IMPROVEMENT ONLY | [aws.marketplace.mpm.md](aws.marketplace.mpm.md) |
| `ballerinax/aws.secretmanager` | `0.4.1` | `v0.4.1` | 459 | 471 | +12 | IMPROVEMENT ONLY | [aws.secretmanager.md](aws.secretmanager.md) |
| `ballerinax/guidewire.insnow` | `0.2.0` | `v0.2.0` | 2237 | 2249 | +12 | IMPROVEMENT ONLY | [guidewire.insnow.md](guidewire.insnow.md) |
| `ballerinax/copybook` | `1.1.0` | `v1.1.0` | 30 | 40 | +10 | IMPROVEMENT ONLY | [copybook.md](copybook.md) |
| `ballerinax/ai.microsoft.sharepoint` | `1.0.1` | `v1.0.1` | 309 | 318 | +9 | IMPROVEMENT ONLY | [ai.microsoft.sharepoint.md](ai.microsoft.sharepoint.md) |
| `ballerinax/aws.redshiftdata` | `1.1.0` | `v1.1.0` | 531 | 540 | +9 | IMPROVEMENT ONLY | [aws.redshiftdata.md](aws.redshiftdata.md) |
| `ballerinax/pinecone.vector` | `1.0.2` | `none — no module-scoped tag exists in` | 305 | 314 | +9 | IMPROVEMENT ONLY | [pinecone.vector.md](pinecone.vector.md) |
| `ballerinax/sap.commerce.webservices` | `0.9.1` | `v0.9.1` | 8233 | 8242 | +9 | IMPROVEMENT ONLY | [sap.commerce.webservices.md](sap.commerce.webservices.md) |
| `ballerinax/sap.s4hana.api_sd_incoterms_srv` | `2.1.0` | `api_sd_incoterms_srv-v2.1.0` | 498 | 507 | +9 | IMPROVEMENT ONLY | [sap.s4hana.api_sd_incoterms_srv.md](sap.s4hana.api_sd_incoterms_srv.md) |
| `ballerinax/aws.sns` | `4.0.1` | `v4.0.1` | 1237 | 1245 | +8 | IMPROVEMENT ONLY | [aws.sns.md](aws.sns.md) |
| `ballerina/yaml` | `0.8.0` | `v0.8.0` | 195 | 203 | +8 | IMPROVEMENT ONLY | [yaml.md](yaml.md) |
| `ballerina/data.jsondata` | `1.1.4` | `v1.1.4` | 307 | 314 | +7 | IMPROVEMENT ONLY | [data.jsondata.md](data.jsondata.md) |
| `ballerina/data.yaml` | `0.8.0` | `v0.8.0` | 191 | 198 | +7 | IMPROVEMENT ONLY | [data.yaml.md](data.yaml.md) |
| `ballerina/edi` | `1.6.0` | `v1.6.0` | 597 | 604 | +7 | IMPROVEMENT ONLY | [edi.md](edi.md) |
| `ballerinax/openai.chat` | `5.0.0` | `v5.0.0` | 970 | 977 | +7 | IMPROVEMENT ONLY | [openai.chat.md](openai.chat.md) |
| `ballerinax/weaviate` | `1.0.2` | `default branch` | 662 | 669 | +7 | IMPROVEMENT ONLY | [weaviate.md](weaviate.md) |
| `ballerina/data.csv` | `0.10.0` | `v0.10.0` | 595 | 601 | +6 | IMPROVEMENT ONLY | [data.csv.md](data.csv.md) |
| `ballerina/pdf` | `0.9.1` | `v0.9.1` | 240 | 246 | +6 | IMPROVEMENT ONLY | [pdf.md](pdf.md) |
| `ballerina/protobuf` | `1.8.0` | `v1.8.0` | 80 | 86 | +6 | IMPROVEMENT ONLY | [protobuf.md](protobuf.md) |
| `ballerinax/sap.s4hana.api_salesdistrict_srv` | `2.1.0` | `api_salesdistrict_srv-v2.1.0` | 360 | 366 | +6 | IMPROVEMENT ONLY | [sap.s4hana.api_salesdistrict_srv.md](sap.s4hana.api_salesdistrict_srv.md) |
| `ballerinax/sap.s4hana.api_salesorganization_srv` | `2.1.0` | `api_salesorganization_srv-v2.1.0` | 365 | 371 | +6 | IMPROVEMENT ONLY | [sap.s4hana.api_salesorganization_srv.md](sap.s4hana.api_salesorganization_srv.md) |
| `ballerinax/sap.s4hana.api_sd_sa_soldtopartydetn` | `2.1.0` | `api_sd_sa_soldtopartydetn-v2.1.0` | 250 | 256 | +6 | IMPROVEMENT ONLY | [sap.s4hana.api_sd_sa_soldtopartydetn.md](sap.s4hana.api_sd_sa_soldtopartydetn.md) |
| `ballerinax/aws.marketplace.mpe` | `1.0.0` | `v1.0.0` | 221 | 226 | +5 | IMPROVEMENT ONLY | [aws.marketplace.mpe.md](aws.marketplace.mpe.md) |
| `ballerinax/azure.openai.chat` | `4.0.0` | `v4.0.0` | 1038 | 1043 | +5 | IMPROVEMENT ONLY | [azure.openai.chat.md](azure.openai.chat.md) |
| `ballerina/etl` | `0.8.0` | `v0.8.0` | 588 | 593 | +5 | IMPROVEMENT ONLY | [etl.md](etl.md) |
| `ballerinax/googleapis.gmail` | `4.2.0` | `v4.2.0` | 730 | 735 | +5 | IMPROVEMENT ONLY | [googleapis.gmail.md](googleapis.gmail.md) |
| `ballerinax/sap.s4hana.salesarea_0001` | `2.1.0` | `salesarea_0001-v2.1.0` | 238 | 243 | +5 | IMPROVEMENT ONLY | [sap.s4hana.salesarea_0001.md](sap.s4hana.salesarea_0001.md) |
| `ballerina/persist` | `1.7.0` | `v1.7.0` | 207 | 211 | +4 | IMPROVEMENT ONLY | [persist.md](persist.md) |
| `ballerina/toml` | `0.8.0` | `v0.8.0` | 90 | 94 | +4 | IMPROVEMENT ONLY | [toml.md](toml.md) |
| `ballerinax/azure.ai.search` | `1.0.2` | `v1.0.2` | 1856 | 1859 | +3 | IMPROVEMENT ONLY | [azure.ai.search.md](azure.ai.search.md) |
| `ballerinax/googleapis.gcalendar` | `4.0.1` | `v4.0.1` | 1240 | 1243 | +3 | IMPROVEMENT ONLY | [googleapis.gcalendar.md](googleapis.gcalendar.md) |
| `ballerinax/hubspot.crm.owners` | `2.0.2` | `v2.0.2` | 362 | 365 | +3 | IMPROVEMENT ONLY | [hubspot.crm.owners.md](hubspot.crm.owners.md) |
| `ballerinax/azure.ai.search.index` | `1.0.2` | `v1.0.2` | 831 | 833 | +2 | IMPROVEMENT ONLY | [azure.ai.search.index.md](azure.ai.search.index.md) |
| `ballerinax/docusign.dsadmin` | `2.0.0` | `v2.0.0` | 2514 | 2516 | +2 | IMPROVEMENT ONLY | [docusign.dsadmin.md](docusign.dsadmin.md) |
| `ballerinax/hubspot.crm.extensions.videoconferencing` | `2.0.2` | `v2.0.2` | 243 | 245 | +2 | IMPROVEMENT ONLY | [hubspot.crm.extensions.videoconferencing.md](hubspot.crm.extensions.videoconferencing.md) |
| `ballerina/random` | `1.7.0` | `v1.7.0` | 43 | 45 | +2 | IMPROVEMENT ONLY | [random.md](random.md) |
| `ballerina/regex` | `1.4.3` | `v1.4.3` | 202 | 204 | +2 | IMPROVEMENT ONLY | [regex.md](regex.md) |
| `ballerinax/sap` | `1.3.1` | `v1.3.1` | 207 | 209 | +2 | IMPROVEMENT ONLY | [sap.md](sap.md) |
| `ballerinax/snowflake` | `2.2.2` | `v2.2.2` | 288 | 290 | +2 | IMPROVEMENT ONLY | [snowflake.md](snowflake.md) |
| `ballerinax/aws.redshift` | `1.2.2` | `v1.2.2` | 199 | 200 | +1 | IMPROVEMENT ONLY | [aws.redshift.md](aws.redshift.md) |
| `ballerinax/azure_storage_service` | `4.3.4` | `v4.3.4` | 37 | 38 | +1 | IMPROVEMENT ONLY | [azure_storage_service.md](azure_storage_service.md) |
| `ballerinax/confluent.cavroserdes` | `1.0.3` | `v1.0.3` | 94 | 95 | +1 | IMPROVEMENT ONLY | [confluent.cavroserdes.md](confluent.cavroserdes.md) |
| `ballerinax/confluent.cregistry` | `0.4.5` | `v0.4.5` | 120 | 121 | +1 | IMPROVEMENT ONLY | [confluent.cregistry.md](confluent.cregistry.md) |
| `ballerina/crypto` | `2.12.1` | `v2.12.1` | 1507 | 1508 | +1 | IMPROVEMENT ONLY | [crypto.md](crypto.md) |
| `ballerinax/hubspot.automation.actions` | `2.0.0` | `v2.0.0` | 673 | 674 | +1 | IMPROVEMENT ONLY | [hubspot.automation.actions.md](hubspot.automation.actions.md) |
| `ballerinax/hubspot.crm.associations` | `2.0.2` | `v2.0.2` | 681 | 682 | +1 | IMPROVEMENT ONLY | [hubspot.crm.associations.md](hubspot.crm.associations.md) |
| `ballerinax/hubspot.crm.associations.schema` | `2.0.2` | `v2.0.2` | 581 | 582 | +1 | IMPROVEMENT ONLY | [hubspot.crm.associations.schema.md](hubspot.crm.associations.schema.md) |
| `ballerinax/hubspot.crm.commerce.carts` | `2.0.2` | `v2.0.2` | 781 | 782 | +1 | IMPROVEMENT ONLY | [hubspot.crm.commerce.carts.md](hubspot.crm.commerce.carts.md) |
| `ballerinax/hubspot.crm.commerce.discounts` | `2.0.2` | `v2.0.2` | 763 | 764 | +1 | IMPROVEMENT ONLY | [hubspot.crm.commerce.discounts.md](hubspot.crm.commerce.discounts.md) |
| `ballerinax/hubspot.crm.commerce.orders` | `2.0.2` | `v2.0.2` | 785 | 786 | +1 | IMPROVEMENT ONLY | [hubspot.crm.commerce.orders.md](hubspot.crm.commerce.orders.md) |
| `ballerinax/hubspot.crm.commerce.quotes` | `2.0.2` | `v2.0.2` | 792 | 793 | +1 | IMPROVEMENT ONLY | [hubspot.crm.commerce.quotes.md](hubspot.crm.commerce.quotes.md) |
| `ballerinax/hubspot.crm.commerce.taxes` | `2.0.2` | `v2.0.2` | 761 | 762 | +1 | IMPROVEMENT ONLY | [hubspot.crm.commerce.taxes.md](hubspot.crm.commerce.taxes.md) |
| `ballerinax/hubspot.crm.engagement.meeting` | `2.0.0` | `v2.0.0` | 773 | 774 | +1 | IMPROVEMENT ONLY | [hubspot.crm.engagement.meeting.md](hubspot.crm.engagement.meeting.md) |
| `ballerinax/hubspot.crm.engagement.notes` | `2.0.2` | `v2.0.2` | 784 | 785 | +1 | IMPROVEMENT ONLY | [hubspot.crm.engagement.notes.md](hubspot.crm.engagement.notes.md) |
| `ballerinax/hubspot.crm.engagements.calls` | `2.0.2` | `v2.0.2` | 826 | 827 | +1 | IMPROVEMENT ONLY | [hubspot.crm.engagements.calls.md](hubspot.crm.engagements.calls.md) |
| `ballerinax/hubspot.crm.engagements.communications` | `2.0.2` | `v2.0.2` | 772 | 773 | +1 | IMPROVEMENT ONLY | [hubspot.crm.engagements.communications.md](hubspot.crm.engagements.communications.md) |
| `ballerinax/hubspot.crm.engagements.email` | `2.0.2` | `v2.0.2` | 777 | 778 | +1 | IMPROVEMENT ONLY | [hubspot.crm.engagements.email.md](hubspot.crm.engagements.email.md) |
| `ballerinax/hubspot.crm.engagements.tasks` | `2.0.2` | `v2.0.2` | 790 | 791 | +1 | IMPROVEMENT ONLY | [hubspot.crm.engagements.tasks.md](hubspot.crm.engagements.tasks.md) |
| `ballerinax/hubspot.crm.extensions.timelines` | `2.0.2` | `v2.0.2` | 604 | 605 | +1 | IMPROVEMENT ONLY | [hubspot.crm.extensions.timelines.md](hubspot.crm.extensions.timelines.md) |
| `ballerinax/hubspot.crm.import` | `4.0.2` | `v4.0.2` | 525 | 526 | +1 | IMPROVEMENT ONLY | [hubspot.crm.import.md](hubspot.crm.import.md) |
| `ballerinax/hubspot.crm.lists` | `1.0.2` | `v1.0.2` | 1860 | 1861 | +1 | IMPROVEMENT ONLY | [hubspot.crm.lists.md](hubspot.crm.lists.md) |
| `ballerinax/hubspot.crm.obj.companies` | `2.0.1` | `v2.0.1` | 648 | 649 | +1 | IMPROVEMENT ONLY | [hubspot.crm.obj.companies.md](hubspot.crm.obj.companies.md) |
| `ballerinax/hubspot.crm.obj.contacts` | `1.0.2` | `v1.0.2` | 782 | 783 | +1 | IMPROVEMENT ONLY | [hubspot.crm.obj.contacts.md](hubspot.crm.obj.contacts.md) |
| `ballerinax/hubspot.crm.obj.deals` | `1.0.2` | `v1.0.2` | 795 | 796 | +1 | IMPROVEMENT ONLY | [hubspot.crm.obj.deals.md](hubspot.crm.obj.deals.md) |
| `ballerinax/hubspot.crm.obj.feedback` | `2.0.2` | `v2.0.2` | 780 | 781 | +1 | IMPROVEMENT ONLY | [hubspot.crm.obj.feedback.md](hubspot.crm.obj.feedback.md) |
| `ballerinax/hubspot.crm.obj.leads` | `2.0.2` | `v2.0.2` | 803 | 804 | +1 | IMPROVEMENT ONLY | [hubspot.crm.obj.leads.md](hubspot.crm.obj.leads.md) |
| `ballerinax/hubspot.crm.obj.lineitems` | `2.0.2` | `v2.0.2` | 797 | 798 | +1 | IMPROVEMENT ONLY | [hubspot.crm.obj.lineitems.md](hubspot.crm.obj.lineitems.md) |
| `ballerinax/hubspot.crm.obj.products` | `2.0.2` | `v2.0.2` | 781 | 782 | +1 | IMPROVEMENT ONLY | [hubspot.crm.obj.products.md](hubspot.crm.obj.products.md) |
| `ballerinax/hubspot.crm.obj.schemas` | `2.0.2` | `v2.0.2` | 567 | 568 | +1 | IMPROVEMENT ONLY | [hubspot.crm.obj.schemas.md](hubspot.crm.obj.schemas.md) |
| `ballerinax/hubspot.crm.obj.tickets` | `2.0.2` | `v2.0.2` | 786 | 787 | +1 | IMPROVEMENT ONLY | [hubspot.crm.obj.tickets.md](hubspot.crm.obj.tickets.md) |
| `ballerinax/hubspot.crm.pipelines` | `2.0.2` | `v2.0.2` | 469 | 470 | +1 | IMPROVEMENT ONLY | [hubspot.crm.pipelines.md](hubspot.crm.pipelines.md) |
| `ballerinax/hubspot.crm.properties` | `2.0.2` | `v2.0.2` | 575 | 576 | +1 | IMPROVEMENT ONLY | [hubspot.crm.properties.md](hubspot.crm.properties.md) |
| `ballerinax/hubspot.marketing.campaigns` | `2.0.2` | `v2.0.2` | 672 | 673 | +1 | IMPROVEMENT ONLY | [hubspot.marketing.campaigns.md](hubspot.marketing.campaigns.md) |
| `ballerinax/hubspot.marketing.emails` | `1.0.2` | `v1.0.2` | 1010 | 1011 | +1 | IMPROVEMENT ONLY | [hubspot.marketing.emails.md](hubspot.marketing.emails.md) |
| `ballerinax/hubspot.marketing.events` | `1.0.2` | `v1.0.2` | 1366 | 1367 | +1 | IMPROVEMENT ONLY | [hubspot.marketing.events.md](hubspot.marketing.events.md) |
| `ballerinax/hubspot.marketing.forms` | `1.0.2` | `v1.0.2` | 1043 | 1044 | +1 | IMPROVEMENT ONLY | [hubspot.marketing.forms.md](hubspot.marketing.forms.md) |
| `ballerinax/hubspot.marketing.subscriptions` | `2.0.2` | `v2.0.2` | 761 | 762 | +1 | IMPROVEMENT ONLY | [hubspot.marketing.subscriptions.md](hubspot.marketing.subscriptions.md) |
| `ballerinax/hubspot.marketing.transactional` | `1.0.2` | `v1.0.2` | 407 | 408 | +1 | IMPROVEMENT ONLY | [hubspot.marketing.transactional.md](hubspot.marketing.transactional.md) |
| `ballerinax/ibm.ctg` | `0.1.1` | `v0.1.1` | 253 | 254 | +1 | IMPROVEMENT ONLY | [ibm.ctg.md](ibm.ctg.md) |
| `ballerina/ldap` | `1.4.0` | `v1.4.0` | 552 | 553 | +1 | IMPROVEMENT ONLY | [ldap.md](ldap.md) |
| `ballerinax/milvus` | `1.1.1` | `v1.1.1` | 342 | 343 | +1 | IMPROVEMENT ONLY | [milvus.md](milvus.md) |
| `ballerinax/scim` | `1.0.2` | `v1.0.2` | 917 | 918 | +1 | IMPROVEMENT ONLY | [scim.md](scim.md) |
| `ballerina/soap` | `2.3.1` | `v2.3.1` | 709 | 710 | +1 | IMPROVEMENT ONLY | [soap.md](soap.md) |
| `ballerina/url` | `2.6.2` | `v2.6.2` | 44 | 45 | +1 | IMPROVEMENT ONLY | [url.md](url.md) |
| `ballerina/uuid` | `1.10.0` | `v1.10.0` | 249 | 250 | +1 | IMPROVEMENT ONLY | [uuid.md](uuid.md) |
| `ballerina/xslt` | `2.9.1` | `v2.9.1` | 38 | 39 | +1 | IMPROVEMENT ONLY | [xslt.md](xslt.md) |
| `ballerinax/java.jdbc` | `1.15.1` | `v1.15.1` | 545 | 545 | +0 | IMPROVEMENT ONLY | [java.jdbc.md](java.jdbc.md) |
| `ballerina/ai.np` | `0.5.1` | `v0.5.1` | 60 | 60 | +0 | NO REGRESSION | [ai.np.md](ai.np.md) |
| `ballerinax/amp` | `1.1.0` | `v1.1.0` | 60 | 60 | +0 | NO REGRESSION | [amp.md](amp.md) |
| `ballerinax/candid` | `0.2.1` | `v0.2.1` | 133 | 133 | +0 | NO REGRESSION | [candid.md](candid.md) |
| `ballerinax/idetraceprovider` | `0.9.0` | `v0.9.0` | 44 | 44 | +0 | NO REGRESSION | [idetraceprovider.md](idetraceprovider.md) |
| `ballerina/jballerina.java.arrays` | `1.6.1` | `v1.6.1` | 115 | 115 | +0 | NO REGRESSION | [jballerina.java.arrays.md](jballerina.java.arrays.md) |
| `ballerina/math.vector` | `1.2.0` | `v1.2.0` | 101 | 101 | +0 | NO REGRESSION | [math.vector.md](math.vector.md) |
| `ballerinax/moesif` | `1.0.3` | `v1.0.3` | 295 | 295 | +0 | NO REGRESSION | [moesif.md](moesif.md) |
| `ballerinax/newrelic` | `1.0.3` | `v1.0.3` | 111 | 111 | +0 | NO REGRESSION | [newrelic.md](newrelic.md) |
| `ballerina/otel` | `0.9.0` | `v0.9.0` | 103 | 103 | +0 | NO REGRESSION | [otel.md](otel.md) |

## Report structure

Every report carries the same ten sections: Summary; Change inventory; Correctness against
library source; Regressions; Issues in `new` independent of `old`; Coverage gaps vs. the
library; Compiler plugin; Other considerations; Evidence log; Caveats and unverified items.
The Evidence log lists the commands actually run; the Caveats section lists what could not
be verified.

