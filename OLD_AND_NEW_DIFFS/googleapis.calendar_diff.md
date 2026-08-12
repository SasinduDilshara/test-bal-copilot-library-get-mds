# googleapis.calendar — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `googleapis.calendar` |
| **Old file** | `googleapis.calendar/old/ballerinax_googleapis.calendar.bal.txt` |
| **New file** | `googleapis.calendar/new/ballerinax_googleapis.calendar.bal.txt` |
| **Old lines** | 804 |
| **New lines** | 878 |
| **Lines added** | 84 |
| **Lines removed** | 10 |
| **Hunks** | 17 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 5 | 5 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 89–94 | 89–95 | Types | +1 | −0 |
| 2 | 113–158 | 114–181 | Types | +22 | −0 |
| 3 | 161–170 | 184–196 | Types | +3 | −0 |
| 4 | 175–180 | 201–207 | Types | +1 | −0 |
| 5 | 184–193 | 211–223 | Types | +3 | −0 |
| 6 | 217–222 | 247–253 | Types | +1 | −0 |
| 7 | 225–234 | 256–268 | Types | +3 | −0 |
| 8 | 236–241 | 270–276 | Types | +1 | −0 |
| 9 | 244–249 | 279–285 | Types | +1 | −0 |
| 10 | 252–259 | 288–297 | Types | +2 | −0 |
| 11 | 262–269 | 300–309 | Types | +2 | −0 |
| 12 | 272–279 | 312–321 | Types | +2 | −0 |
| 13 | 282–287 | 324–330 | Types | +1 | −0 |
| 14 | 298–309 | 341–356 | Types | +4 | −0 |
| 15 | 681–690 | 728–740 | Types | +3 | −0 |
| 16 | 709–738 | 759–801 | Types | +13 | −0 |
| 17 | 747–794 | 810–868 | Client | +21 | −10 |

---

## Unified diff

`````diff
--- googleapis.calendar/old/ballerinax_googleapis.calendar.bal.txt	2026-08-12 12:57:30
+++ googleapis.calendar/new/ballerinax_googleapis.calendar.bal.txt	2026-08-12 13:19:19
@@ -89,6 +89,7 @@
 
 # Client configuration details.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|config:OAuth2RefreshTokenGrantConfig|http:JwtIssuerConfig auth; // Special Agent Note: BearerTokenConfig, JwtIssuerConfig FROM ballerina/http package, OAuth2RefreshTokenGrantConfig FROM ballerinax/client.config package
@@ -113,46 +114,68 @@
 
 type InputEvent record {
     # Title of the event
+    @display {label: "Event Title"}
     string summary?;
     # Description of the event
+    @display {label: "Event Description"}
     string description?;
     # Location of the event
+    @display {label: "Event Location"}
     string location?;
     # Color Id of the event
+    @display {label: "Event Color Id"}
     string colorId?;
     # Opaque identifier of the event
+    @display {label: "Event Id"}
     string id?;
+    @display {label: "Event Start Time"}
     Time 'start;
     # End time of the event
+    @display {label: "Event End Time"}
     Time end;
     # List of RRULE, EXRULE, RDATE and EXDATE lines for a recurring event, as specified in RFC5545
+    @display {label: "Recurrence Config"}
     string[] recurrence?;
     # The start time of the event in recurring events
+    @display {label: "Start Time in Recurrent Event"}
     Time originalStartTime?;
     # Whether the event blocks time on the calendar
+    @display {label: "Time Blocks Config"}
     string transparency?;
     # Visibility of the event
+    @display {label: "Event Visibility"}
     string visibility?;
     # Sequence number as per iCalendar
+    @display {label: "Sequence Number"}
     int sequence?;
     # The attendees of the event
+    @display {label: "Attendees List"}
     Attendee[] attendees?;
     # Properties of the event that appears on this calendar
+    @display {label: "Extended Config"}
     ExtendedProperties extendedProperties?;
     # The conference-related information
+    @display {label: "Conference Config"}
     ConferenceInputData conferenceData?;
     # Whether anyone can invite themselves to the event
+    @display {label: "Can Anyone Invite Themselves?"}
     boolean anyoneCanAddSelf?;
     # Whether attendees other than the organizer can invite others to the event
+    @display {label: "Can Guests Invite Others?"}
     boolean guestsCanInviteOthers?;
     # Whether attendees other than the organizer can modify the event
+    @display {label: "Can Guests Modify Event?"}
     boolean guestsCanModify?;
     # Whether attendees other than the organizer can see who the event's attendees are
+    @display {label: "Can Guests See Attendees?"}
     boolean guestsCanSeeOtherGuests?;
     # Information about the event's reminders
+    @display {label: "Reminder Config"}
     Reminders reminders?;
+    @display {label: "Event Source"}
     Source 'source?;
     # Attachments of the events
+    @display {label: "List of Attachments"}
     Attachment[] attachments?;
 };
 
@@ -161,10 +184,13 @@
 
 type Time record {
     # The date, in the format "yyyy-mm-dd"
+    @display {label: "Date"}
     string date?;
     # A combined date-time value formatted according to RFC3339
+    @display {label: "Date And Time"}
     string dateTime?;
     # The time zone in which the time is specified
+    @display {label: "Time Zone"}
     string timeZone?;
 };
 
@@ -175,6 +201,7 @@
     # The attendee's Profile ID
     string id?;
     # The attendee's email address
+    @display {label: "Email Address"}
     string email;
     # The attendee's name
     string displayName?;
@@ -184,10 +211,13 @@
     boolean self?;
     boolean 'resource?;
     # Whether this is an optional attendee
+    @display {label: "Is Optional"}
     boolean optional?;
     # The attendee's response status
+    @display {label: "Status"}
     string responseStatus?;
     # The attendee's response comment
+    @display {label: "Comment"}
     string comment?;
     # Number of additional guests
     int additionalGuests?;
@@ -217,6 +247,7 @@
 
 type ConferenceInputData record {
     # A request to generate a new conference and attach it to the event
+    @display {label: "Request to Generate Conference"}
     CreateRequest createRequest?;
 };
 
@@ -225,10 +256,13 @@
 
 type CreateRequest record {
     # The client-generated unique ID for this request
+    @display {label: "Request Id"}
     string requestId;
     # The conference solution
+    @display {label: "Conference Solution Type"}
     ConferenceSolutionKey conferenceSolutionKey;
     # The status of the conference create request
+    @display {label: "Request Status"}
     Status status?;
 };
 
@@ -236,6 +270,7 @@
 # 
 
 type ConferenceSolutionKey record {
+    @display {label: "Conference Type"}
     string 'type;
 };
 
@@ -244,6 +279,7 @@
 
 type Status record {
     # The current status of the conference create request
+    @display {label: "Request Status Code"}
     string statusCode;
 };
 
@@ -252,8 +288,10 @@
 
 type Reminders record {
     # Whether the default reminders of the calendar apply to the event
+    @display {label: "Use Default Reminder?"}
     boolean useDefault;
     # List the reminders specific to the event
+    @display {label: "Reminders List"}
     Reminder[] overrides?;
 };
 
@@ -262,8 +300,10 @@
 
 type Reminder record {
     # The method used by the reminder
+    @display {label: "Reminder Method"}
     string method;
     # Number of minutes before the start of the event when the reminder should trigger
+    @display {label: "Reminder Before (Mins)"}
     int minutes;
 };
 
@@ -272,8 +312,10 @@
 
 type Source record {
     # URL of the source pointing to a resource
+    @display {label: "Source Url"}
     string url;
     # Title of the source
+    @display {label: "Source Name"}
     string title;
 };
 
@@ -282,6 +324,7 @@
 
 type Attachment record {
     # URL link to the attachment
+    @display {label: "File Url"}
     string fileUrl;
     # Attachment title
     string title?;
@@ -298,12 +341,16 @@
 
 type EventsToAccess record {
     # Version number of conference data supported by the API client
+    @display {label: "Conference Data Version"}
     int? conferenceDataVersion?;
     # The maximum number of attendees to include in the response
+    @display {label: "Number of Attendees"}
     int? maxAttendees?;
     # Whether to send notifications about the creation of the new event
+    @display {label: "Notification Config"}
     string? sendUpdates?;
     # Whether API client performing operation supports event attachment
+    @display {label: "Attachment Config"}
     boolean? supportsAttachments?;
 };
 
@@ -681,10 +728,13 @@
 
 type CalendarsToAccess record {
     # The minimum access role for the user in the returned entries
+    @display {label: "Access Role of User"}
     string minAccessRole?;
     # Whether to include deleted calendar list entries in the result
+    @display {label: "Show Deleted Calendars"}
     boolean showDeleted?;
     # Whether to show hidden entries
+    @display {label: "Show Hidden Calendars"}
     boolean showHidden?;
 };
 
@@ -709,30 +759,43 @@
 
 type EventFilterCriteria record {
     # Event unique identifier
+    @display {label: "iCalUID"}
     string iCalUID?;
     # The maximum number of attendees to include in the response
+    @display {label: "Maximum Attendess"}
     int maxAttendees?;
     # The order of the events returned in the result
+    @display {label: "Order by"}
     OrderBy orderBy?;
     # Extended private properties constraint specified as propertyName=value
+    @display {label: "Private Extended Property"}
     string privateExtendedProperty?;
     # Free text search terms to find events that match these terms in any field, except for extended properties
+    @display {label: "Search Term"}
     string q?;
     # Extended shared properties constraint specified as propertyName=value
+    @display {label: "Shared Extended Property"}
     string sharedExtendedProperty?;
     # Whether to include deleted events (with status equals "cancelled") in the result
+    @display {label: "Show Deleted?"}
     boolean showDeleted?;
     # Whether to include hidden invitations in the result
+    @display {label: "Show Hidden Invitations?"}
     boolean showHiddenInvitations?;
     # Whether to expand recurring events into instances and only return single one-off events
+    @display {label: "Single Events?"}
     boolean singleEvents?;
     # Upper bound (exclusive) for an event's start time to filter by. Must be an RFC3339 timestamp
+    @display {label: "Start Time Max"}
     string timeMax?;
     # Lower bound (exclusive) for an event's end time to filter by. Must be an RFC3339 timestamp
+    @display {label: "Start Time Min"}
     string timeMin?;
     # Time zone used in the response
+    @display {label: "Time Zone"}
     string timeZone?;
     # Lower bound for an event's last modification time (as a RFC3339 timestamp) to filter by
+    @display {label: "Updated Time Min"}
     string updatedMin?;
 };
 
@@ -747,48 +810,59 @@
 # Ballerina Google Calendar connector provides the capability to access Google Calendar API.
 # The connector let you perform calendar and event management operations.
 # 
+@display {label: "Google Calendar", iconPath: "icon.png"}
 client class Client {
     function init(ConnectionConfig config) returns error?;
 
     # Gets calendars.
     # 
-    remote function getCalendars(CalendarsToAccess|() optional = (), string|() userAccount = ()) returns Calendar, error?>|error;
+    @display {label: "Get Calendars"}
+    remote function getCalendars(@display {label: "Calendars to Access"} CalendarsToAccess|() optional = (), @display {label: "User Account"} string|() userAccount = ()) returns stream<Calendar, error?>|error;
 
     # Creates a calendar.
     # 
-    remote function createCalendar(string title, string|() userAccount = ()) returns CalendarResource|error;
+    @display {label: "Create Calendar"}
+    remote function createCalendar(@display {label: "Calendar Name"} string title, @display {label: "User Account"} string|() userAccount = ()) returns CalendarResource|error;
 
     # Deletes a calendar.
     # 
-    remote function deleteCalendar(string calendarId, string|() userAccount = ()) returns error?;
+    @display {label: "Delete Calendar"}
+    remote function deleteCalendar(@display {label: "Calendar ID"} string calendarId, @display {label: "User Account"} string|() userAccount = ()) returns error?;
 
     # Creates an event.
     # 
-    remote function createEvent(string calendarId, InputEvent event, EventsToAccess|() optional = (), string|() userAccount = ()) returns Event|error;
+    @display {label: "Create Event"}
+    remote function createEvent(@display {label: "Calendar ID"} string calendarId, @display {label: "Event Details"} InputEvent event, @display {label: "Events to Access"} EventsToAccess|() optional = (), @display {label: "User Account"} string|() userAccount = ()) returns Event|error;
 
     # Creates an event at the moment with simple text.
     # 
-    remote function quickAddEvent(string calendarId, string text, string|() sendUpdates = (), string|() userAccount = ()) returns Event|error;
+    @display {label: "Create Quick Event"}
+    remote function quickAddEvent(@display {label: "Calendar ID"} string calendarId, @display {label: "Event Description"} string text, @display {label: "Send Creation Updates"} string|() sendUpdates = (), @display {label: "User Account"} string|() userAccount = ()) returns Event|error;
 
     # Updates an existing event.
     # 
-    remote function updateEvent(string calendarId, string eventId, InputEvent event, EventsToAccess|() optional = (), string|() userAccount = ()) returns Event|error;
+    @display {label: "Update Event"}
+    remote function updateEvent(@display {label: "Calendar ID"} string calendarId, @display {label: "Event ID"} string eventId, @display {label: "Event Details"} InputEvent event, @display {label: "Events to Access"} EventsToAccess|() optional = (), @display {label: "User Account"} string|() userAccount = ()) returns Event|error;
 
     # Gets events.
     # 
-    remote function getEvents(string calendarId, EventFilterCriteria|() filter = (), string|() userAccount = ()) returns Event, error?>|error;
+    @display {label: "Get Events"}
+    remote function getEvents(@display {label: "Calendar ID"} string calendarId, @display {label: "Filtering Criteria"} EventFilterCriteria|() filter = (), @display {label: "User Account"} string|() userAccount = ()) returns stream<Event, error?>|error;
 
     # Gets an event.
     # 
-    remote function getEvent(string calendarId, string eventId, string|() userAccount = ()) returns Event|error;
+    @display {label: "Get Event"}
+    remote function getEvent(@display {label: "Calendar ID"} string calendarId, @display {label: "Event ID"} string eventId, @display {label: "User Account"} string|() userAccount = ()) returns Event|error;
 
     # Deletes an event.
     # 
-    remote function deleteEvent(string calendarId, string eventId, string|() userAccount = ()) returns error?;
+    @display {label: "Delete Event"}
+    remote function deleteEvent(@display {label: "Calendar ID"} string calendarId, @display {label: "Event ID"} string eventId, @display {label: "User Account"} string|() userAccount = ()) returns error?;
 
     # Gets events response.
     # 
-    remote function getEventsResponse(string calendarId, int|() count = (), string|() pageToken = (), string|() syncToken = (), EventFilterCriteria|() filter = (), string|() userAccount = ()) returns EventResponse|error;
+    @display {label: "Get Events By Page"}
+    remote function getEventsResponse(@display {label: "Calendar ID"} string calendarId, @display {label: "Number of Events Required"} int|() count = (), @display {label: "Token for Next Page"} string|() pageToken = (), @display {label: "Token for Incremental Sync"} string|() syncToken = (), @display {label: "Filtering Criteria"} EventFilterCriteria|() filter = (), @display {label: "User Account"} string|() userAccount = ()) returns EventResponse|error;
 }
 
 // --- Functions ---
`````
