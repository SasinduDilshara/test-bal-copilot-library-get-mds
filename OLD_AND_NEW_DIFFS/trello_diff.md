# trello — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `trello` |
| **Old file** | `trello/old/ballerinax_trello.bal.txt` |
| **New file** | `trello/new/ballerinax_trello.bal.txt` |
| **Old lines** | 4379 |
| **New lines** | 4499 |
| **Lines added** | 336 |
| **Lines removed** | 216 |
| **Hunks** | 131 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 24 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 65 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (24)

- `type AttachmentsAttachmentsOneOf12`
- `type AttachmentsOneOf1`
- `type CardCheckItemStates`
- `type Channel`
- `type CheckItemStatesOneOf1`
- `type Id1OneOf2`
- `type Id2OneOf2`
- `type IdBoardsOneOf1`
- `type IdMember1OneOf2`
- `type IdMemberOneOf1`
- `type IdOneOf2`
- `type InlineParameterItemsIdLabels`
- `type InlineParameterItemsIdMembers`
- `type ListFields`
- `type MemberFields`
- `type Pos1Pos1OneOf12`
- `type Pos2OneOf1`
- `type Pos3OneOf1`
- `type PosPosOneOf12`
- `type PosStringOrNumberPosStringOrNumberOneOf12`
- `type TrelloID`
- `type Value1OneOf1`
- `type Value1Value1OneOf12`
- `type Value1Value1Value1Value1OneOf1234`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 112–118 | 112–119 | Types | +2 | −1 |
| 2 | 147–159 | 148–162 | Types | +6 | −4 |
| 3 | 273–281 | 276–284 | Types | +2 | −2 |
| 4 | 303–308 | 306–312 | Types | +1 | −0 |
| 5 | 343–349 | 347–353 | Types | +1 | −1 |
| 6 | 361–369 | 365–373 | Types | +2 | −2 |
| 7 | 438–443 | 442–448 | Types | +1 | −0 |
| 8 | 445–451 | 450–456 | Types | +1 | −1 |
| 9 | 453–458 | 458–464 | Types | +1 | −0 |
| 10 | 464–469 | 470–476 | Types | +1 | −0 |
| 11 | 475–483 | 482–491 | Types | +3 | −2 |
| 12 | 493–503 | 501–511 | Types | +3 | −3 |
| 13 | 511–517 | 519–525 | Types | +1 | −1 |
| 14 | 535–541 | 543–549 | Types | +1 | −1 |
| 15 | 656–662 | 664–670 | Types | +1 | −1 |
| 16 | 664–676 | 672–684 | Types | +2 | −2 |
| 17 | 681–687 | 689–695 | Types | +1 | −1 |
| 18 | 693–699 | 701–707 | Types | +1 | −1 |
| 19 | 809–817 | 817–826 | Types | +3 | −2 |
| 20 | 820–840 | 829–849 | Types | +6 | −6 |
| 21 | 851–865 | 860–876 | Types | +5 | −3 |
| 22 | 880–888 | 891–899 | Types | +2 | −2 |
| 23 | 907–913 | 918–924 | Types | +1 | −1 |
| 24 | 950–956 | 961–967 | Types | +1 | −1 |
| 25 | 969–975 | 980–986 | Types | +1 | −1 |
| 26 | 1008–1013 | 1019–1025 | Types | +1 | −0 |
| 27 | 1016–1035 | 1028–1051 | Types | +4 | −0 |
| 28 | 1068–1073 | 1084–1090 | Types | +1 | −0 |
| 29 | 1129–1134 | 1146–1152 | Types | +1 | −0 |
| 30 | 1418–1423 | 1436–1442 | Types | +1 | −0 |
| 31 | 1464–1469 | 1483–1489 | Types | +1 | −0 |
| 32 | 1499–1505 | 1519–1525 | Types | +1 | −1 |
| 33 | 1541–1557 | 1561–1582 | Types | +5 | −0 |
| 34 | 1562–1567 | 1587–1593 | Types | +1 | −0 |
| 35 | 1569–1577 | 1595–1603 | Types | +2 | −2 |
| 36 | 1600–1607 | 1626–1635 | Types | +2 | −0 |
| 37 | 1615–1620 | 1643–1649 | Types | +1 | −0 |
| 38 | 1658–1663 | 1687–1693 | Types | +1 | −0 |
| 39 | 1685–1690 | 1715–1721 | Types | +1 | −0 |
| 40 | 1700–1706 | 1731–1737 | Types | +1 | −1 |
| 41 | 1714–1719 | 1745–1751 | Types | +1 | −0 |
| 42 | 1799–1805 | 1831–1838 | Types | +2 | −1 |
| 43 | 1812–1817 | 1845–1851 | Types | +1 | −0 |
| 44 | 1878–1887 | 1912–1924 | Types | +3 | −0 |
| 45 | 1904–1929 | 1941–1975 | Types | +9 | −0 |
| 46 | 1932–1937 | 1978–1984 | Types | +1 | −0 |
| 47 | 1941–1968 | 1988–2027 | Types | +12 | −0 |
| 48 | 1971–1984 | 2030–2047 | Types | +4 | −0 |
| 49 | 2077–2082 | 2140–2146 | Types | +1 | −0 |
| 50 | 2088–2117 | 2152–2191 | Types | +12 | −2 |
| 51 | 2220–2226 | 2294–2300 | Types | +1 | −1 |
| 52 | 2258–2272 | 2332–2348 | Types | +4 | −2 |
| 53 | 2275–2281 | 2351–2357 | Types | +1 | −1 |
| 54 | 2290–2296 | 2366–2372 | Types | +1 | −1 |
| 55 | 2306–2321 | 2382–2401 | Types | +4 | −0 |
| 56 | 2332–2344 | 2412–2425 | Types | +2 | −1 |
| 57 | 2401–2406 | 2482–2488 | Types | +1 | −0 |
| 58 | 2459–2467 | 2541–2549 | Types | +2 | −2 |
| 59 | 2596–2602 | 2678–2684 | Types | +1 | −1 |
| 60 | 2632–2638 | 2714–2720 | Types | +1 | −1 |
| 61 | 2668–2673 | 2750–2756 | Types | +1 | −0 |
| 62 | 2678–2683 | 2761–2767 | Types | +1 | −0 |
| 63 | 2686–2691 | 2770–2776 | Types | +1 | −0 |
| 64 | 2714–2721 | 2799–2808 | Types | +2 | −0 |
| 65 | 2750–2765 | 2837–2856 | Types | +5 | −1 |
| 66 | 2770–2779 | 2861–2873 | Types | +4 | −1 |
| 67 | 2807–2812 | 2901–2907 | Types | +1 | −0 |
| 68 | 2830–2836 | 2925–2931 | Types | +1 | −1 |
| 69 | 2842–2857 | 2937–2955 | Types | +4 | −1 |
| 70 | 2993–2998 | 3091–3097 | Types | +1 | −0 |
| 71 | 3058–3103 | 3157–3218 | Types | +18 | −2 |
| 72 | 3146–3151 | 3261–3267 | Types | +1 | −0 |
| 73 | 3162–3167 | 3278–3284 | Types | +1 | −0 |
| 74 | 3224–3229 | 3341–3347 | Types | +1 | −0 |
| 75 | 3265–3270 | 3383–3389 | Types | +1 | −0 |
| 76 | 3283–3288 | 3402–3408 | Types | +1 | −0 |
| 77 | 3319–3325 | 3439–3445 | Types | +1 | −1 |
| 78 | 3337–3343 | 3457–3463 | Types | +1 | −1 |
| 79 | 3349–3357 | 3469–3477 | Types | +2 | −2 |
| 80 | 3381–3391 | 3501–3511 | Client | +2 | −2 |
| 81 | 3397–3431 | 3517–3551 | Client | +8 | −8 |
| 82 | 3433–3439 | 3553–3559 | Client | +1 | −1 |
| 83 | 3449–3467 | 3569–3587 | Client | +4 | −4 |
| 84 | 3473–3483 | 3593–3603 | Client | +2 | −2 |
| 85 | 3497–3515 | 3617–3635 | Client | +4 | −4 |
| 86 | 3521–3531 | 3641–3651 | Client | +2 | −2 |
| 87 | 3533–3565 | 3653–3685 | Client | +8 | −8 |
| 88 | 3571–3577 | 3691–3697 | Client | +1 | −1 |
| 89 | 3583–3589 | 3703–3709 | Client | +1 | −1 |
| 90 | 3591–3609 | 3711–3729 | Client | +4 | −4 |
| 91 | 3615–3633 | 3735–3753 | Client | +4 | −4 |
| 92 | 3635–3661 | 3755–3781 | Client | +6 | −6 |
| 93 | 3663–3681 | 3783–3801 | Client | +4 | −4 |
| 94 | 3683–3701 | 3803–3821 | Client | +4 | −4 |
| 95 | 3703–3709 | 3823–3829 | Client | +1 | −1 |
| 96 | 3723–3741 | 3843–3861 | Client | +4 | −4 |
| 97 | 3755–3761 | 3875–3881 | Client | +1 | −1 |
| 98 | 3763–3777 | 3883–3897 | Client | +3 | −3 |
| 99 | 3783–3793 | 3903–3913 | Client | +2 | −2 |
| 100 | 3795–3809 | 3915–3929 | Client | +3 | −3 |
| 101 | 3843–3853 | 3963–3973 | Client | +2 | −2 |
| 102 | 3855–3907 | 3975–4027 | Client | +12 | −12 |
| 103 | 3917–3927 | 4037–4047 | Client | +2 | −2 |
| 104 | 3929–3951 | 4049–4071 | Client | +5 | −5 |
| 105 | 3953–3979 | 4073–4099 | Client | +6 | −6 |
| 106 | 3981–3991 | 4101–4111 | Client | +2 | −2 |
| 107 | 3993–4015 | 4113–4135 | Client | +5 | −5 |
| 108 | 4021–4027 | 4141–4147 | Client | +1 | −1 |
| 109 | 4029–4035 | 4149–4155 | Client | +1 | −1 |
| 110 | 4037–4051 | 4157–4171 | Client | +3 | −3 |
| 111 | 4053–4059 | 4173–4179 | Client | +1 | −1 |
| 112 | 4061–4067 | 4181–4187 | Client | +1 | −1 |
| 113 | 4073–4083 | 4193–4203 | Client | +2 | −2 |
| 114 | 4085–4095 | 4205–4215 | Client | +2 | −2 |
| 115 | 4097–4111 | 4217–4231 | Client | +3 | −3 |
| 116 | 4113–4119 | 4233–4239 | Client | +1 | −1 |
| 117 | 4121–4127 | 4241–4247 | Client | +1 | −1 |
| 118 | 4129–4143 | 4249–4263 | Client | +3 | −3 |
| 119 | 4161–4171 | 4281–4291 | Client | +2 | −2 |
| 120 | 4173–4211 | 4293–4331 | Client | +9 | −9 |
| 121 | 4213–4219 | 4333–4339 | Client | +1 | −1 |
| 122 | 4229–4235 | 4349–4355 | Client | +1 | −1 |
| 123 | 4237–4243 | 4357–4363 | Client | +1 | −1 |
| 124 | 4245–4259 | 4365–4379 | Client | +3 | −3 |
| 125 | 4269–4275 | 4389–4395 | Client | +1 | −1 |
| 126 | 4277–4287 | 4397–4407 | Client | +2 | −2 |
| 127 | 4325–4341 | 4445–4461 | Client | +4 | −4 |
| 128 | 4343–4349 | 4463–4469 | Client | +1 | −1 |
| 129 | 4351–4357 | 4471–4477 | Client | +1 | −1 |
| 130 | 4359–4365 | 4479–4485 | Client | +1 | −1 |
| 131 | 4367–4373 | 4487–4493 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- trello/old/ballerinax_trello.bal.txt	2026-08-12 12:57:30
+++ trello/new/ballerinax_trello.bal.txt	2026-08-12 13:19:20
@@ -112,7 +112,8 @@
     TrelloID value;
 };
 
-// Unknown type: TrelloID
+@constraint:String {pattern: re `^[0-9a-fA-F]{24}$`}
+type TrelloID string;
 
 
 type EnterpriseLicenses record {
@@ -147,13 +148,15 @@
     Value1 value?;
 };
 
-// Unknown type: Value1OneOf1
+# The new name for the List
+type Value1OneOf1 string;
 
-// Unknown type: Value1Value1OneOf12
+# The new position for the List
+type Value1Value1OneOf12 float;
 
-// Unknown type: Value1Value1Value1Value1OneOf1234
+type Value1Value1Value1Value1OneOf1234 boolean;
 
-type Value1 ballerinax/trello:2.0.1:Value1OneOf1|ballerinax/trello:2.0.1:Value1Value1OneOf12|ballerinax/trello:2.0.1:Value1Value1Value1OneOf123|ballerinax/trello:2.0.1:Value1Value1Value1Value1OneOf1234;
+type Value1 Value1OneOf1|Value1Value1OneOf12|Value1Value1Value1OneOf123|Value1Value1Value1Value1OneOf1234;
 
 # Represents the Queries record for the operation: get-members-id-tokens
 
@@ -273,9 +276,9 @@
 
 type PosStringOrNumberOneOf1 "top"|"bottom";
 
-// Unknown type: PosStringOrNumberPosStringOrNumberOneOf12
+type PosStringOrNumberPosStringOrNumberOneOf12 float;
 
-type PosStringOrNumber ballerinax/trello:2.0.1:PosStringOrNumberOneOf1|ballerinax/trello:2.0.1:PosStringOrNumberPosStringOrNumberOneOf12;
+type PosStringOrNumber PosStringOrNumberOneOf1|PosStringOrNumberPosStringOrNumberOneOf12;
 
 # Represents the Queries record for the operation: get-cards-id-members
 
@@ -303,6 +306,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # The HTTP version understood by the client
     http:HttpVersion httpVersion?; // Special Agent Note: HttpVersion FROM ballerina/http package
@@ -343,7 +347,7 @@
     boolean laxDataBinding?;
 };
 
-// Unknown type: InlineParameterItemsIdMembers
+type InlineParameterItemsIdMembers TrelloID;
 
 # Represents the Queries record for the operation: get-cards-id-list
 
@@ -361,9 +365,9 @@
     string text?;
 };
 
-// Unknown type: IdOneOf2
+type IdOneOf2 string;
 
-type id_4 string|ballerinax/trello:2.0.1:TrelloID;
+type id_4 string|TrelloID;
 
 # Represents the Queries record for the operation: get-notifications-id-card
 
@@ -438,6 +442,7 @@
     # Works for premium organizations only
     boolean activity?;
     # Fields to show if `member=true`. Valid values: [nested member resource fields](/cloud/trello/guides/rest-api/nested-resources/)
+    @http:Query {name: "member_fields"}
     MemberFields memberFields?;
     # Shows the type of member to the org the user is. For instance, an org admin will have a `orgMemberType` of `admin`
     boolean orgMemberType?;
@@ -445,7 +450,7 @@
     boolean member?;
 };
 
-// Unknown type: MemberFields
+type MemberFields "id";
 
 # Represents the Queries record for the operation: get-members-id-organizations
 
@@ -453,6 +458,7 @@
     # One of: `all`, `members`, `none`, `public` (Note: `members` filters to only private Workspaces)
     "all"|"members"|"none"|"public" filter?;
     # Whether or not to include paid account information in the returned workspace object
+    @http:Query {name: "paid_account"}
     boolean paidAccount?;
     # `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/)
     OrganizationFields fields?;
@@ -464,6 +470,7 @@
 
 type PutWebhooksIdQueries record {
     # A string with a length from `0` to `16384`
+    @constraint:String {maxLength: 16384}
     string description?;
     # Determines whether the webhook is active and sending `POST` requests
     boolean active?;
@@ -475,9 +482,10 @@
 
 type PosOneOf1 "top"|"bottom";
 
-// Unknown type: PosPosOneOf12
+@constraint:Float {minValue: 0}
+type PosPosOneOf12 float;
 
-type Pos ballerinax/trello:2.0.1:PosOneOf1|ballerinax/trello:2.0.1:PosPosOneOf12;
+type Pos PosOneOf1|PosPosOneOf12;
 
 type Pos1OneOf1 "top"|"bottom";
 
@@ -493,11 +501,11 @@
     string fullName?;
 };
 
-type id_1 ballerinax/trello:2.0.1:TrelloID|string;
+type id_1 TrelloID|string;
 
-type id_3 ballerinax/trello:2.0.1:TrelloID|string;
+type id_3 TrelloID|string;
 
-type id_2 ballerinax/trello:2.0.1:TrelloID|string;
+type id_2 TrelloID|string;
 
 # Represents the Queries record for the operation: get-labels-id
 
@@ -511,7 +519,7 @@
     TrelloID id?;
 };
 
-// Unknown type: InlineParameterItemsIdLabels
+type InlineParameterItemsIdLabels TrelloID;
 
 # Represents the Queries record for the operation: get-cards-id-stickers
 
@@ -535,7 +543,7 @@
     decimal attempts?;
 };
 
-// Unknown type: CheckItemStatesOneOf1
+type CheckItemStatesOneOf1 string;
 
 # Represents the Queries record for the operation: put-enterprises-id-members-idmember-licensed
 
@@ -656,7 +664,7 @@
 
 type Label record {
     TrelloID idBoard?;
-    ballerinax/trello:2.0.1:Color? color?;
+    Color? color?;
     # The name displayed for the label
     string? name?;
     TrelloID id?;
@@ -664,13 +672,13 @@
 
 type Color "lime"|()|"yellow"|"purple"|"blue"|"red"|"green"|"orange"|"black"|"sky"|"pink";
 
-type CardIdLabels ballerinax/trello:2.0.1:Label|ballerinax/trello:2.0.1:TrelloID;
+type CardIdLabels Label|TrelloID;
 
 
 type CardCover record {
     boolean? idUploadedBackground?;
     "light"|"dark" brightness?;
-    ballerinax/trello:2.0.1:Color? color?;
+    Color? color?;
     "normal" size?;
     TrelloID idAttachment?;
     boolean isTemplate?;
@@ -681,7 +689,7 @@
     TrelloID id?;
 };
 
-type CardIdChecklists ballerinax/trello:2.0.1:Checklist|ballerinax/trello:2.0.1:TrelloID;
+type CardIdChecklists Checklist|TrelloID;
 
 
 type Limits record {
@@ -693,7 +701,7 @@
     LimitsObject perBoard?;
 };
 
-// Unknown type: CardCheckItemStates
+type CardCheckItemStates CheckItemStatesOneOf1;
 
 
 type CardBadges record {
@@ -809,9 +817,10 @@
     string filter?;
 };
 
-// Unknown type: Id2OneOf2
+# Name of the organization
+type Id2OneOf2 string;
 
-type Id2 ballerinax/trello:2.0.1:TrelloID|ballerinax/trello:2.0.1:Id2OneOf2;
+type Id2 TrelloID|Id2OneOf2;
 
 # Represents the Queries record for the operation: put-actions-id
 
@@ -820,21 +829,21 @@
     string text;
 };
 
-// Unknown type: Id1OneOf2
+type Id1OneOf2 string;
 
-type Id1 ballerinax/trello:2.0.1:TrelloID|ballerinax/trello:2.0.1:Id1OneOf2;
+type Id1 TrelloID|Id1OneOf2;
 
-// Unknown type: Pos2OneOf1
+type Pos2OneOf1 float;
 
 type Pos2Pos2OneOf12 "top"|"bottom";
 
-type Pos2 ballerinax/trello:2.0.1:Pos2OneOf1|ballerinax/trello:2.0.1:Pos2Pos2OneOf12;
+type Pos2 Pos2OneOf1|Pos2Pos2OneOf12;
 
-// Unknown type: Pos3OneOf1
+type Pos3OneOf1 float;
 
 type Pos3Pos3OneOf12 "top"|"bottom";
 
-type Pos3 ballerinax/trello:2.0.1:Pos3OneOf1|ballerinax/trello:2.0.1:Pos3Pos3OneOf12;
+type Pos3 Pos3OneOf1|Pos3Pos3OneOf12;
 
 type TokenFields "identifier"|"idMember"|"dateCreated"|"dateExpires"|"permissions";
 
@@ -851,15 +860,17 @@
     TrelloID idBoard?;
     boolean onlyOrgMembers?;
     # Search query 1 to 16384 characters long
+    @constraint:String {maxLength: 16394, minLength: 1}
     string query;
     # The maximum number of results to return. Maximum of 20
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    @constraint:Int {maxValue: 20}
+    int:Signed32 'limit?;
     TrelloID idOrganization?;
 };
 
-// Unknown type: Pos1Pos1OneOf12
+type Pos1Pos1OneOf12 float;
 
-type Pos1 ballerinax/trello:2.0.1:Pos1OneOf1|ballerinax/trello:2.0.1:Pos1Pos1OneOf12;
+type Pos1 Pos1OneOf1|Pos1Pos1OneOf12;
 
 
 type CardsidCardcustomFieldsCustomFieldItems record {
@@ -880,9 +891,9 @@
     string text?;
 };
 
-// Unknown type: IdMember1OneOf2
+type IdMember1OneOf2 string;
 
-type IdMember1 ballerinax/trello:2.0.1:TrelloID|ballerinax/trello:2.0.1:IdMember1OneOf2;
+type IdMember1 TrelloID|IdMember1OneOf2;
 
 # Represents the Queries record for the operation: post-lists
 
@@ -907,7 +918,7 @@
 
 type BlockedKey "notification_comment_card"|"notification_added_a_due_date"|"notification_changed_due_date"|"notification_card_due_soon"|"notification_removed_from_card"|"notification_added_attachment_to_card"|"notification_created_card"|"notification_moved_card"|"notification_archived_card"|"notification_unarchived_card";
 
-// Unknown type: Channel
+type Channel "email";
 
 type NotificationFields "id"|"unread"|"type"|"date"|"dateRead"|"data"|"card"|"board"|"idMemberCreator"|"idAction"|"reactions";
 
@@ -950,7 +961,7 @@
 
 type PutLabelsIdQueries record {
     # The new color for the label. See: [fields](/cloud/trello/guides/rest-api/object-definitions/) for color options
-    ballerinax/trello:2.0.1:Color? color?;
+    Color? color?;
     # The new name for the label
     string name?;
 };
@@ -969,7 +980,7 @@
     PosStringOrNumber pos?;
 };
 
-// Unknown type: AttachmentsOneOf1
+type AttachmentsOneOf1 "cover";
 
 # Represents the Queries record for the operation: put-lists-id
 
@@ -1008,6 +1019,7 @@
     # Whether or not to include paid account information in the returned member object
 
     @deprecated
+    @http:Query {name: "paid_account"}
     boolean paidAccount?;
     # One of: `all`, `members`, `none`, `public`
     "all"|"members"|"none"|"public" organizationsInvited?;
@@ -1016,20 +1028,24 @@
     # `all` or `none`
     "all"|"none" customBoardBackgrounds?;
     # `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/)
+    @http:Query {name: "organizationsInvited_fields"}
     OrganizationFields organizationsInvitedFields?;
     # `all` or `none`
     "all"|"none" customEmoji?;
     # `all` or `none`
     "all"|"none" customStickers?;
     # `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/)
+    @http:Query {name: "boardsInvited_fields"}
     BoardFields boardsInvitedFields?;
     # `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/)
+    @http:Query {name: "organization_fields"}
     OrganizationFields organizationFields?;
     # `all` or a comma-separated list of: closed, members, open, organization, pinned, public, starred, unpinned
     "closed"|"members"|"open"|"organization"|"pinned"|"public"|"starred"|"unpinned" boardsInvited?;
     # Whether to return the boardStars or not
     boolean boardStars?;
     # Whether or not to include paid account information in the returned workspace object
+    @http:Query {name: "organization_paid_account"}
     boolean organizationPaidAccount?;
     # One of: `all`, `members`, `none`, `public`
     "all"|"members"|"none"|"public" organizations?;
@@ -1068,6 +1084,7 @@
 
 type PutOrganizationsIdMembersQueries record {
     # Name for the member, at least 1 character not beginning or ending with a space
+    @constraint:String {minLength: 1}
     string fullName;
     # One of: `admin`, `normal`
     "admin"|"normal" 'type?;
@@ -1129,6 +1146,7 @@
 type MemberMessagesDismissed record {
     string name?;
     string count?;
+    @jsondata:Name {value: "_id"}
     TrelloID id?;
     string lastDismissed?;
 };
@@ -1418,6 +1436,7 @@
 type CustomFieldsBody record {
     PosStringOrNumber pos;
     # Whether this Custom Field should be shown on the front of Cards
+    @jsondata:Name {value: "display_cardFront"}
     boolean displayCardFront?;
     # The name of the Custom Field
     string name;
@@ -1464,6 +1483,7 @@
     # Filter to apply to Lists
     ViewFilter filter?;
     # `all` or a comma-separated list of card [fields](/cloud/trello/guides/rest-api/object-definitions/#card-object)
+    @http:Query {name: "card_fields"}
     string cardFields?;
     # Filter to apply to Cards
     ViewFilter cards?;
@@ -1499,7 +1519,7 @@
 
 type Attachment record {
     string date?;
-    ballerinax/trello:2.0.1:Color? edgeColor?;
+    Color? edgeColor?;
     float pos?;
     string? bytes?;
     TrelloID idMember?;
@@ -1541,17 +1561,22 @@
     # `true`, `false`, or `cover`
     Attachments attachments?;
     # `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/). **Defaults**: `avatarHash, fullName, initials, username`
+    @http:Query {name: "member_fields"}
     string memberFields?;
     # `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/). **Defaults**: `avatarHash, fullName, initials, username`
+    @http:Query {name: "memberVoted_fields"}
     string memberVotedFields?;
     # `all` or a comma-separated list of sticker [fields](/cloud/trello/guides/rest-api/object-definitions/)
+    @http:Query {name: "sticker_fields"}
     string stickerFields?;
     # See the [Lists Nested Resource](/cloud/trello/guides/rest-api/nested-resources/)
     boolean list?;
     boolean checkItemStates?;
     # `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/#board-object). **Defaults**: `name, desc, descData, closed, idOrganization, pinned, url, prefs`
+    @http:Query {name: "board_fields"}
     string boardFields?;
     # `all` or a comma-separated list of attachment [fields](/cloud/trello/guides/rest-api/object-definitions/)
+    @http:Query {name: "attachment_fields"}
     string attachmentFields?;
     # Whether to return member objects for members on the card
     boolean members?;
@@ -1562,6 +1587,7 @@
     # `all` or a comma-separated list of [fields](/cloud/trello/guides/rest-api/object-definitions/). **Defaults**: `badges, checkItemStates, closed, dateLastActivity, desc, descData, due, start, idBoard, idChecklists, idLabels, idList, idMembers, idShort, idAttachmentCover, manualCoverAttachment, labels, name, pos, shortUrl, url`
     string fields?;
     # `all` or a comma-separated list of `idBoard,idCard,name,pos`
+    @http:Query {name: "checklist_fields"}
     string checklistFields?;
     # See the [Actions Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#actions-nested-resource)
     string actions?;
@@ -1569,9 +1595,9 @@
     boolean board?;
 };
 
-// Unknown type: AttachmentsAttachmentsOneOf12
+type AttachmentsAttachmentsOneOf12 boolean;
 
-type Attachments ballerinax/trello:2.0.1:AttachmentsOneOf1|ballerinax/trello:2.0.1:AttachmentsAttachmentsOneOf12;
+type Attachments AttachmentsOneOf1|AttachmentsAttachmentsOneOf12;
 
 # Represents the Queries record for the operation: put-lists-id-closed
 
@@ -1600,8 +1626,10 @@
 
 type EnterprisesIdMembersIdMemberDeactivatedQueries record {
     # Any valid value that the [nested board resource](/cloud/trello/guides/rest-api/nested-resources/) accepts
+    @http:Query {name: "board_fields"}
     BoardFields boardFields?;
     # Any valid value that the [nested organization resource](/cloud/trello/guides/rest-api/nested-resources/) accepts
+    @http:Query {name: "organization_fields"}
     OrganizationFields organizationFields?;
     # A comma separated list of any valid values that the [nested member field resource]() accepts
     MemberFields fields?;
@@ -1615,6 +1643,7 @@
     # Valid values: `all`, `closed`, `none`, `open`, `visible`. Cards is a nested resource. The additional query params available are documented at [Cards Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#cards-nested-resource)
     "all"|"closed"|"none"|"open"|"visible" cards?;
     # The fields on the checkItem to return if checkItems are being returned. `all` or a comma-separated list of: `name`, `nameData`, `pos`, `state`, `type`, `due`, `dueReminder`, `idMember`
+    @http:Query {name: "checkItem_fields"}
     "all"|"name"|"nameData"|"pos"|"state"|"type"|"due"|"dueReminder"|"idMember" checkItemFields?;
     # The check items on the list to return. One of: `all`, `none`
     "all"|"none" checkItems?;
@@ -1658,6 +1687,7 @@
     # The ID of the Card that the checklist should be added to
     TrelloID idCard;
     # The name of the checklist. Should be a string of length 1 to 16384
+    @constraint:String {maxLength: 16384, minLength: 1}
     string name?;
 };
 
@@ -1685,6 +1715,7 @@
     # The name of the Custom Field
     string name?;
     # Whether to display this custom field on the front of cards
+    @jsondata:Name {value: "display/cardFront"}
     boolean displayCardFront?;
 };
 
@@ -1700,7 +1731,7 @@
     ListFields fields?;
 };
 
-// Unknown type: ListFields
+type ListFields "id";
 
 # Represents the Queries record for the operation: post-checklists-id-checkitems
 
@@ -1714,6 +1745,7 @@
     # An ID of a member resource
     TrelloID idMember?;
     # The name of the new check item on the checklist. Should be a string of length 1 to 16384
+    @constraint:String {maxLength: 16384, minLength: 1}
     string name;
     # Determines whether the check item is already checked when created
     boolean checked?;
@@ -1799,7 +1831,8 @@
 
 type GetBoardsIdLabelsQueries record {
     # The number of Labels to be returned
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    @constraint:Int {minValue: 0, maxValue: 1000}
+    int:Signed32 'limit?;
     # The fields to be returned for the Labels
     Label fields?;
 };
@@ -1812,6 +1845,7 @@
     # The name to display for the Organization
     string displayName;
     # A string with a length of at least 3. Only lowercase letters, underscores, and numbers are allowed. If the name contains invalid characters, they will be removed. If the name conflicts with an existing name, a new name will be substituted
+    @constraint:String {minLength: 3}
     string name?;
     # The description for the organizations
     string desc?;
@@ -1878,10 +1912,13 @@
     # For custom stickers, the id of the sticker. For default stickers, the string identifier (like 'taco-cool', see below)
     string image;
     # The rotation of the sticker
+    @constraint:Float {minValue: 0, maxValue: 360}
     float rotate?;
     # The top position of the sticker, from -60 to 100
+    @constraint:Float {minValue: -60, maxValue: 100}
     float top;
     # The left position of the sticker, from -60 to 100
+    @constraint:Float {minValue: -60, maxValue: 100}
     float left;
     # The z-index of the sticker
     int zIndex;
@@ -1904,26 +1941,35 @@
 
 type PostBoardsQueries record {
     # Determines whether card covers are enabled
+    @http:Query {name: "prefs_cardCovers"}
     boolean prefsCardCovers?;
     # The id of a custom background or one of: `blue`, `orange`, `green`, `red`, `purple`, `pink`, `lime`, `sky`, `grey`
+    @http:Query {name: "prefs_background"}
     "blue"|"orange"|"green"|"red"|"purple"|"pink"|"lime"|"sky"|"grey" prefsBackground?;
     # Determines whether to use the default set of labels
     boolean defaultLabels?;
     # Who can vote on this board. One of `disabled`, `members`, `observers`, `org`, `public`
+    @http:Query {name: "prefs_voting"}
     "disabled"|"members"|"observers"|"org"|"public" prefsVoting?;
     # Determines what types of members can invite users to join. One of: `admins`, `members`
+    @http:Query {name: "prefs_invitations"}
     "members"|"admins" prefsInvitations?;
     # Determines whether users can join the boards themselves or whether they have to be invited
+    @http:Query {name: "prefs_selfJoin"}
     boolean prefsSelfJoin?;
     # The permissions level of the board. One of: `org`, `private`, `public`
+    @http:Query {name: "prefs_permissionLevel"}
     "org"|"private"|"public" prefsPermissionLevel?;
     # Determines the type of card aging that should take place on the board if card aging is enabled. One of: `pirate`, `regular`
+    @http:Query {name: "prefs_cardAging"}
     "pirate"|"regular" prefsCardAging?;
     # The id of a board to copy into the new board
     TrelloID idBoardSource?;
     # Who can comment on cards on this board. One of: `disabled`, `members`, `observers`, `org`, `public`
+    @http:Query {name: "prefs_comments"}
     "disabled"|"members"|"observers"|"org"|"public" prefsComments?;
     # The new name for the board. 1 to 16384 characters long
+    @constraint:String {maxLength: 16384, minLength: 1}
     string name;
     # The id or name of the Workspace the board should belong to
     TrelloID idOrganization?;
@@ -1932,6 +1978,7 @@
     # To keep cards from the original board pass in the value `cards`
     "cards"|"none" keepFromSource?;
     # A new description for the board, 0 to 16384 characters long
+    @constraint:String {maxLength: 16384}
     string desc?;
     # The Power-Ups that should be enabled on the new board. One of: `all`, `calendar`, `cardAging`, `recap`, `voting`
     "all"|"calendar"|"cardAging"|"recap"|"voting" powerUps?;
@@ -1941,28 +1988,40 @@
 
 type PutBoardsIdQueries record {
     # One of: pirate, regular
+    @http:Query {name: "prefs/cardAging"}
     string prefsCardAging?;
     # Name for the orange label. 1 to 16384 characters long
+    @http:Query {name: "labelNames/orange"}
     string labelNamesOrange?;
     # Determines whether the calendar feed is enabled or not
+    @http:Query {name: "prefs/calendarFeedEnabled"}
     boolean prefsCalendarFeedEnabled?;
     # One of: org, private, public
+    @http:Query {name: "prefs/permissionLevel"}
     string prefsPermissionLevel?;
     # Name for the yellow label. 1 to 16384 characters long
+    @http:Query {name: "labelNames/yellow"}
     string labelNamesYellow?;
     # Name for the purple label. 1 to 16384 characters long
+    @http:Query {name: "labelNames/purple"}
     string labelNamesPurple?;
     # Who can invite people to this board. One of: admins, members
+    @http:Query {name: "prefs/invitations"}
     string prefsInvitations?;
     # Who can vote on this board. One of disabled, members, observers, org, public
+    @http:Query {name: "prefs/voting"}
     string prefsVoting?;
     # Who can comment on cards on this board. One of: disabled, members, observers, org, public
+    @http:Query {name: "prefs/comments"}
     string prefsComments?;
     # Name for the blue label. 1 to 16384 characters long
+    @http:Query {name: "labelNames/blue"}
     string labelNamesBlue?;
     # The id of a custom background or one of: blue, orange, green, red, purple, pink, lime, sky, grey
+    @http:Query {name: "prefs/background"}
     string prefsBackground?;
     # Name for the red label. 1 to 16384 characters long
+    @http:Query {name: "labelNames/red"}
     string labelNamesRed?;
     # Whether the acting user is subscribed to the board
     TrelloID subscribed?;
@@ -1971,14 +2030,18 @@
     # The id of the Workspace the board should be moved to
     string idOrganization?;
     # Whether Workspace members can join the board themselves
+    @http:Query {name: "prefs/selfJoin"}
     boolean prefsSelfJoin?;
     # Whether the board is closed
     boolean closed?;
     # Whether card covers should be displayed on this board
+    @http:Query {name: "prefs/cardCovers"}
     boolean prefsCardCovers?;
     # Name for the green label. 1 to 16384 characters long
+    @http:Query {name: "labelNames/green"}
     string labelNamesGreen?;
     # Determines whether the Voting Power-Up should hide who voted on cards or not
+    @http:Query {name: "prefs/hideVotes"}
     boolean prefsHideVotes?;
     # A new description for the board, 0 to 16384 characters long
     string desc?;
@@ -2077,6 +2140,7 @@
     # `all` or `none`
     "all"|"none" filter?;
     # `all` or a comma-separated list of: `name,nameData,pos,state,type,due,dueReminder,idMember`
+    @http:Query {name: "checkItem_fields"}
     string checkItemFields?;
     # `all` or `none`
     "all"|"none" checkItems?;
@@ -2088,30 +2152,40 @@
 
 type GetEnterprisesIdQueries record {
     # Whether or not to include paid account information in the returned workspace objects
+    @http:Query {name: "organization_paid_accounts"}
     boolean organizationPaidAccounts?;
     # One of: `avatarHash`, `fullName`, `initials`, `username`
+    @http:Query {name: "member_fields"}
     string memberFields?;
     # Pass a [SCIM-style query](/cloud/trello/scim/) to filter members. This takes precedence over the all/normal/admins value of members. If any of the member_* args are set, the member array will be paginated
+    @http:Query {name: "member_filter"}
     string memberFilter?;
     # Deprecated: Please use member_sort. One of: `ascending`, `descending`, `asc`, `desc`
+    @http:Query {name: "member_sortOrder"}
     string memberSortOrder?;
     # Any valid value that the [nested organization field resource]() accepts
+    @http:Query {name: "organization_fields"}
     string organizationFields?;
     # Comma-seperated list of: `me`, `normal`, `admin`, `active`, `deactivated`
+    @http:Query {name: "organization_memberships"}
     string organizationMemberships?;
     # Any integer between 0 and 100
-    ballerina/lang.int:0.0.0:Signed32 memberStartIndex?;
+    @http:Query {name: "member_startIndex"}
+    int:Signed32 memberStartIndex?;
     # One of: `none`, `normal`, `admins`, `owners`, `all`
     string members?;
     # Deprecated: Please use member_sort. This parameter expects a [SCIM-style sorting value](/cloud/trello/scim/). Note that the members array returned will be paginated if `members` is `normal` or `admins`. Pagination can be controlled with `member_startIndex`, etc, and the API response's header will contain the total count and pagination state
+    @http:Query {name: "member_sortBy"}
     string memberSortBy?;
     # One of: `none`, `members`, `public`, `all`
     string organizations?;
     # Comma-separated list of: `id`, `name`, `displayName`, `prefs`, `ssoActivationFailed`, `idAdmins`, `idMembers` (Note that the members array returned will be paginated if `members` is 'normal' or 'admins'. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. Read the SCIM documentation [here]() for more information on filtering), `idOrganizations`, `products`, `userTypes`, `idMembers`, `idOrganizations`
     string fields?;
     # 0 to 100
-    ballerina/lang.int:0.0.0:Signed32 memberCount?;
+    @http:Query {name: "member_count"}
+    int:Signed32 memberCount?;
     # This parameter expects a [SCIM-style](/cloud/trello/scim/) sorting value prefixed by a `-` to sort descending. If no `-` is prefixed, it will be sorted ascending. Note that the members array returned will be paginated if `members` is 'normal' or 'admins'. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data
+    @http:Query {name: "member_sort"}
     string memberSort?;
 };
 
@@ -2220,7 +2294,7 @@
     Value value;
 };
 
-type Value ballerinax/trello:2.0.1:PosStringOrNumberOneOf1|ballerinax/trello:2.0.1:PosStringOrNumberPosStringOrNumberOneOf12|ballerinax/trello:2.0.1:TrelloID;
+type Value PosStringOrNumberOneOf1|PosStringOrNumberPosStringOrNumberOneOf12|TrelloID;
 
 
 type InlineResponseItems2007 record {
@@ -2258,15 +2332,17 @@
     string before?;
     boolean display?;
     # Max 1000
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     boolean memberCreator?;
     # Max 100
-    ballerina/lang.int:0.0.0:Signed32 page?;
+    int:Signed32 page?;
     # One of: `all`, `read`, `unread`
+    @http:Query {name: "read_filter"}
     string readFilter?;
     # `all` or a comma-separated list of notification [fields](/cloud/trello/guides/rest-api/object-definitions/)
     string fields?;
     # `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)
+    @http:Query {name: "memberCreator_fields"}
     string memberCreatorFields?;
     # A notification ID
     string since?;
@@ -2275,7 +2351,7 @@
 
 type InlineResponseItems2002 record {
     string date?;
-    ballerinax/trello:2.0.1:Color? edgeColor?;
+    Color? edgeColor?;
     float pos?;
     string? bytes?;
     TrelloID idMember?;
@@ -2290,7 +2366,7 @@
 
 type InlineResponseItems2003 record {
     string date?;
-    ballerinax/trello:2.0.1:Color? edgeColor?;
+    Color? edgeColor?;
     float pos?;
     string? bytes?;
     TrelloID idMember?;
@@ -2306,16 +2382,20 @@
 
 type GetNotificationsIdQueries record {
     # `all` or a comma-separated list of card [fields](/cloud/trello/guides/rest-api/object-definitions/)
+    @http:Query {name: "card_fields"}
     CardFields cardFields?;
     # `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)
+    @http:Query {name: "member_fields"}
     MemberFields memberFields?;
     # Whether to include the display object with the results
     boolean display?;
     # Whether to include the list object
     boolean list?;
     # `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/)
+    @http:Query {name: "board_fields"}
     BoardFields boardFields?;
     # `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/)
+    @http:Query {name: "organization_fields"}
     OrganizationFields organizationFields?;
     # Whether to include the entities object with the results
     boolean entities?;
@@ -2332,13 +2412,14 @@
     # Whether to include the card object
     boolean card?;
     # `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)
+    @http:Query {name: "memberCreator_fields"}
     MemberFields memberCreatorFields?;
 };
 
 
 type InlineResponseItems2001 record {
     string date?;
-    ballerinax/trello:2.0.1:Color? edgeColor?;
+    Color? edgeColor?;
     float pos?;
     string? bytes?;
     TrelloID idMember?;
@@ -2401,6 +2482,7 @@
     # `all` or a comma-separated list of: `closed`, `members`, `open`, `organization`, `public`, `starred`
     "all"|"closed"|"members"|"open"|"organization"|"public"|"starred" filter?;
     # `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/)
+    @http:Query {name: "organization_fields"}
     OrganizationFields organizationFields?;
     # Which lists to include with the boards. One of: `all`, `closed`, `none`, `open`
     "all"|"closed"|"none"|"open" lists?;
@@ -2459,9 +2541,9 @@
     TrelloID id?;
 };
 
-type id ballerinax/trello:2.0.1:TrelloID|string;
+type id TrelloID|string;
 
-type InlineResponseItems20014 ballerinax/trello:2.0.1:Member|ballerinax/trello:2.0.1:Card|ballerinax/trello:2.0.1:Board|ballerinax/trello:2.0.1:Organization;
+type InlineResponseItems20014 Member|Card|Board|Organization;
 
 
 type TransferrableOrganization record {
@@ -2596,7 +2678,7 @@
     boolean member?;
 };
 
-type Id ballerinax/trello:2.0.1:TrelloID|ballerinax/trello:2.0.1:IdOneOf2;
+type Id TrelloID|IdOneOf2;
 
 # Represents the Queries record for the operation: get-organizations-id-memberships-idmembership
 
@@ -2632,7 +2714,7 @@
     # Who on the Workspace can make Workspace visible boards. One of `admin`, `none`, `org`
     string prefs\/boardVisibilityRestrict\/org?;
     # `1` or `2`
-    ballerina/lang.int:0.0.0:Signed32 prefs\/googleAppsVersion?;
+    int:Signed32 prefs\/googleAppsVersion?;
     # Who on the Workspace can make public boards. One of: `admin`, `none`, `org`
     string prefs\/boardVisibilityRestrict\/public?;
     # An email address with optional wildcard characters. (E.g. `subdomain.*.trello.com`)
@@ -2668,6 +2750,7 @@
 
 type PutBoardsIdMembershipsIdmembershipQueries record {
     # Valid values: all, avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username
+    @http:Query {name: "member_fields"}
     "all"|"avatarHash"|"bio"|"bioData"|"confirmed"|"fullName"|"idPremOrgsAdmin"|"initials"|"memberType"|"products"|"status"|"url"|"username" memberFields?;
     # One of: admin, normal, observer. Determines the type of member that this membership will be to this board
     "admin"|"normal"|"observer" 'type;
@@ -2678,6 +2761,7 @@
 type GetActionsIdQueries record {
     boolean entities?;
     # `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)
+    @http:Query {name: "member_fields"}
     string memberFields?;
     boolean display?;
     boolean member?;
@@ -2686,6 +2770,7 @@
     # `all` or a comma-separated list of action [fields](/cloud/trello/guides/rest-api/object-definitions/#action-object)
     string fields?;
     # `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/)
+    @http:Query {name: "memberCreator_fields"}
     string memberCreatorFields?;
 };
 
@@ -2714,8 +2799,10 @@
 
 type GetEnterprisesIdMembersIdmemberQueries record {
     # Any valid value that the [nested board resource](/cloud/trello/guides/rest-api/nested-resources/) accepts
+    @http:Query {name: "board_fields"}
     string boardFields?;
     # Any valid value that the [nested organization field resource](/cloud/trello/guides/rest-api/nested-resources/) accepts
+    @http:Query {name: "organization_fields"}
     string organizationFields?;
     # A comma separated list of any valid values that the [nested member field resource]() accepts
     string fields?;
@@ -2750,16 +2837,20 @@
 
 type PutMembersIdQueries record {
     # New initials for the member. 1-4 characters long
+    @constraint:String {maxLength: 4, minLength: 1}
     string initials?;
+    @http:Query {name: "prefs/locale"}
     string prefsLocale?;
     # New name for the member. Cannot begin or end with a space
     string fullName?;
     string bio?;
     # One of: `gravatar`, `none`, `upload`
     "gravatar"|"none"|"upload" avatarSource?;
+    @http:Query {name: "prefs/colorBlind"}
     boolean prefsColorBlind?;
     # `-1` for disabled, `1`, or `60`
-    ballerina/lang.int:0.0.0:Signed32 prefsMinutesBetweenSummaries?;
+    @http:Query {name: "prefs/minutesBetweenSummaries"}
+    int:Signed32 prefsMinutesBetweenSummaries?;
     # New username for the member. At least 3 characters long, only lowercase letters, underscores, and numbers. Must be unique
     string username?;
 };
@@ -2770,10 +2861,13 @@
     # Pass a [SCIM-style query](/cloud/trello/scim/) to filter members. This takes precedence over the all/normal/admins value of members. If any of the below member_* args are set, the member array will be paginated
     string? filter?;
     # Any valid value that the [nested board resource](/cloud/trello/guides/rest-api/nested-resources/) accepts
+    @http:Query {name: "board_fields"}
     string boardFields?;
     # Any integer between 0 and 9999
-    ballerina/lang.int:0.0.0:Signed32 startIndex?;
+    @constraint:Int {minValue: 0, maxValue: 9999}
+    int:Signed32 startIndex?;
     # Any valid value that the [nested organization field resource](/cloud/trello/guides/rest-api/nested-resources/) accepts
+    @http:Query {name: "organization_fields"}
     string organizationFields?;
     # Deprecated: Please use `sort` instead. One of: `ascending`, `descending`, `asc`, `desc`
     "desc"?|"ascending"|"descending"|"asc" sortOrder?;
@@ -2807,6 +2901,7 @@
 
 type PostWebhooksQueries record {
     # A string with a length from `0` to `16384`
+    @constraint:String {maxLength: 16384}
     string description?;
     # Determines whether the webhook is active and sending `POST` requests
     boolean active?;
@@ -2830,7 +2925,7 @@
     boolean value;
 };
 
-// Unknown type: IdBoardsOneOf1
+type IdBoardsOneOf1 "mine";
 
 # Represents the Queries record for the operation: post-members-id-boardbackgrounds-1
 
@@ -2842,16 +2937,19 @@
 
 type PutCardsIdStickersIdstickerQueries record {
     # The rotation of the sticker
+    @constraint:Float {minValue: 0, maxValue: 360}
     float rotate?;
     # The top position of the sticker, from -60 to 100
+    @constraint:Float {minValue: -60, maxValue: 100}
     float top;
     # The left position of the sticker, from -60 to 100
+    @constraint:Float {minValue: -60, maxValue: 100}
     float left;
     # The z-index of the sticker
     int zIndex;
 };
 
-type IdBoards ballerinax/trello:2.0.1:IdBoardsOneOf1|ballerinax/trello:2.0.1:TrelloID;
+type IdBoards IdBoardsOneOf1|TrelloID;
 
 
 type IdCardCustomFieldsBody record {
@@ -2993,6 +3091,7 @@
 type PostMembersIdCustomemojiQueries record {
     record {|byte[] fileContent; string fileName; anydata...;|} file;
     # Name for the emoji. 2 - 64 characters
+    @constraint:String {maxLength: 64, minLength: 2}
     string name;
 };
 
@@ -3058,46 +3157,62 @@
 
 type GetSearchQueries record {
     # all or a comma-separated list of: `badges`, `checkItemStates`, `closed`, `dateLastActivity`, `desc`, `descData`, `due`, `idAttachmentCover`, `idBoard`, `idChecklists`, `idLabels`, `idList`, `idMembers`, `idMembersVoted`, `idShort`, `labels`, `manualCoverAttachment`, `name`, `pos`, `shortLink`, `shortUrl`, `subscribed`, `url`
+    @http:Query {name: "card_fields"}
     string cardFields?;
     # Whether to include member objects with card results
+    @http:Query {name: "card_members"}
     boolean cardMembers?;
     # all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username
+    @http:Query {name: "member_fields"}
     string memberFields?;
     # The search query with a length of 1 to 16384 characters
+    @constraint:String {maxLength: 16834, minLength: 1}
     string query;
     # Whether to include the parent board with card results
+    @http:Query {name: "card_board"}
     boolean cardBoard?;
     # Whether to include the parent list with card results
+    @http:Query {name: "card_list"}
     boolean cardList?;
     # Whether to include the parent organization with board results
+    @http:Query {name: "board_organization"}
     boolean boardOrganization?;
     # What type or types of Trello objects you want to search. all or a comma-separated list of: `actions`, `boards`, `cards`, `members`, `organizations`
     string modelTypes?;
     # The maximum number of boards returned. Maximum: 1000
+    @http:Query {name: "boards_limit"}
     int boardsLimit?;
     # all or a comma-separated list of: `closed`, `dateLastActivity`, `dateLastView`, `desc`, `descData`, `idOrganization`, `invitations`, `invited`, `labelNames`, `memberships`, `name`, `pinned`, `powerUps`, `prefs`, `shortLink`, `shortUrl`, `starred`, `subscribed`, `url`
+    @http:Query {name: "board_fields"}
     string boardFields?;
     # Whether to include sticker objects with card results
+    @http:Query {name: "card_stickers"}
     boolean cardStickers?;
     # all or a comma-separated list of billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url, website
+    @http:Query {name: "organization_fields"}
     string organizationFields?;
     # The maximum number of Workspaces to return. Maximum 1000
-    ballerina/lang.int:0.0.0:Signed32 organizationsLimit?;
+    @http:Query {name: "organizations_limit"}
+    int:Signed32 organizationsLimit?;
     # A comma-separated list of Card IDs
     string idCards?;
     # The maximum number of members to return. Maximum 1000
-    ballerina/lang.int:0.0.0:Signed32 membersLimit?;
+    @http:Query {name: "members_limit"}
+    int:Signed32 membersLimit?;
     # `mine` or a comma-separated list of Board IDs
     IdBoards idBoards?;
     # A comma-separated list of Organization IDs
     string idOrganizations?;
     # The page of results for cards. Maximum: 100
+    @http:Query {name: "cards_page"}
     decimal cardsPage?;
     # By default, Trello searches for each word in your query against exactly matching words within Member content. Specifying partial to be true means that we will look for content that starts with any of the words in your query.  If you are looking for a Card titled "My Development Status Report", by default you would need to search for "Development". If you have partial enabled, you will be able to search for "dev" but not "velopment"
     boolean partial?;
     # The maximum number of cards to return. Maximum: 1000
+    @http:Query {name: "cards_limit"}
     int cardsLimit?;
     # Whether to include attachment objects with card results. A boolean value (true or false) or cover for only card cover attachments
+    @http:Query {name: "card_attachments"}
     string cardAttachments?;
 };
 
@@ -3146,6 +3261,7 @@
     # This is a nested resource. Read more about custom fields as nested resources [here](#custom-fields-nested-resource)
     boolean customFields?;
     # Use with the `cards` param to include card pluginData with the response
+    @http:Query {name: "card_pluginData"}
     boolean cardPluginData?;
     # This is a nested resource. Read more about memberships as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/)
     string memberships?;
@@ -3162,6 +3278,7 @@
     # This is a nested resource. Read more about organizations as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/)
     boolean organization?;
     # Use with the `organization` param to include organization pluginData with the response
+    @http:Query {name: "organization_pluginData"}
     boolean organizationPluginData?;
     # Determines whether the pluginData for this board should be returned. Valid values: true or false
     boolean pluginData?;
@@ -3224,6 +3341,7 @@
     # A comma-separated list of [action types](https://developer.atlassian.com/cloud/trello/guides/rest-api/action-types/)
     string filter?;
     # The page of results for actions. Each page of results has 50 actions
+    @constraint:Number {maxValue: 19}
     decimal page?;
 };
 
@@ -3265,6 +3383,7 @@
     # A date string in the form of YYYY-MM-DDThh:mm:ssZ or a mongo object ID. Only objects created before this date will be returned
     string before?;
     # The fields of the [member](/cloud/trello/guides/rest-api/object-definitions/#member-object) to return
+    @http:Query {name: "member_fields"}
     string memberFields?;
     # The format of the returned Actions. Either list or count
     string format?;
@@ -3283,6 +3402,7 @@
     # The fields to be returned for the Actions. [See Action fields here](/cloud/trello/guides/rest-api/object-definitions/#action-object)
     Action fields?;
     # The fields of the [member](/cloud/trello/guides/rest-api/object-definitions/#member-object) creator to return
+    @http:Query {name: "memberCreator_fields"}
     string memberCreatorFields?;
     # A comma-separated list of idModels. Only actions related to these models will be returned
     string idModels?;
@@ -3319,7 +3439,7 @@
     # The ID of the Board to create the Label on
     string idBoard;
     # The color for the label
-    ballerinax/trello:2.0.1:Color? color;
+    Color? color;
     # Name for the label
     string name;
 };
@@ -3337,7 +3457,7 @@
     string url?;
 };
 
-type IdCustomFieldItemBody ballerinax/trello:2.0.1:CardsidCardcustomFieldidCustomFielditemOneOf1|ballerinax/trello:2.0.1:CardsidCardcustomFieldidCustomFielditemcardsidCardcustomFieldidCustomFielditemOneOf12;
+type IdCustomFieldItemBody CardsidCardcustomFieldidCustomFielditemOneOf1|CardsidCardcustomFieldidCustomFielditemcardsidCardcustomFieldidCustomFielditemOneOf12;
 
 
 type CustomField record {
@@ -3349,9 +3469,9 @@
     string idModel?;
 };
 
-// Unknown type: IdMemberOneOf1
+type IdMemberOneOf1 string;
 
-type IdMember ballerinax/trello:2.0.1:IdMemberOneOf1|ballerinax/trello:2.0.1:TrelloID;
+type IdMember IdMemberOneOf1|TrelloID;
 
 # Represents the Queries record for the operation: get-actions-id-board
 
@@ -3381,11 +3501,11 @@
 
     # Get an Action
     # 
-    resource function get actions/[trello:TrelloID id](map<string|string[]> headers = {}, boolean entities = false, string memberFields = "", boolean display = false, boolean member = false, boolean memberCreator = false, string fields = "", string memberCreatorFields = "", anydata Additional Values, GetActionsIdQueries queries) returns error?;
+    resource function get actions/[trello:TrelloID id](map<string|string[]> headers = {}, boolean entities = false, string memberFields = "", boolean display = false, boolean member = false, boolean memberCreator = false, string fields = "", string memberCreatorFields = "", GetActionsIdQueries queries) returns error?;
 
     # Update an Action
     # 
-    resource function put actions/[trello:TrelloID id](map<string|string[]> headers = {}, string text = "", anydata Additional Values, PutActionsIdQueries queries) returns error?;
+    resource function put actions/[trello:TrelloID id](map<string|string[]> headers = {}, string text = "", PutActionsIdQueries queries) returns error?;
 
     # Delete an Action
     # 
@@ -3397,35 +3517,35 @@
 
     # Get the Board for an Action
     # 
-    resource function get actions/[trello:TrelloID id]/board(map<string|string[]> headers = {}, BoardFields fields = "id", anydata Additional Values, GetActionsIdBoardQueries queries) returns Board|error;
+    resource function get actions/[trello:TrelloID id]/board(map<string|string[]> headers = {}, BoardFields fields = "id", GetActionsIdBoardQueries queries) returns Board|error;
 
     # Get the Card for an Action
     # 
-    resource function get actions/[trello:TrelloID id]/card(map<string|string[]> headers = {}, CardFields fields = "id", anydata Additional Values, GetActionsIdCardQueries queries) returns Card|error;
+    resource function get actions/[trello:TrelloID id]/card(map<string|string[]> headers = {}, CardFields fields = "id", GetActionsIdCardQueries queries) returns Card|error;
 
     # Get the List for an Action
     # 
-    resource function get actions/[trello:TrelloID id]/list(map<string|string[]> headers = {}, ListFields fields = "id", anydata Additional Values, GetActionsIdListQueries queries) returns TrelloList|error;
+    resource function get actions/[trello:TrelloID id]/list(map<string|string[]> headers = {}, ListFields fields = "id", GetActionsIdListQueries queries) returns TrelloList|error;
 
     # Get the Member of an Action
     # 
-    resource function get actions/[trello:TrelloID id]/member(map<string|string[]> headers = {}, MemberFields fields = "id", anydata Additional Values, GetActionsIdMemberQueries queries) returns Member|error;
+    resource function get actions/[trello:TrelloID id]/member(map<string|string[]> headers = {}, MemberFields fields = "id", GetActionsIdMemberQueries queries) returns Member|error;
 
     # Get the Member Creator of an Action
     # 
-    resource function get actions/[trello:TrelloID id]/memberCreator(map<string|string[]> headers = {}, MemberFields fields = "id", anydata Additional Values, GetActionsIdMembercreatorQueries queries) returns Member|error;
+    resource function get actions/[trello:TrelloID id]/memberCreator(map<string|string[]> headers = {}, MemberFields fields = "id", GetActionsIdMembercreatorQueries queries) returns Member|error;
 
     # Get the Organization of an Action
     # 
-    resource function get actions/[trello:TrelloID id]/organization(map<string|string[]> headers = {}, OrganizationFields fields = "id", anydata Additional Values, GetActionsIdOrganizationQueries queries) returns Organization|error;
+    resource function get actions/[trello:TrelloID id]/organization(map<string|string[]> headers = {}, OrganizationFields fields = "id", GetActionsIdOrganizationQueries queries) returns Organization|error;
 
     # Update a Comment Action
     # 
-    resource function put actions/[trello:TrelloID id]/text(map<string|string[]> headers = {}, string value = "", anydata Additional Values, PutActionsIdTextQueries queries) returns error?;
+    resource function put actions/[trello:TrelloID id]/text(map<string|string[]> headers = {}, string value = "", PutActionsIdTextQueries queries) returns error?;
 
     # Get Action's Reactions
     # 
-    resource function get actions/[trello:TrelloID idAction]/reactions(map<string|string[]> headers = {}, boolean emoji = false, boolean member = false, anydata Additional Values, GetActionsIdactionReactionsQueries queries) returns error?;
+    resource function get actions/[trello:TrelloID idAction]/reactions(map<string|string[]> headers = {}, boolean emoji = false, boolean member = false, GetActionsIdactionReactionsQueries queries) returns error?;
 
     # Create Reaction for Action
     # 
@@ -3433,7 +3553,7 @@
 
     # Get Action's Reaction
     # 
-    resource function get actions/[trello:TrelloID idAction]/reactions/[trello:TrelloID id](map<string|string[]> headers = {}, boolean emoji = false, boolean member = false, anydata Additional Values, GetActionsIdactionReactionsIdQueries queries) returns error?;
+    resource function get actions/[trello:TrelloID idAction]/reactions/[trello:TrelloID id](map<string|string[]> headers = {}, boolean emoji = false, boolean member = false, GetActionsIdactionReactionsIdQueries queries) returns error?;
 
     # Delete Action's Reaction
     # 
@@ -3449,19 +3569,19 @@
 
     # Batch Requests
     # 
-    resource function get batch(map<string|string[]> headers = {}, string urls = "", anydata Additional Values, GetBatchQueries queries) returns error?;
+    resource function get batch(map<string|string[]> headers = {}, string urls = "", GetBatchQueries queries) returns error?;
 
     # Get Memberships of a Board
     # 
-    resource function get boards/[trello:TrelloID id]/memberships(map<string|string[]> headers = {}, "admins"|"all"|"none"|"normal" filter = "admins", boolean activity = false, MemberFields memberFields = "id", boolean orgMemberType = false, boolean member = false, anydata Additional Values, GetBoardsIdMembershipsQueries queries) returns Memberships|error;
+    resource function get boards/[trello:TrelloID id]/memberships(map<string|string[]> headers = {}, "admins"|"all"|"none"|"normal" filter = "admins", boolean activity = false, MemberFields memberFields = "id", boolean orgMemberType = false, boolean member = false, GetBoardsIdMembershipsQueries queries) returns Memberships|error;
 
     # Get a Board
     # 
-    resource function get boards/[trello:TrelloID id](map<string|string[]> headers = {}, string checklists = "", string cards = "", boolean customFields = false, boolean cardPluginData = false, string memberships = "", string labels = "", boolean tags = false, string boardStars = "", string lists = "", string members = "", boolean organization = false, boolean organizationPluginData = false, boolean pluginData = false, boolean myPrefs = false, string fields = "", string actions = "", anydata Additional Values, GetBoardsIdQueries queries) returns Board|error;
+    resource function get boards/[trello:TrelloID id](map<string|string[]> headers = {}, string checklists = "", string cards = "", boolean customFields = false, boolean cardPluginData = false, string memberships = "", string labels = "", boolean tags = false, string boardStars = "", string lists = "", string members = "", boolean organization = false, boolean organizationPluginData = false, boolean pluginData = false, boolean myPrefs = false, string fields = "", string actions = "", GetBoardsIdQueries queries) returns Board|error;
 
     # Update a Board
     # 
-    resource function put boards/[trello:TrelloID id](map<string|string[]> headers = {}, string prefsCardAging = "", string labelNamesOrange = "", boolean prefsCalendarFeedEnabled = false, string prefsPermissionLevel = "", string labelNamesYellow = "", string labelNamesPurple = "", string prefsInvitations = "", string prefsVoting = "", string prefsComments = "", string labelNamesBlue = "", string prefsBackground = "", string labelNamesRed = "", TrelloID subscribed = "", string name = "", string idOrganization = "", boolean prefsSelfJoin = false, boolean closed = false, boolean prefsCardCovers = false, string labelNamesGreen = "", boolean prefsHideVotes = false, string desc = "", anydata Additional Values, PutBoardsIdQueries queries) returns error?;
+    resource function put boards/[trello:TrelloID id](map<string|string[]> headers = {}, string prefsCardAging = "", string labelNamesOrange = "", boolean prefsCalendarFeedEnabled = false, string prefsPermissionLevel = "", string labelNamesYellow = "", string labelNamesPurple = "", string prefsInvitations = "", string prefsVoting = "", string prefsComments = "", string labelNamesBlue = "", string prefsBackground = "", string labelNamesRed = "", TrelloID subscribed = "", string name = "", string idOrganization = "", boolean prefsSelfJoin = false, boolean closed = false, boolean prefsCardCovers = false, string labelNamesGreen = "", boolean prefsHideVotes = false, string desc = "", PutBoardsIdQueries queries) returns error?;
 
     # Delete a Board
     # 
@@ -3473,11 +3593,11 @@
 
     # Get Actions of a Board
     # 
-    resource function get boards/[string boardId]/actions(map<string|string[]> headers = {}, string before = "", string memberFields = "", string format = "", string filter = "", decimal limit = 0.0d, boolean member = false, boolean memberCreator = false, boolean reactions = false, decimal page = 0.0d, Action fields = {}, string memberCreatorFields = "", string idModels = "", string since = "", anydata Additional Values, GetBoardsIdActionsQueries queries) returns error?;
+    resource function get boards/[string boardId]/actions(map<string|string[]> headers = {}, string before = "", string memberFields = "", string format = "", string filter = "", decimal limit = 0.0d, boolean member = false, boolean memberCreator = false, boolean reactions = false, decimal page = 0.0d, Action fields = {}, string memberCreatorFields = "", string idModels = "", string since = "", GetBoardsIdActionsQueries queries) returns error?;
 
     # Get boardStars on a Board
     # 
-    resource function get boards/[string boardId]/boardStars(map<string|string[]> headers = {}, string filter = "", anydata Additional Values, GetBoardsIdBoardstarsQueries queries) returns InlineResponseItems200[]|error;
+    resource function get boards/[string boardId]/boardStars(map<string|string[]> headers = {}, string filter = "", GetBoardsIdBoardstarsQueries queries) returns InlineResponseItems200[]|error;
 
     # Get Checklists on a Board
     # 
@@ -3497,19 +3617,19 @@
 
     # Get Labels on a Board
     # 
-    resource function get boards/[trello:TrelloID id]/labels(map<string|string[]> headers = {}, int:Signed32 limit = 0, Label fields = {}, anydata Additional Values, GetBoardsIdLabelsQueries queries) returns error?;
+    resource function get boards/[trello:TrelloID id]/labels(map<string|string[]> headers = {}, int:Signed32 limit = 0, Label fields = {}, GetBoardsIdLabelsQueries queries) returns error?;
 
     # Create a Label on a Board
     # 
-    resource function post boards/[string id]/labels(map<string|string[]> headers = {}, string color = "", string name = "", anydata Additional Values, PostBoardsIdLabelsQueries queries) returns error?;
+    resource function post boards/[string id]/labels(map<string|string[]> headers = {}, string color = "", string name = "", PostBoardsIdLabelsQueries queries) returns error?;
 
     # Get Lists on a Board
     # 
-    resource function get boards/[trello:TrelloID id]/lists(map<string|string[]> headers = {}, ViewFilter filter = "all", string cardFields = "", ViewFilter cards = "all", string fields = "", anydata Additional Values, GetBoardsIdListsQueries queries) returns TrelloList[]|error;
+    resource function get boards/[trello:TrelloID id]/lists(map<string|string[]> headers = {}, ViewFilter filter = "all", string cardFields = "", ViewFilter cards = "all", string fields = "", GetBoardsIdListsQueries queries) returns TrelloList[]|error;
 
     # Create a List on a Board
     # 
-    resource function post boards/[trello:TrelloID id]/lists(map<string|string[]> headers = {}, string pos = "", string name = "", anydata Additional Values, PostBoardsIdListsQueries queries) returns TrelloList|error;
+    resource function post boards/[trello:TrelloID id]/lists(map<string|string[]> headers = {}, string pos = "", string name = "", PostBoardsIdListsQueries queries) returns TrelloList|error;
 
     # Get filtered Lists on a Board
     # 
@@ -3521,11 +3641,11 @@
 
     # Invite Member to Board via email
     # 
-    resource function put boards/[trello:TrelloID id]/members(IdMembersBody payload, map<string|string[]> headers = {}, "admin"|"normal"|"observer" type = "admin", string email = "", anydata Additional Values, PutBoardsIdMembersQueries queries) returns error?;
+    resource function put boards/[trello:TrelloID id]/members(IdMembersBody payload, map<string|string[]> headers = {}, "admin"|"normal"|"observer" type = "admin", string email = "", PutBoardsIdMembersQueries queries) returns error?;
 
     # Add a Member to a Board
     # 
-    resource function put boards/[trello:TrelloID id]/members/[trello:TrelloID idMember](map<string|string[]> headers = {}, boolean allowBillableGuest = false, "admin"|"normal"|"observer" type = "admin", anydata Additional Values, PutBoardsIdMembersIdmemberQueries queries) returns error?;
+    resource function put boards/[trello:TrelloID id]/members/[trello:TrelloID idMember](map<string|string[]> headers = {}, boolean allowBillableGuest = false, "admin"|"normal"|"observer" type = "admin", PutBoardsIdMembersIdmemberQueries queries) returns error?;
 
     # Remove Member from Board
     # 
@@ -3533,33 +3653,33 @@
 
     # Update Membership of Member on a Board
     # 
-    resource function put boards/[trello:TrelloID id]/memberships/[trello:TrelloID idMembership](map<string|string[]> headers = {}, "all"|"avatarHash"|"bio"|"bioData"|"confirmed"|"fullName"|"idPremOrgsAdmin"|"initials"|"memberType"|"products"|"status"|"url"|"username" memberFields = "all", "admin"|"normal"|"observer" type = "admin", anydata Additional Values, PutBoardsIdMembershipsIdmembershipQueries queries) returns error?;
+    resource function put boards/[trello:TrelloID id]/memberships/[trello:TrelloID idMembership](map<string|string[]> headers = {}, "all"|"avatarHash"|"bio"|"bioData"|"confirmed"|"fullName"|"idPremOrgsAdmin"|"initials"|"memberType"|"products"|"status"|"url"|"username" memberFields = "all", "admin"|"normal"|"observer" type = "admin", PutBoardsIdMembershipsIdmembershipQueries queries) returns error?;
 
     # Update emailPosition Pref on a Board
     # 
-    resource function put boards/[trello:TrelloID id]/myPrefs/emailPosition(map<string|string[]> headers = {}, "bottom"|"top" value = "bottom", anydata Additional Values, PutBoardsIdMyprefsEmailpositionQueries queries) returns error?;
+    resource function put boards/[trello:TrelloID id]/myPrefs/emailPosition(map<string|string[]> headers = {}, "bottom"|"top" value = "bottom", PutBoardsIdMyprefsEmailpositionQueries queries) returns error?;
 
     # Update idEmailList Pref on a Board
     # 
-    resource function put boards/[trello:TrelloID id]/myPrefs/idEmailList(map<string|string[]> headers = {}, TrelloID value = "", anydata Additional Values, PutBoardsIdMyprefsIdemaillistQueries queries) returns error?;
+    resource function put boards/[trello:TrelloID id]/myPrefs/idEmailList(map<string|string[]> headers = {}, TrelloID value = "", PutBoardsIdMyprefsIdemaillistQueries queries) returns error?;
 
     # Update showSidebar Pref on a Board
     # 
-    resource function put boards/[trello:TrelloID id]/myPrefs/showSidebar(map<string|string[]> headers = {}, boolean value = false, anydata Additional Values, PutBoardsIdMyPrefsShowsidebarQueries queries) returns error?;
+    resource function put boards/[trello:TrelloID id]/myPrefs/showSidebar(map<string|string[]> headers = {}, boolean value = false, PutBoardsIdMyPrefsShowsidebarQueries queries) returns error?;
 
     # Update showSidebarActivity Pref on a Board
     # 
-    resource function put boards/[trello:TrelloID id]/myPrefs/showSidebarActivity(map<string|string[]> headers = {}, boolean value = false, anydata Additional Values, PutBoardsIdMyPrefsShowsidebaractivityQueries queries) returns error?;
+    resource function put boards/[trello:TrelloID id]/myPrefs/showSidebarActivity(map<string|string[]> headers = {}, boolean value = false, PutBoardsIdMyPrefsShowsidebaractivityQueries queries) returns error?;
 
     # Update showSidebarBoardActions Pref on a Board
     # 
-    resource function put boards/[trello:TrelloID id]/myPrefs/showSidebarBoardActions(map<string|string[]> headers = {}, boolean value = false, anydata Additional Values, PutBoardsIdMyPrefsShowsidebarboardactionsQueries queries) returns error?;
+    resource function put boards/[trello:TrelloID id]/myPrefs/showSidebarBoardActions(map<string|string[]> headers = {}, boolean value = false, PutBoardsIdMyPrefsShowsidebarboardactionsQueries queries) returns error?;
 
     # Update showSidebarMembers Pref on a Board
     # 
-    resource function put boards/[trello:TrelloID id]/myPrefs/showSidebarMembers(map<string|string[]> headers = {}, boolean value = false, anydata Additional Values, PutBoardsIdMyPrefsShowsidebarmembersQueries queries) returns error?;
+    resource function put boards/[trello:TrelloID id]/myPrefs/showSidebarMembers(map<string|string[]> headers = {}, boolean value = false, PutBoardsIdMyPrefsShowsidebarmembersQueries queries) returns error?;
 
-    resource function post boards(map<string|string[]> headers = {}, boolean prefsCardCovers = false, "blue"|"orange"|"green"|"red"|"purple"|"pink"|"lime"|"sky"|"grey" prefsBackground = "blue", boolean defaultLabels = false, "disabled"|"members"|"observers"|"org"|"public" prefsVoting = "disabled", "members"|"admins" prefsInvitations = "members", boolean prefsSelfJoin = false, "org"|"private"|"public" prefsPermissionLevel = "org", "pirate"|"regular" prefsCardAging = "pirate", TrelloID idBoardSource = "", "disabled"|"members"|"observers"|"org"|"public" prefsComments = "disabled", string name = "", TrelloID idOrganization = "", boolean defaultLists = false, "cards"|"none" keepFromSource = "cards", string desc = "", "all"|"calendar"|"cardAging"|"recap"|"voting" powerUps = "all", anydata Additional Values, PostBoardsQueries queries) returns error?;
+    resource function post boards(map<string|string[]> headers = {}, boolean prefsCardCovers = false, "blue"|"orange"|"green"|"red"|"purple"|"pink"|"lime"|"sky"|"grey" prefsBackground = "blue", boolean defaultLabels = false, "disabled"|"members"|"observers"|"org"|"public" prefsVoting = "disabled", "members"|"admins" prefsInvitations = "members", boolean prefsSelfJoin = false, "org"|"private"|"public" prefsPermissionLevel = "org", "pirate"|"regular" prefsCardAging = "pirate", TrelloID idBoardSource = "", "disabled"|"members"|"observers"|"org"|"public" prefsComments = "disabled", string name = "", TrelloID idOrganization = "", boolean defaultLists = false, "cards"|"none" keepFromSource = "cards", string desc = "", "all"|"calendar"|"cardAging"|"recap"|"voting" powerUps = "all", PostBoardsQueries queries) returns error?;
 
     # Create a calendarKey for a Board
     # 
@@ -3571,7 +3691,7 @@
 
     # Create a Tag for a Board
     # 
-    resource function post boards/[trello:TrelloID id]/idTags(map<string|string[]> headers = {}, TrelloID value = "", anydata Additional Values, PostBoardsIdIdtagsQueries queries) returns error?;
+    resource function post boards/[trello:TrelloID id]/idTags(map<string|string[]> headers = {}, TrelloID value = "", PostBoardsIdIdtagsQueries queries) returns error?;
 
     # Mark Board as viewed
     # 
@@ -3583,7 +3703,7 @@
 
     # Enable a Power-Up on a Board
     # 
-    resource function post boards/[trello:TrelloID id]/boardPlugins(map<string|string[]> headers = {}, TrelloID idPlugin = "", anydata Additional Values, PostBoardsIdBoardpluginsQueries queries) returns error?;
+    resource function post boards/[trello:TrelloID id]/boardPlugins(map<string|string[]> headers = {}, TrelloID idPlugin = "", PostBoardsIdBoardpluginsQueries queries) returns error?;
 
     # Disable a Power-Up on a Board
     # 
@@ -3591,19 +3711,19 @@
 
     # Get Power-Ups on a Board
     # 
-    resource function get boards/[trello:TrelloID id]/plugins(map<string|string[]> headers = {}, "enabled"|"available" filter = "enabled", anydata Additional Values, GetBoardIdPluginsQueries queries) returns Plugin|error;
+    resource function get boards/[trello:TrelloID id]/plugins(map<string|string[]> headers = {}, "enabled"|"available" filter = "enabled", GetBoardIdPluginsQueries queries) returns Plugin|error;
 
     # Create a new Card
     # 
-    resource function post cards(map<string|string[]> headers = {}, string address = "", string locationName = "", InlineParameterItemsIdLabels[] idLabels = [], TrelloID idCardSource = "", string|() start = (), boolean dueComplete = false, string coordinates = "", string urlSource = "", record {|byte[] fileContent; string fileName; anydata...;|} fileSource = {fileContent: [], fileName: ""}, TrelloID idList = "", string mimeType = "", InlineParameterItemsIdMembers[] idMembers = [], Pos pos = "top", string due = "", string name = "", "all"|"attachments"|"checklists"|"comments"|"customFields"|"due"|"start"|"labels"|"members"|"start"|"stickers" keepFromSource = "all", string desc = "", anydata Additional Values, PostCardsQueries queries) returns Card|error;
+    resource function post cards(map<string|string[]> headers = {}, string address = "", string locationName = "", InlineParameterItemsIdLabels[] idLabels = [], TrelloID idCardSource = "", string|() start = (), boolean dueComplete = false, string coordinates = "", string urlSource = "", record {|byte[] fileContent; string fileName; anydata...;|} fileSource = {fileContent: [], fileName: ""}, TrelloID idList = "", string mimeType = "", InlineParameterItemsIdMembers[] idMembers = [], Pos pos = "top", string due = "", string name = "", "all"|"attachments"|"checklists"|"comments"|"customFields"|"due"|"start"|"labels"|"members"|"start"|"stickers" keepFromSource = "all", string desc = "", PostCardsQueries queries) returns Card|error;
 
     # Get a Card
     # 
-    resource function get cards/[trello:TrelloID id](map<string|string[]> headers = {}, string checklists = "", boolean membersVoted = false, boolean customFieldItems = false, Attachments attachments = "cover", string memberFields = "", string memberVotedFields = "", string stickerFields = "", boolean list = false, boolean checkItemStates = false, string boardFields = "", string attachmentFields = "", boolean members = false, boolean pluginData = false, boolean stickers = false, string fields = "", string checklistFields = "", string actions = "", boolean board = false, anydata Additional Values, GetCardsIdQueries queries) returns Card|error;
+    resource function get cards/[trello:TrelloID id](map<string|string[]> headers = {}, string checklists = "", boolean membersVoted = false, boolean customFieldItems = false, Attachments attachments = "cover", string memberFields = "", string memberVotedFields = "", string stickerFields = "", boolean list = false, boolean checkItemStates = false, string boardFields = "", string attachmentFields = "", boolean members = false, boolean pluginData = false, boolean stickers = false, string fields = "", string checklistFields = "", string actions = "", boolean board = false, GetCardsIdQueries queries) returns Card|error;
 
     # Update a Card
     # 
-    resource function put cards/[trello:TrelloID id](map<string|string[]> headers = {}, TrelloID idBoard = "", string address = "", string locationName = "", TrelloID idLabels = "", string|() start = (), boolean dueComplete = false, string coordinates = "", TrelloID idList = "", TrelloID idMembers = "", Cover cover = {}, boolean subscribed = false, Pos1 pos = "top", string|() due = (), TrelloID idAttachmentCover = "", string name = "", boolean closed = false, string desc = "", anydata Additional Values, PutCardsIdQueries queries) returns Card|error;
+    resource function put cards/[trello:TrelloID id](map<string|string[]> headers = {}, TrelloID idBoard = "", string address = "", string locationName = "", TrelloID idLabels = "", string|() start = (), boolean dueComplete = false, string coordinates = "", TrelloID idList = "", TrelloID idMembers = "", Cover cover = {}, boolean subscribed = false, Pos1 pos = "top", string|() due = (), TrelloID idAttachmentCover = "", string name = "", boolean closed = false, string desc = "", PutCardsIdQueries queries) returns Card|error;
 
     # Delete a Card
     # 
@@ -3615,19 +3735,19 @@
 
     # Get Actions on a Card
     # 
-    resource function get cards/[trello:TrelloID id]/actions(map<string|string[]> headers = {}, string filter = "", decimal page = 0.0d, anydata Additional Values, GetCardsIdActionsQueries queries) returns Action[]|error;
+    resource function get cards/[trello:TrelloID id]/actions(map<string|string[]> headers = {}, string filter = "", decimal page = 0.0d, GetCardsIdActionsQueries queries) returns Action[]|error;
 
     # Get Attachments on a Card
     # 
-    resource function get cards/[trello:TrelloID id]/attachments(map<string|string[]> headers = {}, string filter = "", string fields = "", anydata Additional Values, GetCardsIdAttachmentsQueries queries) returns InlineResponseItems2001[]|error;
+    resource function get cards/[trello:TrelloID id]/attachments(map<string|string[]> headers = {}, string filter = "", string fields = "", GetCardsIdAttachmentsQueries queries) returns InlineResponseItems2001[]|error;
 
     # Create Attachment On Card
     # 
-    resource function post cards/[trello:TrelloID id]/attachments(map<string|string[]> headers = {}, record {|byte[] fileContent; string fileName; anydata...;|} file = {fileContent: [], fileName: ""}, boolean setCover = false, string name = "", string mimeType = "", string url = "", anydata Additional Values, PostCardsIdAttachmentsQueries queries) returns InlineResponseItems2002[]|error;
+    resource function post cards/[trello:TrelloID id]/attachments(map<string|string[]> headers = {}, record {|byte[] fileContent; string fileName; anydata...;|} file = {fileContent: [], fileName: ""}, boolean setCover = false, string name = "", string mimeType = "", string url = "", PostCardsIdAttachmentsQueries queries) returns InlineResponseItems2002[]|error;
 
     # Get an Attachment on a Card
     # 
-    resource function get cards/[trello:TrelloID id]/attachments/[trello:TrelloID idAttachment](map<string|string[]> headers = {}, InlineParameterItemsFields[] fields = [], anydata Additional Values, GetCardsIdAttachmentsIdattachmentQueries queries) returns InlineResponseItems2003[]|error;
+    resource function get cards/[trello:TrelloID id]/attachments/[trello:TrelloID idAttachment](map<string|string[]> headers = {}, InlineParameterItemsFields[] fields = [], GetCardsIdAttachmentsIdattachmentQueries queries) returns InlineResponseItems2003[]|error;
 
     # Delete an Attachment on a Card
     # 
@@ -3635,27 +3755,27 @@
 
     # Get the Board the Card is on
     # 
-    resource function get cards/[trello:TrelloID id]/board(map<string|string[]> headers = {}, string fields = "", anydata Additional Values, GetCardsIdBoardQueries queries) returns error?;
+    resource function get cards/[trello:TrelloID id]/board(map<string|string[]> headers = {}, string fields = "", GetCardsIdBoardQueries queries) returns error?;
 
     # Get checkItems on a Card
     # 
-    resource function get cards/[trello:TrelloID id]/checkItemStates(map<string|string[]> headers = {}, string fields = "", anydata Additional Values, GetCardsIdCheckitemstatesQueries queries) returns error?;
+    resource function get cards/[trello:TrelloID id]/checkItemStates(map<string|string[]> headers = {}, string fields = "", GetCardsIdCheckitemstatesQueries queries) returns error?;
 
     # Get Checklists on a Card
     # 
-    resource function get cards/[trello:TrelloID id]/checklists(map<string|string[]> headers = {}, "all"|"none" filter = "all", string checkItemFields = "", "all"|"none" checkItems = "all", "all"|"name"|"nameData"|"pos"|"state"|"type" fields = "all", anydata Additional Values, GetCardsIdChecklistsQueries queries) returns error?;
+    resource function get cards/[trello:TrelloID id]/checklists(map<string|string[]> headers = {}, "all"|"none" filter = "all", string checkItemFields = "", "all"|"none" checkItems = "all", "all"|"name"|"nameData"|"pos"|"state"|"type" fields = "all", GetCardsIdChecklistsQueries queries) returns error?;
 
     # Create Checklist on a Card
     # 
-    resource function post cards/[trello:TrelloID id]/checklists(map<string|string[]> headers = {}, TrelloID idChecklistSource = "", string pos = "", string name = "", anydata Additional Values, PostCardsIdChecklistsQueries queries) returns error?;
+    resource function post cards/[trello:TrelloID id]/checklists(map<string|string[]> headers = {}, TrelloID idChecklistSource = "", string pos = "", string name = "", PostCardsIdChecklistsQueries queries) returns error?;
 
     # Get checkItem on a Card
     # 
-    resource function get cards/[trello:TrelloID id]/checkItem/[trello:TrelloID idCheckItem](map<string|string[]> headers = {}, string fields = "", anydata Additional Values, GetCardsIdCheckitemIdcheckitemQueries queries) returns error?;
+    resource function get cards/[trello:TrelloID id]/checkItem/[trello:TrelloID idCheckItem](map<string|string[]> headers = {}, string fields = "", GetCardsIdCheckitemIdcheckitemQueries queries) returns error?;
 
     # Update a checkItem on a Card
     # 
-    resource function put cards/[trello:TrelloID id]/checkItem/[trello:TrelloID idCheckItem](map<string|string[]> headers = {}, decimal|() dueReminder = (), PosStringOrNumber pos = "top", string due = "", TrelloID idChecklist = "", TrelloID idMember = "", string name = "", "complete"|"incomplete" state = "complete", anydata Additional Values, PutCardsIdCheckitemIdcheckitemQueries queries) returns error?;
+    resource function put cards/[trello:TrelloID id]/checkItem/[trello:TrelloID idCheckItem](map<string|string[]> headers = {}, decimal|() dueReminder = (), PosStringOrNumber pos = "top", string due = "", TrelloID idChecklist = "", TrelloID idMember = "", string name = "", "complete"|"incomplete" state = "complete", PutCardsIdCheckitemIdcheckitemQueries queries) returns error?;
 
     # Delete checkItem on a Card
     # 
@@ -3663,19 +3783,19 @@
 
     # Get the List of a Card
     # 
-    resource function get cards/[trello:TrelloID id]/list(map<string|string[]> headers = {}, string fields = "", anydata Additional Values, GetCardsIdListQueries queries) returns error?;
+    resource function get cards/[trello:TrelloID id]/list(map<string|string[]> headers = {}, string fields = "", GetCardsIdListQueries queries) returns error?;
 
     # Get the Members of a Card
     # 
-    resource function get cards/[trello:TrelloID id]/members(map<string|string[]> headers = {}, string fields = "", anydata Additional Values, GetCardsIdMembersQueries queries) returns error?;
+    resource function get cards/[trello:TrelloID id]/members(map<string|string[]> headers = {}, string fields = "", GetCardsIdMembersQueries queries) returns error?;
 
     # Get Members who have voted on a Card
     # 
-    resource function get cards/[trello:TrelloID id]/membersVoted(map<string|string[]> headers = {}, string fields = "", anydata Additional Values, GetCardsIdMembersvotedQueries queries) returns error?;
+    resource function get cards/[trello:TrelloID id]/membersVoted(map<string|string[]> headers = {}, string fields = "", GetCardsIdMembersvotedQueries queries) returns error?;
 
     # Add Member vote to Card
     # 
-    resource function post cards/[trello:TrelloID id]/membersVoted(map<string|string[]> headers = {}, TrelloID value = "", anydata Additional Values, Cardsidmembersvoted1Queries queries) returns error?;
+    resource function post cards/[trello:TrelloID id]/membersVoted(map<string|string[]> headers = {}, TrelloID value = "", Cardsidmembersvoted1Queries queries) returns error?;
 
     # Get pluginData on a Card
     # 
@@ -3683,19 +3803,19 @@
 
     # Get Stickers on a Card
     # 
-    resource function get cards/[trello:TrelloID id]/stickers(map<string|string[]> headers = {}, string fields = "", anydata Additional Values, GetCardsIdStickersQueries queries) returns error?;
+    resource function get cards/[trello:TrelloID id]/stickers(map<string|string[]> headers = {}, string fields = "", GetCardsIdStickersQueries queries) returns error?;
 
     # Add a Sticker to a Card
     # 
-    resource function post cards/[trello:TrelloID id]/stickers(map<string|string[]> headers = {}, string image = "", float rotate = 0.0, float top = 0.0, float left = 0.0, int zIndex = 0, anydata Additional Values, PostCardsIdStickersQueries queries) returns error?;
+    resource function post cards/[trello:TrelloID id]/stickers(map<string|string[]> headers = {}, string image = "", float rotate = 0.0, float top = 0.0, float left = 0.0, int zIndex = 0, PostCardsIdStickersQueries queries) returns error?;
 
     # Get a Sticker on a Card
     # 
-    resource function get cards/[trello:TrelloID id]/stickers/[trello:TrelloID idSticker](map<string|string[]> headers = {}, string fields = "", anydata Additional Values, GetCardsIdStickersIdstickerQueries queries) returns error?;
+    resource function get cards/[trello:TrelloID id]/stickers/[trello:TrelloID idSticker](map<string|string[]> headers = {}, string fields = "", GetCardsIdStickersIdstickerQueries queries) returns error?;
 
     # Update a Sticker on a Card
     # 
-    resource function put cards/[trello:TrelloID id]/stickers/[trello:TrelloID idSticker](map<string|string[]> headers = {}, float rotate = 0.0, float top = 0.0, float left = 0.0, int zIndex = 0, anydata Additional Values, PutCardsIdStickersIdstickerQueries queries) returns error?;
+    resource function put cards/[trello:TrelloID id]/stickers/[trello:TrelloID idSticker](map<string|string[]> headers = {}, float rotate = 0.0, float top = 0.0, float left = 0.0, int zIndex = 0, PutCardsIdStickersIdstickerQueries queries) returns error?;
 
     # Delete a Sticker on a Card
     # 
@@ -3703,7 +3823,7 @@
 
     # Update Comment Action on a Card
     # 
-    resource function put cards/[trello:TrelloID id]/actions/[trello:TrelloID idAction]/comments(map<string|string[]> headers = {}, string text = "", anydata Additional Values, PutCardsIdActionsIdactionCommentsQueries queries) returns error?;
+    resource function put cards/[trello:TrelloID id]/actions/[trello:TrelloID idAction]/comments(map<string|string[]> headers = {}, string text = "", PutCardsIdActionsIdactionCommentsQueries queries) returns error?;
 
     # Delete a comment on a Card
     # 
@@ -3723,19 +3843,19 @@
 
     # Add a new comment to a Card
     # 
-    resource function post cards/[trello:TrelloID id]/actions/comments(map<string|string[]> headers = {}, string text = "", anydata Additional Values, PostCardsIdActionsCommentsQueries queries) returns Action|error;
+    resource function post cards/[trello:TrelloID id]/actions/comments(map<string|string[]> headers = {}, string text = "", PostCardsIdActionsCommentsQueries queries) returns Action|error;
 
     # Add a Label to a Card
     # 
-    resource function post cards/[trello:TrelloID id]/idLabels(map<string|string[]> headers = {}, TrelloID value = "", anydata Additional Values, PostCardsIdIdlabelsQueries queries) returns error?;
+    resource function post cards/[trello:TrelloID id]/idLabels(map<string|string[]> headers = {}, TrelloID value = "", PostCardsIdIdlabelsQueries queries) returns error?;
 
     # Add a Member to a Card
     # 
-    resource function post cards/[trello:TrelloID id]/idMembers(map<string|string[]> headers = {}, TrelloID value = "", anydata Additional Values, PostCardsIdIdmembersQueries queries) returns error?;
+    resource function post cards/[trello:TrelloID id]/idMembers(map<string|string[]> headers = {}, TrelloID value = "", PostCardsIdIdmembersQueries queries) returns error?;
 
     # Create a new Label on a Card
     # 
-    resource function post cards/[trello:TrelloID id]/labels(map<string|string[]> headers = {}, string color = "", string name = "", anydata Additional Values, PostCardsIdLabelsQueries queries) returns error?;
+    resource function post cards/[trello:TrelloID id]/labels(map<string|string[]> headers = {}, string color = "", string name = "", PostCardsIdLabelsQueries queries) returns error?;
 
     # Mark a Card's Notifications as read
     # 
@@ -3755,7 +3875,7 @@
 
     # Update Checkitem on Checklist on Card
     # 
-    resource function put cards/[trello:TrelloID idCard]/checklist/[trello:TrelloID idChecklist]/checkItem/[trello:TrelloID idCheckItem](map<string|string[]> headers = {}, PosStringOrNumber pos = "top", anydata Additional Values, PutCardsIdcardChecklistIdchecklistCheckitemIdcheckitemQueries queries) returns CheckItem|error;
+    resource function put cards/[trello:TrelloID idCard]/checklist/[trello:TrelloID idChecklist]/checkItem/[trello:TrelloID idCheckItem](map<string|string[]> headers = {}, PosStringOrNumber pos = "top", PutCardsIdcardChecklistIdchecklistCheckitemIdcheckitemQueries queries) returns CheckItem|error;
 
     # Delete a Checklist on a Card
     # 
@@ -3763,15 +3883,15 @@
 
     # Create a Checklist
     # 
-    resource function post checklists(map<string|string[]> headers = {}, TrelloID idChecklistSource = "", PosStringOrNumber pos = "top", TrelloID idCard = "", string name = "", anydata Additional Values, PostChecklistsQueries queries) returns error?;
+    resource function post checklists(map<string|string[]> headers = {}, TrelloID idChecklistSource = "", PosStringOrNumber pos = "top", TrelloID idCard = "", string name = "", PostChecklistsQueries queries) returns error?;
 
     # Get a Checklist
     # 
-    resource function get checklists/[trello:TrelloID id](map<string|string[]> headers = {}, "all"|"closed"|"none"|"open"|"visible" cards = "all", "all"|"name"|"nameData"|"pos"|"state"|"type"|"due"|"dueReminder"|"idMember" checkItemFields = "all", "all"|"none" checkItems = "all", string fields = "", anydata Additional Values, GetChecklistsIdQueries queries) returns error?;
+    resource function get checklists/[trello:TrelloID id](map<string|string[]> headers = {}, "all"|"closed"|"none"|"open"|"visible" cards = "all", "all"|"name"|"nameData"|"pos"|"state"|"type"|"due"|"dueReminder"|"idMember" checkItemFields = "all", "all"|"none" checkItems = "all", string fields = "", GetChecklistsIdQueries queries) returns error?;
 
     # Update a Checklist
     # 
-    resource function put checklists/[trello:TrelloID id](map<string|string[]> headers = {}, PosStringOrNumber pos = "top", string name = "", anydata Additional Values, PutCheclistsIdQueries queries) returns error?;
+    resource function put checklists/[trello:TrelloID id](map<string|string[]> headers = {}, PosStringOrNumber pos = "top", string name = "", PutCheclistsIdQueries queries) returns error?;
 
     # Delete a Checklist
     # 
@@ -3783,11 +3903,11 @@
 
     # Update field on a Checklist
     # 
-    resource function put checklists/[trello:TrelloID id]/["name"|"pos" 'field](map<string|string[]> headers = {}, Value value = "top", anydata Additional Values, PutChecklistsIdFieldQueries queries) returns error?;
+    resource function put checklists/[trello:TrelloID id]/["name"|"pos" 'field](map<string|string[]> headers = {}, Value value = "top", PutChecklistsIdFieldQueries queries) returns error?;
 
     # Get the Board the Checklist is on
     # 
-    resource function get checklists/[trello:TrelloID id]/board(map<string|string[]> headers = {}, "all"|"name" fields = "all", anydata Additional Values, GetChecklistsIdBoardQueries queries) returns error?;
+    resource function get checklists/[trello:TrelloID id]/board(map<string|string[]> headers = {}, "all"|"name" fields = "all", GetChecklistsIdBoardQueries queries) returns error?;
 
     # Get the Card a Checklist is on
     # 
@@ -3795,15 +3915,15 @@
 
     # Get Checkitems on a Checklist
     # 
-    resource function get checklists/[trello:TrelloID id]/checkItems(map<string|string[]> headers = {}, "all"|"none" filter = "all", "all"|"name"|"nameData"|"pos"|"state"|"type"|"due"|"dueReminder"|"idMember" fields = "all", anydata Additional Values, GetChecklistsIdCheckitemsQueries queries) returns error?;
+    resource function get checklists/[trello:TrelloID id]/checkItems(map<string|string[]> headers = {}, "all"|"none" filter = "all", "all"|"name"|"nameData"|"pos"|"state"|"type"|"due"|"dueReminder"|"idMember" fields = "all", GetChecklistsIdCheckitemsQueries queries) returns error?;
 
     # Create Checkitem on Checklist
     # 
-    resource function post checklists/[trello:TrelloID id]/checkItems(map<string|string[]> headers = {}, decimal|() dueReminder = (), PosStringOrNumber pos = "top", string due = "", TrelloID idMember = "", string name = "", boolean checked = false, anydata Additional Values, PostChecklistsIdCheckitemsQueries queries) returns error?;
+    resource function post checklists/[trello:TrelloID id]/checkItems(map<string|string[]> headers = {}, decimal|() dueReminder = (), PosStringOrNumber pos = "top", string due = "", TrelloID idMember = "", string name = "", boolean checked = false, PostChecklistsIdCheckitemsQueries queries) returns error?;
 
     # Get a Checkitem on a Checklist
     # 
-    resource function get checklists/[trello:TrelloID id]/checkItems/[trello:TrelloID idCheckItem](map<string|string[]> headers = {}, "all"|"name"|"nameData"|"pos"|"state"|"type"|"due"|"dueReminder"|"idMember" fields = "all", anydata Additional Values, GetChecklistsIdCheckitemsIdcheckitemQueries queries) returns error?;
+    resource function get checklists/[trello:TrelloID id]/checkItems/[trello:TrelloID idCheckItem](map<string|string[]> headers = {}, "all"|"name"|"nameData"|"pos"|"state"|"type"|"due"|"dueReminder"|"idMember" fields = "all", GetChecklistsIdCheckitemsIdcheckitemQueries queries) returns error?;
 
     # Delete Checkitem from Checklist
     # 
@@ -3843,11 +3963,11 @@
 
     # List available Emoji
     # 
-    resource function get emoji(map<string|string[]> headers = {}, string locale = "", boolean spritesheets = false, anydata Additional Values, EmojiQueries queries) returns Emoji|error;
+    resource function get emoji(map<string|string[]> headers = {}, string locale = "", boolean spritesheets = false, EmojiQueries queries) returns Emoji|error;
 
     # Get an Enterprise
     # 
-    resource function get enterprises/[trello:TrelloID id](map<string|string[]> headers = {}, boolean organizationPaidAccounts = false, string memberFields = "", string memberFilter = "", string memberSortOrder = "", string organizationFields = "", string organizationMemberships = "", int:Signed32 memberStartIndex = 0, string members = "", string memberSortBy = "", string organizations = "", string fields = "", int:Signed32 memberCount = 0, string memberSort = "", anydata Additional Values, GetEnterprisesIdQueries queries) returns Enterprise|error;
+    resource function get enterprises/[trello:TrelloID id](map<string|string[]> headers = {}, boolean organizationPaidAccounts = false, string memberFields = "", string memberFilter = "", string memberSortOrder = "", string organizationFields = "", string organizationMemberships = "", int:Signed32 memberStartIndex = 0, string members = "", string memberSortBy = "", string organizations = "", string fields = "", int:Signed32 memberCount = 0, string memberSort = "", GetEnterprisesIdQueries queries) returns Enterprise|error;
 
     # Get auditlog data for an Enterprise
     # 
@@ -3855,53 +3975,53 @@
 
     # Get Enterprise admin Members
     # 
-    resource function get enterprises/[trello:TrelloID id]/admins(map<string|string[]> headers = {}, string fields = "", anydata Additional Values, GetEnterprisesIdAdminsQueries queries) returns EnterpriseAdmin|error;
+    resource function get enterprises/[trello:TrelloID id]/admins(map<string|string[]> headers = {}, string fields = "", GetEnterprisesIdAdminsQueries queries) returns EnterpriseAdmin|error;
 
     # Get signupUrl for Enterprise
     # 
-    resource function get enterprises/[trello:TrelloID id]/signupUrl(map<string|string[]> headers = {}, boolean tosAccepted = false, boolean authenticate = false, boolean confirmationAccepted = false, string|() returnUrl = (), anydata Additional Values, GetEnterprisesIdSignupurlQueries queries) returns InlineResponse200|error;
+    resource function get enterprises/[trello:TrelloID id]/signupUrl(map<string|string[]> headers = {}, boolean tosAccepted = false, boolean authenticate = false, boolean confirmationAccepted = false, string|() returnUrl = (), GetEnterprisesIdSignupurlQueries queries) returns InlineResponse200|error;
 
     # Get Users of an Enterprise
     # 
-    resource function get enterprises/[trello:TrelloID id]/members/query(map<string|string[]> headers = {}, string cursor = "", string search = "", boolean licensed = false, string activeSince = "", string inactiveSince = "", boolean managed = false, boolean admin = false, boolean deactivated = false, boolean collaborator = false, anydata Additional Values, GetUsersIdQueries queries) returns Membership[]|error;
+    resource function get enterprises/[trello:TrelloID id]/members/query(map<string|string[]> headers = {}, string cursor = "", string search = "", boolean licensed = false, string activeSince = "", string inactiveSince = "", boolean managed = false, boolean admin = false, boolean deactivated = false, boolean collaborator = false, GetUsersIdQueries queries) returns Membership[]|error;
 
     # Get Members of Enterprise
     # 
-    resource function get enterprises/[trello:TrelloID id]/members(map<string|string[]> headers = {}, string|() filter = (), string boardFields = "", int:Signed32 startIndex = 0, string organizationFields = "", "desc"|()|"ascending"|"descending"|"asc" sortOrder = (), string count = "", string sortBy = "", string sort = "", string fields = "", anydata Additional Values, GetEnterprisesIdMembersQueries queries) returns Member[]|error;
+    resource function get enterprises/[trello:TrelloID id]/members(map<string|string[]> headers = {}, string|() filter = (), string boardFields = "", int:Signed32 startIndex = 0, string organizationFields = "", "desc"|()|"ascending"|"descending"|"asc" sortOrder = (), string count = "", string sortBy = "", string sort = "", string fields = "", GetEnterprisesIdMembersQueries queries) returns Member[]|error;
 
     # Get a Member of Enterprise
     # 
-    resource function get enterprises/[trello:TrelloID id]/members/[trello:TrelloID idMember](map<string|string[]> headers = {}, string boardFields = "", string organizationFields = "", string fields = "", anydata Additional Values, GetEnterprisesIdMembersIdmemberQueries queries) returns Member|error;
+    resource function get enterprises/[trello:TrelloID id]/members/[trello:TrelloID idMember](map<string|string[]> headers = {}, string boardFields = "", string organizationFields = "", string fields = "", GetEnterprisesIdMembersIdmemberQueries queries) returns Member|error;
 
     # Get whether an organization can be transferred to an enterprise.
     # 
     resource function get enterprises/[trello:TrelloID id]/transferrable/organization/[trello:TrelloID idOrganization](map<string|string[]> headers = {}) returns TransferrableOrganization|error;
 
-    resource function put enterprises/[trello:TrelloID id]/enterpriseJoinRequest/bulk(map<string|string[]> headers = {}, InlineParameterItemsIdOrganizations1[] idOrganizations = [], anydata Additional Values, PutEnterprisesIdEnterpriseJoinRequestBulkQueries queries) returns error?;
+    resource function put enterprises/[trello:TrelloID id]/enterpriseJoinRequest/bulk(map<string|string[]> headers = {}, InlineParameterItemsIdOrganizations1[] idOrganizations = [], PutEnterprisesIdEnterpriseJoinRequestBulkQueries queries) returns error?;
 
     # Get ClaimableOrganizations of an Enterprise
     # 
-    resource function get enterprises/[trello:TrelloID id]/claimableOrganizations(map<string|string[]> headers = {}, string cursor = "", string activeSince = "", string inactiveSince = "", int limit = 0, string name = "", anydata Additional Values, GetEnterprisesIdClaimableOrganizationsQueries queries) returns ClaimableOrganizations|error;
+    resource function get enterprises/[trello:TrelloID id]/claimableOrganizations(map<string|string[]> headers = {}, string cursor = "", string activeSince = "", string inactiveSince = "", int limit = 0, string name = "", GetEnterprisesIdClaimableOrganizationsQueries queries) returns ClaimableOrganizations|error;
 
     # Get PendingOrganizations of an Enterprise
     # 
-    resource function get enterprises/[trello:TrelloID id]/pendingOrganizations(map<string|string[]> headers = {}, string activeSince = "", string inactiveSince = "", anydata Additional Values, GetEnterprisesIdPendingOrganizationsQueries queries) returns PendingOrganizations[]|error;
+    resource function get enterprises/[trello:TrelloID id]/pendingOrganizations(map<string|string[]> headers = {}, string activeSince = "", string inactiveSince = "", GetEnterprisesIdPendingOrganizationsQueries queries) returns PendingOrganizations[]|error;
 
     # Create an auth Token for an Enterprise.
     # 
-    resource function post enterprises/[string id]/tokens(map<string|string[]> headers = {}, string expiration = "", anydata Additional Values, PostEnterprisesIdTokensQueries queries) returns error?;
+    resource function post enterprises/[string id]/tokens(map<string|string[]> headers = {}, string expiration = "", PostEnterprisesIdTokensQueries queries) returns error?;
 
     # Transfer an Organization to an Enterprise.
     # 
-    resource function put enterprises/[trello:TrelloID id]/organizations(map<string|string[]> headers = {}, string idOrganization = "", anydata Additional Values, PutEnterprisesIdOrganizationsQueries queries) returns InlineResponseItems2005[]|error;
+    resource function put enterprises/[trello:TrelloID id]/organizations(map<string|string[]> headers = {}, string idOrganization = "", PutEnterprisesIdOrganizationsQueries queries) returns InlineResponseItems2005[]|error;
 
     # Update a Member's licensed status
     # 
-    resource function put enterprises/[trello:TrelloID id]/members/[trello:TrelloID idMember]/licensed(map<string|string[]> headers = {}, boolean value = false, anydata Additional Values, PutEnterprisesIdMembersIdmemberLicensedQueries queries) returns Member|error;
+    resource function put enterprises/[trello:TrelloID id]/members/[trello:TrelloID idMember]/licensed(map<string|string[]> headers = {}, boolean value = false, PutEnterprisesIdMembersIdmemberLicensedQueries queries) returns Member|error;
 
     # Deactivate a Member of an Enterprise.
     # 
-    resource function put enterprises/[trello:TrelloID id]/members/[trello:TrelloID idMember]/deactivated(map<string|string[]> headers = {}, BoardFields boardFields = "id", OrganizationFields organizationFields = "id", MemberFields fields = "id", boolean value = false, anydata Additional Values, EnterprisesIdMembersIdMemberDeactivatedQueries queries) returns error?;
+    resource function put enterprises/[trello:TrelloID id]/members/[trello:TrelloID idMember]/deactivated(map<string|string[]> headers = {}, BoardFields boardFields = "id", OrganizationFields organizationFields = "id", MemberFields fields = "id", boolean value = false, EnterprisesIdMembersIdMemberDeactivatedQueries queries) returns error?;
 
     # Update Member to be admin of Enterprise
     # 
@@ -3917,11 +4037,11 @@
 
     # Get a Label
     # 
-    resource function get labels/[trello:TrelloID id](map<string|string[]> headers = {}, string fields = "", anydata Additional Values, GetLabelsIdQueries queries) returns error?;
+    resource function get labels/[trello:TrelloID id](map<string|string[]> headers = {}, string fields = "", GetLabelsIdQueries queries) returns error?;
 
     # Update a Label
     # 
-    resource function put labels/[trello:TrelloID id](map<string|string[]> headers = {}, "lime"|()|"yellow"|"purple"|"blue"|"red"|"green"|"orange"|"black"|"sky"|"pink" color = (), string name = "", anydata Additional Values, PutLabelsIdQueries queries) returns error?;
+    resource function put labels/[trello:TrelloID id](map<string|string[]> headers = {}, "lime"|()|"yellow"|"purple"|"blue"|"red"|"green"|"orange"|"black"|"sky"|"pink" color = (), string name = "", PutLabelsIdQueries queries) returns error?;
 
     # Delete a Label
     # 
@@ -3929,23 +4049,23 @@
 
     # Update a field on a label
     # 
-    resource function put labels/[string id]/["color"|"name" 'field](map<string|string[]> headers = {}, TrelloID value = "", anydata Additional Values, PutLabelsIdFieldQueries queries) returns error?;
+    resource function put labels/[string id]/["color"|"name" 'field](map<string|string[]> headers = {}, TrelloID value = "", PutLabelsIdFieldQueries queries) returns error?;
 
     # Create a Label
     # 
-    resource function post labels(map<string|string[]> headers = {}, string idBoard = "", "lime"|()|"yellow"|"purple"|"blue"|"red"|"green"|"orange"|"black"|"sky"|"pink" color = (), string name = "", anydata Additional Values, PostLabelsQueries queries) returns error?;
+    resource function post labels(map<string|string[]> headers = {}, string idBoard = "", "lime"|()|"yellow"|"purple"|"blue"|"red"|"green"|"orange"|"black"|"sky"|"pink" color = (), string name = "", PostLabelsQueries queries) returns error?;
 
     # Get a List
     # 
-    resource function get lists/[string id](map<string|string[]> headers = {}, string fields = "", anydata Additional Values, GetListsIdQueries queries) returns TrelloList|error;
+    resource function get lists/[string id](map<string|string[]> headers = {}, string fields = "", GetListsIdQueries queries) returns TrelloList|error;
 
     # Update a List
     # 
-    resource function put lists/[string id](map<string|string[]> headers = {}, boolean subscribed = false, TrelloID idBoard = "", Pos2 pos = 0.0, string name = "", boolean closed = false, anydata Additional Values, PutListsIdQueries queries) returns error?;
+    resource function put lists/[string id](map<string|string[]> headers = {}, boolean subscribed = false, TrelloID idBoard = "", Pos2 pos = 0.0, string name = "", boolean closed = false, PutListsIdQueries queries) returns error?;
 
     # Create a new List
     # 
-    resource function post lists(map<string|string[]> headers = {}, TrelloID idBoard = "", TrelloID idListSource = "", Pos3 pos = 0.0, string name = "", anydata Additional Values, PostListsQueries queries) returns TrelloList|error;
+    resource function post lists(map<string|string[]> headers = {}, TrelloID idBoard = "", TrelloID idListSource = "", Pos3 pos = 0.0, string name = "", PostListsQueries queries) returns TrelloList|error;
 
     # Archive all Cards in List
     # 
@@ -3953,27 +4073,27 @@
 
     # Move all Cards in List
     # 
-    resource function post lists/[trello:TrelloID id]/moveAllCards(map<string|string[]> headers = {}, TrelloID idBoard = "", TrelloID idList = "", anydata Additional Values, PostListsIdMoveallcardsQueries queries) returns error?;
+    resource function post lists/[trello:TrelloID id]/moveAllCards(map<string|string[]> headers = {}, TrelloID idBoard = "", TrelloID idList = "", PostListsIdMoveallcardsQueries queries) returns error?;
 
     # Archive or unarchive a list
     # 
-    resource function put lists/[trello:TrelloID id]/closed(map<string|string[]> headers = {}, TrelloID value = "", anydata Additional Values, PutListsIdClosedQueries queries) returns error?;
+    resource function put lists/[trello:TrelloID id]/closed(map<string|string[]> headers = {}, TrelloID value = "", PutListsIdClosedQueries queries) returns error?;
 
     # Move List to Board
     # 
-    resource function put lists/[trello:TrelloID id]/idBoard(map<string|string[]> headers = {}, TrelloID value = "", anydata Additional Values, PutIdIdboardQueries queries) returns error?;
+    resource function put lists/[trello:TrelloID id]/idBoard(map<string|string[]> headers = {}, TrelloID value = "", PutIdIdboardQueries queries) returns error?;
 
     # Update a field on a List
     # 
-    resource function put lists/[trello:TrelloID id]/["name"|"pos"|"subscribed" 'field](map<string|string[]> headers = {}, Value1 value = "", anydata Additional Values, PutListsIdFieldQueries queries) returns error?;
+    resource function put lists/[trello:TrelloID id]/["name"|"pos"|"subscribed" 'field](map<string|string[]> headers = {}, Value1 value = "", PutListsIdFieldQueries queries) returns error?;
 
     # Get Actions for a List
     # 
-    resource function get lists/[string id]/actions(map<string|string[]> headers = {}, string filter = "", anydata Additional Values, GetListsIdActionsQueries queries) returns error?;
+    resource function get lists/[string id]/actions(map<string|string[]> headers = {}, string filter = "", GetListsIdActionsQueries queries) returns error?;
 
     # Get the Board a List is on
     # 
-    resource function get lists/[string id]/board(map<string|string[]> headers = {}, string fields = "", anydata Additional Values, GetListsIdBoardQueries queries) returns error?;
+    resource function get lists/[string id]/board(map<string|string[]> headers = {}, string fields = "", GetListsIdBoardQueries queries) returns error?;
 
     # Get Cards in a List
     # 
@@ -3981,11 +4101,11 @@
 
     # Get a Member
     # 
-    resource function get members/[trello:Id id](map<string|string[]> headers = {}, boolean savedSearches = false, "all"|"custom"|"default"|"none"|"premium" boardBackgrounds = "all", string cards = "", boolean paidAccount = false, "all"|"members"|"none"|"public" organizationsInvited = "all", string boards = "", "all"|"none" customBoardBackgrounds = "all", OrganizationFields organizationsInvitedFields = "id", "all"|"none" customEmoji = "all", "all"|"none" customStickers = "all", BoardFields boardsInvitedFields = "id", OrganizationFields organizationFields = "id", "closed"|"members"|"open"|"organization"|"pinned"|"public"|"starred"|"unpinned" boardsInvited = "closed", boolean boardStars = false, boolean organizationPaidAccount = false, "all"|"members"|"none"|"public" organizations = "all", "all"|"none" tokens = "all", MemberFields fields = "id", string actions = "", string notifications = "", anydata Additional Values, GetMembersIdQueries queries) returns InlineResponse2001|error;
+    resource function get members/[trello:Id id](map<string|string[]> headers = {}, boolean savedSearches = false, "all"|"custom"|"default"|"none"|"premium" boardBackgrounds = "all", string cards = "", boolean paidAccount = false, "all"|"members"|"none"|"public" organizationsInvited = "all", string boards = "", "all"|"none" customBoardBackgrounds = "all", OrganizationFields organizationsInvitedFields = "id", "all"|"none" customEmoji = "all", "all"|"none" customStickers = "all", BoardFields boardsInvitedFields = "id", OrganizationFields organizationFields = "id", "closed"|"members"|"open"|"organization"|"pinned"|"public"|"starred"|"unpinned" boardsInvited = "closed", boolean boardStars = false, boolean organizationPaidAccount = false, "all"|"members"|"none"|"public" organizations = "all", "all"|"none" tokens = "all", MemberFields fields = "id", string actions = "", string notifications = "", GetMembersIdQueries queries) returns InlineResponse2001|error;
 
     # Update a Member
     # 
-    resource function put members/[trello:TrelloID id](map<string|string[]> headers = {}, string initials = "", string prefsLocale = "", string fullName = "", string bio = "", "gravatar"|"none"|"upload" avatarSource = "gravatar", boolean prefsColorBlind = false, int:Signed32 prefsMinutesBetweenSummaries = 0, string username = "", anydata Additional Values, PutMembersIdQueries queries) returns InlineResponse2001|error;
+    resource function put members/[trello:TrelloID id](map<string|string[]> headers = {}, string initials = "", string prefsLocale = "", string fullName = "", string bio = "", "gravatar"|"none"|"upload" avatarSource = "gravatar", boolean prefsColorBlind = false, int:Signed32 prefsMinutesBetweenSummaries = 0, string username = "", PutMembersIdQueries queries) returns InlineResponse2001|error;
 
     # Get a field on a Member
     # 
@@ -3993,23 +4113,23 @@
 
     # Get a Member's Actions
     # 
-    resource function get members/[trello:TrelloID id]/actions(map<string|string[]> headers = {}, string filter = "", anydata Additional Values, GetMembersIdActionsQueries queries) returns InlineResponseItems2006[]|error;
+    resource function get members/[trello:TrelloID id]/actions(map<string|string[]> headers = {}, string filter = "", GetMembersIdActionsQueries queries) returns InlineResponseItems2006[]|error;
 
     # Get Member's custom Board backgrounds
     # 
-    resource function get members/[trello:TrelloID id]/boardBackgrounds(map<string|string[]> headers = {}, "all"|"custom"|"default"|"none"|"premium" filter = "all", anydata Additional Values, GetMembersIdBoardbackgroundsQueries queries) returns InlineResponseItems2007[]|error;
+    resource function get members/[trello:TrelloID id]/boardBackgrounds(map<string|string[]> headers = {}, "all"|"custom"|"default"|"none"|"premium" filter = "all", GetMembersIdBoardbackgroundsQueries queries) returns InlineResponseItems2007[]|error;
 
     # Upload new boardBackground for Member
     # 
-    resource function post members/[trello:TrelloID id]/boardBackgrounds(map<string|string[]> headers = {}, record {|byte[] fileContent; string fileName; anydata...;|} file = {fileContent: [], fileName: ""}, anydata Additional Values, PostMembersIdBoardbackgrounds1Queries queries) returns InlineResponseItems2008[]|error;
+    resource function post members/[trello:TrelloID id]/boardBackgrounds(map<string|string[]> headers = {}, record {|byte[] fileContent; string fileName; anydata...;|} file = {fileContent: [], fileName: ""}, PostMembersIdBoardbackgrounds1Queries queries) returns InlineResponseItems2008[]|error;
 
     # Get a boardBackground of a Member
     # 
-    resource function get members/[trello:TrelloID id]/boardBackgrounds/[trello:TrelloID idBackground](map<string|string[]> headers = {}, "all"|"brightness"|"fullSizeUrl"|"scaled"|"tile" fields = "all", anydata Additional Values, GetMembersIdBoardbackgroundsIdbackgroundQueries queries) returns BoardBackground|error;
+    resource function get members/[trello:TrelloID id]/boardBackgrounds/[trello:TrelloID idBackground](map<string|string[]> headers = {}, "all"|"brightness"|"fullSizeUrl"|"scaled"|"tile" fields = "all", GetMembersIdBoardbackgroundsIdbackgroundQueries queries) returns BoardBackground|error;
 
     # Update a Member's custom Board background
     # 
-    resource function put members/[trello:TrelloID id]/boardBackgrounds/[trello:TrelloID idBackground](map<string|string[]> headers = {}, "dark"|"light"|"unknown" brightness = "dark", boolean tile = false, anydata Additional Values, PutMembersIdBoardbackgroundsIdbackgroundQueries queries) returns BoardBackground|error;
+    resource function put members/[trello:TrelloID id]/boardBackgrounds/[trello:TrelloID idBackground](map<string|string[]> headers = {}, "dark"|"light"|"unknown" brightness = "dark", boolean tile = false, PutMembersIdBoardbackgroundsIdbackgroundQueries queries) returns BoardBackground|error;
 
     # Delete a Member's custom Board background
     # 
@@ -4021,7 +4141,7 @@
 
     # Create Star for Board
     # 
-    resource function post members/[trello:Id1 id]/boardStars(map<string|string[]> headers = {}, TrelloID idBoard = "", PosStringOrNumber pos = "top", anydata Additional Values, PostMembersIdBoardstarsQueries queries) returns BoardStars[]|error;
+    resource function post members/[trello:Id1 id]/boardStars(map<string|string[]> headers = {}, TrelloID idBoard = "", PosStringOrNumber pos = "top", PostMembersIdBoardstarsQueries queries) returns BoardStars[]|error;
 
     # Get a boardStar of Member
     # 
@@ -4029,7 +4149,7 @@
 
     # Update the position of a boardStar of Member
     # 
-    resource function put members/[trello:TrelloID id]/boardStars/[trello:TrelloID idStar](map<string|string[]> headers = {}, PosStringOrNumber pos = "top", anydata Additional Values, PutMembersIdBoardstarsIdstarQueries queries) returns error?;
+    resource function put members/[trello:TrelloID id]/boardStars/[trello:TrelloID idStar](map<string|string[]> headers = {}, PosStringOrNumber pos = "top", PutMembersIdBoardstarsIdstarQueries queries) returns error?;
 
     # Delete Star for Board
     # 
@@ -4037,15 +4157,15 @@
 
     # Get Boards that Member belongs to
     # 
-    resource function get members/[trello:TrelloID id]/boards(map<string|string[]> headers = {}, "all"|"closed"|"members"|"open"|"organization"|"public"|"starred" filter = "all", OrganizationFields organizationFields = "id", "all"|"closed"|"none"|"open" lists = "all", boolean organization = false, BoardFields fields = "id", anydata Additional Values, GetMembersIdBoardsQueries queries) returns Board[]|error;
+    resource function get members/[trello:TrelloID id]/boards(map<string|string[]> headers = {}, "all"|"closed"|"members"|"open"|"organization"|"public"|"starred" filter = "all", OrganizationFields organizationFields = "id", "all"|"closed"|"none"|"open" lists = "all", boolean organization = false, BoardFields fields = "id", GetMembersIdBoardsQueries queries) returns Board[]|error;
 
     # Get Boards the Member has been invited to
     # 
-    resource function get members/[trello:TrelloID id]/boardsInvited(map<string|string[]> headers = {}, BoardFields fields = "id", anydata Additional Values, GetMembersIdBoardsinvitedQueries queries) returns Board[]|error;
+    resource function get members/[trello:TrelloID id]/boardsInvited(map<string|string[]> headers = {}, BoardFields fields = "id", GetMembersIdBoardsinvitedQueries queries) returns Board[]|error;
 
     # Get Cards the Member is on
     # 
-    resource function get members/[trello:TrelloID id]/cards(map<string|string[]> headers = {}, "all"|"closed"|"complete"|"incomplete"|"none"|"open"|"visible" filter = "all", anydata Additional Values, GetMembersIdCardsQueries queries) returns Card[]|error;
+    resource function get members/[trello:TrelloID id]/cards(map<string|string[]> headers = {}, "all"|"closed"|"complete"|"incomplete"|"none"|"open"|"visible" filter = "all", GetMembersIdCardsQueries queries) returns Card[]|error;
 
     # Get a Member's custom Board Backgrounds
     # 
@@ -4053,7 +4173,7 @@
 
     # Create a new custom Board Background
     # 
-    resource function post members/[trello:TrelloID id]/customBoardBackgrounds(map<string|string[]> headers = {}, record {|byte[] fileContent; string fileName; anydata...;|} file = {fileContent: [], fileName: ""}, anydata Additional Values, Membersidcustomboardbackgrounds1Queries queries) returns BoardBackground|error;
+    resource function post members/[trello:TrelloID id]/customBoardBackgrounds(map<string|string[]> headers = {}, record {|byte[] fileContent; string fileName; anydata...;|} file = {fileContent: [], fileName: ""}, Membersidcustomboardbackgrounds1Queries queries) returns BoardBackground|error;
 
     # Get custom Board Background of Member
     # 
@@ -4061,7 +4181,7 @@
 
     # Update custom Board Background of Member
     # 
-    resource function put members/[trello:id id]/customBoardBackgrounds/[trello:TrelloID idBackground](map<string|string[]> headers = {}, "dark"|"light"|"unknown" brightness = "dark", boolean tile = false, anydata Additional Values, PutMembersIdCustomboardbackgroundsIdbackgroundQueries queries) returns BoardBackground|error;
+    resource function put members/[trello:id id]/customBoardBackgrounds/[trello:TrelloID idBackground](map<string|string[]> headers = {}, "dark"|"light"|"unknown" brightness = "dark", boolean tile = false, PutMembersIdCustomboardbackgroundsIdbackgroundQueries queries) returns BoardBackground|error;
 
     # Delete custom Board Background of Member
     # 
@@ -4073,11 +4193,11 @@
 
     # Create custom Emoji for Member
     # 
-    resource function post members/[trello:TrelloID id]/customEmoji(map<string|string[]> headers = {}, record {|byte[] fileContent; string fileName; anydata...;|} file = {fileContent: [], fileName: ""}, string name = "", anydata Additional Values, PostMembersIdCustomemojiQueries queries) returns CustomEmoji|error;
+    resource function post members/[trello:TrelloID id]/customEmoji(map<string|string[]> headers = {}, record {|byte[] fileContent; string fileName; anydata...;|} file = {fileContent: [], fileName: ""}, string name = "", PostMembersIdCustomemojiQueries queries) returns CustomEmoji|error;
 
     # Get a Member's custom Emoji
     # 
-    resource function get members/[trello:TrelloID id]/customEmoji/[trello:TrelloID idEmoji](map<string|string[]> headers = {}, "name"|"url"|"all" fields = "name", anydata Additional Values, MembersidcustomemojiidemojiQueries queries) returns CustomEmoji|error;
+    resource function get members/[trello:TrelloID id]/customEmoji/[trello:TrelloID idEmoji](map<string|string[]> headers = {}, "name"|"url"|"all" fields = "name", MembersidcustomemojiidemojiQueries queries) returns CustomEmoji|error;
 
     # Get Member's custom Stickers
     # 
@@ -4085,11 +4205,11 @@
 
     # Create custom Sticker for Member
     # 
-    resource function post members/[trello:TrelloID id]/customStickers(map<string|string[]> headers = {}, record {|byte[] fileContent; string fileName; anydata...;|} file = {fileContent: [], fileName: ""}, anydata Additional Values, PostMembersIdCustomstickersQueries queries) returns CustomSticker|error;
+    resource function post members/[trello:TrelloID id]/customStickers(map<string|string[]> headers = {}, record {|byte[] fileContent; string fileName; anydata...;|} file = {fileContent: [], fileName: ""}, PostMembersIdCustomstickersQueries queries) returns CustomSticker|error;
 
     # Get a Member's custom Sticker
     # 
-    resource function get members/[trello:TrelloID id]/customStickers/[trello:TrelloID idSticker](map<string|string[]> headers = {}, "scaled"|"url"|"all" fields = "scaled", anydata Additional Values, GetMembersIdCustomstickersIdstickerQueries queries) returns CustomSticker|error;
+    resource function get members/[trello:TrelloID id]/customStickers/[trello:TrelloID idSticker](map<string|string[]> headers = {}, "scaled"|"url"|"all" fields = "scaled", GetMembersIdCustomstickersIdstickerQueries queries) returns CustomSticker|error;
 
     # Delete a Member's custom Sticker
     # 
@@ -4097,15 +4217,15 @@
 
     # Get Member's Notifications
     # 
-    resource function get members/[trello:TrelloID id]/notifications(map<string|string[]> headers = {}, string filter = "", boolean entities = false, string before = "", boolean display = false, int:Signed32 limit = 0, boolean memberCreator = false, int:Signed32 page = 0, string readFilter = "", string fields = "", string memberCreatorFields = "", string since = "", anydata Additional Values, GetMembersIdNotificationsQueries queries) returns Notification[]|error;
+    resource function get members/[trello:TrelloID id]/notifications(map<string|string[]> headers = {}, string filter = "", boolean entities = false, string before = "", boolean display = false, int:Signed32 limit = 0, boolean memberCreator = false, int:Signed32 page = 0, string readFilter = "", string fields = "", string memberCreatorFields = "", string since = "", GetMembersIdNotificationsQueries queries) returns Notification[]|error;
 
     # Get Member's Organizations
     # 
-    resource function get members/[trello:TrelloID id]/organizations(map<string|string[]> headers = {}, "all"|"members"|"none"|"public" filter = "all", boolean paidAccount = false, OrganizationFields fields = "id", anydata Additional Values, GetMembersIdOrganizationsQueries queries) returns Organization[]|error;
+    resource function get members/[trello:TrelloID id]/organizations(map<string|string[]> headers = {}, "all"|"members"|"none"|"public" filter = "all", boolean paidAccount = false, OrganizationFields fields = "id", GetMembersIdOrganizationsQueries queries) returns Organization[]|error;
 
     # Get Organizations a Member has been invited to
     # 
-    resource function get members/[trello:TrelloID id]/organizationsInvited(map<string|string[]> headers = {}, OrganizationFields fields = "id", anydata Additional Values, GetMembersIdOrganizationsinvitedQueries queries) returns Organization[]|error;
+    resource function get members/[trello:TrelloID id]/organizationsInvited(map<string|string[]> headers = {}, OrganizationFields fields = "id", GetMembersIdOrganizationsinvitedQueries queries) returns Organization[]|error;
 
     # Get Member's saved searched
     # 
@@ -4113,7 +4233,7 @@
 
     # Create saved Search for Member
     # 
-    resource function post members/[trello:TrelloID id]/savedSearches(map<string|string[]> headers = {}, PosStringOrNumber pos = "top", string query = "", string name = "", anydata Additional Values, PostMembersIdSavedsearchesQueries queries) returns SavedSearch|error;
+    resource function post members/[trello:TrelloID id]/savedSearches(map<string|string[]> headers = {}, PosStringOrNumber pos = "top", string query = "", string name = "", PostMembersIdSavedsearchesQueries queries) returns SavedSearch|error;
 
     # Get a saved search
     # 
@@ -4121,7 +4241,7 @@
 
     # Update a saved search
     # 
-    resource function put members/[string id]/savedSearches/[string idSearch](map<string|string[]> headers = {}, string pos = "", string query = "", string name = "", anydata Additional Values, PutMembersIdSavedsearchesIdsearchQueries queries) returns SavedSearch|error;
+    resource function put members/[string id]/savedSearches/[string idSearch](map<string|string[]> headers = {}, string pos = "", string query = "", string name = "", PutMembersIdSavedsearchesIdsearchQueries queries) returns SavedSearch|error;
 
     # Delete a saved search
     # 
@@ -4129,15 +4249,15 @@
 
     # Get Member's Tokens
     # 
-    resource function get members/[trello:TrelloID id]/tokens(map<string|string[]> headers = {}, boolean webhooks = false, anydata Additional Values, GetMembersIdTokensQueries queries) returns Token[]|error;
+    resource function get members/[trello:TrelloID id]/tokens(map<string|string[]> headers = {}, boolean webhooks = false, GetMembersIdTokensQueries queries) returns Token[]|error;
 
     # Create Avatar for Member
     # 
-    resource function post members/[string id]/avatar(map<string|string[]> headers = {}, record {|byte[] fileContent; string fileName; anydata...;|} file = {fileContent: [], fileName: ""}, anydata Additional Values, MembersidavatarQueries queries) returns error?;
+    resource function post members/[string id]/avatar(map<string|string[]> headers = {}, record {|byte[] fileContent; string fileName; anydata...;|} file = {fileContent: [], fileName: ""}, MembersidavatarQueries queries) returns error?;
 
     # Dismiss a message for Member
     # 
-    resource function post members/[trello:TrelloID id]/oneTimeMessagesDismissed(map<string|string[]> headers = {}, TrelloID value = "", anydata Additional Values, PostMembersIdOnetimemessagesdismissedQueries queries) returns error?;
+    resource function post members/[trello:TrelloID id]/oneTimeMessagesDismissed(map<string|string[]> headers = {}, TrelloID value = "", PostMembersIdOnetimemessagesdismissedQueries queries) returns error?;
 
     # Get a Member's notification channel settings
     # 
@@ -4161,11 +4281,11 @@
 
     # Get a Notification
     # 
-    resource function get notifications/[trello:TrelloID id](map<string|string[]> headers = {}, CardFields cardFields = "id", MemberFields memberFields = "id", boolean display = false, boolean list = false, BoardFields boardFields = "id", OrganizationFields organizationFields = "id", boolean entities = false, boolean organization = false, boolean member = false, boolean memberCreator = false, NotificationFields fields = "id", boolean board = false, boolean card = false, MemberFields memberCreatorFields = "id", anydata Additional Values, GetNotificationsIdQueries queries) returns InlineResponse2002|error;
+    resource function get notifications/[trello:TrelloID id](map<string|string[]> headers = {}, CardFields cardFields = "id", MemberFields memberFields = "id", boolean display = false, boolean list = false, BoardFields boardFields = "id", OrganizationFields organizationFields = "id", boolean entities = false, boolean organization = false, boolean member = false, boolean memberCreator = false, NotificationFields fields = "id", boolean board = false, boolean card = false, MemberFields memberCreatorFields = "id", GetNotificationsIdQueries queries) returns InlineResponse2002|error;
 
     # Update a Notification's read status
     # 
-    resource function put notifications/[trello:TrelloID id](map<string|string[]> headers = {}, boolean unread = false, anydata Additional Values, PutNotificationsIdQueries queries) returns InlineResponse2002|error;
+    resource function put notifications/[trello:TrelloID id](map<string|string[]> headers = {}, boolean unread = false, PutNotificationsIdQueries queries) returns InlineResponse2002|error;
 
     # Get a field of a Notification
     # 
@@ -4173,39 +4293,39 @@
 
     # Mark all Notifications as read
     # 
-    resource function post notifications/all/read(map<string|string[]> headers = {}, boolean read = false, TrelloID[] ids = [], anydata Additional Values, PostNotificationsAllReadQueries queries) returns InlineResponse2002|error;
+    resource function post notifications/all/read(map<string|string[]> headers = {}, boolean read = false, TrelloID[] ids = [], PostNotificationsAllReadQueries queries) returns InlineResponse2002|error;
 
     # Update Notification's read status
     # 
-    resource function put notifications/[trello:TrelloID id]/unread(map<string|string[]> headers = {}, string value = "", anydata Additional Values, PutNotificationsIdUnreadQueries queries) returns InlineResponse2002|error;
+    resource function put notifications/[trello:TrelloID id]/unread(map<string|string[]> headers = {}, string value = "", PutNotificationsIdUnreadQueries queries) returns InlineResponse2002|error;
 
     # Get the Board a Notification is on
     # 
-    resource function get notifications/[trello:TrelloID id]/board(map<string|string[]> headers = {}, BoardFields fields = "id", anydata Additional Values, GetNotificationsIdBoardQueries queries) returns InlineResponse2003|error;
+    resource function get notifications/[trello:TrelloID id]/board(map<string|string[]> headers = {}, BoardFields fields = "id", GetNotificationsIdBoardQueries queries) returns InlineResponse2003|error;
 
     # Get the Card a Notification is on
     # 
-    resource function get notifications/[trello:TrelloID id]/card(map<string|string[]> headers = {}, CardFields fields = "id", anydata Additional Values, GetNotificationsIdCardQueries queries) returns InlineResponse2004|error;
+    resource function get notifications/[trello:TrelloID id]/card(map<string|string[]> headers = {}, CardFields fields = "id", GetNotificationsIdCardQueries queries) returns InlineResponse2004|error;
 
     # Get the List a Notification is on
     # 
-    resource function get notifications/[trello:TrelloID id]/list(map<string|string[]> headers = {}, ListFields fields = "id", anydata Additional Values, GetNotificationsIdListQueries queries) returns InlineResponse2005|error;
+    resource function get notifications/[trello:TrelloID id]/list(map<string|string[]> headers = {}, ListFields fields = "id", GetNotificationsIdListQueries queries) returns InlineResponse2005|error;
 
     # Get the Member a Notification is about (not the creator)
     # 
-    resource function get notifications/[trello:TrelloID id]/member(map<string|string[]> headers = {}, MemberFields fields = "id", anydata Additional Values, NotificationsidmemberQueries queries) returns InlineResponseItems2006|error;
+    resource function get notifications/[trello:TrelloID id]/member(map<string|string[]> headers = {}, MemberFields fields = "id", NotificationsidmemberQueries queries) returns InlineResponseItems2006|error;
 
     # Get the Member who created the Notification
     # 
-    resource function get notifications/[trello:TrelloID id]/memberCreator(map<string|string[]> headers = {}, MemberFields fields = "id", anydata Additional Values, GetNotificationsIdMembercreatorQueries queries) returns InlineResponseItems2006|error;
+    resource function get notifications/[trello:TrelloID id]/memberCreator(map<string|string[]> headers = {}, MemberFields fields = "id", GetNotificationsIdMembercreatorQueries queries) returns InlineResponseItems2006|error;
 
     # Get a Notification's associated Organization
     # 
-    resource function get notifications/[trello:TrelloID id]/organization(map<string|string[]> headers = {}, OrganizationFields fields = "id", anydata Additional Values, GetNotificationsIdOrganizationQueries queries) returns InlineResponse2006|error;
+    resource function get notifications/[trello:TrelloID id]/organization(map<string|string[]> headers = {}, OrganizationFields fields = "id", GetNotificationsIdOrganizationQueries queries) returns InlineResponse2006|error;
 
     # Create a new Organization
     # 
-    resource function post organizations(map<string|string[]> headers = {}, string website = "", string displayName = "", string name = "", string desc = "", anydata Additional Values, PostOrganizationsQueries queries) returns InlineResponse2006|error;
+    resource function post organizations(map<string|string[]> headers = {}, string website = "", string displayName = "", string name = "", string desc = "", PostOrganizationsQueries queries) returns InlineResponse2006|error;
 
     # Get an Organization
     # 
@@ -4213,7 +4333,7 @@
 
     # Update an Organization
     # 
-    resource function put organizations/[trello:TrelloID id](map<string|string[]> headers = {}, string website = "", boolean prefs\/externalMembersDisabled = false, string prefs\/permissionLevel = "", string displayName = "", string name = "", string prefs\/boardVisibilityRestrict\/private = "", string prefs\/associatedDomain = "", string prefs\/boardVisibilityRestrict\/org = "", int:Signed32 prefs\/googleAppsVersion = 0, string prefs\/boardVisibilityRestrict\/public = "", string prefs\/orgInviteRestrict = "", string desc = "", anydata Additional Values, PutOrganizationsIdQueries queries) returns Organization|error;
+    resource function put organizations/[trello:TrelloID id](map<string|string[]> headers = {}, string website = "", boolean prefs\/externalMembersDisabled = false, string prefs\/permissionLevel = "", string displayName = "", string name = "", string prefs\/boardVisibilityRestrict\/private = "", string prefs\/associatedDomain = "", string prefs\/boardVisibilityRestrict\/org = "", int:Signed32 prefs\/googleAppsVersion = 0, string prefs\/boardVisibilityRestrict\/public = "", string prefs\/orgInviteRestrict = "", string desc = "", PutOrganizationsIdQueries queries) returns Organization|error;
 
     # Delete an Organization
     # 
@@ -4229,7 +4349,7 @@
 
     # Get Boards in an Organization
     # 
-    resource function get organizations/[trello:TrelloID id]/boards(map<string|string[]> headers = {}, "all"|"open"|"closed"|"members"|"organization"|"public" filter = "all", BoardFields fields = "id", anydata Additional Values, GetOrganizationsIdBoardsQueries queries) returns InlineResponseItems2009[]|error;
+    resource function get organizations/[trello:TrelloID id]/boards(map<string|string[]> headers = {}, "all"|"open"|"closed"|"members"|"organization"|"public" filter = "all", BoardFields fields = "id", GetOrganizationsIdBoardsQueries queries) returns InlineResponseItems2009[]|error;
 
     # Retrieve Organization's Exports
     # 
@@ -4237,7 +4357,7 @@
 
     # Create Export for Organizations
     # 
-    resource function post organizations/[trello:TrelloID id]/exports(map<string|string[]> headers = {}, boolean attachments = false, anydata Additional Values, PostOrganizationsIdExportsQueries queries) returns Export|error;
+    resource function post organizations/[trello:TrelloID id]/exports(map<string|string[]> headers = {}, boolean attachments = false, PostOrganizationsIdExportsQueries queries) returns Export|error;
 
     # Get the Members of an Organization
     # 
@@ -4245,15 +4365,15 @@
 
     # Update an Organization's Members
     # 
-    resource function put organizations/[trello:TrelloID id]/members(map<string|string[]> headers = {}, string fullName = "", "admin"|"normal" type = "admin", string email = "", anydata Additional Values, PutOrganizationsIdMembersQueries queries) returns error?;
+    resource function put organizations/[trello:TrelloID id]/members(map<string|string[]> headers = {}, string fullName = "", "admin"|"normal" type = "admin", string email = "", PutOrganizationsIdMembersQueries queries) returns error?;
 
     # Get Memberships of an Organization
     # 
-    resource function get organizations/[trello:TrelloID id]/memberships(map<string|string[]> headers = {}, "all"|"active"|"admin"|"deactivated"|"me"|"normal" filter = "all", boolean member = false, anydata Additional Values, GetOrganizationsIdMembershipsQueries queries) returns InlineResponseItems20011[]|error;
+    resource function get organizations/[trello:TrelloID id]/memberships(map<string|string[]> headers = {}, "all"|"active"|"admin"|"deactivated"|"me"|"normal" filter = "all", boolean member = false, GetOrganizationsIdMembershipsQueries queries) returns InlineResponseItems20011[]|error;
 
     # Get a Membership of an Organization
     # 
-    resource function get organizations/[trello:TrelloID id]/memberships/[trello:TrelloID idMembership](map<string|string[]> headers = {}, boolean member = false, anydata Additional Values, GetOrganizationsIdMembershipsIdmembershipQueries queries) returns InlineResponseItems20011|error;
+    resource function get organizations/[trello:TrelloID id]/memberships/[trello:TrelloID idMembership](map<string|string[]> headers = {}, boolean member = false, GetOrganizationsIdMembershipsIdmembershipQueries queries) returns InlineResponseItems20011|error;
 
     # Get the pluginData Scoped to Organization
     # 
@@ -4269,7 +4389,7 @@
 
     # Update a Member of an Organization
     # 
-    resource function put organizations/[trello:TrelloID id]/members/[trello:IdMember idMember](map<string|string[]> headers = {}, "admin"|"normal" type = "admin", anydata Additional Values, PutOrganizationsIdMembersIdmemberQueries queries) returns InlineResponseItems20010|error;
+    resource function put organizations/[trello:TrelloID id]/members/[trello:IdMember idMember](map<string|string[]> headers = {}, "admin"|"normal" type = "admin", PutOrganizationsIdMembersIdmemberQueries queries) returns InlineResponseItems20010|error;
 
     # Remove a Member from an Organization
     # 
@@ -4277,11 +4397,11 @@
 
     # Deactivate or reactivate a member of an Organization
     # 
-    resource function put organizations/[trello:TrelloID id]/members/[trello:IdMember1 idMember]/deactivated(map<string|string[]> headers = {}, boolean value = false, anydata Additional Values, PutOrganizationsIdMembersIdmemberDeactivatedQueries queries) returns error?;
+    resource function put organizations/[trello:TrelloID id]/members/[trello:IdMember1 idMember]/deactivated(map<string|string[]> headers = {}, boolean value = false, PutOrganizationsIdMembersIdmemberDeactivatedQueries queries) returns error?;
 
     # Update logo for an Organization
     # 
-    resource function post organizations/[trello:TrelloID id]/logo(map<string|string[]> headers = {}, record {|byte[] fileContent; string fileName; anydata...;|} file = {fileContent: [], fileName: ""}, anydata Additional Values, PostOrganizationsIdLogoQueries queries) returns InlineResponse2006|error;
+    resource function post organizations/[trello:TrelloID id]/logo(map<string|string[]> headers = {}, record {|byte[] fileContent; string fileName; anydata...;|} file = {fileContent: [], fileName: ""}, PostOrganizationsIdLogoQueries queries) returns InlineResponse2006|error;
 
     # Delete Logo for Organization
     # 
@@ -4325,17 +4445,17 @@
 
     # Search Trello
     # 
-    resource function get search(map<string|string[]> headers = {}, string cardFields = "", boolean cardMembers = false, string memberFields = "", string query = "", boolean cardBoard = false, boolean cardList = false, boolean boardOrganization = false, string modelTypes = "", int boardsLimit = 0, string boardFields = "", boolean cardStickers = false, string organizationFields = "", int:Signed32 organizationsLimit = 0, string idCards = "", int:Signed32 membersLimit = 0, IdBoards idBoards = "mine", string idOrganizations = "", decimal cardsPage = 0.0d, boolean partial = false, int cardsLimit = 0, string cardAttachments = "", anydata Additional Values, GetSearchQueries queries) returns InlineResponseItems20014[]|error;
+    resource function get search(map<string|string[]> headers = {}, string cardFields = "", boolean cardMembers = false, string memberFields = "", string query = "", boolean cardBoard = false, boolean cardList = false, boolean boardOrganization = false, string modelTypes = "", int boardsLimit = 0, string boardFields = "", boolean cardStickers = false, string organizationFields = "", int:Signed32 organizationsLimit = 0, string idCards = "", int:Signed32 membersLimit = 0, IdBoards idBoards = "mine", string idOrganizations = "", decimal cardsPage = 0.0d, boolean partial = false, int cardsLimit = 0, string cardAttachments = "", GetSearchQueries queries) returns InlineResponseItems20014[]|error;
 
-    resource function get search/members(map<string|string[]> headers = {}, TrelloID idBoard = "", boolean onlyOrgMembers = false, string query = "", int:Signed32 limit = 0, TrelloID idOrganization = "", anydata Additional Values, GetSearchMembersQueries queries) returns Member[]|error;
+    resource function get search/members(map<string|string[]> headers = {}, TrelloID idBoard = "", boolean onlyOrgMembers = false, string query = "", int:Signed32 limit = 0, TrelloID idOrganization = "", GetSearchMembersQueries queries) returns Member[]|error;
 
     # Get a Token
     # 
-    resource function get tokens/[string token](map<string|string[]> headers = {}, boolean webhooks = false, TokenFields fields = "identifier", anydata Additional Values, GetTokensTokenQueries queries) returns Token|error;
+    resource function get tokens/[string token](map<string|string[]> headers = {}, boolean webhooks = false, TokenFields fields = "identifier", GetTokensTokenQueries queries) returns Token|error;
 
     # Get Token's Member
     # 
-    resource function get tokens/[string token]/member(map<string|string[]> headers = {}, MemberFields fields = "id", anydata Additional Values, GetTokensTokenMemberQueries queries) returns Member|error;
+    resource function get tokens/[string token]/member(map<string|string[]> headers = {}, MemberFields fields = "id", GetTokensTokenMemberQueries queries) returns Member|error;
 
     # Get Webhooks for Token
     # 
@@ -4343,7 +4463,7 @@
 
     # Create Webhooks for Token
     # 
-    resource function post tokens/[string token]/webhooks(map<string|string[]> headers = {}, string description = "", string callbackURL = "", TrelloID idModel = "", anydata Additional Values, PostTokensTokenWebhooksQueries queries) returns Webhook|error;
+    resource function post tokens/[string token]/webhooks(map<string|string[]> headers = {}, string description = "", string callbackURL = "", TrelloID idModel = "", PostTokensTokenWebhooksQueries queries) returns Webhook|error;
 
     # Get a Webhook belonging to a Token
     # 
@@ -4351,7 +4471,7 @@
 
     # Update a Webhook created by Token
     # 
-    resource function put tokens/[string token]/webhooks/[trello:TrelloID idWebhook](map<string|string[]> headers = {}, string description = "", string callbackURL = "", TrelloID idModel = "", anydata Additional Values, Tokenstokenwebhooks1Queries queries) returns error?;
+    resource function put tokens/[string token]/webhooks/[trello:TrelloID idWebhook](map<string|string[]> headers = {}, string description = "", string callbackURL = "", TrelloID idModel = "", Tokenstokenwebhooks1Queries queries) returns error?;
 
     # Delete a Webhook created by Token
     # 
@@ -4359,7 +4479,7 @@
 
     resource function delete tokens/[string token](map<string|string[]> headers = {}) returns error?;
 
-    resource function post webhooks(map<string|string[]> headers = {}, string description = "", boolean active = false, string callbackURL = "", TrelloID idModel = "", anydata Additional Values, PostWebhooksQueries queries) returns Webhook|error;
+    resource function post webhooks(map<string|string[]> headers = {}, string description = "", boolean active = false, string callbackURL = "", TrelloID idModel = "", PostWebhooksQueries queries) returns Webhook|error;
 
     # Get a Webhook
     # 
@@ -4367,7 +4487,7 @@
 
     # Update a Webhook
     # 
-    resource function put webhooks/[trello:TrelloID id](map<string|string[]> headers = {}, string description = "", boolean active = false, string callbackURL = "", TrelloID idModel = "", anydata Additional Values, PutWebhooksIdQueries queries) returns Webhook|error;
+    resource function put webhooks/[trello:TrelloID id](map<string|string[]> headers = {}, string description = "", boolean active = false, string callbackURL = "", TrelloID idModel = "", PutWebhooksIdQueries queries) returns Webhook|error;
 
     # Delete a Webhook
     # 
`````
