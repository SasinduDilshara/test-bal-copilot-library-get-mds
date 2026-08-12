# peoplehr — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `peoplehr` |
| **Old file** | `peoplehr/old/ballerinax_peoplehr.bal.txt` |
| **New file** | `peoplehr/new/ballerinax_peoplehr.bal.txt` |
| **Old lines** | 1345 |
| **New lines** | 1374 |
| **Lines added** | 53 |
| **Lines removed** | 24 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 65–73 | 65–75 | Types | +2 | −0 |
| 2 | 1236–1345 | 1238–1374 | Client | +51 | −24 |

---

## Unified diff

`````diff
--- peoplehr/old/ballerinax_peoplehr.bal.txt	2026-08-12 12:57:30
+++ peoplehr/new/ballerinax_peoplehr.bal.txt	2026-08-12 13:19:19
@@ -65,9 +65,11 @@
 
 # Client configuration details.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     never auth?;
     # PeopleHR API key
+    @display {label: "", kind: "password"}
     string apiKey;
     # Base URL
     string baseURL?;
@@ -1236,110 +1238,137 @@
 # This connector helps you easily integrate People with other systems and applications, for seamless cross-platform data sharing. The People API 
 # accepts and returns JSON data in the request body, with status indicating the outcome of the operation (sucess/failure).
 # 
+@display {label: "PeopleHR", iconPath: "icon.png"}
 client class Client {
     function init(ConnectionConfig config) returns error?;
 
     # Creates new employee
     # 
-    remote function createNewEmployee(NewEmployeeRequest|json payload) returns OperationStatus|error;
+    @display {label: "Create New Employee"}
+    remote function createNewEmployee(@display {label: "Employee Detail"} NewEmployeeRequest|json payload) returns OperationStatus|error;
 
     # Gets employee detail by id
     # 
-    remote function getEmployeeById(EmployeeRequest payload) returns EmployeeResponse|error;
+    @display {label: "Get Employee Detail By Id"}
+    remote function getEmployeeById(@display {label: "Employee Request Detail"} EmployeeRequest payload) returns EmployeeResponse|error;
 
     # Updates employee id.
     # 
-    remote function updateEmployeeId(EmployeeIdUpdateRequest payload) returns OperationStatus|error;
+    @display {label: "Update EmployeeId"}
+    remote function updateEmployeeId(@display {label: "Request Detail"} EmployeeIdUpdateRequest payload) returns OperationStatus|error;
 
     # Gets all employees.
     # 
-    remote function getAllEmployees(AllEmployeesRequest payload) returns EmployeesResponse|error;
+    @display {label: "Get All Employee Detail"}
+    remote function getAllEmployees(@display {label: "Request Detail"} AllEmployeesRequest payload) returns EmployeesResponse|error;
 
     # Updates employee details.
     # 
-    remote function updateEmployee(EmployeeUpdateRequest|json payload) returns OperationStatus|error;
+    @display {label: "Update Employee"}
+    remote function updateEmployee(@display {label: "Employee Detail"} EmployeeUpdateRequest|json payload) returns OperationStatus|error;
 
     # Updates/marks employee leaver status by id.
     # 
-    remote function markAsLeaverById(EmployeeLeaverStatus payload) returns OperationStatus|error;
+    @display {label: "Mark As Leaver By Id"}
+    remote function markAsLeaverById(@display {label: "Employee Detail"} EmployeeLeaverStatus payload) returns OperationStatus|error;
 
     # Gets employee salary details.
     # 
-    remote function getSalaryDetail(SalaryDetailRequest payload) returns SalaryDetailGetResponse|error;
+    @display {label: "Get Salary Detail"}
+    remote function getSalaryDetail(@display {label: "Request Detail"} SalaryDetailRequest payload) returns SalaryDetailGetResponse|error;
 
     # Add new holiday.
     # 
-    remote function addNewHoliday(NewHolidayRequest|json payload) returns OperationStatus|error;
+    @display {label: "Add New Holiday"}
+    remote function addNewHoliday(@display {label: "Holiday Detail"} NewHolidayRequest|json payload) returns OperationStatus|error;
 
     # Gets holiday detail list
     # 
-    remote function getHolidayDetail(HolidayDetail payload) returns HolidayGetResponse|error;
+    @display {label: "Get Holiday Detail"}
+    remote function getHolidayDetail(@display {label: "Holiday Detail"} HolidayDetail payload) returns HolidayGetResponse|error;
 
     # Deletes holiday detail
     # 
-    remote function deleteHoliday(HolidayDetail payload) returns OperationStatus|error;
+    @display {label: "Delete Holiday"}
+    remote function deleteHoliday(@display {label: "Holiday Detail"} HolidayDetail payload) returns OperationStatus|error;
 
     # Create new vacancy
     # 
-    remote function createNewVacancy(NewVacancy payload) returns OperationStatus|error;
+    @display {label: "Add new Vacancies"}
+    remote function createNewVacancy(@display {label: "New vacancy detail"} NewVacancy payload) returns OperationStatus|error;
 
     # Gets vacancy detail
     # 
-    remote function getVacancy(GetVacancyResultRequest|json payload) returns VacancyGetResponse|error;
+    @display {label: "Get Vacancy"}
+    remote function getVacancy(@display {label: "Request Detail"} GetVacancyResultRequest|json payload) returns VacancyGetResponse|error;
 
     # Gets all vacancy detail
     # 
+    @display {label: "Get Vacancies"}
     remote function getAllVacancies() returns AllVacancies|error;
 
     # Creates New Applicant
     # 
-    remote function createNewApplicant(NewApplicant payload) returns OperationStatus|error;
+    @display {label: "Create New Applicant"}
+    remote function createNewApplicant(@display {label: "New Applicant detail"} NewApplicant payload) returns OperationStatus|error;
 
     # Upload applicant document
     # 
-    remote function uploadApplicantDocument(NewDocument payload) returns OperationStatus|error;
+    @display {label: "Upload new applicant document"}
+    remote function uploadApplicantDocument(@display {label: "New applicant document"} NewDocument payload) returns OperationStatus|error;
 
     # Checks duplicate applicant
     # 
-    remote function checkDuplicateApplicant(ApplicantInformation payload) returns OperationStatus|error;
+    @display {label: "Check duplicate applicant"}
+    remote function checkDuplicateApplicant(@display {label: "Applicant detail"} ApplicantInformation payload) returns OperationStatus|error;
 
     # Gets query result By query name details.
     # 
-    remote function getQueryByName(QueryResultGetRequest payload) returns QueryDetail|error;
+    @display {label: "Get Query Result By Query Name"}
+    remote function getQueryByName(@display {label: "Request Detail on Query Result"} QueryResultGetRequest payload) returns QueryDetail|error;
 
     # Checks if credentials of a given login user is valid.
     # 
-    remote function checkAuthentication(AuthenticationInfo payload) returns AuthenticationResponse|error;
+    @display {label: "Check Authentication"}
+    remote function checkAuthentication(@display {label: "Authentication Detail"} AuthenticationInfo payload) returns AuthenticationResponse|error;
 
     # Retrieves employee screen detail
     # 
+    @display {label: "Get Employee Screen Detail"}
     remote function getEmployeeScreenDetail() returns EmployeeScreenDetailResponse|error;
 
     # Retrieves employee screen detail by employee ID
     # 
-    remote function getEmployeeScreenDetailByEmployeeID(ScreenDetailByEmployeeIDRequest payload) returns EmployeeScreenDetailResponse|error;
+    @display {label: "Get Employee Screen Detail by employee ID"}
+    remote function getEmployeeScreenDetailByEmployeeID(@display {label: "Employee Screen Detail Request Info"} ScreenDetailByEmployeeIDRequest payload) returns EmployeeScreenDetailResponse|error;
 
     # Retrieves employee screen detail by transaction ID
     # 
-    remote function getEmployeeScreenDetailByTransactionID(ScreenDetailByTransactionIDRequest payload) returns EmployeeScreenDetailResponse|error;
+    @display {label: "Get Employee Screen Detail by transaction ID"}
+    remote function getEmployeeScreenDetailByTransactionID(@display {label: "Employee Screen Detail Request Info"} ScreenDetailByTransactionIDRequest payload) returns EmployeeScreenDetailResponse|error;
 
     # New custom screen transaction details
     # 
-    remote function addNewCustomScreenTransaction(NewCustomScreenTransactionDetails payload) returns OperationStatus|error;
+    @display {label: "Add Employee Screen Detail by employee ID"}
+    remote function addNewCustomScreenTransaction(@display {label: "New Custom Screen Details"} NewCustomScreenTransactionDetails payload) returns OperationStatus|error;
 
     # Update custom screen transaction details
     # 
-    remote function updateCustomScreenTransaction(ExistingCustomScreenTransactionDetails payload) returns OperationStatus|error;
+    @display {label: "Update Employee Screen Detail"}
+    remote function updateCustomScreenTransaction(@display {label: "Custom Screen Details"} ExistingCustomScreenTransactionDetails payload) returns OperationStatus|error;
 
     # Delete custom screen transaction details
     # 
-    remote function DeleteCustomScreenTransaction(ScreenDetailByTransactionIDRequest payload) returns OperationStatus|error;
+    @display {label: "Delete Employee Screen Detail"}
+    remote function DeleteCustomScreenTransaction(@display {label: "Custom Screen Details"} ScreenDetailByTransactionIDRequest payload) returns OperationStatus|error;
 
     # Retrieves By Employee Id Appraisal details
     # 
-    remote function getAppraisalDetailsByEmployeeID(AppraisalDetailsRequest payload) returns AppraisalDetailsResponse|error;
+    @display {label: "Get Appraisal details by employee ID"}
+    remote function getAppraisalDetailsByEmployeeID(@display {label: "Employee Details"} AppraisalDetailsRequest payload) returns AppraisalDetailsResponse|error;
 
     # Retrieves appraisal details by appraisal Id
     # 
-    remote function getAppraisalDetailsByAppraisalID(AppraisalDetailsByAppraisalIDRequest payload) returns AppraisalDetailsResponse|error;
+    @display {label: "Get Appraisal details by employee ID"}
+    remote function getAppraisalDetailsByAppraisalID(@display {label: "Employee Details"} AppraisalDetailsByAppraisalIDRequest payload) returns AppraisalDetailsResponse|error;
 }
`````
