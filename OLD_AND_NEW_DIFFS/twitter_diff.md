# twitter — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `twitter` |
| **Old file** | `twitter/old/ballerinax_twitter.bal.txt` |
| **New file** | `twitter/new/ballerinax_twitter.bal.txt` |
| **Old lines** | 4045 |
| **New lines** | 4965 |
| **Lines added** | 1139 |
| **Lines removed** | 219 |
| **Hunks** | 171 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 54 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 114 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (54)

- `type Aggregate`
- `type AllProjectClientApps`
- `type ClientAppId`
- `type ComplianceJobName`
- `type CountryCode`
- `type CreatedAt`
- `type DmAttachments`
- `type DmConversationId`
- `type DmEventId`
- `type DmParticipants`
- `type DownloadExpiration`
- `type DownloadUrl`
- `type End`
- `type FindSpacesByIdsQueriesIdsItemsString`
- `type FindUsersByUsernameQueriesUsernamesItemsString`
- `type GeoBboxItemsNumber`
- `type HttpStatusCode`
- `type JobId`
- `type LikeId`
- `type ListId`
- `type MediaHeight`
- `type MediaId`
- `type MediaKey`
- `type MediaWidth`
- `type NewestId`
- `type NextToken`
- `type NoteTweetText`
- `type OldestId`
- `type PaginationToken32`
- `type PaginationToken36`
- `type PaginationTokenLong`
- `type PlaceId`
- `type PollId`
- `type PollOptionLabel`
- `type Position`
- `type PreviousToken`
- `type ResultCount`
- `type RuleId`
- `type RuleTag`
- `type RuleValue`
- `type SpaceId`
- `type Start`
- `type TopicId`
- `type TweetCount`
- `type TweetCreateRequestPollOptionsItemsString`
- `type TweetId`
- `type TweetText`
- `type UploadExpiration`
- `type UploadUrl`
- `type Url`
- `type UserId`
- `type UserIdMatchesAuthenticatedUser`
- `type UserName`
- `type UserSearchQuery`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 196–264 | 196–293 | Types | +39 | −10 |
| 2 | 270–292 | 299–330 | Types | +11 | −2 |
| 3 | 301–323 | 339–370 | Types | +11 | −2 |
| 4 | 326–352 | 373–410 | Types | +13 | −2 |
| 5 | 355–360 | 413–419 | Types | +1 | −0 |
| 6 | 369–393 | 428–460 | Types | +9 | −1 |
| 7 | 413–418 | 480–486 | Types | +1 | −0 |
| 8 | 424–463 | 492–542 | Types | +11 | −0 |
| 9 | 470–475 | 549–555 | Types | +1 | −0 |
| 10 | 479–492 | 559–577 | Types | +5 | −0 |
| 11 | 496–505 | 581–593 | Types | +4 | −1 |
| 12 | 511–520 | 599–613 | Types | +5 | −0 |
| 13 | 522–529 | 615–624 | Types | +2 | −0 |
| 14 | 535–541 | 630–636 | Types | +1 | −1 |
| 15 | 544–558 | 639–658 | Types | +5 | −0 |
| 16 | 571–588 | 671–695 | Types | +12 | −5 |
| 17 | 604–610 | 711–717 | Types | +1 | −1 |
| 18 | 618–628 | 725–737 | Types | +4 | −2 |
| 19 | 632–639 | 741–750 | Types | +2 | −0 |
| 20 | 641–648 | 752–761 | Types | +2 | −0 |
| 21 | 651–695 | 764–822 | Types | +16 | −2 |
| 22 | 699–704 | 826–832 | Types | +1 | −0 |
| 23 | 706–712 | 834–841 | Types | +2 | −1 |
| 24 | 716–724 | 845–856 | Types | +5 | −2 |
| 25 | 733–746 | 865–883 | Types | +7 | −2 |
| 26 | 757–771 | 894–913 | Types | +7 | −2 |
| 27 | 776–792 | 918–939 | Types | +5 | −0 |
| 28 | 794–813 | 941–970 | Types | +10 | −0 |
| 29 | 817–826 | 974–986 | Types | +3 | −0 |
| 30 | 832–847 | 992–1011 | Types | +4 | −0 |
| 31 | 850–859 | 1014–1025 | Types | +3 | −1 |
| 32 | 869–892 | 1035–1065 | Types | +10 | −3 |
| 33 | 899–923 | 1072–1105 | Types | +14 | −5 |
| 34 | 931–942 | 1113–1128 | Types | +4 | −0 |
| 35 | 953–977 | 1139–1172 | Types | +10 | −1 |
| 36 | 979–984 | 1174–1180 | Types | +1 | −0 |
| 37 | 986–1003 | 1182–1204 | Types | +5 | −0 |
| 38 | 1010–1030 | 1211–1239 | Types | +9 | −1 |
| 39 | 1032–1053 | 1241–1268 | Types | +6 | −0 |
| 40 | 1061–1077 | 1276–1302 | Types | +10 | −0 |
| 41 | 1087–1093 | 1312–1318 | Types | +1 | −1 |
| 42 | 1100–1131 | 1325–1370 | Types | +18 | −4 |
| 43 | 1137–1145 | 1376–1387 | Types | +5 | −2 |
| 44 | 1148–1172 | 1390–1422 | Types | +11 | −3 |
| 45 | 1177–1188 | 1427–1440 | Types | +2 | −0 |
| 46 | 1195–1224 | 1447–1485 | Types | +9 | −0 |
| 47 | 1226–1250 | 1487–1518 | Types | +7 | −0 |
| 48 | 1252–1272 | 1520–1547 | Types | +7 | −0 |
| 49 | 1274–1297 | 1549–1582 | Types | +12 | −2 |
| 50 | 1304–1361 | 1589–1659 | Types | +13 | −0 |
| 51 | 1366–1389 | 1664–1690 | Types | +8 | −5 |
| 52 | 1391–1406 | 1692–1713 | Types | +7 | −1 |
| 53 | 1409–1415 | 1716–1724 | Types | +3 | −1 |
| 54 | 1418–1426 | 1727–1738 | Types | +3 | −0 |
| 55 | 1429–1442 | 1741–1757 | Types | +4 | −1 |
| 56 | 1447–1460 | 1762–1778 | Types | +3 | −0 |
| 57 | 1462–1476 | 1780–1800 | Types | +8 | −2 |
| 58 | 1478–1526 | 1802–1867 | Types | +21 | −4 |
| 59 | 1528–1578 | 1869–1934 | Types | +22 | −7 |
| 60 | 1591–1597 | 1947–1954 | Types | +2 | −1 |
| 61 | 1609–1615 | 1966–1972 | Types | +1 | −1 |
| 62 | 1636–1641 | 1993–1999 | Types | +1 | −0 |
| 63 | 1647–1652 | 2005–2011 | Types | +1 | −0 |
| 64 | 1675–1702 | 2034–2071 | Types | +12 | −2 |
| 65 | 1707–1712 | 2076–2082 | Types | +1 | −0 |
| 66 | 1714–1723 | 2084–2096 | Types | +4 | −1 |
| 67 | 1727–1737 | 2100–2111 | Types | +2 | −1 |
| 68 | 1739–1746 | 2113–2122 | Types | +3 | −1 |
| 69 | 1748–1759 | 2124–2139 | Types | +4 | −0 |
| 70 | 1762–1781 | 2142–2165 | Types | +5 | −1 |
| 71 | 1783–1832 | 2167–2234 | Types | +20 | −2 |
| 72 | 1836–1848 | 2238–2255 | Types | +9 | −4 |
| 73 | 1850–1862 | 2257–2273 | Types | +4 | −0 |
| 74 | 1871–1892 | 2282–2312 | Types | +10 | −1 |
| 75 | 1897–1906 | 2317–2329 | Types | +3 | −0 |
| 76 | 1914–1947 | 2337–2383 | Types | +14 | −1 |
| 77 | 1949–1968 | 2385–2412 | Types | +9 | −1 |
| 78 | 1970–1987 | 2414–2438 | Types | +7 | −0 |
| 79 | 1989–2004 | 2440–2458 | Types | +4 | −1 |
| 80 | 2006–2019 | 2460–2478 | Types | +6 | −1 |
| 81 | 2022–2027 | 2481–2487 | Types | +1 | −0 |
| 82 | 2029–2040 | 2489–2504 | Types | +6 | −2 |
| 83 | 2042–2056 | 2506–2526 | Types | +9 | −3 |
| 84 | 2058–2076 | 2528–2552 | Types | +7 | −1 |
| 85 | 2078–2087 | 2554–2566 | Types | +3 | −0 |
| 86 | 2092–2118 | 2571–2603 | Types | +7 | −1 |
| 87 | 2130–2135 | 2615–2621 | Types | +1 | −0 |
| 88 | 2137–2181 | 2623–2683 | Types | +16 | −0 |
| 89 | 2183–2196 | 2685–2703 | Types | +6 | −1 |
| 90 | 2198–2207 | 2705–2717 | Types | +3 | −0 |
| 91 | 2209–2216 | 2719–2728 | Types | +3 | −1 |
| 92 | 2218–2243 | 2730–2764 | Types | +10 | −1 |
| 93 | 2245–2255 | 2766–2778 | Types | +2 | −0 |
| 94 | 2257–2293 | 2780–2828 | Types | +13 | −1 |
| 95 | 2306–2313 | 2841–2850 | Types | +2 | −0 |
| 96 | 2316–2321 | 2853–2859 | Types | +1 | −0 |
| 97 | 2323–2356 | 2861–2909 | Types | +16 | −1 |
| 98 | 2373–2403 | 2926–2961 | Types | +6 | −1 |
| 99 | 2405–2440 | 2963–3012 | Types | +15 | −1 |
| 100 | 2446–2483 | 3018–3067 | Types | +12 | −0 |
| 101 | 2485–2504 | 3069–3094 | Types | +6 | −0 |
| 102 | 2506–2525 | 3096–3123 | Types | +9 | −1 |
| 103 | 2527–2557 | 3125–3168 | Types | +15 | −2 |
| 104 | 2559–2591 | 3170–3209 | Types | +7 | −0 |
| 105 | 2593–2627 | 3211–3255 | Types | +12 | −2 |
| 106 | 2667–2699 | 3295–3336 | Types | +10 | −1 |
| 107 | 2701–2706 | 3338–3344 | Types | +1 | −0 |
| 108 | 2712–2717 | 3350–3356 | Types | +1 | −0 |
| 109 | 2729–2746 | 3368–3389 | Types | +4 | −0 |
| 110 | 2748–2787 | 3391–3446 | Types | +17 | −1 |
| 111 | 2789–2815 | 3448–3485 | Types | +12 | −1 |
| 112 | 2817–2822 | 3487–3493 | Types | +1 | −0 |
| 113 | 2824–2841 | 3495–3518 | Types | +9 | −3 |
| 114 | 2846–2879 | 3523–3569 | Types | +14 | −1 |
| 115 | 2881–2903 | 3571–3601 | Types | +9 | −1 |
| 116 | 2905–2931 | 3603–3637 | Types | +8 | −0 |
| 117 | 2938–2958 | 3644–3671 | Types | +8 | −1 |
| 118 | 2960–2975 | 3673–3694 | Types | +6 | −0 |
| 119 | 2977–3000 | 3696–3729 | Types | +12 | −2 |
| 120 | 3002–3027 | 3731–3763 | Types | +8 | −1 |
| 121 | 3029–3046 | 3765–3789 | Types | +8 | −1 |
| 122 | 3048–3053 | 3791–3797 | Types | +1 | −0 |
| 123 | 3055–3060 | 3799–3805 | Types | +1 | −0 |
| 124 | 3063–3080 | 3808–3830 | Types | +6 | −1 |
| 125 | 3083–3126 | 3833–3889 | Types | +15 | −2 |
| 126 | 3128–3149 | 3891–3921 | Types | +10 | −1 |
| 127 | 3151–3164 | 3923–3941 | Types | +6 | −1 |
| 128 | 3166–3177 | 3943–3958 | Types | +6 | −2 |
| 129 | 3180–3185 | 3961–3967 | Types | +1 | −0 |
| 130 | 3187–3208 | 3969–3997 | Types | +8 | −1 |
| 131 | 3211–3222 | 4000–4013 | Types | +2 | −0 |
| 132 | 3227–3232 | 4018–4024 | Types | +1 | −0 |
| 133 | 3234–3259 | 4026–4060 | Types | +11 | −2 |
| 134 | 3261–3274 | 4062–4080 | Types | +6 | −1 |
| 135 | 3276–3291 | 4082–4101 | Types | +4 | −0 |
| 136 | 3293–3306 | 4103–4121 | Types | +6 | −1 |
| 137 | 3308–3317 | 4123–4135 | Types | +4 | −1 |
| 138 | 3322–3332 | 4140–4154 | Types | +4 | −0 |
| 139 | 3337–3372 | 4159–4202 | Types | +8 | −0 |
| 140 | 3374–3391 | 4204–4228 | Types | +8 | −1 |
| 141 | 3393–3414 | 4230–4258 | Types | +8 | −1 |
| 142 | 3416–3421 | 4260–4266 | Types | +1 | −0 |
| 143 | 3423–3455 | 4268–4312 | Types | +14 | −2 |
| 144 | 3457–3498 | 4314–4366 | Types | +11 | −0 |
| 145 | 3500–3519 | 4368–4393 | Types | +6 | −0 |
| 146 | 3522–3527 | 4396–4402 | Types | +1 | −0 |
| 147 | 3529–3538 | 4404–4416 | Types | +4 | −1 |
| 148 | 3544–3550 | 4422–4428 | Types | +1 | −1 |
| 149 | 3552–3566 | 4430–4448 | Types | +4 | −0 |
| 150 | 3568–3589 | 4450–4478 | Types | +8 | −1 |
| 151 | 3591–3614 | 4480–4513 | Types | +12 | −2 |
| 152 | 3616–3640 | 4515–4548 | Types | +10 | −1 |
| 153 | 3642–3671 | 4550–4591 | Types | +13 | −1 |
| 154 | 3677–3683 | 4597–4603 | Client | +1 | −1 |
| 155 | 3685–3691 | 4605–4611 | Client | +1 | −1 |
| 156 | 3693–3699 | 4613–4619 | Client | +1 | −1 |
| 157 | 3705–3719 | 4625–4639 | Client | +3 | −3 |
| 158 | 3721–3735 | 4641–4655 | Client | +3 | −3 |
| 159 | 3737–3743 | 4657–4663 | Client | +1 | −1 |
| 160 | 3749–3759 | 4669–4679 | Client | +2 | −2 |
| 161 | 3765–3771 | 4685–4691 | Client | +1 | −1 |
| 162 | 3773–3807 | 4693–4727 | Client | +8 | −8 |
| 163 | 3809–3883 | 4729–4803 | Client | +18 | −18 |
| 164 | 3885–3903 | 4805–4823 | Client | +4 | −4 |
| 165 | 3905–3947 | 4825–4867 | Client | +10 | −10 |
| 166 | 3953–3959 | 4873–4879 | Client | +1 | −1 |
| 167 | 3965–3975 | 4885–4895 | Client | +2 | −2 |
| 168 | 3977–3983 | 4897–4903 | Client | +1 | −1 |
| 169 | 3989–4003 | 4909–4923 | Client | +3 | −3 |
| 170 | 4005–4015 | 4925–4935 | Client | +2 | −2 |
| 171 | 4029–4039 | 4949–4959 | Client | +2 | −2 |

---

## Unified diff

`````diff
--- twitter/old/ballerinax_twitter.bal.txt	2026-08-12 12:57:30
+++ twitter/new/ballerinax_twitter.bal.txt	2026-08-12 13:19:20
@@ -196,69 +196,98 @@
 
 
 type Get2TweetsCountsAllResponseMeta record {
+    @jsondata:Name {value: "total_tweet_count"}
     Aggregate totalTweetCount?;
+    @jsondata:Name {value: "oldest_id"}
     OldestId oldestId?;
+    @jsondata:Name {value: "newest_id"}
     NewestId newestId?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
 };
 
-// Unknown type: Aggregate
+# The sum of results returned in this response
+type Aggregate int:Signed32;
 
-// Unknown type: OldestId
+# The oldest id in this response
+type OldestId string;
 
-// Unknown type: NewestId
+# The newest id in this response
+type NewestId string;
 
-// Unknown type: NextToken
+# The next token
+@constraint:String {minLength: 1}
+type NextToken string;
 
 
 type ListPinnedRequest record {
+    @jsondata:Name {value: "list_id"}
     ListId listId;
 };
 
-// Unknown type: ListId
+# The unique identifier of this List
+@constraint:String {pattern: re `^[0-9]{1,19}$`}
+type ListId string;
 
 
 type UnlikeComplianceSchema record {
     # Event time
+    @jsondata:Name {value: "event_at"}
     string eventAt;
     UnlikeComplianceSchemaFavorite favorite;
 };
 
 
 type UnlikeComplianceSchemaFavorite record {
+    @jsondata:Name {value: "user_id"}
     UserId userId;
     # Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers
     TweetId id;
 };
 
-// Unknown type: UserId
+# Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers
+@constraint:String {pattern: re `^[0-9]{1,19}$`}
+type UserId string;
 
-// Unknown type: TweetId
+# Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers
+@constraint:String {pattern: re `^[0-9]{1,19}$`}
+type TweetId string;
 
 # Represents the Queries record for the operation: listGetFollowers
 
 type ListGetFollowersQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get a specified 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationTokenLong paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
-// Unknown type: PaginationTokenLong
+# A 'long' pagination token
+@constraint:String {maxLength: 19, minLength: 1}
+type PaginationTokenLong string;
 
-// Unknown type: HttpStatusCode
+# HTTP Status Code
+@constraint:Int {minValue: 100, maxValue: 599}
+type HttpStatusCode int;
 
 
 type UserScrubGeoObjectSchema record {
     # Event time
+    @jsondata:Name {value: "event_at"}
     string eventAt;
     UserScrubGeoObjectSchemaUser user;
+    @jsondata:Name {value: "up_to_tweet_id"}
     TweetId upToTweetId;
 };
 
@@ -270,23 +299,32 @@
 
 
 type Get2UsersIdLikedTweetsResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
-// Unknown type: PreviousToken
+# The previous token
+@constraint:String {minLength: 1}
+type PreviousToken string;
 
-// Unknown type: ResultCount
+# The number of results returned in this response
+type ResultCount int:Signed32;
 
 # Represents the Queries record for the operation: findUserByUsername
 
 type FindUserByUsernameQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
@@ -301,23 +339,32 @@
     "tweets"|"users" 'type;
 };
 
-// Unknown type: ComplianceJobName
+# User-provided name for a compliance job
+@constraint:String {maxLength: 64}
+type ComplianceJobName string;
 
 # Media information being attached to created Tweet. This is mutually exclusive from Quote Tweet Id, Poll, and Card URI
 
 type TweetCreateRequestMedia record {
     # A list of Media Ids to be attached to a created Tweet
+    @jsondata:Name {value: "media_ids"}
     MediaId[] mediaIds;
     # A list of User Ids to be tagged in the media for created Tweet
+    @jsondata:Name {value: "tagged_user_ids"}
     UserId[] taggedUserIds?;
 };
 
-// Unknown type: MediaId
+# The unique identifier of this Media
+@constraint:String {pattern: re `^[0-9]{1,19}$`}
+type MediaId string;
 
 
 type Get2UsersIdOwnedListsResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -326,27 +373,38 @@
     # The topics of a Space, as selected by its creator
     SpaceTopics[] topics?;
     # A date time stamp for when a Space is scheduled to begin
+    @jsondata:Name {value: "scheduled_start"}
     string scheduledStart?;
     # Creation time of the Space
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     # Denotes if the Space is a ticketed Space
+    @jsondata:Name {value: "is_ticketed"}
     boolean isTicketed?;
     # The title of the Space
     string title?;
     # An array of user ids for people who were invited to a Space
+    @jsondata:Name {value: "invited_user_ids"}
     UserId[] invitedUserIds?;
     # An array of user ids for people who were speakers in a Space
+    @jsondata:Name {value: "speaker_ids"}
     UserId[] speakerIds?;
     # The number of participants in a Space
-    ballerina/lang.int:0.0.0:Signed32 participantCount?;
+    @jsondata:Name {value: "participant_count"}
+    int:Signed32 participantCount?;
     # When the Space was last updated
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     # The number of people who have either purchased a ticket or set a reminder for this Space
-    ballerina/lang.int:0.0.0:Signed32 subscriberCount?;
+    @jsondata:Name {value: "subscriber_count"}
+    int:Signed32 subscriberCount?;
+    @jsondata:Name {value: "creator_id"}
     UserId creatorId?;
     # When the Space was started as a date string
+    @jsondata:Name {value: "started_at"}
     string startedAt?;
     # The user ids for the hosts of the Space
+    @jsondata:Name {value: "host_ids"}
     UserId[] hostIds?;
     # The unique identifier of this Space
     SpaceId id;
@@ -355,6 +413,7 @@
     # The language of the Space
     string lang?;
     # End time of the Space
+    @jsondata:Name {value: "ended_at"}
     string endedAt?;
 };
 
@@ -369,25 +428,33 @@
     string id;
 };
 
-// Unknown type: SpaceId
+# The unique identifier of this Space
+@constraint:String {pattern: re `^[a-zA-Z0-9]{1,13}$`}
+type SpaceId string;
 
 # Represents the Queries record for the operation: getDmEventsById
 
 type GetDmEventsByIdQueries record {
     # A comma separated list of DmEvent fields to display
+    @http:Query {name: "dm_event.fields"}
     ("attachments"|"created_at"|"dm_conversation_id"|"entities"|"event_type"|"id"|"participant_ids"|"referenced_tweets"|"sender_id"|"text")[] dmEventFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"participant_ids"|"referenced_tweets.id"|"sender_id")[] expansions?;
 };
 
 
 type UsersRetweetsCreateRequest record {
+    @jsondata:Name {value: "tweet_id"}
     TweetId tweetId;
 };
 
@@ -413,6 +480,7 @@
     # Description of the context annotation domain
     string description?;
     # The unique id for a context annotation domain
+    @constraint:String {pattern: re `^[0-9]{1,19}$`}
     string id;
 };
 
@@ -424,40 +492,51 @@
     # Description of the context annotation entity
     string description?;
     # The unique id for a context annotation entity
+    @constraint:String {pattern: re `^[0-9]{1,19}$`}
     string id;
 };
 
 
 type Get2ListsIdMembersResponse record {
+    @constraint:Array {minLength: 1}
     User[] data?;
     Get2ListsIdMembersResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 # The X User object
 
 type User record {
+    @jsondata:Name {value: "pinned_tweet_id"}
     TweetId pinnedTweetId?;
     # Returns detailed information about the relationship between two users
+    @jsondata:Name {value: "connection_status"}
     ("follow_request_received"|"follow_request_sent"|"blocking"|"followed_by"|"following"|"muting")[] connectionStatus?;
+    @jsondata:Name {value: "public_metrics"}
     UserPublicMetrics publicMetrics?;
     # Indicate if this User is a verified X User
     boolean verified?;
     # Creation time of this User
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     # The text of this User's profile description (also known as bio), if the User provided one
     string description?;
     # The URL to the profile image for this User
+    @jsondata:Name {value: "profile_image_url"}
     string profileImageUrl?;
     # Indicates if you can send a DM to this User
+    @jsondata:Name {value: "receives_your_dm"}
     boolean receivesYourDm?;
     # The X Blue verified type of the user, eg: blue, government, business or none
+    @jsondata:Name {value: "verified_type"}
     "blue"|"government"|"business"|"none" verifiedType?;
     # Indicates withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country)
     UserWithheld withheld?;
     # The URL specified in the User's profile
     string url?;
+    @jsondata:Name {value: "most_recent_tweet_id"}
     TweetId mostRecentTweetId?;
     # Indicates if this User has chosen to protect their Posts (in other words, if this User's Posts are private)
     boolean protected?;
@@ -470,6 +549,7 @@
     # Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers
     UserId id;
     # The X Blue subscription type of the user, eg: Basic, Premium, PremiumPlus or None
+    @jsondata:Name {value: "subscription_type"}
     "Basic"|"Premium"|"PremiumPlus"|"None" subscriptionType?;
     # The X handle (screen name) of this user
     UserName username;
@@ -479,14 +559,19 @@
 
 type UserPublicMetrics record {
     # The number of Posts (including Retweets) posted by this User
+    @jsondata:Name {value: "tweet_count"}
     int tweetCount;
     # The number of likes created by this User
+    @jsondata:Name {value: "like_count"}
     int likeCount?;
     # Number of Users this User is following
+    @jsondata:Name {value: "following_count"}
     int followingCount;
     # The number of lists that include this User
+    @jsondata:Name {value: "listed_count"}
     int listedCount;
     # Number of Users who are following this User
+    @jsondata:Name {value: "followers_count"}
     int followersCount;
 };
 
@@ -496,10 +581,13 @@
     # Indicates that the content being withheld is a `user`
     "user" scope?;
     # Provides a list of countries where this content is not available
+    @jsondata:Name {value: "country_codes"}
     CountryCode[] countryCodes;
 };
 
-// Unknown type: CountryCode
+# A two-letter ISO 3166-1 alpha-2 country code
+@constraint:String {pattern: re `^[A-Z]{2}$`}
+type CountryCode string;
 
 # A list of metadata found in the User's profile description
 
@@ -511,10 +599,15 @@
 
 
 type FullTextEntities record {
+    @constraint:Array {minLength: 1}
     CashtagEntity[] cashtags?;
+    @constraint:Array {minLength: 1}
     UrlEntity[] urls?;
+    @constraint:Array {minLength: 1}
     HashtagEntity[] hashtags?;
+    @constraint:Array {minLength: 1}
     MentionEntity[] mentions?;
+    @constraint:Array {minLength: 1}
     FullTextEntitiesAnnotations[] annotations?;
 };
 
@@ -522,8 +615,10 @@
 
 type EntityIndicesInclusiveExclusive record {
     # Index (zero-based) at which position this entity starts.  The index is inclusive
+    @constraint:Int {minValue: 0}
     int 'start;
     # Index (zero-based) at which position this entity ends.  The index is exclusive
+    @constraint:Int {minValue: 0}
     int end;
 };
 
@@ -535,7 +630,7 @@
 
 
 type CashtagEntity record {
-    int start;
+    int 'start;
     int end;
     string tag;
 };
@@ -544,15 +639,20 @@
 
 type UrlFields record {
     # The URL as displayed in the X client
+    @jsondata:Name {value: "display_url"}
     string displayUrl?;
+    @constraint:Array {minLength: 1}
     UrlImage[] images?;
+    @jsondata:Name {value: "expanded_url"}
     Url expandedUrl?;
     # Fully resolved url
+    @jsondata:Name {value: "unwound_url"}
     string unwoundUrl?;
     # Description of the URL landing page
     string description?;
     # Title of the page the URL points to
     string title?;
+    @jsondata:Name {value: "media_key"}
     MediaKey mediaKey?;
     # A validly formatted URL
     Url url;
@@ -571,18 +671,25 @@
     MediaHeight height?;
 };
 
-// Unknown type: MediaWidth
+# The width of the media in pixels
+@constraint:Int {minValue: 0}
+type MediaWidth int;
 
-// Unknown type: Url
+# A validly formatted URL
+type Url string;
 
-// Unknown type: MediaHeight
+# The height of the media in pixels
+@constraint:Int {minValue: 0}
+type MediaHeight int;
 
-// Unknown type: MediaKey
+# The Media Key identifier for this attachment
+@constraint:String {pattern: re `^([0-9]+)_([0-9]+)$`}
+type MediaKey string;
 
 # Represent the portion of text recognized as a URL, and its start and end position within the text
 
 type UrlEntity record {
-    int start;
+    int 'start;
     int end;
     string displayUrl?;
     UrlImage[] images?;
@@ -604,7 +711,7 @@
 
 
 type HashtagEntity record {
-    int start;
+    int 'start;
     int end;
     string tag;
 };
@@ -618,11 +725,13 @@
     UserName username;
 };
 
-// Unknown type: UserName
+# The X handle (screen name) of this user
+@constraint:String {pattern: re `^[A-Za-z0-9_]{1,15}$`}
+type UserName string;
 
 
 type MentionEntity record {
-    int start;
+    int 'start;
     int end;
     UserId id?;
     UserName username;
@@ -632,8 +741,10 @@
 
 type EntityIndicesInclusiveInclusive record {
     # Index (zero-based) at which position this entity starts.  The index is inclusive
+    @constraint:Int {minValue: 0}
     int 'start;
     # Index (zero-based) at which position this entity ends.  The index is inclusive
+    @constraint:Int {minValue: 0}
     int end;
 };
 
@@ -641,8 +752,10 @@
 
 type AnnotationsAllOf2 record {
     # Confidence factor for annotation type
+    @constraint:Number {minValue: 0, maxValue: 1}
     decimal probability?;
     # Text used to determine annotation
+    @jsondata:Name {value: "normalized_text"}
     string normalizedText?;
     # Annotation type
     string 'type?;
@@ -651,45 +764,59 @@
 # Annotation for entities based on the Tweet text
 
 type FullTextEntitiesAnnotations record {
-    int start;
+    int 'start;
     int end;
     decimal probability?;
     string normalizedText?;
-    string type?;
+    string 'type?;
 };
 
 # Expanded details for the URL specified in the User's profile, with start and end indices
 
 type UserEntitiesUrl record {
+    @constraint:Array {minLength: 1}
     UrlEntity[] urls?;
 };
 
 
 type Get2ListsIdMembersResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
 
 type Expansions record {
+    @constraint:Array {minLength: 1}
     Place[] places?;
+    @constraint:Array {minLength: 1}
     Topic[] topics?;
+    @constraint:Array {minLength: 1}
     Poll[] polls?;
+    @constraint:Array {minLength: 1}
     Media[] media?;
+    @constraint:Array {minLength: 1}
     Tweet[] tweets?;
+    @constraint:Array {minLength: 1}
     User[] users?;
 };
 
 
 type Place record {
     Geo geo?;
+    @jsondata:Name {value: "contained_within"}
     PlaceId[] containedWithin?;
     # The full name of the county in which this place exists
     string country?;
+    @jsondata:Name {value: "country_code"}
     CountryCode countryCode?;
     # The full name of this place
+    @jsondata:Name {value: "full_name"}
     string fullName;
+    @jsondata:Name {value: "place_type"}
     PlaceType placeType?;
     # The human readable name of this place
     string name?;
@@ -699,6 +826,7 @@
 
 
 type Geo record {
+    @constraint:Array {maxLength: 4, minLength: 4}
     GeoBboxItemsNumber[] bbox;
     # A [GeoJson Point](https://tools.ietf.org/html/rfc7946#section-3.1.2) geometry object
     Point geometry?;
@@ -706,7 +834,8 @@
     record {|anydata...;|} properties;
 };
 
-// Unknown type: GeoBboxItemsNumber
+@constraint:Number {minValue: -180, maxValue: 180}
+type GeoBboxItemsNumber decimal;
 
 # A [GeoJson Point](https://tools.ietf.org/html/rfc7946#section-3.1.2) geometry object
 
@@ -716,9 +845,12 @@
     "Point" 'type;
 };
 
-// Unknown type: Position
+# A [GeoJson Position](https://tools.ietf.org/html/rfc7946#section-3.1.1) in the format `[longitude,latitude]`
+@constraint:Array {maxLength: 2, minLength: 2}
+type Position decimal[];
 
-// Unknown type: PlaceId
+# The identifier for this place
+type PlaceId string;
 
 type PlaceType "poi"|"neighborhood"|"city"|"admin"|"country"|"unknown";
 
@@ -733,14 +865,19 @@
     TopicId id;
 };
 
-// Unknown type: TopicId
+# Unique identifier of this Topic
+type TopicId string;
 
 # Represent a Poll attached to a Tweet
 
 type Poll record {
+    @jsondata:Name {value: "voting_status"}
     "open"|"closed" votingStatus?;
-    ballerina/lang.int:0.0.0:Signed32 durationMinutes?;
+    @jsondata:Name {value: "duration_minutes"}
+    int:Signed32 durationMinutes?;
+    @jsondata:Name {value: "end_datetime"}
     string endDatetime?;
+    @constraint:Array {maxLength: 4, minLength: 2}
     PollOption[] options;
     # Unique identifier of this poll
     PollId id;
@@ -757,15 +894,20 @@
     int position;
 };
 
-// Unknown type: PollOptionLabel
+# The text of a poll choice
+@constraint:String {maxLength: 25, minLength: 1}
+type PollOptionLabel string;
 
-// Unknown type: PollId
+# Unique identifier of this poll
+@constraint:String {pattern: re `^[0-9]{1,19}$`}
+type PollId string;
 
 
 type Media record {
     # The width of the media in pixels
     MediaWidth width?;
     string 'type;
+    @jsondata:Name {value: "media_key"}
     MediaKey mediaKey?;
     # The height of the media in pixels
     MediaHeight height?;
@@ -776,17 +918,22 @@
     # Specifies the type of attachments (if any) present in this Tweet
     TweetAttachments attachments?;
     # Creation time of the Tweet
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     # This is deprecated
     string 'source?;
     # Indicates withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country)
     TweetWithheld withheld?;
+    @jsondata:Name {value: "edit_controls"}
     TweetEditControls editControls?;
     # The location tagged on the Tweet, if the user provided one
     TweetGeo geo?;
+    @jsondata:Name {value: "conversation_id"}
     TweetId conversationId?;
     # A list of Tweet Ids in this Tweet chain
+    @jsondata:Name {value: "edit_history_tweet_ids"}
     TweetId[] editHistoryTweetIds?;
+    @jsondata:Name {value: "in_reply_to_user_id"}
     UserId inReplyToUserId?;
     # Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers
     TweetId id?;
@@ -794,20 +941,30 @@
     TweetText text?;
     # Language of the Tweet, if detected by X. Returned as a BCP47 language tag
     string lang?;
+    @jsondata:Name {value: "reply_settings"}
     ReplySettingsWithVerifiedUsers replySettings?;
     # A list of Posts this Tweet refers to. For example, if the parent Tweet is a Retweet, a Quoted Tweet or a Reply, it will include the related Tweet referenced to by its parent
+    @jsondata:Name {value: "referenced_tweets"}
     TweetReferencedTweets[] referencedTweets?;
     # Indicates if this Tweet contains URLs marked as sensitive, for example content suitable for mature audiences
+    @jsondata:Name {value: "possibly_sensitive"}
     boolean possiblySensitive?;
+    @jsondata:Name {value: "public_metrics"}
     TweetPublicMetrics publicMetrics?;
+    @jsondata:Name {value: "non_public_metrics"}
     TweetNonPublicMetrics nonPublicMetrics?;
+    @jsondata:Name {value: "note_tweet"}
     TweetNoteTweet noteTweet?;
+    @jsondata:Name {value: "context_annotations"}
     ContextAnnotation[] contextAnnotations?;
     FullTextEntities entities?;
+    @jsondata:Name {value: "promoted_metrics"}
     TweetPromotedMetrics promotedMetrics?;
     # The scopes for this tweet
     TweetScopes scopes?;
+    @jsondata:Name {value: "author_id"}
     UserId authorId?;
+    @jsondata:Name {value: "organic_metrics"}
     TweetOrganicMetrics organicMetrics?;
     # The X handle (screen name) of this user
     UserName username?;
@@ -817,10 +974,13 @@
 
 type TweetAttachments record {
     # A list of Posts the media on this Tweet was originally posted in. For example, if the media on a tweet is re-used in another Tweet, this refers to the original, source Tweet
+    @jsondata:Name {value: "media_source_tweet_id"}
     TweetId[] mediaSourceTweetId?;
     # A list of Media Keys for each one of the media attachments (if media are attached)
+    @jsondata:Name {value: "media_keys"}
     MediaKey[] mediaKeys?;
     # A list of poll IDs (if polls are attached)
+    @jsondata:Name {value: "poll_ids"}
     PollId[] pollIds?;
 };
 
@@ -832,16 +992,20 @@
     # Indicates whether the content being withheld is the `tweet` or a `user`
     "tweet"|"user" scope?;
     # Provides a list of countries where this content is not available
+    @jsondata:Name {value: "country_codes"}
     CountryCode[] countryCodes;
 };
 
 
 type TweetEditControls record {
     # Indicates if this Tweet is eligible to be edited
+    @jsondata:Name {value: "is_edit_eligible"}
     boolean isEditEligible;
     # Number of times this Tweet can be edited
+    @jsondata:Name {value: "edits_remaining"}
     int editsRemaining;
     # Time when Tweet is no longer editable
+    @jsondata:Name {value: "editable_until"}
     string editableUntil;
 };
 
@@ -850,10 +1014,12 @@
 type TweetGeo record {
     # A [GeoJson Point](https://tools.ietf.org/html/rfc7946#section-3.1.2) geometry object
     Point coordinates?;
+    @jsondata:Name {value: "place_id"}
     PlaceId placeId?;
 };
 
-// Unknown type: TweetText
+# The content of the Tweet
+type TweetText string;
 
 # Shows who can reply a Tweet. Fields returned are everyone, mentioned_users, subscribers, verified and following
 type ReplySettingsWithVerifiedUsers "everyone"|"mentionedUsers"|"following"|"other"|"subscribers"|"verified";
@@ -869,24 +1035,31 @@
 
 type TweetPublicMetrics record {
     # Number of times this Tweet has been liked
+    @jsondata:Name {value: "like_count"}
     int likeCount;
     # Number of times this Tweet has been bookmarked
-    ballerina/lang.int:0.0.0:Signed32 bookmarkCount;
+    @jsondata:Name {value: "bookmark_count"}
+    int:Signed32 bookmarkCount;
     # Number of times this Tweet has been replied to
+    @jsondata:Name {value: "reply_count"}
     int replyCount;
     # Number of times this Tweet has been quoted
+    @jsondata:Name {value: "quote_count"}
     int quoteCount?;
     # Number of times this Tweet has been Retweeted
+    @jsondata:Name {value: "retweet_count"}
     int retweetCount;
     # Number of times this Tweet has been viewed
-    ballerina/lang.int:0.0.0:Signed32 impressionCount;
+    @jsondata:Name {value: "impression_count"}
+    int:Signed32 impressionCount;
 };
 
 # Nonpublic engagement metrics for the Tweet at the time of the request
 
 type TweetNonPublicMetrics record {
     # Number of times this Tweet has been viewed
-    ballerina/lang.int:0.0.0:Signed32 impressionCount?;
+    @jsondata:Name {value: "impression_count"}
+    int:Signed32 impressionCount?;
 };
 
 # The full-content of the Tweet, including text beyond 280 characters
@@ -899,25 +1072,34 @@
 
 
 type TweetNoteTweetEntities record {
+    @constraint:Array {minLength: 1}
     CashtagEntity[] cashtags?;
+    @constraint:Array {minLength: 1}
     UrlEntity[] urls?;
+    @constraint:Array {minLength: 1}
     HashtagEntity[] hashtags?;
+    @constraint:Array {minLength: 1}
     MentionEntity[] mentions?;
 };
 
-// Unknown type: NoteTweetText
+# The note content of the Tweet
+type NoteTweetText string;
 
 # Promoted nonpublic engagement metrics for the Tweet at the time of the request
 
 type TweetPromotedMetrics record {
     # Number of times this Tweet has been liked
-    ballerina/lang.int:0.0.0:Signed32 likeCount?;
+    @jsondata:Name {value: "like_count"}
+    int:Signed32 likeCount?;
     # Number of times this Tweet has been replied to
-    ballerina/lang.int:0.0.0:Signed32 replyCount?;
+    @jsondata:Name {value: "reply_count"}
+    int:Signed32 replyCount?;
     # Number of times this Tweet has been Retweeted
-    ballerina/lang.int:0.0.0:Signed32 retweetCount?;
+    @jsondata:Name {value: "retweet_count"}
+    int:Signed32 retweetCount?;
     # Number of times this Tweet has been viewed
-    ballerina/lang.int:0.0.0:Signed32 impressionCount?;
+    @jsondata:Name {value: "impression_count"}
+    int:Signed32 impressionCount?;
 };
 
 # The scopes for this tweet
@@ -931,12 +1113,16 @@
 
 type TweetOrganicMetrics record {
     # Number of times this Tweet has been liked
+    @jsondata:Name {value: "like_count"}
     int likeCount;
     # Number of times this Tweet has been replied to
+    @jsondata:Name {value: "reply_count"}
     int replyCount;
     # Number of times this Tweet has been Retweeted
+    @jsondata:Name {value: "retweet_count"}
     int retweetCount;
     # Number of times this Tweet has been viewed
+    @jsondata:Name {value: "impression_count"}
     int impressionCount;
 };
 
@@ -953,25 +1139,34 @@
 
 type SearchSpacesQueries record {
     # A comma separated list of Space fields to display
+    @http:Query {name: "space.fields"}
     ("created_at"|"creator_id"|"ended_at"|"host_ids"|"id"|"invited_user_ids"|"is_ticketed"|"lang"|"participant_count"|"scheduled_start"|"speaker_ids"|"started_at"|"state"|"subscriber_count"|"title"|"topic_ids"|"updated_at")[] spaceFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # The search query
+    @constraint:String {maxLength: 2048, minLength: 1}
     string query;
     # The number of results to return
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # The state of Spaces to search for
     "live"|"scheduled"|"all" state?;
     # A comma separated list of Topic fields to display
+    @http:Query {name: "topic.fields"}
     ("description"|"id"|"name")[] topicFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("creator_id"|"host_ids"|"invited_user_ids"|"speaker_ids"|"topic_ids")[] expansions?;
 };
 
 
 type Get2UsersIdFollowersResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -979,6 +1174,7 @@
 
 type GetRuleCountQueries record {
     # A comma separated list of RulesCount fields to display
+    @http:Query {name: "rules_count.fields"}
     ("all_project_client_apps"|"cap_per_client_app"|"cap_per_project"|"client_app_rules_count"|"project_rules_count")[] rulesCountFields?;
 };
 
@@ -986,18 +1182,23 @@
 
 type FindUsersByIdQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A list of User IDs, comma-separated. You can specify up to 100 IDs
+    @constraint:Array {maxLength: 100, minLength: 1}
     UserId[] ids;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
 
 type ListUpdateResponse record {
     ListUpdateResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -1010,21 +1211,29 @@
 
 type GetUserListMembershipsQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get a specified 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationTokenLong paginationToken?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of List fields to display
+    @http:Query {name: "list.fields"}
     ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     "owner_id"[] expansions?;
 };
 
 
 type Get2TweetsIdLikingUsersResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -1032,22 +1241,28 @@
 
 type DmEventAttachments record {
     # A list of Media Keys for each one of the media attachments (if media are attached)
+    @jsondata:Name {value: "media_keys"}
     MediaKey[] mediaKeys?;
     # A list of card IDs (if cards are attached)
+    @jsondata:Name {value: "card_ids"}
     string[] cardIds?;
 };
 
 
 type Get2UsersSearchResponse record {
+    @constraint:Array {minLength: 1}
     User[] data?;
     Get2UsersSearchResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2UsersSearchResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
 };
 
@@ -1061,17 +1276,27 @@
 type DmEvent record {
     # Specifies the type of attachments (if any) present in this DM
     DmEventAttachments attachments?;
+    @constraint:Array {minLength: 1}
     HashtagEntity[] hashtags?;
     # A list of Posts this DM refers to
+    @jsondata:Name {value: "referenced_tweets"}
     DmEventReferencedTweets[] referencedTweets?;
     # A list of participants for a ParticipantsJoin or ParticipantsLeave event_type
+    @jsondata:Name {value: "participant_ids"}
     UserId[] participantIds?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "sender_id"}
     UserId senderId?;
+    @constraint:Array {minLength: 1}
     CashtagEntity[] cashtags?;
+    @constraint:Array {minLength: 1}
     UrlEntityDm[] urls?;
+    @jsondata:Name {value: "dm_conversation_id"}
     DmConversationId dmConversationId?;
+    @jsondata:Name {value: "event_type"}
     string eventType;
+    @constraint:Array {minLength: 1}
     MentionEntity[] mentions?;
     # Unique identifier of a DM Event
     DmEventId id;
@@ -1087,7 +1312,7 @@
 # Represent the portion of text recognized as a URL, and its start and end position within the text
 
 type UrlEntityDm record {
-    int start;
+    int 'start;
     int end;
     string displayUrl?;
     UrlImage[] images?;
@@ -1100,32 +1325,46 @@
     HttpStatusCode status?;
 };
 
-// Unknown type: DmConversationId
+# Unique identifier of a DM conversation. This can either be a numeric string, or a pair of numeric strings separated by a '-' character in the case of one-on-one DM Conversations
+@constraint:String {pattern: re `^([0-9]{1,19}-[0-9]{1,19}|[0-9]{15,19})$`}
+type DmConversationId string;
 
-// Unknown type: DmEventId
+# Unique identifier of a DM Event
+@constraint:String {pattern: re `^[0-9]{1,19}$`}
+type DmEventId string;
 
 # Represents the Queries record for the operation: getTweetsFirehoseStreamLangEn
 
 type GetTweetsFirehoseStreamLangEnQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # The number of minutes of backfill requested
-    ballerina/lang.int:0.0.0:Signed32 backfillMinutes?;
+    @http:Query {name: "backfill_minutes"}
+    int:Signed32 backfillMinutes?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "start_time"}
     string startTime?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # The partition number
-    ballerina/lang.int:0.0.0:Signed32 partition;
+    @constraint:Int {minValue: 1, maxValue: 8}
+    int:Signed32 partition;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "end_time"}
     string endTime?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
@@ -1137,9 +1376,12 @@
     RuleTag tag?;
 };
 
-// Unknown type: RuleId
+# Unique identifier of this rule
+@constraint:String {pattern: re `^[0-9]{1,19}$`}
+type RuleId string;
 
-// Unknown type: RuleTag
+# A tag meant for the labeling of user provided rules
+type RuleTag string;
 
 
 type LikeComplianceSchema record {
@@ -1148,25 +1390,33 @@
 
 
 type Get2TweetsResponse record {
+    @constraint:Array {minLength: 1}
     Tweet[] data?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 # A count of user-provided stream filtering rules at the client application level
 
 type AppRulesCount record {
+    @jsondata:Name {value: "client_app_id"}
     ClientAppId clientAppId?;
     # Number of rules for client application
-    ballerina/lang.int:0.0.0:Signed32 ruleCount?;
+    @jsondata:Name {value: "rule_count"}
+    int:Signed32 ruleCount?;
 };
 
-// Unknown type: ClientAppId
+# The ID of the client application
+@constraint:String {maxLength: 19, minLength: 1}
+type ClientAppId string;
 
-// Unknown type: AllProjectClientApps
+# Client App Rule Counts for all applications in the project
+type AllProjectClientApps AppRulesCount[];
 
 
 type LikesComplianceStreamResponseLikesComplianceStreamResponseOneOf12 record {
+    @constraint:Array {minLength: 1}
     Problem[] errors;
 };
 
@@ -1177,12 +1427,14 @@
 
 
 type UserDeleteComplianceSchema record {
+    @jsondata:Name {value: "user_delete"}
     UserComplianceSchema userDelete;
 };
 
 
 type UserComplianceSchema record {
     # Event time
+    @jsondata:Name {value: "event_at"}
     string eventAt;
     UserComplianceSchemaUser user;
 };
@@ -1195,30 +1447,39 @@
 
 
 type Get2TweetsIdQuoteTweetsResponse record {
+    @constraint:Array {minLength: 1}
     Tweet[] data?;
     Get2TweetsIdQuoteTweetsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2TweetsIdQuoteTweetsResponseMeta record {
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
 
 type Get2DmConversationsWithParticipantIdDmEventsResponse record {
+    @constraint:Array {minLength: 1}
     DmEvent[] data?;
     Get2DmConversationsWithParticipantIdDmEventsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2DmConversationsWithParticipantIdDmEventsResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -1226,25 +1487,32 @@
 
 type ListIdGetQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of List fields to display
+    @http:Query {name: "list.fields"}
     ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     "owner_id"[] expansions?;
 };
 
 
 type ListUpdateRequest record {
     boolean 'private?;
+    @constraint:String {maxLength: 25, minLength: 1}
     string name?;
+    @constraint:String {maxLength: 100}
     string description?;
 };
 
 
 type Get2UsersIdFollowedListsResponse record {
+    @constraint:Array {minLength: 1}
     List[] data?;
     Get2UsersIdFollowedListsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -1252,21 +1520,28 @@
 
 type List record {
     boolean 'private?;
+    @jsondata:Name {value: "owner_id"}
     UserId ownerId?;
     # The name of this List
     string name;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string description?;
     # The unique identifier of this List
     ListId id;
+    @jsondata:Name {value: "member_count"}
     int memberCount?;
+    @jsondata:Name {value: "follower_count"}
     int followerCount?;
 };
 
 
 type Get2UsersIdFollowedListsResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -1274,24 +1549,34 @@
 
 type GetTweetsFirehoseStreamLangJaQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # The number of minutes of backfill requested
-    ballerina/lang.int:0.0.0:Signed32 backfillMinutes?;
+    @http:Query {name: "backfill_minutes"}
+    int:Signed32 backfillMinutes?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "start_time"}
     string startTime?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # The partition number
-    ballerina/lang.int:0.0.0:Signed32 partition;
+    @constraint:Int {minValue: 1, maxValue: 2}
+    int:Signed32 partition;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "end_time"}
     string endTime?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
@@ -1304,58 +1589,71 @@
 
 
 type UserProtectComplianceSchema record {
+    @jsondata:Name {value: "user_protect"}
     UserComplianceSchema userProtect;
 };
 
 
 type UserUnprotectComplianceSchema record {
+    @jsondata:Name {value: "user_unprotect"}
     UserComplianceSchema userUnprotect;
 };
 
 
 type UserUndeleteComplianceSchema record {
+    @jsondata:Name {value: "user_undelete"}
     UserComplianceSchema userUndelete;
 };
 
 
 type UserSuspendComplianceSchema record {
+    @jsondata:Name {value: "user_suspend"}
     UserComplianceSchema userSuspend;
 };
 
 
 type UserUnsuspendComplianceSchema record {
+    @jsondata:Name {value: "user_unsuspend"}
     UserComplianceSchema userUnsuspend;
 };
 
 
 type UserWithheldComplianceSchema record {
+    @jsondata:Name {value: "user_withheld"}
     UserTakedownComplianceSchema userWithheld;
 };
 
 
 type UserTakedownComplianceSchema record {
+    @jsondata:Name {value: "withheld_in_countries"}
     CountryCode[] withheldInCountries;
     # Event time
+    @jsondata:Name {value: "event_at"}
     string eventAt;
     UserTakedownComplianceSchemaUser user;
 };
 
 
 type UserScrubGeoSchema record {
+    @jsondata:Name {value: "scrub_geo"}
     UserScrubGeoObjectSchema scrubGeo;
 };
 
 
 type UserProfileModificationComplianceSchema record {
+    @jsondata:Name {value: "user_profile_modification"}
     UserProfileModificationObjectSchema userProfileModification;
 };
 
 
 type UserProfileModificationObjectSchema record {
     # Event time
+    @jsondata:Name {value: "event_at"}
     string eventAt;
     UserProfileModificationObjectSchemaUser user;
+    @jsondata:Name {value: "new_value"}
     string newValue;
+    @jsondata:Name {value: "profile_field"}
     string profileField;
 };
 
@@ -1366,24 +1664,27 @@
 };
 
 # User compliance data
-type UserComplianceData ballerinax/twitter:5.0.1:UserProtectComplianceSchema|ballerinax/twitter:5.0.1:UserUnprotectComplianceSchema|ballerinax/twitter:5.0.1:UserDeleteComplianceSchema|ballerinax/twitter:5.0.1:UserUndeleteComplianceSchema|ballerinax/twitter:5.0.1:UserSuspendComplianceSchema|ballerinax/twitter:5.0.1:UserUnsuspendComplianceSchema|ballerinax/twitter:5.0.1:UserWithheldComplianceSchema|ballerinax/twitter:5.0.1:UserScrubGeoSchema|ballerinax/twitter:5.0.1:UserProfileModificationComplianceSchema;
+type UserComplianceData UserProtectComplianceSchema|UserUnprotectComplianceSchema|UserDeleteComplianceSchema|UserUndeleteComplianceSchema|UserSuspendComplianceSchema|UserUnsuspendComplianceSchema|UserWithheldComplianceSchema|UserScrubGeoSchema|UserProfileModificationComplianceSchema;
 
 
 type UserComplianceStreamResponseUserComplianceStreamResponseOneOf12 record {
+    @constraint:Array {minLength: 1}
     Problem[] errors;
 };
 
 # User compliance stream events
-type UserComplianceStreamResponse ballerinax/twitter:5.0.1:UserComplianceStreamResponseOneOf1|ballerinax/twitter:5.0.1:UserComplianceStreamResponseUserComplianceStreamResponseOneOf12;
+type UserComplianceStreamResponse UserComplianceStreamResponseOneOf1|UserComplianceStreamResponseUserComplianceStreamResponseOneOf12;
 
-// Unknown type: Start
+# The start time of the bucket
+type Start string;
 
 
 type RulesRequestSummaryRulesRequestSummaryOneOf12 record {
     # Number of user-specified stream filtering rules that were deleted
-    ballerina/lang.int:0.0.0:Signed32 deleted;
+    int:Signed32 deleted;
     # Number of user-specified stream filtering rules that were not deleted
-    ballerina/lang.int:0.0.0:Signed32 notDeleted;
+    @jsondata:Name {value: "not_deleted"}
+    int:Signed32 notDeleted;
 };
 
 # Type of compliance job to list
@@ -1391,16 +1692,22 @@
 
 
 type Get2ListsIdTweetsResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
-// Unknown type: PaginationToken32
+# A base32 pagination token
+@constraint:String {minLength: 16}
+type PaginationToken32 string;
 
 
 type DeleteDmResponse record {
     DeleteDmResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -1409,7 +1716,9 @@
     boolean deleted?;
 };
 
-// Unknown type: LikeId
+# The unique identifier of this Like
+@constraint:String {pattern: re `^[A-Za-z0-9_]{1,40}$`}
+type LikeId string;
 
 
 type TweetWithheldComplianceSchema record {
@@ -1418,9 +1727,12 @@
 
 
 type TweetTakedownComplianceSchema record {
+    @jsondata:Name {value: "quote_tweet_id"}
     TweetId quoteTweetId?;
+    @jsondata:Name {value: "withheld_in_countries"}
     CountryCode[] withheldInCountries;
     # Event time
+    @jsondata:Name {value: "event_at"}
     string eventAt;
     TweetTakedownComplianceSchemaTweet tweet;
 };
@@ -1429,14 +1741,17 @@
 type TweetTakedownComplianceSchemaTweet record {
     # Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers
     TweetId id;
+    @jsondata:Name {value: "author_id"}
     UserId authorId;
 };
 
-// Unknown type: DownloadUrl
+# URL from which the user will retrieve their compliance results
+type DownloadUrl string;
 
 
 type ListFollowedResponse record {
     ListFollowedResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -1447,14 +1762,17 @@
 
 
 type Get2TweetsCountsRecentResponse record {
+    @constraint:Array {minLength: 1}
     SearchCount[] data?;
     Get2TweetsCountsRecentResponseMeta meta?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 # Represent a Search Count Result
 
 type SearchCount record {
+    @jsondata:Name {value: "tweet_count"}
     TweetCount tweetCount;
     # The start time of the bucket
     Start 'start;
@@ -1462,15 +1780,21 @@
     End end;
 };
 
-// Unknown type: TweetCount
+# The count for the bucket
+type TweetCount int;
 
-// Unknown type: End
+# The end time of the bucket
+type End string;
 
 
 type Get2TweetsCountsRecentResponseMeta record {
+    @jsondata:Name {value: "total_tweet_count"}
     Aggregate totalTweetCount?;
+    @jsondata:Name {value: "oldest_id"}
     OldestId oldestId?;
+    @jsondata:Name {value: "newest_id"}
     NewestId newestId?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
 };
 
@@ -1478,49 +1802,66 @@
 
 type SearchUserByQueryQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # TThe the query string by which to query for users
     UserSearchQuery query;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified
+    @http:Query {name: "next_token"}
     PaginationToken36 nextToken?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
-// Unknown type: UserSearchQuery
+# The the search string by which to query for users
+@constraint:String {pattern: re `^[A-Za-z0-9_]{1,32}$`}
+type UserSearchQuery string;
 
-// Unknown type: PaginationToken36
+# A base36 pagination token
+@constraint:String {minLength: 1}
+type PaginationToken36 string;
 
 
 type Get2TweetsIdRetweetsResponse record {
+    @constraint:Array {minLength: 1}
     Tweet[] data?;
     Get2TweetsIdRetweetsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2TweetsIdRetweetsResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
 
 type MuteUserRequest record {
+    @jsondata:Name {value: "target_user_id"}
     UserId targetUserId;
 };
 
 
 type RulesResponseMetadata record {
     RulesRequestSummary summary?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
     # Number of Rules in result set
-    ballerina/lang.int:0.0.0:Signed32 resultCount?;
+    @jsondata:Name {value: "result_count"}
+    int:Signed32 resultCount?;
     string sent;
 };
 
@@ -1528,51 +1869,66 @@
 
 type RulesRequestSummaryOneOf1 record {
     # Number of valid user-specified stream filtering rules
-    ballerina/lang.int:0.0.0:Signed32 valid;
+    int:Signed32 valid;
     # Number of user-specified stream filtering rules that were not created
-    ballerina/lang.int:0.0.0:Signed32 notCreated;
+    @jsondata:Name {value: "not_created"}
+    int:Signed32 notCreated;
     # Number of user-specified stream filtering rules that were created
-    ballerina/lang.int:0.0.0:Signed32 created;
+    int:Signed32 created;
     # Number of invalid user-specified stream filtering rules
-    ballerina/lang.int:0.0.0:Signed32 invalid;
+    int:Signed32 invalid;
 };
 
-type RulesRequestSummary ballerinax/twitter:5.0.1:RulesRequestSummaryOneOf1|ballerinax/twitter:5.0.1:RulesRequestSummaryRulesRequestSummaryOneOf12;
+type RulesRequestSummary RulesRequestSummaryOneOf1|RulesRequestSummaryRulesRequestSummaryOneOf12;
 
 # Represents the Queries record for the operation: getTweetsFirehoseStreamLangPt
 
 type GetTweetsFirehoseStreamLangPtQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # The number of minutes of backfill requested
-    ballerina/lang.int:0.0.0:Signed32 backfillMinutes?;
+    @http:Query {name: "backfill_minutes"}
+    int:Signed32 backfillMinutes?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "start_time"}
     string startTime?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # The partition number
-    ballerina/lang.int:0.0.0:Signed32 partition;
+    @constraint:Int {minValue: 1, maxValue: 2}
+    int:Signed32 partition;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "end_time"}
     string endTime?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
 
 type Get2UsersIdBookmarksResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
 
 type ListAddUserRequest record {
+    @jsondata:Name {value: "user_id"}
     UserId userId;
 };
 
@@ -1591,7 +1947,8 @@
     RuleValue value;
 };
 
-// Unknown type: RuleValue
+# The filterlang value of the rule
+type RuleValue string;
 
 # A response from deleting user-specified stream filtering rules
 
@@ -1609,7 +1966,7 @@
     RuleId[] ids?;
 };
 
-type AddOrDeleteRulesRequest ballerinax/twitter:5.0.1:AddRulesRequest|ballerinax/twitter:5.0.1:DeleteRulesRequest;
+type AddOrDeleteRulesRequest AddRulesRequest|DeleteRulesRequest;
 
 
 type RulesLookupResponse record {
@@ -1636,6 +1993,7 @@
 
 type ListUnpinResponse record {
     ListUnpinResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -1647,6 +2005,7 @@
 
 type UsersLikesCreateResponse record {
     UsersLikesCreateResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -1675,28 +2034,38 @@
 
 type GetDmConversationsIdDmEventsQueries record {
     # A comma separated list of DmEvent fields to display
+    @http:Query {name: "dm_event.fields"}
     ("attachments"|"created_at"|"dm_conversation_id"|"entities"|"event_type"|"id"|"participant_ids"|"referenced_tweets"|"sender_id"|"text")[] dmEventFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get a specified 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken32 paginationToken?;
     # The set of event_types to include in the results
+    @http:Query {name: "event_types"}
     ("MessageCreate"|"ParticipantsJoin"|"ParticipantsLeave")[] eventTypes?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"participant_ids"|"referenced_tweets.id"|"sender_id")[] expansions?;
 };
 
-// Unknown type: FindSpacesByIdsQueriesIdsItemsString
+@constraint:String {pattern: re `^[a-zA-Z0-9]{1,13}$`}
+type FindSpacesByIdsQueriesIdsItemsString string;
 
 
 type UsersFollowingDeleteResponse record {
     UsersFollowingDeleteResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -1707,6 +2076,7 @@
 
 
 type TweetComplianceStreamResponseTweetComplianceStreamResponseOneOf12 record {
+    @constraint:Array {minLength: 1}
     Problem[] errors;
 };
 
@@ -1714,10 +2084,13 @@
 
 type ClientAppUsage record {
     # The number of results returned
-    ballerina/lang.int:0.0.0:Signed32 usageResultCount?;
+    @jsondata:Name {value: "usage_result_count"}
+    int:Signed32 usageResultCount?;
     # The unique identifier for this project
+    @jsondata:Name {value: "client_app_id"}
     string clientAppId?;
     # The usage value
+    @constraint:Array {minLength: 1}
     UsageFields[] usage?;
 };
 
@@ -1727,11 +2100,12 @@
     # The time period for the usage
     string date?;
     # The usage value
-    ballerina/lang.int:0.0.0:Signed32 usage?;
+    int:Signed32 usage?;
 };
 
 
 type UsersFollowingCreateRequest record {
+    @jsondata:Name {value: "target_user_id"}
     UserId targetUserId;
 };
 
@@ -1739,8 +2113,10 @@
 
 type UsageDailyProjectUsage record {
     # The unique identifier for this project
-    ballerina/lang.int:0.0.0:Signed32 projectId?;
+    @jsondata:Name {value: "project_id"}
+    int:Signed32 projectId?;
     # The usage value
+    @constraint:Array {minLength: 1}
     UsageFields[] usage?;
 };
 
@@ -1748,12 +2124,16 @@
 
 type FindSpaceByIdQueries record {
     # A comma separated list of Space fields to display
+    @http:Query {name: "space.fields"}
     ("created_at"|"creator_id"|"ended_at"|"host_ids"|"id"|"invited_user_ids"|"is_ticketed"|"lang"|"participant_count"|"scheduled_start"|"speaker_ids"|"started_at"|"state"|"subscriber_count"|"title"|"topic_ids"|"updated_at")[] spaceFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of Topic fields to display
+    @http:Query {name: "topic.fields"}
     ("description"|"id"|"name")[] topicFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("creator_id"|"host_ids"|"invited_user_ids"|"speaker_ids"|"topic_ids")[] expansions?;
 };
 
@@ -1762,20 +2142,24 @@
     # Attachments to a DM Event
     DmAttachments attachments;
     # Text of the message
+    @constraint:String {minLength: 1}
     string text?;
 };
 
 
 type DmMediaAttachment record {
+    @jsondata:Name {value: "media_id"}
     MediaId mediaId;
 };
 
-// Unknown type: DmAttachments
+# Attachments to a DM Event
+type DmAttachments DmMediaAttachment[];
 
 # Represents the Queries record for the operation: getTrends
 
 type GetTrendsQueries record {
     # A comma separated list of Trend fields to display
+    @http:Query {name: "trend.fields"}
     ("trend_name"|"tweet_count")[] trendFields?;
 };
 
@@ -1783,50 +2167,68 @@
 
 type ListUserOwnedListsQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get a specified 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationTokenLong paginationToken?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of List fields to display
+    @http:Query {name: "list.fields"}
     ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     "owner_id"[] expansions?;
 };
 
 
 type Get2SpacesIdBuyersResponse record {
+    @constraint:Array {minLength: 1}
     User[] data?;
     Get2SpacesIdBuyersResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2SpacesIdBuyersResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
 
 type Get2UsersIdFollowersResponse record {
+    @constraint:Array {minLength: 1}
     User[] data?;
     Get2UsersIdFollowersResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
-// Unknown type: DownloadExpiration
+# Expiration time of the download URL
+type DownloadExpiration string;
 
 
 type ComplianceJob record {
+    @jsondata:Name {value: "download_expires_at"}
     DownloadExpiration downloadExpiresAt;
+    @jsondata:Name {value: "download_url"}
     DownloadUrl downloadUrl;
     # User-provided name for a compliance job
     ComplianceJobName name?;
+    @jsondata:Name {value: "upload_expires_at"}
     UploadExpiration uploadExpiresAt;
+    @jsondata:Name {value: "created_at"}
     CreatedAt createdAt;
+    @jsondata:Name {value: "upload_url"}
     UploadUrl uploadUrl;
     # Compliance Job ID
     JobId id;
@@ -1836,13 +2238,18 @@
     ComplianceJobStatus status;
 };
 
-// Unknown type: UploadExpiration
+# Expiration time of the upload URL
+type UploadExpiration string;
 
-// Unknown type: CreatedAt
+# Creation time of the compliance job
+type CreatedAt string;
 
-// Unknown type: UploadUrl
+# URL to which the user will upload their Tweet or user IDs
+type UploadUrl string;
 
-// Unknown type: JobId
+# Compliance Job ID
+@constraint:String {pattern: re `^[0-9]{1,19}$`}
+type JobId string;
 
 # Status of a compliance job
 type ComplianceJobStatus "created"|"in_progress"|"failed"|"complete"|"expired";
@@ -1850,13 +2257,17 @@
 
 type BookmarkMutationResponse record {
     BookmarkMutationResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2UsersIdListMembershipsResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -1871,22 +2282,31 @@
 
 type SearchStreamQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # The number of minutes of backfill requested
-    ballerina/lang.int:0.0.0:Signed32 backfillMinutes?;
+    @http:Query {name: "backfill_minutes"}
+    int:Signed32 backfillMinutes?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided
+    @http:Query {name: "start_time"}
     string startTime?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "end_time"}
     string endTime?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
@@ -1897,10 +2317,13 @@
 
 
 type TweetEditComplianceObjectSchema record {
+    @jsondata:Name {value: "initial_tweet_id"}
     TweetId initialTweetId;
     # Event time
+    @jsondata:Name {value: "event_at"}
     string eventAt;
     TweetEditComplianceObjectSchemaTweet tweet;
+    @jsondata:Name {value: "edit_tweet_ids"}
     TweetId[] editTweetIds;
 };
 
@@ -1914,34 +2337,47 @@
 
 type UsersIdMentionsQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified
+    @http:Query {name: "start_time"}
     string startTime?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get the next 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken36 paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified
+    @http:Query {name: "end_time"}
     string endTime?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified
+    @http:Query {name: "since_id"}
     TweetId sinceId?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
     # The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified
+    @http:Query {name: "until_id"}
     TweetId untilId?;
 };
 
 # Place ID being attached to the Tweet for geo location
 
 type TweetCreateRequestGeo record {
+    @jsondata:Name {value: "place_id"}
     string placeId?;
 };
 
@@ -1949,20 +2385,28 @@
 
 type FindTweetsThatRetweetATweetQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get the next 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken36 paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
@@ -1970,18 +2414,25 @@
 
 type FindTweetsByIdQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # A comma separated list of Post IDs. Up to 100 are allowed in a single request
+    @constraint:Array {maxLength: 100, minLength: 1}
     TweetId[] ids;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
@@ -1989,16 +2440,19 @@
 
 type GetRulesQueries record {
     # This value is populated by passing the 'next_token' returned in a request to paginate through results
+    @http:Query {name: "pagination_token"}
     string paginationToken?;
     # A comma-separated list of Rule IDs
     RuleId[] ids?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
 };
 
 
 type ListPinnedResponse record {
     ListPinnedResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -2006,14 +2460,19 @@
 
 type TweetsIdLikingUsersQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get the next 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken36 paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
@@ -2022,6 +2481,7 @@
     # Attachments to a DM Event
     DmAttachments attachments?;
     # Text of the message
+    @constraint:String {minLength: 1}
     string text;
 };
 
@@ -2029,12 +2489,16 @@
 
 type GetTweetsComplianceStreamQueries record {
     # The number of minutes of backfill requested
-    ballerina/lang.int:0.0.0:Signed32 backfillMinutes?;
+    @http:Query {name: "backfill_minutes"}
+    int:Signed32 backfillMinutes?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post Compliance events will be provided
+    @http:Query {name: "start_time"}
     string startTime?;
     # The partition number
-    ballerina/lang.int:0.0.0:Signed32 partition;
+    @constraint:Int {minValue: 1, maxValue: 4}
+    int:Signed32 partition;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Post Compliance events will be provided
+    @http:Query {name: "end_time"}
     string endTime?;
 };
 
@@ -2042,15 +2506,21 @@
 
 type Usage record {
     # Number of days left for the Tweet cap to reset
-    ballerina/lang.int:0.0.0:Signed32 capResetDay?;
+    @jsondata:Name {value: "cap_reset_day"}
+    int:Signed32 capResetDay?;
     # The number of Posts read in this project
-    ballerina/lang.int:0.0.0:Signed32 projectUsage?;
+    @jsondata:Name {value: "project_usage"}
+    int:Signed32 projectUsage?;
     # Total number of Posts that can be read in this project per month
-    ballerina/lang.int:0.0.0:Signed32 projectCap?;
+    @jsondata:Name {value: "project_cap"}
+    int:Signed32 projectCap?;
     # The unique identifier for this project
+    @jsondata:Name {value: "project_id"}
     string projectId?;
     # The daily usage breakdown for each Client Application a project
+    @jsondata:Name {value: "daily_client_app_usage"}
     ClientAppUsage[] dailyClientAppUsage?;
+    @jsondata:Name {value: "daily_project_usage"}
     UsageDailyProjectUsage dailyProjectUsage?;
 };
 
@@ -2058,19 +2528,25 @@
 
 type FindUsersByUsernameQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A list of usernames, comma-separated
+    @constraint:Array {maxLength: 100, minLength: 1}
     FindUsersByUsernameQueriesUsernamesItemsString[] usernames;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
-// Unknown type: FindUsersByUsernameQueriesUsernamesItemsString
+@constraint:String {pattern: re `^[A-Za-z0-9_]{1,15}$`}
+type FindUsersByUsernameQueriesUsernamesItemsString string;
 
 
 type BookmarkAddRequest record {
+    @jsondata:Name {value: "tweet_id"}
     TweetId tweetId;
 };
 
@@ -2078,10 +2554,13 @@
 
 type FindMyUserQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
@@ -2092,27 +2571,33 @@
 };
 
 # Likes compliance stream events
-type LikesComplianceStreamResponse ballerinax/twitter:5.0.1:LikesComplianceStreamResponseOneOf1|ballerinax/twitter:5.0.1:LikesComplianceStreamResponseLikesComplianceStreamResponseOneOf12;
+type LikesComplianceStreamResponse LikesComplianceStreamResponseOneOf1|LikesComplianceStreamResponseLikesComplianceStreamResponseOneOf12;
 
 
 type Get2TweetsSample10StreamResponse record {
     Tweet data?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2UsersIdLikedTweetsResponse record {
+    @constraint:Array {minLength: 1}
     Tweet[] data?;
     Get2UsersIdLikedTweetsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2TweetsIdRetweetedByResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -2130,6 +2615,7 @@
 type Get2UsageTweetsResponse record {
     # Usage per client app
     Usage data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -2137,45 +2623,61 @@
 type TweetUnviewableTweet record {
     # Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers
     TweetId id;
+    @jsondata:Name {value: "author_id"}
     UserId authorId;
 };
 
 
 type ListMutateResponseData record {
+    @jsondata:Name {value: "is_member"}
     boolean isMember?;
 };
 
 
 type Get2UsersIdOwnedListsResponse record {
+    @constraint:Array {minLength: 1}
     List[] data?;
     Get2UsersIdOwnedListsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2UsersIdTweetsResponseMeta record {
+    @jsondata:Name {value: "oldest_id"}
     OldestId oldestId?;
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "newest_id"}
     NewestId newestId?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
 
 type Get2UsersIdTimelinesReverseChronologicalResponse record {
+    @constraint:Array {minLength: 1}
     Tweet[] data?;
     Get2UsersIdTimelinesReverseChronologicalResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2UsersIdTimelinesReverseChronologicalResponseMeta record {
+    @jsondata:Name {value: "oldest_id"}
     OldestId oldestId?;
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "newest_id"}
     NewestId newestId?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -2183,14 +2685,19 @@
 
 type UsersIdBlockingQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get a specified 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken32 paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
@@ -2198,10 +2705,13 @@
 
 type ListUserPinnedListsQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of List fields to display
+    @http:Query {name: "list.fields"}
     ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     "owner_id"[] expansions?;
 };
 
@@ -2209,8 +2719,10 @@
 
 type Trend record {
     # Number of Posts in this trend
-    ballerina/lang.int:0.0.0:Signed32 tweetCount?;
+    @jsondata:Name {value: "tweet_count"}
+    int:Signed32 tweetCount?;
     # Name of the trend
+    @jsondata:Name {value: "trend_name"}
     string trendName?;
 };
 
@@ -2218,26 +2730,35 @@
 
 type TweetCountsFullArchiveSearchQueries record {
     # YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute)
+    @http:Query {name: "start_time"}
     string startTime?;
     # A comma separated list of SearchCount fields to display
+    @http:Query {name: "search_count.fields"}
     ("end"|"start"|"tweet_count")[] searchCountFields?;
     # This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified
+    @http:Query {name: "pagination_token"}
     PaginationToken36 paginationToken?;
     # The granularity for the search counts results
     "minute"|"hour"|"day" granularity?;
     # One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length
+    @constraint:String {maxLength: 4096, minLength: 1}
     string query;
     # YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute)
+    @http:Query {name: "end_time"}
     string endTime?;
     # Returns results with a Post ID greater than (that is, more recent than) the specified ID
+    @http:Query {name: "since_id"}
     TweetId sinceId?;
     # This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified
+    @http:Query {name: "next_token"}
     PaginationToken36 nextToken?;
     # Returns results with a Post ID less than (that is, older than) the specified ID
+    @http:Query {name: "until_id"}
     TweetId untilId?;
 };
 
-// Unknown type: TweetCreateRequestPollOptionsItemsString
+@constraint:String {maxLength: 25, minLength: 1}
+type TweetCreateRequestPollOptionsItemsString string;
 
 # A response from modifying user-specified stream filtering rules
 
@@ -2245,11 +2766,13 @@
     # All user-specified stream filtering rules that were created
     Rule[] data?;
     RulesResponseMetadata meta;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2SpacesSearchResponseMeta record {
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -2257,37 +2780,49 @@
 
 type TweetCountsRecentSearchQueries record {
     # YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute)
+    @http:Query {name: "start_time"}
     string startTime?;
     # A comma separated list of SearchCount fields to display
+    @http:Query {name: "search_count.fields"}
     ("end"|"start"|"tweet_count")[] searchCountFields?;
     # This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified
+    @http:Query {name: "pagination_token"}
     PaginationToken36 paginationToken?;
     # The granularity for the search counts results
     "minute"|"hour"|"day" granularity?;
     # One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length
+    @constraint:String {maxLength: 4096, minLength: 1}
     string query;
     # YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute)
+    @http:Query {name: "end_time"}
     string endTime?;
     # Returns results with a Post ID greater than (that is, more recent than) the specified ID
+    @http:Query {name: "since_id"}
     TweetId sinceId?;
     # This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified
+    @http:Query {name: "next_token"}
     PaginationToken36 nextToken?;
     # Returns results with a Post ID less than (that is, older than) the specified ID
+    @http:Query {name: "until_id"}
     TweetId untilId?;
 };
 
 
 type Get2DmEventsResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
-type CreateMessageRequest ballerinax/twitter:5.0.1:CreateTextMessageRequest|ballerinax/twitter:5.0.1:CreateAttachmentsMessageRequest;
+type CreateMessageRequest CreateTextMessageRequest|CreateAttachmentsMessageRequest;
 
 
 type TweetCreateResponse record {
     TweetCreateResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -2306,8 +2841,10 @@
 
 
 type TweetComplianceSchema record {
+    @jsondata:Name {value: "quote_tweet_id"}
     TweetId quoteTweetId?;
     # Event time
+    @jsondata:Name {value: "event_at"}
     string eventAt;
     TweetComplianceSchemaTweet tweet;
 };
@@ -2316,6 +2853,7 @@
 type TweetComplianceSchemaTweet record {
     # Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers
     TweetId id;
+    @jsondata:Name {value: "author_id"}
     UserId authorId;
 };
 
@@ -2323,34 +2861,49 @@
 
 type TweetsFullarchiveSearchQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length
+    @constraint:String {maxLength: 4096, minLength: 1}
     string query;
     # YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute)
+    @http:Query {name: "end_time"}
     string endTime?;
     # Returns results with a Post ID greater than (that is, more recent than) the specified ID
+    @http:Query {name: "since_id"}
     TweetId sinceId?;
     # This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified
+    @http:Query {name: "next_token"}
     PaginationToken36 nextToken?;
     # YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute)
+    @http:Query {name: "start_time"}
     string startTime?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified
+    @http:Query {name: "pagination_token"}
     PaginationToken36 paginationToken?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # The maximum number of search results to be returned by a request
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
     # This order in which to return results
+    @http:Query {name: "sort_order"}
     "recency"|"relevancy" sortOrder?;
     # Returns results with a Post ID less than (that is, older than) the specified ID
+    @http:Query {name: "until_id"}
     TweetId untilId?;
 };
 
@@ -2373,31 +2926,36 @@
 
 
 type TweetEditComplianceSchema record {
+    @jsondata:Name {value: "tweet_edit"}
     TweetEditComplianceObjectSchema tweetEdit;
 };
 
 # Tweet compliance data
-type TweetComplianceData ballerinax/twitter:5.0.1:TweetDeleteComplianceSchema|ballerinax/twitter:5.0.1:TweetWithheldComplianceSchema|ballerinax/twitter:5.0.1:TweetDropComplianceSchema|ballerinax/twitter:5.0.1:TweetUndropComplianceSchema|ballerinax/twitter:5.0.1:TweetEditComplianceSchema;
+type TweetComplianceData TweetDeleteComplianceSchema|TweetWithheldComplianceSchema|TweetDropComplianceSchema|TweetUndropComplianceSchema|TweetEditComplianceSchema;
 
 
 type TweetUnviewable record {
     # If the label is being applied or removed. Possible values are ‘apply’ or ‘remove’
     string application;
     # Event time
+    @jsondata:Name {value: "event_at"}
     string eventAt;
     TweetUnviewableTweet tweet;
 };
 
 
 type Get2UsersIdPinnedListsResponse record {
+    @constraint:Array {minLength: 1}
     List[] data?;
     Get2UsersIdPinnedListsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2UsersIdPinnedListsResponseMeta record {
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -2405,36 +2963,50 @@
 
 type UsersIdTweetsQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified
+    @http:Query {name: "end_time"}
     string endTime?;
     # The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified
+    @http:Query {name: "since_id"}
     TweetId sinceId?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified
+    @http:Query {name: "start_time"}
     string startTime?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get the next 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken36 paginationToken?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # The set of entities to exclude (e.g. 'replies' or 'retweets')
+    @constraint:Array {minLength: 1}
     ("replies"|"retweets")[] exclude?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
     # The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified
+    @http:Query {name: "until_id"}
     TweetId untilId?;
 };
 
 
 type ListDeleteResponse record {
     ListDeleteResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -2446,38 +3018,50 @@
 
 type TweetDeleteResponse record {
     TweetDeleteResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2UsersIdMentionsResponse record {
+    @constraint:Array {minLength: 1}
     Tweet[] data?;
     Get2UsersIdMentionsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2UsersIdMentionsResponseMeta record {
+    @jsondata:Name {value: "oldest_id"}
     OldestId oldestId?;
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "newest_id"}
     NewestId newestId?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
 
 type Get2ListsIdTweetsResponse record {
+    @constraint:Array {minLength: 1}
     Tweet[] data?;
     Get2ListsIdTweetsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type ListCreateRequest record {
     boolean 'private?;
+    @constraint:String {maxLength: 25, minLength: 1}
     string name;
+    @constraint:String {maxLength: 100}
     string description?;
 };
 
@@ -2485,20 +3069,26 @@
 type Get2DmEventsEventIdResponse record {
     DmEvent data?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2UsersResponse record {
+    @constraint:Array {minLength: 1}
     User[] data?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2UsersIdBlockingResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -2506,20 +3096,28 @@
 
 type ListsIdTweetsQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get the next 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken36 paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
@@ -2527,31 +3125,44 @@
 
 type GetTweetsSample10StreamQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # The number of minutes of backfill requested
-    ballerina/lang.int:0.0.0:Signed32 backfillMinutes?;
+    @http:Query {name: "backfill_minutes"}
+    int:Signed32 backfillMinutes?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "start_time"}
     string startTime?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # The partition number
-    ballerina/lang.int:0.0.0:Signed32 partition;
+    @constraint:Int {minValue: 1, maxValue: 2}
+    int:Signed32 partition;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "end_time"}
     string endTime?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
 
 type Get2SpacesIdTweetsResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -2559,33 +3170,40 @@
 type Get2SpacesIdResponse record {
     Space data?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type TweetUnviewableSchema record {
+    @jsondata:Name {value: "public_tweet_unviewable"}
     TweetUnviewable publicTweetUnviewable;
 };
 
 
 type TweetNoticeSchema record {
+    @jsondata:Name {value: "public_tweet_notice"}
     TweetNotice publicTweetNotice;
 };
 
 
 type TweetNotice record {
     # The type of label on the Tweet
+    @jsondata:Name {value: "event_type"}
     string eventType;
     # If the label is being applied or removed. Possible values are ‘apply’ or ‘remove’
     string application;
     # Title/header of the Tweet label
+    @jsondata:Name {value: "label_title"}
     string labelTitle?;
     # Information shown on the Tweet label
     string details?;
     # Event time
+    @jsondata:Name {value: "event_at"}
     string eventAt;
     TweetNoticeTweet tweet;
     # Link to more information about this kind of label
+    @jsondata:Name {value: "extended_details_url"}
     string extendedDetailsUrl?;
 };
 
@@ -2593,35 +3211,45 @@
 type TweetNoticeTweet record {
     # Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers
     TweetId id;
+    @jsondata:Name {value: "author_id"}
     UserId authorId;
 };
 
 # Tweet label data
-type TweetLabelData ballerinax/twitter:5.0.1:TweetNoticeSchema|ballerinax/twitter:5.0.1:TweetUnviewableSchema;
+type TweetLabelData TweetNoticeSchema|TweetUnviewableSchema;
 
 # Represents the Queries record for the operation: usersIdLikedTweets
 
 type UsersIdLikedTweetsQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get the next 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken36 paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -2667,33 +3295,42 @@
 
 type UsersFollowingCreateResponse record {
     UsersFollowingCreateResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type UsersFollowingCreateResponseData record {
     boolean following?;
+    @jsondata:Name {value: "pending_follow"}
     boolean pendingFollow?;
 };
 
 
 type CreateDmConversationRequest record {
     # The conversation type that is being created
+    @jsondata:Name {value: "conversation_type"}
     "Group" conversationType;
+    @jsondata:Name {value: "participant_ids"}
     DmParticipants participantIds;
     CreateMessageRequest message;
 };
 
-// Unknown type: DmParticipants
+# Participants for the DM Conversation
+@constraint:Array {maxLength: 49, minLength: 2}
+type DmParticipants UserId[];
 
 # Represents the Queries record for the operation: findUserById
 
 type FindUserByIdQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
@@ -2701,6 +3338,7 @@
 
 type ListBatchComplianceJobsQueries record {
     # A comma separated list of ComplianceJob fields to display
+    @http:Query {name: "compliance_job.fields"}
     ("created_at"|"download_expires_at"|"download_url"|"id"|"name"|"resumable"|"status"|"type"|"upload_expires_at"|"upload_url")[] complianceJobFields?;
     # Type of Compliance Job to list
     "tweets"|"users" 'type;
@@ -2712,6 +3350,7 @@
 type ListCreateResponse record {
     # A X List is a curated group of accounts
     ListCreateResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -2729,18 +3368,22 @@
     # The X User object
     User data?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type CreateDmEventResponse record {
     CreateDmEventResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type CreateDmEventResponseData record {
+    @jsondata:Name {value: "dm_conversation_id"}
     DmConversationId dmConversationId;
+    @jsondata:Name {value: "dm_event_id"}
     DmEventId dmEventId;
 };
 
@@ -2748,40 +3391,56 @@
 
 type TweetsRecentSearchQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length
+    @constraint:String {maxLength: 4096, minLength: 1}
     string query;
     # YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute)
+    @http:Query {name: "end_time"}
     string endTime?;
     # Returns results with a Post ID greater than (that is, more recent than) the specified ID
+    @http:Query {name: "since_id"}
     TweetId sinceId?;
     # This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified
+    @http:Query {name: "next_token"}
     PaginationToken36 nextToken?;
     # YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute)
+    @http:Query {name: "start_time"}
     string startTime?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified
+    @http:Query {name: "pagination_token"}
     PaginationToken36 paginationToken?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # The maximum number of search results to be returned by a request
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
     # This order in which to return results
+    @http:Query {name: "sort_order"}
     "recency"|"relevancy" sortOrder?;
     # Returns results with a Post ID less than (that is, older than) the specified ID
+    @http:Query {name: "until_id"}
     TweetId untilId?;
 };
 
 
 type UsersRetweetsCreateResponse record {
     UsersRetweetsCreateResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -2789,27 +3448,38 @@
 
 type GetDmEventsQueries record {
     # A comma separated list of DmEvent fields to display
+    @http:Query {name: "dm_event.fields"}
     ("attachments"|"created_at"|"dm_conversation_id"|"entities"|"event_type"|"id"|"participant_ids"|"referenced_tweets"|"sender_id"|"text")[] dmEventFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get a specified 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken32 paginationToken?;
     # The set of event_types to include in the results
+    @http:Query {name: "event_types"}
     ("MessageCreate"|"ParticipantsJoin"|"ParticipantsLeave")[] eventTypes?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"participant_ids"|"referenced_tweets.id"|"sender_id")[] expansions?;
 };
 
 
 type Get2ListsIdFollowersResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -2817,6 +3487,7 @@
 type Get2TweetsSearchStreamRulesCountsResponse record {
     # A count of user-provided stream filtering rules at the application and project levels
     RulesCount data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -2824,18 +3495,24 @@
 
 type RulesCount record {
     # Cap of number of rules allowed per project
-    ballerina/lang.int:0.0.0:Signed32 capPerProject?;
+    @jsondata:Name {value: "cap_per_project"}
+    int:Signed32 capPerProject?;
+    @jsondata:Name {value: "all_project_client_apps"}
     AllProjectClientApps allProjectClientApps?;
     # Number of rules for project
-    ballerina/lang.int:0.0.0:Signed32 projectRulesCount?;
+    @jsondata:Name {value: "project_rules_count"}
+    int:Signed32 projectRulesCount?;
     # Cap of number of rules allowed per client application
-    ballerina/lang.int:0.0.0:Signed32 capPerClientApp?;
+    @jsondata:Name {value: "cap_per_client_app"}
+    int:Signed32 capPerClientApp?;
+    @jsondata:Name {value: "client_app_rules_count"}
     AppRulesCount clientAppRulesCount?;
 };
 
 
 type UsersLikesDeleteResponse record {
     UsersLikesDeleteResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -2846,34 +3523,47 @@
 
 
 type Get2ListsIdFollowersResponse record {
+    @constraint:Array {minLength: 1}
     User[] data?;
     Get2ListsIdFollowersResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
-// Unknown type: UserIdMatchesAuthenticatedUser
+# Unique identifier of this User. The value must be the same as the authenticated user
+type UserIdMatchesAuthenticatedUser string;
 
 
 type Get2TweetsCountsAllResponse record {
+    @constraint:Array {minLength: 1}
     SearchCount[] data?;
     Get2TweetsCountsAllResponseMeta meta?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2TweetsSearchRecentResponseMeta record {
+    @jsondata:Name {value: "oldest_id"}
     OldestId oldestId?;
+    @jsondata:Name {value: "newest_id"}
     NewestId newestId?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
 
 type Get2TweetsSearchAllResponseMeta record {
+    @jsondata:Name {value: "oldest_id"}
     OldestId oldestId?;
+    @jsondata:Name {value: "newest_id"}
     NewestId newestId?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -2881,23 +3571,31 @@
 
 type TweetCreateRequestPoll record {
     # Duration of the poll in minutes
-    ballerina/lang.int:0.0.0:Signed32 durationMinutes;
+    @jsondata:Name {value: "duration_minutes"}
+    int:Signed32 durationMinutes;
+    @constraint:Array {maxLength: 4, minLength: 2}
     TweetCreateRequestPollOptionsItemsString[] options;
     # Settings to indicate who can reply to the Tweet
+    @jsondata:Name {value: "reply_settings"}
     "following"|"mentionedUsers" replySettings?;
 };
 
 
 type Get2UsersIdMutingResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
 
 type Get2UsersByResponse record {
+    @constraint:Array {minLength: 1}
     User[] data?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -2905,27 +3603,35 @@
 
 type TweetCreateRequestReply record {
     # A list of User Ids to be excluded from the reply Tweet
+    @jsondata:Name {value: "exclude_reply_user_ids"}
     UserId[] excludeReplyUserIds?;
+    @jsondata:Name {value: "in_reply_to_tweet_id"}
     TweetId inReplyToTweetId;
 };
 
 
 type Get2SpacesByCreatorIdsResponseMeta record {
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
 
 type Get2UsersIdFollowingResponse record {
+    @constraint:Array {minLength: 1}
     User[] data?;
     Get2UsersIdFollowingResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2UsersIdFollowingResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
@@ -2938,21 +3644,28 @@
 
 type SpaceBuyersQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get a specified 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken32 paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
 
 type Get2SpacesResponse record {
+    @constraint:Array {minLength: 1}
     Space[] data?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -2960,16 +3673,22 @@
 
 type FindTweetByIdQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
@@ -2977,24 +3696,34 @@
 
 type GetTweetsFirehoseStreamLangKoQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # The number of minutes of backfill requested
-    ballerina/lang.int:0.0.0:Signed32 backfillMinutes?;
+    @http:Query {name: "backfill_minutes"}
+    int:Signed32 backfillMinutes?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "start_time"}
     string startTime?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # The partition number
-    ballerina/lang.int:0.0.0:Signed32 partition;
+    @constraint:Int {minValue: 1, maxValue: 2}
+    int:Signed32 partition;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "end_time"}
     string endTime?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
@@ -3002,26 +3731,33 @@
 
 type GetUsageTweetsQueries record {
     # A comma separated list of Usage fields to display
+    @http:Query {name: "usage.fields"}
     ("cap_reset_day"|"daily_client_app_usage"|"daily_project_usage"|"project_cap"|"project_id"|"project_usage")[] usageFields?;
     # The number of days for which you need usage for
-    ballerina/lang.int:0.0.0:Signed32 days?;
+    @constraint:Int {minValue: 1, maxValue: 90}
+    int:Signed32 days?;
 };
 
 
 type Get2ComplianceJobsResponse record {
+    @constraint:Array {minLength: 1}
     ComplianceJob[] data?;
     Get2ComplianceJobsResponseMeta meta?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2ComplianceJobsResponseMeta record {
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
 
 type Get2TrendsByWoeidWoeidResponse record {
+    @constraint:Array {minLength: 1}
     Trend[] data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3029,18 +3765,25 @@
 
 type SpaceTweetsQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # The number of Posts to fetch from the provided space. If not provided, the value will default to the maximum of 100
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
@@ -3048,6 +3791,7 @@
 type StreamingTweetResponse record {
     Tweet data?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3055,6 +3799,7 @@
 type Get2TweetsIdResponse record {
     Tweet data?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3063,18 +3808,23 @@
     # A Like event, with the liking user and the tweet being liked
     Like data?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 # A Like event, with the liking user and the tweet being liked
 
 type Like record {
+    @jsondata:Name {value: "liked_tweet_id"}
     TweetId likedTweetId?;
     # Creation time of the Tweet
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "liking_user_id"}
     UserId likingUserId?;
     # Timestamp in milliseconds of creation
-    ballerina/lang.int:0.0.0:Signed32 timestampMs?;
+    @jsondata:Name {value: "timestamp_ms"}
+    int:Signed32 timestampMs?;
     # The unique identifier of this Like
     LikeId id?;
 };
@@ -3083,44 +3833,57 @@
 
 type GetDmConversationsWithParticipantIdDmEventsQueries record {
     # A comma separated list of DmEvent fields to display
+    @http:Query {name: "dm_event.fields"}
     ("attachments"|"created_at"|"dm_conversation_id"|"entities"|"event_type"|"id"|"participant_ids"|"referenced_tweets"|"sender_id"|"text")[] dmEventFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get a specified 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken32 paginationToken?;
     # The set of event_types to include in the results
+    @http:Query {name: "event_types"}
     ("MessageCreate"|"ParticipantsJoin"|"ParticipantsLeave")[] eventTypes?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"participant_ids"|"referenced_tweets.id"|"sender_id")[] expansions?;
 };
 
 # Tweet compliance stream events
-type TweetComplianceStreamResponse ballerinax/twitter:5.0.1:TweetComplianceStreamResponseOneOf1|ballerinax/twitter:5.0.1:TweetComplianceStreamResponseTweetComplianceStreamResponseOneOf12;
+type TweetComplianceStreamResponse TweetComplianceStreamResponseOneOf1|TweetComplianceStreamResponseTweetComplianceStreamResponseOneOf12;
 
 
 type Get2UsersIdBlockingResponse record {
+    @constraint:Array {minLength: 1}
     User[] data?;
     Get2UsersIdBlockingResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2TweetsIdLikingUsersResponse record {
+    @constraint:Array {minLength: 1}
     User[] data?;
     Get2TweetsIdLikingUsersResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type TweetLabelStreamResponseTweetLabelStreamResponseOneOf12 record {
+    @constraint:Array {minLength: 1}
     Problem[] errors;
 };
 
@@ -3128,22 +3891,31 @@
 
 type FindTweetsThatQuoteATweetQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get a specified 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken36 paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # The maximum number of results to be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # The set of entities to exclude (e.g. 'replies' or 'retweets')
+    @constraint:Array {minLength: 1}
     ("replies"|"retweets")[] exclude?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
@@ -3151,14 +3923,19 @@
 
 type ListGetMembersQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get a specified 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationTokenLong paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
@@ -3166,12 +3943,16 @@
 
 type GetUsersComplianceStreamQueries record {
     # The number of minutes of backfill requested
-    ballerina/lang.int:0.0.0:Signed32 backfillMinutes?;
+    @http:Query {name: "backfill_minutes"}
+    int:Signed32 backfillMinutes?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the User Compliance events will be provided
+    @http:Query {name: "start_time"}
     string startTime?;
     # The partition number
-    ballerina/lang.int:0.0.0:Signed32 partition;
+    @constraint:Int {minValue: 1, maxValue: 4}
+    int:Signed32 partition;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the User Compliance events will be provided
+    @http:Query {name: "end_time"}
     string endTime?;
 };
 
@@ -3180,6 +3961,7 @@
     # A X List is a curated group of accounts
     List data?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3187,22 +3969,29 @@
 
 type UserFollowedListsQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get a specified 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationTokenLong paginationToken?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of List fields to display
+    @http:Query {name: "list.fields"}
     ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     "owner_id"[] expansions?;
 };
 
 
 type Get2UsersIdTweetsResponse record {
+    @constraint:Array {minLength: 1}
     Tweet[] data?;
     Get2UsersIdTweetsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3211,12 +4000,14 @@
     # The X User object
     User data?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type MuteUserMutationResponse record {
     MuteUserMutationResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3227,6 +4018,7 @@
 
 
 type ListFollowedRequest record {
+    @jsondata:Name {value: "list_id"}
     ListId listId;
 };
 
@@ -3234,26 +4026,35 @@
 
 type LikesSample10StreamQueries record {
     # A comma separated list of Like fields to display
+    @http:Query {name: "like.fields"}
     ("created_at"|"id"|"liked_tweet_id"|"timestamp_ms")[] likeFields?;
     # The number of minutes of backfill requested
-    ballerina/lang.int:0.0.0:Signed32 backfillMinutes?;
+    @http:Query {name: "backfill_minutes"}
+    int:Signed32 backfillMinutes?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided
+    @http:Query {name: "start_time"}
     string startTime?;
     # The partition number
-    ballerina/lang.int:0.0.0:Signed32 partition;
+    @constraint:Int {minValue: 1, maxValue: 2}
+    int:Signed32 partition;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "end_time"}
     string endTime?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     "liked_tweet_id"[] expansions?;
 };
 
 
 type Get2SpacesIdTweetsResponse record {
+    @constraint:Array {minLength: 1}
     Tweet[] data?;
     Get2SpacesIdTweetsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3261,14 +4062,19 @@
 
 type UsersIdFollowersQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get a specified 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken32 paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
@@ -3276,16 +4082,20 @@
 
 type AddOrDeleteRulesQueries record {
     # Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes
+    @http:Query {name: "dry_run"}
     boolean dryRun?;
     # Delete All can be used to delete all of the rules associated this client app, it should be specified with no other parameters. Once deleted, rules cannot be recovered
+    @http:Query {name: "delete_all"}
     boolean deleteAll?;
 };
 
 
 type Get2TweetsIdRetweetedByResponse record {
+    @constraint:Array {minLength: 1}
     User[] data?;
     Get2TweetsIdRetweetedByResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3293,14 +4103,19 @@
 
 type UsersIdMutingQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get the next 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationTokenLong paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
@@ -3308,10 +4123,13 @@
 
 type GetTweetsLabelStreamQueries record {
     # The number of minutes of backfill requested
-    ballerina/lang.int:0.0.0:Signed32 backfillMinutes?;
+    @http:Query {name: "backfill_minutes"}
+    int:Signed32 backfillMinutes?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post labels will be provided
+    @http:Query {name: "start_time"}
     string startTime?;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Post labels will be provided
+    @http:Query {name: "end_time"}
     string endTime?;
 };
 
@@ -3322,11 +4140,15 @@
     # Nullcasted (promoted-only) Posts do not appear in the public timeline and are not served to followers
     boolean nullcast?;
     # Exclusive Tweet for super followers
+    @jsondata:Name {value: "for_super_followers_only"}
     boolean forSuperFollowersOnly?;
+    @jsondata:Name {value: "quote_tweet_id"}
     TweetId quoteTweetId?;
     # Link to take the conversation from the public timeline to a private Direct Message
+    @jsondata:Name {value: "direct_message_deep_link"}
     string directMessageDeepLink?;
     # Card Uri Parameter. This is mutually exclusive from Quote Tweet Id, Poll, Media, and Direct Message Deep Link
+    @jsondata:Name {value: "card_uri"}
     string cardUri?;
     # Media information being attached to created Tweet. This is mutually exclusive from Quote Tweet Id, Poll, and Card URI
     TweetCreateRequestMedia media?;
@@ -3337,36 +4159,44 @@
     # Tweet information of the Tweet being replied to
     TweetCreateRequestReply reply?;
     # Settings to indicate who can reply to the Tweet
+    @jsondata:Name {value: "reply_settings"}
     "following"|"mentionedUsers"|"subscribers" replySettings?;
 };
 
 
 type Get2UsersIdListMembershipsResponse record {
+    @constraint:Array {minLength: 1}
     List[] data?;
     Get2UsersIdListMembershipsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2SpacesSearchResponse record {
+    @constraint:Array {minLength: 1}
     Space[] data?;
     Get2SpacesSearchResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2TweetsSearchAllResponse record {
+    @constraint:Array {minLength: 1}
     Tweet[] data?;
     Get2TweetsSearchAllResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type ListMutateResponse record {
     ListMutateResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3374,18 +4204,25 @@
 
 type SampleStreamQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # The number of minutes of backfill requested
-    ballerina/lang.int:0.0.0:Signed32 backfillMinutes?;
+    @http:Query {name: "backfill_minutes"}
+    int:Signed32 backfillMinutes?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
@@ -3393,22 +4230,29 @@
 
 type TweetsIdRetweetingUsersQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get the next 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken36 paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
 
 type Get2TweetsSearchRecentResponse record {
+    @constraint:Array {minLength: 1}
     Tweet[] data?;
     Get2TweetsSearchRecentResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3416,6 +4260,7 @@
 
 type GetBatchComplianceJobQueries record {
     # A comma separated list of ComplianceJob fields to display
+    @http:Query {name: "compliance_job.fields"}
     ("created_at"|"download_expires_at"|"download_url"|"id"|"name"|"resumable"|"status"|"type"|"upload_expires_at"|"upload_url")[] complianceJobFields?;
 };
 
@@ -3423,33 +4268,45 @@
 
 type LikesFirehoseStreamQueries record {
     # A comma separated list of Like fields to display
+    @http:Query {name: "like.fields"}
     ("created_at"|"id"|"liked_tweet_id"|"timestamp_ms")[] likeFields?;
     # The number of minutes of backfill requested
-    ballerina/lang.int:0.0.0:Signed32 backfillMinutes?;
+    @http:Query {name: "backfill_minutes"}
+    int:Signed32 backfillMinutes?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided
+    @http:Query {name: "start_time"}
     string startTime?;
     # The partition number
-    ballerina/lang.int:0.0.0:Signed32 partition;
+    @constraint:Int {minValue: 1, maxValue: 20}
+    int:Signed32 partition;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "end_time"}
     string endTime?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     "liked_tweet_id"[] expansions?;
 };
 
 
 type Get2DmConversationsIdDmEventsResponseMeta record {
+    @jsondata:Name {value: "previous_token"}
     PreviousToken previousToken?;
+    @jsondata:Name {value: "next_token"}
     NextToken nextToken?;
+    @jsondata:Name {value: "result_count"}
     ResultCount resultCount?;
 };
 
 
 type Get2DmEventsResponse record {
+    @constraint:Array {minLength: 1}
     DmEvent[] data?;
     Get2DmEventsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3457,42 +4314,53 @@
 
 type FindSpacesByCreatorIdsQueries record {
     # A comma separated list of Space fields to display
+    @http:Query {name: "space.fields"}
     ("created_at"|"creator_id"|"ended_at"|"host_ids"|"id"|"invited_user_ids"|"is_ticketed"|"lang"|"participant_count"|"scheduled_start"|"speaker_ids"|"started_at"|"state"|"subscriber_count"|"title"|"topic_ids"|"updated_at")[] spaceFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # The IDs of Users to search through
+    @http:Query {name: "user_ids"}
     UserId[] userIds;
     # A comma separated list of Topic fields to display
+    @http:Query {name: "topic.fields"}
     ("description"|"id"|"name")[] topicFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("creator_id"|"host_ids"|"invited_user_ids"|"speaker_ids"|"topic_ids")[] expansions?;
 };
 
 
 type Get2UsersIdBookmarksResponse record {
+    @constraint:Array {minLength: 1}
     Tweet[] data?;
     Get2UsersIdBookmarksResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2SpacesByCreatorIdsResponse record {
+    @constraint:Array {minLength: 1}
     Space[] data?;
     Get2SpacesByCreatorIdsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type CreateComplianceJobResponse record {
     ComplianceJob data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type UsersRetweetsDeleteResponse record {
     UsersRetweetsDeleteResponseData data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3500,20 +4368,26 @@
 
 type FindSpacesByIdsQueries record {
     # A comma separated list of Space fields to display
+    @http:Query {name: "space.fields"}
     ("created_at"|"creator_id"|"ended_at"|"host_ids"|"id"|"invited_user_ids"|"is_ticketed"|"lang"|"participant_count"|"scheduled_start"|"speaker_ids"|"started_at"|"state"|"subscriber_count"|"title"|"topic_ids"|"updated_at")[] spaceFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # The list of Space IDs to return
+    @constraint:Array {maxLength: 100, minLength: 1}
     FindSpacesByIdsQueriesIdsItemsString[] ids;
     # A comma separated list of Topic fields to display
+    @http:Query {name: "topic.fields"}
     ("description"|"id"|"name")[] topicFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("creator_id"|"host_ids"|"invited_user_ids"|"speaker_ids"|"topic_ids")[] expansions?;
 };
 
 
 type Get2ComplianceJobsIdResponse record {
     ComplianceJob data?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3522,6 +4396,7 @@
     # The X User object
     User data?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3529,10 +4404,13 @@
 
 type GetLikesComplianceStreamQueries record {
     # The number of minutes of backfill requested
-    ballerina/lang.int:0.0.0:Signed32 backfillMinutes?;
+    @http:Query {name: "backfill_minutes"}
+    int:Signed32 backfillMinutes?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Likes Compliance events will be provided
+    @http:Query {name: "start_time"}
     string startTime?;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Likes Compliance events will be provided
+    @http:Query {name: "end_time"}
     string endTime?;
 };
 
@@ -3544,7 +4422,7 @@
 };
 
 # Tweet label stream events
-type TweetLabelStreamResponse ballerinax/twitter:5.0.1:TweetLabelStreamResponseOneOf1|ballerinax/twitter:5.0.1:TweetLabelStreamResponseTweetLabelStreamResponseOneOf12;
+type TweetLabelStreamResponse TweetLabelStreamResponseOneOf1|TweetLabelStreamResponseTweetLabelStreamResponseOneOf12;
 
 # A Tweet or error that can be returned by the streaming Tweet API. The values returned with a successful streamed Tweet includes the user provided rules that the Tweet matched
 
@@ -3552,15 +4430,19 @@
     Tweet data?;
     Expansions includes?;
     # The list of rules which matched the Tweet
+    @jsondata:Name {value: "matching_rules"}
     FilteredStreamingTweetResponseMatchingRules[] matchingRules?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
 
 type Get2UsersIdMutingResponse record {
+    @constraint:Array {minLength: 1}
     User[] data?;
     Get2UsersIdMutingResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3568,22 +4450,29 @@
 
 type UsersIdFollowingQueries record {
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get a specified 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken32 paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions?;
 };
 
 
 type Get2DmConversationsIdDmEventsResponse record {
+    @constraint:Array {minLength: 1}
     DmEvent[] data?;
     Get2DmConversationsIdDmEventsResponseMeta meta?;
     Expansions includes?;
+    @constraint:Array {minLength: 1}
     Problem[] errors?;
 };
 
@@ -3591,24 +4480,34 @@
 
 type GetTweetsFirehoseStreamQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # The number of minutes of backfill requested
-    ballerina/lang.int:0.0.0:Signed32 backfillMinutes?;
+    @http:Query {name: "backfill_minutes"}
+    int:Signed32 backfillMinutes?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "start_time"}
     string startTime?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # The partition number
-    ballerina/lang.int:0.0.0:Signed32 partition;
+    @constraint:Int {minValue: 1, maxValue: 20}
+    int:Signed32 partition;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided
+    @http:Query {name: "end_time"}
     string endTime?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
@@ -3616,25 +4515,34 @@
 
 type GetUsersIdBookmarksQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get the next 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken36 paginationToken?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
 };
 
 
 type UsersLikesCreateRequest record {
+    @jsondata:Name {value: "tweet_id"}
     TweetId tweetId;
 };
 
@@ -3642,30 +4550,42 @@
 
 type UsersIdTimelineQueries record {
     # A comma separated list of Poll fields to display
+    @http:Query {name: "poll.fields"}
     ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields?;
     # A comma separated list of Tweet fields to display
+    @http:Query {name: "tweet.fields"}
     ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields?;
     # YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified
+    @http:Query {name: "end_time"}
     string endTime?;
     # The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified
+    @http:Query {name: "since_id"}
     TweetId sinceId?;
     # YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified
+    @http:Query {name: "start_time"}
     string startTime?;
     # A comma separated list of User fields to display
+    @http:Query {name: "user.fields"}
     ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields?;
     # This parameter is used to get the next 'page' of results
+    @http:Query {name: "pagination_token"}
     PaginationToken36 paginationToken?;
     # A comma separated list of Media fields to display
+    @http:Query {name: "media.fields"}
     ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields?;
     # The maximum number of results
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @http:Query {name: "max_results"}
+    int:Signed32 maxResults?;
     # A comma separated list of Place fields to display
+    @http:Query {name: "place.fields"}
     ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields?;
     # The set of entities to exclude (e.g. 'replies' or 'retweets')
     ("replies"|"retweets")[] exclude?;
     # A comma separated list of fields to expand
+    @constraint:Array {minLength: 1}
     ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions?;
     # The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified
+    @http:Query {name: "until_id"}
     TweetId untilId?;
 };
 
@@ -3677,7 +4597,7 @@
 
     # List Compliance Jobs
     # 
-    resource function get compliance/jobs(map<string|string[]> headers = {}, ("created_at"|"download_expires_at"|"download_url"|"id"|"name"|"resumable"|"status"|"type"|"upload_expires_at"|"upload_url")[] complianceJobFields = [], "tweets"|"users" type = "tweets", "created"|"in_progress"|"failed"|"complete" status = "created", anydata Additional Values, ListBatchComplianceJobsQueries queries) returns Get2ComplianceJobsResponse|error;
+    resource function get compliance/jobs(map<string|string[]> headers = {}, ("created_at"|"download_expires_at"|"download_url"|"id"|"name"|"resumable"|"status"|"type"|"upload_expires_at"|"upload_url")[] complianceJobFields = [], "tweets"|"users" type = "tweets", "created"|"in_progress"|"failed"|"complete" status = "created", ListBatchComplianceJobsQueries queries) returns Get2ComplianceJobsResponse|error;
 
     # Create compliance job
     # 
@@ -3685,7 +4605,7 @@
 
     # Get Compliance Job
     # 
-    resource function get compliance/jobs/[twitter:JobId id](map<string|string[]> headers = {}, ("created_at"|"download_expires_at"|"download_url"|"id"|"name"|"resumable"|"status"|"type"|"upload_expires_at"|"upload_url")[] complianceJobFields = [], anydata Additional Values, GetBatchComplianceJobQueries queries) returns Get2ComplianceJobsIdResponse|error;
+    resource function get compliance/jobs/[twitter:JobId id](map<string|string[]> headers = {}, ("created_at"|"download_expires_at"|"download_url"|"id"|"name"|"resumable"|"status"|"type"|"upload_expires_at"|"upload_url")[] complianceJobFields = [], GetBatchComplianceJobQueries queries) returns Get2ComplianceJobsIdResponse|error;
 
     # Create a new DM Conversation
     # 
@@ -3693,7 +4613,7 @@
 
     # Get DM Events for a DM Conversation
     # 
-    resource function get dm_conversations/with/[twitter:UserId participantId]/dm_events(map<string|string[]> headers = {}, ("attachments"|"created_at"|"dm_conversation_id"|"entities"|"event_type"|"id"|"participant_ids"|"referenced_tweets"|"sender_id"|"text")[] dmEventFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken32 paginationToken = "", ("MessageCreate"|"ParticipantsJoin"|"ParticipantsLeave")[] eventTypes = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("attachments.media_keys"|"participant_ids"|"referenced_tweets.id"|"sender_id")[] expansions = [], anydata Additional Values, GetDmConversationsWithParticipantIdDmEventsQueries queries) returns Get2DmConversationsWithParticipantIdDmEventsResponse|error;
+    resource function get dm_conversations/with/[twitter:UserId participantId]/dm_events(map<string|string[]> headers = {}, ("attachments"|"created_at"|"dm_conversation_id"|"entities"|"event_type"|"id"|"participant_ids"|"referenced_tweets"|"sender_id"|"text")[] dmEventFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken32 paginationToken = "", ("MessageCreate"|"ParticipantsJoin"|"ParticipantsLeave")[] eventTypes = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("attachments.media_keys"|"participant_ids"|"referenced_tweets.id"|"sender_id")[] expansions = [], GetDmConversationsWithParticipantIdDmEventsQueries queries) returns Get2DmConversationsWithParticipantIdDmEventsResponse|error;
 
     # Send a new message to a user
     # 
@@ -3705,15 +4625,15 @@
 
     # Get DM Events for a DM Conversation
     # 
-    resource function get dm_conversations/[twitter:DmConversationId id]/dm_events(map<string|string[]> headers = {}, ("attachments"|"created_at"|"dm_conversation_id"|"entities"|"event_type"|"id"|"participant_ids"|"referenced_tweets"|"sender_id"|"text")[] dmEventFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken32 paginationToken = "", ("MessageCreate"|"ParticipantsJoin"|"ParticipantsLeave")[] eventTypes = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("attachments.media_keys"|"participant_ids"|"referenced_tweets.id"|"sender_id")[] expansions = [], anydata Additional Values, GetDmConversationsIdDmEventsQueries queries) returns Get2DmConversationsIdDmEventsResponse|error;
+    resource function get dm_conversations/[twitter:DmConversationId id]/dm_events(map<string|string[]> headers = {}, ("attachments"|"created_at"|"dm_conversation_id"|"entities"|"event_type"|"id"|"participant_ids"|"referenced_tweets"|"sender_id"|"text")[] dmEventFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken32 paginationToken = "", ("MessageCreate"|"ParticipantsJoin"|"ParticipantsLeave")[] eventTypes = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("attachments.media_keys"|"participant_ids"|"referenced_tweets.id"|"sender_id")[] expansions = [], GetDmConversationsIdDmEventsQueries queries) returns Get2DmConversationsIdDmEventsResponse|error;
 
     # Get recent DM Events
     # 
-    resource function get dm_events(map<string|string[]> headers = {}, ("attachments"|"created_at"|"dm_conversation_id"|"entities"|"event_type"|"id"|"participant_ids"|"referenced_tweets"|"sender_id"|"text")[] dmEventFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken32 paginationToken = "", ("MessageCreate"|"ParticipantsJoin"|"ParticipantsLeave")[] eventTypes = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("attachments.media_keys"|"participant_ids"|"referenced_tweets.id"|"sender_id")[] expansions = [], anydata Additional Values, GetDmEventsQueries queries) returns Get2DmEventsResponse|error;
+    resource function get dm_events(map<string|string[]> headers = {}, ("attachments"|"created_at"|"dm_conversation_id"|"entities"|"event_type"|"id"|"participant_ids"|"referenced_tweets"|"sender_id"|"text")[] dmEventFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken32 paginationToken = "", ("MessageCreate"|"ParticipantsJoin"|"ParticipantsLeave")[] eventTypes = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("attachments.media_keys"|"participant_ids"|"referenced_tweets.id"|"sender_id")[] expansions = [], GetDmEventsQueries queries) returns Get2DmEventsResponse|error;
 
     # Get DM Events by id
     # 
-    resource function get dm_events/[twitter:DmEventId eventId](map<string|string[]> headers = {}, ("attachments"|"created_at"|"dm_conversation_id"|"entities"|"event_type"|"id"|"participant_ids"|"referenced_tweets"|"sender_id"|"text")[] dmEventFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], ("attachments.media_keys"|"participant_ids"|"referenced_tweets.id"|"sender_id")[] expansions = [], anydata Additional Values, GetDmEventsByIdQueries queries) returns Get2DmEventsEventIdResponse|error;
+    resource function get dm_events/[twitter:DmEventId eventId](map<string|string[]> headers = {}, ("attachments"|"created_at"|"dm_conversation_id"|"entities"|"event_type"|"id"|"participant_ids"|"referenced_tweets"|"sender_id"|"text")[] dmEventFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], ("attachments.media_keys"|"participant_ids"|"referenced_tweets.id"|"sender_id")[] expansions = [], GetDmEventsByIdQueries queries) returns Get2DmEventsEventIdResponse|error;
 
     # Delete Dm
     # 
@@ -3721,15 +4641,15 @@
 
     # Likes Compliance stream
     # 
-    resource function get likes/compliance/'stream(map<string|string[]> headers = {}, int:Signed32 backfillMinutes = 0, string startTime = "", string endTime = "", anydata Additional Values, GetLikesComplianceStreamQueries queries) returns LikesComplianceStreamResponseOneOf1|LikesComplianceStreamResponseLikesComplianceStreamResponseOneOf12|error;
+    resource function get likes/compliance/'stream(map<string|string[]> headers = {}, int:Signed32 backfillMinutes = 0, string startTime = "", string endTime = "", GetLikesComplianceStreamQueries queries) returns LikesComplianceStreamResponseOneOf1|LikesComplianceStreamResponseLikesComplianceStreamResponseOneOf12|error;
 
     # Likes Firehose stream
     # 
-    resource function get likes/firehose/'stream(map<string|string[]> headers = {}, ("created_at"|"id"|"liked_tweet_id"|"timestamp_ms")[] likeFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], string endTime = "", "liked_tweet_id"[] expansions = [], anydata Additional Values, LikesFirehoseStreamQueries queries) returns StreamingLikeResponse|error;
+    resource function get likes/firehose/'stream(map<string|string[]> headers = {}, ("created_at"|"id"|"liked_tweet_id"|"timestamp_ms")[] likeFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], string endTime = "", "liked_tweet_id"[] expansions = [], LikesFirehoseStreamQueries queries) returns StreamingLikeResponse|error;
 
     # Likes Sample 10 stream
     # 
-    resource function get likes/sample10/'stream(map<string|string[]> headers = {}, ("created_at"|"id"|"liked_tweet_id"|"timestamp_ms")[] likeFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], string endTime = "", "liked_tweet_id"[] expansions = [], anydata Additional Values, LikesSample10StreamQueries queries) returns StreamingLikeResponse|error;
+    resource function get likes/sample10/'stream(map<string|string[]> headers = {}, ("created_at"|"id"|"liked_tweet_id"|"timestamp_ms")[] likeFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], string endTime = "", "liked_tweet_id"[] expansions = [], LikesSample10StreamQueries queries) returns StreamingLikeResponse|error;
 
     # Create List
     # 
@@ -3737,7 +4657,7 @@
 
     # List lookup by List ID.
     # 
-    resource function get lists/[twitter:ListId id](map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields = [], "owner_id"[] expansions = [], anydata Additional Values, ListIdGetQueries queries) returns Get2ListsIdResponse|error;
+    resource function get lists/[twitter:ListId id](map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields = [], "owner_id"[] expansions = [], ListIdGetQueries queries) returns Get2ListsIdResponse|error;
 
     # Update List.
     # 
@@ -3749,11 +4669,11 @@
 
     # Returns User objects that follow a List by the provided List ID
     # 
-    resource function get lists/[twitter:ListId id]/followers(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationTokenLong paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, ListGetFollowersQueries queries) returns Get2ListsIdFollowersResponse|error;
+    resource function get lists/[twitter:ListId id]/followers(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationTokenLong paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], ListGetFollowersQueries queries) returns Get2ListsIdFollowersResponse|error;
 
     # Returns User objects that are members of a List by the provided List ID.
     # 
-    resource function get lists/[twitter:ListId id]/members(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationTokenLong paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, ListGetMembersQueries queries) returns Get2ListsIdMembersResponse|error;
+    resource function get lists/[twitter:ListId id]/members(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationTokenLong paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], ListGetMembersQueries queries) returns Get2ListsIdMembersResponse|error;
 
     # Add a List member
     # 
@@ -3765,7 +4685,7 @@
 
     # List Posts timeline by List ID.
     # 
-    resource function get lists/[twitter:ListId id]/tweets(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, ListsIdTweetsQueries queries) returns Get2ListsIdTweetsResponse|error;
+    resource function get lists/[twitter:ListId id]/tweets(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], ListsIdTweetsQueries queries) returns Get2ListsIdTweetsResponse|error;
 
     # Returns the OpenAPI Specification document.
     # 
@@ -3773,35 +4693,35 @@
 
     # Space lookup up Space IDs
     # 
-    resource function get spaces(map<string|string[]> headers = {}, ("created_at"|"creator_id"|"ended_at"|"host_ids"|"id"|"invited_user_ids"|"is_ticketed"|"lang"|"participant_count"|"scheduled_start"|"speaker_ids"|"started_at"|"state"|"subscriber_count"|"title"|"topic_ids"|"updated_at")[] spaceFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], FindSpacesByIdsQueriesIdsItemsString[] ids = [], ("description"|"id"|"name")[] topicFields = [], ("creator_id"|"host_ids"|"invited_user_ids"|"speaker_ids"|"topic_ids")[] expansions = [], anydata Additional Values, FindSpacesByIdsQueries queries) returns Get2SpacesResponse|error;
+    resource function get spaces(map<string|string[]> headers = {}, ("created_at"|"creator_id"|"ended_at"|"host_ids"|"id"|"invited_user_ids"|"is_ticketed"|"lang"|"participant_count"|"scheduled_start"|"speaker_ids"|"started_at"|"state"|"subscriber_count"|"title"|"topic_ids"|"updated_at")[] spaceFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], FindSpacesByIdsQueriesIdsItemsString[] ids = [], ("description"|"id"|"name")[] topicFields = [], ("creator_id"|"host_ids"|"invited_user_ids"|"speaker_ids"|"topic_ids")[] expansions = [], FindSpacesByIdsQueries queries) returns Get2SpacesResponse|error;
 
     # Space lookup by their creators
     # 
-    resource function get spaces/'by/creator_ids(map<string|string[]> headers = {}, ("created_at"|"creator_id"|"ended_at"|"host_ids"|"id"|"invited_user_ids"|"is_ticketed"|"lang"|"participant_count"|"scheduled_start"|"speaker_ids"|"started_at"|"state"|"subscriber_count"|"title"|"topic_ids"|"updated_at")[] spaceFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], UserId[] userIds = [], ("description"|"id"|"name")[] topicFields = [], ("creator_id"|"host_ids"|"invited_user_ids"|"speaker_ids"|"topic_ids")[] expansions = [], anydata Additional Values, FindSpacesByCreatorIdsQueries queries) returns Get2SpacesByCreatorIdsResponse|error;
+    resource function get spaces/'by/creator_ids(map<string|string[]> headers = {}, ("created_at"|"creator_id"|"ended_at"|"host_ids"|"id"|"invited_user_ids"|"is_ticketed"|"lang"|"participant_count"|"scheduled_start"|"speaker_ids"|"started_at"|"state"|"subscriber_count"|"title"|"topic_ids"|"updated_at")[] spaceFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], UserId[] userIds = [], ("description"|"id"|"name")[] topicFields = [], ("creator_id"|"host_ids"|"invited_user_ids"|"speaker_ids"|"topic_ids")[] expansions = [], FindSpacesByCreatorIdsQueries queries) returns Get2SpacesByCreatorIdsResponse|error;
 
     # Search for Spaces
     # 
-    resource function get spaces/search(map<string|string[]> headers = {}, ("created_at"|"creator_id"|"ended_at"|"host_ids"|"id"|"invited_user_ids"|"is_ticketed"|"lang"|"participant_count"|"scheduled_start"|"speaker_ids"|"started_at"|"state"|"subscriber_count"|"title"|"topic_ids"|"updated_at")[] spaceFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], string query = "", int:Signed32 maxResults = 0, "live"|"scheduled"|"all" state = "live", ("description"|"id"|"name")[] topicFields = [], ("creator_id"|"host_ids"|"invited_user_ids"|"speaker_ids"|"topic_ids")[] expansions = [], anydata Additional Values, SearchSpacesQueries queries) returns Get2SpacesSearchResponse|error;
+    resource function get spaces/search(map<string|string[]> headers = {}, ("created_at"|"creator_id"|"ended_at"|"host_ids"|"id"|"invited_user_ids"|"is_ticketed"|"lang"|"participant_count"|"scheduled_start"|"speaker_ids"|"started_at"|"state"|"subscriber_count"|"title"|"topic_ids"|"updated_at")[] spaceFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], string query = "", int:Signed32 maxResults = 0, "live"|"scheduled"|"all" state = "live", ("description"|"id"|"name")[] topicFields = [], ("creator_id"|"host_ids"|"invited_user_ids"|"speaker_ids"|"topic_ids")[] expansions = [], SearchSpacesQueries queries) returns Get2SpacesSearchResponse|error;
 
     # Space lookup by Space ID
     # 
-    resource function get spaces/[string id](map<string|string[]> headers = {}, ("created_at"|"creator_id"|"ended_at"|"host_ids"|"id"|"invited_user_ids"|"is_ticketed"|"lang"|"participant_count"|"scheduled_start"|"speaker_ids"|"started_at"|"state"|"subscriber_count"|"title"|"topic_ids"|"updated_at")[] spaceFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("description"|"id"|"name")[] topicFields = [], ("creator_id"|"host_ids"|"invited_user_ids"|"speaker_ids"|"topic_ids")[] expansions = [], anydata Additional Values, FindSpaceByIdQueries queries) returns Get2SpacesIdResponse|error;
+    resource function get spaces/[string id](map<string|string[]> headers = {}, ("created_at"|"creator_id"|"ended_at"|"host_ids"|"id"|"invited_user_ids"|"is_ticketed"|"lang"|"participant_count"|"scheduled_start"|"speaker_ids"|"started_at"|"state"|"subscriber_count"|"title"|"topic_ids"|"updated_at")[] spaceFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("description"|"id"|"name")[] topicFields = [], ("creator_id"|"host_ids"|"invited_user_ids"|"speaker_ids"|"topic_ids")[] expansions = [], FindSpaceByIdQueries queries) returns Get2SpacesIdResponse|error;
 
     # Retrieve the list of Users who purchased a ticket to the given space
     # 
-    resource function get spaces/[string id]/buyers(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken32 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, SpaceBuyersQueries queries) returns Get2SpacesIdBuyersResponse|error;
+    resource function get spaces/[string id]/buyers(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken32 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], SpaceBuyersQueries queries) returns Get2SpacesIdBuyersResponse|error;
 
     # Retrieve Posts from a Space.
     # 
-    resource function get spaces/[string id]/tweets(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, SpaceTweetsQueries queries) returns Get2SpacesIdTweetsResponse|error;
+    resource function get spaces/[string id]/tweets(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], SpaceTweetsQueries queries) returns Get2SpacesIdTweetsResponse|error;
 
     # Trends
     # 
-    resource function get trends/'by/woeid/[int:Signed32 woeid](map<string|string[]> headers = {}, ("trend_name"|"tweet_count")[] trendFields = [], anydata Additional Values, GetTrendsQueries queries) returns Get2TrendsByWoeidWoeidResponse|error;
+    resource function get trends/'by/woeid/[int:Signed32 woeid](map<string|string[]> headers = {}, ("trend_name"|"tweet_count")[] trendFields = [], GetTrendsQueries queries) returns Get2TrendsByWoeidWoeidResponse|error;
 
     # Post lookup by Post IDs
     # 
-    resource function get tweets(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], TweetId[] ids = [], ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, FindTweetsByIdQueries queries) returns Get2TweetsResponse|error;
+    resource function get tweets(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], TweetId[] ids = [], ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], FindTweetsByIdQueries queries) returns Get2TweetsResponse|error;
 
     # Creation of a Post
     # 
@@ -3809,75 +4729,75 @@
 
     # Posts Compliance stream
     # 
-    resource function get tweets/compliance/'stream(map<string|string[]> headers = {}, int:Signed32 backfillMinutes = 0, string startTime = "", int:Signed32 partition = 0, string endTime = "", anydata Additional Values, GetTweetsComplianceStreamQueries queries) returns TweetComplianceStreamResponseOneOf1|TweetComplianceStreamResponseTweetComplianceStreamResponseOneOf12|error;
+    resource function get tweets/compliance/'stream(map<string|string[]> headers = {}, int:Signed32 backfillMinutes = 0, string startTime = "", int:Signed32 partition = 0, string endTime = "", GetTweetsComplianceStreamQueries queries) returns TweetComplianceStreamResponseOneOf1|TweetComplianceStreamResponseTweetComplianceStreamResponseOneOf12|error;
 
     # Full archive search counts
     # 
-    resource function get tweets/counts/all(map<string|string[]> headers = {}, string startTime = "", ("end"|"start"|"tweet_count")[] searchCountFields = [], PaginationToken36 paginationToken = "", "minute"|"hour"|"day" granularity = "minute", string query = "", string endTime = "", TweetId sinceId = "", PaginationToken36 nextToken = "", TweetId untilId = "", anydata Additional Values, TweetCountsFullArchiveSearchQueries queries) returns Get2TweetsCountsAllResponse|error;
+    resource function get tweets/counts/all(map<string|string[]> headers = {}, string startTime = "", ("end"|"start"|"tweet_count")[] searchCountFields = [], PaginationToken36 paginationToken = "", "minute"|"hour"|"day" granularity = "minute", string query = "", string endTime = "", TweetId sinceId = "", PaginationToken36 nextToken = "", TweetId untilId = "", TweetCountsFullArchiveSearchQueries queries) returns Get2TweetsCountsAllResponse|error;
 
     # Recent search counts
     # 
-    resource function get tweets/counts/recent(map<string|string[]> headers = {}, string startTime = "", ("end"|"start"|"tweet_count")[] searchCountFields = [], PaginationToken36 paginationToken = "", "minute"|"hour"|"day" granularity = "minute", string query = "", string endTime = "", TweetId sinceId = "", PaginationToken36 nextToken = "", TweetId untilId = "", anydata Additional Values, TweetCountsRecentSearchQueries queries) returns Get2TweetsCountsRecentResponse|error;
+    resource function get tweets/counts/recent(map<string|string[]> headers = {}, string startTime = "", ("end"|"start"|"tweet_count")[] searchCountFields = [], PaginationToken36 paginationToken = "", "minute"|"hour"|"day" granularity = "minute", string query = "", string endTime = "", TweetId sinceId = "", PaginationToken36 nextToken = "", TweetId untilId = "", TweetCountsRecentSearchQueries queries) returns Get2TweetsCountsRecentResponse|error;
 
     # Firehose stream
     # 
-    resource function get tweets/firehose/'stream(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, GetTweetsFirehoseStreamQueries queries) returns StreamingTweetResponse|error;
+    resource function get tweets/firehose/'stream(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], GetTweetsFirehoseStreamQueries queries) returns StreamingTweetResponse|error;
 
     # English Language Firehose stream
     # 
-    resource function get tweets/firehose/'stream/lang/en(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, GetTweetsFirehoseStreamLangEnQueries queries) returns StreamingTweetResponse|error;
+    resource function get tweets/firehose/'stream/lang/en(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], GetTweetsFirehoseStreamLangEnQueries queries) returns StreamingTweetResponse|error;
 
     # Japanese Language Firehose stream
     # 
-    resource function get tweets/firehose/'stream/lang/ja(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, GetTweetsFirehoseStreamLangJaQueries queries) returns StreamingTweetResponse|error;
+    resource function get tweets/firehose/'stream/lang/ja(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], GetTweetsFirehoseStreamLangJaQueries queries) returns StreamingTweetResponse|error;
 
     # Korean Language Firehose stream
     # 
-    resource function get tweets/firehose/'stream/lang/ko(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, GetTweetsFirehoseStreamLangKoQueries queries) returns StreamingTweetResponse|error;
+    resource function get tweets/firehose/'stream/lang/ko(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], GetTweetsFirehoseStreamLangKoQueries queries) returns StreamingTweetResponse|error;
 
     # Portuguese Language Firehose stream
     # 
-    resource function get tweets/firehose/'stream/lang/pt(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, GetTweetsFirehoseStreamLangPtQueries queries) returns StreamingTweetResponse|error;
+    resource function get tweets/firehose/'stream/lang/pt(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], GetTweetsFirehoseStreamLangPtQueries queries) returns StreamingTweetResponse|error;
 
     # Posts Label stream
     # 
-    resource function get tweets/label/'stream(map<string|string[]> headers = {}, int:Signed32 backfillMinutes = 0, string startTime = "", string endTime = "", anydata Additional Values, GetTweetsLabelStreamQueries queries) returns TweetLabelStreamResponseOneOf1|TweetLabelStreamResponseTweetLabelStreamResponseOneOf12|error;
+    resource function get tweets/label/'stream(map<string|string[]> headers = {}, int:Signed32 backfillMinutes = 0, string startTime = "", string endTime = "", GetTweetsLabelStreamQueries queries) returns TweetLabelStreamResponseOneOf1|TweetLabelStreamResponseTweetLabelStreamResponseOneOf12|error;
 
     # Sample stream
     # 
-    resource function get tweets/sample/'stream(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, SampleStreamQueries queries) returns StreamingTweetResponse|error;
+    resource function get tweets/sample/'stream(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], SampleStreamQueries queries) returns StreamingTweetResponse|error;
 
     # Sample 10% stream
     # 
-    resource function get tweets/sample10/'stream(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, GetTweetsSample10StreamQueries queries) returns Get2TweetsSample10StreamResponse|error;
+    resource function get tweets/sample10/'stream(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], int:Signed32 partition = 0, ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], GetTweetsSample10StreamQueries queries) returns Get2TweetsSample10StreamResponse|error;
 
     # Full-archive search
     # 
-    resource function get tweets/search/all(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], string query = "", string endTime = "", TweetId sinceId = "", PaginationToken36 nextToken = "", string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], "recency"|"relevancy" sortOrder = "recency", TweetId untilId = "", anydata Additional Values, TweetsFullarchiveSearchQueries queries) returns Get2TweetsSearchAllResponse|error;
+    resource function get tweets/search/all(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], string query = "", string endTime = "", TweetId sinceId = "", PaginationToken36 nextToken = "", string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], "recency"|"relevancy" sortOrder = "recency", TweetId untilId = "", TweetsFullarchiveSearchQueries queries) returns Get2TweetsSearchAllResponse|error;
 
     # Recent search
     # 
-    resource function get tweets/search/recent(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], string query = "", string endTime = "", TweetId sinceId = "", PaginationToken36 nextToken = "", string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], "recency"|"relevancy" sortOrder = "recency", TweetId untilId = "", anydata Additional Values, TweetsRecentSearchQueries queries) returns Get2TweetsSearchRecentResponse|error;
+    resource function get tweets/search/recent(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], string query = "", string endTime = "", TweetId sinceId = "", PaginationToken36 nextToken = "", string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], "recency"|"relevancy" sortOrder = "recency", TweetId untilId = "", TweetsRecentSearchQueries queries) returns Get2TweetsSearchRecentResponse|error;
 
     # Filtered stream
     # 
-    resource function get tweets/search/'stream(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, SearchStreamQueries queries) returns FilteredStreamingTweetResponse|error;
+    resource function get tweets/search/'stream(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], int:Signed32 backfillMinutes = 0, string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], SearchStreamQueries queries) returns FilteredStreamingTweetResponse|error;
 
     # Rules lookup
     # 
-    resource function get tweets/search/'stream/rules(map<string|string[]> headers = {}, string paginationToken = "", RuleId[] ids = [], int:Signed32 maxResults = 0, anydata Additional Values, GetRulesQueries queries) returns RulesLookupResponse|error;
+    resource function get tweets/search/'stream/rules(map<string|string[]> headers = {}, string paginationToken = "", RuleId[] ids = [], int:Signed32 maxResults = 0, GetRulesQueries queries) returns RulesLookupResponse|error;
 
     # Add/Delete rules
     # 
-    resource function post tweets/search/'stream/rules(AddOrDeleteRulesRequest payload, map<string|string[]> headers = {}, boolean dryRun = false, boolean deleteAll = false, anydata Additional Values, AddOrDeleteRulesQueries queries) returns AddOrDeleteRulesResponse|error;
+    resource function post tweets/search/'stream/rules(AddOrDeleteRulesRequest payload, map<string|string[]> headers = {}, boolean dryRun = false, boolean deleteAll = false, AddOrDeleteRulesQueries queries) returns AddOrDeleteRulesResponse|error;
 
     # Rules Count
     # 
-    resource function get tweets/search/'stream/rules/counts(map<string|string[]> headers = {}, ("all_project_client_apps"|"cap_per_client_app"|"cap_per_project"|"client_app_rules_count"|"project_rules_count")[] rulesCountFields = [], anydata Additional Values, GetRuleCountQueries queries) returns Get2TweetsSearchStreamRulesCountsResponse|error;
+    resource function get tweets/search/'stream/rules/counts(map<string|string[]> headers = {}, ("all_project_client_apps"|"cap_per_client_app"|"cap_per_project"|"client_app_rules_count"|"project_rules_count")[] rulesCountFields = [], GetRuleCountQueries queries) returns Get2TweetsSearchStreamRulesCountsResponse|error;
 
     # Post lookup by Post ID
     # 
-    resource function get tweets/[twitter:TweetId id](map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, FindTweetByIdQueries queries) returns Get2TweetsIdResponse|error;
+    resource function get tweets/[twitter:TweetId id](map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], FindTweetByIdQueries queries) returns Get2TweetsIdResponse|error;
 
     # Post delete by Post ID
     # 
@@ -3885,19 +4805,19 @@
 
     # Returns User objects that have liked the provided Post ID
     # 
-    resource function get tweets/[twitter:TweetId id]/liking_users(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, TweetsIdLikingUsersQueries queries) returns Get2TweetsIdLikingUsersResponse|error;
+    resource function get tweets/[twitter:TweetId id]/liking_users(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], TweetsIdLikingUsersQueries queries) returns Get2TweetsIdLikingUsersResponse|error;
 
     # Retrieve Posts that quote a Post.
     # 
-    resource function get tweets/[twitter:TweetId id]/quote_tweets(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("replies"|"retweets")[] exclude = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, FindTweetsThatQuoteATweetQueries queries) returns Get2TweetsIdQuoteTweetsResponse|error;
+    resource function get tweets/[twitter:TweetId id]/quote_tweets(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("replies"|"retweets")[] exclude = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], FindTweetsThatQuoteATweetQueries queries) returns Get2TweetsIdQuoteTweetsResponse|error;
 
     # Returns User objects that have retweeted the provided Post ID
     # 
-    resource function get tweets/[twitter:TweetId id]/retweeted_by(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, TweetsIdRetweetingUsersQueries queries) returns Get2TweetsIdRetweetedByResponse|error;
+    resource function get tweets/[twitter:TweetId id]/retweeted_by(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], TweetsIdRetweetingUsersQueries queries) returns Get2TweetsIdRetweetedByResponse|error;
 
     # Retrieve Posts that repost a Post.
     # 
-    resource function get tweets/[twitter:TweetId id]/retweets(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, FindTweetsThatRetweetATweetQueries queries) returns Get2TweetsIdRetweetsResponse|error;
+    resource function get tweets/[twitter:TweetId id]/retweets(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], FindTweetsThatRetweetATweetQueries queries) returns Get2TweetsIdRetweetsResponse|error;
 
     # Hide replies
     # 
@@ -3905,43 +4825,43 @@
 
     # Post Usage
     # 
-    resource function get usage/tweets(map<string|string[]> headers = {}, ("cap_reset_day"|"daily_client_app_usage"|"daily_project_usage"|"project_cap"|"project_id"|"project_usage")[] usageFields = [], int:Signed32 days = 0, anydata Additional Values, GetUsageTweetsQueries queries) returns Get2UsageTweetsResponse|error;
+    resource function get usage/tweets(map<string|string[]> headers = {}, ("cap_reset_day"|"daily_client_app_usage"|"daily_project_usage"|"project_cap"|"project_id"|"project_usage")[] usageFields = [], int:Signed32 days = 0, GetUsageTweetsQueries queries) returns Get2UsageTweetsResponse|error;
 
     # User lookup by IDs
     # 
-    resource function get users(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], UserId[] ids = [], ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, FindUsersByIdQueries queries) returns Get2UsersResponse|error;
+    resource function get users(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], UserId[] ids = [], ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], FindUsersByIdQueries queries) returns Get2UsersResponse|error;
 
     # User lookup by usernames
     # 
-    resource function get users/'by(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], FindUsersByUsernameQueriesUsernamesItemsString[] usernames = [], ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, FindUsersByUsernameQueries queries) returns Get2UsersByResponse|error;
+    resource function get users/'by(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], FindUsersByUsernameQueriesUsernamesItemsString[] usernames = [], ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], FindUsersByUsernameQueries queries) returns Get2UsersByResponse|error;
 
     # User lookup by username
     # 
-    resource function get users/'by/username/[string username](map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, FindUserByUsernameQueries queries) returns Get2UsersByUsernameUsernameResponse|error;
+    resource function get users/'by/username/[string username](map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], FindUserByUsernameQueries queries) returns Get2UsersByUsernameUsernameResponse|error;
 
     # Users Compliance stream
     # 
-    resource function get users/compliance/'stream(map<string|string[]> headers = {}, int:Signed32 backfillMinutes = 0, string startTime = "", int:Signed32 partition = 0, string endTime = "", anydata Additional Values, GetUsersComplianceStreamQueries queries) returns UserComplianceStreamResponseOneOf1|UserComplianceStreamResponseUserComplianceStreamResponseOneOf12|error;
+    resource function get users/compliance/'stream(map<string|string[]> headers = {}, int:Signed32 backfillMinutes = 0, string startTime = "", int:Signed32 partition = 0, string endTime = "", GetUsersComplianceStreamQueries queries) returns UserComplianceStreamResponseOneOf1|UserComplianceStreamResponseUserComplianceStreamResponseOneOf12|error;
 
     # User lookup me
     # 
-    resource function get users/me(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, FindMyUserQueries queries) returns Get2UsersMeResponse|error;
+    resource function get users/me(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], FindMyUserQueries queries) returns Get2UsersMeResponse|error;
 
     # User search
     # 
-    resource function get users/search(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], UserSearchQuery query = "", int:Signed32 maxResults = 0, PaginationToken36 nextToken = "", ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, SearchUserByQueryQueries queries) returns Get2UsersSearchResponse|error;
+    resource function get users/search(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], UserSearchQuery query = "", int:Signed32 maxResults = 0, PaginationToken36 nextToken = "", ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], SearchUserByQueryQueries queries) returns Get2UsersSearchResponse|error;
 
     # User lookup by ID
     # 
-    resource function get users/[twitter:UserId id](map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, FindUserByIdQueries queries) returns Get2UsersIdResponse|error;
+    resource function get users/[twitter:UserId id](map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], FindUserByIdQueries queries) returns Get2UsersIdResponse|error;
 
     # Returns User objects that are blocked by provided User ID
     # 
-    resource function get users/[twitter:UserIdMatchesAuthenticatedUser id]/blocking(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken32 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, UsersIdBlockingQueries queries) returns Get2UsersIdBlockingResponse|error;
+    resource function get users/[twitter:UserIdMatchesAuthenticatedUser id]/blocking(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken32 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], UsersIdBlockingQueries queries) returns Get2UsersIdBlockingResponse|error;
 
     # Bookmarks by User
     # 
-    resource function get users/[twitter:UserIdMatchesAuthenticatedUser id]/bookmarks(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, GetUsersIdBookmarksQueries queries) returns Get2UsersIdBookmarksResponse|error;
+    resource function get users/[twitter:UserIdMatchesAuthenticatedUser id]/bookmarks(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], GetUsersIdBookmarksQueries queries) returns Get2UsersIdBookmarksResponse|error;
 
     # Add Post to Bookmarks
     # 
@@ -3953,7 +4873,7 @@
 
     # Get User's Followed Lists
     # 
-    resource function get users/[twitter:UserId id]/followed_lists(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationTokenLong paginationToken = "", int:Signed32 maxResults = 0, ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields = [], "owner_id"[] expansions = [], anydata Additional Values, UserFollowedListsQueries queries) returns Get2UsersIdFollowedListsResponse|error;
+    resource function get users/[twitter:UserId id]/followed_lists(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationTokenLong paginationToken = "", int:Signed32 maxResults = 0, ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields = [], "owner_id"[] expansions = [], UserFollowedListsQueries queries) returns Get2UsersIdFollowedListsResponse|error;
 
     # Follow a List
     # 
@@ -3965,11 +4885,11 @@
 
     # Followers by User ID
     # 
-    resource function get users/[twitter:UserId id]/followers(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken32 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, UsersIdFollowersQueries queries) returns Get2UsersIdFollowersResponse|error;
+    resource function get users/[twitter:UserId id]/followers(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken32 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], UsersIdFollowersQueries queries) returns Get2UsersIdFollowersResponse|error;
 
     # Following by User ID
     # 
-    resource function get users/[twitter:UserId id]/following(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken32 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, UsersIdFollowingQueries queries) returns Get2UsersIdFollowingResponse|error;
+    resource function get users/[twitter:UserId id]/following(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken32 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], UsersIdFollowingQueries queries) returns Get2UsersIdFollowingResponse|error;
 
     # Follow User
     # 
@@ -3977,7 +4897,7 @@
 
     # Returns Post objects liked by the provided User ID
     # 
-    resource function get users/[twitter:UserId id]/liked_tweets(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], anydata Additional Values, UsersIdLikedTweetsQueries queries) returns Get2UsersIdLikedTweetsResponse|error;
+    resource function get users/[twitter:UserId id]/liked_tweets(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], UsersIdLikedTweetsQueries queries) returns Get2UsersIdLikedTweetsResponse|error;
 
     # Causes the User (in the path) to like the specified Post
     # 
@@ -3989,15 +4909,15 @@
 
     # Get a User's List Memberships
     # 
-    resource function get users/[twitter:UserId id]/list_memberships(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationTokenLong paginationToken = "", int:Signed32 maxResults = 0, ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields = [], "owner_id"[] expansions = [], anydata Additional Values, GetUserListMembershipsQueries queries) returns Get2UsersIdListMembershipsResponse|error;
+    resource function get users/[twitter:UserId id]/list_memberships(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationTokenLong paginationToken = "", int:Signed32 maxResults = 0, ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields = [], "owner_id"[] expansions = [], GetUserListMembershipsQueries queries) returns Get2UsersIdListMembershipsResponse|error;
 
     # User mention timeline by User ID
     # 
-    resource function get users/[twitter:UserId id]/mentions(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], TweetId sinceId = "", ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], TweetId untilId = "", anydata Additional Values, UsersIdMentionsQueries queries) returns Get2UsersIdMentionsResponse|error;
+    resource function get users/[twitter:UserId id]/mentions(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], string endTime = "", int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], TweetId sinceId = "", ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], TweetId untilId = "", UsersIdMentionsQueries queries) returns Get2UsersIdMentionsResponse|error;
 
     # Returns User objects that are muted by the provided User ID
     # 
-    resource function get users/[twitter:UserIdMatchesAuthenticatedUser id]/muting(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationTokenLong paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], anydata Additional Values, UsersIdMutingQueries queries) returns Get2UsersIdMutingResponse|error;
+    resource function get users/[twitter:UserIdMatchesAuthenticatedUser id]/muting(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationTokenLong paginationToken = "", ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], int:Signed32 maxResults = 0, ("most_recent_tweet_id"|"pinned_tweet_id")[] expansions = [], UsersIdMutingQueries queries) returns Get2UsersIdMutingResponse|error;
 
     # Mute User by User ID.
     # 
@@ -4005,11 +4925,11 @@
 
     # Get a User's Owned Lists.
     # 
-    resource function get users/[twitter:UserId id]/owned_lists(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationTokenLong paginationToken = "", int:Signed32 maxResults = 0, ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields = [], "owner_id"[] expansions = [], anydata Additional Values, ListUserOwnedListsQueries queries) returns Get2UsersIdOwnedListsResponse|error;
+    resource function get users/[twitter:UserId id]/owned_lists(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationTokenLong paginationToken = "", int:Signed32 maxResults = 0, ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields = [], "owner_id"[] expansions = [], ListUserOwnedListsQueries queries) returns Get2UsersIdOwnedListsResponse|error;
 
     # Get a User's Pinned Lists
     # 
-    resource function get users/[twitter:UserIdMatchesAuthenticatedUser id]/pinned_lists(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields = [], "owner_id"[] expansions = [], anydata Additional Values, ListUserPinnedListsQueries queries) returns Get2UsersIdPinnedListsResponse|error;
+    resource function get users/[twitter:UserIdMatchesAuthenticatedUser id]/pinned_lists(map<string|string[]> headers = {}, ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], ("created_at"|"description"|"follower_count"|"id"|"member_count"|"name"|"owner_id"|"private")[] listFields = [], "owner_id"[] expansions = [], ListUserPinnedListsQueries queries) returns Get2UsersIdPinnedListsResponse|error;
 
     # Pin a List
     # 
@@ -4029,11 +4949,11 @@
 
     # User home timeline by User ID
     # 
-    resource function get users/[twitter:UserIdMatchesAuthenticatedUser id]/timelines/reverse_chronological(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], string endTime = "", TweetId sinceId = "", string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("replies"|"retweets")[] exclude = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], TweetId untilId = "", anydata Additional Values, UsersIdTimelineQueries queries) returns Get2UsersIdTimelinesReverseChronologicalResponse|error;
+    resource function get users/[twitter:UserIdMatchesAuthenticatedUser id]/timelines/reverse_chronological(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], string endTime = "", TweetId sinceId = "", string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("replies"|"retweets")[] exclude = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], TweetId untilId = "", UsersIdTimelineQueries queries) returns Get2UsersIdTimelinesReverseChronologicalResponse|error;
 
     # User Posts timeline by User ID
     # 
-    resource function get users/[twitter:UserId id]/tweets(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], string endTime = "", TweetId sinceId = "", string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("replies"|"retweets")[] exclude = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], TweetId untilId = "", anydata Additional Values, UsersIdTweetsQueries queries) returns Get2UsersIdTweetsResponse|error;
+    resource function get users/[twitter:UserId id]/tweets(map<string|string[]> headers = {}, ("duration_minutes"|"end_datetime"|"id"|"options"|"voting_status")[] pollFields = [], ("attachments"|"author_id"|"card_uri"|"context_annotations"|"conversation_id"|"created_at"|"edit_controls"|"edit_history_tweet_ids"|"entities"|"geo"|"id"|"in_reply_to_user_id"|"lang"|"non_public_metrics"|"note_tweet"|"organic_metrics"|"possibly_sensitive"|"promoted_metrics"|"public_metrics"|"referenced_tweets"|"reply_settings"|"scopes"|"source"|"text"|"username"|"withheld")[] tweetFields = [], string endTime = "", TweetId sinceId = "", string startTime = "", ("connection_status"|"created_at"|"description"|"entities"|"id"|"location"|"most_recent_tweet_id"|"name"|"pinned_tweet_id"|"profile_image_url"|"protected"|"public_metrics"|"receives_your_dm"|"subscription_type"|"url"|"username"|"verified"|"verified_type"|"withheld")[] userFields = [], PaginationToken36 paginationToken = "", ("alt_text"|"duration_ms"|"height"|"media_key"|"non_public_metrics"|"organic_metrics"|"preview_image_url"|"promoted_metrics"|"public_metrics"|"type"|"url"|"variants"|"width")[] mediaFields = [], int:Signed32 maxResults = 0, ("contained_within"|"country"|"country_code"|"full_name"|"geo"|"id"|"name"|"place_type")[] placeFields = [], ("replies"|"retweets")[] exclude = [], ("attachments.media_keys"|"attachments.media_source_tweet"|"attachments.poll_ids"|"author_id"|"edit_history_tweet_ids"|"entities.mentions.username"|"geo.place_id"|"in_reply_to_user_id"|"entities.note.mentions.username"|"referenced_tweets.id"|"referenced_tweets.id.author_id"|"author_screen_name")[] expansions = [], TweetId untilId = "", UsersIdTweetsQueries queries) returns Get2UsersIdTweetsResponse|error;
 
     # Unfollow User
     # 
`````
