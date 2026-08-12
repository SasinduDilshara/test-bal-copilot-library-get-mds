# slack — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `slack` |
| **Old file** | `slack/old/ballerinax_slack.bal.txt` |
| **New file** | `slack/new/ballerinax_slack.bal.txt` |
| **Old lines** | 5041 |
| **New lines** | 5754 |
| **Lines added** | 845 |
| **Lines removed** | 132 |
| **Hunks** | 202 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 31 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 67 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (31)

- `type AppIdDef`
- `type Blocks`
- `type BotIdDef`
- `type ChannelActionsTsAnyOf1`
- `type ChannelDef`
- `type ChannelIdDef`
- `type ChannelNameDef`
- `type CommentIdDef`
- `type CommentsObj`
- `type ConversationObj`
- `type DiscoverableDiscoverableAnyOf12`
- `type DmIdDef`
- `type EnterpriseIdDef`
- `type EnterpriseNameDef`
- `type EnterpriseUserIdDef`
- `type FileIdDef`
- `type GroupIdDef`
- `type OkTrueDef`
- `type OptionalAppIdDef`
- `type ReminderIdDef`
- `type ResponseMetadataObj`
- `type ScopesObj`
- `type SubteamIdDef`
- `type TeamDef`
- `type TopicPurposeCreatorDef`
- `type TsDef`
- `type TzTzAnyOf112`
- `type TzTzAnyOf12`
- `type UserIdDef`
- `type UserObj`
- `type WorkspaceIdDef`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 119–211 | 119–263 | Types | +57 | −5 |
| 2 | 213–219 | 265–273 | Types | +2 | −0 |
| 3 | 221–254 | 275–326 | Types | +18 | −0 |
| 4 | 260–272 | 332–352 | Types | +8 | −0 |
| 5 | 280–342 | 360–448 | Types | +31 | −5 |
| 6 | 349–446 | 455–613 | Types | +61 | −0 |
| 7 | 450–468 | 617–639 | Types | +9 | −5 |
| 8 | 471–493 | 642–668 | Types | +8 | −4 |
| 9 | 497–603 | 672–829 | Types | +55 | −4 |
| 10 | 605–610 | 831–837 | Types | +1 | −0 |
| 11 | 612–618 | 839–847 | Types | +2 | −0 |
| 12 | 620–660 | 849–906 | Types | +19 | −2 |
| 13 | 663–692 | 909–943 | Types | +10 | −5 |
| 14 | 695–701 | 946–952 | Types | +1 | −1 |
| 15 | 703–710 | 954–963 | Types | +2 | −0 |
| 16 | 713–723 | 966–978 | Types | +2 | −0 |
| 17 | 728–786 | 983–1077 | Types | +37 | −1 |
| 18 | 792–803 | 1083–1097 | Types | +3 | −0 |
| 19 | 810–817 | 1104–1113 | Types | +2 | −0 |
| 20 | 825–835 | 1121–1137 | Types | +6 | −0 |
| 21 | 849–859 | 1151–1162 | Types | +2 | −1 |
| 22 | 875–881 | 1178–1184 | Types | +1 | −1 |
| 23 | 903–908 | 1206–1212 | Types | +1 | −0 |
| 24 | 910–915 | 1214–1220 | Types | +1 | −0 |
| 25 | 922–959 | 1227–1279 | Types | +17 | −2 |
| 26 | 961–979 | 1281–1303 | Types | +5 | −1 |
| 27 | 984–997 | 1308–1325 | Types | +4 | −0 |
| 28 | 1003–1016 | 1331–1348 | Types | +4 | −0 |
| 29 | 1037–1048 | 1369–1384 | Types | +4 | −0 |
| 30 | 1050–1062 | 1386–1402 | Types | +5 | −1 |
| 31 | 1068–1075 | 1408–1417 | Types | +2 | −0 |
| 32 | 1079–1088 | 1421–1432 | Types | +2 | −0 |
| 33 | 1090–1095 | 1434–1440 | Types | +1 | −0 |
| 34 | 1125–1135 | 1470–1482 | Types | +2 | −0 |
| 35 | 1138–1145 | 1485–1494 | Types | +2 | −0 |
| 36 | 1149–1168 | 1498–1522 | Types | +6 | −1 |
| 37 | 1174–1179 | 1528–1534 | Types | +1 | −0 |
| 38 | 1182–1192 | 1537–1549 | Types | +2 | −0 |
| 39 | 1198–1218 | 1555–1585 | Types | +10 | −0 |
| 40 | 1236–1241 | 1603–1609 | Types | +1 | −0 |
| 41 | 1262–1279 | 1630–1653 | Types | +6 | −0 |
| 42 | 1302–1323 | 1676–1704 | Types | +7 | −0 |
| 43 | 1330–1349 | 1711–1734 | Types | +4 | −0 |
| 44 | 1382–1395 | 1767–1784 | Types | +4 | −0 |
| 45 | 1404–1409 | 1793–1799 | Types | +1 | −0 |
| 46 | 1413–1422 | 1803–1813 | Types | +2 | −1 |
| 47 | 1429–1434 | 1820–1826 | Types | +1 | −0 |
| 48 | 1437–1442 | 1829–1835 | Types | +1 | −0 |
| 49 | 1447–1461 | 1840–1857 | Types | +4 | −1 |
| 50 | 1465–1473 | 1861–1869 | Types | +2 | −2 |
| 51 | 1495–1500 | 1891–1897 | Types | +1 | −0 |
| 52 | 1502–1511 | 1899–1910 | Types | +2 | −0 |
| 53 | 1516–1521 | 1915–1921 | Types | +1 | −0 |
| 54 | 1556–1561 | 1956–1962 | Types | +1 | −0 |
| 55 | 1576–1607 | 1977–2028 | Types | +20 | −0 |
| 56 | 1609–1634 | 2030–2061 | Types | +9 | −3 |
| 57 | 1638–1647 | 2065–2077 | Types | +3 | −0 |
| 58 | 1686–1697 | 2116–2129 | Types | +2 | −0 |
| 59 | 1700–1718 | 2132–2153 | Types | +4 | −1 |
| 60 | 1721–1726 | 2156–2162 | Types | +1 | −0 |
| 61 | 1730–1737 | 2166–2175 | Types | +2 | −0 |
| 62 | 1748–1753 | 2186–2192 | Types | +1 | −0 |
| 63 | 1771–1789 | 2210–2233 | Types | +5 | −0 |
| 64 | 1792–1799 | 2236–2245 | Types | +2 | −0 |
| 65 | 1806–1811 | 2252–2258 | Types | +1 | −0 |
| 66 | 1815–1820 | 2262–2268 | Types | +1 | −0 |
| 67 | 1822–1844 | 2270–2298 | Types | +7 | −1 |
| 68 | 1863–1869 | 2317–2325 | Types | +2 | −0 |
| 69 | 1876–1885 | 2332–2344 | Types | +3 | −0 |
| 70 | 1911–1930 | 2370–2395 | Types | +6 | −0 |
| 71 | 1958–1967 | 2423–2435 | Types | +3 | −0 |
| 72 | 1975–1980 | 2443–2449 | Types | +1 | −0 |
| 73 | 1991–1998 | 2460–2470 | Types | +3 | −0 |
| 74 | 2001–2031 | 2473–2523 | Types | +20 | −0 |
| 75 | 2033–2044 | 2525–2537 | Types | +3 | −2 |
| 76 | 2050–2059 | 2543–2555 | Types | +3 | −0 |
| 77 | 2073–2079 | 2569–2575 | Types | +1 | −1 |
| 78 | 2102–2111 | 2598–2610 | Types | +3 | −0 |
| 79 | 2117–2122 | 2616–2622 | Types | +1 | −0 |
| 80 | 2143–2152 | 2643–2654 | Types | +2 | −0 |
| 81 | 2154–2161 | 2656–2666 | Types | +3 | −0 |
| 82 | 2163–2180 | 2668–2690 | Types | +5 | −0 |
| 83 | 2194–2209 | 2704–2723 | Types | +4 | −0 |
| 84 | 2216–2223 | 2730–2739 | Types | +2 | −0 |
| 85 | 2225–2233 | 2741–2750 | Types | +2 | −1 |
| 86 | 2243–2248 | 2760–2766 | Types | +1 | −0 |
| 87 | 2258–2266 | 2776–2788 | Types | +4 | −0 |
| 88 | 2291–2304 | 2813–2829 | Types | +3 | −0 |
| 89 | 2312–2326 | 2837–2854 | Types | +3 | −0 |
| 90 | 2353–2360 | 2881–2890 | Types | +2 | −0 |
| 91 | 2376–2383 | 2906–2915 | Types | +2 | −0 |
| 92 | 2415–2428 | 2947–2969 | Types | +9 | −0 |
| 93 | 2431–2436 | 2972–2978 | Types | +1 | −0 |
| 94 | 2464–2478 | 3006–3024 | Types | +4 | −0 |
| 95 | 2486–2495 | 3032–3044 | Types | +3 | −0 |
| 96 | 2527–2532 | 3076–3082 | Types | +1 | −0 |
| 97 | 2537–2549 | 3087–3102 | Types | +3 | −0 |
| 98 | 2576–2595 | 3129–3154 | Types | +6 | −0 |
| 99 | 2611–2616 | 3170–3176 | Types | +1 | −0 |
| 100 | 2622–2634 | 3182–3200 | Types | +6 | −0 |
| 101 | 2636–2641 | 3202–3208 | Types | +1 | −0 |
| 102 | 2651–2688 | 3218–3265 | Types | +10 | −0 |
| 103 | 2693–2718 | 3270–3303 | Types | +8 | −0 |
| 104 | 2724–2729 | 3309–3315 | Types | +1 | −0 |
| 105 | 2744–2750 | 3330–3336 | Types | +1 | −1 |
| 106 | 2761–2766 | 3347–3353 | Types | +1 | −0 |
| 107 | 2835–2848 | 3422–3438 | Types | +3 | −0 |
| 108 | 2878–2883 | 3468–3474 | Types | +1 | −0 |
| 109 | 2885–2898 | 3476–3497 | Types | +8 | −0 |
| 110 | 2902–2911 | 3501–3512 | Types | +2 | −0 |
| 111 | 2943–2948 | 3544–3550 | Types | +1 | −0 |
| 112 | 2959–2964 | 3561–3567 | Types | +1 | −0 |
| 113 | 2985–2990 | 3588–3594 | Types | +1 | −0 |
| 114 | 3011–3017 | 3615–3623 | Types | +2 | −0 |
| 115 | 3040–3051 | 3646–3661 | Types | +4 | −0 |
| 116 | 3058–3063 | 3668–3674 | Types | +1 | −0 |
| 117 | 3081–3096 | 3692–3711 | Types | +4 | −0 |
| 118 | 3115–3163 | 3730–3802 | Types | +25 | −1 |
| 119 | 3173–3178 | 3812–3818 | Types | +1 | −0 |
| 120 | 3196–3201 | 3836–3842 | Types | +1 | −0 |
| 121 | 3228–3233 | 3869–3875 | Types | +1 | −0 |
| 122 | 3241–3246 | 3883–3889 | Types | +1 | −0 |
| 123 | 3252–3257 | 3895–3901 | Types | +1 | −0 |
| 124 | 3309–3314 | 3953–3959 | Types | +1 | −0 |
| 125 | 3337–3348 | 3982–3997 | Types | +4 | −0 |
| 126 | 3368–3379 | 4017–4029 | Types | +2 | −1 |
| 127 | 3386–3398 | 4036–4050 | Types | +3 | −1 |
| 128 | 3410–3419 | 4062–4074 | Types | +3 | −0 |
| 129 | 3421–3426 | 4076–4082 | Types | +1 | −0 |
| 130 | 3457–3462 | 4113–4119 | Types | +1 | −0 |
| 131 | 3465–3474 | 4122–4134 | Types | +3 | −0 |
| 132 | 3553–3564 | 4213–4226 | Types | +2 | −0 |
| 133 | 3580–3585 | 4242–4248 | Types | +1 | −0 |
| 134 | 3610–3615 | 4273–4279 | Types | +1 | −0 |
| 135 | 3621–3626 | 4285–4291 | Types | +1 | −0 |
| 136 | 3689–3694 | 4354–4360 | Types | +1 | −0 |
| 137 | 3703–3710 | 4369–4378 | Types | +2 | −0 |
| 138 | 3713–3719 | 4381–4388 | Types | +2 | −1 |
| 139 | 3727–3738 | 4396–4410 | Types | +3 | −0 |
| 140 | 3743–3756 | 4415–4433 | Types | +5 | −0 |
| 141 | 3770–3775 | 4447–4453 | Types | +1 | −0 |
| 142 | 3788–3795 | 4466–4475 | Types | +2 | −0 |
| 143 | 3830–3835 | 4510–4516 | Types | +1 | −0 |
| 144 | 3861–3868 | 4542–4551 | Types | +2 | −0 |
| 145 | 3875–3886 | 4558–4573 | Types | +4 | −0 |
| 146 | 3906–3917 | 4593–4607 | Types | +3 | −0 |
| 147 | 3930–3935 | 4620–4626 | Types | +1 | −0 |
| 148 | 3971–3980 | 4662–4672 | Types | +2 | −1 |
| 149 | 4024–4029 | 4716–4722 | Types | +1 | −0 |
| 150 | 4071–4076 | 4764–4770 | Types | +1 | −0 |
| 151 | 4081–4090 | 4775–4789 | Types | +5 | −0 |
| 152 | 4092–4103 | 4791–4805 | Types | +3 | −0 |
| 153 | 4131–4136 | 4833–4839 | Types | +1 | −0 |
| 154 | 4155–4160 | 4858–4864 | Types | +1 | −0 |
| 155 | 4163–4168 | 4867–4873 | Types | +1 | −0 |
| 156 | 4219–4226 | 4924–4933 | Types | +2 | −0 |
| 157 | 4241–4247 | 4948–4956 | Types | +2 | −0 |
| 158 | 4257–4262 | 4966–4972 | Types | +1 | −0 |
| 159 | 4266–4271 | 4976–4982 | Types | +1 | −0 |
| 160 | 4305–4310 | 5016–5022 | Types | +1 | −0 |
| 161 | 4318–4323 | 5030–5036 | Types | +1 | −0 |
| 162 | 4349–4359 | 5062–5072 | Client | +2 | −2 |
| 163 | 4361–4367 | 5074–5080 | Client | +1 | −1 |
| 164 | 4385–4399 | 5098–5112 | Client | +3 | −3 |
| 165 | 4409–4415 | 5122–5128 | Client | +1 | −1 |
| 166 | 4417–4423 | 5130–5136 | Client | +1 | −1 |
| 167 | 4441–4447 | 5154–5160 | Client | +1 | −1 |
| 168 | 4457–4467 | 5170–5180 | Client | +2 | −2 |
| 169 | 4469–4479 | 5182–5192 | Client | +2 | −2 |
| 170 | 4481–4495 | 5194–5208 | Client | +3 | −3 |
| 171 | 4521–4527 | 5234–5240 | Client | +1 | −1 |
| 172 | 4537–4543 | 5250–5256 | Client | +1 | −1 |
| 173 | 4569–4579 | 5282–5292 | Client | +2 | −2 |
| 174 | 4581–4591 | 5294–5304 | Client | +2 | −2 |
| 175 | 4593–4611 | 5306–5324 | Client | +4 | −4 |
| 176 | 4613–4619 | 5326–5332 | Client | +1 | −1 |
| 177 | 4625–4631 | 5338–5344 | Client | +1 | −1 |
| 178 | 4649–4655 | 5362–5368 | Client | +1 | −1 |
| 179 | 4669–4675 | 5382–5388 | Client | +1 | −1 |
| 180 | 4693–4703 | 5406–5416 | Client | +2 | −2 |
| 181 | 4717–4723 | 5430–5436 | Client | +1 | −1 |
| 182 | 4725–4731 | 5438–5444 | Client | +1 | −1 |
| 183 | 4737–4743 | 5450–5456 | Client | +1 | −1 |
| 184 | 4753–4759 | 5466–5472 | Client | +1 | −1 |
| 185 | 4765–4771 | 5478–5484 | Client | +1 | −1 |
| 186 | 4773–4779 | 5486–5492 | Client | +1 | −1 |
| 187 | 4789–4799 | 5502–5512 | Client | +2 | −2 |
| 188 | 4801–4811 | 5514–5524 | Client | +2 | −2 |
| 189 | 4813–4819 | 5526–5532 | Client | +1 | −1 |
| 190 | 4833–4851 | 5546–5564 | Client | +4 | −4 |
| 191 | 4853–4859 | 5566–5572 | Client | +1 | −1 |
| 192 | 4865–4875 | 5578–5588 | Client | +2 | −2 |
| 193 | 4889–4895 | 5602–5608 | Client | +1 | −1 |
| 194 | 4897–4907 | 5610–5620 | Client | +2 | −2 |
| 195 | 4909–4915 | 5622–5628 | Client | +1 | −1 |
| 196 | 4917–4939 | 5630–5652 | Client | +5 | −5 |
| 197 | 4949–4955 | 5662–5668 | Client | +1 | −1 |
| 198 | 4957–4963 | 5670–5676 | Client | +1 | −1 |
| 199 | 4965–4971 | 5678–5684 | Client | +1 | −1 |
| 200 | 4973–4979 | 5686–5692 | Client | +1 | −1 |
| 201 | 4981–4999 | 5694–5712 | Client | +4 | −4 |
| 202 | 5013–5041 | 5726–5754 | Client | +7 | −7 |

---

## Unified diff

`````diff
--- slack/old/ballerinax_slack.bal.txt	2026-08-12 12:57:30
+++ slack/new/ballerinax_slack.bal.txt	2026-08-12 13:19:19
@@ -119,93 +119,145 @@
     # A [view payload](/reference/surfaces/views). This must be a JSON-encoded string
     string view;
     # Exchange a trigger to post to the user
+    @http:Query {name: "trigger_id"}
     string triggerId;
 };
 
 
 type ConversationObject record {
+    @jsondata:Name {value: "is_global_shared"}
     boolean isGlobalShared?;
+    @jsondata:Name {value: "is_pending_ext_shared"}
     boolean isPendingExtShared?;
+    @jsondata:Name {value: "pending_shared"}
     TeamDef[] pendingShared?;
+    @jsondata:Name {value: "internal_team_ids"}
     TeamDef[] internalTeamIds?;
+    @jsondata:Name {value: "is_channel"}
     boolean isChannel;
     UserIdDef[] members?;
+    @jsondata:Name {value: "is_non_threadable"}
     boolean isNonThreadable?;
+    @jsondata:Name {value: "pin_count"}
     int pinCount?;
+    @jsondata:Name {value: "is_read_only"}
     boolean isReadOnly?;
     ChannelDef id;
+    @jsondata:Name {value: "is_org_default"}
     boolean isOrgDefault?;
+    @jsondata:Name {value: "is_org_mandatory"}
     boolean isOrgMandatory?;
+    @jsondata:Name {value: "is_im"}
     boolean isIm;
+    @jsondata:Name {value: "is_member"}
     boolean isMember?;
+    @jsondata:Name {value: "is_open"}
     boolean isOpen?;
     int created;
+    @jsondata:Name {value: "display_counts"}
     ConversationObjDisplayCounts displayCounts?;
     decimal priority?;
     int version?;
+    @jsondata:Name {value: "is_starred"}
     boolean isStarred?;
+    @jsondata:Name {value: "is_archived"}
     boolean isArchived;
     string name;
     ConversationObjTopic topic;
+    @jsondata:Name {value: "shared_team_ids"}
     TeamDef[] sharedTeamIds?;
+    @jsondata:Name {value: "is_org_shared"}
     boolean isOrgShared;
+    @jsondata:Name {value: "is_private"}
     boolean isPrivate;
+    @jsondata:Name {value: "accepted_user"}
     UserIdDef acceptedUser?;
+    @jsondata:Name {value: "conversation_host_id"}
     WorkspaceIdDef conversationHostId?;
     ConversationObjPurpose purpose;
+    @jsondata:Name {value: "is_moved"}
     int isMoved?;
     ConversationObjShares[] shares?;
+    @jsondata:Name {value: "unread_count"}
     int unreadCount?;
+    @jsondata:Name {value: "is_shared"}
     boolean isShared;
+    @jsondata:Name {value: "previous_names"}
     ChannelNameDef[] previousNames?;
+    @jsondata:Name {value: "connected_team_ids"}
     WorkspaceIdDef[] connectedTeamIds?;
+    @jsondata:Name {value: "pending_connected_team_ids"}
     TeamDef[] pendingConnectedTeamIds?;
     ConversationObjLatest[] latest?;
+    @jsondata:Name {value: "has_pins"}
     boolean hasPins?;
+    @jsondata:Name {value: "last_read"}
     TsDef lastRead?;
     UserIdDef creator;
+    @jsondata:Name {value: "is_frozen"}
     boolean isFrozen?;
+    @jsondata:Name {value: "is_mpim"}
     false isMpim;
+    @jsondata:Name {value: "timezone_count"}
     int timezoneCount?;
+    @jsondata:Name {value: "is_ext_shared"}
     boolean isExtShared?;
+    @jsondata:Name {value: "name_normalized"}
     string nameNormalized;
+    @jsondata:Name {value: "enterprise_id"}
     EnterpriseIdDef enterpriseId?;
+    @jsondata:Name {value: "unread_count_display"}
     int unreadCountDisplay?;
+    @jsondata:Name {value: "is_group"}
     boolean isGroup;
     int unlinked?;
+    @jsondata:Name {value: "use_case"}
     string useCase?;
+    @jsondata:Name {value: "is_general"}
     boolean isGeneral;
+    @jsondata:Name {value: "num_members"}
     int numMembers?;
+    @jsondata:Name {value: "is_thread_only"}
     boolean isThreadOnly?;
     UserIdDef user?;
+    @jsondata:Name {value: "parent_conversation"}
     ConversationObjParentConversation[] parentConversation?;
 };
 
-// Unknown type: TeamDef
+@constraint:String {pattern: re `^[T][A-Z0-9]{2,}$`}
+type TeamDef string;
 
-// Unknown type: UserIdDef
+@constraint:String {pattern: re `^[UW][A-Z0-9]{2,}$`}
+type UserIdDef string;
 
-// Unknown type: ChannelDef
+@constraint:String {pattern: re `^[CGD][A-Z0-9]{8,}$`}
+type ChannelDef string;
 
 
 type ConversationObjDisplayCounts record {
+    @jsondata:Name {value: "display_counts"}
     int displayCounts;
+    @jsondata:Name {value: "guest_counts"}
     int guestCounts;
 };
 
 
 type ConversationObjTopic record {
+    @jsondata:Name {value: "last_set"}
     int lastSet;
     TopicPurposeCreatorDef creator;
     string value;
 };
 
-// Unknown type: TopicPurposeCreatorDef
+@constraint:String {pattern: re `^[UW][A-Z0-9]{8,}$|^$`}
+type TopicPurposeCreatorDef string;
 
-// Unknown type: WorkspaceIdDef
+@constraint:String {pattern: re `^[TE][A-Z0-9]{8,}$`}
+type WorkspaceIdDef string;
 
 
 type ConversationObjPurpose record {
+    @jsondata:Name {value: "last_set"}
     int lastSet;
     TopicPurposeCreatorDef creator;
     string value;
@@ -213,7 +265,9 @@
 
 
 type ConversationObjShares record {
+    @jsondata:Name {value: "is_active"}
     boolean isActive;
+    @jsondata:Name {value: "accepted_user"}
     UserIdDef acceptedUser?;
     TeamObj team;
     UserIdDef user;
@@ -221,34 +275,52 @@
 
 
 type TeamObj record {
+    @jsondata:Name {value: "primary_owner"}
     PrimaryOwnerObj primaryOwner?;
+    @jsondata:Name {value: "is_enterprise"}
     int isEnterprise?;
     IconObj icon;
     string? description?;
+    @jsondata:Name {value: "msg_edit_window_mins"}
     int msgEditWindowMins?;
+    @jsondata:Name {value: "avatar_base_url"}
     string avatarBaseUrl?;
+    @jsondata:Name {value: "sso_provider"}
     TeamObjSsoProvider ssoProvider?;
     string locale?;
     boolean archived?;
+    @jsondata:Name {value: "messages_count"}
     int messagesCount?;
+    @jsondata:Name {value: "pay_prod_cur"}
     string payProdCur?;
     WorkspaceIdDef id;
+    @jsondata:Name {value: "is_over_storage_limit"}
     boolean isOverStorageLimit?;
     ""|"std"|"plus"|"compliance"|"enterprise" plan?;
+    @jsondata:Name {value: "external_org_migrations"}
     ExternalOrgMigrationsObj externalOrgMigrations?;
+    @jsondata:Name {value: "over_integrations_limit"}
     boolean overIntegrationsLimit?;
     int created?;
+    @jsondata:Name {value: "is_assigned"}
     boolean isAssigned?;
+    @jsondata:Name {value: "limit_ts"}
     int limitTs?;
+    @jsondata:Name {value: "enterprise_id"}
     EnterpriseIdDef enterpriseId?;
     boolean deleted?;
+    @jsondata:Name {value: "has_compliance_export"}
     boolean hasComplianceExport?;
+    @jsondata:Name {value: "date_create"}
     int dateCreate?;
     TeamObjDiscoverable[] discoverable?;
     string domain;
     string name;
+    @jsondata:Name {value: "email_domain"}
     string emailDomain;
+    @jsondata:Name {value: "enterprise_name"}
     EnterpriseNameDef enterpriseName?;
+    @jsondata:Name {value: "over_storage_limit"}
     boolean overStorageLimit?;
 };
 
@@ -260,13 +332,21 @@
 
 
 type IconObj record {
+    @jsondata:Name {value: "image_132"}
     string image132?;
+    @jsondata:Name {value: "image_102"}
     string image102?;
+    @jsondata:Name {value: "image_68"}
     string image68?;
+    @jsondata:Name {value: "image_default"}
     boolean imageDefault?;
+    @jsondata:Name {value: "image_34"}
     string image34?;
+    @jsondata:Name {value: "image_230"}
     string image230?;
+    @jsondata:Name {value: "image_44"}
     string image44?;
+    @jsondata:Name {value: "image_88"}
     string image88?;
 };
 
@@ -280,63 +360,89 @@
 
 type ExternalOrgMigrationsObj record {
     ExternalOrgMigrationsObjCurrent[] current;
+    @jsondata:Name {value: "date_updated"}
     int dateUpdated;
 };
 
 
 type ExternalOrgMigrationsObjCurrent record {
+    @jsondata:Name {value: "team_id"}
     string teamId;
+    @jsondata:Name {value: "date_started"}
     int dateStarted;
 };
 
-// Unknown type: EnterpriseIdDef
+@constraint:String {pattern: re `^[E][A-Z0-9]{8,}$`}
+type EnterpriseIdDef string;
 
 type DiscoverableAnyOf1 anydata|();
 
-// Unknown type: DiscoverableDiscoverableAnyOf12
+type DiscoverableDiscoverableAnyOf12 string;
 
-type TeamObjDiscoverable anydata|()|ballerinax/slack:5.0.1:DiscoverableDiscoverableAnyOf12;
+type TeamObjDiscoverable anydata|()|DiscoverableDiscoverableAnyOf12;
 
-// Unknown type: EnterpriseNameDef
+type EnterpriseNameDef string;
 
-// Unknown type: ChannelNameDef
+type ChannelNameDef string;
 
 
 type MessageObj record {
+    @constraint:Array {minLength: 1}
     MessageObjAttachments[] attachments?;
+    @jsondata:Name {value: "client_msg_id"}
     string clientMsgId?;
     string purpose?;
     boolean upload?;
+    @jsondata:Name {value: "is_intro"}
     boolean isIntro?;
+    @jsondata:Name {value: "user_profile"}
     UserProfileShortObj userProfile?;
     string 'type;
+    @jsondata:Name {value: "is_delayed_message"}
     boolean isDelayedMessage?;
     boolean subscribed?;
+    @jsondata:Name {value: "unread_count"}
     int unreadCount?;
     FileObj file?;
     string subtype?;
+    @jsondata:Name {value: "reply_users_count"}
     int replyUsersCount?;
     UserIdDef inviter?;
     string text;
+    @jsondata:Name {value: "display_as_bot"}
     boolean displayAsBot?;
+    @jsondata:Name {value: "bot_id"}
     MessageObjBotId[] botId?;
+    @jsondata:Name {value: "latest_reply"}
     TsDef latestReply?;
+    @jsondata:Name {value: "last_read"}
     TsDef lastRead?;
+    @jsondata:Name {value: "parent_user_id"}
     UserIdDef parentUserId?;
     # This is a very loose definition, in the future, we'll populate this with deeper schema in this definition namespace
     Blocks blocks?;
+    @jsondata:Name {value: "reply_users"}
     UserIdDef[] replyUsers?;
     WorkspaceIdDef team?;
     MessageObjIcons icons?;
+    @jsondata:Name {value: "reply_count"}
     int replyCount?;
+    @jsondata:Name {value: "user_team"}
     WorkspaceIdDef userTeam?;
+    @jsondata:Name {value: "pinned_to"}
     ChannelDef[] pinnedTo?;
+    @jsondata:Name {value: "is_starred"}
     boolean isStarred?;
+    @jsondata:Name {value: "bot_profile"}
     BotProfileObj botProfile?;
+    @jsondata:Name {value: "old_name"}
     string oldName?;
+    @jsondata:Name {value: "source_team"}
     WorkspaceIdDef sourceTeam?;
+    @jsondata:Name {value: "thread_ts"}
     TsDef threadTs?;
     string name?;
+    @constraint:Array {minLength: 1}
     FileObj[] files?;
     string topic?;
     CommentObj comment?;
@@ -349,98 +455,159 @@
 
 
 type MessageObjAttachments record {
+    @jsondata:Name {value: "image_height"}
     int imageHeight?;
+    @jsondata:Name {value: "image_url"}
     string imageUrl?;
     int id;
+    @jsondata:Name {value: "image_width"}
     int imageWidth?;
     string fallback?;
+    @jsondata:Name {value: "image_bytes"}
     int imageBytes?;
 };
 
 
 type UserProfileShortObj record {
+    @jsondata:Name {value: "is_ultra_restricted"}
     boolean isUltraRestricted;
+    @jsondata:Name {value: "is_restricted"}
     boolean isRestricted;
+    @jsondata:Name {value: "real_name_normalized"}
     string realNameNormalized?;
     string name;
+    @jsondata:Name {value: "real_name"}
     string realName;
     WorkspaceIdDef team;
+    @jsondata:Name {value: "avatar_hash"}
     string avatarHash;
+    @jsondata:Name {value: "display_name"}
     string displayName;
+    @jsondata:Name {value: "image_72"}
     string image72;
+    @jsondata:Name {value: "first_name"}
     string? firstName;
+    @jsondata:Name {value: "display_name_normalized"}
     string displayNameNormalized?;
 };
 
 
 type FileObj record {
     string filetype?;
+    @jsondata:Name {value: "thumb_360"}
     string thumb360?;
+    @jsondata:Name {value: "thumb_160"}
     string thumb160?;
+    @jsondata:Name {value: "date_delete"}
     int dateDelete?;
+    @jsondata:Name {value: "thumb_480"}
     string thumb480?;
+    @jsondata:Name {value: "pinned_info"}
     PinnedInfoDef pinnedInfo?;
+    @jsondata:Name {value: "thumb_800"}
     string thumb800?;
+    @jsondata:Name {value: "thumb_720"}
     string thumb720?;
+    @jsondata:Name {value: "non_owner_editable"}
     boolean nonOwnerEditable?;
+    @jsondata:Name {value: "thumb_960"}
     string thumb960?;
+    @jsondata:Name {value: "thumb_800_w"}
     int thumb800W?;
     string mode?;
+    @jsondata:Name {value: "external_url"}
     string externalUrl?;
+    @jsondata:Name {value: "is_tombstoned"}
     boolean isTombstoned?;
+    @jsondata:Name {value: "num_stars"}
     int numStars?;
+    @jsondata:Name {value: "image_exif_rotation"}
     int imageExifRotation?;
     FileIdDef id?;
     string state?;
+    @jsondata:Name {value: "thumb_64"}
     string thumb64?;
     int created?;
+    @jsondata:Name {value: "last_editor"}
     UserIdDef lastEditor?;
+    @jsondata:Name {value: "thumb_480_w"}
     int thumb480W?;
+    @jsondata:Name {value: "thumb_960_h"}
     int thumb960H?;
+    @jsondata:Name {value: "url_private_download"}
     string urlPrivateDownload?;
+    @jsondata:Name {value: "permalink_public"}
     string permalinkPublic?;
+    @jsondata:Name {value: "has_rich_preview"}
     boolean hasRichPreview?;
+    @jsondata:Name {value: "is_starred"}
     boolean isStarred?;
     ChannelIdDef[] channels?;
     int size?;
+    @jsondata:Name {value: "comments_count"}
     int commentsCount?;
     string name?;
     string permalink?;
+    @jsondata:Name {value: "public_url_shared"}
     boolean publicUrlShared?;
     int updated?;
+    @jsondata:Name {value: "original_w"}
     int originalW?;
+    @jsondata:Name {value: "thumb_480_h"}
     int thumb480H?;
+    @jsondata:Name {value: "thumb_720_w"}
     int thumb720W?;
     string preview?;
+    @jsondata:Name {value: "external_id"}
     string externalId?;
+    @jsondata:Name {value: "thumb_1024_h"}
     int thumb1024H?;
     string title?;
+    @jsondata:Name {value: "original_h"}
     int originalH?;
     DmIdDef[] ims?;
+    @jsondata:Name {value: "thumb_720_h"}
     int thumb720H?;
     FileObjShares shares?;
+    @jsondata:Name {value: "url_private"}
     string urlPrivate?;
+    @jsondata:Name {value: "thumb_960_w"}
     int thumb960W?;
+    @jsondata:Name {value: "display_as_bot"}
     boolean displayAsBot?;
     int timestamp?;
     UserIdDef editor?;
+    @jsondata:Name {value: "thumb_80"}
     string thumb80?;
     boolean editable?;
     GroupIdDef[] groups?;
+    @jsondata:Name {value: "is_external"}
     boolean isExternal?;
+    @jsondata:Name {value: "thumb_360_h"}
     int thumb360H?;
+    @jsondata:Name {value: "pretty_type"}
     string prettyType?;
+    @jsondata:Name {value: "external_type"}
     string externalType?;
+    @jsondata:Name {value: "user_team"}
     TeamDef userTeam?;
+    @jsondata:Name {value: "pinned_to"}
     ChannelDef[] pinnedTo?;
+    @jsondata:Name {value: "thumb_800_h"}
     int thumb800H?;
+    @jsondata:Name {value: "source_team"}
     TeamDef sourceTeam?;
+    @jsondata:Name {value: "is_public"}
     boolean isPublic?;
+    @jsondata:Name {value: "thumb_360_w"}
     int thumb360W?;
+    @jsondata:Name {value: "thumb_tiny"}
     string thumbTiny?;
     string mimetype?;
     ReactionObj[] reactions?;
+    @jsondata:Name {value: "thumb_1024_w"}
     int thumb1024W?;
+    @jsondata:Name {value: "thumb_1024"}
     string thumb1024?;
     string user?;
     string username?;
@@ -450,19 +617,23 @@
 type PinnedInfoDef record {
 };
 
-// Unknown type: FileIdDef
-
-// Unknown type: ChannelIdDef
+@constraint:String {pattern: re `^[F][A-Z0-9]{8,}$`}
+type FileIdDef string;
 
-// Unknown type: DmIdDef
+@constraint:String {pattern: re `^[C][A-Z0-9]{2,}$`}
+type ChannelIdDef string;
 
+@constraint:String {pattern: re `^[D][A-Z0-9]{8,}$`}
+type DmIdDef string;
 
+
 type FileObjShares record {
     record {||} 'private?;
     record {||} 'public?;
 };
 
-// Unknown type: GroupIdDef
+@constraint:String {pattern: re `^[G][A-Z0-9]{8,}$`}
+type GroupIdDef string;
 
 
 type ReactionObj record {
@@ -471,23 +642,27 @@
     UserIdDef[] users;
 };
 
-// Unknown type: BotIdDef
+@constraint:String {pattern: re `^B[A-Z0-9]{8,}$`}
+type BotIdDef string;
 
 type NilBotIdSetWhenDisplayAsBotIsFalse anydata|();
 
-type MessageObjBotId ballerinax/slack:5.0.1:BotIdDef|anydata|();
+type MessageObjBotId BotIdDef|anydata|();
 
-// Unknown type: TsDef
+@constraint:String {pattern: re `^\d{10}\.\d{6}$`}
+type TsDef string;
 
 
 type BlocksInner record {
     string 'type;
 };
 
-// Unknown type: Blocks
+# This is a very loose definition, in the future, we'll populate this with deeper schema in this definition namespace
+type Blocks BlocksInner[];
 
 
 type MessageObjIcons record {
+    @jsondata:Name {value: "image_64"}
     string image64?;
     string emoji?;
 };
@@ -497,107 +672,158 @@
     boolean deleted;
     string name;
     BotIdDef id;
+    @jsondata:Name {value: "team_id"}
     TeamDef teamId;
     BotProfileObjIcons icons;
+    @jsondata:Name {value: "app_id"}
     AppIdDef appId;
     int updated;
 };
 
 
 type BotProfileObjIcons record {
+    @jsondata:Name {value: "image_36"}
     string image36;
+    @jsondata:Name {value: "image_48"}
     string image48;
+    @jsondata:Name {value: "image_72"}
     string image72;
 };
 
-// Unknown type: AppIdDef
+@constraint:String {pattern: re `^A[A-Z0-9]{1,}$`}
+type AppIdDef string;
 
 
 type CommentObj record {
+    @jsondata:Name {value: "is_starred"}
     boolean isStarred?;
     int created;
+    @jsondata:Name {value: "num_stars"}
     int numStars?;
+    @jsondata:Name {value: "is_intro"}
     boolean isIntro;
+    @jsondata:Name {value: "pinned_info"}
     PinnedInfoDef pinnedInfo?;
     string comment;
     ReactionObj[] reactions?;
     CommentIdDef id;
     UserIdDef user;
+    @jsondata:Name {value: "pinned_to"}
     ChannelDef[] pinnedTo?;
     int timestamp;
 };
 
-// Unknown type: CommentIdDef
+@constraint:String {pattern: re `^Fc[A-Z0-9]{8,}$`}
+type CommentIdDef string;
 
 type LatestAnyOf21 anydata|();
 
-type ConversationObjLatest ballerinax/slack:5.0.1:MessageObj|anydata|();
+type ConversationObjLatest MessageObj|anydata|();
 
 type ParentConversationAnyOf2 anydata|();
 
-type ConversationObjParentConversation ballerinax/slack:5.0.1:ChannelDef|anydata|();
+type ConversationObjParentConversation ChannelDef|anydata|();
 
 
 type ConversationMPIMObject record {
+    @jsondata:Name {value: "is_pending_ext_shared"}
     boolean isPendingExtShared?;
+    @jsondata:Name {value: "pending_shared"}
     TeamDef[] pendingShared?;
+    @jsondata:Name {value: "internal_team_ids"}
     TeamDef[] internalTeamIds?;
+    @jsondata:Name {value: "is_channel"}
     boolean isChannel;
     UserIdDef[] members?;
+    @jsondata:Name {value: "is_non_threadable"}
     boolean isNonThreadable?;
+    @jsondata:Name {value: "pin_count"}
     int pinCount?;
+    @jsondata:Name {value: "is_read_only"}
     boolean isReadOnly?;
     ChannelDef id;
+    @jsondata:Name {value: "is_im"}
     boolean isIm;
+    @jsondata:Name {value: "is_member"}
     boolean isMember?;
+    @jsondata:Name {value: "is_open"}
     boolean isOpen?;
     int created;
+    @jsondata:Name {value: "display_counts"}
     ConversationObjDisplayCounts1 displayCounts?;
     decimal priority?;
     int version?;
+    @jsondata:Name {value: "is_starred"}
     boolean isStarred?;
+    @jsondata:Name {value: "is_archived"}
     boolean isArchived;
     string name;
     ConversationObjTopic1 topic;
+    @jsondata:Name {value: "shared_team_ids"}
     TeamDef[] sharedTeamIds?;
+    @jsondata:Name {value: "is_org_shared"}
     boolean isOrgShared;
+    @jsondata:Name {value: "is_private"}
     boolean isPrivate;
+    @jsondata:Name {value: "accepted_user"}
     UserIdDef acceptedUser?;
+    @jsondata:Name {value: "conversation_host_id"}
     WorkspaceIdDef conversationHostId?;
     ConversationObjPurpose1 purpose;
+    @jsondata:Name {value: "is_moved"}
     int isMoved?;
     ConversationObjShares1[] shares?;
+    @jsondata:Name {value: "unread_count"}
     int unreadCount?;
+    @jsondata:Name {value: "is_shared"}
     boolean isShared;
+    @jsondata:Name {value: "previous_names"}
     ChannelNameDef[] previousNames?;
+    @jsondata:Name {value: "connected_team_ids"}
     TeamDef[] connectedTeamIds?;
+    @jsondata:Name {value: "pending_connected_team_ids"}
     TeamDef[] pendingConnectedTeamIds?;
     ConversationObjLatest1[] latest?;
+    @jsondata:Name {value: "last_read"}
     TsDef lastRead?;
     UserIdDef creator;
+    @jsondata:Name {value: "is_frozen"}
     boolean isFrozen?;
+    @jsondata:Name {value: "is_mpim"}
     true isMpim;
+    @jsondata:Name {value: "timezone_count"}
     int timezoneCount?;
+    @jsondata:Name {value: "is_ext_shared"}
     boolean isExtShared?;
+    @jsondata:Name {value: "name_normalized"}
     string nameNormalized;
+    @jsondata:Name {value: "unread_count_display"}
     int unreadCountDisplay?;
+    @jsondata:Name {value: "is_group"}
     boolean isGroup;
     int unlinked?;
+    @jsondata:Name {value: "is_general"}
     boolean isGeneral;
+    @jsondata:Name {value: "num_members"}
     int numMembers?;
+    @jsondata:Name {value: "is_thread_only"}
     boolean isThreadOnly?;
     UserIdDef user?;
+    @jsondata:Name {value: "parent_conversation"}
     ConversationObjParentConversation1[] parentConversation?;
 };
 
 
 type ConversationObjDisplayCounts1 record {
+    @jsondata:Name {value: "display_counts"}
     int displayCounts;
+    @jsondata:Name {value: "guest_counts"}
     int guestCounts;
 };
 
 
 type ConversationObjTopic1 record {
+    @jsondata:Name {value: "last_set"}
     int lastSet;
     TopicPurposeCreatorDef creator;
     string value;
@@ -605,6 +831,7 @@
 
 
 type ConversationObjPurpose1 record {
+    @jsondata:Name {value: "last_set"}
     int lastSet;
     TopicPurposeCreatorDef creator;
     string value;
@@ -612,7 +839,9 @@
 
 
 type ConversationObjShares1 record {
+    @jsondata:Name {value: "is_active"}
     boolean isActive;
+    @jsondata:Name {value: "accepted_user"}
     UserIdDef acceptedUser?;
     TeamObj team;
     UserIdDef user;
@@ -620,41 +849,58 @@
 
 type LatestAnyOf22 anydata|();
 
-type ConversationObjLatest1 ballerinax/slack:5.0.1:MessageObj|anydata|();
+type ConversationObjLatest1 MessageObj|anydata|();
 
 type ParentConversationAnyOf21 anydata|();
 
-type ConversationObjParentConversation1 ballerinax/slack:5.0.1:ChannelDef|anydata|();
+type ConversationObjParentConversation1 ChannelDef|anydata|();
 
 
 type ConversationIMChannelObjectFromConversationsMethods record {
+    @jsondata:Name {value: "has_pins"}
     boolean hasPins?;
+    @jsondata:Name {value: "last_read"}
     TsDef lastRead?;
+    @jsondata:Name {value: "is_user_deleted"}
     boolean isUserDeleted?;
+    @jsondata:Name {value: "is_frozen"}
     boolean isFrozen?;
+    @jsondata:Name {value: "is_im"}
     boolean isIm;
+    @jsondata:Name {value: "is_open"}
     boolean isOpen?;
     int created;
+    @jsondata:Name {value: "is_ext_shared"}
     boolean isExtShared?;
     decimal priority;
+    @jsondata:Name {value: "unread_count_display"}
     int unreadCountDisplay?;
     int version?;
     ConversationObjShares2[] shares?;
+    @jsondata:Name {value: "unread_count"}
     int unreadCount?;
+    @jsondata:Name {value: "is_starred"}
     boolean isStarred?;
+    @jsondata:Name {value: "is_archived"}
     boolean isArchived?;
+    @jsondata:Name {value: "is_shared"}
     boolean isShared?;
+    @jsondata:Name {value: "pin_count"}
     int pinCount?;
     DmIdDef id;
+    @jsondata:Name {value: "is_org_shared"}
     boolean isOrgShared;
     UserIdDef user;
     ConversationObjLatest2[] latest?;
+    @jsondata:Name {value: "parent_conversation"}
     ConversationObjParentConversation2[] parentConversation?;
 };
 
 
 type ConversationObjShares2 record {
+    @jsondata:Name {value: "is_active"}
     boolean isActive;
+    @jsondata:Name {value: "date_create"}
     int dateCreate;
     string name;
     TeamDef id;
@@ -663,30 +909,35 @@
 
 type LatestAnyOf23 anydata|();
 
-type ConversationObjLatest2 ballerinax/slack:5.0.1:MessageObj|anydata|();
+type ConversationObjLatest2 MessageObj|anydata|();
 
 type ParentConversationAnyOf22 anydata|();
 
-type ConversationObjParentConversation2 ballerinax/slack:5.0.1:ChannelDef|anydata|();
+type ConversationObjParentConversation2 ChannelDef|anydata|();
 
-type InlineArrayItemsConversationObj ballerinax/slack:5.0.1:ConversationObject|ballerinax/slack:5.0.1:ConversationMPIMObject|ballerinax/slack:5.0.1:ConversationIMChannelObjectFromConversationsMethods;
+type InlineArrayItemsConversationObj ConversationObject|ConversationMPIMObject|ConversationIMChannelObjectFromConversationsMethods;
 
-// Unknown type: ConversationObj
+type ConversationObj InlineArrayItemsConversationObj[];
 
 
 type ChannelAnyOf2 record {
+    @jsondata:Name {value: "last_read"}
     TsDef lastRead?;
+    @jsondata:Name {value: "unread_count"}
     decimal unreadCount?;
+    @jsondata:Name {value: "is_im"}
     boolean isIm?;
+    @jsondata:Name {value: "is_open"}
     boolean isOpen?;
     string created?;
     DmIdDef id;
+    @jsondata:Name {value: "unread_count_display"}
     decimal unreadCountDisplay?;
     UserIdDef user?;
     MessageObj latest?;
 };
 
-type ConversationsOpenResponseChannel ballerinax/slack:5.0.1:ConversationObj|ballerinax/slack:5.0.1:ChannelAnyOf2;
+type ConversationsOpenResponseChannel ConversationObj|ChannelAnyOf2;
 
 # Schema for successful response from usergroups.users.list method
 
@@ -695,7 +946,7 @@
     UserIdDef[] users;
 };
 
-// Unknown type: OkTrueDef
+type OkTrueDef true;
 
 # Represents the Queries record for the operation: admin_conversations_search
 
@@ -703,8 +954,10 @@
     # Set `cursor` to `next_cursor` returned by the previous call to list items in the next page
     string cursor?;
     # The type of channel to include or exclude in the search. For example `private` will search private channels, while `private_exclude` will exclude them. For a full list of types, check the [Types section](#types)
+    @http:Query {name: "search_channel_types"}
     string searchChannelTypes?;
     # Comma separated string of team IDs, signifying the workspaces to search through
+    @http:Query {name: "team_ids"}
     string teamIds?;
     # Name of the the channel to query by
     string query?;
@@ -713,11 +966,13 @@
     # Possible values are `relevant` (search ranking based on what we think is closest), `name` (alphabetical), `member_count` (number of users in the channel), and `created` (date channel was created). You can optionally pair this with the `sort_dir` arg to change how it is sorted 
     string sort?;
     # Sort direction. Possible values are `asc` for ascending order like (1, 2, 3) or (a, b, c), and `desc` for descending order like (3, 2, 1) or (c, b, a)
+    @http:Query {name: "sort_dir"}
     string sortDir?;
 };
 
 
 type DeprecationWarningAndPagingStyleTogether record {
+    @jsondata:Name {value: "next_cursor"}
     string nextCursor;
     "method_deprecated"[] warnings;
     string[] messages;
@@ -728,59 +983,95 @@
 type UsersProfileSetResponse record {
     UserProfileObj profile;
     OkTrueDef ok;
+    @jsondata:Name {value: "email_pending"}
     string emailPending?;
     string username;
 };
 
 
 type UserProfileObj record {
+    @jsondata:Name {value: "image_32"}
     string? image32?;
+    @jsondata:Name {value: "status_emoji"}
     string statusEmoji;
+    @jsondata:Name {value: "guest_invited_by"}
     string? guestInvitedBy?;
+    @jsondata:Name {value: "is_restricted"}
     boolean? isRestricted?;
+    @jsondata:Name {value: "api_app_id"}
     OptionalAppIdDef apiAppId?;
+    @jsondata:Name {value: "image_192"}
     string? image192?;
+    @jsondata:Name {value: "real_name"}
     string realName;
     string title;
+    @jsondata:Name {value: "status_text_canonical"}
     string? statusTextCanonical?;
     string skype;
+    @jsondata:Name {value: "is_app_user"}
     boolean isAppUser?;
+    @jsondata:Name {value: "image_original"}
     string? imageOriginal?;
+    @jsondata:Name {value: "guest_expiration_ts"}
     int? guestExpirationTs?;
+    @jsondata:Name {value: "real_name_normalized"}
     string realNameNormalized;
+    @jsondata:Name {value: "avatar_hash"}
     string avatarHash;
+    @jsondata:Name {value: "first_name"}
     string? firstName?;
+    @jsondata:Name {value: "bot_id"}
     BotIdDef botId?;
     string? email?;
+    @jsondata:Name {value: "image_512"}
     string? image512?;
+    @jsondata:Name {value: "status_default_text_canonical"}
     string? statusDefaultTextCanonical?;
+    @jsondata:Name {value: "is_ultra_restricted"}
     boolean? isUltraRestricted?;
+    @jsondata:Name {value: "image_1024"}
     string? image1024?;
+    @jsondata:Name {value: "status_default_emoji"}
     string statusDefaultEmoji?;
+    @jsondata:Name {value: "image_24"}
     string? image24?;
+    @jsondata:Name {value: "last_name"}
     string? lastName?;
+    @jsondata:Name {value: "image_48"}
     string? image48?;
     WorkspaceIdDef team?;
+    @jsondata:Name {value: "display_name"}
     string displayName;
+    @jsondata:Name {value: "last_avatar_image_hash"}
     string lastAvatarImageHash?;
+    @jsondata:Name {value: "always_active"}
     boolean alwaysActive?;
+    @jsondata:Name {value: "status_expiration"}
     int statusExpiration?;
+    @jsondata:Name {value: "memberships_count"}
     int membershipsCount?;
     string phone;
+    @jsondata:Name {value: "user_id"}
     string userId?;
     string? name?;
+    @jsondata:Name {value: "status_default_text"}
     string statusDefaultText?;
     string pronouns?;
+    @jsondata:Name {value: "is_custom_image"}
     boolean isCustomImage?;
+    @jsondata:Name {value: "status_text"}
     string statusText;
     record {|anydata...;|}[]? fields;
+    @jsondata:Name {value: "image_72"}
     string? image72?;
     int updated?;
+    @jsondata:Name {value: "display_name_normalized"}
     string displayNameNormalized;
     string? username?;
 };
 
-// Unknown type: OptionalAppIdDef
+@constraint:String {pattern: re `^(A[A-Z0-9]{1,})?$`}
+type OptionalAppIdDef string;
 
 
 type FilesSharedPublicURLBody record {
@@ -792,12 +1083,15 @@
 
 type FilesListQueries record {
     # Filter files created after this timestamp (inclusive)
+    @http:Query {name: "ts_from"}
     decimal tsFrom?;
     # Show truncated file info for files hidden due to being too old, and the team who owns the file being over the file limit
+    @http:Query {name: "show_files_hidden_by_limit"}
     boolean showFilesHiddenByLimit?;
     # Filter files by type ([see below](#file_types)). You can pass multiple values in the types argument, like `types=spaces,snippets`.The default value is `all`, which does not filter the list
     string types?;
     # Filter files created before this timestamp (inclusive)
+    @http:Query {name: "ts_to"}
     decimal tsTo?;
     # Filter files appearing in a specific channel, indicated by its ID
     string channel?;
@@ -810,8 +1104,10 @@
 
 type AdminUsersSetAdminBody record {
     # The ID of the user to designate as an admin
+    @jsondata:Name {value: "user_id"}
     string userId;
     # The ID (`T1234`) of the workspace
+    @jsondata:Name {value: "team_id"}
     string teamId;
 };
 
@@ -825,11 +1121,17 @@
 # Schema for successful response from dnd.info method
 
 type DndInfoResponse record {
+    @jsondata:Name {value: "next_dnd_end_ts"}
     int nextDndEndTs;
+    @jsondata:Name {value: "snooze_endtime"}
     int snoozeEndtime?;
+    @jsondata:Name {value: "dnd_enabled"}
     boolean dndEnabled;
+    @jsondata:Name {value: "next_dnd_start_ts"}
     int nextDndStartTs;
+    @jsondata:Name {value: "snooze_enabled"}
     boolean snoozeEnabled?;
+    @jsondata:Name {value: "snooze_remaining"}
     int snoozeRemaining?;
     OkTrueDef ok;
 };
@@ -849,11 +1151,12 @@
 
 type ResourcesObj record {
     ChannelDef|TeamDef[][] ids;
+    @jsondata:Name {value: "excluded_ids"}
     ChannelDef|TeamDef[][] excludedIds?;
     boolean wildcard?;
 };
 
-// Unknown type: ScopesObj
+type ScopesObj string[];
 
 
 type ConversationsInviteBody record {
@@ -875,7 +1178,7 @@
     OkTrueDef ok;
 };
 
-// Unknown type: TzTzAnyOf112
+type TzTzAnyOf112 string;
 
 
 type RtmConnectResponseTeam record {
@@ -903,6 +1206,7 @@
     # This workspace's discovery setting. It must be set to one of `open`, `invite_only`, `closed`, or `unlisted`
     string discoverability;
     # The ID of the workspace to set discoverability on
+    @jsondata:Name {value: "team_id"}
     string teamId;
 };
 
@@ -910,6 +1214,7 @@
 
 type ChatPostEphemeralResponse record {
     OkTrueDef ok;
+    @jsondata:Name {value: "message_ts"}
     TsDef messageTs;
 };
 
@@ -922,38 +1227,53 @@
 
 
 type SubteamObj record {
+    @jsondata:Name {value: "channel_count"}
     int channelCount?;
+    @jsondata:Name {value: "date_delete"}
     int dateDelete;
+    @jsondata:Name {value: "date_update"}
     int dateUpdate;
+    @jsondata:Name {value: "deleted_by"}
     SubteamObjDeletedBy[] deletedBy;
     string description;
+    @jsondata:Name {value: "is_external"}
     boolean isExternal;
     string 'handle;
+    @jsondata:Name {value: "team_id"}
     TeamDef teamId;
+    @jsondata:Name {value: "created_by"}
     UserIdDef createdBy;
     UserIdDef[] users?;
+    @jsondata:Name {value: "auto_type"}
     SubteamObjAutoType[] autoType;
     SubteamObjPrefs prefs;
+    @jsondata:Name {value: "is_subteam"}
     boolean isSubteam;
+    @jsondata:Name {value: "user_count"}
     int userCount?;
+    @jsondata:Name {value: "date_create"}
     int dateCreate;
     string name;
+    @jsondata:Name {value: "updated_by"}
     UserIdDef updatedBy;
+    @jsondata:Name {value: "is_usergroup"}
     boolean isUsergroup;
     SubteamIdDef id;
+    @jsondata:Name {value: "auto_provision"}
     boolean autoProvision;
+    @jsondata:Name {value: "enterprise_subteam_id"}
     string enterpriseSubteamId;
 };
 
 type DeletedByAnyOf1 anydata|();
 
-type SubteamObjDeletedBy anydata|()|ballerinax/slack:5.0.1:UserIdDef;
+type SubteamObjDeletedBy anydata|()|UserIdDef;
 
 type AutoTypeAnyOf1 anydata|();
 
 type AutoTypeAutoTypeAnyOf12 "owner"|"admin";
 
-type SubteamObjAutoType anydata|()|ballerinax/slack:5.0.1:AutoTypeAutoTypeAnyOf12;
+type SubteamObjAutoType anydata|()|AutoTypeAutoTypeAnyOf12;
 
 
 type SubteamObjPrefs record {
@@ -961,19 +1281,23 @@
     GroupIdDef[] groups;
 };
 
-// Unknown type: SubteamIdDef
+@constraint:String {pattern: re `^S[A-Z0-9]{2,}$`}
+type SubteamIdDef string;
 
 
 type ChatUnfurlBody record {
     # URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their unfurl blocks or message attachments
     string unfurls?;
     # Provide a simply-formatted string to send as an ephemeral message to the user as invitation to authenticate further and enable full unfurling behavior
+    @jsondata:Name {value: "user_auth_message"}
     string userAuthMessage?;
     # Channel ID of the message
     string channel;
     # Send users to this custom URL where they will complete authentication in your app to fully trigger unfurling. Value should be properly URL-encoded
+    @jsondata:Name {value: "user_auth_url"}
     string userAuthUrl?;
     # Set to `true` or `1` to indicate the user must install your Slack app to trigger unfurls for this domain
+    @jsondata:Name {value: "user_auth_required"}
     boolean userAuthRequired?;
     # Timestamp of the message to add unfurl behavior to
     string ts;
@@ -984,14 +1308,18 @@
     # type of file
     string filetype?;
     # URL of the remote file
+    @jsondata:Name {value: "external_url"}
     string externalUrl?;
     # Specify a file by providing its ID
     string file?;
     # Preview of the document via `multipart/form-data`
+    @jsondata:Name {value: "preview_image"}
     string previewImage?;
     # Creator defined GUID for the file
+    @jsondata:Name {value: "external_id"}
     string externalId?;
     # File containing contents that can be used to improve searchability for the remote file
+    @jsondata:Name {value: "indexable_file_contents"}
     string indexableFileContents?;
     # Title of the file being shared
     string title?;
@@ -1003,14 +1331,18 @@
 
 type OauthAccessQueries record {
     # Request the user to add your app only to a single channel. Only valid with a [legacy workspace app](https://api.slack.com/legacy-workspace-apps)
+    @http:Query {name: "single_channel"}
     boolean singleChannel?;
     # The `code` param returned via the OAuth callback
     string code?;
     # Issued when you created your application
+    @http:Query {name: "client_secret"}
     string clientSecret?;
     # This must match the originally submitted URI (if one was sent)
+    @http:Query {name: "redirect_uri"}
     string redirectUri?;
     # Issued when you created your application
+    @http:Query {name: "client_id"}
     string clientId?;
 };
 
@@ -1037,12 +1369,16 @@
 type TeamProfileFieldObj record {
     decimal ordering;
     string hint;
+    @jsondata:Name {value: "possible_values"}
     string[]? possibleValues?;
+    @jsondata:Name {value: "is_hidden"}
     boolean isHidden?;
     TeamProfileFieldObjOptions[] options?;
+    @constraint:String {pattern: re `^X[a-zA-Z0-9]{9,}$`}
     string id;
     string label;
     "text"|"date"|"link"|"mailto"|"options_list"|"user" 'type;
+    @jsondata:Name {value: "field_name"}
     string? fieldName?;
 };
 
@@ -1050,13 +1386,17 @@
 
 
 type TeamProfileFieldOptionObj record {
+    @jsondata:Name {value: "is_scim"}
     boolean? isScim?;
+    @jsondata:Name {value: "is_custom"}
     boolean? isCustom?;
+    @jsondata:Name {value: "is_protected"}
     boolean? isProtected?;
+    @jsondata:Name {value: "is_multiple_entry"}
     boolean? isMultipleEntry?;
 };
 
-type TeamProfileFieldObjOptions anydata|()|ballerinax/slack:5.0.1:TeamProfileFieldOptionObj;
+type TeamProfileFieldObjOptions anydata|()|TeamProfileFieldOptionObj;
 
 # Schema for successful response from auth.revoke method
 
@@ -1068,8 +1408,10 @@
 
 type AdminTeamsSettingsSetDefaultChannelsBody record {
     # An array of channel IDs
+    @jsondata:Name {value: "channel_ids"}
     string channelIds;
     # ID for the workspace to set the default channel for
+    @jsondata:Name {value: "team_id"}
     string teamId;
     # Authentication token. Requires scope: `admin.teams:write`
     string token;
@@ -1079,10 +1421,12 @@
 
 type ConversationsInfoQueries record {
     # Set to `true` to include the member count for the specified conversation. Defaults to `false`
+    @http:Query {name: "include_num_members"}
     boolean includeNumMembers?;
     # Conversation ID to learn more about
     string channel?;
     # Set this to `true` to receive the locale for this conversation. Defaults to `false`
+    @http:Query {name: "include_locale"}
     boolean includeLocale?;
 };
 
@@ -1090,6 +1434,7 @@
 
 type UsersInfoQueries record {
     # Set this to `true` to receive the locale for this user. Defaults to `false`
+    @http:Query {name: "include_locale"}
     boolean includeLocale?;
     # User to get info on
     string user?;
@@ -1125,11 +1470,13 @@
 
 type AdminConversationsCreateResponse record {
     OkTrueDef ok;
+    @jsondata:Name {value: "channel_id"}
     ChannelIdDef channelId?;
 };
 
 
 type ChannelObjPurpose record {
+    @jsondata:Name {value: "last_set"}
     int lastSet;
     TopicPurposeCreatorDef creator;
     string value;
@@ -1138,8 +1485,10 @@
 
 type AdminUsersRemoveBody record {
     # The ID of the user to remove
+    @jsondata:Name {value: "user_id"}
     string userId;
     # The ID (`T1234`) of the workspace
+    @jsondata:Name {value: "team_id"}
     string teamId;
 };
 
@@ -1149,20 +1498,25 @@
     # Specify a file by providing its ID
     string file?;
     # Creator defined GUID for the file
+    @http:Query {name: "external_id"}
     string externalId?;
 };
 
-type UserObjTz1 anydata|()|ballerinax/slack:5.0.1:TzTzAnyOf112;
+type UserObjTz1 anydata|()|TzTzAnyOf112;
 
 
 type BotsInfoResponseBotIcons record {
+    @jsondata:Name {value: "image_36"}
     string image36;
+    @jsondata:Name {value: "image_48"}
     string image48;
+    @jsondata:Name {value: "image_72"}
     string image72;
 };
 
 
 type AppsPermissionsResourcesListResponseResponseMetadata record {
+    @jsondata:Name {value: "next_cursor"}
     string nextCursor;
 };
 
@@ -1174,6 +1528,7 @@
     # The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive
     int 'limit?;
     # ID for the workspace where the invite requests were made
+    @http:Query {name: "team_id"}
     string teamId?;
 };
 
@@ -1182,11 +1537,13 @@
 type TeamIntegrationLogsResponse record {
     PagingObj paging;
     OkTrueDef ok;
+    @constraint:Array {minLength: 1}
     TeamIntegrationLogsResponseLogs[] logs;
 };
 
 
 type PagingObj record {
+    @jsondata:Name {value: "per_page"}
     int perPage?;
     int total;
     int pages?;
@@ -1198,21 +1555,31 @@
 
 type TeamIntegrationLogsResponseLogs record {
     string date;
+    @jsondata:Name {value: "service_type"}
     string serviceType?;
+    @jsondata:Name {value: "app_type"}
     string appType;
+    @jsondata:Name {value: "user_id"}
     UserIdDef userId;
+    @jsondata:Name {value: "user_name"}
     string userName;
     string scope;
+    @jsondata:Name {value: "service_id"}
     string serviceId?;
     ChannelDef channel?;
+    @jsondata:Name {value: "change_type"}
     string changeType;
+    @jsondata:Name {value: "admin_app_id"}
     AppIdDef adminAppId?;
+    @jsondata:Name {value: "app_id"}
     AppIdDef appId;
 };
 
 
 type AdminConversationsGetConversationPrefsResponsePrefs record {
+    @jsondata:Name {value: "can_thread"}
     AdminConversationsGetConversationPrefsResponsePrefsCanThread canThread?;
+    @jsondata:Name {value: "who_can_post"}
     AdminConversationsGetConversationPrefsResponsePrefsWhoCanPost whoCanPost?;
 };
 
@@ -1236,6 +1603,7 @@
 
 
 type ChannelObjTopic record {
+    @jsondata:Name {value: "last_set"}
     int lastSet;
     TopicPurposeCreatorDef creator;
     string value;
@@ -1262,18 +1630,24 @@
 
 type CallsAddBody record {
     # Call start time in UTC UNIX timestamp format
+    @jsondata:Name {value: "date_start"}
     int dateStart?;
     # The URL required for a client to join the Call
+    @jsondata:Name {value: "join_url"}
     string joinUrl;
     # When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL
+    @jsondata:Name {value: "desktop_app_join_url"}
     string desktopAppJoinUrl?;
     # An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied, this ID will be displayed in the Call object
+    @jsondata:Name {value: "external_display_id"}
     string externalDisplayId?;
     # An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from that service
+    @jsondata:Name {value: "external_unique_id"}
     string externalUniqueId;
     # The name of the Call
     string title?;
     # The valid Slack user ID of the user who created this Call. When this method is called with a user token, the `created_by` field is optional and defaults to the authed user of the token. Otherwise, the field is required
+    @jsondata:Name {value: "created_by"}
     string createdBy?;
     # The list of users to register as participants in the Call. [Read more on how to specify users here](/apis/calls#users)
     string users?;
@@ -1302,22 +1676,29 @@
 # Schema for successful response from chat.scheduledMessages.list method
 
 type ChatScheduledMessagesListResponse record {
+    @jsondata:Name {value: "scheduled_messages"}
     ChatScheduledMessagesListResponseScheduledMessages[] scheduledMessages;
+    @jsondata:Name {value: "response_metadata"}
     ChatScheduledMessagesListResponseResponseMetadata responseMetadata;
     OkTrueDef ok;
 };
 
 
 type ChatScheduledMessagesListResponseScheduledMessages record {
+    @jsondata:Name {value: "date_created"}
     int dateCreated;
+    @constraint:String {pattern: re `^[Q][A-Z0-9]{8,}$`}
     string id;
     string text?;
+    @jsondata:Name {value: "post_at"}
     int postAt;
+    @jsondata:Name {value: "channel_id"}
     ChannelIdDef channelId;
 };
 
 
 type ChatScheduledMessagesListResponseResponseMetadata record {
+    @jsondata:Name {value: "next_cursor"}
     string nextCursor;
 };
 
@@ -1330,20 +1711,24 @@
 # Schema for successful response of chat.scheduleMessage method
 
 type ChatScheduleMessageResponse record {
+    @jsondata:Name {value: "scheduled_message_id"}
     string scheduledMessageId;
     ChannelDef channel;
     ChatScheduleMessageResponseMessage message;
     OkTrueDef ok;
+    @jsondata:Name {value: "post_at"}
     int postAt;
 };
 
 
 type ChatScheduleMessageResponseMessage record {
+    @jsondata:Name {value: "bot_profile"}
     BotProfileObj botProfile?;
     TeamDef team;
     string text;
     string 'type;
     UserIdDef user;
+    @jsondata:Name {value: "bot_id"}
     BotIdDef botId;
     string username?;
 };
@@ -1382,14 +1767,18 @@
 
 type OauthTokenQueries record {
     # Request the user to add your app only to a single channel
+    @http:Query {name: "single_channel"}
     boolean singleChannel?;
     # The `code` param returned via the OAuth callback
     string code?;
     # Issued when you created your application
+    @http:Query {name: "client_secret"}
     string clientSecret?;
     # This must match the originally submitted URI (if one was sent)
+    @http:Query {name: "redirect_uri"}
     string redirectUri?;
     # Issued when you created your application
+    @http:Query {name: "client_id"}
     string clientId?;
 };
 
@@ -1404,6 +1793,7 @@
     FileObj file?;
     int created?;
     "file" 'type?;
+    @jsondata:Name {value: "created_by"}
     UserIdDef createdBy?;
 };
 
@@ -1413,10 +1803,11 @@
     ChannelDef channel?;
     MessageObj message?;
     "message" 'type?;
+    @jsondata:Name {value: "created_by"}
     UserIdDef createdBy?;
 };
 
-type 200Items ballerinax/slack:5.0.1:FilePin|ballerinax/slack:5.0.1:MessagePin;
+type 200Items FilePin|MessagePin;
 
 # Schema for successful response of admin.conversations.setConversationPrefs
 
@@ -1429,6 +1820,7 @@
     # The encoded ID of the User Group to enable
     string usergroup;
     # Include the number of users in the User Group
+    @jsondata:Name {value: "include_count"}
     boolean includeCount?;
 };
 
@@ -1437,6 +1829,7 @@
     # The new name of the workspace
     string name;
     # ID for the workspace to set the name for
+    @jsondata:Name {value: "team_id"}
     string teamId;
 };
 
@@ -1447,15 +1840,18 @@
     CommentsObj comments;
     FileObj file;
     PagingObj paging?;
+    @jsondata:Name {value: "response_metadata"}
     ResponseMetadataObj responseMetadata?;
     OkTrueDef ok;
+    @jsondata:Name {value: "content_html"}
     anydata? contentHtml?;
 };
 
-// Unknown type: CommentsObj
+type CommentsObj anydata[];
 
 
 type NewPagingStyle record {
+    @jsondata:Name {value: "next_cursor"}
     string nextCursor;
 };
 
@@ -1465,9 +1861,9 @@
     string[] messages;
 };
 
-type InlineArrayItemsResponseMetadataObj ballerinax/slack:5.0.1:NewPagingStyle|ballerinax/slack:5.0.1:DeprecationWarning|ballerinax/slack:5.0.1:DeprecationWarningAndPagingStyleTogether;
+type InlineArrayItemsResponseMetadataObj NewPagingStyle|DeprecationWarning|DeprecationWarningAndPagingStyleTogether;
 
-// Unknown type: ResponseMetadataObj
+type ResponseMetadataObj InlineArrayItemsResponseMetadataObj[];
 
 # Schema for successful response api.permissions.scopes.list method
 
@@ -1495,6 +1891,7 @@
     # The number of results that will be returned by the API on each invocation. Must be between 1 - 1000 both inclusive
     int 'limit?;
     # ID for the workspace where the invite requests were made
+    @http:Query {name: "team_id"}
     string teamId?;
 };
 
@@ -1502,10 +1899,12 @@
 
 type AdminConversationsEkmListOriginalConnectedChannelInfoQueries record {
     # A comma-separated list of channels to filter to
+    @http:Query {name: "channel_ids"}
     string channelIds?;
     # Set `cursor` to `next_cursor` returned by the previous call to list items in the next page
     string cursor?;
     # A comma-separated list of the workspaces to which the channels you would like returned belong
+    @http:Query {name: "team_ids"}
     string teamIds?;
     # The maximum number of items to return. Must be between 1 - 1000 both inclusive
     int 'limit?;
@@ -1516,6 +1915,7 @@
     AppsPermissionsInfoResponseInfoIm im;
     AppsPermissionsInfoResponseInfoMpim mpim;
     AppsPermissionsInfoResponseInfoChannel channel;
+    @jsondata:Name {value: "app_home"}
     AppsPermissionsInfoResponseInfoAppHome appHome;
     AppsPermissionsInfoResponseInfoTeam team;
     AppsPermissionsInfoResponseInfoGroup group;
@@ -1556,6 +1956,7 @@
     # The name of the emoji to be renamed. Colons (`:myemoji:`) around the value are not required, although they may be included
     string name;
     # The new name of the emoji
+    @jsondata:Name {value: "new_name"}
     string newName;
     # Authentication token. Requires scope: `admin.teams:write`
     string token;
@@ -1576,32 +1977,52 @@
 # user object for non enterprise type
 
 type UserObjAnyOf1 record {
+    @constraint:String {pattern: re `^[a-fA-F0-9]{6}$`}
     string color?;
+    @jsondata:Name {value: "is_invited_user"}
     boolean isInvitedUser?;
+    @jsondata:Name {value: "has_2fa"}
     boolean has2fa?;
+    @jsondata:Name {value: "is_restricted"}
     boolean isRestricted?;
     UserObjTz[] tz?;
+    @jsondata:Name {value: "tz_label"}
     string tzLabel?;
+    @jsondata:Name {value: "is_primary_owner"}
     boolean isPrimaryOwner?;
+    @jsondata:Name {value: "team_profile"}
     UserObjTeamProfile teamProfile?;
+    @jsondata:Name {value: "real_name"}
     string realName?;
+    @jsondata:Name {value: "team_id"}
     WorkspaceIdDef teamId?;
     string locale?;
+    @jsondata:Name {value: "is_admin"}
     boolean isAdmin?;
+    @jsondata:Name {value: "is_app_user"}
     boolean isAppUser;
+    @jsondata:Name {value: "tz_offset"}
     decimal tzOffset?;
+    @jsondata:Name {value: "is_stranger"}
     boolean isStranger?;
+    @jsondata:Name {value: "is_forgotten"}
     boolean isForgotten?;
     UserIdDef id;
+    @jsondata:Name {value: "is_bot"}
     boolean isBot;
     string presence?;
+    @jsondata:Name {value: "is_ultra_restricted"}
     boolean isUltraRestricted?;
+    @jsondata:Name {value: "is_owner"}
     boolean isOwner?;
     UserProfileObj profile;
+    @jsondata:Name {value: "is_external"}
     boolean isExternal?;
     WorkspaceIdDef team?;
+    @jsondata:Name {value: "enterprise_user"}
     EnterpriseUserObj enterpriseUser?;
     boolean deleted?;
+    @jsondata:Name {value: "two_factor_type"}
     string twoFactorType?;
     string name;
     decimal updated;
@@ -1609,26 +2030,32 @@
 
 type TzAnyOf1 anydata|();
 
-// Unknown type: TzTzAnyOf12
+type TzTzAnyOf12 string;
 
-type UserObjTz anydata|()|ballerinax/slack:5.0.1:TzTzAnyOf12;
+type UserObjTz anydata|()|TzTzAnyOf12;
 
 
 type UserObjTeamProfile record {
+    @constraint:Array {minLength: 1}
     TeamProfileFieldObj[] fields;
 };
 
 
 type EnterpriseUserObj record {
+    @jsondata:Name {value: "is_admin"}
     boolean isAdmin;
     TeamDef[] teams;
+    @jsondata:Name {value: "is_owner"}
     boolean isOwner;
     EnterpriseUserIdDef id;
+    @jsondata:Name {value: "enterprise_id"}
     EnterpriseIdDef enterpriseId;
+    @jsondata:Name {value: "enterprise_name"}
     EnterpriseNameDef enterpriseName;
 };
 
-// Unknown type: EnterpriseUserIdDef
+@constraint:String {pattern: re `^[WU][A-Z0-9]{8,}$`}
+type EnterpriseUserIdDef string;
 
 # Represents the Queries record for the operation: workflows_updateStep
 
@@ -1638,10 +2065,13 @@
     # A JSON key-value map of inputs required from a user during configuration. This is the data your app expects to receive when the workflow step starts. **Please note**: the embedded variable format is set and replaced by the workflow system. You cannot create custom variables that will be replaced at runtime. [Read more about variables in workflow steps here](/workflows/steps#variables)
     string inputs?;
     # An optional field that can be used to override the step name that is shown in the Workflow Builder
+    @http:Query {name: "step_name"}
     string stepName?;
     # An optional field that can be used to override app image that is shown in the Workflow Builder
+    @http:Query {name: "step_image_url"}
     string stepImageUrl?;
     # A context identifier provided with `view_submission` payloads used to call back to `workflows.updateStep`
+    @http:Query {name: "workflow_step_edit_id"}
     string workflowStepEditId;
 };
 
@@ -1686,12 +2116,14 @@
 type ConversationsJoinResponse record {
     ConversationObj channel;
     string warning?;
+    @jsondata:Name {value: "response_metadata"}
     ResponseMetadata responseMetadata?;
     OkTrueDef ok;
 };
 
 
 type ResponseMetadata record {
+    @constraint:Array {minLength: 1}
     string[] warnings?;
 };
 
@@ -1700,19 +2132,22 @@
 type StarsListResponse record {
     PagingObj paging?;
     OkTrueDef ok;
-    (record {|ballerinax/slack:5.0.1:ChannelDef channel; int date_create; ballerinax/slack:5.0.1:MessageObj message; "message" 'type;|}|record {|int date_create; ballerinax/slack:5.0.1:FileObj file; "file" 'type;|}|record {|ballerinax/slack:5.0.1:CommentObj comment; int date_create; ballerinax/slack:5.0.1:FileObj file; "file_comment" 'type;|}|record {|ballerinax/slack:5.0.1:ChannelDef channel; int date_create; "channel" 'type;|}|record {|ballerinax/slack:5.0.1:DmIdDef channel; int date_create; "im" 'type;|}|record {|ballerinax/slack:5.0.1:GroupIdDef channel; int date_create; "group" 'type;|})[][] items;
+    (record {|ChannelDef channel; int date_create; MessageObj message; "message" 'type;|}|record {|int date_create; FileObj file; "file" 'type;|}|record {|CommentObj comment; int date_create; FileObj file; "file_comment" 'type;|}|record {|ChannelDef channel; int date_create; "channel" 'type;|}|record {|DmIdDef channel; int date_create; "im" 'type;|}|record {|GroupIdDef channel; int date_create; "group" 'type;|})[][] items;
 };
 
 # Schema for successful response conversations.members method
 
 type ConversationsMembersResponse record {
+    @constraint:Array {minLength: 1}
     UserIdDef[] members;
+    @jsondata:Name {value: "response_metadata"}
     ConversationsMembersResponseResponseMetadata responseMetadata;
     OkTrueDef ok;
 };
 
 
 type ConversationsMembersResponseResponseMetadata record {
+    @jsondata:Name {value: "next_cursor"}
     string nextCursor;
 };
 
@@ -1721,6 +2156,7 @@
     # The new description for the workspace
     string description;
     # ID for the workspace to set the description for
+    @jsondata:Name {value: "team_id"}
     string teamId;
 };
 
@@ -1730,8 +2166,10 @@
     # A [view object](/reference/surfaces/views). This must be a JSON-encoded string
     string view?;
     # A unique identifier of the view to be updated. Either `view_id` or `external_id` is required
+    @http:Query {name: "view_id"}
     string viewId?;
     # A unique identifier of the view set by the developer. Must be unique for all views on a team. Max length of 255 characters. Either `view_id` or `external_id` is required
+    @http:Query {name: "external_id"}
     string externalId?;
     # A string that represents view state to protect against possible race conditions
     string hash?;
@@ -1748,6 +2186,7 @@
 
 type AppsPermissionsRequestQueries record {
     # Token used to trigger the permissions API
+    @http:Query {name: "trigger_id"}
     string triggerId;
     # A comma separated list of scopes to request for
     string scopes;
@@ -1771,19 +2210,24 @@
 type TeamAccessLogsResponse record {
     PagingObj paging;
     OkTrueDef ok;
+    @constraint:Array {minLength: 1}
     TeamAccessLogsResponseLogins[] logins;
 };
 
 
 type TeamAccessLogsResponseLogins record {
     string? country;
+    @jsondata:Name {value: "date_last"}
     int dateLast;
+    @jsondata:Name {value: "user_id"}
     UserIdDef userId;
     string? ip;
     string? isp;
     int count;
+    @jsondata:Name {value: "date_first"}
     int dateFirst;
     string? region;
+    @jsondata:Name {value: "user_agent"}
     string userAgent;
     string username;
 };
@@ -1792,8 +2236,10 @@
 
 type MigrationExchangeQueries record {
     # Specify `true` to convert `W` global user IDs to workspace-specific `U` IDs. Defaults to `false`
+    @http:Query {name: "to_old"}
     boolean toOld?;
     # Specify team_id starts with `T` in case of Org Token
+    @http:Query {name: "team_id"}
     string teamId?;
     # A comma-separated list of user ids, up to 400 per request
     string users;
@@ -1806,6 +2252,7 @@
     # Channel to remove star from, or channel where the message to remove star from was posted (used with `timestamp`)
     string channel?;
     # File comment to remove star from
+    @jsondata:Name {value: "file_comment"}
     string fileComment?;
     # Timestamp of the message to remove star from
     string timestamp?;
@@ -1815,6 +2262,7 @@
 type ReminderObj record {
     UserIdDef creator;
     boolean recurring;
+    @jsondata:Name {value: "complete_ts"}
     int completeTs?;
     ReminderIdDef id;
     string text;
@@ -1822,23 +2270,29 @@
     UserIdDef user;
 };
 
-// Unknown type: ReminderIdDef
+@constraint:String {pattern: re `^Rm[A-Z0-9]{8,}$`}
+type ReminderIdDef string;
 
 
 type AdminUsersSetExpirationBody record {
     # Timestamp when guest account should be disabled
+    @jsondata:Name {value: "expiration_ts"}
     int expirationTs;
     # The ID of the user to set an expiration for
+    @jsondata:Name {value: "user_id"}
     string userId;
     # The ID (`T1234`) of the workspace
+    @jsondata:Name {value: "team_id"}
     string teamId;
 };
 
 
 type AdminUsergroupsRemoveChannelsBody record {
     # Comma-separated string of channel IDs
+    @jsondata:Name {value: "channel_ids"}
     string channelIds;
     # ID of the IDP Group
+    @jsondata:Name {value: "usergroup_id"}
     string usergroupId;
 };
 
@@ -1863,7 +2317,9 @@
     string cursor?;
     # The maximum number of items to return. Must be between 1 - 1000 both inclusive
     int 'limit?;
+    @http:Query {name: "team_id"}
     string teamId?;
+    @http:Query {name: "enterprise_id"}
     string enterpriseId?;
 };
 
@@ -1876,10 +2332,13 @@
 
 type AdminConversationsRestrictAccessAddGroupBody record {
     # The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to be an allowlist for the private channel
+    @jsondata:Name {value: "group_id"}
     string groupId;
     # The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization
+    @jsondata:Name {value: "team_id"}
     string teamId?;
     # The channel to link this group to
+    @jsondata:Name {value: "channel_id"}
     string channelId;
     # Authentication token. Requires scope: `admin.conversations:write`
     string token;
@@ -1911,20 +2370,26 @@
     # Return matches sorted by either `score` or `timestamp`
     string sort?;
     # Change sort direction to ascending (`asc`) or descending (`desc`)
+    @http:Query {name: "sort_dir"}
     string sortDir?;
 };
 
 
 type AdminUsersAssignBody record {
     # Comma separated values of channel IDs to add user in the new workspace
+    @jsondata:Name {value: "channel_ids"}
     string channelIds?;
     # True if user should be added to the workspace as a single-channel guest
+    @jsondata:Name {value: "is_ultra_restricted"}
     boolean isUltraRestricted?;
     # The ID of the user to add to the workspace
+    @jsondata:Name {value: "user_id"}
     string userId;
     # True if user should be added to the workspace as a guest
+    @jsondata:Name {value: "is_restricted"}
     boolean isRestricted?;
     # The ID (`T1234`) of the workspace
+    @jsondata:Name {value: "team_id"}
     string teamId;
 };
 
@@ -1958,10 +2423,13 @@
     # The `code` param returned via the OAuth callback
     string code;
     # Issued when you created your application
+    @http:Query {name: "client_secret"}
     string clientSecret?;
     # This must match the originally submitted URI (if one was sent)
+    @http:Query {name: "redirect_uri"}
     string redirectUri?;
     # Issued when you created your application
+    @http:Query {name: "client_id"}
     string clientId?;
 };
 
@@ -1975,6 +2443,7 @@
 
 type WorkflowsStepFailedQueries record {
     # Context identifier that maps to the correct workflow step execution
+    @http:Query {name: "workflow_step_execute_id"}
     string workflowStepExecuteId;
     # A JSON-based object with a `message` property that should contain a human readable error message
     string 'error;
@@ -1991,8 +2460,11 @@
 # Schema for successful response from users.list method
 
 type UsersListResponse record {
+    @jsondata:Name {value: "cache_ts"}
     int cacheTs;
+    @constraint:Array {minLength: 1}
     UserObj[] members;
+    @jsondata:Name {value: "response_metadata"}
     ResponseMetadataObj responseMetadata?;
     OkTrueDef ok;
 };
@@ -2001,31 +2473,51 @@
 
 type UserObjUserObjAnyOf12 record {
     # refercing to bug: https://jira.tinyspeck.com/browse/EVALUE-1559
+    @constraint:String {pattern: re `^([a-fA-F0-9]{6})?$`}
     string color?;
+    @jsondata:Name {value: "has_2fa"}
     boolean has2fa?;
+    @jsondata:Name {value: "is_restricted"}
     boolean isRestricted?;
     UserObjTz1[] tz?;
+    @jsondata:Name {value: "tz_label"}
     string tzLabel?;
+    @jsondata:Name {value: "is_primary_owner"}
     boolean isPrimaryOwner?;
+    @jsondata:Name {value: "team_profile"}
     UserObjTeamProfile1 teamProfile?;
+    @jsondata:Name {value: "real_name"}
     string realName?;
+    @jsondata:Name {value: "team_id"}
     WorkspaceIdDef teamId?;
     string locale?;
+    @jsondata:Name {value: "is_admin"}
     boolean isAdmin?;
+    @jsondata:Name {value: "is_app_user"}
     boolean isAppUser;
+    @jsondata:Name {value: "tz_offset"}
     decimal tzOffset?;
+    @jsondata:Name {value: "is_stranger"}
     boolean isStranger?;
+    @jsondata:Name {value: "is_forgotten"}
     boolean isForgotten?;
     UserIdDef id;
+    @jsondata:Name {value: "is_bot"}
     boolean isBot;
     string presence?;
+    @jsondata:Name {value: "is_ultra_restricted"}
     boolean isUltraRestricted?;
+    @constraint:Array {minLength: 1}
     WorkspaceIdDef[] teams?;
+    @jsondata:Name {value: "is_owner"}
     boolean isOwner?;
     UserProfileObj profile;
+    @jsondata:Name {value: "is_external"}
     boolean isExternal?;
+    @jsondata:Name {value: "enterprise_user"}
     EnterpriseUserObj enterpriseUser?;
     boolean deleted?;
+    @jsondata:Name {value: "two_factor_type"}
     string twoFactorType?;
     string name;
     decimal updated;
@@ -2033,12 +2525,13 @@
 
 
 type UserObjTeamProfile1 record {
+    @constraint:Array {minLength: 1}
     TeamProfileFieldObj[] fields;
 };
 
-type InlineArrayItemsUserObj ballerinax/slack:5.0.1:UserObjAnyOf1|ballerinax/slack:5.0.1:UserObjUserObjAnyOf12;
+type InlineArrayItemsUserObj UserObjAnyOf1|UserObjUserObjAnyOf12;
 
-// Unknown type: UserObj
+type UserObj InlineArrayItemsUserObj[];
 
 
 type ConversationsArchiveBody record {
@@ -2050,10 +2543,13 @@
 
 type UsergroupsListQueries record {
     # Include disabled User Groups
+    @http:Query {name: "include_disabled"}
     boolean includeDisabled?;
     # Include the list of users for each User Group
+    @http:Query {name: "include_users"}
     boolean includeUsers?;
     # Include the number of users in each User Group
+    @http:Query {name: "include_count"}
     boolean includeCount?;
 };
 
@@ -2073,7 +2569,7 @@
     OkTrueDef ok;
 };
 
-// Unknown type: ChannelActionsTsAnyOf1
+type ChannelActionsTsAnyOf1 int;
 
 # Represents the Headers record for the operation: admin_users_setOwner
 
@@ -2102,10 +2598,13 @@
 
 type AdminUsergroupsAddTeamsBody record {
     # A comma separated list of encoded team (workspace) IDs. Each workspace *MUST* belong to the organization associated with the token
+    @jsondata:Name {value: "team_ids"}
     string teamIds;
     # An encoded usergroup (IDP Group) ID
+    @jsondata:Name {value: "usergroup_id"}
     string usergroupId;
     # When `true`, this method automatically creates new workspace accounts for the IDP group members
+    @jsondata:Name {value: "auto_provision"}
     boolean autoProvision?;
 };
 
@@ -2117,6 +2616,7 @@
     # The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive
     int 'limit?;
     # ID for the workspace where the invite requests were made
+    @http:Query {name: "team_id"}
     string teamId?;
 };
 
@@ -2143,10 +2643,12 @@
 
 type BotsInfoResponseBot record {
     boolean deleted;
+    @jsondata:Name {value: "user_id"}
     UserIdDef userId?;
     string name;
     BotIdDef id;
     BotsInfoResponseBotIcons icons;
+    @jsondata:Name {value: "app_id"}
     AppIdDef appId;
     int updated;
 };
@@ -2154,8 +2656,11 @@
 # Schema for successful response from dnd.setSnooze method
 
 type DndSetSnoozeResponse record {
+    @jsondata:Name {value: "snooze_endtime"}
     int snoozeEndtime;
+    @jsondata:Name {value: "snooze_enabled"}
     boolean snoozeEnabled;
+    @jsondata:Name {value: "snooze_remaining"}
     int snoozeRemaining;
     OkTrueDef ok;
 };
@@ -2163,18 +2668,23 @@
 
 type ChatPostEphemeralBody record {
     # URL to an image to use as the icon for this message. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](#authorship) below
+    @jsondata:Name {value: "icon_url"}
     string iconUrl?;
     # Find and link channel names and usernames
+    @jsondata:Name {value: "link_names"}
     boolean linkNames?;
     # Pass true to post the message as the authed user. Defaults to true if the chat:write:bot scope is not included. Otherwise, defaults to false
+    @jsondata:Name {value: "as_user"}
     boolean asUser?;
     # A JSON-based array of structured attachments, presented as a URL-encoded string
     string attachments?;
     # Emoji to use as the icon for this message. Overrides `icon_url`. Must be used in conjunction with `as_user` set to `false`, otherwise ignored. See [authorship](#authorship) below
+    @jsondata:Name {value: "icon_emoji"}
     string iconEmoji?;
     # A JSON-based array of structured blocks, presented as a URL-encoded string
     string blocks?;
     # Provide another message's `ts` value to post this message in a thread. Avoid using a reply's `ts` value; use its parent's value instead. Ephemeral messages in threads are only shown if there is already an active thread
+    @jsondata:Name {value: "thread_ts"}
     string threadTs?;
     # Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name
     string channel;
@@ -2194,16 +2704,20 @@
 
 type RtmConnectQueries record {
     # Batch presence deliveries via subscription. Enabling changes the shape of `presence_change` events. See [batch presence](/docs/presence-and-status#batching)
+    @http:Query {name: "batch_presence_aware"}
     boolean batchPresenceAware?;
     # Only deliver presence events when requested by subscription. See [presence subscriptions](/docs/presence-and-status#subscriptions)
+    @http:Query {name: "presence_sub"}
     boolean presenceSub?;
 };
 
 # Schema for successful response conversations.close method
 
 type ConversationsCloseResponse record {
+    @jsondata:Name {value: "already_closed"}
     boolean alreadyClosed?;
     OkTrueDef ok;
+    @jsondata:Name {value: "no_op"}
     boolean noOp?;
 };
 
@@ -2216,8 +2730,10 @@
 
 
 type AdminUsersSessionInvalidateBody record {
+    @jsondata:Name {value: "session_id"}
     int sessionId;
     # ID of the team that the session belongs to
+    @jsondata:Name {value: "team_id"}
     string teamId;
 };
 
@@ -2225,9 +2741,10 @@
 
 type ReactionsListResponse record {
     PagingObj paging?;
+    @jsondata:Name {value: "response_metadata"}
     ResponseMetadataObj responseMetadata?;
     OkTrueDef ok;
-    (record {|ballerinax/slack:5.0.1:ChannelDef channel; ballerinax/slack:5.0.1:MessageObj message; "message" 'type;|}|record {|ballerinax/slack:5.0.1:FileObj file; "file" 'type;|}|record {|ballerinax/slack:5.0.1:CommentObj comment; ballerinax/slack:5.0.1:FileObj file; "file_comment" 'type;|})[][] items;
+    (record {|ChannelDef channel; MessageObj message; "message" 'type;|}|record {|FileObj file; "file" 'type;|}|record {|CommentObj comment; FileObj file; "file_comment" 'type;|})[][] items;
 };
 
 
@@ -2243,6 +2760,7 @@
     # A mention handle. Must be unique among channels, users and User Groups
     string 'handle?;
     # Include the number of users in the User Group
+    @jsondata:Name {value: "include_count"}
     boolean includeCount?;
 };
 
@@ -2258,9 +2776,13 @@
 # Schema for successful response from dnd.endSnooze method
 
 type DndEndSnoozeResponse record {
+    @jsondata:Name {value: "next_dnd_end_ts"}
     int nextDndEndTs;
+    @jsondata:Name {value: "dnd_enabled"}
     boolean dndEnabled;
+    @jsondata:Name {value: "next_dnd_start_ts"}
     int nextDndStartTs;
+    @jsondata:Name {value: "snooze_enabled"}
     boolean snoozeEnabled;
     OkTrueDef ok;
 };
@@ -2291,14 +2813,17 @@
 
 type AdminConversationsCreateBody record {
     # When `true`, creates a private channel instead of a public channel
+    @jsondata:Name {value: "is_private"}
     boolean isPrivate;
     # When `true`, the channel will be available org-wide. Note: if the channel is not `org_wide=true`, you must specify a `team_id` for this channel
+    @jsondata:Name {value: "org_wide"}
     boolean orgWide?;
     # Name of the public or private channel to create
     string name;
     # Description of the public or private channel to create
     string description?;
     # The workspace to create the channel in. Note: this argument is required unless you set `org_wide=true`
+    @jsondata:Name {value: "team_id"}
     string teamId?;
 };
 
@@ -2312,15 +2837,18 @@
 
 
 type UsersConversationsResponseResponseMetadata record {
+    @jsondata:Name {value: "next_cursor"}
     string nextCursor;
 };
 
 # Schema for successful response from conversations.open method when opening channels, ims, mpims
 
 type ConversationsOpenResponse record {
+    @jsondata:Name {value: "already_open"}
     boolean alreadyOpen?;
     ConversationsOpenResponseChannel[] channel;
     OkTrueDef ok;
+    @jsondata:Name {value: "no_op"}
     boolean noOp?;
 };
 
@@ -2353,8 +2881,10 @@
 
 type AdminConversationsDisconnectSharedBody record {
     # The channel to be disconnected from some workspaces
+    @jsondata:Name {value: "channel_id"}
     string channelId;
     # The team to be removed from the channel. Currently only a single team id can be specified
+    @jsondata:Name {value: "leaving_team_ids"}
     string leavingTeamIds?;
 };
 
@@ -2376,8 +2906,10 @@
     # Comma-separated list of channel names or IDs where the file will be shared
     string channels?;
     # Provide another message's `ts` value to upload this file as a reply. Never use a reply's `ts` value; use its parent instead
+    @jsondata:Name {value: "thread_ts"}
     decimal threadTs?;
     # The message text introducing the file in specified `channels`
+    @jsondata:Name {value: "initial_comment"}
     string initialComment?;
     # Title of file
     string title?;
@@ -2415,14 +2947,23 @@
 
 
 type UsersSetPhotoResponseProfile record {
+    @jsondata:Name {value: "image_32"}
     string image32;
+    @jsondata:Name {value: "image_original"}
     string imageOriginal;
+    @jsondata:Name {value: "image_1024"}
     string image1024;
+    @jsondata:Name {value: "image_24"}
     string image24;
+    @jsondata:Name {value: "image_192"}
     string image192;
+    @jsondata:Name {value: "image_48"}
     string image48;
+    @jsondata:Name {value: "avatar_hash"}
     string avatarHash;
+    @jsondata:Name {value: "image_72"}
     string image72;
+    @jsondata:Name {value: "image_512"}
     string image512;
 };
 
@@ -2431,6 +2972,7 @@
     # The encoded ID of the User Group to update
     string usergroup;
     # Include the number of users in the User Group
+    @jsondata:Name {value: "include_count"}
     boolean includeCount?;
     # A comma separated string of encoded user IDs that represent the entire list of users for the User Group
     string users;
@@ -2464,15 +3006,19 @@
 
 
 type AdminConversationsGetTeamsResponseResponseMetadata record {
+    @jsondata:Name {value: "next_cursor"}
     string nextCursor;
 };
 
 
 type AdminAppsApproveBody record {
+    @jsondata:Name {value: "team_id"}
     string teamId?;
     # The id of the app to approve
+    @jsondata:Name {value: "app_id"}
     string appId?;
     # The id of the request to approve
+    @jsondata:Name {value: "request_id"}
     string requestId?;
 };
 
@@ -2486,10 +3032,13 @@
 
 type AdminUsergroupsListChannelsQueries record {
     # Flag to include or exclude the count of members per channel
+    @http:Query {name: "include_num_members"}
     boolean includeNumMembers?;
     # ID of the IDP group to list default channels for
+    @http:Query {name: "usergroup_id"}
     string usergroupId;
     # ID of the the workspace
+    @http:Query {name: "team_id"}
     string teamId?;
 };
 
@@ -2527,6 +3076,7 @@
 
 
 type ConversationsListResponseResponseMetadata record {
+    @jsondata:Name {value: "next_cursor"}
     string nextCursor;
 };
 
@@ -2537,13 +3087,16 @@
     string cursor?;
     # The maximum number of items to return. Must be between 1 - 1000 both inclusive
     int 'limit?;
+    @http:Query {name: "team_id"}
     string teamId?;
+    @http:Query {name: "enterprise_id"}
     string enterpriseId?;
 };
 
 # Represents the Queries record for the operation: admin_teams_settings_info
 
 type AdminTeamsSettingsInfoQueries record {
+    @http:Query {name: "team_id"}
     string teamId;
 };
 
@@ -2576,20 +3129,26 @@
 
 type AppsUninstallQueries record {
     # Issued when you created your application
+    @http:Query {name: "client_secret"}
     string clientSecret?;
     # Issued when you created your application
+    @http:Query {name: "client_id"}
     string clientId?;
 };
 
 # Schema for successful response auth.test method
 
 type AuthTestResponse record {
+    @jsondata:Name {value: "user_id"}
     UserIdDef userId;
+    @jsondata:Name {value: "is_enterprise_install"}
     boolean isEnterpriseInstall?;
     string team;
+    @jsondata:Name {value: "team_id"}
     TeamDef teamId;
     OkTrueDef ok;
     string user;
+    @jsondata:Name {value: "bot_id"}
     BotIdDef botId?;
     string url;
 };
@@ -2611,6 +3170,7 @@
 
 type AdminConversationsArchiveBody record {
     # The channel to archive
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
@@ -2622,13 +3182,19 @@
 
 
 type 200User2 record {
+    @jsondata:Name {value: "image_32"}
     string image32;
+    @jsondata:Name {value: "image_24"}
     string image24;
     string name;
+    @jsondata:Name {value: "image_192"}
     string image192;
     UserIdDef id;
+    @jsondata:Name {value: "image_48"}
     string image48;
+    @jsondata:Name {value: "image_72"}
     string image72;
+    @jsondata:Name {value: "image_512"}
     string image512;
 };
 
@@ -2636,6 +3202,7 @@
 
 type UsergroupsUsersListQueries record {
     # Allow results that involve disabled User Groups
+    @http:Query {name: "include_disabled"}
     boolean includeDisabled?;
     # The encoded ID of the User Group to update
     string usergroup;
@@ -2651,38 +3218,48 @@
 
 type ChatScheduleMessageBody record {
     # Find and link channel names and usernames
+    @jsondata:Name {value: "link_names"}
     boolean linkNames?;
     # Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [chat.postMessage](chat.postMessage#authorship)
+    @jsondata:Name {value: "as_user"}
     boolean asUser?;
     # A JSON-based array of structured attachments, presented as a URL-encoded string
     string attachments?;
     # A JSON-based array of structured blocks, presented as a URL-encoded string
     string blocks?;
     # Provide another message's `ts` value to make this message a reply. Avoid using a reply's `ts` value; use its parent instead
+    @jsondata:Name {value: "thread_ts"}
     decimal threadTs?;
     # Pass false to disable unfurling of media content
+    @jsondata:Name {value: "unfurl_media"}
     boolean unfurlMedia?;
     # Channel, private group, or DM channel to send message to. Can be an encoded ID, or a name. See [below](#channels) for more details
     string channel?;
     # Used in conjunction with `thread_ts` and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to `false`
+    @jsondata:Name {value: "reply_broadcast"}
     boolean replyBroadcast?;
     # Pass true to enable unfurling of primarily text-based content
+    @jsondata:Name {value: "unfurl_links"}
     boolean unfurlLinks?;
     # Change how messages are treated. Defaults to `none`. See [chat.postMessage](chat.postMessage#formatting)
     string parse?;
     # How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail
     string text?;
     # Unix EPOCH timestamp of time in future to send the message
+    @jsondata:Name {value: "post_at"}
     string postAt?;
 };
 
 
 type AdminConversationsRestrictAccessRemoveGroupBody record {
     # The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to remove from the private channel
+    @jsondata:Name {value: "group_id"}
     string groupId;
     # The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization
+    @jsondata:Name {value: "team_id"}
     string teamId;
     # The channel to remove the linked group from
+    @jsondata:Name {value: "channel_id"}
     string channelId;
     # Authentication token. Requires scope: `admin.conversations:write`
     string token;
@@ -2693,26 +3270,34 @@
     # The encoded ID of the User Group to disable
     string usergroup;
     # Include the number of users in the User Group
+    @jsondata:Name {value: "include_count"}
     boolean includeCount?;
 };
 
 
 type AdminUsersInviteBody record {
     # A comma-separated list of `channel_id`s for this user to join. At least one channel is required
+    @jsondata:Name {value: "channel_ids"}
     string channelIds;
     # Is this user a single channel guest user? (default: false)
+    @jsondata:Name {value: "is_ultra_restricted"}
     boolean isUltraRestricted?;
     # An optional message to send to the user in the invite email
+    @jsondata:Name {value: "custom_message"}
     string customMessage?;
     # Timestamp when guest account should be disabled. Only include this timestamp if you are inviting a guest user and you want their account to expire on a certain date
+    @jsondata:Name {value: "guest_expiration_ts"}
     string guestExpirationTs?;
     # Is this user a multi-channel guest user? (default: false)
+    @jsondata:Name {value: "is_restricted"}
     boolean isRestricted?;
     # Allow this invite to be resent in the future if a user has not signed up yet. (default: false)
     boolean resend?;
     # Full name of the user
+    @jsondata:Name {value: "real_name"}
     string realName?;
     # The ID (`T1234`) of the workspace
+    @jsondata:Name {value: "team_id"}
     string teamId;
     # The email address of the person to invite
     string email;
@@ -2724,6 +3309,7 @@
     # The ID of the conversation or channel containing the message
     string channel;
     # A message's `ts` value, uniquely identifying it within a channel
+    @http:Query {name: "message_ts"}
     string messageTs;
 };
 
@@ -2744,7 +3330,7 @@
     decimal latest?;
 };
 
-type ConversationsHistoryResponseChannelActionsTs ballerinax/slack:5.0.1:ChannelActionsTsAnyOf1|anydata|();
+type ConversationsHistoryResponseChannelActionsTs ChannelActionsTsAnyOf1|anydata|();
 
 # Schema for successful response from users.lookupByEmail method
 
@@ -2761,6 +3347,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -2835,14 +3422,17 @@
     string cursor?;
     # The maximum number of items to return. Must be between 1 - 1000 both inclusive
     int 'limit?;
+    @http:Query {name: "team_id"}
     string teamId?;
 };
 
 
 type CallsUpdateBody record {
     # The URL required for a client to join the Call
+    @jsondata:Name {value: "join_url"}
     string joinUrl?;
     # When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL
+    @jsondata:Name {value: "desktop_app_join_url"}
     string desktopAppJoinUrl?;
     # `id` returned by the [`calls.add`](/methods/calls.add) method
     string id;
@@ -2878,6 +3468,7 @@
     # Reaction (emoji) name
     string name;
     # File comment to remove reaction from
+    @jsondata:Name {value: "file_comment"}
     string fileComment?;
     # Timestamp of the message to remove reaction from
     string timestamp?;
@@ -2885,14 +3476,22 @@
 
 
 type 200Team3 record {
+    @jsondata:Name {value: "image_132"}
     string image132;
+    @jsondata:Name {value: "image_102"}
     string image102;
+    @jsondata:Name {value: "image_68"}
     string image68;
+    @jsondata:Name {value: "image_default"}
     boolean imageDefault;
+    @jsondata:Name {value: "image_34"}
     string image34;
     string domain;
+    @jsondata:Name {value: "image_230"}
     string image230;
+    @jsondata:Name {value: "image_44"}
     string image44;
+    @jsondata:Name {value: "image_88"}
     string image88;
     string name;
     TeamDef id;
@@ -2902,10 +3501,12 @@
 
 type FilesRemoteListQueries record {
     # Filter files created after this timestamp (inclusive)
+    @http:Query {name: "ts_from"}
     decimal tsFrom?;
     # Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection. See [pagination](/docs/pagination) for more detail
     string cursor?;
     # Filter files created before this timestamp (inclusive)
+    @http:Query {name: "ts_to"}
     decimal tsTo?;
     # Filter files appearing in a specific channel, indicated by its ID
     string channel?;
@@ -2943,6 +3544,7 @@
     # The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached. Providing no `limit` value will result in Slack attempting to deliver you the entire result set. If the collection is too large you may experience `limit_required` or HTTP 500 errors
     int 'limit?;
     # Set this to `true` to receive the locale for users. Defaults to `false`
+    @http:Query {name: "include_locale"}
     boolean includeLocale?;
 };
 
@@ -2959,6 +3561,7 @@
     # A [view payload](/reference/surfaces/views). This must be a JSON-encoded string
     string view;
     # Exchange a trigger to post to the user
+    @http:Query {name: "trigger_id"}
     string triggerId;
 };
 
@@ -2985,6 +3588,7 @@
     # The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer no larger than 1000
     int 'limit?;
     # Set to `true` to exclude archived channels from the list
+    @http:Query {name: "exclude_archived"}
     boolean excludeArchived?;
 };
 
@@ -3011,7 +3615,9 @@
 
 type AdminConversationsRestrictAccessListGroupsQueries record {
     # The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization
+    @http:Query {name: "team_id"}
     string teamId?;
+    @http:Query {name: "channel_id"}
     string channelId;
 };
 
@@ -3040,12 +3646,16 @@
     # type of file
     string filetype?;
     # URL of the remote file
+    @jsondata:Name {value: "external_url"}
     string externalUrl?;
     # Preview of the document via `multipart/form-data`
+    @jsondata:Name {value: "preview_image"}
     string previewImage?;
     # Creator defined GUID for the file
+    @jsondata:Name {value: "external_id"}
     string externalId?;
     # A text file (txt, pdf, doc, etc.) containing textual search terms that are used to improve discovery of the remote file
+    @jsondata:Name {value: "indexable_file_contents"}
     string indexableFileContents?;
     # Title of the file being shared
     string title?;
@@ -3058,6 +3668,7 @@
 type AppsEventAuthorizationsListQueries record {
     string cursor?;
     int 'limit?;
+    @http:Query {name: "event_context"}
     string eventContext;
 };
 
@@ -3081,16 +3692,20 @@
     # The dialog definition. This must be a JSON-encoded string
     string dialog;
     # Exchange a trigger to post to the user
+    @http:Query {name: "trigger_id"}
     string triggerId;
 };
 
 
 type AdminUsersSessionResetBody record {
     # The ID of the user to wipe sessions for
+    @jsondata:Name {value: "user_id"}
     string userId;
     # Only expire mobile sessions (default: false)
+    @jsondata:Name {value: "mobile_only"}
     boolean mobileOnly?;
     # Only expire web sessions (default: false)
+    @jsondata:Name {value: "web_only"}
     boolean webOnly?;
 };
 
@@ -3115,49 +3730,73 @@
     "message" 'type;
 };
 
-type ChannelObjLatest ballerinax/slack:5.0.1:MessageObj|anydata|();
+type ChannelObjLatest MessageObj|anydata|();
 
 
 type ChannelObj record {
+    @jsondata:Name {value: "is_private"}
     boolean isPrivate;
+    @jsondata:Name {value: "accepted_user"}
     UserIdDef acceptedUser?;
     ChannelObjPurpose purpose;
+    @jsondata:Name {value: "is_moved"}
     int isMoved?;
+    @jsondata:Name {value: "is_pending_ext_shared"}
     boolean isPendingExtShared?;
+    @jsondata:Name {value: "unread_count"}
     int unreadCount?;
+    @jsondata:Name {value: "pending_shared"}
     TeamDef[] pendingShared?;
+    @jsondata:Name {value: "is_channel"}
     boolean isChannel;
+    @jsondata:Name {value: "is_shared"}
     boolean isShared;
     UserIdDef[] members;
+    @jsondata:Name {value: "is_non_threadable"}
     boolean isNonThreadable?;
+    @jsondata:Name {value: "is_read_only"}
     boolean isReadOnly?;
     ChannelIdDef id;
+    @jsondata:Name {value: "previous_names"}
     ChannelNameDef[] previousNames?;
     ChannelObjLatest[] latest?;
+    @jsondata:Name {value: "last_read"}
     TsDef lastRead?;
     UserIdDef creator;
+    @jsondata:Name {value: "is_frozen"}
     boolean isFrozen?;
+    @jsondata:Name {value: "is_member"}
     boolean isMember?;
+    @jsondata:Name {value: "is_mpim"}
     boolean isMpim;
     int created;
+    @jsondata:Name {value: "name_normalized"}
     string nameNormalized;
     decimal priority?;
+    @jsondata:Name {value: "unread_count_display"}
     int unreadCountDisplay?;
     int unlinked?;
+    @jsondata:Name {value: "is_archived"}
     boolean isArchived?;
+    @jsondata:Name {value: "is_general"}
     boolean isGeneral?;
+    @jsondata:Name {value: "num_members"}
     int numMembers?;
     string name;
     ChannelObjTopic topic;
+    @jsondata:Name {value: "is_thread_only"}
     boolean isThreadOnly?;
+    @jsondata:Name {value: "is_org_shared"}
     boolean isOrgShared;
 };
 
 
 type AdminUsersSetOwnerBody record {
     # Id of the user to promote to owner
+    @jsondata:Name {value: "user_id"}
     string userId;
     # The ID (`T1234`) of the workspace
+    @jsondata:Name {value: "team_id"}
     string teamId;
 };
 
@@ -3173,6 +3812,7 @@
     # Browse conversations by a specific user ID's membership. Non-public channels are restricted to those where the calling user shares membership
     string user?;
     # Set to `true` to exclude archived channels from the list
+    @http:Query {name: "exclude_archived"}
     boolean excludeArchived?;
 };
 
@@ -3196,6 +3836,7 @@
     # Comma-separated list of channel IDs where the file will be shared
     string channels?;
     # The globally unique identifier (GUID) for the file, as set by the app registering the file with Slack.  Either this field or `file` or both are required
+    @http:Query {name: "external_id"}
     string externalId?;
 };
 
@@ -3228,6 +3869,7 @@
 
 type AdminConversationsSetConversationPrefsBody record {
     # The channel to set the prefs for
+    @jsondata:Name {value: "channel_id"}
     string channelId;
     # The prefs for this channel in a stringified JSON format
     string prefs;
@@ -3241,6 +3883,7 @@
     # Channel where the message to get reactions for was posted
     string channel?;
     # File comment to get reactions for
+    @http:Query {name: "file_comment"}
     string fileComment?;
     # If true always return the complete reaction list
     boolean full?;
@@ -3252,6 +3895,7 @@
 
 type UsersProfileGetQueries record {
     # Include labels for each ID in custom profile fields
+    @http:Query {name: "include_labels"}
     boolean includeLabels?;
     # User to retrieve profile info for
     string user?;
@@ -3309,6 +3953,7 @@
 
 type AdminEmojiAddAliasBody record {
     # The alias of the emoji
+    @jsondata:Name {value: "alias_for"}
     string aliasFor;
     # The name of the emoji to be aliased. Colons (`:myemoji:`) around the value are not required, although they may be included
     string name;
@@ -3337,12 +3982,16 @@
 
 type AdminTeamsCreateBody record {
     # Description for the team
+    @jsondata:Name {value: "team_description"}
     string teamDescription?;
     # Team domain (for example, slacksoftballteam)
+    @jsondata:Name {value: "team_domain"}
     string teamDomain;
     # Team name (for example, Slack Softball Team)
+    @jsondata:Name {value: "team_name"}
     string teamName;
     # Who can join the team. A team's discoverability can be `open`, `closed`, `invite_only`, or `unlisted`
+    @jsondata:Name {value: "team_discoverability"}
     string teamDiscoverability?;
 };
 
@@ -3368,12 +4017,13 @@
     200User2 user;
 };
 
-type InlineResponseItems2002 ballerinax/slack:5.0.1:200AnyOf12|ballerinax/slack:5.0.1:200200AnyOf122|ballerinax/slack:5.0.1:200200200AnyOf1223|ballerinax/slack:5.0.1:200200200200AnyOf12234;
+type InlineResponseItems2002 200AnyOf12|200200AnyOf122|200200200AnyOf1223|200200200200AnyOf12234;
 
 # Schema for successful response from conversations.list method
 
 type ConversationsListResponse record {
     ConversationObj[] channels;
+    @jsondata:Name {value: "response_metadata"}
     ConversationsListResponseResponseMetadata responseMetadata?;
     OkTrueDef ok;
 };
@@ -3386,13 +4036,15 @@
     "file_comment" 'type;
 };
 
-type InlineResponseItems2001 ballerinax/slack:5.0.1:200AnyOf11|ballerinax/slack:5.0.1:200200AnyOf112|ballerinax/slack:5.0.1:200200200AnyOf1123;
+type InlineResponseItems2001 200AnyOf11|200200AnyOf112|200200200AnyOf1123;
 
 
 type ChatUpdateBody record {
     # Find and link channel names and usernames. Defaults to `none`. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, `none`
+    @jsondata:Name {value: "link_names"}
     string linkNames?;
     # Pass true to update the message as the authed user. [Bot users](/bot-users) in this context are considered authed users
+    @jsondata:Name {value: "as_user"}
     string asUser?;
     # A JSON-based array of structured attachments, presented as a URL-encoded string. This field is required when not presenting `text`. If you don't include this field, the message's previous `attachments` will be retained. To remove previous `attachments`, include an empty array for this field
     string attachments?;
@@ -3410,10 +4062,13 @@
 
 
 type AdminAppsRestrictBody record {
+    @jsondata:Name {value: "team_id"}
     string teamId?;
     # The id of the app to restrict
+    @jsondata:Name {value: "app_id"}
     string appId?;
     # The id of the request to restrict
+    @jsondata:Name {value: "request_id"}
     string requestId?;
 };
 
@@ -3421,6 +4076,7 @@
 type AdminConversationsRenameBody record {
     string name;
     # The channel to rename
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
@@ -3457,6 +4113,7 @@
     # Channel to add star to, or channel where the message to add star to was posted (used with `timestamp`)
     string channel?;
     # File comment to add star to
+    @jsondata:Name {value: "file_comment"}
     string fileComment?;
     # Timestamp of the message to add star to
     string timestamp?;
@@ -3465,10 +4122,13 @@
 
 type AdminUsergroupsAddChannelsBody record {
     # Comma separated string of channel IDs
+    @jsondata:Name {value: "channel_ids"}
     string channelIds;
     # ID of the IDP group to add default channels for
+    @jsondata:Name {value: "usergroup_id"}
     string usergroupId;
     # The workspace to add default channels in
+    @jsondata:Name {value: "team_id"}
     string teamId?;
 };
 
@@ -3553,12 +4213,14 @@
     # The maximum number of items to return. Must be between 1 - 1000 both inclusive
     int 'limit?;
     # The channel to determine connected workspaces within the organization for
+    @http:Query {name: "channel_id"}
     string channelId;
 };
 
 # Schema for successful response of admin.conversations.search
 
 type AdminConversationsSearchResponse record {
+    @jsondata:Name {value: "next_cursor"}
     string nextCursor;
     ChannelObj[] channels;
 };
@@ -3580,6 +4242,7 @@
 
 type AdminConversationsDeleteBody record {
     # The channel to delete
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
@@ -3610,6 +4273,7 @@
 
 type AdminConversationsConvertToPrivateBody record {
     # The channel to convert to private
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
@@ -3621,6 +4285,7 @@
     # Limit for how many users to be retrieved per page
     int 'limit?;
     # The ID (`T1234`) of the workspace
+    @http:Query {name: "team_id"}
     string teamId;
 };
 
@@ -3689,6 +4354,7 @@
 
 type AdminConversationsUnarchiveBody record {
     # The channel to unarchive
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
@@ -3703,8 +4369,10 @@
 
 type AdminTeamsSettingsSetIconBody record {
     # Image URL for the icon
+    @jsondata:Name {value: "image_url"}
     string imageUrl;
     # ID for the workspace to set the icon for
+    @jsondata:Name {value: "team_id"}
     string teamId;
     # Authentication token. Requires scope: `admin.teams:write`
     string token;
@@ -3713,7 +4381,8 @@
 # Schema for successful response from conversations.replies method
 
 type ConversationsRepliesResponse record {
-    (record {|ballerinax/slack:5.0.1:TsDef last_read?; ballerinax/slack:5.0.1:TsDef latest_reply?; int reply_count; ballerinax/slack:5.0.1:UserIdDef[] reply_users?; int reply_users_count?; ballerinax/slack:5.0.1:TeamDef source_team?; boolean subscribed; ballerinax/slack:5.0.1:TeamDef team?; string text; ballerinax/slack:5.0.1:TsDef thread_ts; ballerinax/slack:5.0.1:TsDef ts; string 'type; int unread_count?; ballerinax/slack:5.0.1:UserIdDef user; ballerinax/slack:5.0.1:UserProfileShortObj user_profile?; ballerinax/slack:5.0.1:TeamDef user_team?;|}|record {|boolean is_starred?; ballerinax/slack:5.0.1:UserIdDef parent_user_id; ballerinax/slack:5.0.1:TeamDef source_team?; ballerinax/slack:5.0.1:TeamDef team?; string text; ballerinax/slack:5.0.1:TsDef thread_ts; ballerinax/slack:5.0.1:TsDef ts; string 'type; ballerinax/slack:5.0.1:UserIdDef user; ballerinax/slack:5.0.1:UserProfileShortObj user_profile?; ballerinax/slack:5.0.1:TeamDef user_team?;|})[][] messages;
+    (record {|TsDef last_read?; TsDef latest_reply?; int reply_count; UserIdDef[] reply_users?; int reply_users_count?; TeamDef source_team?; boolean subscribed; TeamDef team?; string text; TsDef thread_ts; TsDef ts; string 'type; int unread_count?; UserIdDef user; UserProfileShortObj user_profile?; TeamDef user_team?;|}|record {|boolean is_starred?; UserIdDef parent_user_id; TeamDef source_team?; TeamDef team?; string text; TsDef thread_ts; TsDef ts; string 'type; UserIdDef user; UserProfileShortObj user_profile?; TeamDef user_team?;|})[][] messages;
+    @jsondata:Name {value: "has_more"}
     boolean hasMore?;
     OkTrueDef ok;
 };
@@ -3727,12 +4396,15 @@
 
 type ChatPostMessageBody record {
     # URL to an image to use as the icon for this message. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](#authorship) below
+    @jsondata:Name {value: "icon_url"}
     string iconUrl?;
     # Find and link channel names and usernames
+    @jsondata:Name {value: "link_names"}
     boolean linkNames?;
     # A JSON-based array of structured attachments, presented as a URL-encoded string
     string attachments?;
     # Emoji to use as the icon for this message. Overrides `icon_url`. Must be used in conjunction with `as_user` set to `false`, otherwise ignored. See [authorship](#authorship) below
+    @jsondata:Name {value: "icon_emoji"}
     string iconEmoji?;
     # A JSON-based array of structured blocks, presented as a URL-encoded string
     string blocks?;
@@ -3743,14 +4415,19 @@
     # Disable Slack markup parsing by setting to `false`. Enabled by default
     boolean mrkdwn?;
     # Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [authorship](#authorship) below
+    @jsondata:Name {value: "as_user"}
     string asUser?;
     # Provide another message's `ts` value to make this message a reply. Avoid using a reply's `ts` value; use its parent instead
+    @jsondata:Name {value: "thread_ts"}
     string threadTs?;
     # Pass false to disable unfurling of media content
+    @jsondata:Name {value: "unfurl_media"}
     boolean unfurlMedia?;
     # Used in conjunction with `thread_ts` and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to `false`
+    @jsondata:Name {value: "reply_broadcast"}
     boolean replyBroadcast?;
     # Pass true to enable unfurling of primarily text-based content
+    @jsondata:Name {value: "unfurl_links"}
     boolean unfurlLinks?;
     # How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail
     string text?;
@@ -3770,6 +4447,7 @@
     # Key-value object of outputs from your step. Keys of this object reflect the configured `key` properties of your [`outputs`](/reference/workflows/workflow_step#output) array from your `workflow_step` object
     string outputs?;
     # Context identifier that maps to the correct workflow step execution
+    @http:Query {name: "workflow_step_execute_id"}
     string workflowStepExecuteId;
 };
 
@@ -3788,8 +4466,10 @@
 
 type ChatDeleteScheduledMessageBody record {
     # Pass true to delete the message as the authed user with `chat:write:user` scope. [Bot users](/bot-users) in this context are considered authed users. If unused or false, the message will be deleted with `chat:write:bot` scope
+    @jsondata:Name {value: "as_user"}
     boolean asUser?;
     # `scheduled_message_id` returned from call to chat.scheduleMessage
+    @jsondata:Name {value: "scheduled_message_id"}
     string scheduledMessageId;
     # The channel the scheduled_message is posting to
     string channel;
@@ -3830,6 +4510,7 @@
     # A mention handle. Must be unique among channels, users and User Groups
     string 'handle?;
     # Include the number of users in each User Group
+    @jsondata:Name {value: "include_count"}
     boolean includeCount?;
 };
 
@@ -3861,8 +4542,10 @@
 
 type AdminUsersSetRegularBody record {
     # The ID of the user to designate as a regular user
+    @jsondata:Name {value: "user_id"}
     string userId;
     # The ID (`T1234`) of the workspace
+    @jsondata:Name {value: "team_id"}
     string teamId;
 };
 
@@ -3875,12 +4558,16 @@
 
 type AdminConversationsSetTeamsBody record {
     # True if channel has to be converted to an org channel
+    @jsondata:Name {value: "org_channel"}
     boolean orgChannel?;
     # A comma-separated list of workspaces to which the channel should be shared. Not required if the channel is being shared org-wide
+    @jsondata:Name {value: "target_team_ids"}
     string targetTeamIds?;
     # The workspace to which the channel belongs. Omit this argument if the channel is a cross-workspace shared channel
+    @jsondata:Name {value: "team_id"}
     string teamId?;
     # The encoded `channel_id` to add or remove to workspaces
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
@@ -3906,12 +4593,15 @@
 
 type TeamIntegrationLogsQueries record {
     # Filter logs to this service. Defaults to all logs
+    @http:Query {name: "service_id"}
     string serviceId?;
     string count?;
     # Filter logs with this change type. Defaults to all logs
+    @http:Query {name: "change_type"}
     string changeType?;
     string page?;
     # Filter logs to this Slack app. Defaults to all logs
+    @http:Query {name: "app_id"}
     string appId?;
     # Filter logs generated by this user’s actions. Defaults to all logs
     string user?;
@@ -3930,6 +4620,7 @@
     string cursor?;
     # The maximum number of items to return. Must be between 1 - 1000 both inclusive
     int 'limit?;
+    @http:Query {name: "team_id"}
     string teamId;
 };
 
@@ -3971,10 +4662,11 @@
     string cursor?;
     # The maximum number of items to return
     int 'limit?;
+    @http:Query {name: "team_id"}
     string teamId;
 };
 
-type InlineResponseItems200 ballerinax/slack:5.0.1:200AnyOf1|ballerinax/slack:5.0.1:200200AnyOf12;
+type InlineResponseItems200 200AnyOf1|200200AnyOf12;
 
 # This method either only returns a brief _OK_ response or a verbose schema is not available for this method
 
@@ -4024,6 +4716,7 @@
 
 type AdminConversationsGetConversationPrefsQueries record {
     # The channel to get preferences for
+    @http:Query {name: "channel_id"}
     string channelId;
 };
 
@@ -4071,6 +4764,7 @@
 
 type ChatDeleteBody record {
     # Pass true to delete the message as the authed user with `chat:write:user` scope. [Bot users](/bot-users) in this context are considered authed users. If unused or false, the message will be deleted with `chat:write:bot` scope
+    @jsondata:Name {value: "as_user"}
     boolean asUser?;
     # Channel containing the message to be deleted
     string channel?;
@@ -4081,10 +4775,15 @@
 # Schema for successful response from conversations.history method
 
 type ConversationsHistoryResponse record {
+    @jsondata:Name {value: "channel_actions_count"}
     int channelActionsCount;
+    @jsondata:Name {value: "pin_count"}
     int pinCount;
+    @constraint:Array {minLength: 1}
     MessageObj[] messages;
+    @jsondata:Name {value: "channel_actions_ts"}
     ConversationsHistoryResponseChannelActionsTs[] channelActionsTs;
+    @jsondata:Name {value: "has_more"}
     boolean hasMore;
     OkTrueDef ok;
 };
@@ -4092,12 +4791,15 @@
 
 type UsersSetPhotoBody record {
     # Y coordinate of top-left corner of crop box
+    @jsondata:Name {value: "crop_y"}
     string cropY?;
     # File contents via `multipart/form-data`
     string image?;
     # Width/height of crop box (always square)
+    @jsondata:Name {value: "crop_w"}
     string cropW?;
     # X coordinate of top-left corner of crop box
+    @jsondata:Name {value: "crop_x"}
     string cropX?;
     # Authentication token. Requires scope: `users.profile:write`
     string token;
@@ -4131,6 +4833,7 @@
 
 type ConversationsLeaveResponse record {
     OkTrueDef ok;
+    @jsondata:Name {value: "not_in_channel"}
     true notInChannel?;
 };
 
@@ -4155,6 +4858,7 @@
 
 type DndSetSnoozeBody record {
     # Number of minutes, from now, to snooze until
+    @jsondata:Name {value: "num_minutes"}
     string numMinutes;
     # Authentication token. Requires scope: `dnd:write`
     string token;
@@ -4163,6 +4867,7 @@
 
 type ConversationsCreateBody record {
     # Create a private channel instead of a public one
+    @jsondata:Name {value: "is_private"}
     boolean isPrivate?;
     # Name of the public or private channel to create
     string name?;
@@ -4219,8 +4924,10 @@
 
 type AdminConversationsInviteBody record {
     # The users to invite
+    @jsondata:Name {value: "user_ids"}
     string userIds;
     # The channel that the users will be invited to
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
@@ -4241,7 +4948,9 @@
 # Schema for successful response of admin.conversations.getTeams
 
 type AdminConversationsGetTeamsResponse record {
+    @jsondata:Name {value: "team_ids"}
     TeamDef[] teamIds;
+    @jsondata:Name {value: "response_metadata"}
     AdminConversationsGetTeamsResponseResponseMetadata responseMetadata?;
     OkTrueDef ok;
 };
@@ -4257,6 +4966,7 @@
     # Specify a file by providing its ID
     string file?;
     # Creator defined GUID for the file
+    @jsondata:Name {value: "external_id"}
     string externalId?;
     # Authentication token. Requires scope: `remote_files:write`
     string token?;
@@ -4266,6 +4976,7 @@
 
 type AppsPermissionsUsersRequestQueries record {
     # Token used to trigger the request
+    @http:Query {name: "trigger_id"}
     string triggerId;
     # A comma separated list of user scopes to request for
     string scopes;
@@ -4305,6 +5016,7 @@
 
 type ConversationsOpenBody record {
     # Boolean, indicates you want the full IM channel definition in the response
+    @jsondata:Name {value: "return_im"}
     boolean returnIm?;
     # Resume a conversation by supplying an `im` or `mpim`'s ID. Or provide the `users` field instead
     string channel?;
@@ -4318,6 +5030,7 @@
     # A [view payload](/reference/surfaces/views). This must be a JSON-encoded string
     string view;
     # `id` of the user you want publish a view to
+    @http:Query {name: "user_id"}
     string userId;
     # A string that represents view state to protect against possible race conditions
     string hash?;
@@ -4349,11 +5062,11 @@
 
     # List approved apps for an org or workspace.
     # 
-    resource function get admin\.apps\.approved\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", string enterpriseId = "", anydata Additional Values, AdminAppsApprovedListQueries queries) returns DefaultSuccessResponse1|error;
+    resource function get admin\.apps\.approved\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", string enterpriseId = "", AdminAppsApprovedListQueries queries) returns DefaultSuccessResponse1|error;
 
     # List app requests for a team/workspace.
     # 
-    resource function get admin\.apps\.requests\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", anydata Additional Values, AdminAppsRequestsListQueries queries) returns DefaultSuccessResponse2|error;
+    resource function get admin\.apps\.requests\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", AdminAppsRequestsListQueries queries) returns DefaultSuccessResponse2|error;
 
     # Restrict an app for installation on a workspace.
     # 
@@ -4361,7 +5074,7 @@
 
     # List restricted apps for an org or workspace.
     # 
-    resource function get admin\.apps\.restricted\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", string enterpriseId = "", anydata Additional Values, AdminAppsRestrictedListQueries queries) returns DefaultSuccessResponse4|error;
+    resource function get admin\.apps\.restricted\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", string enterpriseId = "", AdminAppsRestrictedListQueries queries) returns DefaultSuccessResponse4|error;
 
     # Archive a public or private channel.
     # 
@@ -4385,15 +5098,15 @@
 
     # List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM.
     # 
-    resource function get admin\.conversations\.ekm\.listOriginalConnectedChannelInfo(map<string|string[]> headers = {}, string channelIds = "", string cursor = "", string teamIds = "", int limit = 0, anydata Additional Values, AdminConversationsEkmListOriginalConnectedChannelInfoQueries queries) returns DefaultSuccessResponse5|error;
+    resource function get admin\.conversations\.ekm\.listOriginalConnectedChannelInfo(map<string|string[]> headers = {}, string channelIds = "", string cursor = "", string teamIds = "", int limit = 0, AdminConversationsEkmListOriginalConnectedChannelInfoQueries queries) returns DefaultSuccessResponse5|error;
 
     # Get conversation preferences for a public or private channel.
     # 
-    resource function get admin\.conversations\.getConversationPrefs(map<string|string[]> headers = {}, string channelId = "", anydata Additional Values, AdminConversationsGetConversationPrefsQueries queries) returns AdminConversationsGetConversationPrefsResponse|error;
+    resource function get admin\.conversations\.getConversationPrefs(map<string|string[]> headers = {}, string channelId = "", AdminConversationsGetConversationPrefsQueries queries) returns AdminConversationsGetConversationPrefsResponse|error;
 
     # Get all the workspaces a given public or private channel is connected to within this Enterprise org.
     # 
-    resource function get admin\.conversations\.getTeams(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string channelId = "", anydata Additional Values, AdminConversationsGetTeamsQueries queries) returns AdminConversationsGetTeamsResponse|error;
+    resource function get admin\.conversations\.getTeams(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string channelId = "", AdminConversationsGetTeamsQueries queries) returns AdminConversationsGetTeamsResponse|error;
 
     # Invite a user to a public or private channel.
     # 
@@ -4409,7 +5122,7 @@
 
     # List all IDP Groups linked to a channel
     # 
-    resource function get admin\.conversations\.restrictAccess\.listGroups(map<string|string[]> headers = {}, string teamId = "", string channelId = "", anydata Additional Values, AdminConversationsRestrictAccessListGroupsQueries queries) returns DefaultSuccessResponse7|error;
+    resource function get admin\.conversations\.restrictAccess\.listGroups(map<string|string[]> headers = {}, string teamId = "", string channelId = "", AdminConversationsRestrictAccessListGroupsQueries queries) returns DefaultSuccessResponse7|error;
 
     # Remove a linked IDP group linked from a private channel
     # 
@@ -4417,7 +5130,7 @@
 
     # Search for public or private channels in an Enterprise organization.
     # 
-    resource function get admin\.conversations\.search(map<string|string[]> headers = {}, string cursor = "", string searchChannelTypes = "", string teamIds = "", string query = "", int limit = 0, string sort = "", string sortDir = "", anydata Additional Values, AdminConversationsSearchQueries queries) returns AdminConversationsSearchResponse|error;
+    resource function get admin\.conversations\.search(map<string|string[]> headers = {}, string cursor = "", string searchChannelTypes = "", string teamIds = "", string query = "", int limit = 0, string sort = "", string sortDir = "", AdminConversationsSearchQueries queries) returns AdminConversationsSearchResponse|error;
 
     # Set the posting permissions for a public or private channel.
     # 
@@ -4441,7 +5154,7 @@
 
     # List emoji for an Enterprise Grid organization.
     # 
-    resource function get admin\.emoji\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, anydata Additional Values, AdminEmojiListQueries queries) returns DefaultSuccessResponse12|error;
+    resource function get admin\.emoji\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, AdminEmojiListQueries queries) returns DefaultSuccessResponse12|error;
 
     # Remove an emoji across an Enterprise Grid organization
     # 
@@ -4457,11 +5170,11 @@
 
     # List all approved workspace invite requests.
     # 
-    resource function get admin\.inviteRequests\.approved\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", anydata Additional Values, AdminInviteRequestsApprovedListQueries queries) returns DefaultSuccessResponse16|error;
+    resource function get admin\.inviteRequests\.approved\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", AdminInviteRequestsApprovedListQueries queries) returns DefaultSuccessResponse16|error;
 
     # List all denied workspace invite requests.
     # 
-    resource function get admin\.inviteRequests\.denied\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", anydata Additional Values, AdminInviteRequestsDeniedListQueries queries) returns DefaultSuccessResponse17|error;
+    resource function get admin\.inviteRequests\.denied\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", AdminInviteRequestsDeniedListQueries queries) returns DefaultSuccessResponse17|error;
 
     # Deny a workspace invite request.
     # 
@@ -4469,11 +5182,11 @@
 
     # List all pending workspace invite requests.
     # 
-    resource function get admin\.inviteRequests\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", anydata Additional Values, AdminInviteRequestsListQueries queries) returns DefaultSuccessResponse19|error;
+    resource function get admin\.inviteRequests\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", AdminInviteRequestsListQueries queries) returns DefaultSuccessResponse19|error;
 
     # List all of the admins on a given workspace.
     # 
-    resource function get admin\.teams\.admins\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", anydata Additional Values, AdminTeamsAdminsListQueries queries) returns DefaultSuccessResponse20|error;
+    resource function get admin\.teams\.admins\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", AdminTeamsAdminsListQueries queries) returns DefaultSuccessResponse20|error;
 
     # Create an Enterprise team.
     # 
@@ -4481,15 +5194,15 @@
 
     # List all teams on an Enterprise organization
     # 
-    resource function get admin\.teams\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, anydata Additional Values, AdminTeamsListQueries queries) returns DefaultSuccessResponse22|error;
+    resource function get admin\.teams\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, AdminTeamsListQueries queries) returns DefaultSuccessResponse22|error;
 
     # List all of the owners on a given workspace.
     # 
-    resource function get admin\.teams\.owners\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", anydata Additional Values, AdminTeamsOwnersListQueries queries) returns DefaultSuccessResponse23|error;
+    resource function get admin\.teams\.owners\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", AdminTeamsOwnersListQueries queries) returns DefaultSuccessResponse23|error;
 
     # Fetch information about settings in a workspace
     # 
-    resource function get admin\.teams\.settings\.info(map<string|string[]> headers = {}, string teamId = "", anydata Additional Values, AdminTeamsSettingsInfoQueries queries) returns DefaultSuccessResponse24|error;
+    resource function get admin\.teams\.settings\.info(map<string|string[]> headers = {}, string teamId = "", AdminTeamsSettingsInfoQueries queries) returns DefaultSuccessResponse24|error;
 
     # Set the default channels of a workspace.
     # 
@@ -4521,7 +5234,7 @@
 
     # List the channels linked to an org-level IDP group (user group).
     # 
-    resource function get admin\.usergroups\.listChannels(map<string|string[]> headers = {}, boolean includeNumMembers = false, string usergroupId = "", string teamId = "", anydata Additional Values, AdminUsergroupsListChannelsQueries queries) returns DefaultSuccessResponse32|error;
+    resource function get admin\.usergroups\.listChannels(map<string|string[]> headers = {}, boolean includeNumMembers = false, string usergroupId = "", string teamId = "", AdminUsergroupsListChannelsQueries queries) returns DefaultSuccessResponse32|error;
 
     # Remove one or more default channels from an org-level IDP group (user group).
     # 
@@ -4537,7 +5250,7 @@
 
     # List users on a workspace
     # 
-    resource function get admin\.users\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", anydata Additional Values, AdminUsersListQueries queries) returns DefaultSuccessResponse36|error;
+    resource function get admin\.users\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", AdminUsersListQueries queries) returns DefaultSuccessResponse36|error;
 
     # Remove a user from a workspace.
     # 
@@ -4569,11 +5282,11 @@
 
     # Checks API calling code.
     # 
-    resource function get api\.test(map<string|string[]> headers = {}, string foo = "", anydata Additional Values, ApiTestQueries queries) returns ApiTestResponse|error;
+    resource function get api\.test(map<string|string[]> headers = {}, string foo = "", ApiTestQueries queries) returns ApiTestResponse|error;
 
     # Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.
     # 
-    resource function get apps\.event\.authorizations\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string eventContext = "", anydata Additional Values, AppsEventAuthorizationsListQueries queries) returns DefaultSuccessResponse44|error;
+    resource function get apps\.event\.authorizations\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string eventContext = "", AppsEventAuthorizationsListQueries queries) returns DefaultSuccessResponse44|error;
 
     # Returns list of permissions this app has on a team.
     # 
@@ -4581,11 +5294,11 @@
 
     # Allows an app to request additional scopes
     # 
-    resource function get apps\.permissions\.request(map<string|string[]> headers = {}, string triggerId = "", string scopes = "", anydata Additional Values, AppsPermissionsRequestQueries queries) returns AppsPermissionsRequestResponse|error;
+    resource function get apps\.permissions\.request(map<string|string[]> headers = {}, string triggerId = "", string scopes = "", AppsPermissionsRequestQueries queries) returns AppsPermissionsRequestResponse|error;
 
     # Returns list of resource grants this app has on a team.
     # 
-    resource function get apps\.permissions\.resources\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, anydata Additional Values, AppsPermissionsResourcesListQueries queries) returns AppsPermissionsResourcesListResponse|error;
+    resource function get apps\.permissions\.resources\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, AppsPermissionsResourcesListQueries queries) returns AppsPermissionsResourcesListResponse|error;
 
     # Returns list of scopes this app has on a team.
     # 
@@ -4593,19 +5306,19 @@
 
     # Returns list of user grants and corresponding scopes this app has on a team.
     # 
-    resource function get apps\.permissions\.users\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, anydata Additional Values, AppsPermissionsUsersListQueries queries) returns DefaultSuccessResponse45|error;
+    resource function get apps\.permissions\.users\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, AppsPermissionsUsersListQueries queries) returns DefaultSuccessResponse45|error;
 
     # Enables an app to trigger a permissions modal to grant an app access to a user access scope.
     # 
-    resource function get apps\.permissions\.users\.request(map<string|string[]> headers = {}, string triggerId = "", string scopes = "", string user = "", anydata Additional Values, AppsPermissionsUsersRequestQueries queries) returns DefaultSuccessResponse46|error;
+    resource function get apps\.permissions\.users\.request(map<string|string[]> headers = {}, string triggerId = "", string scopes = "", string user = "", AppsPermissionsUsersRequestQueries queries) returns DefaultSuccessResponse46|error;
 
     # Uninstalls your app from a workspace.
     # 
-    resource function get apps\.uninstall(map<string|string[]> headers = {}, string clientSecret = "", string clientId = "", anydata Additional Values, AppsUninstallQueries queries) returns AppsUninstallResponse|error;
+    resource function get apps\.uninstall(map<string|string[]> headers = {}, string clientSecret = "", string clientId = "", AppsUninstallQueries queries) returns AppsUninstallResponse|error;
 
     # Revokes a token.
     # 
-    resource function get auth\.revoke(map<string|string[]> headers = {}, boolean test = false, anydata Additional Values, AuthRevokeQueries queries) returns AuthRevokeResponse|error;
+    resource function get auth\.revoke(map<string|string[]> headers = {}, boolean test = false, AuthRevokeQueries queries) returns AuthRevokeResponse|error;
 
     # Checks authentication & identity.
     # 
@@ -4613,7 +5326,7 @@
 
     # Gets information about a bot user.
     # 
-    resource function get bots\.info(map<string|string[]> headers = {}, string bot = "", anydata Additional Values, BotsInfoQueries queries) returns BotsInfoResponse|error;
+    resource function get bots\.info(map<string|string[]> headers = {}, string bot = "", BotsInfoQueries queries) returns BotsInfoResponse|error;
 
     # Registers a new Call.
     # 
@@ -4625,7 +5338,7 @@
 
     # Returns information about a Call.
     # 
-    resource function get calls\.info(map<string|string[]> headers = {}, string id = "", anydata Additional Values, CallsInfoQueries queries) returns DefaultSuccessResponse49|error;
+    resource function get calls\.info(map<string|string[]> headers = {}, string id = "", CallsInfoQueries queries) returns DefaultSuccessResponse49|error;
 
     # Registers new participants added to a Call.
     # 
@@ -4649,7 +5362,7 @@
 
     # Retrieve a permalink URL for a specific extant message
     # 
-    resource function get chat\.getPermalink(map<string|string[]> headers = {}, string channel = "", string messageTs = "", anydata Additional Values, ChatGetPermalinkQueries queries) returns ChatGetPermalinkResponse|error;
+    resource function get chat\.getPermalink(map<string|string[]> headers = {}, string channel = "", string messageTs = "", ChatGetPermalinkQueries queries) returns ChatGetPermalinkResponse|error;
 
     # Share a me message into a channel.
     # 
@@ -4669,7 +5382,7 @@
 
     # Returns a list of scheduled messages.
     # 
-    resource function get chat\.scheduledMessages\.list(map<string|string[]> headers = {}, string cursor = "", decimal oldest = 0.0d, string channel = "", int limit = 0, decimal latest = 0.0d, anydata Additional Values, ChatScheduledMessagesListQueries queries) returns ChatScheduledMessagesListResponse|error;
+    resource function get chat\.scheduledMessages\.list(map<string|string[]> headers = {}, string cursor = "", decimal oldest = 0.0d, string channel = "", int limit = 0, decimal latest = 0.0d, ChatScheduledMessagesListQueries queries) returns ChatScheduledMessagesListResponse|error;
 
     # Provide custom unfurl behavior for user-posted URLs
     # 
@@ -4693,11 +5406,11 @@
 
     # Fetches a conversation's history of messages and events.
     # 
-    resource function get conversations\.history(map<string|string[]> headers = {}, string cursor = "", boolean inclusive = false, decimal oldest = 0.0d, string channel = "", int limit = 0, decimal latest = 0.0d, anydata Additional Values, ConversationsHistoryQueries queries) returns ConversationsHistoryResponse|error;
+    resource function get conversations\.history(map<string|string[]> headers = {}, string cursor = "", boolean inclusive = false, decimal oldest = 0.0d, string channel = "", int limit = 0, decimal latest = 0.0d, ConversationsHistoryQueries queries) returns ConversationsHistoryResponse|error;
 
     # Retrieve information about a conversation.
     # 
-    resource function get conversations\.info(map<string|string[]> headers = {}, boolean includeNumMembers = false, string channel = "", boolean includeLocale = false, anydata Additional Values, ConversationsInfoQueries queries) returns ConversationsInfoResponse|error;
+    resource function get conversations\.info(map<string|string[]> headers = {}, boolean includeNumMembers = false, string channel = "", boolean includeLocale = false, ConversationsInfoQueries queries) returns ConversationsInfoResponse|error;
 
     # Invites users to a channel.
     # 
@@ -4717,7 +5430,7 @@
 
     # Lists all channels in a Slack team.
     # 
-    resource function get conversations\.list(map<string|string[]> headers = {}, string cursor = "", string types = "", int limit = 0, boolean excludeArchived = false, anydata Additional Values, ConversationsListQueries queries) returns ConversationsListResponse|error;
+    resource function get conversations\.list(map<string|string[]> headers = {}, string cursor = "", string types = "", int limit = 0, boolean excludeArchived = false, ConversationsListQueries queries) returns ConversationsListResponse|error;
 
     # Sets the read cursor in a channel.
     # 
@@ -4725,7 +5438,7 @@
 
     # Retrieve members of a conversation.
     # 
-    resource function get conversations\.members(map<string|string[]> headers = {}, string cursor = "", string channel = "", int limit = 0, anydata Additional Values, ConversationsMembersQueries queries) returns ConversationsMembersResponse|error;
+    resource function get conversations\.members(map<string|string[]> headers = {}, string cursor = "", string channel = "", int limit = 0, ConversationsMembersQueries queries) returns ConversationsMembersResponse|error;
 
     # Opens or resumes a direct message or multi-person direct message.
     # 
@@ -4737,7 +5450,7 @@
 
     # Retrieve a thread of messages posted to a conversation
     # 
-    resource function get conversations\.replies(map<string|string[]> headers = {}, string cursor = "", boolean inclusive = false, decimal oldest = 0.0d, string channel = "", int limit = 0, decimal ts = 0.0d, decimal latest = 0.0d, anydata Additional Values, ConversationsRepliesQueries queries) returns ConversationsRepliesResponse|error;
+    resource function get conversations\.replies(map<string|string[]> headers = {}, string cursor = "", boolean inclusive = false, decimal oldest = 0.0d, string channel = "", int limit = 0, decimal ts = 0.0d, decimal latest = 0.0d, ConversationsRepliesQueries queries) returns ConversationsRepliesResponse|error;
 
     # Sets the purpose for a conversation.
     # 
@@ -4753,7 +5466,7 @@
 
     # Open a dialog with a user
     # 
-    resource function get dialog\.open(map<string|string[]> headers = {}, string dialog = "", string triggerId = "", anydata Additional Values, DialogOpenQueries queries) returns DialogOpenResponse|error;
+    resource function get dialog\.open(map<string|string[]> headers = {}, string dialog = "", string triggerId = "", DialogOpenQueries queries) returns DialogOpenResponse|error;
 
     # Ends the current user's Do Not Disturb session immediately.
     # 
@@ -4765,7 +5478,7 @@
 
     # Retrieves a user's current Do Not Disturb status.
     # 
-    resource function get dnd\.info(map<string|string[]> headers = {}, string user = "", anydata Additional Values, DndInfoQueries queries) returns DndInfoResponse|error;
+    resource function get dnd\.info(map<string|string[]> headers = {}, string user = "", DndInfoQueries queries) returns DndInfoResponse|error;
 
     # Turns on Do Not Disturb mode for the current user, or changes its duration.
     # 
@@ -4773,7 +5486,7 @@
 
     # Retrieves the Do Not Disturb status for up to 50 users on a team.
     # 
-    resource function get dnd\.teamInfo(map<string|string[]> headers = {}, string users = "", anydata Additional Values, DndTeamInfoQueries queries) returns DefaultSuccessResponse53|error;
+    resource function get dnd\.teamInfo(map<string|string[]> headers = {}, string users = "", DndTeamInfoQueries queries) returns DefaultSuccessResponse53|error;
 
     # Lists custom emoji for a team.
     # 
@@ -4789,11 +5502,11 @@
 
     # Gets information about a file.
     # 
-    resource function get files\.info(map<string|string[]> headers = {}, string cursor = "", string file = "", string count = "", int limit = 0, string page = "", anydata Additional Values, FilesInfoQueries queries) returns FilesInfoResponse|error;
+    resource function get files\.info(map<string|string[]> headers = {}, string cursor = "", string file = "", string count = "", int limit = 0, string page = "", FilesInfoQueries queries) returns FilesInfoResponse|error;
 
     # List for a team, in a channel, or from a user with applied filters.
     # 
-    resource function get files\.list(map<string|string[]> headers = {}, decimal tsFrom = 0.0d, boolean showFilesHiddenByLimit = false, string types = "", decimal tsTo = 0.0d, string channel = "", string count = "", string page = "", string user = "", anydata Additional Values, FilesListQueries queries) returns FilesListResponse|error;
+    resource function get files\.list(map<string|string[]> headers = {}, decimal tsFrom = 0.0d, boolean showFilesHiddenByLimit = false, string types = "", decimal tsTo = 0.0d, string channel = "", string count = "", string page = "", string user = "", FilesListQueries queries) returns FilesListResponse|error;
 
     # Adds a file from a remote service
     # 
@@ -4801,11 +5514,11 @@
 
     # Retrieve information about a remote file added to Slack
     # 
-    resource function get files\.remote\.info(map<string|string[]> headers = {}, string file = "", string externalId = "", anydata Additional Values, FilesRemoteInfoQueries queries) returns DefaultSuccessResponse56|error;
+    resource function get files\.remote\.info(map<string|string[]> headers = {}, string file = "", string externalId = "", FilesRemoteInfoQueries queries) returns DefaultSuccessResponse56|error;
 
     # Retrieve information about a remote file added to Slack
     # 
-    resource function get files\.remote\.list(map<string|string[]> headers = {}, decimal tsFrom = 0.0d, string cursor = "", decimal tsTo = 0.0d, string channel = "", int limit = 0, anydata Additional Values, FilesRemoteListQueries queries) returns DefaultSuccessResponse57|error;
+    resource function get files\.remote\.list(map<string|string[]> headers = {}, decimal tsFrom = 0.0d, string cursor = "", decimal tsTo = 0.0d, string channel = "", int limit = 0, FilesRemoteListQueries queries) returns DefaultSuccessResponse57|error;
 
     # Remove a remote file.
     # 
@@ -4813,7 +5526,7 @@
 
     # Share a remote file into a channel.
     # 
-    resource function get files\.remote\.share(map<string|string[]> headers = {}, string file = "", string channels = "", string externalId = "", anydata Additional Values, FilesRemoteShareQueries queries) returns DefaultSuccessResponse59|error;
+    resource function get files\.remote\.share(map<string|string[]> headers = {}, string file = "", string channels = "", string externalId = "", FilesRemoteShareQueries queries) returns DefaultSuccessResponse59|error;
 
     # Updates an existing remote file.
     # 
@@ -4833,19 +5546,19 @@
 
     # For Enterprise Grid workspaces, map local user IDs to global user IDs
     # 
-    resource function get migration\.exchange(map<string|string[]> headers = {}, boolean toOld = false, string teamId = "", string users = "", anydata Additional Values, MigrationExchangeQueries queries) returns MigrationExchangeResponse|error;
+    resource function get migration\.exchange(map<string|string[]> headers = {}, boolean toOld = false, string teamId = "", string users = "", MigrationExchangeQueries queries) returns MigrationExchangeResponse|error;
 
     # Exchanges a temporary OAuth verifier code for an access token.
     # 
-    resource function get oauth\.access(map<string|string[]> headers = {}, boolean singleChannel = false, string code = "", string clientSecret = "", string redirectUri = "", string clientId = "", anydata Additional Values, OauthAccessQueries queries) returns DefaultSuccessResponse61|error;
+    resource function get oauth\.access(map<string|string[]> headers = {}, boolean singleChannel = false, string code = "", string clientSecret = "", string redirectUri = "", string clientId = "", OauthAccessQueries queries) returns DefaultSuccessResponse61|error;
 
     # Exchanges a temporary OAuth verifier code for a workspace token.
     # 
-    resource function get oauth\.token(map<string|string[]> headers = {}, boolean singleChannel = false, string code = "", string clientSecret = "", string redirectUri = "", string clientId = "", anydata Additional Values, OauthTokenQueries queries) returns DefaultSuccessResponse62|error;
+    resource function get oauth\.token(map<string|string[]> headers = {}, boolean singleChannel = false, string code = "", string clientSecret = "", string redirectUri = "", string clientId = "", OauthTokenQueries queries) returns DefaultSuccessResponse62|error;
 
     # Exchanges a temporary OAuth verifier code for an access token.
     # 
-    resource function get oauth\.v2\.access(map<string|string[]> headers = {}, string code = "", string clientSecret = "", string redirectUri = "", string clientId = "", anydata Additional Values, OauthV2AccessQueries queries) returns DefaultSuccessResponse63|error;
+    resource function get oauth\.v2\.access(map<string|string[]> headers = {}, string code = "", string clientSecret = "", string redirectUri = "", string clientId = "", OauthV2AccessQueries queries) returns DefaultSuccessResponse63|error;
 
     # Pins an item to a channel.
     # 
@@ -4853,7 +5566,7 @@
 
     # Lists items pinned to a channel.
     # 
-    resource function get pins\.list(map<string|string[]> headers = {}, string channel = "", anydata Additional Values, PinsListQueries queries) returns InlineResponseItems200[]|error;
+    resource function get pins\.list(map<string|string[]> headers = {}, string channel = "", PinsListQueries queries) returns InlineResponseItems200[]|error;
 
     # Un-pins an item from a channel.
     # 
@@ -4865,11 +5578,11 @@
 
     # Gets reactions for an item.
     # 
-    resource function get reactions\.get(map<string|string[]> headers = {}, string file = "", string channel = "", string fileComment = "", boolean full = false, string timestamp = "", anydata Additional Values, ReactionsGetQueries queries) returns InlineResponseItems2001[]|error;
+    resource function get reactions\.get(map<string|string[]> headers = {}, string file = "", string channel = "", string fileComment = "", boolean full = false, string timestamp = "", ReactionsGetQueries queries) returns InlineResponseItems2001[]|error;
 
     # Lists reactions made by a user.
     # 
-    resource function get reactions\.list(map<string|string[]> headers = {}, string cursor = "", int count = 0, int limit = 0, int page = 0, string user = "", boolean full = false, anydata Additional Values, ReactionsListQueries queries) returns ReactionsListResponse|error;
+    resource function get reactions\.list(map<string|string[]> headers = {}, string cursor = "", int count = 0, int limit = 0, int page = 0, string user = "", boolean full = false, ReactionsListQueries queries) returns ReactionsListResponse|error;
 
     # Removes a reaction from an item.
     # 
@@ -4889,7 +5602,7 @@
 
     # Gets information about a reminder.
     # 
-    resource function get reminders\.info(map<string|string[]> headers = {}, string reminder = "", anydata Additional Values, RemindersInfoQueries queries) returns RemindersInfoResponse|error;
+    resource function get reminders\.info(map<string|string[]> headers = {}, string reminder = "", RemindersInfoQueries queries) returns RemindersInfoResponse|error;
 
     # Lists all reminders created by or for a given user.
     # 
@@ -4897,11 +5610,11 @@
 
     # Starts a Real Time Messaging session.
     # 
-    resource function get rtm\.connect(map<string|string[]> headers = {}, boolean batchPresenceAware = false, boolean presenceSub = false, anydata Additional Values, RtmConnectQueries queries) returns RtmConnectResponse|error;
+    resource function get rtm\.connect(map<string|string[]> headers = {}, boolean batchPresenceAware = false, boolean presenceSub = false, RtmConnectQueries queries) returns RtmConnectResponse|error;
 
     # Searches for messages matching a query.
     # 
-    resource function get search\.messages(map<string|string[]> headers = {}, boolean highlight = false, string query = "", int count = 0, int page = 0, string sort = "", string sortDir = "", anydata Additional Values, SearchMessagesQueries queries) returns DefaultSuccessResponse64|error;
+    resource function get search\.messages(map<string|string[]> headers = {}, boolean highlight = false, string query = "", int count = 0, int page = 0, string sort = "", string sortDir = "", SearchMessagesQueries queries) returns DefaultSuccessResponse64|error;
 
     # Adds a star to an item.
     # 
@@ -4909,7 +5622,7 @@
 
     # Lists stars for a user.
     # 
-    resource function get stars\.list(map<string|string[]> headers = {}, string cursor = "", string count = "", int limit = 0, string page = "", anydata Additional Values, StarsListQueries queries) returns StarsListResponse|error;
+    resource function get stars\.list(map<string|string[]> headers = {}, string cursor = "", string count = "", int limit = 0, string page = "", StarsListQueries queries) returns StarsListResponse|error;
 
     # Removes a star from an item.
     # 
@@ -4917,23 +5630,23 @@
 
     # Gets the access logs for the current team.
     # 
-    resource function get team\.accessLogs(map<string|string[]> headers = {}, string before = "", string count = "", string page = "", anydata Additional Values, TeamAccessLogsQueries queries) returns TeamAccessLogsResponse|error;
+    resource function get team\.accessLogs(map<string|string[]> headers = {}, string before = "", string count = "", string page = "", TeamAccessLogsQueries queries) returns TeamAccessLogsResponse|error;
 
     # Gets billable users information for the current team.
     # 
-    resource function get team\.billableInfo(map<string|string[]> headers = {}, string user = "", anydata Additional Values, TeamBillableInfoQueries queries) returns DefaultSuccessResponse65|error;
+    resource function get team\.billableInfo(map<string|string[]> headers = {}, string user = "", TeamBillableInfoQueries queries) returns DefaultSuccessResponse65|error;
 
     # Gets information about the current team.
     # 
-    resource function get team\.info(map<string|string[]> headers = {}, string team = "", anydata Additional Values, TeamInfoQueries queries) returns TeamInfoResponse|error;
+    resource function get team\.info(map<string|string[]> headers = {}, string team = "", TeamInfoQueries queries) returns TeamInfoResponse|error;
 
     # Gets the integration logs for the current team.
     # 
-    resource function get team\.integrationLogs(map<string|string[]> headers = {}, string serviceId = "", string count = "", string changeType = "", string page = "", string appId = "", string user = "", anydata Additional Values, TeamIntegrationLogsQueries queries) returns TeamIntegrationLogsResponse|error;
+    resource function get team\.integrationLogs(map<string|string[]> headers = {}, string serviceId = "", string count = "", string changeType = "", string page = "", string appId = "", string user = "", TeamIntegrationLogsQueries queries) returns TeamIntegrationLogsResponse|error;
 
     # Retrieve a team's profile.
     # 
-    resource function get team\.profile\.get(map<string|string[]> headers = {}, string visibility = "", anydata Additional Values, TeamProfileGetQueries queries) returns TeamProfileGetResponse|error;
+    resource function get team\.profile\.get(map<string|string[]> headers = {}, string visibility = "", TeamProfileGetQueries queries) returns TeamProfileGetResponse|error;
 
     # Create a User Group
     # 
@@ -4949,7 +5662,7 @@
 
     # List all User Groups for a team
     # 
-    resource function get usergroups\.list(map<string|string[]> headers = {}, boolean includeDisabled = false, boolean includeUsers = false, boolean includeCount = false, anydata Additional Values, UsergroupsListQueries queries) returns UsergroupsListResponse|error;
+    resource function get usergroups\.list(map<string|string[]> headers = {}, boolean includeDisabled = false, boolean includeUsers = false, boolean includeCount = false, UsergroupsListQueries queries) returns UsergroupsListResponse|error;
 
     # Update an existing User Group
     # 
@@ -4957,7 +5670,7 @@
 
     # List all users in a User Group
     # 
-    resource function get usergroups\.users\.list(map<string|string[]> headers = {}, boolean includeDisabled = false, string usergroup = "", anydata Additional Values, UsergroupsUsersListQueries queries) returns UsergroupsUsersListResponse|error;
+    resource function get usergroups\.users\.list(map<string|string[]> headers = {}, boolean includeDisabled = false, string usergroup = "", UsergroupsUsersListQueries queries) returns UsergroupsUsersListResponse|error;
 
     # Update the list of users for a User Group
     # 
@@ -4965,7 +5678,7 @@
 
     # List conversations the calling user may access.
     # 
-    resource function get users\.conversations(map<string|string[]> headers = {}, string cursor = "", string types = "", int limit = 0, string user = "", boolean excludeArchived = false, anydata Additional Values, UsersConversationsQueries queries) returns UsersConversationsResponse|error;
+    resource function get users\.conversations(map<string|string[]> headers = {}, string cursor = "", string types = "", int limit = 0, string user = "", boolean excludeArchived = false, UsersConversationsQueries queries) returns UsersConversationsResponse|error;
 
     # Delete the user profile photo
     # 
@@ -4973,7 +5686,7 @@
 
     # Gets user presence information.
     # 
-    resource function get users\.getPresence(map<string|string[]> headers = {}, string user = "", anydata Additional Values, UsersGetPresenceQueries queries) returns APIMethodUsersGetPresence|error;
+    resource function get users\.getPresence(map<string|string[]> headers = {}, string user = "", UsersGetPresenceQueries queries) returns APIMethodUsersGetPresence|error;
 
     # Get a user's identity.
     # 
@@ -4981,19 +5694,19 @@
 
     # Gets information about a user.
     # 
-    resource function get users\.info(map<string|string[]> headers = {}, boolean includeLocale = false, string user = "", anydata Additional Values, UsersInfoQueries queries) returns UsersInfoResponse|error;
+    resource function get users\.info(map<string|string[]> headers = {}, boolean includeLocale = false, string user = "", UsersInfoQueries queries) returns UsersInfoResponse|error;
 
     # Lists all users in a Slack team.
     # 
-    resource function get users\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, boolean includeLocale = false, anydata Additional Values, UsersListQueries queries) returns UsersListResponse|error;
+    resource function get users\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, boolean includeLocale = false, UsersListQueries queries) returns UsersListResponse|error;
 
     # Find a user with an email address.
     # 
-    resource function get users\.lookupByEmail(map<string|string[]> headers = {}, string email = "", anydata Additional Values, UsersLookupByEmailQueries queries) returns UsersLookupByEmailResponse|error;
+    resource function get users\.lookupByEmail(map<string|string[]> headers = {}, string email = "", UsersLookupByEmailQueries queries) returns UsersLookupByEmailResponse|error;
 
     # Retrieves a user's profile information.
     # 
-    resource function get users\.profile\.get(map<string|string[]> headers = {}, boolean includeLabels = false, string user = "", anydata Additional Values, UsersProfileGetQueries queries) returns UsersProfileGetResponse|error;
+    resource function get users\.profile\.get(map<string|string[]> headers = {}, boolean includeLabels = false, string user = "", UsersProfileGetQueries queries) returns UsersProfileGetResponse|error;
 
     # Set the profile information for a user.
     # 
@@ -5013,29 +5726,29 @@
 
     # Open a view for a user.
     # 
-    resource function get views\.open(map<string|string[]> headers = {}, string view = "", string triggerId = "", anydata Additional Values, ViewsOpenQueries queries) returns DefaultSuccessResponse66|error;
+    resource function get views\.open(map<string|string[]> headers = {}, string view = "", string triggerId = "", ViewsOpenQueries queries) returns DefaultSuccessResponse66|error;
 
     # Publish a static view for a User.
     # 
-    resource function get views\.publish(map<string|string[]> headers = {}, string view = "", string userId = "", string hash = "", anydata Additional Values, ViewsPublishQueries queries) returns DefaultSuccessResponse67|error;
+    resource function get views\.publish(map<string|string[]> headers = {}, string view = "", string userId = "", string hash = "", ViewsPublishQueries queries) returns DefaultSuccessResponse67|error;
 
     # Push a view onto the stack of a root view.
     # 
-    resource function get views\.push(map<string|string[]> headers = {}, string view = "", string triggerId = "", anydata Additional Values, ViewsPushQueries queries) returns DefaultSuccessResponse68|error;
+    resource function get views\.push(map<string|string[]> headers = {}, string view = "", string triggerId = "", ViewsPushQueries queries) returns DefaultSuccessResponse68|error;
 
     # Update an existing view.
     # 
-    resource function get views\.update(map<string|string[]> headers = {}, string view = "", string viewId = "", string externalId = "", string hash = "", anydata Additional Values, ViewsUpdateQueries queries) returns DefaultSuccessResponse69|error;
+    resource function get views\.update(map<string|string[]> headers = {}, string view = "", string viewId = "", string externalId = "", string hash = "", ViewsUpdateQueries queries) returns DefaultSuccessResponse69|error;
 
     # Indicate that an app's step in a workflow completed execution.
     # 
-    resource function get workflows\.stepCompleted(map<string|string[]> headers = {}, string outputs = "", string workflowStepExecuteId = "", anydata Additional Values, WorkflowsStepCompletedQueries queries) returns DefaultSuccessResponse70|error;
+    resource function get workflows\.stepCompleted(map<string|string[]> headers = {}, string outputs = "", string workflowStepExecuteId = "", WorkflowsStepCompletedQueries queries) returns DefaultSuccessResponse70|error;
 
     # Indicate that an app's step in a workflow failed to execute.
     # 
-    resource function get workflows\.stepFailed(map<string|string[]> headers = {}, string workflowStepExecuteId = "", string error = "", anydata Additional Values, WorkflowsStepFailedQueries queries) returns DefaultSuccessResponse71|error;
+    resource function get workflows\.stepFailed(map<string|string[]> headers = {}, string workflowStepExecuteId = "", string error = "", WorkflowsStepFailedQueries queries) returns DefaultSuccessResponse71|error;
 
     # Update the configuration for a workflow extension step.
     # 
-    resource function get workflows\.updateStep(map<string|string[]> headers = {}, string outputs = "", string inputs = "", string stepName = "", string stepImageUrl = "", string workflowStepEditId = "", anydata Additional Values, WorkflowsUpdateStepQueries queries) returns DefaultSuccessResponse72|error;
+    resource function get workflows\.updateStep(map<string|string[]> headers = {}, string outputs = "", string inputs = "", string stepName = "", string stepImageUrl = "", string workflowStepEditId = "", WorkflowsUpdateStepQueries queries) returns DefaultSuccessResponse72|error;
 }
`````
