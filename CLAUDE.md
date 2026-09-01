1. You are only allow to do edits inside this root. '/Users/admin/Desktop/Copilot-Changes/Check-contents/test-bal-copilot-library-get-mds'
2. The render generation scripts should follow the following instructions.

```
Generating the Copilot rendering for a library

  It's a two-stage pipeline. There is no CLI — you must drive stage 1 from a test, because package resolution needs the Ballerina distribution that the test task wires up.

  Java (language server)                        TypeScript (VS Code extension)
  CopilotLibraryManager.loadFilteredLibraries  →  Library model
  ModelToJsonConverter.libraryToJson           →  JSON   ──►  toSyntaxString([json])  →  final string

  ---
  Stage 1 — produce the JSON
  
  1a. Write a throwaway test

  Put it in this exact package (it needs the test module's classpath and distribution):

  packages/ballerina-language-server/flow-model-generator/modules/
    flow-model-generator-ls-extension/src/test/java/io/ballerina/flowmodelgenerator/extension/CatalogProbeTest.java

  package io.ballerina.flowmodelgenerator.extension;

  import com.google.gson.GsonBuilder;
  import io.ballerina.flowmodelgenerator.core.copilot.CopilotLibraryManager;
  import io.ballerina.flowmodelgenerator.core.copilot.model.Library;
  import io.ballerina.flowmodelgenerator.core.copilot.model.ModelToJsonConverter;
  import org.testng.annotations.Test;

  import java.nio.charset.StandardCharsets;
  import java.nio.file.Files;
  import java.nio.file.Path;
  import java.util.List;

  public class CatalogProbeTest {

      private static final String[] LIBS = {"ballerina/http", "ballerinax/kafka"};   // ← your libraries

      @Test
      public void dumpAll() throws Exception {
          Path dir = Path.of("/absolute/path/to/json-out");     // ← MUST be absolute & hardcoded
          Files.createDirectories(dir);
          for (String lib : LIBS) {
              try {
                  List<Library> libs = new CopilotLibraryManager().loadFilteredLibraries(new String[]{lib});
                  if (libs.isEmpty()) {
                      System.err.println("DUMP|" + lib + "|UNRESOLVED");
                      continue;
                  }
                  Files.writeString(dir.resolve(lib.replace('/', '_') + ".json"),
                          new GsonBuilder().setPrettyPrinting().create()
                                  .toJson(ModelToJsonConverter.libraryToJson(libs.get(0))),
                          StandardCharsets.UTF_8);
              } catch (Throwable e) {
                  System.err.println("DUMP|" + lib + "|ERROR|" + e);
              }
          }
      }
  }

  1b. Register it in the TestNG suite — mandatory

  build.gradle uses useTestNG { suites "src/test/resources/testng.xml" }, so --tests alone will not find your class. It fails with "No tests found for given includes". Add to
  flow-model-generator-ls-extension/src/test/resources/testng.xml, inside <classes>:

  <class name="io.ballerina.flowmodelgenerator.extension.CatalogProbeTest"/>

  1c. Run

  cd packages/ballerina-language-server
  ./gradlew :flow-model-generator:flow-model-generator-ls-extension:test --offline \
    --rerun-tasks --tests "io.ballerina.flowmodelgenerator.extension.CatalogProbeTest"

  --offline works if the balas are in ~/.ballerina. Use --rerun-tasks after editing LS resources (e.g. trigger-metadata-models/), or Gradle will serve stale processResources output.

  ---
  Stage 2 — render the JSON
  
  // render-all.ts  (place anywhere; use absolute import path)
  import * as fs from "fs";
  import * as path from "path";
  import { toSyntaxString } from "/ABS/PATH/packages/ballerina-extension/src/features/ai/utils/libs/to-syntax-string";

  const [, , inDir, outDir] = process.argv;
  fs.mkdirSync(outDir, { recursive: true });
  for (const f of fs.readdirSync(inDir).filter((x) => x.endsWith(".json")).sort()) {
      const json = JSON.parse(fs.readFileSync(path.join(inDir, f), "utf-8"));
      const rendered = toSyntaxString([json]);          // ← note: takes an ARRAY
      fs.writeFileSync(path.join(outDir, f.replace(/\.json$/, ".bal.txt")), rendered, "utf-8");
      console.log(f, rendered.split("\n").length, "lines");
  }

  cd packages/ballerina-extension
  npx ts-node --compiler-options '{"module":"commonjs","esModuleInterop":true,"skipLibCheck":true}' \
    /path/to/render-all.ts /path/to/json-out /path/to/rendered-out

  ---
  Four gotchas that will cost time
  
  1. Gradle -Dfoo=bar does not reach the forked test JVM. System.getProperty(...) returns null → Path.of(null) → NPE. Hardcode the output path, or add systemProperty in build.gradle.
  2. testng.xml registration is required (see 1b). This is the single most common failure.
  3. toSyntaxString takes Library[], not a single library. The dumped JSON is one library, so wrap it: toSyntaxString([json]).
  4. Clean up afterwards — delete the probe class and remove the testng.xml line, or the suite carries a stray test. Verify with:
  git diff --exit-code -- .../src/test/resources/testng.xml

  ---
  Verifying the output
  
  grep -c "^// Unknown type:" out.bal.txt        # expect 0
  grep -n "^// --- " out.bal.txt                 # section markers
```
3. This should MUST render for all the libraries that is in the following list, with the given version exactly, Do not change the versions or missed the libraries. If you have any questions please ask

```
Module	Pinned Version
ballerina/ai	1.13.0
ballerina/email	2.14.0
ballerina/ftp	2.20.1
ballerina/grpc	1.14.7
ballerina/graphql	1.17.0
ballerina/http	2.16.6
ballerina/mcp	1.2.0
ballerina/tcp	1.13.8
ballerina/udp	1.13.6
ballerina/websocket	2.15.5
ballerina/websub	2.15.0
ballerina/mqtt	1.4.1
ballerinax/ai.devant	1.0.4
ballerinax/ai.memory.mssql	1.3.0
ballerinax/ai.anthropic	1.3.4
ballerinax/azure.ai.search	1.0.2
ballerinax/azure.ai.search.index	1.0.2
ballerinax/azure.openai.chat	4.0.0
ballerinax/ai.deepseek	1.1.4
ballerinax/milvus	1.1.1
ballerinax/mistral	1.0.2
ballerinax/ai.ollama	1.2.4
ballerinax/openai.chat	5.0.0
ballerinax/openai.audio	3.0.0
ballerinax/openai.finetunes	3.0.0
ballerinax/ai.pgvector	1.0.5
ballerinax/pinecone.vector	1.0.2
ballerinax/weaviate	1.0.2
ballerinax/aws	1.0.1
ballerinax/aws.lambda	3.3.0
ballerinax/aws.marketplace.mpe	1.0.0
ballerinax/aws.marketplace.mpm	1.0.0
ballerinax/azure.functions	4.2.0
ballerinax/elastic.elasticcloud	1.0.1
ballerinax/aws.sns	4.0.1
ballerinax/discord	2.0.1
ballerinax/googleapis.gmail	4.2.0
ballerinax/slack	5.0.1
ballerinax/twilio	5.0.2
ballerinax/zoom.meetings	1.0.2
ballerinax/zoom.scheduler	1.0.2
ballerinax/salesforce	8.7.0
ballerinax/hubspot.automation.actions	2.0.0
ballerinax/hubspot.crm.associations	2.0.2
ballerinax/hubspot.crm.associations.schema	2.0.2
ballerinax/hubspot.crm.commerce.carts	2.0.2
ballerinax/hubspot.crm.commerce.discounts	2.0.2
ballerinax/hubspot.crm.commerce.orders	2.0.2
ballerinax/hubspot.crm.commerce.quotes	2.0.2
ballerinax/hubspot.crm.commerce.taxes	2.0.2
ballerinax/hubspot.crm.obj.companies	2.0.1
ballerinax/hubspot.crm.obj.contacts	1.0.2
ballerinax/hubspot.crm.obj.deals	1.0.2
ballerinax/hubspot.crm.engagement.meeting	2.0.0
ballerinax/hubspot.crm.engagement.notes	2.0.2
ballerinax/hubspot.crm.engagements.calls	2.0.2
ballerinax/hubspot.crm.engagements.communications	2.0.2
ballerinax/hubspot.crm.engagements.email	2.0.2
ballerinax/hubspot.crm.engagements.tasks	2.0.2
ballerinax/hubspot.crm.extensions.timelines	2.0.2
ballerinax/hubspot.crm.extensions.videoconferencing	2.0.2
ballerinax/hubspot.crm.obj.feedback	2.0.2
ballerinax/hubspot.crm.import	4.0.2
ballerinax/hubspot.crm.obj.leads	2.0.2
ballerinax/hubspot.crm.obj.lineitems	2.0.2
ballerinax/hubspot.crm.lists	1.0.2
ballerinax/hubspot.crm.owners	2.0.2
ballerinax/hubspot.crm.pipelines	2.0.2
ballerinax/hubspot.crm.obj.products	2.0.2
ballerinax/hubspot.crm.properties	2.0.2
ballerinax/hubspot.crm.obj.schemas	2.0.2
ballerinax/hubspot.crm.obj.tickets	2.0.2
ballerinax/mysql	1.19.0
ballerinax/postgresql	1.19.0
ballerinax/mssql	1.19.0
ballerinax/oracledb	1.17.0
ballerinax/mongodb	5.2.4
ballerinax/redis	3.4.1
ballerinax/aws.redshift	1.2.2
ballerinax/aws.redshiftdata	1.1.0
ballerinax/snowflake	2.2.2
ballerinax/java.jdbc	1.15.1
ballerinax/cdc	1.4.0
ballerinax/github	6.0.0
ballerinax/wso2.apim.catalog	1.3.0
ballerinax/copybook	1.1.0
ballerinax/amp	1.1.0
ballerinax/idetraceprovider	0.9.0
ballerinax/moesif	1.0.3
ballerinax/newrelic	1.0.3
ballerinax/shopify.admin	3.0.0
ballerinax/sap.commerce.webservices	0.9.1
ballerinax/sap	1.3.1
ballerinax/sap.s4hana.salesarea_0001	2.1.0
ballerinax/sap.s4hana.api_salesdistrict_srv	2.1.0
ballerinax/sap.s4hana.api_sales_inquiry_srv	2.1.0
ballerinax/sap.s4hana.api_sales_order_srv	2.1.0
ballerinax/sap.s4hana.ce_salesorder_0001	2.1.0
ballerinax/sap.s4hana.api_sales_order_simulation_srv	2.1.0
ballerinax/sap.s4hana.api_salesorganization_srv	2.1.0
ballerinax/sap.s4hana.api_sales_quotation_srv	2.1.0
ballerinax/sap.s4hana.api_sd_incoterms_srv	2.1.0
ballerinax/sap.s4hana.api_sd_sa_soldtopartydetn	2.1.0
ballerinax/guidewire.insnow	0.2.0
ballerinax/ibm.ctg	0.1.1
ballerinax/stripe	2.0.1
ballerinax/paypal.invoices	1.0.2
ballerinax/paypal.orders	2.0.2
ballerinax/paypal.payments	2.0.2
ballerinax/paypal.subscriptions	1.0.2
ballerinax/peoplehr	2.2.1
ballerinax/salesforce.marketingcloud	1.0.2
ballerinax/hubspot.marketing.campaigns	2.0.2
ballerinax/hubspot.marketing.emails	1.0.2
ballerinax/hubspot.marketing.events	1.0.2
ballerinax/hubspot.marketing.forms	1.0.2
ballerinax/hubspot.marketing.subscriptions	2.0.2
ballerinax/hubspot.marketing.transactional	1.0.2
ballerinax/mailchimp.marketing	1.0.2
ballerinax/mailchimp.transactional	1.0.2
ballerinax/twitter	5.0.1
ballerinax/kafka	4.6.5
ballerinax/rabbitmq	3.6.0
ballerinax/aws.sqs	5.0.0
ballerinax/asb	3.10.0
ballerinax/gcloud.pubsub	0.1.1
ballerinax/ibm.ibmmq	1.4.4
ballerinax/java.jms	1.2.1
ballerinax/nats	3.3.1
ballerinax/solace	0.4.0
ballerinax/confluent.cavroserdes	1.0.3
ballerinax/confluent.cregistry	0.4.5
ballerinax/googleapis.sheets	4.0.0
ballerinax/googleapis.calendar	3.2.1
ballerinax/googleapis.gcalendar	4.0.1
ballerinax/jira	2.0.2
ballerinax/asana	3.0.1
ballerinax/trello	2.0.1
ballerinax/smartsheet	1.0.2
ballerinax/docusign.dsadmin	2.0.0
ballerinax/candid	0.2.1
ballerinax/aws.secretmanager	0.4.1
ballerinax/scim	1.0.2
ballerinax/aws.s3	4.0.0
ballerinax/azure_storage_service	4.3.4
ballerinax/microsoft.onedrive	3.0.2
ballerinax/alfresco	2.0.2
ballerina/ai.eval	0.9.0
ballerina/ai.np	0.5.1
ballerinax/ai.agent	0.9.2
ballerinax/ai.aws.dynamodb	1.0.0
ballerinax/ai.azure	1.5.0
ballerinax/ai.googleapis.vertex	1.0.2
ballerinax/ai.memory.postgresql	1.0.0
ballerinax/ai.memory.redis	1.1.0
ballerinax/ai.microsoft.sharepoint	1.0.1
ballerinax/ai.milvus	1.0.4
ballerinax/ai.mistral	1.2.4
ballerinax/ai.openai	1.4.0
ballerinax/ai.openrouter	1.0.2
ballerinax/ai.pinecone	1.1.5
ballerinax/ai.sqlite	1.0.0
ballerinax/ai.weaviate	1.0.5
ballerina/auth	2.14.0
ballerina/avro	1.2.2
ballerina/cache	3.10.0
ballerina/constraint	1.7.0
ballerina/crypto	2.12.1
ballerina/data.csv	0.10.0
ballerina/data.jsondata	1.1.4
ballerina/data.xmldata	1.6.3
ballerina/data.yaml	0.8.0
ballerina/edi	1.6.0
ballerina/etl	0.8.0
ballerina/file	1.13.0
ballerina/io	1.8.1
ballerina/jballerina.java.arrays	1.6.1
ballerina/jwt	2.15.1
ballerina/ldap	1.4.0
ballerina/log	2.17.0
ballerina/math.vector	1.2.0
ballerina/messaging	1.0.0
ballerina/mime	2.12.2
ballerina/oauth2	2.15.0
ballerina/observe	1.7.1
ballerina/os	1.10.1
ballerina/otel	0.9.0
ballerina/pdf	0.9.1
ballerina/persist	1.7.0
ballerina/protobuf	1.8.0
ballerina/random	1.7.0
ballerina/regex	1.4.3
ballerina/serdes	0.2.0
ballerina/smb	2.0.1
ballerina/soap	2.3.1
ballerina/sql	1.19.0
ballerina/task	2.11.2
ballerina/time	2.8.1
ballerina/toml	0.8.0
ballerina/url	2.6.2
ballerina/uuid	1.10.0
ballerina/websubhub	1.16.0
ballerina/workflow	0.8.3
ballerina/xlsx	1.0.1
ballerina/xmldata	2.9.2
ballerina/xslt	2.9.1
ballerina/yaml	0.8.0
```

4. The original source code(ballerina-vscode) should provide in the user prompt, It can be upstream or a local one,. Dont guess, If user tell to render but didnt say from which soyrce code, kindly ask the user to provide the source code path. If user give two source paths, please clearly understand which one should add to the <library-folder>/old and which one should add to the <library-folder>/new. If user give only one source path, please clearly ask is this old or new.
5. Accuracy over speed. If you are not sure about the answer, ask the user for clarification. Do not make assumptions.
6. You should do the task with 100% completenss and 1005 accuracy
7. you should not update the versions of the libraries, or add/remove any libraries from the list, or update the renders by your own. but youcan ask if any confussions. If you are not sure about the versions or libraries, ask the user for clarification. Do not make assumptions.
