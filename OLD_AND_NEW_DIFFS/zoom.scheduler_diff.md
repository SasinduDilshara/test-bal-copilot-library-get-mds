# zoom.scheduler — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `zoom.scheduler` |
| **Old file** | `zoom.scheduler/old/ballerinax_zoom.scheduler.bal.txt` |
| **New file** | `zoom.scheduler/new/ballerinax_zoom.scheduler.bal.txt` |
| **Old lines** | 1419 |
| **New lines** | 1673 |
| **Lines added** | 268 |
| **Lines removed** | 14 |
| **Hunks** | 42 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (3)

- `type InlineResponse2011CustomFieldsAnswerchoicesItemsString`
- `type SchedulerschedulesCustomFieldsAnswerchoicesItemsString`
- `type SchedulerschedulesscheduleIdCustomFieldsAnswerchoicesItemsString`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 206–216 | 206–220 | Types | +4 | −0 |
| 2 | 250–255 | 254–260 | Types | +1 | −0 |
| 3 | 258–268 | 263–277 | Types | +4 | −0 |
| 4 | 300–319 | 309–332 | Types | +4 | −0 |
| 5 | 323–383 | 336–415 | Types | +20 | −1 |
| 6 | 386–399 | 418–434 | Types | +3 | −0 |
| 7 | 403–418 | 438–457 | Types | +5 | −1 |
| 8 | 451–490 | 490–542 | Types | +13 | −0 |
| 9 | 495–512 | 547–570 | Types | +6 | −0 |
| 10 | 525–538 | 583–599 | Types | +3 | −0 |
| 11 | 542–557 | 603–622 | Types | +5 | −1 |
| 12 | 563–573 | 628–640 | Types | +2 | −0 |
| 13 | 613–623 | 680–694 | Types | +4 | −0 |
| 14 | 650–655 | 721–727 | Types | +1 | −0 |
| 15 | 659–664 | 731–737 | Types | +1 | −0 |
| 16 | 678–685 | 751–761 | Types | +3 | −0 |
| 17 | 705–740 | 781–830 | Types | +14 | −0 |
| 18 | 743–804 | 833–917 | Types | +23 | −0 |
| 19 | 810–817 | 923–932 | Types | +2 | −0 |
| 20 | 819–824 | 934–940 | Types | +1 | −0 |
| 21 | 832–840 | 948–959 | Types | +3 | −0 |
| 22 | 845–862 | 964–987 | Types | +6 | −0 |
| 23 | 865–882 | 990–1015 | Types | +8 | −0 |
| 24 | 884–911 | 1017–1056 | Types | +12 | −0 |
| 25 | 913–918 | 1058–1064 | Types | +1 | −0 |
| 26 | 920–925 | 1066–1072 | Types | +1 | −0 |
| 27 | 927–932 | 1074–1080 | Types | +1 | −0 |
| 28 | 934–943 | 1082–1094 | Types | +3 | −0 |
| 29 | 946–951 | 1097–1103 | Types | +1 | −0 |
| 30 | 957–965 | 1109–1120 | Types | +3 | −0 |
| 31 | 980–985 | 1135–1141 | Types | +1 | −0 |
| 32 | 989–1073 | 1145–1256 | Types | +27 | −0 |
| 33 | 1093–1104 | 1276–1289 | Types | +2 | −0 |
| 34 | 1106–1111 | 1291–1297 | Types | +1 | −0 |
| 35 | 1114–1119 | 1300–1306 | Types | +1 | −0 |
| 36 | 1128–1142 | 1315–1333 | Types | +4 | −0 |
| 37 | 1144–1204 | 1335–1416 | Types | +21 | −0 |
| 38 | 1207–1238 | 1419–1461 | Types | +11 | −0 |
| 39 | 1242–1253 | 1465–1479 | Types | +3 | −0 |
| 40 | 1259–1343 | 1485–1597 | Types | +28 | −0 |
| 41 | 1351–1361 | 1605–1615 | Client | +2 | −2 |
| 42 | 1375–1413 | 1629–1667 | Client | +9 | −9 |

---

## Unified diff

`````diff
--- zoom.scheduler/old/ballerinax_zoom.scheduler.bal.txt	2026-08-12 12:57:30
+++ zoom.scheduler/new/ballerinax_zoom.scheduler.bal.txt	2026-08-12 13:19:20
@@ -206,11 +206,15 @@
     # The default availability schedule in use
     boolean default?;
     # The name of this availability schedule
+    @constraint:String {minLength: 1}
     string name;
     # The unique ID of availability
+    @jsondata:Name {value: "availability_id"}
     string availabilityId?;
+    @jsondata:Name {value: "segments_recurrence"}
     ScheduleravailabilitySegmentsRecurrence segmentsRecurrence?;
     # The timezone for which this availability schedule originates
+    @jsondata:Name {value: "time_zone"}
     string timeZone;
     # The date on which the rule needs to be applied outside of the availability rule
     ScheduleravailabilitySegments[] segments?;
@@ -250,6 +254,7 @@
     # This field indicates if you created the schedule. The field is read-only
     boolean self?;
     # This field indicates the creator of the display name
+    @jsondata:Name {value: "display_name"}
     string displayName?;
     # This field indicates the creator's email address
     string email?;
@@ -258,11 +263,15 @@
 
 type InlineResponse2005AvailabilityRules record {
     # This field indicates the use of custom availability instead of the rule
+    @jsondata:Name {value: "use_custom"}
     boolean useCustom?;
     # The ID of this availability rule. 
+    @jsondata:Name {value: "availability_id"}
     string availabilityId?;
+    @jsondata:Name {value: "segments_recurrence"}
     SchedulerschedulesscheduleIdSegmentsRecurrence1 segmentsRecurrence?;
     # The timezone of this availability rule. 
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
     # The owner of this availability rule. 
     string email?;
@@ -300,20 +309,24 @@
 
 type SchedulesSingleUseLinkBody record {
     # The unique identifier of a schedule
+    @jsondata:Name {value: "schedule_id"}
     string scheduleId;
 };
 
 
 type SchedulerschedulesCustomFields record {
     # The invitee's option(s) for `single_select` or `multi_select` type of responses
+    @jsondata:Name {value: "answer_choices"}
     SchedulerschedulesCustomFieldsAnswerchoicesItemsString[] answerChoices?;
     # The ID of this question
+    @jsondata:Name {value: "custom_field_id"}
     string customFieldId?;
     # The type of response that the invitee provides to the custom question. It can be one or multiple lines of text, a phone number, or single- or multiple-select.[`string text phone_number single_select multi_select`]
     "text"|"string"|"phone_number"|"choices_one"|"choices_many"|"select" format;
     # The custom question the host created for the event type
     string name;
     # This field is true if the custom question allows invitees to record a written response in addition to single-select or multiple-select type of responses. This field is false if the custom question does not allow invitees to record a written response
+    @jsondata:Name {value: "include_other"}
     boolean includeOther;
     # The position of this question
     decimal position;
@@ -323,61 +336,80 @@
     boolean required;
 };
 
-// Unknown type: SchedulerschedulesCustomFieldsAnswerchoicesItemsString
+type SchedulerschedulesCustomFieldsAnswerchoicesItemsString string;
 
 # Represents the Queries record for the operation: get_scheduled_events
 
 type GetScheduledEventsQueries record {
     # This field indicates whether the admin handles certain users. It's only for admin
+    @http:Query {name: "user_id"}
     string userId?;
 };
 
 
 type SchedulesscheduleIdBody record {
     # The method of `addOn`, such as Zoom meeting, Zoom phone, and offline
+    @jsondata:Name {value: "add_on_type"}
     "zoomMeeting"|"zoomPhone"|"offline" addOnType?;
     # The schedule's end date
+    @jsondata:Name {value: "end_date"}
     string endDate?;
     # This field sets the frequency of available time slots for invitees
+    @jsondata:Name {value: "start_time_increment"}
     decimal startTimeIncrement?;
     # The event's summary
+    @constraint:String {maxLength: 256}
     string summary?;
     # The hexadecimal color value of the event type's scheduling page
     string color?;
     # The custom question
+    @jsondata:Name {value: "custom_fields"}
     SchedulerschedulesscheduleIdCustomFields[] customFields?;
     # The schedule's description
+    @constraint:String {maxLength: 8192}
     string description?;
     # This field indicates if the schedule is active
     boolean active?;
     # This field sets the maximum events allowed per day
+    @jsondata:Name {value: "booking_limit"}
     decimal bookingLimit?;
     # This field indicates if the event type is hidden on the owner's main scheduling page
     boolean secret?;
     # the timezone of this availability rule. 
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
     # The availability time rule
+    @jsondata:Name {value: "availability_rules"}
     SchedulerschedulesscheduleIdAvailabilityRules[] availabilityRules?;
     # The maximum invitees per event
+    @constraint:Number {minValue: 1, maxValue: 200}
     decimal capacity?;
     # The available time segments of the event
     SchedulerschedulesSegments[] segments?;
     # The duration of meeting in minutes, range: [1, 1440]
+    @constraint:Number {minValue: 15, maxValue: 1440}
     decimal duration?;
     # The minimum time before a schedule starts that attendees can book
+    @constraint:Number {minValue: 0, maxValue: 14340}
     decimal cushion?;
     # The information for a custom location
+    @constraint:String {maxLength: 1024}
     string location?;
     # The extra time before or after booked schedule
     SchedulerschedulesscheduleIdBuffer buffer?;
+    @jsondata:Name {value: "segments_recurrence"}
     SchedulerschedulesscheduleIdSegmentsRecurrence1 segmentsRecurrence?;
     # The event portion of the event's URL that identifies a specific web page
+    @constraint:String {maxLength: 256, minLength: 3}
     string slug?;
     # The schedule time range. Unlimited means forever and fixed means using `startDate` and `endDate`
+    @jsondata:Name {value: "interval_type"}
     "unlimited"|"fixed" intervalType?;
     # This field indicates the use of the availability rule
+    @jsondata:Name {value: "availability_override"}
     boolean availabilityOverride?;
     # The schedule's start date
+    @jsondata:Name {value: "start_date"}
     string startDate?;
     # The status of schedule, confirmed or cancelled
     "confirmed"|"cancelled" status?;
@@ -386,14 +418,17 @@
 
 type SchedulerschedulesscheduleIdCustomFields record {
     # The invitee's option(s) for single_select or multi_select type of responses
+    @jsondata:Name {value: "answer_choices"}
     SchedulerschedulesscheduleIdCustomFieldsAnswerchoicesItemsString[] answerChoices?;
     # The type of response that the invitee provides to the custom question. It can be one or multiple lines of text, a phone number, or single- or multiple-select.[`string text phone_number single_select multi_select`]
     "text"|"string"|"phone_number"|"choices_one"|"choices_many"|"select" format;
     # The ID of this question
+    @jsondata:Name {value: "custom_field_id"}
     string customFieldId?;
     # The custom question that the host created for the event type
     string name;
     # If the custom question lets invitees record a written response, in addition to single-select or multiple-select type of responses, then it's true. Otherwise, it's false
+    @jsondata:Name {value: "include_other"}
     boolean includeOther;
     # The position of this question
     decimal position;
@@ -403,16 +438,20 @@
     boolean required;
 };
 
-// Unknown type: SchedulerschedulesscheduleIdCustomFieldsAnswerchoicesItemsString
+type SchedulerschedulesscheduleIdCustomFieldsAnswerchoicesItemsString string;
 
 
 type SchedulerschedulesscheduleIdAvailabilityRules record {
     # This field indicates whether to use the custom availability instead of the rule
+    @jsondata:Name {value: "use_custom"}
     boolean useCustom?;
     # The ID of this availability rule. 
+    @jsondata:Name {value: "availability_id"}
     string availabilityId?;
+    @jsondata:Name {value: "segments_recurrence"}
     SchedulerschedulesscheduleIdSegmentsRecurrence segmentsRecurrence?;
     # The timezone of this availability rule. 
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
     # The owner of this availability rule. 
     string email?;
@@ -451,40 +490,53 @@
 
 type SchedulerschedulesscheduleIdBuffer record {
     # This field adds time after the booked schedule
+    @constraint:Number {minValue: 0, maxValue: 240}
     decimal before?;
     # This field adds time before the booked schedule
+    @constraint:Number {minValue: 0, maxValue: 240}
     decimal after?;
 };
 
 
 type InlineResponse2003Items record {
     # The event's summary
+    @constraint:String {maxLength: 256}
     string summary?;
     # The attendees of the event
     InlineResponse2003Attendees[] attendees?;
     # The meeting notes of the event
+    @jsondata:Name {value: "meeting_notes"}
     string meetingNotes?;
     # The event's description
+    @constraint:String {maxLength: 8192}
     string description?;
     # The scheduled event end date time
+    @jsondata:Name {value: "end_date_time"}
     string endDateTime?;
     # The unique identifier of event
+    @jsondata:Name {value: "event_id"}
     string eventId?;
     # This field indicates the type is default(scheduled) or pending event
+    @jsondata:Name {value: "event_type"}
     "default"|"pending" eventType?;
     # The information to track the source of invitee. This occurs when you add UTM parameters in schedule links
+    @jsondata:Name {value: "tracking_params"}
     InlineResponse2003TrackingParams[] trackingParams?;
     # The guest's collection
     string[] guests?;
     # The information for a custom location
+    @constraint:String {maxLength: 1024}
     string location?;
     # The scheduled event start date time
+    @jsondata:Name {value: "start_date_time"}
     string startDateTime?;
     # The unique identifier of schedule
+    @jsondata:Name {value: "schedule_id"}
     string scheduleId?;
     # The moment the event was updated
     string updated?;
     # The meeting details for when users have scheduled appointments
+    @jsondata:Name {value: "external_location"}
     record {|string kind?; string meeting_id?; string personal_meeting_id?; string meeting_passcode?; string meeting_description?; string meeting_join_url?; anydata...;|} externalLocation?;
     # The status of event: confirmed or cancelled
     "confirmed"|"cancelled" status?;
@@ -495,18 +547,24 @@
     # This field indicates when the attendee attended this event
     string created?;
     # The ID of attendee
+    @jsondata:Name {value: "attendee_id"}
     string attendeeId?;
     # The attendee's last name
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     # The attendee's name
+    @jsondata:Name {value: "display_name"}
     string displayName?;
     # The attendee's time zone
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
     # Whether to show events or not
+    @jsondata:Name {value: "no_show"}
     boolean noShow?;
     # Whether the attendee is the booker
     boolean booker?;
     # The attendee's first name
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     # The attendee's email
     string email?;
@@ -525,14 +583,17 @@
 
 type InlineResponse2011CustomFields record {
     # The invitee's option(s) for single_select or multi_select type of responses
+    @jsondata:Name {value: "answer_choices"}
     InlineResponse2011CustomFieldsAnswerchoicesItemsString[] answerChoices?;
     # The ID of this question
+    @jsondata:Name {value: "custom_field_id"}
     string customFieldId?;
     # The type of response that the invitee provides to the custom question. It can be one or multiple lines of text, a phone number, or single- or multiple-select.[`string text phone_number single_select multi_select`]
     "text"|"string"|"phone_number"|"choices_one"|"choices_many"|"select" format;
     # The custom question the host created for the event type
     string name;
     # This field is true if the custom question allows invitees to record a written response in addition to single-select or multiple-select type of responses. This field is false if the custom question does not allow invitees to record a written response
+    @jsondata:Name {value: "include_other"}
     boolean includeOther;
     # The position of this question
     decimal position;
@@ -542,16 +603,20 @@
     boolean required;
 };
 
-// Unknown type: InlineResponse2011CustomFieldsAnswerchoicesItemsString
+type InlineResponse2011CustomFieldsAnswerchoicesItemsString string;
 
 
 type InlineResponse2006AvailabilityRules record {
     # This field indicates the use of custom availability instead of the rule
+    @jsondata:Name {value: "use_custom"}
     boolean useCustom?;
     # The ID of this availability rule. 
+    @jsondata:Name {value: "availability_id"}
     string availabilityId?;
+    @jsondata:Name {value: "segments_recurrence"}
     InlineResponse2006SegmentsRecurrence segmentsRecurrence?;
     # The timezone of this availability rule. 
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
     # The owner of this availability rule. 
     string email?;
@@ -563,11 +628,13 @@
 
 type GetScheduleQueries record {
     # This field indicates that admins handle certain users. This setting is only for admin
+    @http:Query {name: "user_id"}
     string userId?;
 };
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|http:OAuth2RefreshTokenGrantConfig auth; // Special Agent Note: BearerTokenConfig, OAuth2RefreshTokenGrantConfig FROM ballerina/http package
@@ -613,11 +680,15 @@
 
 type InlineResponse2011AvailabilityRules record {
     # This field indicates the use of custom availability instead of the rule
+    @jsondata:Name {value: "use_custom"}
     boolean useCustom?;
     # The ID of this availability rule. 
+    @jsondata:Name {value: "availability_id"}
     string availabilityId?;
+    @jsondata:Name {value: "segments_recurrence"}
     SchedulerschedulesSegmentsRecurrence segmentsRecurrence?;
     # The timezone of this availability rule. 
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
     # The owner of this availability rule. 
     string email?;
@@ -650,6 +721,7 @@
     # This field indicates if this user is the organizer. This field is read-only
     boolean self?;
     # The organizer's display name
+    @jsondata:Name {value: "display_name"}
     string displayName?;
     # The organizer's email address
     string email?;
@@ -659,6 +731,7 @@
 
 type InsertScheduleQueries record {
     # This field indicates that the admin handles certain users. This setting is only for admin
+    @http:Query {name: "user_id"}
     string userId?;
 };
 
@@ -678,8 +751,11 @@
     string owner?;
     boolean default?;
     string name?;
+    @jsondata:Name {value: "availability_id"}
     string availabilityId?;
+    @jsondata:Name {value: "segments_recurrence"}
     InlineResponse2001SegmentsRecurrence segmentsRecurrence?;
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
 };
 
@@ -705,36 +781,50 @@
 
 type InlineResponse200PreviousPeriod record {
     # The number of "all host available" type schedules
+    @jsondata:Name {value: "all_host_available"}
     int allHostAvailable?;
     # The number of rescheduled scheduled events
+    @jsondata:Name {value: "scheduled_events_rescheduled"}
     int scheduledEventsRescheduled?;
     # The number of completed scheduled events
+    @jsondata:Name {value: "scheduled_events_completed"}
     int scheduledEventsCompleted?;
     # The number of cancelled schedules
+    @jsondata:Name {value: "schedules_canceled"}
     int schedulesCanceled?;
     # The number of "one-off" type schedules
+    @jsondata:Name {value: "one_off_meeting"}
     int oneOffMeeting?;
     # The number of "meeting poll" type schedules
+    @jsondata:Name {value: "meeting_poll"}
     int meetingPoll?;
     # The number of "one to many" type schedules
+    @jsondata:Name {value: "one_to_many"}
     int oneToMany?;
     # The number of "any host available" type schedules
+    @jsondata:Name {value: "any_host_available"}
     int anyHostAvailable?;
     # The number of cancelled scheduled events
+    @jsondata:Name {value: "scheduled_events_canceled"}
     int scheduledEventsCanceled?;
     # The number of "one to one" type schedules
+    @jsondata:Name {value: "one_to_one"}
     int oneToOne?;
     # The number of created scheduled events
+    @jsondata:Name {value: "scheduled_events_created"}
     int scheduledEventsCreated?;
     # The number of created schedules
+    @jsondata:Name {value: "schedules_created"}
     int schedulesCreated?;
 };
 
 
 type SchedulereventseventIdAttendees record {
     # The ID of attendee
+    @jsondata:Name {value: "attendee_id"}
     string attendeeId?;
     # This field inidcates the attendee if shown in the scheduled event
+    @jsondata:Name {value: "no_show"}
     boolean noShow?;
     # The attendee's email
     string email?;
@@ -743,62 +833,85 @@
 
 type SchedulerSchedulesBody record {
     # The method of the type of `addOn`, such as Zoom meeting, Zoom phone, or offline
+    @jsondata:Name {value: "add_on_type"}
     "zoomMeeting"|"zoomPhone"|"offline" addOnType?;
     # The schedule's end date
+    @jsondata:Name {value: "end_date"}
     string endDate?;
     # This field sets the frequency of available time slots for invitees
+    @jsondata:Name {value: "start_time_increment"}
     decimal startTimeIncrement?;
     # The event's summary
+    @constraint:String {maxLength: 256}
     string summary?;
     # This field indicates if the schedule type is "one" (belongs to an individual user) or "multiple"
+    @jsondata:Name {value: "schedule_type"}
     "one"|"multiple" scheduleType?;
     # The hexadecimal color value of the event type's scheduling page
     string color?;
     # This field contains the custom question
+    @jsondata:Name {value: "custom_fields"}
     SchedulerschedulesCustomFields[] customFields?;
     # The schedule's description
+    @constraint:String {maxLength: 8192}
     string description?;
     # This field indicates if the schedule is active
     boolean active?;
     # This field sets the maximum events allowed per day
+    @jsondata:Name {value: "booking_limit"}
     decimal bookingLimit?;
     # This field indicates if the event type is hidden on the owner's main scheduling page
     boolean secret?;
     # The timezone of this availability rule. 
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
     # The availability of the time rule
+    @jsondata:Name {value: "availability_rules"}
     SchedulerschedulesAvailabilityRules[] availabilityRules;
     # This field indicates the maximum invitees per event
+    @constraint:Number {minValue: 1, maxValue: 200}
     decimal capacity;
     # The available time segments of the event
     SchedulerschedulesSegments[] segments?;
     # This field indicates the duration of the meeting in minutes, range: [1, 1440]
+    @constraint:Number {minValue: 15, maxValue: 1440}
     decimal duration?;
     # This field indicates the minimum time before a schedule starts when the attendees can book
+    @constraint:Number {minValue: 0, maxValue: 14340}
     decimal cushion?;
     # The information for a custom location
+    @constraint:String {maxLength: 1024}
     string location?;
     # This field indicates the extra time before or after the booked schedule
     SchedulerschedulesBuffer buffer?;
+    @jsondata:Name {value: "segments_recurrence"}
     SchedulerschedulesSegmentsRecurrence segmentsRecurrence?;
     # The schedule time range. Unlimited means forever and fixed means using `startDate` and `endDate`
+    @jsondata:Name {value: "interval_type"}
     "unlimited"|"fixed" intervalType?;
     # The event portion of the event's URL that identifies a specific web page
+    @constraint:String {maxLength: 256, minLength: 3}
     string slug?;
     # This field indicates the use of the availability rule
+    @jsondata:Name {value: "availability_override"}
     boolean availabilityOverride;
     # The schedule's start date
+    @jsondata:Name {value: "start_date"}
     string startDate?;
 };
 
 
 type SchedulerschedulesAvailabilityRules record {
     # This field indicates the use of custom availability instead of the rule
+    @jsondata:Name {value: "use_custom"}
     boolean useCustom?;
     # The ID of this availability rule. 
+    @jsondata:Name {value: "availability_id"}
     string availabilityId?;
+    @jsondata:Name {value: "segments_recurrence"}
     SchedulerschedulesSegmentsRecurrence segmentsRecurrence?;
     # the timezone of this availability rule. 
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
     # The owner of this availability rule. 
     string email?;
@@ -810,8 +923,10 @@
 
 type SchedulerschedulesBuffer record {
     # This field adds the time after the booked schedule
+    @constraint:Number {minValue: 0, maxValue: 240}
     decimal before?;
     # This field adds the time before the booked schedule
+    @constraint:Number {minValue: 0, maxValue: 240}
     decimal after?;
 };
 
@@ -819,6 +934,7 @@
 
 type PatchScheduledEventsQueries record {
     # This field indicates whether the admin handles certain users. It's only for admin
+    @http:Query {name: "user_id"}
     string userId?;
 };
 
@@ -832,9 +948,12 @@
     # The name of this availability schedule
     string name?;
     # The unique ID of the availability
+    @jsondata:Name {value: "availability_id"}
     string availabilityId?;
+    @jsondata:Name {value: "segments_recurrence"}
     ScheduleravailabilitySegmentsRecurrence segmentsRecurrence?;
     # The timezone for which this availability schedule originates
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
     # The date on which the rule needs to be applied outside of the availability rule
     record {|anydata...;|}[] segments?;
@@ -845,18 +964,24 @@
     # This field indicates when the attendee attended this event
     string created?;
     # The ID of attendee
+    @jsondata:Name {value: "attendee_id"}
     string attendeeId?;
     # The attendee's last name
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     # The attendee's name
+    @jsondata:Name {value: "display_name"}
     string displayName?;
     # The attendee's time zone
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
     # Whether or not to show the event
+    @jsondata:Name {value: "no_show"}
     boolean noShow?;
     # Whether the attendee is the booker
     boolean booker?;
     # The attendee's first name
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     # The attendee's email
     string email?;
@@ -865,18 +990,26 @@
 
 type InlineResponse200 record {
     # The most popular schedules in the given time range
+    @jsondata:Name {value: "popular_schedules"}
     record {|anydata...;|}[] popularSchedules?;
     # The users with the least scheduled events
+    @jsondata:Name {value: "users_with_least_events"}
     record {|anydata...;|}[] usersWithLeastEvents?;
+    @jsondata:Name {value: "last_n_days"}
     InlineResponse200LastNDays lastNDays?;
     # The distribution of number of events scheduled in a day
+    @jsondata:Name {value: "popular_time_of_day"}
     record {|anydata...;|}[] popularTimeOfDay?;
+    @jsondata:Name {value: "previous_period"}
     InlineResponse200PreviousPeriod previousPeriod?;
     # The event distribution by duration
+    @jsondata:Name {value: "event_distribution_by_duration"}
     record {|anydata...;|}[] eventDistributionByDuration?;
     # The distribution of number of events scheduled in a week
+    @jsondata:Name {value: "popular_time_of_week"}
     record {|anydata...;|}[] popularTimeOfWeek?;
     # The users with the most scheduled events
+    @jsondata:Name {value: "users_with_most_events"}
     record {|anydata...;|}[] usersWithMostEvents?;
 };
 
@@ -884,28 +1017,40 @@
 
 type InlineResponse200LastNDays record {
     # The number of "all host available" type schedules
+    @jsondata:Name {value: "all_host_available"}
     int allHostAvailable?;
     # The number of rescheduled scheduled events
+    @jsondata:Name {value: "scheduled_events_rescheduled"}
     int scheduledEventsRescheduled?;
     # The number of completed scheduled events
+    @jsondata:Name {value: "scheduled_events_completed"}
     int scheduledEventsCompleted?;
     # The number of cancelled schedules
+    @jsondata:Name {value: "schedules_canceled"}
     int schedulesCanceled?;
     # The number of "one-off" type schedules
+    @jsondata:Name {value: "one_off_meeting"}
     int oneOffMeeting?;
     # The number of "meeting poll" type schedules
+    @jsondata:Name {value: "meeting_poll"}
     int meetingPoll?;
     # The number of "one to many" type schedules
+    @jsondata:Name {value: "one_to_many"}
     int oneToMany?;
     # The number of "any host available" type schedules
+    @jsondata:Name {value: "any_host_available"}
     int anyHostAvailable?;
     # The number of cancelled scheduled events
+    @jsondata:Name {value: "scheduled_events_canceled"}
     int scheduledEventsCanceled?;
     # The number of "one to one" type schedules
+    @jsondata:Name {value: "one_to_one"}
     int oneToOne?;
     # The number of created scheduled events
+    @jsondata:Name {value: "scheduled_events_created"}
     int scheduledEventsCreated?;
     # The number of created schedules
+    @jsondata:Name {value: "schedules_created"}
     int schedulesCreated?;
 };
 
@@ -913,6 +1058,7 @@
 
 type DeleteSchedulesQueries record {
     # This field indicates that the admin handles certain users. This setting is only for admin
+    @http:Query {name: "user_id"}
     string userId?;
 };
 
@@ -920,6 +1066,7 @@
 
 type DeleteScheduledEventsQueries record {
     # This field indicates whether the admin handles certain users. It's only for admin
+    @http:Query {name: "user_id"}
     string userId?;
 };
 
@@ -927,6 +1074,7 @@
 
 type PatchScheduleQueries record {
     # This field indicates that the admin handles certain users. This setting is only for admin
+    @http:Query {name: "user_id"}
     string userId?;
 };
 
@@ -934,10 +1082,13 @@
 
 type ListAvailabilityQueries record {
     # The token that specifies which result page to return
+    @http:Query {name: "next_page_token"}
     string nextPageToken?;
     # The return of the specific user's availability
+    @http:Query {name: "user_id"}
     string userId?;
     # The maximum number of availability returned on one result page
+    @http:Query {name: "page_size"}
     int pageSize?;
 };
 
@@ -946,6 +1097,7 @@
 type EventseventIdBody record {
     SchedulereventseventIdAttendees[] attendees?;
     # The meeting notes of the event
+    @jsondata:Name {value: "meeting_notes"}
     string meetingNotes?;
     # The status of event: confirmed or cancelled
     "confirmed"|"cancelled" status?;
@@ -957,9 +1109,12 @@
     # The default availability schedule in use
     boolean default?;
     # The name of this availability schedule
+    @constraint:String {minLength: 1}
     string name;
+    @jsondata:Name {value: "segments_recurrence"}
     ScheduleravailabilitySegmentsRecurrence segmentsRecurrence?;
     # The timezone for which this availability schedule originates
+    @jsondata:Name {value: "time_zone"}
     string timeZone;
     # The date on which the rule needs to be applied outside of the availability rule
     ScheduleravailabilityavailabilityIdSegments[] segments?;
@@ -980,6 +1135,7 @@
     # This field indicates if you created the schedule. The field is read-only
     boolean self?;
     # This field indicates the creator of the display name
+    @jsondata:Name {value: "display_name"}
     string displayName?;
     # This field indicates the creator's email address
     string email?;
@@ -989,85 +1145,112 @@
 
 type ListSchedulesQueries record {
     # Whether to include the deleted schedule (with status equals "cancelled") in the result
+    @http:Query {name: "show_deleted"}
     boolean showDeleted?;
     # The token that specifies which result page to return
+    @http:Query {name: "next_page_token"}
     string nextPageToken?;
     # The return of the specific user's schedules. Ths setting is only for admin
+    @http:Query {name: "user_id"}
     string userId?;
     # The lower bound (exclusive) for a schedule's end time from which to filter
     string 'from?;
     # The upper bound (exclusive) for a schedule's start time from which to filter
     string to?;
     # The time zone in the response
+    @http:Query {name: "time_zone"}
     string timeZone?;
     # The maximum number of schedule results returned on a result page
+    @http:Query {name: "page_size"}
     int pageSize?;
 };
 
 
 type InlineResponse2012 record {
     # The scheduling link URL
+    @jsondata:Name {value: "scheduling_url"}
     string schedulingUrl;
 };
 
 
 type InlineResponse2011 record {
     # The schedule's end date
+    @jsondata:Name {value: "end_date"}
     string endDate?;
     # The hexadecimal color value of the event type's scheduling page
     string color?;
     # The schedule's description
+    @constraint:String {maxLength: 8192}
     string description?;
     # This field indicates if the event type is hidden on the owner's main scheduling page
     boolean secret?;
     # The availability of the time rule
+    @jsondata:Name {value: "availability_rules"}
     InlineResponse2011AvailabilityRules[] availabilityRules?;
     # This field indicates the maximum invitees per event
+    @constraint:Number {minValue: 1, maxValue: 200}
     decimal capacity?;
     # The available time segments of the event
     SchedulerschedulesSegments[] segments?;
     # This field indicates the duration of the meeting in minutes, range: [1, 1440]
+    @constraint:Number {minValue: 15, maxValue: 1440}
     decimal duration?;
     # This field indicates the minimum time before a schedule starts when the attendees can book
+    @constraint:Number {minValue: 0, maxValue: 14340}
     decimal cushion?;
     # This field indicates the extra time before or after the booked schedule
     SchedulerschedulesBuffer buffer?;
+    @jsondata:Name {value: "segments_recurrence"}
     SchedulerschedulesSegmentsRecurrence segmentsRecurrence?;
     # The event portion of the event's URL that identifies a specific web page
+    @constraint:String {maxLength: 256, minLength: 3}
     string slug?;
     # The schedule time range. Unlimited means forever and fixed means using `startDate` and `endDate`
+    @jsondata:Name {value: "interval_type"}
     "unlimited"|"fixed" intervalType?;
     # The schedule's start date
+    @jsondata:Name {value: "start_date"}
     string startDate?;
     # The method of the type of `addOn`, such as Zoom meeting, Zoom phone, or offline
+    @jsondata:Name {value: "add_on_type"}
     "zoomMeeting"|"zoomPhone"|"offline" addOnType?;
     # The URL of the user’s scheduling site where invitees book this event type
+    @jsondata:Name {value: "scheduling_url"}
     string schedulingUrl?;
     # This field sets the frequency of available time slots for invitees
+    @jsondata:Name {value: "start_time_increment"}
     decimal startTimeIncrement?;
     # The event's summary
+    @constraint:String {maxLength: 256}
     string summary?;
     # The creator of the schedule. The field is read-only
     InlineResponse2011Creator creator?;
     # This field indicates if the schedule type is "one" (belongs to an individual user) or "multiple"
+    @jsondata:Name {value: "schedule_type"}
     "one"|"multiple" scheduleType?;
     # This field contains the custom question
+    @jsondata:Name {value: "custom_fields"}
     InlineResponse2011CustomFields[] customFields?;
     # This field indicates if the schedule is active
     boolean active?;
     # This field sets the maximum events allowed per day
+    @jsondata:Name {value: "booking_limit"}
     decimal bookingLimit?;
     # the timezone of this availability rule. 
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
     # The organizer of the schedule. This field is read-only
     InlineResponse2011Organizer organizer?;
     # The information for a custom location
+    @constraint:String {maxLength: 1024}
     string location?;
     # The unique identifier of schedule
+    @jsondata:Name {value: "schedule_id"}
     string scheduleId?;
     # The moment the schedule type was updated
     string updated?;
     # This field indicates the use of the availability rule
+    @jsondata:Name {value: "availability_override"}
     boolean availabilityOverride?;
     # The status of schedule: confirmed or cancelled
     "confirmed"|"cancelled" status?;
@@ -1093,12 +1276,14 @@
 
 type ReportAnalyticsQueries record {
     # The specific user's web user ID. Default is "me". Use "all" to query for analytics with respect to all members under that account. 
+    @http:Query {name: "user_id"}
     string userId?;
     # The lower bound (exclusive) for an event's end time from which to filter. Optional. The default is not to filter by end time. It must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds can be provided but are ignored. If `timeMax` is set, `timeMin` must be smaller than `timeMax`
     string 'from?;
     # The upper bound (exclusive) for an event's start time to filter by. Optional. The default is not to filter by start time. It must be an RFC3339 timestamp with mandatory time zone offset. For example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If `timeMin` is set, `timeMax` must be greater than `timeMin`
     string to?;
     # The time zone in the response. The default is the time zone of the calendar. Optional. 
+    @http:Query {name: "time_zone"}
     string timeZone?;
 };
 
@@ -1106,6 +1291,7 @@
 
 type InlineResponse2001 record {
     # The token for a later to retrieve only the entries that have changed since this result was returned. It's omitted if further results are available, in which case `nextPageToken` is provided
+    @jsondata:Name {value: "next_page_token"}
     string nextPageToken?;
     # array[User Availability Schedule]
     InlineResponse2001Items[] items?;
@@ -1114,6 +1300,7 @@
 
 type InlineResponse2003 record {
     # The token to access the next page of this result
+    @jsondata:Name {value: "next_page_token"}
     string nextPageToken?;
     InlineResponse2003Items[] items?;
 };
@@ -1128,15 +1315,19 @@
     # The name of this availability schedule
     string name?;
     # The unique ID of availability
+    @jsondata:Name {value: "availability_id"}
     string availabilityId?;
+    @jsondata:Name {value: "segments_recurrence"}
     ScheduleravailabilitySegmentsRecurrence segmentsRecurrence?;
     # The timezone for which this availability schedule originates
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
 };
 
 
 type InlineResponse2005 record {
     # The token that accesses the next page of this result
+    @jsondata:Name {value: "next_page_token"}
     string nextPageToken?;
     InlineResponse2005Items[] items?;
 };
@@ -1144,61 +1335,82 @@
 
 type InlineResponse2005Items record {
     # The schedule's end date
+    @jsondata:Name {value: "end_date"}
     string endDate?;
     # The hexadecimal color value of the event type's scheduling page
     string color?;
     # The schedule's description
+    @constraint:String {maxLength: 8192}
     string description?;
     # This field indicates if the event type is hidden on the owner's main scheduling page
     boolean secret?;
     # The availability of the time rule
+    @jsondata:Name {value: "availability_rules"}
     InlineResponse2005AvailabilityRules[] availabilityRules?;
     # This field indicates the maximum invitees per event
+    @constraint:Number {minValue: 1, maxValue: 200}
     decimal capacity?;
     # The available time segments of the event
     SchedulerschedulesSegments[] segments?;
     # This field indicates the duration of the meeting in minutes, range: [1, 1440]
+    @constraint:Number {minValue: 15, maxValue: 1440}
     decimal duration?;
     # This field indicates the minimum time before a schedule starts when the attendees can book
+    @constraint:Number {minValue: 0, maxValue: 14340}
     decimal cushion?;
     # This field indicates the extra time before or after the booked schedule
     SchedulerschedulesBuffer buffer?;
+    @jsondata:Name {value: "segments_recurrence"}
     SchedulerschedulesscheduleIdSegmentsRecurrence1 segmentsRecurrence?;
     # The event portion of the event's URL that identifies a specific web page
+    @constraint:String {maxLength: 256, minLength: 3}
     string slug?;
     # The schedule time range. Unlimited means forever and fixed means using `startDate` and `endDate`
+    @jsondata:Name {value: "interval_type"}
     "unlimited"|"fixed" intervalType?;
     # The schedule's start date
+    @jsondata:Name {value: "start_date"}
     string startDate?;
     # The method of the type of `addOn`, such as Zoom meeting, Zoom phone, or offline
+    @jsondata:Name {value: "add_on_type"}
     "zoomMeeting"|"zoomPhone"|"offline" addOnType?;
     # The URL of the user's scheduling site where invitees book this event type
+    @jsondata:Name {value: "scheduling_url"}
     string schedulingUrl?;
     # This field sets the frequency of available time slots for invitees
+    @jsondata:Name {value: "start_time_increment"}
     decimal startTimeIncrement?;
     # The event's summary
+    @constraint:String {maxLength: 256}
     string summary?;
     # The creator of the schedule. This field is read-only
     InlineResponse2005Creator creator?;
     # This field indicates if the schedule type is "one" (belongs to an individual user) or "multiple"
+    @jsondata:Name {value: "schedule_type"}
     "one"|"multiple" scheduleType?;
     # This field contains the custom question
+    @jsondata:Name {value: "custom_fields"}
     InlineResponse2011CustomFields[] customFields?;
     # This field indicates if the schedule is active
     boolean active?;
     # This field sets the maximum events allowed per day
+    @jsondata:Name {value: "booking_limit"}
     decimal bookingLimit?;
     # the timezone of this availability rule. 
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
     # The organizer of the schedule. This field is read-only
     InlineResponse2011Organizer organizer?;
     # The information for a custom location
+    @constraint:String {maxLength: 1024}
     string location?;
     # The unique identifier of the schedule
+    @jsondata:Name {value: "schedule_id"}
     string scheduleId?;
     # The moment the schedule type was updated
     string updated?;
     # This field indicates the use of the availability rule
+    @jsondata:Name {value: "availability_override"}
     boolean availabilityOverride?;
     # The status of schedule: confirmed or cancelled
     "confirmed"|"cancelled" status?;
@@ -1207,32 +1419,43 @@
 
 type InlineResponse2004 record {
     # The event's summary
+    @constraint:String {maxLength: 256}
     string summary?;
     # The attendees of the event
     InlineResponse2004Attendees[] attendees?;
     # The meeting notes of the event
+    @jsondata:Name {value: "meeting_notes"}
     string meetingNotes?;
     # The event's description
+    @constraint:String {maxLength: 8192}
     string description?;
     # The scheduled event's end date time
+    @jsondata:Name {value: "end_date_time"}
     string endDateTime?;
     # The unique identifier of event
+    @jsondata:Name {value: "event_id"}
     string eventId?;
     # This field indicates whether the type is default(scheduled) or a pending event
+    @jsondata:Name {value: "event_type"}
     "default"|"pending" eventType?;
     # The information to track the source of invitee. Only use this setting you add UTM parameters in schedule links
+    @jsondata:Name {value: "tracking_params"}
     InlineResponse2004TrackingParams[] trackingParams?;
     # The guest's collection
     string[] guests?;
     # The information for a custom location
+    @constraint:String {maxLength: 1024}
     string location?;
     # The scheduled event's start date time
+    @jsondata:Name {value: "start_date_time"}
     string startDateTime?;
     # The unique identifier of schedule
+    @jsondata:Name {value: "schedule_id"}
     string scheduleId?;
     # The moment the event was updated
     string updated?;
     # The meeting details for when users have scheduled appointments
+    @jsondata:Name {value: "external_location"}
     record {|string kind?; string meeting_id?; string personal_meeting_id?; string meeting_passcode?; string meeting_description?; string meeting_join_url?; anydata...;|} externalLocation?;
     # The status of event: confirmed or cancelled
     "confirmed"|"cancelled" status?;
@@ -1242,12 +1465,15 @@
 
 type InlineResponse2007 record {
     # The URL of the user’s scheduling site where invitees book this event type
+    @jsondata:Name {value: "scheduling_url"}
     string schedulingUrl?;
     # This field enables users to upload their company's logo on Zoom
     string logo?;
     # The user's name
+    @jsondata:Name {value: "display_name"}
     string displayName?;
     # The time zone to use when presenting time to the user
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
     # The portion of URL for the user's scheduling page where invitees book sessions that renders in a human-readable format
     string slug?;
@@ -1259,85 +1485,113 @@
 
 type ListScheduledEventsQueries record {
     # Whether to include deleted events (with status equals `cancelled`) in the result
+    @http:Query {name: "show_deleted"}
     boolean showDeleted?;
     # This field returns search results from meeting ID or summary
     string search?;
     # Whether to return the pending events
+    @http:Query {name: "event_type"}
     "pending" eventType?;
     # The token that specifies which result page to return
+    @http:Query {name: "next_page_token"}
     string nextPageToken?;
     # The return of the specific user's scheduled event. It's only for admin
+    @http:Query {name: "user_id"}
     string userId?;
     # This field indicates the start time or the time when the event has been updated
+    @http:Query {name: "order_by"}
     string orderBy?;
     # The lower bound (exclusive) for an event's end time from which to filter. 
     string 'from?;
     # The upper bound (exclusive) for an event's start time from which to filter
     string to?;
     # The time zone in the response
+    @http:Query {name: "time_zone"}
     string timeZone?;
     # The maximum number of events returned on one result page
+    @http:Query {name: "page_size"}
     int pageSize?;
 };
 
 
 type InlineResponse2006 record {
     # The schedule's end date
+    @jsondata:Name {value: "end_date"}
     string endDate?;
     # The hexadecimal color value of the event type's scheduling page
     string color?;
     # The schedule's description
+    @constraint:String {maxLength: 8192}
     string description?;
     # This field indicates if the event type is hidden on the owner's main scheduling page
     boolean secret?;
     # The availability of the time rule
+    @jsondata:Name {value: "availability_rules"}
     InlineResponse2006AvailabilityRules[] availabilityRules?;
     # This field indicates the maximum invitees per event
+    @constraint:Number {minValue: 1, maxValue: 200}
     decimal capacity?;
     # The available time segments of the event
     SchedulerschedulesSegments[] segments?;
     # This field indicates the duration of the meeting in minutes, range: [1, 1440]
+    @constraint:Number {minValue: 15, maxValue: 1440}
     decimal duration?;
     # This field indicates the minimum time before a schedule starts when the attendees can book
+    @constraint:Number {minValue: 0, maxValue: 14340}
     decimal cushion?;
     # This field indicates the extra time before or after the booked schedule
     SchedulerschedulesBuffer buffer?;
+    @jsondata:Name {value: "segments_recurrence"}
     SchedulerschedulesSegmentsRecurrence segmentsRecurrence?;
     # The event portion of the event's URL that identifies a specific web page
+    @constraint:String {maxLength: 256, minLength: 3}
     string slug?;
     # The schedule time range. Unlimited means forever and fixed means using `startDate` and `endDate`
+    @jsondata:Name {value: "interval_type"}
     "unlimited"|"fixed" intervalType?;
     # The schedule's start date
+    @jsondata:Name {value: "start_date"}
     string startDate?;
     # The method of the type of `addOn`, such as Zoom meeting, Zoom phone, or offline
+    @jsondata:Name {value: "add_on_type"}
     "zoomMeeting"|"zoomPhone"|"offline" addOnType?;
     # The URL of the user's scheduling site where invitees book this event type
+    @jsondata:Name {value: "scheduling_url"}
     string schedulingUrl?;
     # This field sets the frequency of available time slots for invitees
+    @jsondata:Name {value: "start_time_increment"}
     decimal startTimeIncrement?;
     # The event's summary
+    @constraint:String {maxLength: 256}
     string summary?;
     # The creator of the schedule. The field is read-only
     InlineResponse2011Creator creator?;
     # This field indicates if the schedule type is **one** (belongs to an individual user) or **multiple**
+    @jsondata:Name {value: "schedule_type"}
     "one"|"multiple" scheduleType?;
     # This field contains the custom question
+    @jsondata:Name {value: "custom_fields"}
     InlineResponse2011CustomFields[] customFields?;
     # This field indicates if the schedule is active
     boolean active?;
     # This field sets the maximum events allowed per day
+    @jsondata:Name {value: "booking_limit"}
     decimal bookingLimit?;
     # the timezone of this availability rule. 
+    @jsondata:Name {value: "time_zone"}
     string timeZone?;
     # The organizer of the schedule. This field is read-only
     InlineResponse2011Organizer organizer?;
     # The information for a custom location
+    @constraint:String {maxLength: 1024}
     string location?;
     # The unique identifier of a schedule
+    @jsondata:Name {value: "schedule_id"}
     string scheduleId?;
     # The moment the schedule type was updated
     string updated?;
     # This field indicates the use of the availability rule
+    @jsondata:Name {value: "availability_override"}
     boolean availabilityOverride?;
     # The status of schedule: confirmed or cancelled
     "confirmed"|"cancelled" status?;
@@ -1351,11 +1605,11 @@
 
     # Report analytics
     # 
-    resource function get analytics(map<string|string[]> headers = {}, string userId = "", string from = "", string to = "", string timeZone = "", anydata Additional Values, ReportAnalyticsQueries queries) returns InlineResponse200|error;
+    resource function get analytics(map<string|string[]> headers = {}, string userId = "", string from = "", string to = "", string timeZone = "", ReportAnalyticsQueries queries) returns InlineResponse200|error;
 
     # List availability
     # 
-    resource function get availability(map<string|string[]> headers = {}, string nextPageToken = "", string userId = "", int pageSize = 0, anydata Additional Values, ListAvailabilityQueries queries) returns InlineResponse2001|error;
+    resource function get availability(map<string|string[]> headers = {}, string nextPageToken = "", string userId = "", int pageSize = 0, ListAvailabilityQueries queries) returns InlineResponse2001|error;
 
     # Insert availability
     # 
@@ -1375,39 +1629,39 @@
 
     # List scheduled events
     # 
-    resource function get events(map<string|string[]> headers = {}, boolean showDeleted = false, string search = "", "pending" eventType = "pending", string nextPageToken = "", string userId = "", string orderBy = "", string from = "", string to = "", string timeZone = "", int pageSize = 0, anydata Additional Values, ListScheduledEventsQueries queries) returns InlineResponse2003|error;
+    resource function get events(map<string|string[]> headers = {}, boolean showDeleted = false, string search = "", "pending" eventType = "pending", string nextPageToken = "", string userId = "", string orderBy = "", string from = "", string to = "", string timeZone = "", int pageSize = 0, ListScheduledEventsQueries queries) returns InlineResponse2003|error;
 
     # Get scheduled events 
     # 
-    resource function get events/[string eventId](map<string|string[]> headers = {}, string userId = "", anydata Additional Values, GetScheduledEventsQueries queries) returns InlineResponse2004|error;
+    resource function get events/[string eventId](map<string|string[]> headers = {}, string userId = "", GetScheduledEventsQueries queries) returns InlineResponse2004|error;
 
     # Delete scheduled events 
     # 
-    resource function delete events/[string eventId](map<string|string[]> headers = {}, string userId = "", anydata Additional Values, DeleteScheduledEventsQueries queries) returns error?;
+    resource function delete events/[string eventId](map<string|string[]> headers = {}, string userId = "", DeleteScheduledEventsQueries queries) returns error?;
 
     # Patch scheduled events
     # 
-    resource function patch events/[string eventId](EventseventIdBody payload, map<string|string[]> headers = {}, string userId = "", anydata Additional Values, PatchScheduledEventsQueries queries) returns error?;
+    resource function patch events/[string eventId](EventseventIdBody payload, map<string|string[]> headers = {}, string userId = "", PatchScheduledEventsQueries queries) returns error?;
 
     # List schedules
     # 
-    resource function get schedules(map<string|string[]> headers = {}, boolean showDeleted = false, string nextPageToken = "", string userId = "", string from = "", string to = "", string timeZone = "", int pageSize = 0, anydata Additional Values, ListSchedulesQueries queries) returns InlineResponse2005|error;
+    resource function get schedules(map<string|string[]> headers = {}, boolean showDeleted = false, string nextPageToken = "", string userId = "", string from = "", string to = "", string timeZone = "", int pageSize = 0, ListSchedulesQueries queries) returns InlineResponse2005|error;
 
     # Insert schedules
     # 
-    resource function post schedules(SchedulerSchedulesBody payload, map<string|string[]> headers = {}, string userId = "", anydata Additional Values, InsertScheduleQueries queries) returns InlineResponse2011|error;
+    resource function post schedules(SchedulerSchedulesBody payload, map<string|string[]> headers = {}, string userId = "", InsertScheduleQueries queries) returns InlineResponse2011|error;
 
     # Get schedules
     # 
-    resource function get schedules/[string scheduleId](map<string|string[]> headers = {}, string userId = "", anydata Additional Values, GetScheduleQueries queries) returns InlineResponse2006|error;
+    resource function get schedules/[string scheduleId](map<string|string[]> headers = {}, string userId = "", GetScheduleQueries queries) returns InlineResponse2006|error;
 
     # Delete schedules
     # 
-    resource function delete schedules/[string scheduleId](map<string|string[]> headers = {}, string userId = "", anydata Additional Values, DeleteSchedulesQueries queries) returns error?;
+    resource function delete schedules/[string scheduleId](map<string|string[]> headers = {}, string userId = "", DeleteSchedulesQueries queries) returns error?;
 
     # Patch schedules
     # 
-    resource function patch schedules/[string scheduleId](SchedulesscheduleIdBody payload, map<string|string[]> headers = {}, string userId = "", anydata Additional Values, PatchScheduleQueries queries) returns error?;
+    resource function patch schedules/[string scheduleId](SchedulesscheduleIdBody payload, map<string|string[]> headers = {}, string userId = "", PatchScheduleQueries queries) returns error?;
 
     # Single use link
     # 
`````
