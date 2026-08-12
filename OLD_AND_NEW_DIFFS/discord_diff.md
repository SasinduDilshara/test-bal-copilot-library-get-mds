# discord — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `discord` |
| **Old file** | `discord/old/ballerinax_discord.bal.txt` |
| **New file** | `discord/new/ballerinax_discord.bal.txt` |
| **Old lines** | 5779 |
| **New lines** | 7142 |
| **Lines added** | 2168 |
| **Lines removed** | 805 |
| **Hunks** | 145 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 421 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 821 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (421)

- `type ACCEPTED`
- `type ACTIVE`
- `type ACTIVITIESREAD`
- `type ACTIVITIESWRITE`
- `type AGERESTRICTED`
- `type ALLMEMBERS`
- `type ALLMESSAGES`
- `type ANIMATEDBANNER`
- `type ANIMATEDICON`
- `type ANNOUNCEMENTTHREAD`
- `type APNG`
- `type APPLICATIONCOMMAND`
- `type APPLICATIONCOMMANDAUTOCOMPLETE`
- `type APPLICATIONCOMMANDAUTOCOMPLETERESULT`
- `type APPLICATIONCOMMANDPERMISSIONSV2`
- `type APPLICATIONCOMMANDPERMISSIONUPDATE`
- `type APPLICATIONSBUILDSREAD`
- `type APPLICATIONSBUILDSUPLOAD`
- `type APPLICATIONSCOMMANDS`
- `type APPLICATIONSCOMMANDSPERMISSIONSUPDATE`
- `type APPLICATIONSCOMMANDSUPDATE`
- `type APPLICATIONSENTITLEMENTS`
- `type APPLICATIONSSTOREUPDATE`
- `type APPLICATIONSUBSCRIPTION`
- `type AUTOMODERATION`
- `type AUTOMODERATIONACTION`
- `type AUTOMODERATIONBLOCKMESSAGE`
- `type AUTOMODERATIONFLAGTOCHANNEL`
- `type AUTOMODERATIONQUARANTINEUSER`
- `type AUTOMODERATIONRULECREATE`
- `type AUTOMODERATIONRULEDELETE`
- `type AUTOMODERATIONRULEUPDATE`
- `type AUTOMODERATIONUSERCOMMDISABLED`
- `type ApplicationFormPartialTagsItemsString`
- `type Ar`
- `type BANNER`
- `type BANNER1`
- `type BANNER2`
- `type BANNER3`
- `type BANNER4`
- `type BATTLENET`
- `type BOOLEANEQUAL`
- `type BOOLEANNOTEQUAL`
- `type BOT`
- `type BOTADD`
- `type BUNGIE`
- `type BaseCreateMessageCreateRequestStickeridsItemsString`
- `type BasicMessageResponseMentionrolesItemsString`
- `type Bg`
- `type BulkBanUsersResponseBannedusersItemsString`
- `type BulkBanUsersResponseFailedusersItemsString`
- `type CALL`
- `type CANCELED`
- `type CHANNEL1`
- `type CHANNELCREATE`
- `type CHANNELDELETE`
- `type CHANNELFOLLOWADD`
- `type CHANNELICONCHANGE`
- `type CHANNELMESSAGEWITHSOURCE`
- `type CHANNELNAMECHANGE`
- `type CHANNELOVERWRITECREATE`
- `type CHANNELOVERWRITEDELETE`
- `type CHANNELOVERWRITEUPDATE`
- `type CHANNELPINNEDMESSAGE`
- `type CHANNELUPDATE`
- `type CHAT`
- `type CHATINPUTCOMMAND`
- `type COMMUNITY`
- `type COMPLETED`
- `type CONNECTIONS`
- `type CONTEXTMENUCOMMAND`
- `type CREATORMONETIZABLEPROVISIONAL`
- `type CREATORMONETIZATIONREQUESTCREATED`
- `type CREATORMONETIZATIONTERMSACCEPTED`
- `type CREATORSTOREPAGE`
- `type ChannelIdMessagesBodyStickeridsItemsString`
- `type ChannelsMessagesBulkDeleteRequestMessagesItemsString`
- `type CreateForumThreadRequestAppliedtagsItemsString`
- `type CreatePrivateChannelRequestAccesstokensItemsString`
- `type CreatedThreadResponseAppliedtagsItemsString`
- `type Cs`
- `type DANGER`
- `type DATETIMEGREATERTHANEQUAL`
- `type DATETIMELESSTHANEQUAL`
- `type DEFAULT`
- `type DEFAULTKEYWORDLIST`
- `type DEFERREDCHANNELMESSAGEWITHSOURCE`
- `type DEFERREDUPDATEMESSAGE`
- `type DEVELOPERSUPPORTSERVER`
- `type DISABLED`
- `type DISCORD`
- `type DISCOVERABLE`
- `type DM`
- `type DMCHANNELSREAD`
- `type DOMAIN`
- `type DROPDOWN`
- `type Da`
- `type De`
- `type DefaultKeywordListTriggerMetadataAllowlistItemsString`
- `type DefaultKeywordListUpsertRequestExemptchannelsItemsString`
- `type DefaultKeywordListUpsertRequestExemptrolesItemsString`
- `type DefaultKeywordListUpsertRequestPartialExemptchannelsItemsString`
- `type DefaultKeywordListUpsertRequestPartialExemptrolesItemsString`
- `type DefaultKeywordRuleResponseExemptchannelsItemsString`
- `type DefaultKeywordRuleResponseExemptrolesItemsString`
- `type EBAY`
- `type ELEVATED`
- `type EMAIL`
- `type EMOJICREATE`
- `type EMOJIDELETE`
- `type EMOJIUPDATE`
- `type EPICGAMES`
- `type EVERYONE`
- `type EVERYONE1`
- `type EXPLICIT`
- `type EXTERNAL`
- `type El`
- `type EmojiResponseRolesItemsString`
- `type EnGB`
- `type EnUS`
- `type Es419`
- `type EsES`
- `type FACEBOOK`
- `type FEATURABLE`
- `type FIFTEENMINUTES`
- `type FIVEMINUTES`
- `type Fi`
- `type Fr`
- `type GDMJOIN`
- `type GIF`
- `type GITHUB`
- `type GROUPDM`
- `type GUILDANNOUNCEMENT`
- `type GUILDAPPLICATIONPREMIUMSUBSCRIPTION`
- `type GUILDBOOST`
- `type GUILDBOOSTTIER1`
- `type GUILDBOOSTTIER2`
- `type GUILDBOOSTTIER3`
- `type GUILDCATEGORY`
- `type GUILDDIRECTORY`
- `type GUILDDISCOVERYDISQUALIFIED`
- `type GUILDDISCOVERYGRACEPERIODFINALWARNING`
- `type GUILDDISCOVERYGRACEPERIODINITIALWARNING`
- `type GUILDDISCOVERYREQUALIFIED`
- `type GUILDFORUM`
- `type GUILDHOMEFEATUREITEM`
- `type GUILDHOMEREMOVEITEM`
- `type GUILDINCIDENTALERTMODEDISABLED`
- `type GUILDINCIDENTALERTMODEENABLED`
- `type GUILDINCIDENTREPORTFALSEALARM`
- `type GUILDINCIDENTREPORTRAID`
- `type GUILDINVITEREMINDER`
- `type GUILDMEMBERJOINORUPDATE`
- `type GUILDONLY`
- `type GUILDONLY1`
- `type GUILDPRODUCT`
- `type GUILDS`
- `type GUILDSCHEDULEDEVENTCREATE`
- `type GUILDSCHEDULEDEVENTDELETE`
- `type GUILDSCHEDULEDEVENTUPDATE`
- `type GUILDSJOIN`
- `type GUILDSMEMBERSREAD`
- `type GUILDSTAGEVOICE`
- `type GUILDSUBSCRIPTION`
- `type GUILDTEXT`
- `type GUILDUPDATE`
- `type GUILDVOICE`
- `type GuildMemberResponseRolesItemsString`
- `type GuildOnboardingResponseDefaultchannelidsItemsString`
- `type GuildScheduledEventPrivacyLevels`
- `type GuildsBulkBanRequestUseridsItemsString`
- `type HARMFULLINKSBLOCKEDMESSAGE`
- `type HIGH`
- `type HOMESETTINGSCREATE`
- `type HOMESETTINGSUPDATE`
- `type He`
- `type Hi`
- `type Hr`
- `type Hu`
- `type IDENTIFY`
- `type INSTAGRAM`
- `type INTEGEREQUAL`
- `type INTEGERGREATERTHANEQUAL`
- `type INTEGERLESSTHANEQUAL`
- `type INTEGERNOTEQUAL`
- `type INTEGRATIONCREATE`
- `type INTEGRATIONDELETE`
- `type INTEGRATIONUPDATE`
- `type INTERACTIONPREMIUMUPSELL`
- `type INVITECREATE`
- `type INVITED`
- `type INVITEDELETE`
- `type INVITESDISABLED`
- `type INVITESPLASH`
- `type INVITEUPDATE`
- `type Id`
- `type IncludeRolesIncludeRolesOneOf12`
- `type IncludeRolesIncludeRolesOneOf12OneOf1`
- `type IncludeRolesOneOf1`
- `type IncluderolesItemsnull`
- `type IncomingWebhookRequestPartialAppliedtagsItemsString`
- `type InlineArrayItemsIncludeRolesIncludeRolesOneOf12`
- `type InlineArrayItemsSkuIdsSkuIdsOneOf12`
- `type It`
- `type Ja`
- `type KEYWORD`
- `type KeywordRuleResponseExemptchannelsItemsString`
- `type KeywordRuleResponseExemptrolesItemsString`
- `type KeywordTriggerMetadataAllowlistItemsString`
- `type KeywordTriggerMetadataKeywordfilterItemsString`
- `type KeywordTriggerMetadataRegexpatternsItemsString`
- `type KeywordUpsertRequestExemptchannelsItemsString`
- `type KeywordUpsertRequestExemptrolesItemsString`
- `type KeywordUpsertRequestPartialExemptchannelsItemsString`
- `type KeywordUpsertRequestPartialExemptrolesItemsString`
- `type Ko`
- `type LEAGUEOFLEGENDS`
- `type LINK`
- `type LOTTIE`
- `type LOW`
- `type Lt`
- `type MEDIUM`
- `type MEMBER`
- `type MEMBERBANADD`
- `type MEMBERBANREMOVE`
- `type MEMBERDISCONNECT`
- `type MEMBERKICK`
- `type MEMBERMOVE`
- `type MEMBERPRUNE`
- `type MEMBERROLEUPDATE`
- `type MEMBERSWITHOUTROLES`
- `type MEMBERUPDATE`
- `type MEMBERVERIFICATIONGATEENABLED`
- `type MENTIONSPAM`
- `type MESSAGE`
- `type MESSAGEBULKDELETE`
- `type MESSAGECOMPONENT`
- `type MESSAGEDELETE`
- `type MESSAGEPIN`
- `type MESSAGESEND`
- `type MESSAGESREAD`
- `type MESSAGEUNPIN`
- `type MLSPAM`
- `type MLSpamRuleResponseExemptchannelsItemsString`
- `type MLSpamRuleResponseExemptrolesItemsString`
- `type MLSpamUpsertRequestExemptchannelsItemsString`
- `type MLSpamUpsertRequestExemptrolesItemsString`
- `type MLSpamUpsertRequestPartialExemptchannelsItemsString`
- `type MLSpamUpsertRequestPartialExemptrolesItemsString`
- `type MODAL`
- `type MODALSUBMIT`
- `type MORESTICKERS`
- `type MULTIPLECHOICE`
- `type MentionSpamRuleResponseExemptchannelsItemsString`
- `type MentionSpamRuleResponseExemptrolesItemsString`
- `type MentionSpamUpsertRequestExemptchannelsItemsString`
- `type MentionSpamUpsertRequestExemptrolesItemsString`
- `type MentionSpamUpsertRequestPartialExemptchannelsItemsString`
- `type MentionSpamUpsertRequestPartialExemptrolesItemsString`
- `type MessageCallResponseParticipantsItemsString`
- `type MessageResponseMentionrolesItemsString`
- `type MessagesmessageIdBodyStickeridsItemsString`
- `type NEWS`
- `type NONE`
- `type NONE2`
- `type NONE3`
- `type NONE4`
- `type Nl`
- `type No`
- `type ONBOARDINGCREATE`
- `type ONBOARDINGPROMPTCREATE`
- `type ONBOARDINGPROMPTDELETE`
- `type ONBOARDINGPROMPTUPDATE`
- `type ONBOARDINGUPDATE`
- `type ONEDAY`
- `type ONEHOUR`
- `type ONEHOUR1`
- `type ONEMINUTE`
- `type ONLYMENTIONS`
- `type OPENID`
- `type OnboardingPromptOptionRequestChannelidsItemsString`
- `type OnboardingPromptOptionRequestRoleidsItemsString`
- `type OnboardingPromptOptionResponseChannelidsItemsString`
- `type OnboardingPromptOptionResponseRoleidsItemsString`
- `type PARAGRAPH`
- `type PARTNERED`
- `type PAYPAL`
- `type PING`
- `type PLAYSTATION`
- `type PNG`
- `type PONG`
- `type PREMIUM`
- `type PREVIEWENABLED`
- `type PRIMARY`
- `type PRIVATETHREAD`
- `type PROFANITY`
- `type PUBLIC`
- `type PUBLICTHREAD`
- `type Pl`
- `type PrivateGuildMemberResponseRolesItemsString`
- `type PtBR`
- `type PurchaseType`
- `type QUESTREWARD`
- `type RAIDALERTSDISABLED`
- `type RECIPIENTADD`
- `type RECIPIENTREMOVE`
- `type REDDIT`
- `type RELATIONSHIPSREAD`
- `type REPLY`
- `type RIOTGAMES`
- `type ROBLOX`
- `type ROLE1`
- `type ROLE2`
- `type ROLECONNECTIONSWRITE`
- `type ROLECREATE`
- `type ROLEDELETE`
- `type ROLEICONS`
- `type ROLES`
- `type ROLESUBSCRIPTIONPURCHASE`
- `type ROLESUBSCRIPTIONSAVAILABLEFORPURCHASE`
- `type ROLESUBSCRIPTIONSENABLED`
- `type ROLEUPDATE`
- `type RPC`
- `type RPCACTIVITIESWRITE`
- `type RPCNOTIFICATIONSREAD`
- `type RPCSCREENSHAREREAD`
- `type RPCSCREENSHAREWRITE`
- `type RPCVIDEOREAD`
- `type RPCVIDEOWRITE`
- `type RPCVOICEREAD`
- `type RPCVOICEWRITE`
- `type Ro`
- `type RolesOneOf1`
- `type RolesOneOf11`
- `type RolesOneOf12`
- `type RolesOneOf13`
- `type RolesOneOf14`
- `type Ru`
- `type SAFE`
- `type SCHEDULED`
- `type SECONDARY`
- `type SEVENDAY`
- `type SEXUALCONTENT`
- `type SHIELD`
- `type SHORT`
- `type SKYPE`
- `type SLURS`
- `type SOUNDBOARDSOUNDCREATE`
- `type SOUNDBOARDSOUNDDELETE`
- `type SOUNDBOARDSOUNDUPDATE`
- `type SPAMLINK`
- `type SPOTIFY`
- `type STAGEEND`
- `type STAGEINSTANCE`
- `type STAGEINSTANCECREATE`
- `type STAGEINSTANCEDELETE`
- `type STAGEINSTANCEUPDATE`
- `type STAGESPEAKER`
- `type STAGESTART`
- `type STAGETOPIC`
- `type STEAM`
- `type STICKERCREATE`
- `type STICKERDELETE`
- `type STICKERUPDATE`
- `type SUCCESS`
- `type SkuIdsOneOf1`
- `type SkuIdsSkuIdsOneOf12`
- `type SkuIdsSkuIdsOneOf12OneOf1`
- `type SpamLinkRuleResponseExemptchannelsItemsString`
- `type SpamLinkRuleResponseExemptrolesItemsString`
- `type SvSE`
- `type TALK`
- `type THIRTYMINUTES`
- `type THREADCREATE`
- `type THREADCREATED`
- `type THREADDELETE`
- `type THREADSTARTERMESSAGE`
- `type THREADUPDATE`
- `type THREEDAY`
- `type TICKETEDEVENTSENABLED`
- `type TIER1`
- `type TIER2`
- `type TIER3`
- `type TIKTOK`
- `type TWITCH`
- `type TWITTER`
- `type Th`
- `type ThreadResponseAppliedtagsItemsString`
- `type Tr`
- `type UPDATEMESSAGE`
- `type USER`
- `type USER2`
- `type USERJOIN`
- `type USERS`
- `type Uk`
- `type UpdateGuildOnboardingRequestDefaultchannelidsItemsString`
- `type UpdateThreadRequestPartialAppliedtagsItemsString`
- `type UserGuildOnboardingResponseDefaultchannelidsItemsString`
- `type UsersOneOf1`
- `type VANITYURL`
- `type VERIFIED`
- `type VERYHIGH`
- `type VIEW`
- `type VIPREGIONS`
- `type VOICE`
- `type VOICE1`
- `type VOICECHANNELSTATUSCREATE`
- `type VOICECHANNELSTATUSDELETE`
- `type Vi`
- `type WEBHOOKCREATE`
- `type WEBHOOKDELETE`
- `type WEBHOOKINCOMING`
- `type WEBHOOKUPDATE`
- `type WELCOMESCREENENABLED`
- `type WelcomeMessageResponseAuthoridsItemsString`
- `type WidgetUserDiscriminator`
- `type XBOX`
- `type YOUTUBE`
- `type ZEROES`
- `type ZhCN`
- `type ZhTW`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 113–146 | 113–153 | END README | +15 | −8 |
| 2 | 150–209 | 157–240 | Types | +35 | −11 |
| 3 | 211–247 | 242–287 | Types | +11 | −2 |
| 4 | 249–291 | 289–337 | Types | +17 | −11 |
| 5 | 293–335 | 339–391 | Types | +18 | −8 |
| 6 | 339–496 | 395–608 | Types | +105 | −49 |
| 7 | 506–511 | 618–624 | Types | +1 | −0 |
| 8 | 523–576 | 636–697 | Types | +26 | −18 |
| 9 | 578–642 | 699–776 | Types | +26 | −13 |
| 10 | 644–676 | 778–817 | Types | +15 | −8 |
| 11 | 679–739 | 820–903 | Types | +43 | −20 |
| 12 | 741–750 | 905–918 | Types | +6 | −2 |
| 13 | 752–760 | 920–932 | Types | +6 | −2 |
| 14 | 766–782 | 938–958 | Types | +5 | −1 |
| 15 | 784–790 | 960–966 | Types | +1 | −1 |
| 16 | 800–851 | 976–1038 | Types | +17 | −6 |
| 17 | 863–869 | 1050–1057 | Types | +2 | −1 |
| 18 | 871–890 | 1059–1082 | Types | +6 | −2 |
| 19 | 902–922 | 1094–1118 | Types | +7 | −3 |
| 20 | 925–1063 | 1121–1286 | Types | +69 | −42 |
| 21 | 1067–1113 | 1290–1336 | Types | +21 | −21 |
| 22 | 1123–1132 | 1346–1357 | Types | +3 | −1 |
| 23 | 1134–1179 | 1359–1420 | Types | +26 | −10 |
| 24 | 1181–1398 | 1422–1728 | Types | +180 | −91 |
| 25 | 1400–1419 | 1730–1751 | Types | +5 | −3 |
| 26 | 1422–1449 | 1754–1791 | Types | +12 | −2 |
| 27 | 1453–1458 | 1795–1801 | Types | +1 | −0 |
| 28 | 1464–1469 | 1807–1813 | Types | +1 | −0 |
| 29 | 1481–1502 | 1825–1850 | Types | +8 | −4 |
| 30 | 1507–1513 | 1855–1861 | Types | +1 | −1 |
| 31 | 1529–1534 | 1877–1883 | Types | +1 | −0 |
| 32 | 1543–1588 | 1892–1953 | Types | +23 | −7 |
| 33 | 1590–1611 | 1955–1982 | Types | +11 | −5 |
| 34 | 1617–1669 | 1988–2053 | Types | +23 | −10 |
| 35 | 1671–1714 | 2055–2114 | Types | +21 | −5 |
| 36 | 1716–1727 | 2116–2130 | Types | +6 | −3 |
| 37 | 1737–1770 | 2140–2180 | Types | +15 | −8 |
| 38 | 1773–1835 | 2183–2266 | Types | +27 | −6 |
| 39 | 1837–1846 | 2268–2281 | Types | +4 | −0 |
| 40 | 1848–1856 | 2283–2295 | Types | +4 | −0 |
| 41 | 1858–1887 | 2297–2339 | Types | +13 | −0 |
| 42 | 1889–1918 | 2341–2382 | Types | +12 | −0 |
| 43 | 1920–1949 | 2384–2426 | Types | +15 | −2 |
| 44 | 1951–1995 | 2428–2483 | Types | +16 | −5 |
| 45 | 1998–2071 | 2486–2583 | Types | +39 | −15 |
| 46 | 2075–2176 | 2587–2729 | Types | +45 | −4 |
| 47 | 2178–2204 | 2731–2767 | Types | +10 | −0 |
| 48 | 2206–2216 | 2769–2783 | Types | +4 | −0 |
| 49 | 2218–2229 | 2785–2800 | Types | +4 | −0 |
| 50 | 2231–2242 | 2802–2817 | Types | +4 | −0 |
| 51 | 2244–2285 | 2819–2879 | Types | +28 | −9 |
| 52 | 2287–2305 | 2881–2911 | Types | +13 | −1 |
| 53 | 2308–2534 | 2914–3183 | Types | +114 | −71 |
| 54 | 2536–2549 | 3185–3203 | Types | +7 | −2 |
| 55 | 2555–2574 | 3209–3234 | Types | +7 | −1 |
| 56 | 2577–2587 | 3237–3251 | Types | +6 | −2 |
| 57 | 2591–2603 | 3255–3270 | Types | +3 | −0 |
| 58 | 2608–2629 | 3275–3304 | Types | +11 | −3 |
| 59 | 2631–2654 | 3306–3336 | Types | +10 | −3 |
| 60 | 2656–2697 | 3338–3392 | Types | +17 | −4 |
| 61 | 2706–2723 | 3401–3421 | Types | +6 | −3 |
| 62 | 2727–2760 | 3425–3462 | Types | +7 | −3 |
| 63 | 2764–2796 | 3466–3507 | Types | +12 | −3 |
| 64 | 2798–2870 | 3509–3600 | Types | +29 | −10 |
| 65 | 2873–2903 | 3603–3649 | Types | +22 | −6 |
| 66 | 2905–2953 | 3651–3713 | Types | +24 | −10 |
| 67 | 2955–2968 | 3715–3730 | Types | +4 | −2 |
| 68 | 2970–3003 | 3732–3775 | Types | +18 | −8 |
| 69 | 3005–3031 | 3777–3807 | Types | +15 | −11 |
| 70 | 3035–3059 | 3811–3841 | Types | +9 | −3 |
| 71 | 3062–3092 | 3844–3885 | Types | +17 | −6 |
| 72 | 3096–3105 | 3889–3899 | Types | +2 | −1 |
| 73 | 3107–3140 | 3901–3948 | Types | +20 | −6 |
| 74 | 3144–3162 | 3952–3975 | Types | +6 | −1 |
| 75 | 3168–3175 | 3981–3990 | Types | +4 | −2 |
| 76 | 3180–3197 | 3995–4015 | Types | +4 | −1 |
| 77 | 3200–3206 | 4018–4026 | Types | +2 | −0 |
| 78 | 3210–3217 | 4030–4040 | Types | +3 | −0 |
| 79 | 3219–3246 | 4042–4073 | Types | +7 | −3 |
| 80 | 3254–3259 | 4081–4087 | Types | +1 | −0 |
| 81 | 3262–3403 | 4090–4277 | Types | +65 | −19 |
| 82 | 3405–3416 | 4279–4292 | Types | +2 | −0 |
| 83 | 3425–3491 | 4301–4392 | Types | +39 | −14 |
| 84 | 3493–3511 | 4394–4418 | Types | +7 | −1 |
| 85 | 3514–3567 | 4421–4487 | Types | +25 | −12 |
| 86 | 3571–3577 | 4491–4499 | Types | +2 | −0 |
| 87 | 3580–3585 | 4502–4508 | Types | +1 | −0 |
| 88 | 3588–3594 | 4511–4519 | Types | +2 | −0 |
| 89 | 3596–3625 | 4521–4560 | Types | +15 | −5 |
| 90 | 3632–3726 | 4567–4694 | Types | +40 | −7 |
| 91 | 3729–3769 | 4697–4754 | Types | +20 | −3 |
| 92 | 3778–3872 | 4763–4889 | Types | +41 | −9 |
| 93 | 3875–3887 | 4892–4906 | Types | +3 | −1 |
| 94 | 3889–3911 | 4908–4934 | Types | +7 | −3 |
| 95 | 3914–3926 | 4937–4952 | Types | +5 | −2 |
| 96 | 3928–3955 | 4954–4989 | Types | +10 | −2 |
| 97 | 3957–3970 | 4991–5005 | Types | +4 | −3 |
| 98 | 3972–3977 | 5007–5013 | Types | +1 | −0 |
| 99 | 3980–3985 | 5016–5022 | Types | +1 | −0 |
| 100 | 3987–4101 | 5024–5184 | Types | +64 | −18 |
| 101 | 4103–4123 | 5186–5206 | Types | +5 | −5 |
| 102 | 4132–4143 | 5215–5229 | Types | +3 | −0 |
| 103 | 4154–4173 | 5240–5262 | Types | +4 | −1 |
| 104 | 4180–4193 | 5269–5284 | Types | +5 | −3 |
| 105 | 4196–4201 | 5287–5293 | Types | +1 | −0 |
| 106 | 4203–4233 | 5295–5330 | Types | +12 | −7 |
| 107 | 4240–4301 | 5337–5428 | Types | +36 | −6 |
| 108 | 4311–4323 | 5438–5455 | Types | +6 | −1 |
| 109 | 4329–4355 | 5461–5492 | Types | +10 | −5 |
| 110 | 4357–4364 | 5494–5504 | Types | +4 | −1 |
| 111 | 4369–4385 | 5509–5531 | Types | +7 | −1 |
| 112 | 4387–4444 | 5533–5626 | Types | +45 | −9 |
| 113 | 4456–4466 | 5638–5650 | Types | +2 | −0 |
| 114 | 4507–4619 | 5691–5839 | Types | +46 | −10 |
| 115 | 4622–4659 | 5842–5892 | Types | +15 | −2 |
| 116 | 4666–4748 | 5899–6003 | Types | +31 | −9 |
| 117 | 4750–4825 | 6005–6121 | Types | +51 | −10 |
| 118 | 4828–4852 | 6124–6152 | Types | +5 | −1 |
| 119 | 4855–4861 | 6155–6162 | Types | +2 | −1 |
| 120 | 4863–4974 | 6164–6319 | Types | +54 | −10 |
| 121 | 4976–4987 | 6321–6334 | Types | +2 | −0 |
| 122 | 4989–5021 | 6336–6380 | Types | +17 | −5 |
| 123 | 5023–5043 | 6382–6406 | Types | +6 | −2 |
| 124 | 5059–5065 | 6422–6428 | Client | +1 | −1 |
| 125 | 5111–5117 | 6474–6480 | Client | +1 | −1 |
| 126 | 5135–5145 | 6498–6508 | Client | +2 | −2 |
| 127 | 5179–5185 | 6542–6548 | Client | +1 | −1 |
| 128 | 5207–5213 | 6570–6576 | Client | +1 | −1 |
| 129 | 5227–5245 | 6590–6608 | Client | +4 | −4 |
| 130 | 5267–5273 | 6630–6636 | Client | +1 | −1 |
| 131 | 5299–5305 | 6662–6668 | Client | +1 | −1 |
| 132 | 5319–5325 | 6682–6688 | Client | +1 | −1 |
| 133 | 5335–5341 | 6698–6704 | Client | +1 | −1 |
| 134 | 5347–5353 | 6710–6716 | Client | +1 | −1 |
| 135 | 5383–5389 | 6746–6752 | Client | +1 | −1 |
| 136 | 5427–5449 | 6790–6812 | Client | +5 | −5 |
| 137 | 5459–5465 | 6822–6828 | Client | +1 | −1 |
| 138 | 5471–5477 | 6834–6840 | Client | +1 | −1 |
| 139 | 5515–5525 | 6878–6888 | Client | +2 | −2 |
| 140 | 5599–5605 | 6962–6968 | Client | +1 | −1 |
| 141 | 5663–5669 | 7026–7032 | Client | +1 | −1 |
| 142 | 5683–5689 | 7046–7052 | Client | +1 | −1 |
| 143 | 5715–5721 | 7078–7084 | Client | +1 | −1 |
| 144 | 5755–5761 | 7118–7124 | Client | +1 | −1 |
| 145 | 5763–5769 | 7126–7132 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- discord/old/ballerinax_discord.bal.txt	2026-08-12 12:57:30
+++ discord/new/ballerinax_discord.bal.txt	2026-08-12 13:19:19
@@ -113,34 +113,41 @@
 
 // --- Types ---
 
-// Unknown type: KeywordUpsertRequestPartialExemptrolesItemsString
+type KeywordUpsertRequestPartialExemptrolesItemsString string;
 
-// Unknown type: VOICECHANNELSTATUSCREATE
+type VOICECHANNELSTATUSCREATE 192;
 
-// Unknown type: DATETIMEGREATERTHANEQUAL
+# the metadata value (ISO8601 string) is greater than or equal to the guild's configured value (integer; days before current date)
+type DATETIMEGREATERTHANEQUAL 6;
 
 # Represents the Headers record for the operation: update_webhook_message
 
 type UpdateWebhookMessageHeaders record {
+    @http:Header {name: "Content-Type"}
     "application/x-www-form-urlencoded" contentType;
 };
 
-// Unknown type: ZhCN
+# The zh-CN locale
+type ZhCN "zh-CN";
 
 
 type CommandPermissionResponse record {
     boolean permission;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     ApplicationCommandPermissionType 'type;
 };
 
-// Unknown type: ROLE1
+# This permission is for a role
+type ROLE1 1;
 
-// Unknown type: USER2
+# This permission is for a user
+type USER2 2;
 
-// Unknown type: CHANNEL1
+# This permission is for a channel
+type CHANNEL1 3;
 
-type ApplicationCommandPermissionType ballerinax/discord:2.0.1:ROLE1|ballerinax/discord:2.0.1:USER2|ballerinax/discord:2.0.1:CHANNEL1;
+type ApplicationCommandPermissionType ROLE1|USER2|CHANNEL1;
 
 
 type PrivateChannelRequestPartial record {
@@ -150,60 +157,84 @@
 
 
 type GuildCreateRequest record {
+    @jsondata:Name {value: "preferred_locale"}
     anydata preferredLocale?;
+    @jsondata:Name {value: "default_message_notifications"}
     anydata defaultMessageNotifications?;
     CreateGuildRequestRoleItem[]|() roles?;
-    ballerina/lang.int:0.0.0:Signed32? systemChannelFlags?;
+    @jsondata:Name {value: "system_channel_flags"}
+    int:Signed32? systemChannelFlags?;
     record {|byte[] fileContent; string fileName; anydata...;|}? icon?;
     string? description?;
+    @jsondata:Name {value: "system_channel_id"}
     anydata systemChannelId?;
+    @jsondata:Name {value: "afk_timeout"}
     anydata afkTimeout?;
+    @jsondata:Name {value: "verification_level"}
     anydata verificationLevel?;
+    @jsondata:Name {value: "explicit_content_filter"}
     anydata explicitContentFilter?;
     CreateGuildRequestChannelItem[]|() channels?;
+    @jsondata:Name {value: "afk_channel_id"}
     anydata afkChannelId?;
+    @constraint:String {maxLength: 100, minLength: 2}
     string name;
     string? region?;
 };
 
 
 type CreateGuildRequestRoleItem record {
-    ballerina/lang.int:0.0.0:Signed32? color?;
+    int:Signed32? color?;
+    @jsondata:Name {value: "unicode_emoji"}
     string? unicodeEmoji?;
-    ballerina/lang.int:0.0.0:Signed32? permissions?;
+    int:Signed32? permissions?;
     string? name?;
     boolean? mentionable?;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
     boolean? hoist?;
 };
 
 
 type CreateGuildRequestChannelItem record {
     boolean? nsfw?;
-    ballerina/lang.int:0.0.0:Signed32? rateLimitPerUser?;
-    ballerina/lang.int:0.0.0:Signed32? bitrate?;
+    @jsondata:Name {value: "rate_limit_per_user"}
+    int:Signed32? rateLimitPerUser?;
+    int:Signed32? bitrate?;
     anydata 'type?;
-    ballerina/lang.int:0.0.0:Signed32? userLimit?;
+    @jsondata:Name {value: "user_limit"}
+    int:Signed32? userLimit?;
+    @jsondata:Name {value: "permission_overwrites"}
     ChannelPermissionOverwriteRequest[]|() permissionOverwrites?;
+    @jsondata:Name {value: "rtc_region"}
     string? rtcRegion?;
-    ballerina/lang.int:0.0.0:Signed32? defaultThreadRateLimitPerUser?;
+    @jsondata:Name {value: "default_thread_rate_limit_per_user"}
+    int:Signed32? defaultThreadRateLimitPerUser?;
+    @jsondata:Name {value: "default_auto_archive_duration"}
     anydata defaultAutoArchiveDuration?;
+    @jsondata:Name {value: "parent_id"}
     anydata parentId?;
+    @jsondata:Name {value: "default_reaction_emoji"}
     anydata defaultReactionEmoji?;
+    @constraint:String {maxLength: 100, minLength: 1}
     string name;
     string? topic?;
+    @jsondata:Name {value: "default_forum_layout"}
     anydata defaultForumLayout?;
-    ballerina/lang.int:0.0.0:Signed32? position?;
+    int:Signed32? position?;
     anydata id?;
+    @jsondata:Name {value: "available_tags"}
     CreateOrUpdateThreadTagRequest[]|() availableTags?;
+    @jsondata:Name {value: "video_quality_mode"}
     anydata videoQualityMode?;
+    @jsondata:Name {value: "default_sort_order"}
     anydata defaultSortOrder?;
 };
 
 
 type ChannelPermissionOverwriteRequest record {
-    ballerina/lang.int:0.0.0:Signed32? allow?;
-    ballerina/lang.int:0.0.0:Signed32? deny?;
+    int:Signed32? allow?;
+    int:Signed32? deny?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     anydata 'type?;
 };
@@ -211,37 +242,46 @@
 
 type CreateOrUpdateThreadTagRequest record {
     boolean? moderated?;
+    @constraint:String {maxLength: 20}
     string name;
+    @jsondata:Name {value: "emoji_id"}
     anydata emojiId?;
+    @jsondata:Name {value: "emoji_name"}
     string? emojiName?;
 };
 
-// Unknown type: INVITEUPDATE
+type INVITEUPDATE 41;
 
 
 type GithubCheckSuite record {
     string? conclusion?;
     GithubCheckApp app;
+    @jsondata:Name {value: "pull_requests"}
     GithubCheckPullRequest[]|() pullRequests?;
+    @jsondata:Name {value: "head_branch"}
     string? headBranch?;
+    @jsondata:Name {value: "head_sha"}
     string headSha;
 };
 
 
 type GithubCheckApp record {
+    @constraint:String {maxLength: 152133}
     string name;
 };
 
 
 type GithubCheckPullRequest record {
-    ballerina/lang.int:0.0.0:Signed32 number;
+    int:Signed32 number;
 };
 
 
 type PartialDiscordIntegrationResponse record {
     string? name?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     "discord" 'type;
+    @jsondata:Name {value: "application_id"}
     string applicationId;
     anydata account?;
 };
@@ -249,43 +289,49 @@
 
 type PartialExternalConnectionIntegrationResponse record {
     string? name?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     IntegrationTypes 'type;
     anydata account?;
 };
 
-// Unknown type: DISCORD
+type DISCORD "discord";
 
-// Unknown type: TWITCH
+type TWITCH "twitch";
 
-// Unknown type: YOUTUBE
+type YOUTUBE "youtube";
 
-// Unknown type: GUILDSUBSCRIPTION
+type GUILDSUBSCRIPTION "guild_subscription";
 
-type IntegrationTypes ballerinax/discord:2.0.1:DISCORD|ballerinax/discord:2.0.1:TWITCH|ballerinax/discord:2.0.1:YOUTUBE|ballerinax/discord:2.0.1:GUILDSUBSCRIPTION;
+type IntegrationTypes DISCORD|TWITCH|YOUTUBE|GUILDSUBSCRIPTION;
 
 
 type PartialGuildSubscriptionIntegrationResponse record {
     string? name?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     "guild_subscription" 'type;
     anydata account?;
 };
 
-type GuildAuditLogResponseIntegrations ballerinax/discord:2.0.1:PartialDiscordIntegrationResponse|ballerinax/discord:2.0.1:PartialExternalConnectionIntegrationResponse|ballerinax/discord:2.0.1:PartialGuildSubscriptionIntegrationResponse;
+type GuildAuditLogResponseIntegrations PartialDiscordIntegrationResponse|PartialExternalConnectionIntegrationResponse|PartialGuildSubscriptionIntegrationResponse;
 
-// Unknown type: GUILDPRODUCT
+type GUILDPRODUCT 0;
 
-// Unknown type: PurchaseType
+type PurchaseType GUILDPRODUCT;
 
-// Unknown type: ROLEDELETE
+type ROLEDELETE 32;
 
 
 type UserSelect record {
+    @jsondata:Name {value: "default_values"}
     UserSelectDefaultValue[]|() defaultValues?;
-    ballerina/lang.int:0.0.0:Signed32? minValues?;
+    @jsondata:Name {value: "min_values"}
+    int:Signed32? minValues?;
+    @jsondata:Name {value: "custom_id"}
     string customId;
-    ballerina/lang.int:0.0.0:Signed32? maxValues?;
+    @jsondata:Name {value: "max_values"}
+    int:Signed32? maxValues?;
     boolean? disabled?;
     string? placeholder?;
     5 'type;
@@ -293,43 +339,53 @@
 
 
 type UserSelectDefaultValue record {
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     "user" 'type;
 };
 
-// Unknown type: WelcomeMessageResponseAuthoridsItemsString
+type WelcomeMessageResponseAuthoridsItemsString string;
 
-// Unknown type: CreatePrivateChannelRequestAccesstokensItemsString
+type CreatePrivateChannelRequestAccesstokensItemsString string;
 
 type OptionsOneOf101 anydata|();
 
-// Unknown type: THREADUPDATE
+type THREADUPDATE 111;
 
-// Unknown type: MENTIONSPAM
+# Check if content contains more unique mentions than allowed
+type MENTIONSPAM 5;
 
-// Unknown type: EMOJICREATE
+type EMOJICREATE 60;
 
-// Unknown type: HOMESETTINGSUPDATE
+type HOMESETTINGSUPDATE 191;
 
 
 type ApplicationCommandStringOptionResponse record {
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     boolean? autocomplete?;
-    ballerina/lang.int:0.0.0:Signed32? minLength?;
+    @jsondata:Name {value: "min_length"}
+    int:Signed32? minLength?;
     string name;
     string description;
+    @jsondata:Name {value: "description_localized"}
     string? descriptionLocalized?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     3 'type;
     ApplicationCommandOptionStringChoiceResponse[]|() choices?;
     boolean? required?;
-    ballerina/lang.int:0.0.0:Signed32? maxLength?;
+    @jsondata:Name {value: "max_length"}
+    int:Signed32? maxLength?;
 };
 
 
 type ApplicationCommandOptionStringChoiceResponse record {
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     string name;
     string value;
@@ -339,158 +395,214 @@
 type ConnectedAccountGuildResponse record {
     string name;
     string? icon?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
 };
 
-// Unknown type: SvSE
+# The sv-SE locale
+type SvSE "sv-SE";
 
-// Unknown type: APPLICATIONCOMMANDAUTOCOMPLETERESULT
+type APPLICATIONCOMMANDAUTOCOMPLETERESULT 8;
 
 
 type ExternalScheduledEventResponse record {
     string? image?;
     anydata creator?;
+    @jsondata:Name {value: "privacy_level"}
     GuildScheduledEventPrivacyLevels privacyLevel;
+    @jsondata:Name {value: "entity_metadata"}
     EntityMetadataExternalResponse entityMetadata;
     string? description?;
+    @jsondata:Name {value: "entity_id"}
     anydata entityId?;
+    @jsondata:Name {value: "scheduled_end_time"}
     string? scheduledEndTime?;
+    @jsondata:Name {value: "entity_type"}
     3 entityType;
+    @jsondata:Name {value: "user_rsvp"}
     anydata userRsvp?;
-    ballerina/lang.int:0.0.0:Signed32? userCount?;
+    @jsondata:Name {value: "user_count"}
+    int:Signed32? userCount?;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
     string name;
+    @jsondata:Name {value: "creator_id"}
     anydata creatorId?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
+    @jsondata:Name {value: "scheduled_start_time"}
     string scheduledStartTime;
     GuildScheduledEventStatuses status;
 };
 
-// Unknown type: GUILDONLY
+# the scheduled event is only accessible to guild members
+type GUILDONLY 2;
 
-// Unknown type: GuildScheduledEventPrivacyLevels
+type GuildScheduledEventPrivacyLevels GUILDONLY;
 
 
 type EntityMetadataExternalResponse record {
     string location;
 };
 
-// Unknown type: SCHEDULED
+type SCHEDULED 1;
 
-// Unknown type: ACTIVE
+type ACTIVE 2;
 
-// Unknown type: COMPLETED
+type COMPLETED 3;
 
-// Unknown type: CANCELED
+type CANCELED 4;
 
-type GuildScheduledEventStatuses ballerinax/discord:2.0.1:SCHEDULED|ballerinax/discord:2.0.1:ACTIVE|ballerinax/discord:2.0.1:COMPLETED|ballerinax/discord:2.0.1:CANCELED;
+type GuildScheduledEventStatuses SCHEDULED|ACTIVE|COMPLETED|CANCELED;
 
-// Unknown type: RolesOneOf13
+@constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
+type RolesOneOf13 string;
 
 type RolesRolesOneOf132 anydata|();
 
-type GuildsMembersRequestRoles ballerinax/discord:2.0.1:RolesOneOf13|anydata|();
+type GuildsMembersRequestRoles RolesOneOf13|anydata|();
 
-// Unknown type: GUILDHOMEREMOVEITEM
+type GUILDHOMEREMOVEITEM 172;
 
-// Unknown type: DOMAIN
+type DOMAIN "domain";
 
-// Unknown type: INSTAGRAM
+type INSTAGRAM "instagram";
 
 
 type InviteGuildResponse record {
     GuildFeatures[] features;
+    @jsondata:Name {value: "verification_level"}
     anydata verificationLevel?;
     boolean? nsfw?;
+    @jsondata:Name {value: "vanity_url_code"}
     string? vanityUrlCode?;
     string name;
     string? icon?;
     string? banner?;
     string? description?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
-    ballerina/lang.int:0.0.0:Signed32? premiumSubscriptionCount?;
+    @jsondata:Name {value: "premium_subscription_count"}
+    int:Signed32? premiumSubscriptionCount?;
+    @jsondata:Name {value: "nsfw_level"}
     anydata nsfwLevel?;
     string? splash?;
 };
 
-// Unknown type: ANIMATEDBANNER
+# guild has access to set an animated guild banner image
+type ANIMATEDBANNER "ANIMATED_BANNER";
 
-// Unknown type: ANIMATEDICON
+# guild has access to set an animated guild icon
+type ANIMATEDICON "ANIMATED_ICON";
 
-// Unknown type: APPLICATIONCOMMANDPERMISSIONSV2
+# guild is using the old permissions configuration behavior
+type APPLICATIONCOMMANDPERMISSIONSV2 "APPLICATION_COMMAND_PERMISSIONS_V2";
 
-// Unknown type: AUTOMODERATION
+# guild has set up auto moderation rules
+type AUTOMODERATION "AUTO_MODERATION";
 
-// Unknown type: BANNER
+# guild has access to set a guild banner image
+type BANNER "BANNER";
 
-// Unknown type: COMMUNITY
+# guild can enable welcome screen, Membership Screening, stage channels and discovery, and             receives community updates
+type COMMUNITY "COMMUNITY";
 
-// Unknown type: CREATORMONETIZABLEPROVISIONAL
+# guild has enabled monetization
+type CREATORMONETIZABLEPROVISIONAL "CREATOR_MONETIZABLE_PROVISIONAL";
 
-// Unknown type: CREATORSTOREPAGE
+# guild has enabled the role subscription promo page
+type CREATORSTOREPAGE "CREATOR_STORE_PAGE";
 
-// Unknown type: DEVELOPERSUPPORTSERVER
+# guild has been set as a support server on the App Directory
+type DEVELOPERSUPPORTSERVER "DEVELOPER_SUPPORT_SERVER";
 
-// Unknown type: DISCOVERABLE
+# guild is able to be discovered in the directory
+type DISCOVERABLE "DISCOVERABLE";
 
-// Unknown type: FEATURABLE
+# guild is able to be featured in the directory
+type FEATURABLE "FEATURABLE";
 
-// Unknown type: INVITESDISABLED
+# guild has paused invites, preventing new users from joining
+type INVITESDISABLED "INVITES_DISABLED";
 
-// Unknown type: INVITESPLASH
+# guild has access to set an invite splash background
+type INVITESPLASH "INVITE_SPLASH";
 
-// Unknown type: MEMBERVERIFICATIONGATEENABLED
+# guild has enabled Membership Screening
+type MEMBERVERIFICATIONGATEENABLED "MEMBER_VERIFICATION_GATE_ENABLED";
 
-// Unknown type: MORESTICKERS
+# guild has increased custom sticker slots
+type MORESTICKERS "MORE_STICKERS";
 
-// Unknown type: NEWS
+# guild has access to create announcement channels
+type NEWS "NEWS";
 
-// Unknown type: PARTNERED
+# guild is partnered
+type PARTNERED "PARTNERED";
 
-// Unknown type: PREVIEWENABLED
+# guild can be previewed before joining via Membership Screening or the directory
+type PREVIEWENABLED "PREVIEW_ENABLED";
 
-// Unknown type: RAIDALERTSDISABLED
+# guild has disabled activity alerts in the configured safety alerts channel
+type RAIDALERTSDISABLED "RAID_ALERTS_DISABLED";
 
-// Unknown type: ROLEICONS
+# guild is able to set role icons
+type ROLEICONS "ROLE_ICONS";
 
-// Unknown type: ROLESUBSCRIPTIONSAVAILABLEFORPURCHASE
+# guild has role subscriptions that can be purchased
+type ROLESUBSCRIPTIONSAVAILABLEFORPURCHASE "ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE";
 
-// Unknown type: ROLESUBSCRIPTIONSENABLED
+# guild has enabled role subscriptions
+type ROLESUBSCRIPTIONSENABLED "ROLE_SUBSCRIPTIONS_ENABLED";
 
-// Unknown type: TICKETEDEVENTSENABLED
+# guild has enabled ticketed events
+type TICKETEDEVENTSENABLED "TICKETED_EVENTS_ENABLED";
 
-// Unknown type: VANITYURL
+# guild has access to set a vanity URL
+type VANITYURL "VANITY_URL";
 
-// Unknown type: VERIFIED
+# guild is verified
+type VERIFIED "VERIFIED";
 
-// Unknown type: VIPREGIONS
+# guild has access to set 384kbps bitrate in voice (previously VIP voice servers)
+type VIPREGIONS "VIP_REGIONS";
 
-// Unknown type: WELCOMESCREENENABLED
+# guild has enabled the welcome screen
+type WELCOMESCREENENABLED "WELCOME_SCREEN_ENABLED";
 
-type GuildFeatures ballerinax/discord:2.0.1:ANIMATEDBANNER|ballerinax/discord:2.0.1:ANIMATEDICON|ballerinax/discord:2.0.1:APPLICATIONCOMMANDPERMISSIONSV2|ballerinax/discord:2.0.1:AUTOMODERATION|ballerinax/discord:2.0.1:BANNER|ballerinax/discord:2.0.1:COMMUNITY|ballerinax/discord:2.0.1:CREATORMONETIZABLEPROVISIONAL|ballerinax/discord:2.0.1:CREATORSTOREPAGE|ballerinax/discord:2.0.1:DEVELOPERSUPPORTSERVER|ballerinax/discord:2.0.1:DISCOVERABLE|ballerinax/discord:2.0.1:FEATURABLE|ballerinax/discord:2.0.1:INVITESDISABLED|ballerinax/discord:2.0.1:INVITESPLASH|ballerinax/discord:2.0.1:MEMBERVERIFICATIONGATEENABLED|ballerinax/discord:2.0.1:MORESTICKERS|ballerinax/discord:2.0.1:NEWS|ballerinax/discord:2.0.1:PARTNERED|ballerinax/discord:2.0.1:PREVIEWENABLED|ballerinax/discord:2.0.1:RAIDALERTSDISABLED|ballerinax/discord:2.0.1:ROLEICONS|ballerinax/discord:2.0.1:ROLESUBSCRIPTIONSAVAILABLEFORPURCHASE|ballerinax/discord:2.0.1:ROLESUBSCRIPTIONSENABLED|ballerinax/discord:2.0.1:TICKETEDEVENTSENABLED|ballerinax/discord:2.0.1:VANITYURL|ballerinax/discord:2.0.1:VERIFIED|ballerinax/discord:2.0.1:VIPREGIONS|ballerinax/discord:2.0.1:WELCOMESCREENENABLED;
+type GuildFeatures ANIMATEDBANNER|ANIMATEDICON|APPLICATIONCOMMANDPERMISSIONSV2|AUTOMODERATION|BANNER|COMMUNITY|CREATORMONETIZABLEPROVISIONAL|CREATORSTOREPAGE|DEVELOPERSUPPORTSERVER|DISCOVERABLE|FEATURABLE|INVITESDISABLED|INVITESPLASH|MEMBERVERIFICATIONGATEENABLED|MORESTICKERS|NEWS|PARTNERED|PREVIEWENABLED|RAIDALERTSDISABLED|ROLEICONS|ROLESUBSCRIPTIONSAVAILABLEFORPURCHASE|ROLESUBSCRIPTIONSENABLED|TICKETEDEVENTSENABLED|VANITYURL|VERIFIED|VIPREGIONS|WELCOMESCREENENABLED;
 
 
 type MLSpamUpsertRequest record {
+    @jsondata:Name {value: "event_type"}
     AutomodEventType eventType;
+    @jsondata:Name {value: "trigger_type"}
     3 triggerType;
+    @constraint:String {maxLength: 100}
     string name;
+    @jsondata:Name {value: "exempt_roles"}
     MLSpamUpsertRequestExemptrolesItemsString[]|() exemptRoles?;
+    @jsondata:Name {value: "exempt_channels"}
     MLSpamUpsertRequestExemptchannelsItemsString[]|() exemptChannels?;
     MLSpamUpsertRequestActions[]|() actions?;
     boolean? enabled?;
+    @jsondata:Name {value: "trigger_metadata"}
     anydata triggerMetadata?;
 };
 
-// Unknown type: MESSAGESEND
+# A user submitted a message to a channel
+type MESSAGESEND 1;
 
-// Unknown type: GUILDMEMBERJOINORUPDATE
+# A user is attempting to join the server or a member's properties were updated
+type GUILDMEMBERJOINORUPDATE 2;
 
-type AutomodEventType ballerinax/discord:2.0.1:MESSAGESEND|ballerinax/discord:2.0.1:GUILDMEMBERJOINORUPDATE;
+type AutomodEventType MESSAGESEND|GUILDMEMBERJOINORUPDATE;
 
-// Unknown type: MLSpamUpsertRequestExemptrolesItemsString
+type MLSpamUpsertRequestExemptrolesItemsString string;
 
-// Unknown type: MLSpamUpsertRequestExemptchannelsItemsString
+type MLSpamUpsertRequestExemptchannelsItemsString string;
 
 
 type BlockMessageAction record {
@@ -506,6 +618,7 @@
 
 
 type FlagToChannelActionMetadata record {
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
@@ -523,54 +636,62 @@
 
 
 type UserCommunicationDisabledActionMetadata record {
-    ballerina/lang.int:0.0.0:Signed32? durationSeconds?;
+    @jsondata:Name {value: "duration_seconds"}
+    int:Signed32? durationSeconds?;
 };
 
 type ActionsOneOf54 anydata|();
 
-type MLSpamUpsertRequestActions ballerinax/discord:2.0.1:BlockMessageAction|ballerinax/discord:2.0.1:FlagToChannelAction|ballerinax/discord:2.0.1:QuarantineUserAction|ballerinax/discord:2.0.1:UserCommunicationDisabledAction|anydata|();
+type MLSpamUpsertRequestActions BlockMessageAction|FlagToChannelAction|QuarantineUserAction|UserCommunicationDisabledAction|anydata|();
 
-// Unknown type: SkuIdsSkuIdsOneOf12OneOf1
+@constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
+type SkuIdsSkuIdsOneOf12OneOf1 string;
 
-// Unknown type: InlineArrayItemsSkuIdsSkuIdsOneOf12
+type InlineArrayItemsSkuIdsSkuIdsOneOf12 SkuIdsSkuIdsOneOf12OneOf1;
 
-// Unknown type: NONE
+type NONE 0;
 
-// Unknown type: STAGEINSTANCE
+type STAGEINSTANCE 1;
 
-// Unknown type: VOICE1
+type VOICE1 2;
 
-// Unknown type: EXTERNAL
+type EXTERNAL 3;
 
-type GuildScheduledEventEntityTypes ballerinax/discord:2.0.1:NONE|ballerinax/discord:2.0.1:STAGEINSTANCE|ballerinax/discord:2.0.1:VOICE1|ballerinax/discord:2.0.1:EXTERNAL;
+type GuildScheduledEventEntityTypes NONE|STAGEINSTANCE|VOICE1|EXTERNAL;
 
 # Represents the Queries record for the operation: update_webhook_message
 
 type UpdateWebhookMessageQueries record {
+    @http:Query {name: "thread_id"}
     string threadId?;
 };
 
-// Unknown type: UpdateThreadRequestPartialAppliedtagsItemsString
+type UpdateThreadRequestPartialAppliedtagsItemsString string;
 
-// Unknown type: Ar
+# The ar locale
+type Ar "ar";
 
-// Unknown type: MESSAGE
+# A UI-based command that shows up when you right click or tap on a message
+type MESSAGE 3;
 
-// Unknown type: PNG
+type PNG 1;
 
-// Unknown type: APNG
+type APNG 2;
 
-// Unknown type: LOTTIE
+type LOTTIE 3;
 
-// Unknown type: GIF
+type GIF 4;
 
-type StickerFormatTypes ballerinax/discord:2.0.1:PNG|ballerinax/discord:2.0.1:APNG|ballerinax/discord:2.0.1:LOTTIE|ballerinax/discord:2.0.1:GIF;
+type StickerFormatTypes PNG|APNG|LOTTIE|GIF;
 
 
 type GithubDiscussion record {
-    ballerina/lang.int:0.0.0:Signed32 number;
+    int:Signed32 number;
+    @jsondata:Name {value: "answer_html_url"}
     string? answerHtmlUrl?;
+    @jsondata:Name {value: "html_url"}
     string htmlUrl;
+    @constraint:String {maxLength: 152133}
     string title;
     string? body?;
     GithubUser user;
@@ -578,65 +699,78 @@
 
 
 type GithubUser record {
+    @jsondata:Name {value: "avatar_url"}
     string avatarUrl;
+    @jsondata:Name {value: "html_url"}
     string htmlUrl;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
+    @constraint:String {maxLength: 152133}
     string login;
 };
 
 
 type RoleSelectDefaultValue record {
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     "role" 'type;
 };
 
 type DefaultValuesOneOf3 anydata|();
 
-type MentionableSelectDefaultValues ballerinax/discord:2.0.1:RoleSelectDefaultValue|ballerinax/discord:2.0.1:UserSelectDefaultValue|anydata|();
+type MentionableSelectDefaultValues RoleSelectDefaultValue|UserSelectDefaultValue|anydata|();
 
-// Unknown type: BOTADD
+type BOTADD 28;
 
-// Unknown type: THREADSTARTERMESSAGE
+type THREADSTARTERMESSAGE 21;
 
-// Unknown type: RECIPIENTREMOVE
+type RECIPIENTREMOVE 2;
 
-// Unknown type: GUILDBOOSTTIER1
+type GUILDBOOSTTIER1 9;
 
-// Unknown type: SUCCESS
+type SUCCESS 3;
 
-// Unknown type: Bg
+# The bg locale
+type Bg "bg";
 
 type OptionsOneOf123 anydata|();
 
-// Unknown type: GUILDSMEMBERSREAD
+# allows /users/@me/guilds/{guild.id}/member to return a user's member information in a guild
+type GUILDSMEMBERSREAD "guilds.members.read";
 
 type OptionsOneOf122 anydata|();
 
 type OptionsOneOf121 anydata|();
 
-// Unknown type: NONE3
+# Guild has no MFA/2FA requirement for moderation actions
+type NONE3 0;
 
-// Unknown type: ELEVATED
+# Guild has a 2FA requirement for moderation actions
+type ELEVATED 1;
 
-type GuildMFALevel ballerinax/discord:2.0.1:NONE3|ballerinax/discord:2.0.1:ELEVATED;
+type GuildMFALevel NONE3|ELEVATED;
 
 
 type IncomingWebhookRequestPartial record {
     ActionRow[]|() components?;
     boolean? tts?;
     MessageAttachmentRequest[]|() attachments?;
+    @jsondata:Name {value: "avatar_url"}
     string? avatarUrl?;
+    @jsondata:Name {value: "thread_name"}
     string? threadName?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
+    @jsondata:Name {value: "allowed_mentions"}
     anydata allowedMentions?;
     RichEmbed[]|() embeds?;
     string? content?;
     string? username?;
+    @jsondata:Name {value: "applied_tags"}
     IncomingWebhookRequestPartialAppliedtagsItemsString[]|() appliedTags?;
 };
 
 
 type ActionRow record {
+    @constraint:Array {maxLength: 5, minLength: 1}
     ActionRowComponents[] components;
     1 'type;
 };
@@ -644,33 +778,40 @@
 
 type Button record {
     anydata emoji?;
+    @jsondata:Name {value: "custom_id"}
     string? customId?;
     ButtonStyleTypes style;
     boolean? disabled?;
+    @jsondata:Name {value: "sku_id"}
     anydata skuId?;
     string? label?;
     2 'type;
     string? url?;
 };
 
-// Unknown type: PRIMARY
+type PRIMARY 1;
 
-// Unknown type: SECONDARY
+type SECONDARY 2;
 
-// Unknown type: DANGER
+type DANGER 4;
 
-// Unknown type: LINK
+type LINK 5;
 
-// Unknown type: PREMIUM
+type PREMIUM 6;
 
-type ButtonStyleTypes ballerinax/discord:2.0.1:PRIMARY|ballerinax/discord:2.0.1:SECONDARY|ballerinax/discord:2.0.1:SUCCESS|ballerinax/discord:2.0.1:DANGER|ballerinax/discord:2.0.1:LINK|ballerinax/discord:2.0.1:PREMIUM;
+type ButtonStyleTypes PRIMARY|SECONDARY|SUCCESS|DANGER|LINK|PREMIUM;
 
 
 type ChannelSelect record {
+    @jsondata:Name {value: "default_values"}
     ChannelSelectDefaultValue[]|() defaultValues?;
-    ballerina/lang.int:0.0.0:Signed32? minValues?;
+    @jsondata:Name {value: "min_values"}
+    int:Signed32? minValues?;
+    @jsondata:Name {value: "custom_id"}
     string customId;
-    ballerina/lang.int:0.0.0:Signed32? maxValues?;
+    @jsondata:Name {value: "max_values"}
+    int:Signed32? maxValues?;
+    @jsondata:Name {value: "channel_types"}
     ChannelTypes[]|() channelTypes?;
     boolean? disabled?;
     string? placeholder?;
@@ -679,61 +820,84 @@
 
 
 type ChannelSelectDefaultValue record {
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     "channel" 'type;
 };
 
-// Unknown type: DM
+# A direct message between users
+type DM 1;
 
-// Unknown type: GROUPDM
+# A direct message between multiple users
+type GROUPDM 3;
 
-// Unknown type: GUILDTEXT
+# A text channel within a server
+type GUILDTEXT 0;
 
-// Unknown type: GUILDVOICE
+# A voice channel within a server
+type GUILDVOICE 2;
 
-// Unknown type: GUILDCATEGORY
+# An organizational category that contains up to 50 channels
+type GUILDCATEGORY 4;
 
-// Unknown type: GUILDANNOUNCEMENT
+# A channel that users can follow and crosspost into their own server (formerly news channels)
+type GUILDANNOUNCEMENT 5;
 
-// Unknown type: ANNOUNCEMENTTHREAD
+# A temporary sub-channel within a GUILD_ANNOUNCEMENT channel
+type ANNOUNCEMENTTHREAD 10;
 
-// Unknown type: PUBLICTHREAD
+# A temporary sub-channel within a GUILD_TEXT or GUILD_THREADS_ONLY channel type set
+type PUBLICTHREAD 11;
 
-// Unknown type: PRIVATETHREAD
+# A temporary sub-channel within a GUILD_TEXT channel that is only viewable by those invited and those with the MANAGE_THREADS permission
+type PRIVATETHREAD 12;
 
-// Unknown type: GUILDSTAGEVOICE
+# A voice channel for hosting events with an audience
+type GUILDSTAGEVOICE 13;
 
-// Unknown type: GUILDDIRECTORY
+# The channel in a hub containing the listed servers
+type GUILDDIRECTORY 14;
 
-// Unknown type: GUILDFORUM
+# Channel that can only contain threads
+type GUILDFORUM 15;
 
-type ChannelTypes ballerinax/discord:2.0.1:DM|ballerinax/discord:2.0.1:GROUPDM|ballerinax/discord:2.0.1:GUILDTEXT|ballerinax/discord:2.0.1:GUILDVOICE|ballerinax/discord:2.0.1:GUILDCATEGORY|ballerinax/discord:2.0.1:GUILDANNOUNCEMENT|ballerinax/discord:2.0.1:ANNOUNCEMENTTHREAD|ballerinax/discord:2.0.1:PUBLICTHREAD|ballerinax/discord:2.0.1:PRIVATETHREAD|ballerinax/discord:2.0.1:GUILDSTAGEVOICE|ballerinax/discord:2.0.1:GUILDDIRECTORY|ballerinax/discord:2.0.1:GUILDFORUM;
+type ChannelTypes DM|GROUPDM|GUILDTEXT|GUILDVOICE|GUILDCATEGORY|GUILDANNOUNCEMENT|ANNOUNCEMENTTHREAD|PUBLICTHREAD|PRIVATETHREAD|GUILDSTAGEVOICE|GUILDDIRECTORY|GUILDFORUM;
 
 
 type InputText record {
-    ballerina/lang.int:0.0.0:Signed32? minLength?;
+    @jsondata:Name {value: "min_length"}
+    int:Signed32? minLength?;
+    @jsondata:Name {value: "custom_id"}
     string customId;
     TextStyleTypes style;
+    @constraint:String {maxLength: 45}
     string label;
     string? placeholder?;
     4 'type;
     string? value?;
     boolean? required?;
-    ballerina/lang.int:0.0.0:Signed32? maxLength?;
+    @jsondata:Name {value: "max_length"}
+    int:Signed32? maxLength?;
 };
 
-// Unknown type: SHORT
+# Single-line input
+type SHORT 1;
 
-// Unknown type: PARAGRAPH
+# Multi-line input
+type PARAGRAPH 2;
 
-type TextStyleTypes ballerinax/discord:2.0.1:SHORT|ballerinax/discord:2.0.1:PARAGRAPH;
+type TextStyleTypes SHORT|PARAGRAPH;
 
 
 type MentionableSelect record {
+    @jsondata:Name {value: "default_values"}
     MentionableSelectDefaultValues[]|() defaultValues?;
-    ballerina/lang.int:0.0.0:Signed32? minValues?;
+    @jsondata:Name {value: "min_values"}
+    int:Signed32? minValues?;
+    @jsondata:Name {value: "custom_id"}
     string customId;
-    ballerina/lang.int:0.0.0:Signed32? maxValues?;
+    @jsondata:Name {value: "max_values"}
+    int:Signed32? maxValues?;
     boolean? disabled?;
     string? placeholder?;
     7 'type;
@@ -741,10 +905,14 @@
 
 
 type RoleSelect record {
+    @jsondata:Name {value: "default_values"}
     RoleSelectDefaultValue[]|() defaultValues?;
-    ballerina/lang.int:0.0.0:Signed32? minValues?;
+    @jsondata:Name {value: "min_values"}
+    int:Signed32? minValues?;
+    @jsondata:Name {value: "custom_id"}
     string customId;
-    ballerina/lang.int:0.0.0:Signed32? maxValues?;
+    @jsondata:Name {value: "max_values"}
+    int:Signed32? maxValues?;
     boolean? disabled?;
     string? placeholder?;
     6 'type;
@@ -752,9 +920,13 @@
 
 
 type StringSelect record {
-    ballerina/lang.int:0.0.0:Signed32? minValues?;
+    @jsondata:Name {value: "min_values"}
+    int:Signed32? minValues?;
+    @jsondata:Name {value: "custom_id"}
     string customId;
-    ballerina/lang.int:0.0.0:Signed32? maxValues?;
+    @jsondata:Name {value: "max_values"}
+    int:Signed32? maxValues?;
+    @constraint:Array {maxLength: 25, minLength: 1}
     SelectOption[] options;
     boolean? disabled?;
     string? placeholder?;
@@ -766,17 +938,21 @@
     boolean? default?;
     anydata emoji?;
     string? description?;
+    @constraint:String {maxLength: 100, minLength: 1}
     string label;
+    @constraint:String {maxLength: 100, minLength: 1}
     string value;
 };
 
-type ActionRowComponents ballerinax/discord:2.0.1:Button|ballerinax/discord:2.0.1:ChannelSelect|ballerinax/discord:2.0.1:InputText|ballerinax/discord:2.0.1:MentionableSelect|ballerinax/discord:2.0.1:RoleSelect|ballerinax/discord:2.0.1:StringSelect|ballerinax/discord:2.0.1:UserSelect;
+type ActionRowComponents Button|ChannelSelect|InputText|MentionableSelect|RoleSelect|StringSelect|UserSelect;
 
 
 type MessageAttachmentRequest record {
     string? filename?;
     string? description?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "is_remix"}
     boolean? isRemix?;
 };
 
@@ -784,7 +960,7 @@
 type RichEmbed record {
     anydata image?;
     anydata thumbnail?;
-    ballerina/lang.int:0.0.0:Signed32? color?;
+    int:Signed32? color?;
     anydata footer?;
     anydata author?;
     string? description?;
@@ -800,52 +976,63 @@
 
 type RichEmbedField record {
     boolean? inline?;
+    @constraint:String {maxLength: 256}
     string name;
+    @constraint:String {maxLength: 1024}
     string value;
 };
 
-// Unknown type: IncomingWebhookRequestPartialAppliedtagsItemsString
+type IncomingWebhookRequestPartialAppliedtagsItemsString string;
 
 
 type IncomingWebhookUpdateRequestPartial record {
     ActionRow[]|() components?;
     MessageAttachmentRequest[]|() attachments?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
+    @jsondata:Name {value: "allowed_mentions"}
     anydata allowedMentions?;
     RichEmbed[]|() embeds?;
     string? content?;
 };
 
-type WebhookIdwebhookTokenBody ballerinax/discord:2.0.1:IncomingWebhookRequestPartial|ballerinax/discord:2.0.1:IncomingWebhookUpdateRequestPartial;
+type WebhookIdwebhookTokenBody IncomingWebhookRequestPartial|IncomingWebhookUpdateRequestPartial;
 
 # Represents the Queries record for the operation: delete_original_webhook_message
 
 type DeleteOriginalWebhookMessageQueries record {
+    @http:Query {name: "thread_id"}
     string threadId?;
 };
 
-// Unknown type: MEMBERMOVE
+type MEMBERMOVE 26;
 
 
 type MessagesoriginalBody record {
     ActionRow[]|() components?;
     MessageAttachmentRequest[]|() attachments?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
+    @jsondata:Name {value: "allowed_mentions"}
     anydata allowedMentions?;
     RichEmbed[]|() embeds?;
     string? content?;
 };
 
-// Unknown type: PrivateGuildMemberResponseRolesItemsString
+@constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
+type PrivateGuildMemberResponseRolesItemsString string;
 
 
 type ApplicationCommandChannelOptionResponse record {
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     string name;
     string description;
+    @jsondata:Name {value: "channel_types"}
     ChannelTypes[]|() channelTypes?;
+    @jsondata:Name {value: "description_localized"}
     string? descriptionLocalized?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     7 'type;
     boolean? required?;
@@ -863,7 +1050,8 @@
 type IncomingWebhookUpdateForInteractionCallbackRequestPartial record {
     ActionRow[]|() components?;
     MessageAttachmentRequest[]|() attachments?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
+    @jsondata:Name {value: "allowed_mentions"}
     anydata allowedMentions?;
     RichEmbed[]|() embeds?;
     string? content?;
@@ -871,20 +1059,24 @@
 
 type UsersUsersOneOf12 anydata|();
 
-// Unknown type: SOUNDBOARDSOUNDDELETE
+type SOUNDBOARDSOUNDDELETE 132;
 
 
 type GuildsTemplatesRequest record {
+    @constraint:String {maxLength: 100, minLength: 2}
     string name;
     record {|byte[] fileContent; string fileName; anydata...;|}? icon?;
 };
 
 
 type GuildsChannelsRequest record {
+    @jsondata:Name {value: "lock_permissions"}
     boolean? lockPermissions?;
+    @jsondata:Name {value: "parent_id"}
     anydata parentId?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id?;
-    ballerina/lang.int:0.0.0:Signed32? position?;
+    int:Signed32? position?;
 };
 
 # OAuth2 Client Credentials Grant Configs
@@ -902,21 +1094,25 @@
     oauth2:ClientConfiguration clientConfig?; // Special Agent Note: ClientConfiguration FROM ballerina/oauth2 package
 };
 
-// Unknown type: BOOLEANEQUAL
+# the metadata value (integer) is equal to the guild's configured value (integer; 1)
+type BOOLEANEQUAL 7;
 
-// Unknown type: KeywordRuleResponseExemptchannelsItemsString
+type KeywordRuleResponseExemptchannelsItemsString string;
 
 
 type OnboardingPromptOptionResponse record {
+    @jsondata:Name {value: "channel_ids"}
     OnboardingPromptOptionResponseChannelidsItemsString[] channelIds;
     SettingsEmojiResponse emoji;
     string description;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     string title;
+    @jsondata:Name {value: "role_ids"}
     OnboardingPromptOptionResponseRoleidsItemsString[] roleIds;
 };
 
-// Unknown type: OnboardingPromptOptionResponseChannelidsItemsString
+type OnboardingPromptOptionResponseChannelidsItemsString string;
 
 
 type SettingsEmojiResponse record {
@@ -925,139 +1121,166 @@
     anydata id?;
 };
 
-// Unknown type: OnboardingPromptOptionResponseRoleidsItemsString
+type OnboardingPromptOptionResponseRoleidsItemsString string;
 
 
 type GuildsMembersRequest1 record {
     string? nick?;
+    @jsondata:Name {value: "communication_disabled_until"}
     string? communicationDisabledUntil?;
     GuildsMembersRequest1Roles[]|() roles?;
     boolean? deaf?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
     boolean? mute?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
 };
 
-// Unknown type: RolesOneOf14
+@constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
+type RolesOneOf14 string;
 
 type RolesRolesOneOf142 anydata|();
 
-type GuildsMembersRequest1Roles ballerinax/discord:2.0.1:RolesOneOf14|anydata|();
+type GuildsMembersRequest1Roles RolesOneOf14|anydata|();
 
-// Unknown type: EMAIL
+# enables /users/@me to return an email
+type EMAIL "email";
 
-// Unknown type: Cs
+# The cs locale
+type Cs "cs";
 
 
 type StageInstancesRequest record {
+    @jsondata:Name {value: "privacy_level"}
     anydata privacyLevel?;
+    @jsondata:Name {value: "send_start_notification"}
     boolean? sendStartNotification?;
+    @constraint:String {maxLength: 120, minLength: 1}
     string topic;
+    @jsondata:Name {value: "guild_scheduled_event_id"}
     anydata guildScheduledEventId?;
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
 
 type GuildWelcomeChannel record {
+    @constraint:String {maxLength: 50, minLength: 1}
     string description;
+    @jsondata:Name {value: "emoji_id"}
     anydata emojiId?;
+    @jsondata:Name {value: "emoji_name"}
     string? emojiName?;
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
 
 type KeywordTriggerMetadataResponse record {
+    @jsondata:Name {value: "keyword_filter"}
     string[] keywordFilter;
+    @jsondata:Name {value: "allow_list"}
     string[] allowList;
+    @jsondata:Name {value: "regex_patterns"}
     string[] regexPatterns;
 };
 
-// Unknown type: Da
+# The da locale
+type Da "da";
 
-// Unknown type: DEFAULT
+type DEFAULT 0;
 
-// Unknown type: RECIPIENTADD
+type RECIPIENTADD 1;
 
-// Unknown type: CALL
+type CALL 3;
 
-// Unknown type: CHANNELNAMECHANGE
+type CHANNELNAMECHANGE 4;
 
-// Unknown type: CHANNELICONCHANGE
+type CHANNELICONCHANGE 5;
 
-// Unknown type: CHANNELPINNEDMESSAGE
+type CHANNELPINNEDMESSAGE 6;
 
-// Unknown type: USERJOIN
+type USERJOIN 7;
 
-// Unknown type: GUILDBOOST
+type GUILDBOOST 8;
 
-// Unknown type: GUILDBOOSTTIER2
+type GUILDBOOSTTIER2 10;
 
-// Unknown type: GUILDBOOSTTIER3
+type GUILDBOOSTTIER3 11;
 
-// Unknown type: CHANNELFOLLOWADD
+type CHANNELFOLLOWADD 12;
 
-// Unknown type: GUILDDISCOVERYDISQUALIFIED
+type GUILDDISCOVERYDISQUALIFIED 14;
 
-// Unknown type: GUILDDISCOVERYREQUALIFIED
+type GUILDDISCOVERYREQUALIFIED 15;
 
-// Unknown type: GUILDDISCOVERYGRACEPERIODINITIALWARNING
+type GUILDDISCOVERYGRACEPERIODINITIALWARNING 16;
 
-// Unknown type: GUILDDISCOVERYGRACEPERIODFINALWARNING
+type GUILDDISCOVERYGRACEPERIODFINALWARNING 17;
 
-// Unknown type: THREADCREATED
+type THREADCREATED 18;
 
-// Unknown type: REPLY
+type REPLY 19;
 
-// Unknown type: CHATINPUTCOMMAND
+type CHATINPUTCOMMAND 20;
 
-// Unknown type: GUILDINVITEREMINDER
+type GUILDINVITEREMINDER 22;
 
-// Unknown type: CONTEXTMENUCOMMAND
+type CONTEXTMENUCOMMAND 23;
 
-// Unknown type: AUTOMODERATIONACTION
+type AUTOMODERATIONACTION 24;
 
-// Unknown type: ROLESUBSCRIPTIONPURCHASE
+type ROLESUBSCRIPTIONPURCHASE 25;
 
-// Unknown type: INTERACTIONPREMIUMUPSELL
+type INTERACTIONPREMIUMUPSELL 26;
 
-// Unknown type: STAGESTART
+type STAGESTART 27;
 
-// Unknown type: STAGEEND
+type STAGEEND 28;
 
-// Unknown type: STAGESPEAKER
+type STAGESPEAKER 29;
 
-// Unknown type: STAGETOPIC
+type STAGETOPIC 31;
 
-// Unknown type: GUILDAPPLICATIONPREMIUMSUBSCRIPTION
+type GUILDAPPLICATIONPREMIUMSUBSCRIPTION 32;
 
-// Unknown type: GUILDINCIDENTALERTMODEENABLED
+type GUILDINCIDENTALERTMODEENABLED 36;
 
-// Unknown type: GUILDINCIDENTALERTMODEDISABLED
+type GUILDINCIDENTALERTMODEDISABLED 37;
 
-// Unknown type: GUILDINCIDENTREPORTRAID
+type GUILDINCIDENTREPORTRAID 38;
 
-// Unknown type: GUILDINCIDENTREPORTFALSEALARM
+type GUILDINCIDENTREPORTFALSEALARM 39;
 
-type MessageType ballerinax/discord:2.0.1:DEFAULT|ballerinax/discord:2.0.1:RECIPIENTADD|ballerinax/discord:2.0.1:RECIPIENTREMOVE|ballerinax/discord:2.0.1:CALL|ballerinax/discord:2.0.1:CHANNELNAMECHANGE|ballerinax/discord:2.0.1:CHANNELICONCHANGE|ballerinax/discord:2.0.1:CHANNELPINNEDMESSAGE|ballerinax/discord:2.0.1:USERJOIN|ballerinax/discord:2.0.1:GUILDBOOST|ballerinax/discord:2.0.1:GUILDBOOSTTIER1|ballerinax/discord:2.0.1:GUILDBOOSTTIER2|ballerinax/discord:2.0.1:GUILDBOOSTTIER3|ballerinax/discord:2.0.1:CHANNELFOLLOWADD|ballerinax/discord:2.0.1:GUILDDISCOVERYDISQUALIFIED|ballerinax/discord:2.0.1:GUILDDISCOVERYREQUALIFIED|ballerinax/discord:2.0.1:GUILDDISCOVERYGRACEPERIODINITIALWARNING|ballerinax/discord:2.0.1:GUILDDISCOVERYGRACEPERIODFINALWARNING|ballerinax/discord:2.0.1:THREADCREATED|ballerinax/discord:2.0.1:REPLY|ballerinax/discord:2.0.1:CHATINPUTCOMMAND|ballerinax/discord:2.0.1:THREADSTARTERMESSAGE|ballerinax/discord:2.0.1:GUILDINVITEREMINDER|ballerinax/discord:2.0.1:CONTEXTMENUCOMMAND|ballerinax/discord:2.0.1:AUTOMODERATIONACTION|ballerinax/discord:2.0.1:ROLESUBSCRIPTIONPURCHASE|ballerinax/discord:2.0.1:INTERACTIONPREMIUMUPSELL|ballerinax/discord:2.0.1:STAGESTART|ballerinax/discord:2.0.1:STAGEEND|ballerinax/discord:2.0.1:STAGESPEAKER|ballerinax/discord:2.0.1:STAGETOPIC|ballerinax/discord:2.0.1:GUILDAPPLICATIONPREMIUMSUBSCRIPTION|ballerinax/discord:2.0.1:GUILDINCIDENTALERTMODEENABLED|ballerinax/discord:2.0.1:GUILDINCIDENTALERTMODEDISABLED|ballerinax/discord:2.0.1:GUILDINCIDENTREPORTRAID|ballerinax/discord:2.0.1:GUILDINCIDENTREPORTFALSEALARM;
+type MessageType DEFAULT|RECIPIENTADD|RECIPIENTREMOVE|CALL|CHANNELNAMECHANGE|CHANNELICONCHANGE|CHANNELPINNEDMESSAGE|USERJOIN|GUILDBOOST|GUILDBOOSTTIER1|GUILDBOOSTTIER2|GUILDBOOSTTIER3|CHANNELFOLLOWADD|GUILDDISCOVERYDISQUALIFIED|GUILDDISCOVERYREQUALIFIED|GUILDDISCOVERYGRACEPERIODINITIALWARNING|GUILDDISCOVERYGRACEPERIODFINALWARNING|THREADCREATED|REPLY|CHATINPUTCOMMAND|THREADSTARTERMESSAGE|GUILDINVITEREMINDER|CONTEXTMENUCOMMAND|AUTOMODERATIONACTION|ROLESUBSCRIPTIONPURCHASE|INTERACTIONPREMIUMUPSELL|STAGESTART|STAGEEND|STAGESPEAKER|STAGETOPIC|GUILDAPPLICATIONPREMIUMSUBSCRIPTION|GUILDINCIDENTALERTMODEENABLED|GUILDINCIDENTALERTMODEDISABLED|GUILDINCIDENTREPORTRAID|GUILDINCIDENTREPORTFALSEALARM;
 
 type 200AnyOf4 anydata|();
 
 # Represents the Queries record for the operation: list_guild_audit_log_entries
 
 type ListGuildAuditLogEntriesQueries record {
+    @http:Query {name: "user_id"}
     string userId?;
-    ballerina/lang.int:0.0.0:Signed32 actionType?;
+    @http:Query {name: "action_type"}
+    int:Signed32 actionType?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string before?;
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    @constraint:Int {minValue: 1, maxValue: 100}
+    int:Signed32 'limit?;
+    @http:Query {name: "target_id"}
     string targetId?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string after?;
 };
 
 
 type ConnectedAccountResponse record {
+    @jsondata:Name {value: "friend_sync"}
     boolean friendSync;
+    @jsondata:Name {value: "show_activity"}
     boolean showActivity;
     ConnectedAccountVisibility visibility;
+    @jsondata:Name {value: "two_way_link"}
     boolean twoWayLink;
     string? name?;
     boolean verified;
@@ -1067,47 +1290,47 @@
     ConnectedAccountIntegrationResponse[]|() integrations?;
 };
 
-// Unknown type: EVERYONE1
+type EVERYONE1 1;
 
-type ConnectedAccountVisibility ballerinax/discord:2.0.1:NONE|ballerinax/discord:2.0.1:EVERYONE1;
+type ConnectedAccountVisibility NONE|EVERYONE1;
 
-// Unknown type: BATTLENET
+type BATTLENET "battlenet";
 
-// Unknown type: BUNGIE
+type BUNGIE "bungie";
 
-// Unknown type: EBAY
+type EBAY "ebay";
 
-// Unknown type: EPICGAMES
+type EPICGAMES "epicgames";
 
-// Unknown type: FACEBOOK
+type FACEBOOK "facebook";
 
-// Unknown type: GITHUB
+type GITHUB "github";
 
-// Unknown type: LEAGUEOFLEGENDS
+type LEAGUEOFLEGENDS "leagueoflegends";
 
-// Unknown type: PAYPAL
+type PAYPAL "paypal";
 
-// Unknown type: PLAYSTATION
+type PLAYSTATION "playstation";
 
-// Unknown type: REDDIT
+type REDDIT "reddit";
 
-// Unknown type: RIOTGAMES
+type RIOTGAMES "riotgames";
 
-// Unknown type: ROBLOX
+type ROBLOX "roblox";
 
-// Unknown type: SKYPE
+type SKYPE "skype";
 
-// Unknown type: SPOTIFY
+type SPOTIFY "spotify";
 
-// Unknown type: STEAM
+type STEAM "steam";
 
-// Unknown type: TIKTOK
+type TIKTOK "tiktok";
 
-// Unknown type: TWITTER
+type TWITTER "twitter";
 
-// Unknown type: XBOX
+type XBOX "xbox";
 
-type ConnectedAccountProviders ballerinax/discord:2.0.1:BATTLENET|ballerinax/discord:2.0.1:BUNGIE|ballerinax/discord:2.0.1:EBAY|ballerinax/discord:2.0.1:EPICGAMES|ballerinax/discord:2.0.1:FACEBOOK|ballerinax/discord:2.0.1:GITHUB|ballerinax/discord:2.0.1:INSTAGRAM|ballerinax/discord:2.0.1:LEAGUEOFLEGENDS|ballerinax/discord:2.0.1:PAYPAL|ballerinax/discord:2.0.1:PLAYSTATION|ballerinax/discord:2.0.1:REDDIT|ballerinax/discord:2.0.1:RIOTGAMES|ballerinax/discord:2.0.1:ROBLOX|ballerinax/discord:2.0.1:SKYPE|ballerinax/discord:2.0.1:SPOTIFY|ballerinax/discord:2.0.1:STEAM|ballerinax/discord:2.0.1:TIKTOK|ballerinax/discord:2.0.1:TWITCH|ballerinax/discord:2.0.1:TWITTER|ballerinax/discord:2.0.1:XBOX|ballerinax/discord:2.0.1:YOUTUBE|ballerinax/discord:2.0.1:DOMAIN;
+type ConnectedAccountProviders BATTLENET|BUNGIE|EBAY|EPICGAMES|FACEBOOK|GITHUB|INSTAGRAM|LEAGUEOFLEGENDS|PAYPAL|PLAYSTATION|REDDIT|RIOTGAMES|ROBLOX|SKYPE|SPOTIFY|STEAM|TIKTOK|TWITCH|TWITTER|XBOX|YOUTUBE|DOMAIN;
 
 
 type ConnectedAccountIntegrationResponse record {
@@ -1123,10 +1346,12 @@
     string id;
 };
 
-// Unknown type: De
+# The de locale
+type De "de";
 
 
 type RichEmbedAuthor record {
+    @jsondata:Name {value: "icon_url"}
     string? iconUrl?;
     string? name?;
     string? url?;
@@ -1134,46 +1359,62 @@
 
 
 type GithubRepository record {
+    @jsondata:Name {value: "full_name"}
     string fullName;
+    @jsondata:Name {value: "html_url"}
     string htmlUrl;
+    @constraint:String {maxLength: 152133}
     string name;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
 };
 
 
 type ApplicationRoleConnectionsMetadataItemRequest record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string?...;|}? nameLocalizations?;
+    @constraint:String {maxLength: 100, minLength: 1}
     string name;
+    @constraint:String {maxLength: 200, minLength: 1}
     string description;
+    @jsondata:Name {value: "description_localizations"}
     record {|string?...;|}? descriptionLocalizations?;
     MetadataItemTypes 'type;
+    @constraint:String {maxLength: 50, minLength: 1}
     string 'key;
 };
 
-// Unknown type: INTEGERLESSTHANEQUAL
+# the metadata value (integer) is less than or equal to the guild's configured value (integer)
+type INTEGERLESSTHANEQUAL 1;
 
-// Unknown type: INTEGERGREATERTHANEQUAL
+# the metadata value (integer) is greater than or equal to the guild's configured value (integer)
+type INTEGERGREATERTHANEQUAL 2;
 
-// Unknown type: INTEGEREQUAL
+# the metadata value (integer) is equal to the guild's configured value (integer)
+type INTEGEREQUAL 3;
 
-// Unknown type: INTEGERNOTEQUAL
+# the metadata value (integer) is not equal to the guild's configured value (integer)
+type INTEGERNOTEQUAL 4;
 
-// Unknown type: DATETIMELESSTHANEQUAL
+# the metadata value (ISO8601 string) is less than or equal to the guild's configured value (integer; days before current date)
+type DATETIMELESSTHANEQUAL 5;
 
-// Unknown type: BOOLEANNOTEQUAL
+# the metadata value (integer) is not equal to the guild's configured value (integer; 1)
+type BOOLEANNOTEQUAL 8;
 
-type MetadataItemTypes ballerinax/discord:2.0.1:INTEGERLESSTHANEQUAL|ballerinax/discord:2.0.1:INTEGERGREATERTHANEQUAL|ballerinax/discord:2.0.1:INTEGEREQUAL|ballerinax/discord:2.0.1:INTEGERNOTEQUAL|ballerinax/discord:2.0.1:DATETIMELESSTHANEQUAL|ballerinax/discord:2.0.1:DATETIMEGREATERTHANEQUAL|ballerinax/discord:2.0.1:BOOLEANEQUAL|ballerinax/discord:2.0.1:BOOLEANNOTEQUAL;
+type MetadataItemTypes INTEGERLESSTHANEQUAL|INTEGERGREATERTHANEQUAL|INTEGEREQUAL|INTEGERNOTEQUAL|DATETIMELESSTHANEQUAL|DATETIMEGREATERTHANEQUAL|BOOLEANEQUAL|BOOLEANNOTEQUAL;
 
-// Unknown type: OnboardingPromptOptionRequestChannelidsItemsString
+type OnboardingPromptOptionRequestChannelidsItemsString string;
 
 
 type MessageComponentButtonResponse record {
     anydata emoji?;
+    @jsondata:Name {value: "custom_id"}
     string? customId?;
     ButtonStyleTypes style;
     boolean? disabled?;
+    @jsondata:Name {value: "sku_id"}
     anydata skuId?;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
     string? label?;
     2 'type;
     string? url?;
@@ -1181,218 +1422,307 @@
 
 
 type ApplicationOAuth2InstallParams record {
-    ballerina/lang.int:0.0.0:Signed32? permissions?;
+    int:Signed32? permissions?;
     OAuth2Scopes[]|() scopes?;
 };
 
-// Unknown type: IDENTIFY
+# allows /users/@me without email
+type IDENTIFY "identify";
 
-// Unknown type: CONNECTIONS
+# allows /users/@me/connections to return linked third-party accounts
+type CONNECTIONS "connections";
 
-// Unknown type: GUILDS
+# allows /users/@me/guilds to return basic information about all of a user's guilds
+type GUILDS "guilds";
 
-// Unknown type: GUILDSJOIN
+# allows /guilds/{guild.id}/members/{user.id} to be used for joining users to a guild
+type GUILDSJOIN "guilds.join";
 
-// Unknown type: GDMJOIN
+# allows your app to join users to a group dm
+type GDMJOIN "gdm.join";
 
-// Unknown type: BOT
+# for oauth2 bots, this puts the bot in the user's selected guild by default
+type BOT "bot";
 
-// Unknown type: RPC
+# for local rpc server access, this allows you to control a user's local Discord client - requires Discord approval
+type RPC "rpc";
 
-// Unknown type: RPCNOTIFICATIONSREAD
+# for local rpc server access, this allows you to receive notifications pushed out to the user - requires Discord approval
+type RPCNOTIFICATIONSREAD "rpc.notifications.read";
 
-// Unknown type: RPCVOICEREAD
+# for local rpc server access, this allows you to read a user's voice settings and listen for voice events - requires Discord approval
+type RPCVOICEREAD "rpc.voice.read";
 
-// Unknown type: RPCVOICEWRITE
+# for local rpc server access, this allows you to update a user's voice settings - requires Discord approval
+type RPCVOICEWRITE "rpc.voice.write";
 
-// Unknown type: RPCVIDEOREAD
+# for local rpc server access, this allows you to read a user's video status - requires Discord approval
+type RPCVIDEOREAD "rpc.video.read";
 
-// Unknown type: RPCVIDEOWRITE
+# for local rpc server access, this allows you to update a user's video settings - requires Discord approval
+type RPCVIDEOWRITE "rpc.video.write";
 
-// Unknown type: RPCSCREENSHAREREAD
+# for local rpc server access, this allows you to read a user's screenshare status- requires Discord approval
+type RPCSCREENSHAREREAD "rpc.screenshare.read";
 
-// Unknown type: RPCSCREENSHAREWRITE
+# for local rpc server access, this allows you to update a user's screenshare settings- requires Discord approval
+type RPCSCREENSHAREWRITE "rpc.screenshare.write";
 
-// Unknown type: RPCACTIVITIESWRITE
+# for local rpc server access, this allows you to update a user's activity - requires Discord approval
+type RPCACTIVITIESWRITE "rpc.activities.write";
 
-// Unknown type: WEBHOOKINCOMING
+# this generates a webhook that is returned in the oauth token response for authorization code grants
+type WEBHOOKINCOMING "webhook.incoming";
 
-// Unknown type: MESSAGESREAD
+# for local rpc server api access, this allows you to read messages from all client channels (otherwise restricted to channels/guilds your app creates)
+type MESSAGESREAD "messages.read";
 
-// Unknown type: APPLICATIONSBUILDSUPLOAD
+# allows your app to upload/update builds for a user's applications - requires Discord approval
+type APPLICATIONSBUILDSUPLOAD "applications.builds.upload";
 
-// Unknown type: APPLICATIONSBUILDSREAD
+# allows your app to read build data for a user's applications
+type APPLICATIONSBUILDSREAD "applications.builds.read";
 
-// Unknown type: APPLICATIONSCOMMANDS
+# allows your app to use commands in a guild
+type APPLICATIONSCOMMANDS "applications.commands";
 
-// Unknown type: APPLICATIONSCOMMANDSPERMISSIONSUPDATE
+# allows your app to update permissions for its commands in a guild a user has permissions to
+type APPLICATIONSCOMMANDSPERMISSIONSUPDATE "applications.commands.permissions.update";
 
-// Unknown type: APPLICATIONSCOMMANDSUPDATE
+# allows your app to update its commands using a Bearer token - client credentials grant only
+type APPLICATIONSCOMMANDSUPDATE "applications.commands.update";
 
-// Unknown type: APPLICATIONSSTOREUPDATE
+# allows your app to read and update store data (SKUs, store listings, achievements, etc.) for a user's applications
+type APPLICATIONSSTOREUPDATE "applications.store.update";
 
-// Unknown type: APPLICATIONSENTITLEMENTS
+# allows your app to read entitlements for a user's applications
+type APPLICATIONSENTITLEMENTS "applications.entitlements";
 
-// Unknown type: ACTIVITIESREAD
+# allows your app to fetch data from a user's "Now Playing/Recently Played" list - requires Discord approval
+type ACTIVITIESREAD "activities.read";
 
-// Unknown type: ACTIVITIESWRITE
+# allows your app to update a user's activity - requires Discord approval (NOT REQUIRED FOR GAMESDK ACTIVITY MANAGER)
+type ACTIVITIESWRITE "activities.write";
 
-// Unknown type: RELATIONSHIPSREAD
+# allows your app to know a user's friends and implicit relationships - requires Discord approval
+type RELATIONSHIPSREAD "relationships.read";
 
-// Unknown type: VOICE
+# allows your app to connect to voice on user's behalf and see all the voice members - requires Discord approval
+type VOICE "voice";
 
-// Unknown type: DMCHANNELSREAD
+# allows your app to see information about the user's DMs and group DMs - requires Discord approval
+type DMCHANNELSREAD "dm_channels.read";
 
-// Unknown type: ROLECONNECTIONSWRITE
+# allows your app to update a user's connection and metadata for the app
+type ROLECONNECTIONSWRITE "role_connections.write";
 
-// Unknown type: OPENID
+# for OpenID Connect, this allows your app to receive user id and basic profile information
+type OPENID "openid";
 
-type OAuth2Scopes ballerinax/discord:2.0.1:IDENTIFY|ballerinax/discord:2.0.1:EMAIL|ballerinax/discord:2.0.1:CONNECTIONS|ballerinax/discord:2.0.1:GUILDS|ballerinax/discord:2.0.1:GUILDSJOIN|ballerinax/discord:2.0.1:GUILDSMEMBERSREAD|ballerinax/discord:2.0.1:GDMJOIN|ballerinax/discord:2.0.1:BOT|ballerinax/discord:2.0.1:RPC|ballerinax/discord:2.0.1:RPCNOTIFICATIONSREAD|ballerinax/discord:2.0.1:RPCVOICEREAD|ballerinax/discord:2.0.1:RPCVOICEWRITE|ballerinax/discord:2.0.1:RPCVIDEOREAD|ballerinax/discord:2.0.1:RPCVIDEOWRITE|ballerinax/discord:2.0.1:RPCSCREENSHAREREAD|ballerinax/discord:2.0.1:RPCSCREENSHAREWRITE|ballerinax/discord:2.0.1:RPCACTIVITIESWRITE|ballerinax/discord:2.0.1:WEBHOOKINCOMING|ballerinax/discord:2.0.1:MESSAGESREAD|ballerinax/discord:2.0.1:APPLICATIONSBUILDSUPLOAD|ballerinax/discord:2.0.1:APPLICATIONSBUILDSREAD|ballerinax/discord:2.0.1:APPLICATIONSCOMMANDS|ballerinax/discord:2.0.1:APPLICATIONSCOMMANDSPERMISSIONSUPDATE|ballerinax/discord:2.0.1:APPLICATIONSCOMMANDSUPDATE|ballerinax/discord:2.0.1:APPLICATIONSSTOREUPDATE|ballerinax/discord:2.0.1:APPLICATIONSENTITLEMENTS|ballerinax/discord:2.0.1:ACTIVITIESREAD|ballerinax/discord:2.0.1:ACTIVITIESWRITE|ballerinax/discord:2.0.1:RELATIONSHIPSREAD|ballerinax/discord:2.0.1:VOICE|ballerinax/discord:2.0.1:DMCHANNELSREAD|ballerinax/discord:2.0.1:ROLECONNECTIONSWRITE|ballerinax/discord:2.0.1:OPENID;
+type OAuth2Scopes IDENTIFY|EMAIL|CONNECTIONS|GUILDS|GUILDSJOIN|GUILDSMEMBERSREAD|GDMJOIN|BOT|RPC|RPCNOTIFICATIONSREAD|RPCVOICEREAD|RPCVOICEWRITE|RPCVIDEOREAD|RPCVIDEOWRITE|RPCSCREENSHAREREAD|RPCSCREENSHAREWRITE|RPCACTIVITIESWRITE|WEBHOOKINCOMING|MESSAGESREAD|APPLICATIONSBUILDSUPLOAD|APPLICATIONSBUILDSREAD|APPLICATIONSCOMMANDS|APPLICATIONSCOMMANDSPERMISSIONSUPDATE|APPLICATIONSCOMMANDSUPDATE|APPLICATIONSSTOREUPDATE|APPLICATIONSENTITLEMENTS|ACTIVITIESREAD|ACTIVITIESWRITE|RELATIONSHIPSREAD|VOICE|DMCHANNELSREAD|ROLECONNECTIONSWRITE|OPENID;
 
 
 type GuildTemplateSnapshotResponse record {
+    @jsondata:Name {value: "preferred_locale"}
     AvailableLocalesEnum preferredLocale;
+    @jsondata:Name {value: "default_message_notifications"}
     UserNotificationSettings defaultMessageNotifications;
-    ballerina/lang.int:0.0.0:Signed32 systemChannelFlags;
+    @jsondata:Name {value: "system_channel_flags"}
+    int:Signed32 systemChannelFlags;
     GuildTemplateRoleResponse[] roles;
     string? description?;
+    @jsondata:Name {value: "system_channel_id"}
     anydata systemChannelId?;
+    @jsondata:Name {value: "afk_timeout"}
     AfkTimeouts afkTimeout;
+    @jsondata:Name {value: "verification_level"}
     VerificationLevels verificationLevel;
+    @jsondata:Name {value: "explicit_content_filter"}
     GuildExplicitContentFilterTypes explicitContentFilter;
     GuildTemplateChannelResponse[] channels;
+    @jsondata:Name {value: "afk_channel_id"}
     anydata afkChannelId?;
     string name;
     string? region?;
 };
 
-// Unknown type: El
+# The el locale
+type El "el";
 
-// Unknown type: EnGB
+# The en-GB locale
+type EnGB "en-GB";
 
-// Unknown type: EnUS
+# The en-US locale
+type EnUS "en-US";
 
-// Unknown type: Es419
+# The es-419 locale
+type Es419 "es-419";
 
-// Unknown type: EsES
+# The es-ES locale
+type EsES "es-ES";
 
-// Unknown type: Fi
+# The fi locale
+type Fi "fi";
 
-// Unknown type: Fr
+# The fr locale
+type Fr "fr";
 
-// Unknown type: He
+# The he locale
+type He "he";
 
-// Unknown type: Hi
+# The hi locale
+type Hi "hi";
 
-// Unknown type: Hr
+# The hr locale
+type Hr "hr";
 
-// Unknown type: Hu
+# The hu locale
+type Hu "hu";
 
-// Unknown type: Id
-
-// Unknown type: It
+# The id locale
+type Id "id";
 
-// Unknown type: Ja
+# The it locale
+type It "it";
 
-// Unknown type: Ko
+# The ja locale
+type Ja "ja";
 
-// Unknown type: Lt
+# The ko locale
+type Ko "ko";
 
-// Unknown type: Nl
+# The lt locale
+type Lt "lt";
 
-// Unknown type: No
+# The nl locale
+type Nl "nl";
 
-// Unknown type: Pl
+# The no locale
+type No "no";
 
-// Unknown type: PtBR
+# The pl locale
+type Pl "pl";
 
-// Unknown type: Ro
+# The pt-BR locale
+type PtBR "pt-BR";
 
-// Unknown type: Ru
+# The ro locale
+type Ro "ro";
 
-// Unknown type: Th
+# The ru locale
+type Ru "ru";
 
-// Unknown type: Tr
+# The th locale
+type Th "th";
 
-// Unknown type: Uk
+# The tr locale
+type Tr "tr";
 
-// Unknown type: Vi
+# The uk locale
+type Uk "uk";
 
-// Unknown type: ZhTW
+# The vi locale
+type Vi "vi";
 
-type AvailableLocalesEnum ballerinax/discord:2.0.1:Ar|ballerinax/discord:2.0.1:Bg|ballerinax/discord:2.0.1:Cs|ballerinax/discord:2.0.1:Da|ballerinax/discord:2.0.1:De|ballerinax/discord:2.0.1:El|ballerinax/discord:2.0.1:EnGB|ballerinax/discord:2.0.1:EnUS|ballerinax/discord:2.0.1:Es419|ballerinax/discord:2.0.1:EsES|ballerinax/discord:2.0.1:Fi|ballerinax/discord:2.0.1:Fr|ballerinax/discord:2.0.1:He|ballerinax/discord:2.0.1:Hi|ballerinax/discord:2.0.1:Hr|ballerinax/discord:2.0.1:Hu|ballerinax/discord:2.0.1:Id|ballerinax/discord:2.0.1:It|ballerinax/discord:2.0.1:Ja|ballerinax/discord:2.0.1:Ko|ballerinax/discord:2.0.1:Lt|ballerinax/discord:2.0.1:Nl|ballerinax/discord:2.0.1:No|ballerinax/discord:2.0.1:Pl|ballerinax/discord:2.0.1:PtBR|ballerinax/discord:2.0.1:Ro|ballerinax/discord:2.0.1:Ru|ballerinax/discord:2.0.1:SvSE|ballerinax/discord:2.0.1:Th|ballerinax/discord:2.0.1:Tr|ballerinax/discord:2.0.1:Uk|ballerinax/discord:2.0.1:Vi|ballerinax/discord:2.0.1:ZhCN|ballerinax/discord:2.0.1:ZhTW;
+# The zh-TW locale
+type ZhTW "zh-TW";
 
-// Unknown type: ALLMESSAGES
+type AvailableLocalesEnum Ar|Bg|Cs|Da|De|El|EnGB|EnUS|Es419|EsES|Fi|Fr|He|Hi|Hr|Hu|Id|It|Ja|Ko|Lt|Nl|No|Pl|PtBR|Ro|Ru|SvSE|Th|Tr|Uk|Vi|ZhCN|ZhTW;
 
-// Unknown type: ONLYMENTIONS
+# members will receive notifications for all messages by default
+type ALLMESSAGES 0;
 
-type UserNotificationSettings ballerinax/discord:2.0.1:ALLMESSAGES|ballerinax/discord:2.0.1:ONLYMENTIONS;
+# members will receive notifications only for messages that @mention them by default
+type ONLYMENTIONS 1;
 
+type UserNotificationSettings ALLMESSAGES|ONLYMENTIONS;
 
+
 type GuildTemplateRoleResponse record {
-    ballerina/lang.int:0.0.0:Signed32 color;
+    int:Signed32 color;
+    @jsondata:Name {value: "unicode_emoji"}
     string? unicodeEmoji?;
     string permissions;
     string name;
     string? icon?;
     boolean mentionable;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
     boolean hoist;
 };
 
-// Unknown type: ONEMINUTE
+type ONEMINUTE 60;
 
-// Unknown type: FIVEMINUTES
+type FIVEMINUTES 300;
 
-// Unknown type: FIFTEENMINUTES
+type FIFTEENMINUTES 900;
 
-// Unknown type: THIRTYMINUTES
+type THIRTYMINUTES 1800;
 
-// Unknown type: ONEHOUR
+type ONEHOUR 3600;
 
-type AfkTimeouts ballerinax/discord:2.0.1:ONEMINUTE|ballerinax/discord:2.0.1:FIVEMINUTES|ballerinax/discord:2.0.1:FIFTEENMINUTES|ballerinax/discord:2.0.1:THIRTYMINUTES|ballerinax/discord:2.0.1:ONEHOUR;
+type AfkTimeouts ONEMINUTE|FIVEMINUTES|FIFTEENMINUTES|THIRTYMINUTES|ONEHOUR;
 
-// Unknown type: NONE2
+# unrestricted
+type NONE2 0;
 
-// Unknown type: LOW
+# must have verified email on account
+type LOW 1;
 
-// Unknown type: MEDIUM
+# must be registered on Discord for longer than 5 minutes
+type MEDIUM 2;
 
-// Unknown type: HIGH
+# must be a member of the server for longer than 10 minutes
+type HIGH 3;
 
-// Unknown type: VERYHIGH
+# must have a verified phone number
+type VERYHIGH 4;
 
-type VerificationLevels ballerinax/discord:2.0.1:NONE2|ballerinax/discord:2.0.1:LOW|ballerinax/discord:2.0.1:MEDIUM|ballerinax/discord:2.0.1:HIGH|ballerinax/discord:2.0.1:VERYHIGH;
+type VerificationLevels NONE2|LOW|MEDIUM|HIGH|VERYHIGH;
 
-// Unknown type: DISABLED
+# media content will not be scanned
+type DISABLED 0;
 
-// Unknown type: MEMBERSWITHOUTROLES
+# media content sent by members without roles will be scanned
+type MEMBERSWITHOUTROLES 1;
 
-// Unknown type: ALLMEMBERS
+# media content sent by all members will be scanned
+type ALLMEMBERS 2;
 
-type GuildExplicitContentFilterTypes ballerinax/discord:2.0.1:DISABLED|ballerinax/discord:2.0.1:MEMBERSWITHOUTROLES|ballerinax/discord:2.0.1:ALLMEMBERS;
+type GuildExplicitContentFilterTypes DISABLED|MEMBERSWITHOUTROLES|ALLMEMBERS;
 
 
 type GuildTemplateChannelResponse record {
     string template;
-    ballerina/lang.int:0.0.0:Signed32? themeColor?;
+    @jsondata:Name {value: "theme_color"}
+    int:Signed32? themeColor?;
     boolean nsfw;
+    @jsondata:Name {value: "icon_emoji"}
     anydata iconEmoji?;
-    ballerina/lang.int:0.0.0:Signed32 rateLimitPerUser;
-    ballerina/lang.int:0.0.0:Signed32 bitrate;
+    @jsondata:Name {value: "rate_limit_per_user"}
+    int:Signed32 rateLimitPerUser;
+    int:Signed32 bitrate;
     ChannelTypes 'type;
-    ballerina/lang.int:0.0.0:Signed32 userLimit;
+    @jsondata:Name {value: "user_limit"}
+    int:Signed32 userLimit;
+    @jsondata:Name {value: "permission_overwrites"}
     GuildTemplateChannelResponsePermissionOverwrites[] permissionOverwrites;
-    ballerina/lang.int:0.0.0:Signed32? defaultThreadRateLimitPerUser?;
+    @jsondata:Name {value: "default_thread_rate_limit_per_user"}
+    int:Signed32? defaultThreadRateLimitPerUser?;
+    @jsondata:Name {value: "default_auto_archive_duration"}
     anydata defaultAutoArchiveDuration?;
+    @jsondata:Name {value: "parent_id"}
     anydata parentId?;
+    @jsondata:Name {value: "default_reaction_emoji"}
     anydata defaultReactionEmoji?;
     string? name?;
     string? topic?;
+    @jsondata:Name {value: "default_forum_layout"}
     anydata defaultForumLayout?;
-    ballerina/lang.int:0.0.0:Signed32? id?;
-    ballerina/lang.int:0.0.0:Signed32? position?;
+    int:Signed32? id?;
+    int:Signed32? position?;
+    @jsondata:Name {value: "available_tags"}
     GuildTemplateChannelTags[]|() availableTags?;
+    @jsondata:Name {value: "default_sort_order"}
     anydata defaultSortOrder?;
 };
 
@@ -1400,20 +1730,22 @@
 type ChannelPermissionOverwriteResponse record {
     string allow;
     string deny;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     ChannelPermissionOverwrites 'type;
 };
 
-// Unknown type: ROLE2
+type ROLE2 0;
 
-// Unknown type: MEMBER
+type MEMBER 1;
 
-type ChannelPermissionOverwrites ballerinax/discord:2.0.1:ROLE2|ballerinax/discord:2.0.1:MEMBER;
+type ChannelPermissionOverwrites ROLE2|MEMBER;
 
 
 type GuildTemplateChannelResponsePermissionOverwrites record {
     string allow;
     string deny;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     ChannelPermissionOverwrites 'type;
 };
@@ -1422,28 +1754,38 @@
 type GuildTemplateChannelTags record {
     boolean? moderated?;
     string name;
+    @jsondata:Name {value: "emoji_id"}
     anydata emojiId?;
+    @jsondata:Name {value: "emoji_name"}
     string? emojiName?;
 };
 
 
 type MentionSpamRuleResponse record {
+    @jsondata:Name {value: "event_type"}
     AutomodEventType eventType;
+    @jsondata:Name {value: "trigger_type"}
     5 triggerType;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
+    @jsondata:Name {value: "creator_id"}
     string creatorId;
     string name;
+    @jsondata:Name {value: "exempt_roles"}
     MentionSpamRuleResponseExemptrolesItemsString[]|() exemptRoles?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "exempt_channels"}
     MentionSpamRuleResponseExemptchannelsItemsString[]|() exemptChannels?;
     DefaultKeywordRuleResponseActions[] actions;
     boolean? enabled?;
+    @jsondata:Name {value: "trigger_metadata"}
     MentionSpamTriggerMetadataResponse triggerMetadata;
 };
 
-// Unknown type: MentionSpamRuleResponseExemptrolesItemsString
+type MentionSpamRuleResponseExemptrolesItemsString string;
 
-// Unknown type: MentionSpamRuleResponseExemptchannelsItemsString
+type MentionSpamRuleResponseExemptchannelsItemsString string;
 
 
 type BlockMessageActionResponse record {
@@ -1453,6 +1795,7 @@
 
 
 type BlockMessageActionMetadataResponse record {
+    @jsondata:Name {value: "custom_message"}
     string? customMessage?;
 };
 
@@ -1464,6 +1807,7 @@
 
 
 type FlagToChannelActionMetadataResponse record {
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
@@ -1481,22 +1825,26 @@
 
 
 type UserCommunicationDisabledActionMetadataResponse record {
-    ballerina/lang.int:0.0.0:Signed32 durationSeconds;
+    @jsondata:Name {value: "duration_seconds"}
+    int:Signed32 durationSeconds;
 };
 
-type DefaultKeywordRuleResponseActions ballerinax/discord:2.0.1:BlockMessageActionResponse|ballerinax/discord:2.0.1:FlagToChannelActionResponse|ballerinax/discord:2.0.1:QuarantineUserActionResponse|ballerinax/discord:2.0.1:UserCommunicationDisabledActionResponse;
+type DefaultKeywordRuleResponseActions BlockMessageActionResponse|FlagToChannelActionResponse|QuarantineUserActionResponse|UserCommunicationDisabledActionResponse;
 
 
 type MentionSpamTriggerMetadataResponse record {
-    ballerina/lang.int:0.0.0:Signed32 mentionTotalLimit;
+    @jsondata:Name {value: "mention_total_limit"}
+    int:Signed32 mentionTotalLimit;
 };
 
-// Unknown type: ZEROES
+type ZEROES "0000";
 
 
 type UsersMeApplicationsRoleConnectionRequest record {
     record {|string...;|}? metadata?;
+    @jsondata:Name {value: "platform_username"}
     string? platformUsername?;
+    @jsondata:Name {value: "platform_name"}
     string? platformName?;
 };
 
@@ -1507,7 +1855,7 @@
     string? value?;
 };
 
-// Unknown type: GUILDSCHEDULEDEVENTUPDATE
+type GUILDSCHEDULEDEVENTUPDATE 101;
 
 # OAuth2 Refresh Token Grant Configs
 
@@ -1529,6 +1877,7 @@
 type DiscordIntegrationResponse record {
     IntegrationApplicationResponse application;
     string? name?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     OAuth2Scopes[] scopes;
     "discord" 'type;
@@ -1543,46 +1892,62 @@
     string name;
     string? icon?;
     string description;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "cover_image"}
     string? coverImage?;
+    @jsondata:Name {value: "primary_sku_id"}
     anydata primarySkuId?;
     anydata 'type?;
 };
 
-// Unknown type: INVITED
+# User has been invited to the team
+type INVITED 1;
 
-// Unknown type: ACCEPTED
+# User has accepted the team invitation
+type ACCEPTED 2;
 
-type TeamMembershipStates ballerinax/discord:2.0.1:INVITED|ballerinax/discord:2.0.1:ACCEPTED;
+type TeamMembershipStates INVITED|ACCEPTED;
 
-// Unknown type: SLURS
+# Words and phrases that may be considered slurs and hate speech
+type SLURS 3;
 
 
 type PrivateGroupChannelResponse record {
+    @jsondata:Name {value: "last_message_id"}
     anydata lastMessageId?;
+    @jsondata:Name {value: "last_pin_timestamp"}
     string? lastPinTimestamp?;
     UserResponse[] recipients;
+    @jsondata:Name {value: "owner_id"}
     anydata ownerId?;
     boolean? managed?;
-    ballerina/lang.int:0.0.0:Signed32 flags;
+    int:Signed32 flags;
     string? name?;
     string? icon?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     3 'type;
+    @jsondata:Name {value: "application_id"}
     anydata applicationId?;
 };
 
 
 type UserResponse record {
-    ballerina/lang.int:0.0.0:Signed32? accentColor?;
+    @jsondata:Name {value: "accent_color"}
+    int:Signed32? accentColor?;
     boolean? system?;
+    @jsondata:Name {value: "global_name"}
     string? globalName?;
     boolean? bot?;
+    @constraint:Int {minValue: -9007199254740991, maxValue: 9007199254740991}
     int flags;
     string? banner?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     string? avatar?;
-    ballerina/lang.int:0.0.0:Signed32 publicFlags;
+    @jsondata:Name {value: "public_flags"}
+    int:Signed32 publicFlags;
     string username;
     string discriminator;
 };
@@ -1590,22 +1955,28 @@
 
 type DefaultKeywordListTriggerMetadata record {
     AutomodKeywordPresetType[]|() presets?;
+    @jsondata:Name {value: "allow_list"}
     DefaultKeywordListTriggerMetadataAllowlistItemsString[]|() allowList?;
 };
 
-// Unknown type: PROFANITY
+# Words and phrases that may be considered profanity
+type PROFANITY 1;
 
-// Unknown type: SEXUALCONTENT
+# Words and phrases that may be considered as sexual content
+type SEXUALCONTENT 2;
 
-type AutomodKeywordPresetType ballerinax/discord:2.0.1:PROFANITY|ballerinax/discord:2.0.1:SEXUALCONTENT|ballerinax/discord:2.0.1:SLURS;
+type AutomodKeywordPresetType PROFANITY|SEXUALCONTENT|SLURS;
 
-// Unknown type: DefaultKeywordListTriggerMetadataAllowlistItemsString
+type DefaultKeywordListTriggerMetadataAllowlistItemsString string;
 
-// Unknown type: DROPDOWN
+# Many options shown as a dropdown
+type DROPDOWN 1;
 
 
 type TeamMemberResponse record {
+    @jsondata:Name {value: "membership_state"}
     TeamMembershipStates membershipState;
+    @jsondata:Name {value: "team_id"}
     string teamId;
     UserResponse user;
 };
@@ -1617,53 +1988,66 @@
 
 
 type CreateTextThreadWithoutMessageRequest record {
-    ballerina/lang.int:0.0.0:Signed32? rateLimitPerUser?;
+    @jsondata:Name {value: "rate_limit_per_user"}
+    int:Signed32? rateLimitPerUser?;
+    @constraint:String {maxLength: 100, minLength: 1}
     string name;
     boolean? invitable?;
     anydata 'type?;
+    @jsondata:Name {value: "auto_archive_duration"}
     anydata autoArchiveDuration?;
 };
 
 
 type GuildsEmojisRequest record {
     GuildsEmojisRequestRoles[]|() roles?;
+    @constraint:String {maxLength: 32, minLength: 2}
     string name?;
 };
 
-// Unknown type: RolesOneOf11
+@constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
+type RolesOneOf11 string;
 
 type RolesRolesOneOf112 anydata|();
 
-type GuildsEmojisRequestRoles ballerinax/discord:2.0.1:RolesOneOf11|anydata|();
+type GuildsEmojisRequestRoles RolesOneOf11|anydata|();
 
-// Unknown type: IncludeRolesOneOf1
+type IncludeRolesOneOf1 string;
 
-// Unknown type: IncludeRolesIncludeRolesOneOf12OneOf1
+@constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
+type IncludeRolesIncludeRolesOneOf12OneOf1 string;
 
-// Unknown type: InlineArrayItemsIncludeRolesIncludeRolesOneOf12
+type InlineArrayItemsIncludeRolesIncludeRolesOneOf12 IncludeRolesIncludeRolesOneOf12OneOf1;
 
-// Unknown type: IncludeRolesIncludeRolesOneOf12
+@constraint:Array {maxLength: 100}
+type IncludeRolesIncludeRolesOneOf12 InlineArrayItemsIncludeRolesIncludeRolesOneOf12[];
 
-type IncludeRoles ballerinax/discord:2.0.1:IncludeRolesOneOf1|ballerinax/discord:2.0.1:IncludeRolesIncludeRolesOneOf12;
+type IncludeRoles IncludeRolesOneOf1|IncludeRolesIncludeRolesOneOf12;
 
 
 type MessagesmessageIdBody record {
     ActionRow[]|() components?;
     MessageAttachmentRequest[]|() attachments?;
+    @jsondata:Name {value: "sticker_ids"}
     MessagesmessageIdBodyStickeridsItemsString[]|() stickerIds?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
+    @jsondata:Name {value: "allowed_mentions"}
     anydata allowedMentions?;
     RichEmbed[]|() embeds?;
     string? content?;
 };
 
-// Unknown type: MessagesmessageIdBodyStickeridsItemsString
+type MessagesmessageIdBodyStickeridsItemsString string;
 
 
 type ApplicationCommandAttachmentOption record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
+    @constraint:String {maxLength: 32, minLength: 1}
     string name;
+    @constraint:String {maxLength: 100, minLength: 1}
     string description;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     11 'type;
     boolean? required?;
@@ -1671,44 +2055,60 @@
 
 
 type MessageComponentMentionableSelectResponse record {
-    ballerina/lang.int:0.0.0:Signed32? minValues?;
+    @jsondata:Name {value: "min_values"}
+    int:Signed32? minValues?;
+    @jsondata:Name {value: "custom_id"}
     string customId;
-    ballerina/lang.int:0.0.0:Signed32? maxValues?;
+    @jsondata:Name {value: "max_values"}
+    int:Signed32? maxValues?;
     boolean? disabled?;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
     string? placeholder?;
     7 'type;
 };
 
 
 type ModalInteractionCallbackData record {
+    @constraint:Array {maxLength: 5, minLength: 1}
     ActionRow[] components;
+    @jsondata:Name {value: "custom_id"}
     string customId;
+    @constraint:String {maxLength: 45}
     string title;
 };
 
-// Unknown type: MULTIPLECHOICE
+# Multiple choice options
+type MULTIPLECHOICE 0;
 
 # Represents the Queries record for the operation: list_message_reactions_by_emoji
 
 type ListMessageReactionsByEmojiQueries record {
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    @constraint:Int {minValue: 1, maxValue: 100}
+    int:Signed32 'limit?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string after?;
 };
 
 
 type MessageEmbedFooterResponse record {
+    @jsondata:Name {value: "icon_url"}
     string? iconUrl?;
+    @jsondata:Name {value: "proxy_icon_url"}
     string? proxyIconUrl?;
     string text;
 };
 
 
 type ApplicationCommandChannelOption record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
+    @constraint:String {maxLength: 32, minLength: 1}
     string name;
+    @constraint:String {maxLength: 100, minLength: 1}
     string description;
+    @jsondata:Name {value: "channel_types"}
     ChannelTypes[]|() channelTypes?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     7 'type;
     boolean? required?;
@@ -1716,12 +2116,15 @@
 
 
 type MessageComponentStringSelectResponse record {
-    ballerina/lang.int:0.0.0:Signed32? minValues?;
+    @jsondata:Name {value: "min_values"}
+    int:Signed32? minValues?;
+    @jsondata:Name {value: "custom_id"}
     string customId;
-    ballerina/lang.int:0.0.0:Signed32? maxValues?;
+    @jsondata:Name {value: "max_values"}
+    int:Signed32? maxValues?;
     MessageComponentStringSelectResponseOptions[]|() options?;
     boolean? disabled?;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
     string? placeholder?;
     3 'type;
 };
@@ -1737,34 +2140,41 @@
 
 type OptionsOneOf2 anydata|();
 
-type MessageComponentStringSelectResponseOptions ballerinax/discord:2.0.1:SelectOptionResponse|anydata|();
+type MessageComponentStringSelectResponseOptions SelectOptionResponse|anydata|();
 
-// Unknown type: RolesOneOf12
+@constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
+type RolesOneOf12 string;
 
 type RolesRolesOneOf122 anydata|();
 
-type GuildsEmojisRequest1Roles ballerinax/discord:2.0.1:RolesOneOf12|anydata|();
+type GuildsEmojisRequest1Roles RolesOneOf12|anydata|();
 
-// Unknown type: MLSpamUpsertRequestPartialExemptchannelsItemsString
+type MLSpamUpsertRequestPartialExemptchannelsItemsString string;
 
 # Represents the Queries record for the operation: search_guild_members
 
 type SearchGuildMembersQueries record {
+    @constraint:String {maxLength: 100, minLength: 1}
     string query;
-    ballerina/lang.int:0.0.0:Signed32 'limit;
+    @constraint:Int {minValue: 1, maxValue: 1000}
+    int:Signed32 'limit;
 };
 
 
 type StageInstancesRequest1 record {
+    @jsondata:Name {value: "privacy_level"}
     StageInstancesPrivacyLevels privacyLevel?;
+    @constraint:String {maxLength: 120, minLength: 1}
     string topic?;
 };
 
-// Unknown type: PUBLIC
+# The Stage instance is visible publicly. (deprecated)
+type PUBLIC 1;
 
-// Unknown type: GUILDONLY1
+# The Stage instance is visible publicly. (deprecated)
+type GUILDONLY1 2;
 
-type StageInstancesPrivacyLevels ballerinax/discord:2.0.1:PUBLIC|ballerinax/discord:2.0.1:GUILDONLY1;
+type StageInstancesPrivacyLevels PUBLIC|GUILDONLY1;
 
 
 type WidgetActivity record {
@@ -1773,63 +2183,84 @@
 
 
 type ApplicationCommandNumberOptionResponse record {
+    @jsondata:Name {value: "min_value"}
     decimal? minValue?;
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     boolean? autocomplete?;
     string name;
     string description;
+    @jsondata:Name {value: "description_localized"}
     string? descriptionLocalized?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     10 'type;
     ApplicationCommandOptionNumberChoiceResponse[]|() choices?;
     boolean? required?;
+    @jsondata:Name {value: "max_value"}
     decimal? maxValue?;
 };
 
 
 type ApplicationCommandOptionNumberChoiceResponse record {
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     string name;
     decimal value;
 };
 
-// Unknown type: ChannelsMessagesBulkDeleteRequestMessagesItemsString
+@constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
+type ChannelsMessagesBulkDeleteRequestMessagesItemsString string;
 
 
 type CreateGroupDMInviteRequest record {
-    ballerina/lang.int:0.0.0:Signed32? maxAge?;
+    @jsondata:Name {value: "max_age"}
+    int:Signed32? maxAge?;
 };
 
 
 type CreateGuildInviteRequest record {
-    ballerina/lang.int:0.0.0:Signed32? maxAge?;
+    @jsondata:Name {value: "max_age"}
+    int:Signed32? maxAge?;
     boolean? temporary?;
-    ballerina/lang.int:0.0.0:Signed32? maxUses?;
+    @jsondata:Name {value: "max_uses"}
+    int:Signed32? maxUses?;
     boolean? unique?;
+    @jsondata:Name {value: "target_type"}
     anydata targetType?;
+    @jsondata:Name {value: "target_user_id"}
     anydata targetUserId?;
+    @jsondata:Name {value: "target_application_id"}
     anydata targetApplicationId?;
 };
 
-type ChannelIdInvitesBody ballerinax/discord:2.0.1:CreateGroupDMInviteRequest|ballerinax/discord:2.0.1:CreateGuildInviteRequest;
+type ChannelIdInvitesBody CreateGroupDMInviteRequest|CreateGuildInviteRequest;
 
-// Unknown type: USERS
+# Controls role mentions
+type USERS "users";
 
 # Represents the Queries record for the operation: execute_webhook
 
 type ExecuteWebhookQueries record {
     boolean 'wait?;
+    @http:Query {name: "thread_id"}
     string threadId?;
 };
 
 
 type ApplicationCommandSubcommandGroupOption record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
+    @constraint:String {maxLength: 32, minLength: 1}
     string name;
     ApplicationCommandSubcommandOption[]|() options?;
+    @constraint:String {maxLength: 100, minLength: 1}
     string description;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     2 'type;
     boolean? required?;
@@ -1837,10 +2268,14 @@
 
 
 type ApplicationCommandSubcommandOption record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
+    @constraint:String {maxLength: 32, minLength: 1}
     string name;
     ApplicationCommandSubcommandOptionOptions[]|() options?;
+    @constraint:String {maxLength: 100, minLength: 1}
     string description;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     1 'type;
     boolean? required?;
@@ -1848,9 +2283,13 @@
 
 
 type ApplicationCommandBooleanOption record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
+    @constraint:String {maxLength: 32, minLength: 1}
     string name;
+    @constraint:String {maxLength: 100, minLength: 1}
     string description;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     5 'type;
     boolean? required?;
@@ -1858,30 +2297,43 @@
 
 
 type ApplicationCommandIntegerOption record {
+    @jsondata:Name {value: "min_value"}
     anydata minValue?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     boolean? autocomplete?;
+    @constraint:String {maxLength: 32, minLength: 1}
     string name;
+    @constraint:String {maxLength: 100, minLength: 1}
     string description;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     4 'type;
     ApplicationCommandOptionIntegerChoice[]|() choices?;
     boolean? required?;
+    @jsondata:Name {value: "max_value"}
     anydata maxValue?;
 };
 
 
 type ApplicationCommandOptionIntegerChoice record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
+    @constraint:String {maxLength: 100, minLength: 1}
     string name;
+    @constraint:Int {minValue: -9007199254740991, maxValue: 9007199254740991}
     int value;
 };
 
 
 type ApplicationCommandMentionableOption record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
+    @constraint:String {maxLength: 32, minLength: 1}
     string name;
+    @constraint:String {maxLength: 100, minLength: 1}
     string description;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     9 'type;
     boolean? required?;
@@ -1889,30 +2341,42 @@
 
 
 type ApplicationCommandNumberOption record {
+    @jsondata:Name {value: "min_value"}
     decimal? minValue?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     boolean? autocomplete?;
+    @constraint:String {maxLength: 32, minLength: 1}
     string name;
+    @constraint:String {maxLength: 100, minLength: 1}
     string description;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     10 'type;
     ApplicationCommandOptionNumberChoice[]|() choices?;
     boolean? required?;
+    @jsondata:Name {value: "max_value"}
     decimal? maxValue?;
 };
 
 
 type ApplicationCommandOptionNumberChoice record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
+    @constraint:String {maxLength: 100, minLength: 1}
     string name;
     decimal value;
 };
 
 
 type ApplicationCommandRoleOption record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
+    @constraint:String {maxLength: 32, minLength: 1}
     string name;
+    @constraint:String {maxLength: 100, minLength: 1}
     string description;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     8 'type;
     boolean? required?;
@@ -1920,30 +2384,43 @@
 
 
 type ApplicationCommandStringOption record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     boolean? autocomplete?;
-    ballerina/lang.int:0.0.0:Signed32? minLength?;
+    @jsondata:Name {value: "min_length"}
+    int:Signed32? minLength?;
+    @constraint:String {maxLength: 32, minLength: 1}
     string name;
+    @constraint:String {maxLength: 100, minLength: 1}
     string description;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     3 'type;
     ApplicationCommandOptionStringChoice[]|() choices?;
     boolean? required?;
-    ballerina/lang.int:0.0.0:Signed32? maxLength?;
+    @jsondata:Name {value: "max_length"}
+    int:Signed32? maxLength?;
 };
 
 
 type ApplicationCommandOptionStringChoice record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
+    @constraint:String {maxLength: 100, minLength: 1}
     string name;
+    @constraint:String {maxLength: 6000}
     string value;
 };
 
 
 type ApplicationCommandUserOption record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
+    @constraint:String {maxLength: 32, minLength: 1}
     string name;
+    @constraint:String {maxLength: 100, minLength: 1}
     string description;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     6 'type;
     boolean? required?;
@@ -1951,45 +2428,56 @@
 
 type OptionsOneOf10 anydata|();
 
-type ApplicationCommandSubcommandOptionOptions ballerinax/discord:2.0.1:ApplicationCommandAttachmentOption|ballerinax/discord:2.0.1:ApplicationCommandBooleanOption|ballerinax/discord:2.0.1:ApplicationCommandChannelOption|ballerinax/discord:2.0.1:ApplicationCommandIntegerOption|ballerinax/discord:2.0.1:ApplicationCommandMentionableOption|ballerinax/discord:2.0.1:ApplicationCommandNumberOption|ballerinax/discord:2.0.1:ApplicationCommandRoleOption|ballerinax/discord:2.0.1:ApplicationCommandStringOption|ballerinax/discord:2.0.1:ApplicationCommandUserOption|anydata|();
+type ApplicationCommandSubcommandOptionOptions ApplicationCommandAttachmentOption|ApplicationCommandBooleanOption|ApplicationCommandChannelOption|ApplicationCommandIntegerOption|ApplicationCommandMentionableOption|ApplicationCommandNumberOption|ApplicationCommandRoleOption|ApplicationCommandStringOption|ApplicationCommandUserOption|anydata|();
 
-// Unknown type: CreateForumThreadRequestAppliedtagsItemsString
+type CreateForumThreadRequestAppliedtagsItemsString string;
 
 
 type StandardStickerResponse record {
+    @jsondata:Name {value: "format_type"}
     anydata formatType?;
+    @jsondata:Name {value: "pack_id"}
     string packId;
     string name;
     string? description?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
-    ballerina/lang.int:0.0.0:Signed32 sortValue;
+    @jsondata:Name {value: "sort_value"}
+    int:Signed32 sortValue;
     1 'type;
     string tags;
 };
 
 type ActionsOneOf5 anydata|();
 
-type DefaultKeywordListUpsertRequestActions ballerinax/discord:2.0.1:BlockMessageAction|ballerinax/discord:2.0.1:FlagToChannelAction|ballerinax/discord:2.0.1:QuarantineUserAction|ballerinax/discord:2.0.1:UserCommunicationDisabledAction|anydata|();
+type DefaultKeywordListUpsertRequestActions BlockMessageAction|FlagToChannelAction|QuarantineUserAction|UserCommunicationDisabledAction|anydata|();
 
 
 type ApplicationCommandAttachmentOptionResponse record {
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     string name;
     string description;
+    @jsondata:Name {value: "description_localized"}
     string? descriptionLocalized?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     11 'type;
     boolean? required?;
 };
 
-// Unknown type: PING
+# Sent by Discord to validate your application's interaction handler
+type PING 1;
 
 
 type ApplicationRoleConnectionsMetadataItemResponse record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     string name;
     string description;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     MetadataItemTypes 'type;
     string 'key;
@@ -1998,74 +2486,98 @@
 
 type WebhookSourceChannelResponse record {
     string name;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
 };
 
 
 type MLSpamRuleResponse record {
+    @jsondata:Name {value: "event_type"}
     AutomodEventType eventType;
+    @jsondata:Name {value: "trigger_type"}
     3 triggerType;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
+    @jsondata:Name {value: "creator_id"}
     string creatorId;
     string name;
+    @jsondata:Name {value: "exempt_roles"}
     MLSpamRuleResponseExemptrolesItemsString[]|() exemptRoles?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "exempt_channels"}
     MLSpamRuleResponseExemptchannelsItemsString[]|() exemptChannels?;
     DefaultKeywordRuleResponseActions[] actions;
     boolean? enabled?;
+    @jsondata:Name {value: "trigger_metadata"}
     record {|anydata...;|} triggerMetadata;
 };
 
-// Unknown type: MLSpamRuleResponseExemptrolesItemsString
+type MLSpamRuleResponseExemptrolesItemsString string;
 
-// Unknown type: MLSpamRuleResponseExemptchannelsItemsString
+type MLSpamRuleResponseExemptchannelsItemsString string;
 
-// Unknown type: KEYWORD
+# Check if content contains words from a list of keywords or matches regex
+type KEYWORD 1;
 
-// Unknown type: SPAMLINK
+# DEPRECATED
+type SPAMLINK 2;
 
-// Unknown type: MLSPAM
+# Check if content represents generic spam
+type MLSPAM 3;
 
-// Unknown type: DEFAULTKEYWORDLIST
+# Check if content contains words from internal pre-defined wordsets
+type DEFAULTKEYWORDLIST 4;
 
-type AutomodTriggerType ballerinax/discord:2.0.1:KEYWORD|ballerinax/discord:2.0.1:SPAMLINK|ballerinax/discord:2.0.1:MLSPAM|ballerinax/discord:2.0.1:DEFAULTKEYWORDLIST|ballerinax/discord:2.0.1:MENTIONSPAM;
+type AutomodTriggerType KEYWORD|SPAMLINK|MLSPAM|DEFAULTKEYWORDLIST|MENTIONSPAM;
 
 
 type GatewayBotSessionStartLimitResponse record {
-    ballerina/lang.int:0.0.0:Signed32 resetAfter;
-    ballerina/lang.int:0.0.0:Signed32 maxConcurrency;
-    ballerina/lang.int:0.0.0:Signed32 total;
-    ballerina/lang.int:0.0.0:Signed32 remaining;
+    @jsondata:Name {value: "reset_after"}
+    int:Signed32 resetAfter;
+    @jsondata:Name {value: "max_concurrency"}
+    int:Signed32 maxConcurrency;
+    int:Signed32 total;
+    int:Signed32 remaining;
 };
 
 
 type GithubCheckRun record {
     string? conclusion?;
     anydata output?;
+    @jsondata:Name {value: "pull_requests"}
     GithubCheckPullRequest[]|() pullRequests?;
+    @jsondata:Name {value: "html_url"}
     string htmlUrl;
+    @constraint:String {maxLength: 152133}
     string name;
+    @jsondata:Name {value: "check_suite"}
     GithubCheckSuite checkSuite;
+    @jsondata:Name {value: "details_url"}
     string? detailsUrl?;
 };
 
 
 type ApplicationCommandOptionIntegerChoiceResponse record {
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     string name;
+    @constraint:Int {minValue: -9007199254740991, maxValue: 9007199254740991}
     int value;
 };
 
-// Unknown type: ThreadResponseAppliedtagsItemsString
+type ThreadResponseAppliedtagsItemsString string;
 
-// Unknown type: MentionSpamUpsertRequestExemptrolesItemsString
+type MentionSpamUpsertRequestExemptrolesItemsString string;
 
 
 type GuildsRolesRequest record {
-    ballerina/lang.int:0.0.0:Signed32? color?;
+    int:Signed32? color?;
+    @jsondata:Name {value: "unicode_emoji"}
     string? unicodeEmoji?;
-    ballerina/lang.int:0.0.0:Signed32? permissions?;
+    int:Signed32? permissions?;
     string? name?;
     record {|byte[] fileContent; string fileName; anydata...;|}? icon?;
     boolean? mentionable?;
@@ -2075,102 +2587,143 @@
 
 type VoiceScheduledEventCreateRequest record {
     record {|byte[] fileContent; string fileName; anydata...;|}? image?;
+    @jsondata:Name {value: "entity_type"}
     2 entityType;
+    @jsondata:Name {value: "privacy_level"}
     GuildScheduledEventPrivacyLevels privacyLevel;
+    @constraint:String {maxLength: 100}
     string name;
+    @jsondata:Name {value: "entity_metadata"}
     anydata entityMetadata?;
     string? description?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
+    @jsondata:Name {value: "scheduled_start_time"}
     string scheduledStartTime;
+    @jsondata:Name {value: "scheduled_end_time"}
     string? scheduledEndTime?;
 };
 
 
 type GuildAuditLogResponse record {
     InlineResponse2004[] webhooks;
+    @jsondata:Name {value: "application_commands"}
     ApplicationCommandResponse[] applicationCommands;
     ThreadResponse[] threads;
+    @jsondata:Name {value: "guild_scheduled_events"}
     InlineResponse2003[] guildScheduledEvents;
     GuildAuditLogResponseIntegrations[] integrations;
+    @jsondata:Name {value: "auto_moderation_rules"}
     InlineResponse2001[] autoModerationRules;
     UserResponse[] users;
+    @jsondata:Name {value: "audit_log_entries"}
     AuditLogEntryResponse[] auditLogEntries;
 };
 
 
 type ApplicationIncomingWebhookResponse record {
+    @jsondata:Name {value: "guild_id"}
     anydata guildId?;
     string name;
     string? avatar?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     3 'type;
+    @jsondata:Name {value: "application_id"}
     anydata applicationId?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
     anydata user?;
 };
 
 
 type ChannelFollowerWebhookResponse record {
+    @jsondata:Name {value: "source_channel"}
     anydata sourceChannel?;
+    @jsondata:Name {value: "source_guild"}
     anydata sourceGuild?;
+    @jsondata:Name {value: "guild_id"}
     anydata guildId?;
     string name;
     string? avatar?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     2 'type;
+    @jsondata:Name {value: "application_id"}
     anydata applicationId?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
     anydata user?;
 };
 
 
 type GuildIncomingWebhookResponse record {
+    @jsondata:Name {value: "guild_id"}
     anydata guildId?;
     string name;
     string? avatar?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     1 'type;
+    @jsondata:Name {value: "application_id"}
     anydata applicationId?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
     anydata user?;
     string? url?;
     string? token?;
 };
 
-type InlineResponse2004 ballerinax/discord:2.0.1:ApplicationIncomingWebhookResponse|ballerinax/discord:2.0.1:ChannelFollowerWebhookResponse|ballerinax/discord:2.0.1:GuildIncomingWebhookResponse;
+type InlineResponse2004 ApplicationIncomingWebhookResponse|ChannelFollowerWebhookResponse|GuildIncomingWebhookResponse;
 
 
 type ApplicationCommandResponse record {
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     boolean? nsfw?;
     string description;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     ApplicationCommandType 'type;
+    @jsondata:Name {value: "application_id"}
     string applicationId;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string version;
+    @jsondata:Name {value: "dm_permission"}
     boolean? dmPermission?;
     string name;
+    @jsondata:Name {value: "guild_id"}
     anydata guildId?;
     ApplicationCommandResponseOptions[]|() options?;
+    @jsondata:Name {value: "description_localized"}
     string? descriptionLocalized?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "default_member_permissions"}
     string? defaultMemberPermissions?;
 };
 
-// Unknown type: CHAT
+# Slash commands; a text-based command that shows up when a user types /
+type CHAT 1;
 
-// Unknown type: USER
+# A UI-based command that shows up when you right click or tap on a user
+type USER 2;
 
-type ApplicationCommandType ballerinax/discord:2.0.1:CHAT|ballerinax/discord:2.0.1:USER|ballerinax/discord:2.0.1:MESSAGE;
+type ApplicationCommandType CHAT|USER|MESSAGE;
 
 
 type ApplicationCommandBooleanOptionResponse record {
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     string name;
     string description;
+    @jsondata:Name {value: "description_localized"}
     string? descriptionLocalized?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     5 'type;
     boolean? required?;
@@ -2178,27 +2731,37 @@
 
 
 type ApplicationCommandIntegerOptionResponse record {
+    @jsondata:Name {value: "min_value"}
     anydata minValue?;
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     boolean? autocomplete?;
     string name;
     string description;
+    @jsondata:Name {value: "description_localized"}
     string? descriptionLocalized?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     4 'type;
     ApplicationCommandOptionIntegerChoiceResponse[]|() choices?;
     boolean? required?;
+    @jsondata:Name {value: "max_value"}
     anydata maxValue?;
 };
 
 
 type ApplicationCommandMentionableOptionResponse record {
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     string name;
     string description;
+    @jsondata:Name {value: "description_localized"}
     string? descriptionLocalized?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     9 'type;
     boolean? required?;
@@ -2206,11 +2769,15 @@
 
 
 type ApplicationCommandRoleOptionResponse record {
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     string name;
     string description;
+    @jsondata:Name {value: "description_localized"}
     string? descriptionLocalized?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     8 'type;
     boolean? required?;
@@ -2218,12 +2785,16 @@
 
 
 type ApplicationCommandSubcommandGroupOptionResponse record {
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     string name;
     ApplicationCommandSubcommandOptionResponse[]|() options?;
     string description;
+    @jsondata:Name {value: "description_localized"}
     string? descriptionLocalized?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     2 'type;
     boolean? required?;
@@ -2231,12 +2802,16 @@
 
 
 type ApplicationCommandSubcommandOptionResponse record {
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     string name;
     ApplicationCommandSubcommandOptionResponseOptions[]|() options?;
     string description;
+    @jsondata:Name {value: "description_localized"}
     string? descriptionLocalized?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     1 'type;
     boolean? required?;
@@ -2244,42 +2819,61 @@
 
 
 type ApplicationCommandUserOptionResponse record {
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
     string name;
     string description;
+    @jsondata:Name {value: "description_localized"}
     string? descriptionLocalized?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
     6 'type;
     boolean? required?;
 };
 
-type ApplicationCommandSubcommandOptionResponseOptions ballerinax/discord:2.0.1:ApplicationCommandAttachmentOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandBooleanOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandChannelOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandIntegerOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandMentionableOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandNumberOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandRoleOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandStringOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandUserOptionResponse|anydata|();
+type ApplicationCommandSubcommandOptionResponseOptions ApplicationCommandAttachmentOptionResponse|ApplicationCommandBooleanOptionResponse|ApplicationCommandChannelOptionResponse|ApplicationCommandIntegerOptionResponse|ApplicationCommandMentionableOptionResponse|ApplicationCommandNumberOptionResponse|ApplicationCommandRoleOptionResponse|ApplicationCommandStringOptionResponse|ApplicationCommandUserOptionResponse|anydata|();
 
-type ApplicationCommandResponseOptions ballerinax/discord:2.0.1:ApplicationCommandAttachmentOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandBooleanOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandChannelOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandIntegerOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandMentionableOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandNumberOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandRoleOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandStringOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandSubcommandGroupOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandSubcommandOptionResponse|ballerinax/discord:2.0.1:ApplicationCommandUserOptionResponse|anydata|();
+type ApplicationCommandResponseOptions ApplicationCommandAttachmentOptionResponse|ApplicationCommandBooleanOptionResponse|ApplicationCommandChannelOptionResponse|ApplicationCommandIntegerOptionResponse|ApplicationCommandMentionableOptionResponse|ApplicationCommandNumberOptionResponse|ApplicationCommandRoleOptionResponse|ApplicationCommandStringOptionResponse|ApplicationCommandSubcommandGroupOptionResponse|ApplicationCommandSubcommandOptionResponse|ApplicationCommandUserOptionResponse|anydata|();
 
 
 type ThreadResponse record {
+    @jsondata:Name {value: "last_pin_timestamp"}
     string? lastPinTimestamp?;
-    ballerina/lang.int:0.0.0:Signed32? rateLimitPerUser?;
+    @jsondata:Name {value: "rate_limit_per_user"}
+    int:Signed32? rateLimitPerUser?;
+    @jsondata:Name {value: "owner_id"}
     string ownerId;
-    ballerina/lang.int:0.0.0:Signed32 flags;
-    ballerina/lang.int:0.0.0:Signed32? bitrate?;
+    int:Signed32 flags;
+    int:Signed32? bitrate?;
     ChannelTypes 'type;
-    ballerina/lang.int:0.0.0:Signed32? userLimit?;
-    ballerina/lang.int:0.0.0:Signed32 messageCount;
-    ballerina/lang.int:0.0.0:Signed32 totalMessageSent;
+    @jsondata:Name {value: "user_limit"}
+    int:Signed32? userLimit?;
+    @jsondata:Name {value: "message_count"}
+    int:Signed32 messageCount;
+    @jsondata:Name {value: "total_message_sent"}
+    int:Signed32 totalMessageSent;
+    @jsondata:Name {value: "last_message_id"}
     anydata lastMessageId?;
+    @jsondata:Name {value: "rtc_region"}
     string? rtcRegion?;
+    @jsondata:Name {value: "parent_id"}
     anydata parentId?;
     string? permissions?;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
     string name;
     anydata member?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "thread_metadata"}
     anydata threadMetadata?;
-    ballerina/lang.int:0.0.0:Signed32 memberCount;
+    @jsondata:Name {value: "member_count"}
+    int:Signed32 memberCount;
+    @jsondata:Name {value: "video_quality_mode"}
     anydata videoQualityMode?;
+    @jsondata:Name {value: "applied_tags"}
     ThreadResponseAppliedtagsItemsString[]|() appliedTags?;
 };
 
@@ -2287,19 +2881,31 @@
 type StageScheduledEventResponse record {
     string? image?;
     anydata creator?;
+    @jsondata:Name {value: "privacy_level"}
     GuildScheduledEventPrivacyLevels privacyLevel;
+    @jsondata:Name {value: "entity_metadata"}
     anydata entityMetadata?;
     string? description?;
+    @jsondata:Name {value: "entity_id"}
     anydata entityId?;
+    @jsondata:Name {value: "scheduled_end_time"}
     string? scheduledEndTime?;
+    @jsondata:Name {value: "entity_type"}
     1 entityType;
+    @jsondata:Name {value: "user_rsvp"}
     anydata userRsvp?;
-    ballerina/lang.int:0.0.0:Signed32? userCount?;
+    @jsondata:Name {value: "user_count"}
+    int:Signed32? userCount?;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
     string name;
+    @jsondata:Name {value: "creator_id"}
     anydata creatorId?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
+    @jsondata:Name {value: "scheduled_start_time"}
     string scheduledStartTime;
     GuildScheduledEventStatuses status;
 };
@@ -2308,227 +2914,270 @@
 type VoiceScheduledEventResponse record {
     string? image?;
     anydata creator?;
+    @jsondata:Name {value: "privacy_level"}
     GuildScheduledEventPrivacyLevels privacyLevel;
+    @jsondata:Name {value: "entity_metadata"}
     anydata entityMetadata?;
     string? description?;
+    @jsondata:Name {value: "entity_id"}
     anydata entityId?;
+    @jsondata:Name {value: "scheduled_end_time"}
     string? scheduledEndTime?;
+    @jsondata:Name {value: "entity_type"}
     2 entityType;
+    @jsondata:Name {value: "user_rsvp"}
     anydata userRsvp?;
-    ballerina/lang.int:0.0.0:Signed32? userCount?;
+    @jsondata:Name {value: "user_count"}
+    int:Signed32? userCount?;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
     string name;
+    @jsondata:Name {value: "creator_id"}
     anydata creatorId?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
+    @jsondata:Name {value: "scheduled_start_time"}
     string scheduledStartTime;
     GuildScheduledEventStatuses status;
 };
 
-type InlineResponse2003 ballerinax/discord:2.0.1:ExternalScheduledEventResponse|ballerinax/discord:2.0.1:StageScheduledEventResponse|ballerinax/discord:2.0.1:VoiceScheduledEventResponse;
+type InlineResponse2003 ExternalScheduledEventResponse|StageScheduledEventResponse|VoiceScheduledEventResponse;
 
 
 type DefaultKeywordRuleResponse record {
+    @jsondata:Name {value: "event_type"}
     AutomodEventType eventType;
+    @jsondata:Name {value: "trigger_type"}
     4 triggerType;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
+    @jsondata:Name {value: "creator_id"}
     string creatorId;
     string name;
+    @jsondata:Name {value: "exempt_roles"}
     DefaultKeywordRuleResponseExemptrolesItemsString[]|() exemptRoles?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "exempt_channels"}
     DefaultKeywordRuleResponseExemptchannelsItemsString[]|() exemptChannels?;
     DefaultKeywordRuleResponseActions[] actions;
     boolean? enabled?;
+    @jsondata:Name {value: "trigger_metadata"}
     DefaultKeywordListTriggerMetadataResponse triggerMetadata;
 };
 
-// Unknown type: DefaultKeywordRuleResponseExemptrolesItemsString
+type DefaultKeywordRuleResponseExemptrolesItemsString string;
 
-// Unknown type: DefaultKeywordRuleResponseExemptchannelsItemsString
+type DefaultKeywordRuleResponseExemptchannelsItemsString string;
 
 
 type DefaultKeywordListTriggerMetadataResponse record {
     AutomodKeywordPresetType[] presets;
+    @jsondata:Name {value: "allow_list"}
     string[] allowList;
 };
 
 
 type KeywordRuleResponse record {
+    @jsondata:Name {value: "event_type"}
     AutomodEventType eventType;
+    @jsondata:Name {value: "trigger_type"}
     1 triggerType;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
+    @jsondata:Name {value: "creator_id"}
     string creatorId;
     string name;
+    @jsondata:Name {value: "exempt_roles"}
     KeywordRuleResponseExemptrolesItemsString[]|() exemptRoles?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "exempt_channels"}
     KeywordRuleResponseExemptchannelsItemsString[]|() exemptChannels?;
     DefaultKeywordRuleResponseActions[] actions;
     boolean? enabled?;
+    @jsondata:Name {value: "trigger_metadata"}
     KeywordTriggerMetadataResponse triggerMetadata;
 };
 
-// Unknown type: KeywordRuleResponseExemptrolesItemsString
+type KeywordRuleResponseExemptrolesItemsString string;
 
 
 type SpamLinkRuleResponse record {
+    @jsondata:Name {value: "event_type"}
     AutomodEventType eventType;
+    @jsondata:Name {value: "trigger_type"}
     2 triggerType;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
+    @jsondata:Name {value: "creator_id"}
     string creatorId;
     string name;
+    @jsondata:Name {value: "exempt_roles"}
     SpamLinkRuleResponseExemptrolesItemsString[]|() exemptRoles?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "exempt_channels"}
     SpamLinkRuleResponseExemptchannelsItemsString[]|() exemptChannels?;
     DefaultKeywordRuleResponseActions[] actions;
     boolean? enabled?;
+    @jsondata:Name {value: "trigger_metadata"}
     record {|anydata...;|} triggerMetadata;
 };
 
-// Unknown type: SpamLinkRuleResponseExemptrolesItemsString
+type SpamLinkRuleResponseExemptrolesItemsString string;
 
-// Unknown type: SpamLinkRuleResponseExemptchannelsItemsString
+type SpamLinkRuleResponseExemptchannelsItemsString string;
 
-type InlineResponse2001 ballerinax/discord:2.0.1:DefaultKeywordRuleResponse|ballerinax/discord:2.0.1:KeywordRuleResponse|ballerinax/discord:2.0.1:MLSpamRuleResponse|ballerinax/discord:2.0.1:MentionSpamRuleResponse|ballerinax/discord:2.0.1:SpamLinkRuleResponse;
+type InlineResponse2001 DefaultKeywordRuleResponse|KeywordRuleResponse|MLSpamRuleResponse|MentionSpamRuleResponse|SpamLinkRuleResponse;
 
 
 type AuditLogEntryResponse record {
     string? reason?;
+    @jsondata:Name {value: "action_type"}
     AuditLogActionTypes actionType;
+    @jsondata:Name {value: "user_id"}
     anydata userId?;
     AuditLogObjectChangeResponse[]|() changes?;
     record {|string...;|}? options?;
+    @jsondata:Name {value: "target_id"}
     anydata targetId?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
 };
 
-// Unknown type: GUILDUPDATE
+type GUILDUPDATE 1;
 
-// Unknown type: CHANNELCREATE
+type CHANNELCREATE 10;
 
-// Unknown type: CHANNELUPDATE
+type CHANNELUPDATE 11;
 
-// Unknown type: CHANNELDELETE
+type CHANNELDELETE 12;
 
-// Unknown type: CHANNELOVERWRITECREATE
+type CHANNELOVERWRITECREATE 13;
 
-// Unknown type: CHANNELOVERWRITEUPDATE
+type CHANNELOVERWRITEUPDATE 14;
 
-// Unknown type: CHANNELOVERWRITEDELETE
+type CHANNELOVERWRITEDELETE 15;
 
-// Unknown type: MEMBERKICK
+type MEMBERKICK 20;
 
-// Unknown type: MEMBERPRUNE
+type MEMBERPRUNE 21;
+
+type MEMBERBANADD 22;
 
-// Unknown type: MEMBERBANADD
+type MEMBERBANREMOVE 23;
 
-// Unknown type: MEMBERBANREMOVE
+type MEMBERUPDATE 24;
 
-// Unknown type: MEMBERUPDATE
+type MEMBERROLEUPDATE 25;
 
-// Unknown type: MEMBERROLEUPDATE
+type MEMBERDISCONNECT 27;
 
-// Unknown type: MEMBERDISCONNECT
+type ROLECREATE 30;
 
-// Unknown type: ROLECREATE
+type ROLEUPDATE 31;
 
-// Unknown type: ROLEUPDATE
+type INVITECREATE 40;
 
-// Unknown type: INVITECREATE
+type INVITEDELETE 42;
 
-// Unknown type: INVITEDELETE
+type WEBHOOKCREATE 50;
 
-// Unknown type: WEBHOOKCREATE
+type WEBHOOKUPDATE 51;
 
-// Unknown type: WEBHOOKUPDATE
+type WEBHOOKDELETE 52;
 
-// Unknown type: WEBHOOKDELETE
+type EMOJIUPDATE 61;
 
-// Unknown type: EMOJIUPDATE
+type EMOJIDELETE 62;
 
-// Unknown type: EMOJIDELETE
+type MESSAGEDELETE 72;
 
-// Unknown type: MESSAGEDELETE
+type MESSAGEBULKDELETE 73;
 
-// Unknown type: MESSAGEBULKDELETE
+type MESSAGEPIN 74;
 
-// Unknown type: MESSAGEPIN
+type MESSAGEUNPIN 75;
 
-// Unknown type: MESSAGEUNPIN
+type INTEGRATIONCREATE 80;
 
-// Unknown type: INTEGRATIONCREATE
+type INTEGRATIONUPDATE 81;
 
-// Unknown type: INTEGRATIONUPDATE
+type INTEGRATIONDELETE 82;
 
-// Unknown type: INTEGRATIONDELETE
+type STAGEINSTANCECREATE 83;
 
-// Unknown type: STAGEINSTANCECREATE
+type STAGEINSTANCEUPDATE 84;
 
-// Unknown type: STAGEINSTANCEUPDATE
+type STAGEINSTANCEDELETE 85;
 
-// Unknown type: STAGEINSTANCEDELETE
+type STICKERCREATE 90;
 
-// Unknown type: STICKERCREATE
+type STICKERUPDATE 91;
 
-// Unknown type: STICKERUPDATE
+type STICKERDELETE 92;
 
-// Unknown type: STICKERDELETE
+type GUILDSCHEDULEDEVENTCREATE 100;
 
-// Unknown type: GUILDSCHEDULEDEVENTCREATE
+type GUILDSCHEDULEDEVENTDELETE 102;
 
-// Unknown type: GUILDSCHEDULEDEVENTDELETE
+type THREADCREATE 110;
 
-// Unknown type: THREADCREATE
+type THREADDELETE 112;
 
-// Unknown type: THREADDELETE
+type APPLICATIONCOMMANDPERMISSIONUPDATE 121;
 
-// Unknown type: APPLICATIONCOMMANDPERMISSIONUPDATE
+type SOUNDBOARDSOUNDCREATE 130;
 
-// Unknown type: SOUNDBOARDSOUNDCREATE
+type SOUNDBOARDSOUNDUPDATE 131;
 
-// Unknown type: SOUNDBOARDSOUNDUPDATE
+type AUTOMODERATIONRULECREATE 140;
 
-// Unknown type: AUTOMODERATIONRULECREATE
+type AUTOMODERATIONRULEUPDATE 141;
 
-// Unknown type: AUTOMODERATIONRULEUPDATE
+type AUTOMODERATIONRULEDELETE 142;
 
-// Unknown type: AUTOMODERATIONRULEDELETE
+type AUTOMODERATIONBLOCKMESSAGE 143;
 
-// Unknown type: AUTOMODERATIONBLOCKMESSAGE
+type AUTOMODERATIONFLAGTOCHANNEL 144;
 
-// Unknown type: AUTOMODERATIONFLAGTOCHANNEL
-
-// Unknown type: AUTOMODERATIONUSERCOMMDISABLED
+type AUTOMODERATIONUSERCOMMDISABLED 145;
 
-// Unknown type: AUTOMODERATIONQUARANTINEUSER
+type AUTOMODERATIONQUARANTINEUSER 146;
 
-// Unknown type: CREATORMONETIZATIONREQUESTCREATED
+type CREATORMONETIZATIONREQUESTCREATED 150;
 
-// Unknown type: CREATORMONETIZATIONTERMSACCEPTED
+type CREATORMONETIZATIONTERMSACCEPTED 151;
 
-// Unknown type: ONBOARDINGPROMPTCREATE
+type ONBOARDINGPROMPTCREATE 163;
 
-// Unknown type: ONBOARDINGPROMPTUPDATE
+type ONBOARDINGPROMPTUPDATE 164;
 
-// Unknown type: ONBOARDINGPROMPTDELETE
+type ONBOARDINGPROMPTDELETE 165;
 
-// Unknown type: ONBOARDINGCREATE
+type ONBOARDINGCREATE 166;
 
-// Unknown type: ONBOARDINGUPDATE
+type ONBOARDINGUPDATE 167;
 
-// Unknown type: GUILDHOMEFEATUREITEM
+type GUILDHOMEFEATUREITEM 171;
 
-// Unknown type: HARMFULLINKSBLOCKEDMESSAGE
+type HARMFULLINKSBLOCKEDMESSAGE 180;
 
-// Unknown type: HOMESETTINGSCREATE
+type HOMESETTINGSCREATE 190;
 
-// Unknown type: VOICECHANNELSTATUSDELETE
+type VOICECHANNELSTATUSDELETE 193;
 
-type AuditLogActionTypes ballerinax/discord:2.0.1:GUILDUPDATE|ballerinax/discord:2.0.1:CHANNELCREATE|ballerinax/discord:2.0.1:CHANNELUPDATE|ballerinax/discord:2.0.1:CHANNELDELETE|ballerinax/discord:2.0.1:CHANNELOVERWRITECREATE|ballerinax/discord:2.0.1:CHANNELOVERWRITEUPDATE|ballerinax/discord:2.0.1:CHANNELOVERWRITEDELETE|ballerinax/discord:2.0.1:MEMBERKICK|ballerinax/discord:2.0.1:MEMBERPRUNE|ballerinax/discord:2.0.1:MEMBERBANADD|ballerinax/discord:2.0.1:MEMBERBANREMOVE|ballerinax/discord:2.0.1:MEMBERUPDATE|ballerinax/discord:2.0.1:MEMBERROLEUPDATE|ballerinax/discord:2.0.1:MEMBERMOVE|ballerinax/discord:2.0.1:MEMBERDISCONNECT|ballerinax/discord:2.0.1:BOTADD|ballerinax/discord:2.0.1:ROLECREATE|ballerinax/discord:2.0.1:ROLEUPDATE|ballerinax/discord:2.0.1:ROLEDELETE|ballerinax/discord:2.0.1:INVITECREATE|ballerinax/discord:2.0.1:INVITEUPDATE|ballerinax/discord:2.0.1:INVITEDELETE|ballerinax/discord:2.0.1:WEBHOOKCREATE|ballerinax/discord:2.0.1:WEBHOOKUPDATE|ballerinax/discord:2.0.1:WEBHOOKDELETE|ballerinax/discord:2.0.1:EMOJICREATE|ballerinax/discord:2.0.1:EMOJIUPDATE|ballerinax/discord:2.0.1:EMOJIDELETE|ballerinax/discord:2.0.1:MESSAGEDELETE|ballerinax/discord:2.0.1:MESSAGEBULKDELETE|ballerinax/discord:2.0.1:MESSAGEPIN|ballerinax/discord:2.0.1:MESSAGEUNPIN|ballerinax/discord:2.0.1:INTEGRATIONCREATE|ballerinax/discord:2.0.1:INTEGRATIONUPDATE|ballerinax/discord:2.0.1:INTEGRATIONDELETE|ballerinax/discord:2.0.1:STAGEINSTANCECREATE|ballerinax/discord:2.0.1:STAGEINSTANCEUPDATE|ballerinax/discord:2.0.1:STAGEINSTANCEDELETE|ballerinax/discord:2.0.1:STICKERCREATE|ballerinax/discord:2.0.1:STICKERUPDATE|ballerinax/discord:2.0.1:STICKERDELETE|ballerinax/discord:2.0.1:GUILDSCHEDULEDEVENTCREATE|ballerinax/discord:2.0.1:GUILDSCHEDULEDEVENTUPDATE|ballerinax/discord:2.0.1:GUILDSCHEDULEDEVENTDELETE|ballerinax/discord:2.0.1:THREADCREATE|ballerinax/discord:2.0.1:THREADUPDATE|ballerinax/discord:2.0.1:THREADDELETE|ballerinax/discord:2.0.1:APPLICATIONCOMMANDPERMISSIONUPDATE|ballerinax/discord:2.0.1:SOUNDBOARDSOUNDCREATE|ballerinax/discord:2.0.1:SOUNDBOARDSOUNDUPDATE|ballerinax/discord:2.0.1:SOUNDBOARDSOUNDDELETE|ballerinax/discord:2.0.1:AUTOMODERATIONRULECREATE|ballerinax/discord:2.0.1:AUTOMODERATIONRULEUPDATE|ballerinax/discord:2.0.1:AUTOMODERATIONRULEDELETE|ballerinax/discord:2.0.1:AUTOMODERATIONBLOCKMESSAGE|ballerinax/discord:2.0.1:AUTOMODERATIONFLAGTOCHANNEL|ballerinax/discord:2.0.1:AUTOMODERATIONUSERCOMMDISABLED|ballerinax/discord:2.0.1:AUTOMODERATIONQUARANTINEUSER|ballerinax/discord:2.0.1:CREATORMONETIZATIONREQUESTCREATED|ballerinax/discord:2.0.1:CREATORMONETIZATIONTERMSACCEPTED|ballerinax/discord:2.0.1:ONBOARDINGPROMPTCREATE|ballerinax/discord:2.0.1:ONBOARDINGPROMPTUPDATE|ballerinax/discord:2.0.1:ONBOARDINGPROMPTDELETE|ballerinax/discord:2.0.1:ONBOARDINGCREATE|ballerinax/discord:2.0.1:ONBOARDINGUPDATE|ballerinax/discord:2.0.1:GUILDHOMEFEATUREITEM|ballerinax/discord:2.0.1:GUILDHOMEREMOVEITEM|ballerinax/discord:2.0.1:HARMFULLINKSBLOCKEDMESSAGE|ballerinax/discord:2.0.1:HOMESETTINGSCREATE|ballerinax/discord:2.0.1:HOMESETTINGSUPDATE|ballerinax/discord:2.0.1:VOICECHANNELSTATUSCREATE|ballerinax/discord:2.0.1:VOICECHANNELSTATUSDELETE;
+type AuditLogActionTypes GUILDUPDATE|CHANNELCREATE|CHANNELUPDATE|CHANNELDELETE|CHANNELOVERWRITECREATE|CHANNELOVERWRITEUPDATE|CHANNELOVERWRITEDELETE|MEMBERKICK|MEMBERPRUNE|MEMBERBANADD|MEMBERBANREMOVE|MEMBERUPDATE|MEMBERROLEUPDATE|MEMBERMOVE|MEMBERDISCONNECT|BOTADD|ROLECREATE|ROLEUPDATE|ROLEDELETE|INVITECREATE|INVITEUPDATE|INVITEDELETE|WEBHOOKCREATE|WEBHOOKUPDATE|WEBHOOKDELETE|EMOJICREATE|EMOJIUPDATE|EMOJIDELETE|MESSAGEDELETE|MESSAGEBULKDELETE|MESSAGEPIN|MESSAGEUNPIN|INTEGRATIONCREATE|INTEGRATIONUPDATE|INTEGRATIONDELETE|STAGEINSTANCECREATE|STAGEINSTANCEUPDATE|STAGEINSTANCEDELETE|STICKERCREATE|STICKERUPDATE|STICKERDELETE|GUILDSCHEDULEDEVENTCREATE|GUILDSCHEDULEDEVENTUPDATE|GUILDSCHEDULEDEVENTDELETE|THREADCREATE|THREADUPDATE|THREADDELETE|APPLICATIONCOMMANDPERMISSIONUPDATE|SOUNDBOARDSOUNDCREATE|SOUNDBOARDSOUNDUPDATE|SOUNDBOARDSOUNDDELETE|AUTOMODERATIONRULECREATE|AUTOMODERATIONRULEUPDATE|AUTOMODERATIONRULEDELETE|AUTOMODERATIONBLOCKMESSAGE|AUTOMODERATIONFLAGTOCHANNEL|AUTOMODERATIONUSERCOMMDISABLED|AUTOMODERATIONQUARANTINEUSER|CREATORMONETIZATIONREQUESTCREATED|CREATORMONETIZATIONTERMSACCEPTED|ONBOARDINGPROMPTCREATE|ONBOARDINGPROMPTUPDATE|ONBOARDINGPROMPTDELETE|ONBOARDINGCREATE|ONBOARDINGUPDATE|GUILDHOMEFEATUREITEM|GUILDHOMEREMOVEITEM|HARMFULLINKSBLOCKEDMESSAGE|HOMESETTINGSCREATE|HOMESETTINGSUPDATE|VOICECHANNELSTATUSCREATE|VOICECHANNELSTATUSDELETE;
 
 
 type AuditLogObjectChangeResponse record {
+    @jsondata:Name {value: "old_value"}
     anydata oldValue?;
     string? 'key?;
+    @jsondata:Name {value: "new_value"}
     anydata newValue?;
 };
 
@@ -2536,14 +3185,19 @@
 type GuildPreviewResponse record {
     EmojiResponse[] emojis;
     GuildFeatures[] features;
+    @jsondata:Name {value: "home_header"}
     string? homeHeader?;
-    ballerina/lang.int:0.0.0:Signed32 approximatePresenceCount;
+    @jsondata:Name {value: "approximate_presence_count"}
+    int:Signed32 approximatePresenceCount;
+    @jsondata:Name {value: "discovery_splash"}
     string? discoverySplash?;
-    ballerina/lang.int:0.0.0:Signed32 approximateMemberCount;
+    @jsondata:Name {value: "approximate_member_count"}
+    int:Signed32 approximateMemberCount;
     string name;
     string? icon?;
     string? description?;
     GuildStickerResponse[] stickers;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     string? splash?;
 };
@@ -2555,20 +3209,26 @@
     string name;
     boolean available;
     boolean animated;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     anydata user?;
+    @jsondata:Name {value: "require_colons"}
     boolean requireColons;
 };
 
-// Unknown type: EmojiResponseRolesItemsString
+@constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
+type EmojiResponseRolesItemsString string;
 
 
 type GuildStickerResponse record {
+    @jsondata:Name {value: "format_type"}
     anydata formatType?;
     string name;
     boolean available;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
     string? description?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     2 'type;
     anydata user?;
@@ -2577,11 +3237,15 @@
 
 
 type GroupDMInviteResponse record {
-    ballerina/lang.int:0.0.0:Signed32? maxAge?;
+    @jsondata:Name {value: "max_age"}
+    int:Signed32? maxAge?;
     string code;
+    @jsondata:Name {value: "expires_at"}
     string? expiresAt?;
-    ballerina/lang.int:0.0.0:Signed32? approximateMemberCount?;
+    @jsondata:Name {value: "approximate_member_count"}
+    int:Signed32? approximateMemberCount?;
     anydata channel?;
+    @jsondata:Name {value: "created_at"}
     string? createdAt?;
     anydata inviter?;
     anydata 'type?;
@@ -2591,13 +3255,16 @@
 
 type ExecuteGithubCompatibleWebhookQueries record {
     boolean 'wait?;
+    @http:Query {name: "thread_id"}
     string threadId?;
 };
 
 
 type GuildsVoiceStatesMeRequest record {
+    @jsondata:Name {value: "request_to_speak_timestamp"}
     string? requestToSpeakTimestamp?;
     boolean? suppress?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
 };
 
@@ -2608,22 +3275,30 @@
 
 
 type MessageComponentChannelSelectResponse record {
-    ballerina/lang.int:0.0.0:Signed32? minValues?;
+    @jsondata:Name {value: "min_values"}
+    int:Signed32? minValues?;
+    @jsondata:Name {value: "custom_id"}
     string customId;
-    ballerina/lang.int:0.0.0:Signed32? maxValues?;
+    @jsondata:Name {value: "max_values"}
+    int:Signed32? maxValues?;
+    @jsondata:Name {value: "channel_types"}
     ChannelTypes[]|() channelTypes?;
     boolean? disabled?;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
     string? placeholder?;
     8 'type;
 };
 
 
 type MessageReferenceRequest record {
+    @jsondata:Name {value: "fail_if_not_exists"}
     boolean? failIfNotExists?;
+    @jsondata:Name {value: "guild_id"}
     anydata guildId?;
+    @jsondata:Name {value: "message_id"}
     string messageId;
     anydata 'type?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
 };
 
@@ -2631,24 +3306,31 @@
 type MessageAttachmentResponse record {
     string? description?;
     boolean? ephemeral?;
+    @jsondata:Name {value: "duration_secs"}
     decimal? durationSecs?;
     string? title?;
     string url;
+    @jsondata:Name {value: "clip_participants"}
     UserResponse[]|() clipParticipants?;
     string filename;
-    ballerina/lang.int:0.0.0:Signed32 size;
+    int:Signed32 size;
+    @jsondata:Name {value: "content_type"}
     string? contentType?;
     anydata application?;
-    ballerina/lang.int:0.0.0:Signed32? width?;
+    int:Signed32? width?;
+    @jsondata:Name {value: "clip_created_at"}
     string? clipCreatedAt?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "proxy_url"}
     string proxyUrl;
     string? waveform?;
-    ballerina/lang.int:0.0.0:Signed32? height?;
+    int:Signed32? height?;
 };
 
 
 type GuildWelcomeScreenResponse record {
+    @jsondata:Name {value: "welcome_channels"}
     GuildWelcomeScreenChannelResponse[] welcomeChannels;
     string? description?;
 };
@@ -2656,42 +3338,55 @@
 
 type GuildWelcomeScreenChannelResponse record {
     string description;
+    @jsondata:Name {value: "emoji_id"}
     anydata emojiId?;
+    @jsondata:Name {value: "emoji_name"}
     string? emojiName?;
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
 
 type MentionSpamUpsertRequestPartial record {
+    @jsondata:Name {value: "event_type"}
     AutomodEventType eventType?;
+    @jsondata:Name {value: "trigger_type"}
     AutomodTriggerType triggerType?;
+    @constraint:String {maxLength: 100}
     string name?;
+    @jsondata:Name {value: "exempt_roles"}
     MentionSpamUpsertRequestPartialExemptrolesItemsString[]|() exemptRoles?;
+    @jsondata:Name {value: "exempt_channels"}
     MentionSpamUpsertRequestPartialExemptchannelsItemsString[]|() exemptChannels?;
     MentionSpamUpsertRequestPartialActions[]|() actions?;
     boolean? enabled?;
+    @jsondata:Name {value: "trigger_metadata"}
     anydata triggerMetadata?;
 };
 
-// Unknown type: MentionSpamUpsertRequestPartialExemptrolesItemsString
+type MentionSpamUpsertRequestPartialExemptrolesItemsString string;
 
-// Unknown type: MentionSpamUpsertRequestPartialExemptchannelsItemsString
+type MentionSpamUpsertRequestPartialExemptchannelsItemsString string;
 
 type ActionsOneOf57 anydata|();
 
-type MentionSpamUpsertRequestPartialActions ballerinax/discord:2.0.1:BlockMessageAction|ballerinax/discord:2.0.1:FlagToChannelAction|ballerinax/discord:2.0.1:QuarantineUserAction|ballerinax/discord:2.0.1:UserCommunicationDisabledAction|anydata|();
+type MentionSpamUpsertRequestPartialActions BlockMessageAction|FlagToChannelAction|QuarantineUserAction|UserCommunicationDisabledAction|anydata|();
 
 
 type GithubRelease record {
+    @jsondata:Name {value: "tag_name"}
     string tagName;
     GithubUser author;
+    @jsondata:Name {value: "html_url"}
     string htmlUrl;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
 };
 
 
 type GithubReview record {
+    @jsondata:Name {value: "html_url"}
     string htmlUrl;
+    @constraint:String {maxLength: 152133}
     string state;
     string? body?;
     GithubUser user;
@@ -2706,18 +3401,21 @@
 
 
 type MessageReactionResponse record {
+    @jsondata:Name {value: "count_details"}
     MessageReactionCountDetailsResponse countDetails;
     MessageReactionEmojiResponse emoji;
+    @jsondata:Name {value: "me_burst"}
     boolean meBurst;
-    ballerina/lang.int:0.0.0:Signed32 count;
+    int:Signed32 count;
     boolean me;
+    @jsondata:Name {value: "burst_colors"}
     string[] burstColors;
 };
 
 
 type MessageReactionCountDetailsResponse record {
-    ballerina/lang.int:0.0.0:Signed32 normal;
-    ballerina/lang.int:0.0.0:Signed32 burst;
+    int:Signed32 normal;
+    int:Signed32 burst;
 };
 
 
@@ -2727,34 +3425,38 @@
     anydata id?;
 };
 
-type ApplicationCommandUpdateRequestOptions ballerinax/discord:2.0.1:ApplicationCommandAttachmentOption|ballerinax/discord:2.0.1:ApplicationCommandBooleanOption|ballerinax/discord:2.0.1:ApplicationCommandChannelOption|ballerinax/discord:2.0.1:ApplicationCommandIntegerOption|ballerinax/discord:2.0.1:ApplicationCommandMentionableOption|ballerinax/discord:2.0.1:ApplicationCommandNumberOption|ballerinax/discord:2.0.1:ApplicationCommandRoleOption|ballerinax/discord:2.0.1:ApplicationCommandStringOption|ballerinax/discord:2.0.1:ApplicationCommandSubcommandGroupOption|ballerinax/discord:2.0.1:ApplicationCommandSubcommandOption|ballerinax/discord:2.0.1:ApplicationCommandUserOption|anydata|();
+type ApplicationCommandUpdateRequestOptions ApplicationCommandAttachmentOption|ApplicationCommandBooleanOption|ApplicationCommandChannelOption|ApplicationCommandIntegerOption|ApplicationCommandMentionableOption|ApplicationCommandNumberOption|ApplicationCommandRoleOption|ApplicationCommandStringOption|ApplicationCommandSubcommandGroupOption|ApplicationCommandSubcommandOption|ApplicationCommandUserOption|anydata|();
 
 
 type GuildsEmojisRequest1 record {
     record {|byte[] fileContent; string fileName; anydata...;|} image;
     GuildsEmojisRequest1Roles[]|() roles?;
+    @constraint:String {maxLength: 32, minLength: 2}
     string name;
 };
 
-// Unknown type: BaseCreateMessageCreateRequestStickeridsItemsString
+type BaseCreateMessageCreateRequestStickeridsItemsString string;
 
 # Represents the Queries record for the operation: get_guild
 
 type GetGuildQueries record {
+    @http:Query {name: "with_counts"}
     boolean withCounts?;
 };
 
 
 type MessageMentionChannelResponse record {
     string name;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     ChannelTypes 'type;
 };
 
 type MentionChannelsOneOf2 anydata|();
 
-type BasicMessageResponseMentionChannels ballerinax/discord:2.0.1:MessageMentionChannelResponse|anydata|();
+type BasicMessageResponseMentionChannels MessageMentionChannelResponse|anydata|();
 
 
 type GuildMFALevelResponse record {
@@ -2764,33 +3466,42 @@
 
 type GuildIdStickersBody record {
     record {|byte[] fileContent; string fileName; anydata...;|} file;
+    @constraint:String {maxLength: 30, minLength: 2}
     string name;
     string? description?;
+    @constraint:String {maxLength: 200, minLength: 1}
     string tags;
 };
 
-// Unknown type: UpdateGuildOnboardingRequestDefaultchannelidsItemsString
+type UpdateGuildOnboardingRequestDefaultchannelidsItemsString string;
 
 
 type OnboardingPromptOptionRequest record {
+    @jsondata:Name {value: "channel_ids"}
     OnboardingPromptOptionRequestChannelidsItemsString[]|() channelIds?;
     string? description?;
+    @jsondata:Name {value: "emoji_id"}
     anydata emojiId?;
+    @jsondata:Name {value: "emoji_name"}
     string? emojiName?;
     anydata id?;
+    @constraint:String {maxLength: 50, minLength: 1}
     string title;
+    @jsondata:Name {value: "emoji_animated"}
     boolean? emojiAnimated?;
+    @jsondata:Name {value: "role_ids"}
     OnboardingPromptOptionRequestRoleidsItemsString[]|() roleIds?;
 };
 
-// Unknown type: OnboardingPromptOptionRequestRoleidsItemsString
+type OnboardingPromptOptionRequestRoleidsItemsString string;
 
 
 type IncomingWebhookInteractionRequest record {
     ActionRow[]|() components?;
     boolean? tts?;
     MessageAttachmentRequest[]|() attachments?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
+    @jsondata:Name {value: "allowed_mentions"}
     anydata allowedMentions?;
     RichEmbed[]|() embeds?;
     string? content?;
@@ -2798,73 +3509,92 @@
 
 
 type KeywordUpsertRequest record {
+    @jsondata:Name {value: "event_type"}
     AutomodEventType eventType;
+    @jsondata:Name {value: "trigger_type"}
     1 triggerType;
+    @constraint:String {maxLength: 100}
     string name;
+    @jsondata:Name {value: "exempt_roles"}
     KeywordUpsertRequestExemptrolesItemsString[]|() exemptRoles?;
+    @jsondata:Name {value: "exempt_channels"}
     KeywordUpsertRequestExemptchannelsItemsString[]|() exemptChannels?;
     KeywordUpsertRequestActions[]|() actions?;
     boolean? enabled?;
+    @jsondata:Name {value: "trigger_metadata"}
     anydata triggerMetadata?;
 };
 
-// Unknown type: KeywordUpsertRequestExemptrolesItemsString
+type KeywordUpsertRequestExemptrolesItemsString string;
 
-// Unknown type: KeywordUpsertRequestExemptchannelsItemsString
+type KeywordUpsertRequestExemptchannelsItemsString string;
 
 type ActionsOneOf52 anydata|();
 
-type KeywordUpsertRequestActions ballerinax/discord:2.0.1:BlockMessageAction|ballerinax/discord:2.0.1:FlagToChannelAction|ballerinax/discord:2.0.1:QuarantineUserAction|ballerinax/discord:2.0.1:UserCommunicationDisabledAction|anydata|();
+type KeywordUpsertRequestActions BlockMessageAction|FlagToChannelAction|QuarantineUserAction|UserCommunicationDisabledAction|anydata|();
 
 
 type KeywordUpsertRequestPartial record {
+    @jsondata:Name {value: "event_type"}
     AutomodEventType eventType?;
+    @jsondata:Name {value: "trigger_type"}
     AutomodTriggerType triggerType?;
+    @constraint:String {maxLength: 100}
     string name?;
+    @jsondata:Name {value: "exempt_roles"}
     KeywordUpsertRequestPartialExemptrolesItemsString[]|() exemptRoles?;
+    @jsondata:Name {value: "exempt_channels"}
     KeywordUpsertRequestPartialExemptchannelsItemsString[]|() exemptChannels?;
     KeywordUpsertRequestPartialActions[]|() actions?;
     boolean? enabled?;
+    @jsondata:Name {value: "trigger_metadata"}
     anydata triggerMetadata?;
 };
 
-// Unknown type: KeywordUpsertRequestPartialExemptchannelsItemsString
+type KeywordUpsertRequestPartialExemptchannelsItemsString string;
 
 type ActionsOneOf53 anydata|();
 
-type KeywordUpsertRequestPartialActions ballerinax/discord:2.0.1:BlockMessageAction|ballerinax/discord:2.0.1:FlagToChannelAction|ballerinax/discord:2.0.1:QuarantineUserAction|ballerinax/discord:2.0.1:UserCommunicationDisabledAction|anydata|();
+type KeywordUpsertRequestPartialActions BlockMessageAction|FlagToChannelAction|QuarantineUserAction|UserCommunicationDisabledAction|anydata|();
 
 
 type MentionSpamTriggerMetadata record {
-    ballerina/lang.int:0.0.0:Signed32 mentionTotalLimit;
+    @jsondata:Name {value: "mention_total_limit"}
+    int:Signed32 mentionTotalLimit;
+    @jsondata:Name {value: "mention_raid_protection_enabled"}
     boolean? mentionRaidProtectionEnabled?;
 };
 
 # Represents the Queries record for the operation: get_original_webhook_message
 
 type GetOriginalWebhookMessageQueries record {
+    @http:Query {name: "thread_id"}
     string threadId?;
 };
 
 # Represents the Headers record for the operation: create_message
 
 type CreateMessageHeaders record {
+    @http:Header {name: "Content-Type"}
     "application/x-www-form-urlencoded" contentType;
 };
 
 
 type GuildPruneResponse record {
-    ballerina/lang.int:0.0.0:Signed32? pruned?;
+    int:Signed32? pruned?;
 };
 
-// Unknown type: APPLICATIONSUBSCRIPTION
+type APPLICATIONSUBSCRIPTION 8;
 
 
 type GithubIssue record {
-    ballerina/lang.int:0.0.0:Signed32 number;
+    int:Signed32 number;
+    @jsondata:Name {value: "pull_request"}
     anydata pullRequest?;
+    @jsondata:Name {value: "html_url"}
     string htmlUrl;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
+    @constraint:String {maxLength: 152133}
     string title;
     string? body?;
     GithubUser user;
@@ -2873,31 +3603,47 @@
 
 type UpdateGuildChannelRequestPartial record {
     boolean? nsfw?;
-    ballerina/lang.int:0.0.0:Signed32? rateLimitPerUser?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
-    ballerina/lang.int:0.0.0:Signed32? bitrate?;
+    @jsondata:Name {value: "rate_limit_per_user"}
+    int:Signed32? rateLimitPerUser?;
+    int:Signed32? flags?;
+    int:Signed32? bitrate?;
     anydata 'type?;
-    ballerina/lang.int:0.0.0:Signed32? userLimit?;
+    @jsondata:Name {value: "user_limit"}
+    int:Signed32? userLimit?;
+    @jsondata:Name {value: "permission_overwrites"}
     ChannelPermissionOverwriteRequest[]|() permissionOverwrites?;
+    @jsondata:Name {value: "rtc_region"}
     string? rtcRegion?;
-    ballerina/lang.int:0.0.0:Signed32? defaultThreadRateLimitPerUser?;
+    @jsondata:Name {value: "default_thread_rate_limit_per_user"}
+    int:Signed32? defaultThreadRateLimitPerUser?;
+    @jsondata:Name {value: "default_auto_archive_duration"}
     anydata defaultAutoArchiveDuration?;
+    @jsondata:Name {value: "parent_id"}
     anydata parentId?;
+    @jsondata:Name {value: "default_reaction_emoji"}
     anydata defaultReactionEmoji?;
+    @constraint:String {maxLength: 100, minLength: 1}
     string name?;
     string? topic?;
+    @jsondata:Name {value: "default_forum_layout"}
     anydata defaultForumLayout?;
-    ballerina/lang.int:0.0.0:Signed32? position?;
+    int:Signed32? position?;
+    @jsondata:Name {value: "available_tags"}
     UpdateThreadTagRequest[]|() availableTags?;
+    @jsondata:Name {value: "video_quality_mode"}
     anydata videoQualityMode?;
+    @jsondata:Name {value: "default_sort_order"}
     anydata defaultSortOrder?;
 };
 
 
 type UpdateThreadTagRequest record {
     boolean? moderated?;
+    @constraint:String {maxLength: 20}
     string name;
+    @jsondata:Name {value: "emoji_id"}
     anydata emojiId?;
+    @jsondata:Name {value: "emoji_name"}
     string? emojiName?;
     anydata id?;
 };
@@ -2905,49 +3651,63 @@
 
 type UpdateThreadRequestPartial record {
     boolean? archived?;
+    @jsondata:Name {value: "rtc_region"}
     string? rtcRegion?;
-    ballerina/lang.int:0.0.0:Signed32? rateLimitPerUser?;
+    @jsondata:Name {value: "rate_limit_per_user"}
+    int:Signed32? rateLimitPerUser?;
     string? name?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
     boolean? invitable?;
-    ballerina/lang.int:0.0.0:Signed32? bitrate?;
+    int:Signed32? bitrate?;
     boolean? locked?;
-    ballerina/lang.int:0.0.0:Signed32? userLimit?;
+    @jsondata:Name {value: "user_limit"}
+    int:Signed32? userLimit?;
+    @jsondata:Name {value: "auto_archive_duration"}
     anydata autoArchiveDuration?;
+    @jsondata:Name {value: "applied_tags"}
     UpdateThreadRequestPartialAppliedtagsItemsString[]|() appliedTags?;
+    @jsondata:Name {value: "video_quality_mode"}
     anydata videoQualityMode?;
 };
 
-type ChannelschannelIdBody ballerinax/discord:2.0.1:PrivateChannelRequestPartial|ballerinax/discord:2.0.1:UpdateGuildChannelRequestPartial|ballerinax/discord:2.0.1:UpdateThreadRequestPartial;
+type ChannelschannelIdBody PrivateChannelRequestPartial|UpdateGuildChannelRequestPartial|UpdateThreadRequestPartial;
 
-// Unknown type: ROLES
+# Controls user mentions
+type ROLES "roles";
 
-// Unknown type: GuildsBulkBanRequestUseridsItemsString
+type GuildsBulkBanRequestUseridsItemsString string;
 
 
 type ChannelIdMessagesBody record {
     ActionRow[]|() components?;
     boolean? tts?;
     MessageAttachmentRequest[]|() attachments?;
+    @jsondata:Name {value: "sticker_ids"}
     ChannelIdMessagesBodyStickeridsItemsString[]|() stickerIds?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
+    @jsondata:Name {value: "allowed_mentions"}
     anydata allowedMentions?;
+    @jsondata:Name {value: "message_reference"}
     anydata messageReference?;
     RichEmbed[]|() embeds?;
     anydata nonce?;
     string? content?;
 };
 
-// Unknown type: ChannelIdMessagesBodyStickeridsItemsString
+type ChannelIdMessagesBodyStickeridsItemsString string;
 
 type RolesRolesOneOf12 anydata|();
 
 
 type CreateForumThreadRequest record {
-    ballerina/lang.int:0.0.0:Signed32? rateLimitPerUser?;
+    @jsondata:Name {value: "rate_limit_per_user"}
+    int:Signed32? rateLimitPerUser?;
+    @constraint:String {maxLength: 100, minLength: 1}
     string name;
     BaseCreateMessageCreateRequest message;
+    @jsondata:Name {value: "auto_archive_duration"}
     anydata autoArchiveDuration?;
+    @jsondata:Name {value: "applied_tags"}
     CreateForumThreadRequestAppliedtagsItemsString[]|() appliedTags?;
 };
 
@@ -2955,14 +3715,16 @@
 type BaseCreateMessageCreateRequest record {
     ActionRow[]|() components?;
     MessageAttachmentRequest[]|() attachments?;
+    @jsondata:Name {value: "sticker_ids"}
     BaseCreateMessageCreateRequestStickeridsItemsString[]|() stickerIds?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
+    @jsondata:Name {value: "allowed_mentions"}
     anydata allowedMentions?;
     RichEmbed[]|() embeds?;
     string? content?;
 };
 
-type ChannelIdThreadsBody ballerinax/discord:2.0.1:CreateForumThreadRequest|ballerinax/discord:2.0.1:CreateTextThreadWithoutMessageRequest;
+type ChannelIdThreadsBody CreateForumThreadRequest|CreateTextThreadWithoutMessageRequest;
 
 # Represents the Queries record for the operation: get_guild_widget_png
 
@@ -2970,34 +3732,44 @@
     WidgetImageStyles style?;
 };
 
-// Unknown type: SHIELD
+# shield style widget with Discord icon and guild members online count
+type SHIELD "shield";
 
-// Unknown type: BANNER1
+# large image with guild icon, name and online count. "POWERED BY DISCORD" as the footer of the widget
+type BANNER1 "banner1";
 
-// Unknown type: BANNER2
+# smaller widget style with guild icon, name and online count. Split on the right with Discord logo
+type BANNER2 "banner2";
 
-// Unknown type: BANNER3
+# large image with guild icon, name and online count. In the footer, Discord logo on the left and "Chat Now" on the right
+type BANNER3 "banner3";
 
-// Unknown type: BANNER4
+# large Discord logo at the top of the widget. Guild icon, name and online count in the middle portion of the widget and a "JOIN MY SERVER" button at the bottom
+type BANNER4 "banner4";
 
-type WidgetImageStyles ballerinax/discord:2.0.1:SHIELD|ballerinax/discord:2.0.1:BANNER1|ballerinax/discord:2.0.1:BANNER2|ballerinax/discord:2.0.1:BANNER3|ballerinax/discord:2.0.1:BANNER4;
+type WidgetImageStyles SHIELD|BANNER1|BANNER2|BANNER3|BANNER4;
 
 # Represents the Queries record for the operation: list_messages
 
 type ListMessagesQueries record {
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string before?;
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    @constraint:Int {minValue: 1, maxValue: 100}
+    int:Signed32 'limit?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string after?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string around?;
 };
 
 
 type PurchaseNotificationResponse record {
+    @jsondata:Name {value: "guild_product_purchase"}
     anydata guildProductPurchase?;
     PurchaseType 'type;
 };
 
-// Unknown type: CHANNELMESSAGEWITHSOURCE
+type CHANNELMESSAGEWITHSOURCE 4;
 
 
 type UpdateMessageInteractionCallbackRequest record {
@@ -3005,27 +3777,31 @@
     InteractionCallbackTypes 'type;
 };
 
-// Unknown type: PONG
+type PONG 1;
 
-// Unknown type: DEFERREDCHANNELMESSAGEWITHSOURCE
+type DEFERREDCHANNELMESSAGEWITHSOURCE 5;
 
-// Unknown type: DEFERREDUPDATEMESSAGE
+type DEFERREDUPDATEMESSAGE 6;
 
-// Unknown type: UPDATEMESSAGE
+type UPDATEMESSAGE 7;
 
-// Unknown type: MODAL
+type MODAL 9;
 
-type InteractionCallbackTypes ballerinax/discord:2.0.1:PONG|ballerinax/discord:2.0.1:CHANNELMESSAGEWITHSOURCE|ballerinax/discord:2.0.1:DEFERREDCHANNELMESSAGEWITHSOURCE|ballerinax/discord:2.0.1:DEFERREDUPDATEMESSAGE|ballerinax/discord:2.0.1:UPDATEMESSAGE|ballerinax/discord:2.0.1:APPLICATIONCOMMANDAUTOCOMPLETERESULT|ballerinax/discord:2.0.1:MODAL;
+type InteractionCallbackTypes PONG|CHANNELMESSAGEWITHSOURCE|DEFERREDCHANNELMESSAGEWITHSOURCE|DEFERREDUPDATEMESSAGE|UPDATEMESSAGE|APPLICATIONCOMMANDAUTOCOMPLETERESULT|MODAL;
 
-// Unknown type: APPLICATIONCOMMAND
+# Sent when a user uses an application command
+type APPLICATIONCOMMAND 2;
 
-// Unknown type: MESSAGECOMPONENT
+# Sent when a user interacts with a message component previously sent by your application
+type MESSAGECOMPONENT 3;
 
-// Unknown type: APPLICATIONCOMMANDAUTOCOMPLETE
+# Sent when a user is filling in an autocomplete option in a chat command
+type APPLICATIONCOMMANDAUTOCOMPLETE 4;
 
-// Unknown type: MODALSUBMIT
+# Sent when a user submits a modal previously sent by your application
+type MODALSUBMIT 5;
 
-type InteractionTypes ballerinax/discord:2.0.1:PING|ballerinax/discord:2.0.1:APPLICATIONCOMMAND|ballerinax/discord:2.0.1:MESSAGECOMPONENT|ballerinax/discord:2.0.1:APPLICATIONCOMMANDAUTOCOMPLETE|ballerinax/discord:2.0.1:MODALSUBMIT;
+type InteractionTypes PING|APPLICATIONCOMMAND|MESSAGECOMPONENT|APPLICATIONCOMMANDAUTOCOMPLETE|MODALSUBMIT;
 
 
 type GithubCheckRunOutput record {
@@ -3035,25 +3811,31 @@
 
 
 type CreatePrivateChannelRequest record {
+    @jsondata:Name {value: "access_tokens"}
     CreatePrivateChannelRequestAccesstokensItemsString[]|() accessTokens?;
+    @jsondata:Name {value: "recipient_id"}
     anydata recipientId?;
     record {|string?...;|}? nicks?;
 };
 
 
 type ChannelsWebhooksRequest record {
+    @constraint:String {maxLength: 80, minLength: 1}
     string name;
     record {|byte[] fileContent; string fileName; anydata...;|}? avatar?;
 };
 
-// Unknown type: RolesOneOf1
+@constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
+type RolesOneOf1 string;
 
-type MessageAllowedMentionsRequestRoles ballerinax/discord:2.0.1:RolesOneOf1|anydata|();
+type MessageAllowedMentionsRequestRoles RolesOneOf1|anydata|();
 
-// Unknown type: SkuIdsSkuIdsOneOf12
+@constraint:Array {maxLength: 100}
+type SkuIdsSkuIdsOneOf12 InlineArrayItemsSkuIdsSkuIdsOneOf12[];
 
 
 type WebhookTokenSlackBody record {
+    @jsondata:Name {value: "icon_url"}
     string? iconUrl?;
     WebhookSlackEmbed[]|() attachments?;
     string? text?;
@@ -3062,31 +3844,42 @@
 
 
 type WebhookSlackEmbed record {
+    @jsondata:Name {value: "author_name"}
     string? authorName?;
+    @jsondata:Name {value: "thumb_url"}
     string? thumbUrl?;
     string? color?;
     string? footer?;
+    @jsondata:Name {value: "image_url"}
     string? imageUrl?;
+    @jsondata:Name {value: "footer_icon"}
     string? footerIcon?;
+    @jsondata:Name {value: "title_link"}
     string? titleLink?;
     string? title?;
+    @jsondata:Name {value: "author_link"}
     string? authorLink?;
+    @jsondata:Name {value: "author_icon"}
     string? authorIcon?;
     string? pretext?;
     string? text?;
     WebhookSlackEmbedField[]|() fields?;
-    ballerina/lang.int:0.0.0:Signed32? ts?;
+    int:Signed32? ts?;
 };
 
-// Unknown type: ONEHOUR1
+# One hour
+type ONEHOUR1 60;
 
-// Unknown type: ONEDAY
+# One day
+type ONEDAY 1440;
 
-// Unknown type: THREEDAY
+# Three days
+type THREEDAY 4320;
 
-// Unknown type: SEVENDAY
+# Seven days
+type SEVENDAY 10080;
 
-type ThreadAutoArchiveDuration ballerinax/discord:2.0.1:ONEHOUR1|ballerinax/discord:2.0.1:ONEDAY|ballerinax/discord:2.0.1:THREEDAY|ballerinax/discord:2.0.1:SEVENDAY;
+type ThreadAutoArchiveDuration ONEHOUR1|ONEDAY|THREEDAY|SEVENDAY;
 
 type ActionsOneOf55 anydata|();
 
@@ -3096,10 +3889,11 @@
 type WebhookSourceGuildResponse record {
     string? icon?;
     string name;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
 };
 
-// Unknown type: VIEW
+type VIEW 0;
 
 
 type ResourceChannelResponse record {
@@ -3107,34 +3901,48 @@
     string? icon?;
     string description;
     string title;
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
 
 type CreateGuildChannelRequest record {
     boolean? nsfw?;
-    ballerina/lang.int:0.0.0:Signed32? rateLimitPerUser?;
-    ballerina/lang.int:0.0.0:Signed32? bitrate?;
+    @jsondata:Name {value: "rate_limit_per_user"}
+    int:Signed32? rateLimitPerUser?;
+    int:Signed32? bitrate?;
     anydata 'type?;
-    ballerina/lang.int:0.0.0:Signed32? userLimit?;
+    @jsondata:Name {value: "user_limit"}
+    int:Signed32? userLimit?;
+    @jsondata:Name {value: "permission_overwrites"}
     ChannelPermissionOverwriteRequest[]|() permissionOverwrites?;
+    @jsondata:Name {value: "rtc_region"}
     string? rtcRegion?;
-    ballerina/lang.int:0.0.0:Signed32? defaultThreadRateLimitPerUser?;
+    @jsondata:Name {value: "default_thread_rate_limit_per_user"}
+    int:Signed32? defaultThreadRateLimitPerUser?;
+    @jsondata:Name {value: "default_auto_archive_duration"}
     anydata defaultAutoArchiveDuration?;
+    @jsondata:Name {value: "parent_id"}
     anydata parentId?;
+    @jsondata:Name {value: "default_reaction_emoji"}
     anydata defaultReactionEmoji?;
+    @constraint:String {maxLength: 100, minLength: 1}
     string name;
     string? topic?;
+    @jsondata:Name {value: "default_forum_layout"}
     anydata defaultForumLayout?;
-    ballerina/lang.int:0.0.0:Signed32? position?;
+    int:Signed32? position?;
+    @jsondata:Name {value: "available_tags"}
     CreateGuildChannelRequestAvailableTags[]|() availableTags?;
+    @jsondata:Name {value: "video_quality_mode"}
     anydata videoQualityMode?;
+    @jsondata:Name {value: "default_sort_order"}
     anydata defaultSortOrder?;
 };
 
 type AvailableTagsOneOf2 anydata|();
 
-type CreateGuildChannelRequestAvailableTags ballerinax/discord:2.0.1:CreateOrUpdateThreadTagRequest|anydata|();
+type CreateGuildChannelRequestAvailableTags CreateOrUpdateThreadTagRequest|anydata|();
 
 
 type WidgetMember record {
@@ -3144,19 +3952,24 @@
     string? avatar?;
     boolean? suppress?;
     WidgetUserDiscriminator discriminator;
+    @jsondata:Name {value: "avatar_url"}
     string avatarUrl;
+    @jsondata:Name {value: "self_deaf"}
     boolean? selfDeaf?;
     string id;
+    @jsondata:Name {value: "self_mute"}
     boolean? selfMute?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
     string username;
     string status;
 };
 
-// Unknown type: WidgetUserDiscriminator
+type WidgetUserDiscriminator ZEROES;
 
 
 type ChannelsMessagesBulkDeleteRequest record {
+    @constraint:Array {maxLength: 100, minLength: 2}
     ChannelsMessagesBulkDeleteRequestMessagesItemsString[] messages;
 };
 
@@ -3168,8 +3981,10 @@
 
 
 type GuildsBansRequest record {
-    ballerina/lang.int:0.0.0:Signed32? deleteMessageDays?;
-    ballerina/lang.int:0.0.0:Signed32? deleteMessageSeconds?;
+    @jsondata:Name {value: "delete_message_days"}
+    int:Signed32? deleteMessageDays?;
+    @jsondata:Name {value: "delete_message_seconds"}
+    int:Signed32? deleteMessageSeconds?;
 };
 
 
@@ -3180,18 +3995,21 @@
 
 type 200AnyOf41 anydata|();
 
-type InteractionApplicationCommandAutocompleteCallbackStringDataChoices ballerinax/discord:2.0.1:ApplicationCommandOptionStringChoice|anydata|();
+type InteractionApplicationCommandAutocompleteCallbackStringDataChoices ApplicationCommandOptionStringChoice|anydata|();
 
 
 type WelcomeMessageResponse record {
+    @jsondata:Name {value: "author_ids"}
     WelcomeMessageResponseAuthoridsItemsString[] authorIds;
     string message;
 };
 
 
 type MessageInteractionResponse record {
+    @jsondata:Name {value: "name_localized"}
     string? nameLocalized?;
     string name;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     InteractionTypes 'type;
     anydata user?;
@@ -3200,7 +4018,9 @@
 
 type ApplicationUserRoleConnectionResponse record {
     record {|string...;|}? metadata?;
+    @jsondata:Name {value: "platform_username"}
     string? platformUsername?;
+    @jsondata:Name {value: "platform_name"}
     string? platformName?;
 };
 
@@ -3210,8 +4030,11 @@
     string name;
     string? icon?;
     string description;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "cover_image"}
     string? coverImage?;
+    @jsondata:Name {value: "primary_sku_id"}
     anydata primarySkuId?;
     anydata 'type?;
 };
@@ -3219,28 +4042,32 @@
 # Represents the Queries record for the operation: get_webhook_message
 
 type GetWebhookMessageQueries record {
+    @http:Query {name: "thread_id"}
     string threadId?;
 };
 
-// Unknown type: QUESTREWARD
+type QUESTREWARD 10;
 
 
 type GuildsMembersRequest record {
     string? nick?;
+    @jsondata:Name {value: "access_token"}
     string accessToken;
     GuildsMembersRequestRoles[]|() roles?;
     boolean? deaf?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
     boolean? mute?;
 };
 
-// Unknown type: GuildMemberResponseRolesItemsString
+@constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
+type GuildMemberResponseRolesItemsString string;
 
 type ChoicesOneOf2 anydata|();
 
 # Represents the Queries record for the operation: get_guild_scheduled_event
 
 type GetGuildScheduledEventQueries record {
+    @http:Query {name: "with_user_count"}
     boolean withUserCount?;
 };
 
@@ -3254,6 +4081,7 @@
 
 type ApplicationCommandPermission record {
     boolean permission;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     ApplicationCommandPermissionType 'type;
 };
@@ -3262,142 +4090,188 @@
 type GuildInviteResponse record {
     boolean? temporary?;
     string code;
+    @jsondata:Name {value: "guild_scheduled_event"}
     anydata guildScheduledEvent?;
-    ballerina/lang.int:0.0.0:Signed32? approximatePresenceCount?;
+    @jsondata:Name {value: "approximate_presence_count"}
+    int:Signed32? approximatePresenceCount?;
+    @jsondata:Name {value: "target_application"}
     anydata targetApplication?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
     anydata channel?;
+    @jsondata:Name {value: "target_type"}
     anydata targetType?;
+    @jsondata:Name {value: "created_at"}
     string? createdAt?;
     anydata 'type?;
+    @jsondata:Name {value: "is_contact"}
     boolean? isContact?;
-    ballerina/lang.int:0.0.0:Signed32? maxAge?;
+    @jsondata:Name {value: "max_age"}
+    int:Signed32? maxAge?;
     anydata guild?;
+    @jsondata:Name {value: "expires_at"}
     string? expiresAt?;
-    ballerina/lang.int:0.0.0:Signed32? maxUses?;
-    ballerina/lang.int:0.0.0:Signed32? approximateMemberCount?;
+    @jsondata:Name {value: "max_uses"}
+    int:Signed32? maxUses?;
+    @jsondata:Name {value: "approximate_member_count"}
+    int:Signed32? approximateMemberCount?;
+    @jsondata:Name {value: "guild_id"}
     anydata guildId?;
+    @jsondata:Name {value: "target_user"}
     anydata targetUser?;
     anydata inviter?;
-    ballerina/lang.int:0.0.0:Signed32? uses?;
+    int:Signed32? uses?;
+    @jsondata:Name {value: "stage_instance"}
     anydata stageInstance?;
 };
 
-// Unknown type: TALK
+type TALK 1;
 
-type NewMemberActionType ballerinax/discord:2.0.1:VIEW|ballerinax/discord:2.0.1:TALK;
+type NewMemberActionType VIEW|TALK;
 
 
 type DefaultKeywordListUpsertRequest record {
+    @jsondata:Name {value: "event_type"}
     AutomodEventType eventType;
+    @jsondata:Name {value: "trigger_type"}
     4 triggerType;
+    @constraint:String {maxLength: 100}
     string name;
+    @jsondata:Name {value: "exempt_roles"}
     DefaultKeywordListUpsertRequestExemptrolesItemsString[]|() exemptRoles?;
+    @jsondata:Name {value: "exempt_channels"}
     DefaultKeywordListUpsertRequestExemptchannelsItemsString[]|() exemptChannels?;
     DefaultKeywordListUpsertRequestActions[]|() actions?;
     boolean? enabled?;
+    @jsondata:Name {value: "trigger_metadata"}
     DefaultKeywordListTriggerMetadata triggerMetadata;
 };
 
-// Unknown type: DefaultKeywordListUpsertRequestExemptrolesItemsString
+type DefaultKeywordListUpsertRequestExemptrolesItemsString string;
 
-// Unknown type: DefaultKeywordListUpsertRequestExemptchannelsItemsString
+type DefaultKeywordListUpsertRequestExemptchannelsItemsString string;
 
 type NewMemberActionsOneOf2 anydata|();
 
 
 type GuildOnboardingResponse record {
+    @jsondata:Name {value: "default_channel_ids"}
     GuildOnboardingResponseDefaultchannelidsItemsString[] defaultChannelIds;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
     OnboardingPromptResponse[] prompts;
     boolean enabled;
 };
 
-// Unknown type: GuildOnboardingResponseDefaultchannelidsItemsString
+type GuildOnboardingResponseDefaultchannelidsItemsString string;
 
 
 type OnboardingPromptResponse record {
+    @jsondata:Name {value: "in_onboarding"}
     boolean inOnboarding;
     OnboardingPromptOptionResponse[] options;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     string title;
     OnboardingPromptType 'type;
+    @jsondata:Name {value: "single_select"}
     boolean singleSelect;
     boolean required;
 };
 
-type OnboardingPromptType ballerinax/discord:2.0.1:MULTIPLECHOICE|ballerinax/discord:2.0.1:DROPDOWN;
+type OnboardingPromptType MULTIPLECHOICE|DROPDOWN;
 
 
 type MessageAllowedMentionsRequest record {
     MessageAllowedMentionsRequestRoles[]|() roles?;
     AllowedMentionTypes[]|() parse?;
+    @jsondata:Name {value: "replied_user"}
     boolean? repliedUser?;
     MessageAllowedMentionsRequestUsers[]|() users?;
 };
 
-// Unknown type: EVERYONE
+# Controls @everyone and @here mentions
+type EVERYONE "everyone";
 
-type AllowedMentionTypes ballerinax/discord:2.0.1:USERS|ballerinax/discord:2.0.1:ROLES|ballerinax/discord:2.0.1:EVERYONE;
+type AllowedMentionTypes USERS|ROLES|EVERYONE;
 
-// Unknown type: UsersOneOf1
+@constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
+type UsersOneOf1 string;
 
-type MessageAllowedMentionsRequestUsers ballerinax/discord:2.0.1:UsersOneOf1|anydata|();
+type MessageAllowedMentionsRequestUsers UsersOneOf1|anydata|();
 
 
 type VoiceScheduledEventPatchRequestPartial record {
     record {|byte[] fileContent; string fileName; anydata...;|}? image?;
+    @jsondata:Name {value: "entity_type"}
     anydata entityType?;
+    @jsondata:Name {value: "privacy_level"}
     GuildScheduledEventPrivacyLevels privacyLevel?;
+    @constraint:String {maxLength: 100}
     string name?;
+    @jsondata:Name {value: "entity_metadata"}
     anydata entityMetadata?;
     string? description?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
     anydata status?;
+    @jsondata:Name {value: "scheduled_start_time"}
     string scheduledStartTime?;
+    @jsondata:Name {value: "scheduled_end_time"}
     string? scheduledEndTime?;
 };
 
-type MessageResponseMentionChannels ballerinax/discord:2.0.1:MessageMentionChannelResponse|anydata|();
+type MessageResponseMentionChannels MessageMentionChannelResponse|anydata|();
 
 
 type GuildHomeSettingsResponse record {
+    @jsondata:Name {value: "new_member_actions"}
     GuildHomeSettingsResponseNewMemberActions[]|() newMemberActions?;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
+    @jsondata:Name {value: "welcome_message"}
     anydata welcomeMessage?;
     boolean enabled;
+    @jsondata:Name {value: "resource_channels"}
     GuildHomeSettingsResponseResourceChannels[]|() resourceChannels?;
 };
 
 
 type NewMemberActionResponse record {
     anydata emoji?;
+    @jsondata:Name {value: "action_type"}
     NewMemberActionType actionType;
     string? icon?;
     string description;
     string title;
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
-type GuildHomeSettingsResponseNewMemberActions ballerinax/discord:2.0.1:NewMemberActionResponse|anydata|();
+type GuildHomeSettingsResponseNewMemberActions NewMemberActionResponse|anydata|();
 
 type ResourceChannelsOneOf2 anydata|();
 
-type GuildHomeSettingsResponseResourceChannels ballerinax/discord:2.0.1:ResourceChannelResponse|anydata|();
+type GuildHomeSettingsResponseResourceChannels ResourceChannelResponse|anydata|();
 
 
 type UpdateOnboardingPromptRequest record {
+    @jsondata:Name {value: "in_onboarding"}
     boolean? inOnboarding?;
+    @constraint:Array {maxLength: 50, minLength: 1}
     OnboardingPromptOptionRequest[] options;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @constraint:String {maxLength: 100, minLength: 1}
     string title;
     anydata 'type?;
+    @jsondata:Name {value: "single_select"}
     boolean? singleSelect?;
     boolean? required?;
 };
 
 
 type WidgetSettingsResponse record {
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
     boolean enabled;
 };
@@ -3405,12 +4279,14 @@
 # Represents the Queries record for the operation: list_guild_application_commands
 
 type ListGuildApplicationCommandsQueries record {
+    @http:Query {name: "with_localizations"}
     boolean withLocalizations?;
 };
 
 
 type GuildSubscriptionIntegrationResponse record {
     string? name?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     "guild_subscription" 'type;
     anydata account?;
@@ -3425,67 +4301,92 @@
 
 type GuildsRolesRequest2 record {
     anydata id?;
-    ballerina/lang.int:0.0.0:Signed32? position?;
+    int:Signed32? position?;
 };
 
 
 type MentionSpamUpsertRequest record {
+    @jsondata:Name {value: "event_type"}
     AutomodEventType eventType;
+    @jsondata:Name {value: "trigger_type"}
     5 triggerType;
+    @constraint:String {maxLength: 100}
     string name;
+    @jsondata:Name {value: "exempt_roles"}
     MentionSpamUpsertRequestExemptrolesItemsString[]|() exemptRoles?;
+    @jsondata:Name {value: "exempt_channels"}
     MentionSpamUpsertRequestExemptchannelsItemsString[]|() exemptChannels?;
     MentionSpamUpsertRequestActions[]|() actions?;
     boolean? enabled?;
+    @jsondata:Name {value: "trigger_metadata"}
     anydata triggerMetadata?;
 };
 
-// Unknown type: MentionSpamUpsertRequestExemptchannelsItemsString
+type MentionSpamUpsertRequestExemptchannelsItemsString string;
 
-type MentionSpamUpsertRequestActions ballerinax/discord:2.0.1:BlockMessageAction|ballerinax/discord:2.0.1:FlagToChannelAction|ballerinax/discord:2.0.1:QuarantineUserAction|ballerinax/discord:2.0.1:UserCommunicationDisabledAction|anydata|();
+type MentionSpamUpsertRequestActions BlockMessageAction|FlagToChannelAction|QuarantineUserAction|UserCommunicationDisabledAction|anydata|();
 
-type AutoModerationRulesBody ballerinax/discord:2.0.1:DefaultKeywordListUpsertRequest|ballerinax/discord:2.0.1:KeywordUpsertRequest|ballerinax/discord:2.0.1:MLSpamUpsertRequest|ballerinax/discord:2.0.1:MentionSpamUpsertRequest;
+type AutoModerationRulesBody DefaultKeywordListUpsertRequest|KeywordUpsertRequest|MLSpamUpsertRequest|MentionSpamUpsertRequest;
 
 
 type KeywordTriggerMetadata record {
+    @jsondata:Name {value: "keyword_filter"}
     KeywordTriggerMetadataKeywordfilterItemsString[]|() keywordFilter?;
+    @jsondata:Name {value: "allow_list"}
     KeywordTriggerMetadataAllowlistItemsString[]|() allowList?;
+    @jsondata:Name {value: "regex_patterns"}
     KeywordTriggerMetadataRegexpatternsItemsString[]|() regexPatterns?;
 };
 
-// Unknown type: KeywordTriggerMetadataKeywordfilterItemsString
+type KeywordTriggerMetadataKeywordfilterItemsString string;
 
-// Unknown type: KeywordTriggerMetadataAllowlistItemsString
+type KeywordTriggerMetadataAllowlistItemsString string;
 
-// Unknown type: KeywordTriggerMetadataRegexpatternsItemsString
+type KeywordTriggerMetadataRegexpatternsItemsString string;
 
-// Unknown type: DefaultKeywordListUpsertRequestPartialExemptchannelsItemsString
+type DefaultKeywordListUpsertRequestPartialExemptchannelsItemsString string;
 
 
 type GuildChannelResponse record {
+    @jsondata:Name {value: "last_pin_timestamp"}
     string? lastPinTimestamp?;
     boolean? nsfw?;
-    ballerina/lang.int:0.0.0:Signed32? rateLimitPerUser?;
-    ballerina/lang.int:0.0.0:Signed32 flags;
-    ballerina/lang.int:0.0.0:Signed32? bitrate?;
+    @jsondata:Name {value: "rate_limit_per_user"}
+    int:Signed32? rateLimitPerUser?;
+    int:Signed32 flags;
+    int:Signed32? bitrate?;
     ChannelTypes 'type;
-    ballerina/lang.int:0.0.0:Signed32? userLimit?;
+    @jsondata:Name {value: "user_limit"}
+    int:Signed32? userLimit?;
+    @jsondata:Name {value: "last_message_id"}
     anydata lastMessageId?;
+    @jsondata:Name {value: "rtc_region"}
     string? rtcRegion?;
+    @jsondata:Name {value: "permission_overwrites"}
     ChannelPermissionOverwriteResponse[]|() permissionOverwrites?;
-    ballerina/lang.int:0.0.0:Signed32? defaultThreadRateLimitPerUser?;
+    @jsondata:Name {value: "default_thread_rate_limit_per_user"}
+    int:Signed32? defaultThreadRateLimitPerUser?;
+    @jsondata:Name {value: "default_auto_archive_duration"}
     anydata defaultAutoArchiveDuration?;
+    @jsondata:Name {value: "parent_id"}
     anydata parentId?;
     string? permissions?;
+    @jsondata:Name {value: "default_reaction_emoji"}
     anydata defaultReactionEmoji?;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
     string name;
     string? topic?;
+    @jsondata:Name {value: "default_forum_layout"}
     anydata defaultForumLayout?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
-    ballerina/lang.int:0.0.0:Signed32 position;
+    int:Signed32 position;
+    @jsondata:Name {value: "available_tags"}
     ForumTagResponse[]|() availableTags?;
+    @jsondata:Name {value: "video_quality_mode"}
     anydata videoQualityMode?;
+    @jsondata:Name {value: "default_sort_order"}
     anydata defaultSortOrder?;
 };
 
@@ -3493,19 +4394,25 @@
 type ForumTagResponse record {
     boolean moderated;
     string name;
+    @jsondata:Name {value: "emoji_id"}
     anydata emojiId?;
+    @jsondata:Name {value: "emoji_name"}
     string? emojiName?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
 };
 
 
 type MessageStickerItemResponse record {
+    @jsondata:Name {value: "format_type"}
     StickerFormatTypes formatType;
     string name;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
 };
 
-// Unknown type: NONE4
+# Guild has not unlocked any Server Boost perks
+type NONE4 0;
 
 type OptionsOneOf12 anydata|();
 
@@ -3514,54 +4421,67 @@
     InteractionApplicationCommandAutocompleteCallbackIntegerDataChoices[]|() choices?;
 };
 
-type InteractionApplicationCommandAutocompleteCallbackIntegerDataChoices ballerinax/discord:2.0.1:ApplicationCommandOptionIntegerChoice|anydata|();
+type InteractionApplicationCommandAutocompleteCallbackIntegerDataChoices ApplicationCommandOptionIntegerChoice|anydata|();
 
 # Represents the Queries record for the operation: list_guild_scheduled_event_users
 
 type ListGuildScheduledEventUsersQueries record {
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string before?;
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    @constraint:Int {minValue: 1, maxValue: 100}
+    int:Signed32 'limit?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string after?;
+    @http:Query {name: "with_member"}
     boolean withMember?;
 };
 
 
 type MessageComponentInputTextResponse record {
-    ballerina/lang.int:0.0.0:Signed32? minLength?;
+    @jsondata:Name {value: "min_length"}
+    int:Signed32? minLength?;
+    @jsondata:Name {value: "custom_id"}
     string customId;
     TextStyleTypes style;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
     string? label?;
     string? placeholder?;
     4 'type;
     string? value?;
     boolean? required?;
-    ballerina/lang.int:0.0.0:Signed32? maxLength?;
+    @jsondata:Name {value: "max_length"}
+    int:Signed32? maxLength?;
 };
 
 
 type MessageComponentRoleSelectResponse record {
-    ballerina/lang.int:0.0.0:Signed32? minValues?;
+    @jsondata:Name {value: "min_values"}
+    int:Signed32? minValues?;
+    @jsondata:Name {value: "custom_id"}
     string customId;
-    ballerina/lang.int:0.0.0:Signed32? maxValues?;
+    @jsondata:Name {value: "max_values"}
+    int:Signed32? maxValues?;
     boolean? disabled?;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
     string? placeholder?;
     6 'type;
 };
 
 
 type MessageComponentUserSelectResponse record {
-    ballerina/lang.int:0.0.0:Signed32? minValues?;
+    @jsondata:Name {value: "min_values"}
+    int:Signed32? minValues?;
+    @jsondata:Name {value: "custom_id"}
     string customId;
-    ballerina/lang.int:0.0.0:Signed32? maxValues?;
+    @jsondata:Name {value: "max_values"}
+    int:Signed32? maxValues?;
     boolean? disabled?;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
     string? placeholder?;
     5 'type;
 };
 
-type MessageComponentActionRowResponseComponents ballerinax/discord:2.0.1:MessageComponentButtonResponse|ballerinax/discord:2.0.1:MessageComponentChannelSelectResponse|ballerinax/discord:2.0.1:MessageComponentInputTextResponse|ballerinax/discord:2.0.1:MessageComponentMentionableSelectResponse|ballerinax/discord:2.0.1:MessageComponentRoleSelectResponse|ballerinax/discord:2.0.1:MessageComponentStringSelectResponse|ballerinax/discord:2.0.1:MessageComponentUserSelectResponse|anydata|();
+type MessageComponentActionRowResponseComponents MessageComponentButtonResponse|MessageComponentChannelSelectResponse|MessageComponentInputTextResponse|MessageComponentMentionableSelectResponse|MessageComponentRoleSelectResponse|MessageComponentStringSelectResponse|MessageComponentUserSelectResponse|anydata|();
 
 
 type ModalInteractionCallbackRequest record {
@@ -3571,7 +4491,9 @@
 
 
 type GithubWebhook record {
+    @jsondata:Name {value: "pull_request"}
     anydata pullRequest?;
+    @jsondata:Name {value: "head_commit"}
     anydata headCommit?;
     string? compare?;
     anydata issue?;
@@ -3580,6 +4502,7 @@
     anydata discussion?;
     anydata repository?;
     string? ref?;
+    @jsondata:Name {value: "check_run"}
     anydata checkRun?;
     anydata answer?;
     GithubUser sender;
@@ -3588,7 +4511,9 @@
     string? action?;
     GithubCommit[]|() commits?;
     anydata comment?;
+    @jsondata:Name {value: "ref_type"}
     string? refType?;
+    @jsondata:Name {value: "check_suite"}
     anydata checkSuite?;
     anydata forkee?;
 };
@@ -3596,30 +4521,40 @@
 
 type GithubCommit record {
     GithubAuthor author;
+    @constraint:String {maxLength: 152133}
     string id;
+    @constraint:String {maxLength: 152133}
     string message;
+    @constraint:String {maxLength: 2048}
     string url;
 };
 
 
 type GithubAuthor record {
+    @constraint:String {maxLength: 152133}
     string name;
     string? username?;
 };
 
 
 type FriendInviteResponse record {
-    ballerina/lang.int:0.0.0:Signed32? maxAge?;
-    ballerina/lang.int:0.0.0:Signed32? friendsCount?;
+    @jsondata:Name {value: "max_age"}
+    int:Signed32? maxAge?;
+    @jsondata:Name {value: "friends_count"}
+    int:Signed32? friendsCount?;
     string code;
+    @jsondata:Name {value: "expires_at"}
     string? expiresAt?;
-    ballerina/lang.int:0.0.0:Signed32? maxUses?;
+    @jsondata:Name {value: "max_uses"}
+    int:Signed32? maxUses?;
     anydata channel?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
+    @jsondata:Name {value: "created_at"}
     string? createdAt?;
     anydata inviter?;
-    ballerina/lang.int:0.0.0:Signed32? uses?;
+    int:Signed32? uses?;
     anydata 'type?;
+    @jsondata:Name {value: "is_contact"}
     boolean? isContact?;
 };
 
@@ -3632,95 +4567,128 @@
 
 type ExternalScheduledEventCreateRequest record {
     record {|byte[] fileContent; string fileName; anydata...;|}? image?;
+    @jsondata:Name {value: "entity_type"}
     3 entityType;
+    @jsondata:Name {value: "privacy_level"}
     GuildScheduledEventPrivacyLevels privacyLevel;
+    @constraint:String {maxLength: 100}
     string name;
+    @jsondata:Name {value: "entity_metadata"}
     EntityMetadataExternal entityMetadata;
     string? description?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
+    @jsondata:Name {value: "scheduled_start_time"}
     string scheduledStartTime;
+    @jsondata:Name {value: "scheduled_end_time"}
     string? scheduledEndTime?;
 };
 
 
 type EntityMetadataExternal record {
+    @constraint:String {maxLength: 100}
     string location;
 };
 
 
 type StageScheduledEventCreateRequest record {
     record {|byte[] fileContent; string fileName; anydata...;|}? image?;
+    @jsondata:Name {value: "entity_type"}
     1 entityType;
+    @jsondata:Name {value: "privacy_level"}
     GuildScheduledEventPrivacyLevels privacyLevel;
+    @constraint:String {maxLength: 100}
     string name;
+    @jsondata:Name {value: "entity_metadata"}
     anydata entityMetadata?;
     string? description?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
+    @jsondata:Name {value: "scheduled_start_time"}
     string scheduledStartTime;
+    @jsondata:Name {value: "scheduled_end_time"}
     string? scheduledEndTime?;
 };
 
-type GuildIdScheduledEventsBody ballerinax/discord:2.0.1:ExternalScheduledEventCreateRequest|ballerinax/discord:2.0.1:StageScheduledEventCreateRequest|ballerinax/discord:2.0.1:VoiceScheduledEventCreateRequest;
+type GuildIdScheduledEventsBody ExternalScheduledEventCreateRequest|StageScheduledEventCreateRequest|VoiceScheduledEventCreateRequest;
 
 
 type GuildsStickersRequest record {
+    @constraint:String {maxLength: 30, minLength: 2}
     string name?;
     string? description?;
+    @constraint:String {maxLength: 200, minLength: 1}
     string tags?;
 };
 
 # Represents the Headers record for the operation: update_message
 
 type UpdateMessageHeaders record {
+    @http:Header {name: "Content-Type"}
     "application/x-www-form-urlencoded" contentType;
 };
 
 
 type WebhooksRequest2 record {
+    @constraint:String {maxLength: 80, minLength: 1}
     string name?;
     record {|byte[] fileContent; string fileName; anydata...;|}? avatar?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
 };
 
 
 type WebhooksRequest1 record {
+    @constraint:String {maxLength: 80, minLength: 1}
     string name?;
     record {|byte[] fileContent; string fileName; anydata...;|}? avatar?;
 };
 
 
 type MessageRoleSubscriptionDataResponse record {
+    @jsondata:Name {value: "tier_name"}
     string tierName;
+    @jsondata:Name {value: "is_renewal"}
     boolean isRenewal;
+    @jsondata:Name {value: "role_subscription_listing_id"}
     string roleSubscriptionListingId;
-    ballerina/lang.int:0.0.0:Signed32 totalMonthsSubscribed;
+    @jsondata:Name {value: "total_months_subscribed"}
+    int:Signed32 totalMonthsSubscribed;
 };
 
 
 type Emoji record {
+    @constraint:String {maxLength: 32}
     string name;
     boolean? animated?;
     anydata id?;
 };
 
-// Unknown type: TIER1
+# Guild has unlocked Server Boost level 1 perks
+type TIER1 1;
 
-// Unknown type: TIER2
+# Guild has unlocked Server Boost level 2 perks
+type TIER2 2;
 
-// Unknown type: TIER3
+# Guild has unlocked Server Boost level 3 perks
+type TIER3 3;
 
-type PremiumGuildTiers ballerinax/discord:2.0.1:NONE4|ballerinax/discord:2.0.1:TIER1|ballerinax/discord:2.0.1:TIER2|ballerinax/discord:2.0.1:TIER3;
+type PremiumGuildTiers NONE4|TIER1|TIER2|TIER3;
 
 
 type GuildMemberResponse record {
+    @jsondata:Name {value: "joined_at"}
     string joinedAt;
     string? nick?;
+    @jsondata:Name {value: "premium_since"}
     string? premiumSince?;
+    @jsondata:Name {value: "communication_disabled_until"}
     string? communicationDisabledUntil?;
+    @jsondata:Name {value: "avatar_decoration_data"}
     anydata avatarDecorationData?;
     boolean pending;
     GuildMemberResponseRolesItemsString[] roles;
-    ballerina/lang.int:0.0.0:Signed32 flags;
+    int:Signed32 flags;
     boolean deaf;
     boolean mute;
     string? avatar?;
@@ -3729,41 +4697,58 @@
 
 
 type GuildsWidgetRequest record {
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
     boolean? enabled?;
 };
 
 
 type GithubComment record {
+    @jsondata:Name {value: "html_url"}
     string htmlUrl;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
+    @constraint:String {maxLength: 152133}
     string body;
     GithubUser user;
+    @jsondata:Name {value: "commit_id"}
     string? commitId?;
 };
 
 
 type ApplicationResponse record {
+    @jsondata:Name {value: "rpc_origins"}
     string[]? rpcOrigins?;
+    @jsondata:Name {value: "privacy_policy_url"}
     string? privacyPolicyUrl?;
+    @jsondata:Name {value: "bot_require_code_grant"}
     boolean? botRequireCodeGrant?;
     anydata bot?;
     string? icon?;
-    ballerina/lang.int:0.0.0:Signed32 flags;
+    int:Signed32 flags;
     string description;
+    @jsondata:Name {value: "verify_key"}
     string verifyKey;
     anydata 'type?;
-    ballerina/lang.int:0.0.0:Signed32? maxParticipants?;
+    @jsondata:Name {value: "max_participants"}
+    int:Signed32? maxParticipants?;
     string[]? tags?;
+    @jsondata:Name {value: "custom_install_url"}
     string? customInstallUrl?;
+    @jsondata:Name {value: "install_params"}
     anydata installParams?;
     string name;
+    @jsondata:Name {value: "guild_id"}
     anydata guildId?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "cover_image"}
     string? coverImage?;
+    @jsondata:Name {value: "primary_sku_id"}
     anydata primarySkuId?;
     string? slug?;
+    @jsondata:Name {value: "bot_public"}
     boolean? botPublic?;
+    @jsondata:Name {value: "terms_of_service_url"}
     string? termsOfServiceUrl?;
 };
 
@@ -3778,95 +4763,127 @@
 
 type ListPrivateArchivedThreadsQueries record {
     string before?;
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    @constraint:Int {minValue: 2, maxValue: 100}
+    int:Signed32 'limit?;
 };
 
 
 type MessageCallResponse record {
+    @jsondata:Name {value: "ended_timestamp"}
     string? endedTimestamp?;
     MessageCallResponseParticipantsItemsString[] participants;
 };
 
-// Unknown type: MessageCallResponseParticipantsItemsString
+@constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
+type MessageCallResponseParticipantsItemsString string;
 
 # Represents the Queries record for the operation: list_guild_bans
 
 type ListGuildBansQueries record {
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string before?;
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    @constraint:Int {minValue: 1, maxValue: 1000}
+    int:Signed32 'limit?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string after?;
 };
 
-// Unknown type: DefaultKeywordListUpsertRequestPartialExemptrolesItemsString
+type DefaultKeywordListUpsertRequestPartialExemptrolesItemsString string;
 
 # Represents the Queries record for the operation: list_application_commands
 
 type ListApplicationCommandsQueries record {
+    @http:Query {name: "with_localizations"}
     boolean withLocalizations?;
 };
 
 
 type ExternalScheduledEventPatchRequestPartial record {
     record {|byte[] fileContent; string fileName; anydata...;|}? image?;
+    @jsondata:Name {value: "entity_type"}
     anydata entityType?;
+    @jsondata:Name {value: "privacy_level"}
     GuildScheduledEventPrivacyLevels privacyLevel?;
+    @constraint:String {maxLength: 100}
     string name?;
+    @jsondata:Name {value: "entity_metadata"}
     EntityMetadataExternal entityMetadata?;
     string? description?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
     anydata status?;
+    @jsondata:Name {value: "scheduled_start_time"}
     string scheduledStartTime?;
+    @jsondata:Name {value: "scheduled_end_time"}
     string? scheduledEndTime?;
 };
 
 
 type StageScheduledEventPatchRequestPartial record {
     record {|byte[] fileContent; string fileName; anydata...;|}? image?;
+    @jsondata:Name {value: "entity_type"}
     anydata entityType?;
+    @jsondata:Name {value: "privacy_level"}
     GuildScheduledEventPrivacyLevels privacyLevel?;
+    @constraint:String {maxLength: 100}
     string name?;
+    @jsondata:Name {value: "entity_metadata"}
     anydata entityMetadata?;
     string? description?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
     anydata status?;
+    @jsondata:Name {value: "scheduled_start_time"}
     string scheduledStartTime?;
+    @jsondata:Name {value: "scheduled_end_time"}
     string? scheduledEndTime?;
 };
 
-type ScheduledEventsguildScheduledEventIdBody ballerinax/discord:2.0.1:ExternalScheduledEventPatchRequestPartial|ballerinax/discord:2.0.1:StageScheduledEventPatchRequestPartial|ballerinax/discord:2.0.1:VoiceScheduledEventPatchRequestPartial;
+type ScheduledEventsguildScheduledEventIdBody ExternalScheduledEventPatchRequestPartial|StageScheduledEventPatchRequestPartial|VoiceScheduledEventPatchRequestPartial;
 
 # Represents the Queries record for the operation: list_my_private_archived_threads
 
 type ListMyPrivateArchivedThreadsQueries record {
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string before?;
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    @constraint:Int {minValue: 2, maxValue: 100}
+    int:Signed32 'limit?;
 };
 
 
 type GuildRoleTagsResponse record {
+    @jsondata:Name {value: "subscription_listing_id"}
     anydata subscriptionListingId?;
+    @jsondata:Name {value: "guild_connections"}
     string? guildConnections?;
+    @jsondata:Name {value: "integration_id"}
     anydata integrationId?;
+    @jsondata:Name {value: "premium_subscriber"}
     string? premiumSubscriber?;
+    @jsondata:Name {value: "available_for_purchase"}
     string? availableForPurchase?;
+    @jsondata:Name {value: "bot_id"}
     anydata botId?;
 };
 
-// Unknown type: UserGuildOnboardingResponseDefaultchannelidsItemsString
+type UserGuildOnboardingResponseDefaultchannelidsItemsString string;
 
 
 type VanityURLResponse record {
     string? code?;
-    ballerina/lang.int:0.0.0:Signed32 uses;
+    int:Signed32 uses;
     anydata 'error?;
 };
 
 
 type PrivateChannelResponse record {
+    @jsondata:Name {value: "last_message_id"}
     anydata lastMessageId?;
+    @jsondata:Name {value: "last_pin_timestamp"}
     string? lastPinTimestamp?;
     UserResponse[] recipients;
-    ballerina/lang.int:0.0.0:Signed32 flags;
+    int:Signed32 flags;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     1 'type;
 };
@@ -3875,13 +4892,15 @@
 
 type ListPublicArchivedThreadsQueries record {
     string before?;
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    @constraint:Int {minValue: 2, maxValue: 100}
+    int:Signed32 'limit?;
 };
 
 
 type BotAccountPatchRequest record {
     record {|byte[] fileContent; string fileName; anydata...;|}? banner?;
     record {|byte[] fileContent; string fileName; anydata...;|}? avatar?;
+    @constraint:String {maxLength: 32, minLength: 2}
     string username;
 };
 
@@ -3889,23 +4908,27 @@
 
 type ExecuteSlackCompatibleWebhookQueries record {
     boolean 'wait?;
+    @http:Query {name: "thread_id"}
     string threadId?;
 };
 
 
 type BulkBanUsersResponse record {
+    @jsondata:Name {value: "failed_users"}
     BulkBanUsersResponseFailedusersItemsString[] failedUsers;
+    @jsondata:Name {value: "banned_users"}
     BulkBanUsersResponseBannedusersItemsString[] bannedUsers;
 };
 
-// Unknown type: BulkBanUsersResponseFailedusersItemsString
+type BulkBanUsersResponseFailedusersItemsString string;
 
-// Unknown type: BulkBanUsersResponseBannedusersItemsString
+type BulkBanUsersResponseBannedusersItemsString string;
 
-type ApplicationCommandCreateRequestOptions ballerinax/discord:2.0.1:ApplicationCommandAttachmentOption|ballerinax/discord:2.0.1:ApplicationCommandBooleanOption|ballerinax/discord:2.0.1:ApplicationCommandChannelOption|ballerinax/discord:2.0.1:ApplicationCommandIntegerOption|ballerinax/discord:2.0.1:ApplicationCommandMentionableOption|ballerinax/discord:2.0.1:ApplicationCommandNumberOption|ballerinax/discord:2.0.1:ApplicationCommandRoleOption|ballerinax/discord:2.0.1:ApplicationCommandStringOption|ballerinax/discord:2.0.1:ApplicationCommandSubcommandGroupOption|ballerinax/discord:2.0.1:ApplicationCommandSubcommandOption|ballerinax/discord:2.0.1:ApplicationCommandUserOption|anydata|();
+type ApplicationCommandCreateRequestOptions ApplicationCommandAttachmentOption|ApplicationCommandBooleanOption|ApplicationCommandChannelOption|ApplicationCommandIntegerOption|ApplicationCommandMentionableOption|ApplicationCommandNumberOption|ApplicationCommandRoleOption|ApplicationCommandStringOption|ApplicationCommandSubcommandGroupOption|ApplicationCommandSubcommandOption|ApplicationCommandUserOption|anydata|();
 
 
 type WelcomeScreenPatchRequestPartial record {
+    @jsondata:Name {value: "welcome_channels"}
     GuildWelcomeChannel[]|() welcomeChannels?;
     string? description?;
     boolean? enabled?;
@@ -3914,13 +4937,16 @@
 # Represents the Queries record for the operation: preview_prune_guild
 
 type PreviewPruneGuildQueries record {
-    ballerina/lang.int:0.0.0:Signed32 days?;
+    @constraint:Int {minValue: 1, maxValue: 30}
+    int:Signed32 days?;
+    @http:Query {name: "include_roles"}
     IncludeRoles includeRoles?;
 };
 
 
 type GuildRoleResponse record {
-    ballerina/lang.int:0.0.0:Signed32 color;
+    int:Signed32 color;
+    @jsondata:Name {value: "unicode_emoji"}
     string? unicodeEmoji?;
     string permissions;
     boolean managed;
@@ -3928,28 +4954,36 @@
     string? icon?;
     string? description?;
     boolean mentionable;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
-    ballerina/lang.int:0.0.0:Signed32 position;
+    int:Signed32 position;
     boolean hoist;
     anydata tags?;
 };
 
 
 type StageInstanceResponse record {
+    @jsondata:Name {value: "privacy_level"}
     StageInstancesPrivacyLevels privacyLevel;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
     string topic;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "guild_scheduled_event_id"}
     anydata guildScheduledEventId?;
+    @jsondata:Name {value: "discoverable_disabled"}
     boolean? discoverableDisabled?;
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
 
 type WidgetChannel record {
     string name;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
-    ballerina/lang.int:0.0.0:Signed32 position;
+    int:Signed32 position;
 };
 
 
@@ -3957,14 +4991,15 @@
     InteractionApplicationCommandAutocompleteCallbackStringDataChoices[]|() choices?;
 };
 
-type InlineResponse2002 ballerinax/discord:2.0.1:FriendInviteResponse|ballerinax/discord:2.0.1:GroupDMInviteResponse|ballerinax/discord:2.0.1:GuildInviteResponse;
+type InlineResponse2002 FriendInviteResponse|GroupDMInviteResponse|GuildInviteResponse;
 
-type InlineResponse2005 ballerinax/discord:2.0.1:GuildStickerResponse|ballerinax/discord:2.0.1:StandardStickerResponse;
+type InlineResponse2005 GuildStickerResponse|StandardStickerResponse;
 
-type InlineResponse2006 ballerinax/discord:2.0.1:GuildChannelResponse|ballerinax/discord:2.0.1:PrivateChannelResponse|ballerinax/discord:2.0.1:PrivateGroupChannelResponse|ballerinax/discord:2.0.1:ThreadResponse;
+type InlineResponse2006 GuildChannelResponse|PrivateChannelResponse|PrivateGroupChannelResponse|ThreadResponse;
 
 
 type RichEmbedFooter record {
+    @jsondata:Name {value: "icon_url"}
     string? iconUrl?;
     string? text?;
 };
@@ -3972,6 +5007,7 @@
 # Represents the Queries record for the operation: update_original_webhook_message
 
 type UpdateOriginalWebhookMessageQueries record {
+    @http:Query {name: "thread_id"}
     string threadId?;
 };
 
@@ -3980,6 +5016,7 @@
 # Represents the Headers record for the operation: execute_slack_compatible_webhook
 
 type ExecuteSlackCompatibleWebhookHeaders record {
+    @http:Header {name: "Content-Type"}
     "application/x-www-form-urlencoded" contentType;
 };
 
@@ -3987,115 +5024,161 @@
 type MyGuildResponse record {
     boolean owner;
     GuildFeatures[] features;
-    ballerina/lang.int:0.0.0:Signed32? approximatePresenceCount?;
+    @jsondata:Name {value: "approximate_presence_count"}
+    int:Signed32? approximatePresenceCount?;
     string permissions;
-    ballerina/lang.int:0.0.0:Signed32? approximateMemberCount?;
+    @jsondata:Name {value: "approximate_member_count"}
+    int:Signed32? approximateMemberCount?;
     string name;
     string? icon?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
 };
 
 
 type CommandPermissionsResponse record {
     CommandPermissionResponse[] permissions;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "application_id"}
     string applicationId;
 };
 
 
 type ResolvedObjectsResponse record {
     record {|anydata...;|} channels;
-    record {|ballerinax/discord:2.0.1:GuildMemberResponse...;|} members;
-    record {|ballerinax/discord:2.0.1:GuildRoleResponse...;|} roles;
-    record {|ballerinax/discord:2.0.1:UserResponse...;|} users;
+    record {|GuildMemberResponse...;|} members;
+    record {|GuildRoleResponse...;|} roles;
+    record {|UserResponse...;|} users;
 };
 
-// Unknown type: MLSpamUpsertRequestPartialExemptrolesItemsString
+type MLSpamUpsertRequestPartialExemptrolesItemsString string;
 
 
 type GuildResponse record {
-    ballerina/lang.int:0.0.0:Signed32? maxStageVideoChannelUsers?;
+    @jsondata:Name {value: "max_stage_video_channel_users"}
+    int:Signed32? maxStageVideoChannelUsers?;
+    @jsondata:Name {value: "preferred_locale"}
     AvailableLocalesEnum preferredLocale;
+    @jsondata:Name {value: "default_message_notifications"}
     UserNotificationSettings defaultMessageNotifications;
+    @jsondata:Name {value: "owner_id"}
     string ownerId;
+    @jsondata:Name {value: "widget_channel_id"}
     anydata widgetChannelId?;
     GuildRoleResponse[] roles;
     string? icon?;
     string? description?;
+    @jsondata:Name {value: "system_channel_id"}
     anydata systemChannelId?;
+    @jsondata:Name {value: "rules_channel_id"}
     anydata rulesChannelId?;
+    @jsondata:Name {value: "afk_timeout"}
     AfkTimeouts afkTimeout;
     GuildFeatures[] features;
+    @jsondata:Name {value: "afk_channel_id"}
     anydata afkChannelId?;
-    ballerina/lang.int:0.0.0:Signed32? maxMembers?;
+    @jsondata:Name {value: "max_members"}
+    int:Signed32? maxMembers?;
     GuildStickerResponse[] stickers;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "widget_enabled"}
     boolean widgetEnabled;
-    ballerina/lang.int:0.0.0:Signed32? maxVideoChannelUsers?;
+    @jsondata:Name {value: "max_video_channel_users"}
+    int:Signed32? maxVideoChannelUsers?;
+    @jsondata:Name {value: "nsfw_level"}
     GuildNSFWContentLevel nsfwLevel;
+    @jsondata:Name {value: "safety_alerts_channel_id"}
     anydata safetyAlertsChannelId?;
     EmojiResponse[] emojis;
     boolean nsfw;
+    @jsondata:Name {value: "vanity_url_code"}
     string? vanityUrlCode?;
-    ballerina/lang.int:0.0.0:Signed32 systemChannelFlags;
-    ballerina/lang.int:0.0.0:Signed32? maxPresences?;
+    @jsondata:Name {value: "system_channel_flags"}
+    int:Signed32 systemChannelFlags;
+    @jsondata:Name {value: "max_presences"}
+    int:Signed32? maxPresences?;
+    @jsondata:Name {value: "premium_progress_bar_enabled"}
     boolean premiumProgressBarEnabled;
     string? banner?;
-    ballerina/lang.int:0.0.0:Signed32 premiumSubscriptionCount;
+    @jsondata:Name {value: "premium_subscription_count"}
+    int:Signed32 premiumSubscriptionCount;
+    @jsondata:Name {value: "public_updates_channel_id"}
     anydata publicUpdatesChannelId?;
+    @jsondata:Name {value: "application_id"}
     anydata applicationId?;
+    @jsondata:Name {value: "home_header"}
     string? homeHeader?;
+    @jsondata:Name {value: "verification_level"}
     VerificationLevels verificationLevel;
+    @jsondata:Name {value: "discovery_splash"}
     string? discoverySplash?;
+    @jsondata:Name {value: "explicit_content_filter"}
     GuildExplicitContentFilterTypes explicitContentFilter;
     string name;
+    @jsondata:Name {value: "mfa_level"}
     GuildMFALevel mfaLevel;
+    @jsondata:Name {value: "premium_tier"}
     PremiumGuildTiers premiumTier;
     string region;
     string? splash?;
 };
 
-// Unknown type: EXPLICIT
+type EXPLICIT 1;
 
-// Unknown type: SAFE
+type SAFE 2;
 
-// Unknown type: AGERESTRICTED
+type AGERESTRICTED 3;
 
-type GuildNSFWContentLevel ballerinax/discord:2.0.1:DEFAULT|ballerinax/discord:2.0.1:EXPLICIT|ballerinax/discord:2.0.1:SAFE|ballerinax/discord:2.0.1:AGERESTRICTED;
+type GuildNSFWContentLevel DEFAULT|EXPLICIT|SAFE|AGERESTRICTED;
 
 
 type BasicMessageResponse record {
+    @jsondata:Name {value: "mention_everyone"}
     boolean mentionEveryone;
     BasicMessageResponseComponents[] components;
     boolean pinned;
     MessageAttachmentResponse[] attachments;
     anydata activity?;
-    ballerina/lang.int:0.0.0:Signed32 flags;
+    int:Signed32 flags;
     MessageType 'type;
+    @jsondata:Name {value: "mention_roles"}
     BasicMessageResponseMentionrolesItemsString[] mentionRoles;
     string content;
+    @jsondata:Name {value: "edited_timestamp"}
     string? editedTimestamp?;
     BasicMessageResponseStickers[]|() stickers?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "message_reference"}
     anydata messageReference?;
+    @jsondata:Name {value: "sticker_items"}
     MessageStickerItemResponse[]|() stickerItems?;
     string timestamp;
     anydata resolved?;
+    @jsondata:Name {value: "role_subscription_data"}
     anydata roleSubscriptionData?;
     UserResponse author;
     anydata thread?;
+    @jsondata:Name {value: "application_id"}
     anydata applicationId?;
     anydata nonce?;
     anydata call?;
     boolean tts;
+    @jsondata:Name {value: "mention_channels"}
     BasicMessageResponseMentionChannels[]|() mentionChannels?;
     anydata application?;
+    @jsondata:Name {value: "webhook_id"}
     anydata webhookId?;
     UserResponse[] mentions;
+    @jsondata:Name {value: "purchase_notification"}
     anydata purchaseNotification?;
     anydata interaction?;
-    ballerina/lang.int:0.0.0:Signed32? position?;
+    int:Signed32? position?;
+    @jsondata:Name {value: "channel_id"}
     string channelId;
     MessageEmbedResponse[] embeds;
 };
@@ -4103,21 +5186,21 @@
 
 type MessageComponentActionRowResponse record {
     MessageComponentActionRowResponseComponents[]|() components?;
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
     1 'type;
 };
 
-type BasicMessageResponseComponents ballerinax/discord:2.0.1:MessageComponentActionRowResponse|ballerinax/discord:2.0.1:MessageComponentButtonResponse|ballerinax/discord:2.0.1:MessageComponentChannelSelectResponse|ballerinax/discord:2.0.1:MessageComponentInputTextResponse|ballerinax/discord:2.0.1:MessageComponentMentionableSelectResponse|ballerinax/discord:2.0.1:MessageComponentRoleSelectResponse|ballerinax/discord:2.0.1:MessageComponentStringSelectResponse|ballerinax/discord:2.0.1:MessageComponentUserSelectResponse;
+type BasicMessageResponseComponents MessageComponentActionRowResponse|MessageComponentButtonResponse|MessageComponentChannelSelectResponse|MessageComponentInputTextResponse|MessageComponentMentionableSelectResponse|MessageComponentRoleSelectResponse|MessageComponentStringSelectResponse|MessageComponentUserSelectResponse;
 
-// Unknown type: BasicMessageResponseMentionrolesItemsString
+type BasicMessageResponseMentionrolesItemsString string;
 
-type BasicMessageResponseStickers ballerinax/discord:2.0.1:GuildStickerResponse|ballerinax/discord:2.0.1:StandardStickerResponse|anydata|();
+type BasicMessageResponseStickers GuildStickerResponse|StandardStickerResponse|anydata|();
 
 
 type MessageEmbedResponse record {
     anydata image?;
     anydata thumbnail?;
-    ballerina/lang.int:0.0.0:Signed32? color?;
+    int:Signed32? color?;
     anydata footer?;
     anydata author?;
     string? description?;
@@ -4132,12 +5215,15 @@
 
 
 type GuildProductPurchaseResponse record {
+    @jsondata:Name {value: "listing_id"}
     string listingId;
+    @jsondata:Name {value: "product_name"}
     string productName;
 };
 
 
 type BlockMessageActionMetadata record {
+    @jsondata:Name {value: "custom_message"}
     string? customMessage?;
 };
 
@@ -4154,20 +5240,23 @@
     InviteChannelRecipientResponse[]|() recipients?;
     string? name?;
     string? icon?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
     ChannelTypes 'type;
 };
 
 
 type TeamResponse record {
+    @jsondata:Name {value: "owner_user_id"}
     string ownerUserId;
     TeamMemberResponse[] members;
     string? icon?;
     string name;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
 };
 
-// Unknown type: MessageResponseMentionrolesItemsString
+type MessageResponseMentionrolesItemsString string;
 
 
 type ApplicationCommandAutocompleteCallbackRequest record {
@@ -4180,14 +5269,16 @@
     InteractionApplicationCommandAutocompleteCallbackNumberDataChoices[]|() choices?;
 };
 
-type InteractionApplicationCommandAutocompleteCallbackNumberDataChoices ballerinax/discord:2.0.1:ApplicationCommandOptionNumberChoice|anydata|();
+type InteractionApplicationCommandAutocompleteCallbackNumberDataChoices ApplicationCommandOptionNumberChoice|anydata|();
 
-type InteractionTokenCallbackBody ballerinax/discord:2.0.1:ApplicationCommandAutocompleteCallbackRequest|ballerinax/discord:2.0.1:CreateMessageInteractionCallbackRequest|ballerinax/discord:2.0.1:ModalInteractionCallbackRequest|ballerinax/discord:2.0.1:PongInteractionCallbackRequest|ballerinax/discord:2.0.1:UpdateMessageInteractionCallbackRequest;
+type InteractionTokenCallbackBody ApplicationCommandAutocompleteCallbackRequest|CreateMessageInteractionCallbackRequest|ModalInteractionCallbackRequest|PongInteractionCallbackRequest|UpdateMessageInteractionCallbackRequest;
 
 
 type GuildsPruneRequest record {
+    @jsondata:Name {value: "compute_prune_count"}
     boolean? computePruneCount?;
-    ballerina/lang.int:0.0.0:Signed32? days?;
+    int:Signed32? days?;
+    @jsondata:Name {value: "include_roles"}
     anydata includeRoles?;
 };
 
@@ -4196,6 +5287,7 @@
 
 type UpdateGuildOnboardingRequest record {
     anydata mode?;
+    @jsondata:Name {value: "default_channel_ids"}
     UpdateGuildOnboardingRequestDefaultchannelidsItemsString[]|() defaultChannelIds?;
     UpdateOnboardingPromptRequest[]|() prompts?;
     boolean? enabled?;
@@ -4203,31 +5295,36 @@
 
 
 type RichEmbedThumbnail record {
-    ballerina/lang.int:0.0.0:Signed32? width?;
-    ballerina/lang.int:0.0.0:Signed32? placeholderVersion?;
+    int:Signed32? width?;
+    @jsondata:Name {value: "placeholder_version"}
+    int:Signed32? placeholderVersion?;
     string? placeholder?;
     string? url?;
-    ballerina/lang.int:0.0.0:Signed32? height?;
+    int:Signed32? height?;
 };
 
 
 type ChannelsPermissionsRequest record {
-    ballerina/lang.int:0.0.0:Signed32? allow?;
-    ballerina/lang.int:0.0.0:Signed32? deny?;
+    int:Signed32? allow?;
+    int:Signed32? deny?;
     anydata 'type?;
 };
 
 # Represents the Queries record for the operation: invite_resolve
 
 type InviteResolveQueries record {
+    @http:Query {name: "with_counts"}
     boolean withCounts?;
+    @http:Query {name: "guild_scheduled_event_id"}
     string guildScheduledEventId?;
 };
 
 
 type InviteStageInstanceResponse record {
-    ballerina/lang.int:0.0.0:Signed32? speakerCount?;
-    ballerina/lang.int:0.0.0:Signed32? participantCount?;
+    @jsondata:Name {value: "speaker_count"}
+    int:Signed32? speakerCount?;
+    @jsondata:Name {value: "participant_count"}
+    int:Signed32? participantCount?;
     GuildMemberResponse[]|() members?;
     string topic;
 };
@@ -4240,62 +5337,92 @@
 
 type StickersOneOf31 anydata|();
 
-type MessageResponseStickers ballerinax/discord:2.0.1:GuildStickerResponse|ballerinax/discord:2.0.1:StandardStickerResponse|anydata|();
+type MessageResponseStickers GuildStickerResponse|StandardStickerResponse|anydata|();
 
-type ApplicationCommandPatchRequestPartialOptions ballerinax/discord:2.0.1:ApplicationCommandAttachmentOption|ballerinax/discord:2.0.1:ApplicationCommandBooleanOption|ballerinax/discord:2.0.1:ApplicationCommandChannelOption|ballerinax/discord:2.0.1:ApplicationCommandIntegerOption|ballerinax/discord:2.0.1:ApplicationCommandMentionableOption|ballerinax/discord:2.0.1:ApplicationCommandNumberOption|ballerinax/discord:2.0.1:ApplicationCommandRoleOption|ballerinax/discord:2.0.1:ApplicationCommandStringOption|ballerinax/discord:2.0.1:ApplicationCommandSubcommandGroupOption|ballerinax/discord:2.0.1:ApplicationCommandSubcommandOption|ballerinax/discord:2.0.1:ApplicationCommandUserOption|anydata|();
+type ApplicationCommandPatchRequestPartialOptions ApplicationCommandAttachmentOption|ApplicationCommandBooleanOption|ApplicationCommandChannelOption|ApplicationCommandIntegerOption|ApplicationCommandMentionableOption|ApplicationCommandNumberOption|ApplicationCommandRoleOption|ApplicationCommandStringOption|ApplicationCommandSubcommandGroupOption|ApplicationCommandSubcommandOption|ApplicationCommandUserOption|anydata|();
 
-// Unknown type: ApplicationFormPartialTagsItemsString
+@constraint:String {maxLength: 20}
+type ApplicationFormPartialTagsItemsString string;
 
 # Represents the Queries record for the operation: list_my_guilds
 
 type ListMyGuildsQueries record {
+    @http:Query {name: "with_counts"}
     boolean withCounts?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string before?;
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    @constraint:Int {minValue: 1, maxValue: 200}
+    int:Signed32 'limit?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string after?;
 };
 
 
 type EntitlementResponse record {
+    @jsondata:Name {value: "fulfilled_at"}
     string? fulfilledAt?;
     boolean? consumed?;
+    @jsondata:Name {value: "starts_at"}
     string? startsAt?;
     boolean deleted;
+    @jsondata:Name {value: "fulfillment_status"}
     anydata fulfillmentStatus?;
+    @jsondata:Name {value: "user_id"}
     string userId;
+    @jsondata:Name {value: "guild_id"}
     anydata guildId?;
+    @jsondata:Name {value: "sku_id"}
     string skuId;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "ends_at"}
     string? endsAt?;
     EntitlementTypes 'type;
+    @jsondata:Name {value: "application_id"}
     string applicationId;
 };
 
-type EntitlementTypes ballerinax/discord:2.0.1:APPLICATIONSUBSCRIPTION|ballerinax/discord:2.0.1:QUESTREWARD;
+type EntitlementTypes APPLICATIONSUBSCRIPTION|QUESTREWARD;
 
 
 type GuildPatchRequestPartial record {
+    @jsondata:Name {value: "preferred_locale"}
     anydata preferredLocale?;
+    @jsondata:Name {value: "default_message_notifications"}
     anydata defaultMessageNotifications?;
+    @jsondata:Name {value: "owner_id"}
     string ownerId?;
-    ballerina/lang.int:0.0.0:Signed32? systemChannelFlags?;
+    @jsondata:Name {value: "system_channel_flags"}
+    int:Signed32? systemChannelFlags?;
+    @jsondata:Name {value: "premium_progress_bar_enabled"}
     boolean? premiumProgressBarEnabled?;
     record {|byte[] fileContent; string fileName; anydata...;|}? icon?;
     string? description?;
+    @jsondata:Name {value: "system_channel_id"}
     anydata systemChannelId?;
     record {|byte[] fileContent; string fileName; anydata...;|}? banner?;
+    @jsondata:Name {value: "rules_channel_id"}
     anydata rulesChannelId?;
+    @jsondata:Name {value: "afk_timeout"}
     anydata afkTimeout?;
+    @jsondata:Name {value: "public_updates_channel_id"}
     anydata publicUpdatesChannelId?;
     GuildPatchRequestPartialFeaturesItemsString[]|() features?;
+    @jsondata:Name {value: "home_header"}
     record {|byte[] fileContent; string fileName; anydata...;|}? homeHeader?;
+    @jsondata:Name {value: "verification_level"}
     anydata verificationLevel?;
+    @jsondata:Name {value: "explicit_content_filter"}
     anydata explicitContentFilter?;
+    @jsondata:Name {value: "discovery_splash"}
     record {|byte[] fileContent; string fileName; anydata...;|}? discoverySplash?;
+    @jsondata:Name {value: "afk_channel_id"}
     anydata afkChannelId?;
+    @constraint:String {maxLength: 100, minLength: 2}
     string name?;
     string? region?;
     record {|byte[] fileContent; string fileName; anydata...;|}? splash?;
+    @jsondata:Name {value: "safety_alerts_channel_id"}
     anydata safetyAlertsChannelId?;
 };
 
@@ -4311,13 +5438,18 @@
 
 
 type ApplicationCommandPatchRequestPartial record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
+    @jsondata:Name {value: "dm_permission"}
     boolean? dmPermission?;
+    @constraint:String {maxLength: 32, minLength: 1}
     string name?;
     ApplicationCommandPatchRequestPartialOptions[]|() options?;
     string? description?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
-    ballerina/lang.int:0.0.0:Signed32? defaultMemberPermissions?;
+    @jsondata:Name {value: "default_member_permissions"}
+    int:Signed32? defaultMemberPermissions?;
 };
 
 
@@ -4329,27 +5461,32 @@
 type ThreadsResponse record {
     ThreadMemberResponse[] members;
     ThreadResponse[] threads;
+    @jsondata:Name {value: "has_more"}
     boolean? hasMore?;
 };
 
 
 type ThreadMemberResponse record {
+    @jsondata:Name {value: "join_timestamp"}
     string joinTimestamp;
+    @jsondata:Name {value: "user_id"}
     string userId;
-    ballerina/lang.int:0.0.0:Signed32 flags;
+    int:Signed32 flags;
     anydata member?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
 };
 
-type InlineResponse200 ballerinax/discord:2.0.1:PrivateChannelResponse|ballerinax/discord:2.0.1:PrivateGroupChannelResponse;
+type InlineResponse200 PrivateChannelResponse|PrivateGroupChannelResponse;
 
 
 type RichEmbedVideo record {
-    ballerina/lang.int:0.0.0:Signed32? width?;
-    ballerina/lang.int:0.0.0:Signed32? placeholderVersion?;
+    int:Signed32? width?;
+    @jsondata:Name {value: "placeholder_version"}
+    int:Signed32? placeholderVersion?;
     string? placeholder?;
     string? url?;
-    ballerina/lang.int:0.0.0:Signed32? height?;
+    int:Signed32? height?;
 };
 
 
@@ -4357,8 +5494,11 @@
     WidgetChannel[] channels;
     WidgetMember[] members;
     string name;
-    ballerina/lang.int:0.0.0:Signed32 presenceCount;
+    @jsondata:Name {value: "presence_count"}
+    int:Signed32 presenceCount;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "instant_invite"}
     string? instantInvite?;
 };
 
@@ -4369,17 +5509,23 @@
 
 
 type MLSpamUpsertRequestPartial record {
+    @jsondata:Name {value: "event_type"}
     AutomodEventType eventType?;
+    @jsondata:Name {value: "trigger_type"}
     AutomodTriggerType triggerType?;
+    @constraint:String {maxLength: 100}
     string name?;
+    @jsondata:Name {value: "exempt_roles"}
     MLSpamUpsertRequestPartialExemptrolesItemsString[]|() exemptRoles?;
+    @jsondata:Name {value: "exempt_channels"}
     MLSpamUpsertRequestPartialExemptchannelsItemsString[]|() exemptChannels?;
     MLSpamUpsertRequestPartialActions[]|() actions?;
     boolean? enabled?;
+    @jsondata:Name {value: "trigger_metadata"}
     anydata triggerMetadata?;
 };
 
-type MLSpamUpsertRequestPartialActions ballerinax/discord:2.0.1:BlockMessageAction|ballerinax/discord:2.0.1:FlagToChannelAction|ballerinax/discord:2.0.1:QuarantineUserAction|ballerinax/discord:2.0.1:UserCommunicationDisabledAction|anydata|();
+type MLSpamUpsertRequestPartialActions BlockMessageAction|FlagToChannelAction|QuarantineUserAction|UserCommunicationDisabledAction|anydata|();
 
 
 type ExternalConnectionIntegrationResponse record {
@@ -4387,58 +5533,94 @@
     IntegrationTypes 'type;
     boolean? revoked?;
     boolean? enabled?;
+    @jsondata:Name {value: "expire_behavior"}
     anydata expireBehavior?;
+    @jsondata:Name {value: "expire_grace_period"}
     anydata expireGracePeriod?;
+    @jsondata:Name {value: "role_id"}
     anydata roleId?;
-    ballerina/lang.int:0.0.0:Signed32? subscriberCount?;
+    @jsondata:Name {value: "subscriber_count"}
+    int:Signed32? subscriberCount?;
     string? name?;
     string id;
     UserResponse user;
     anydata account?;
+    @jsondata:Name {value: "enable_emoticons"}
     boolean? enableEmoticons?;
+    @jsondata:Name {value: "synced_at"}
     string? syncedAt?;
 };
 
 
 type GuildWithCountsResponse record {
-    ballerina/lang.int:0.0.0:Signed32? maxStageVideoChannelUsers?;
+    @jsondata:Name {value: "max_stage_video_channel_users"}
+    int:Signed32? maxStageVideoChannelUsers?;
+    @jsondata:Name {value: "preferred_locale"}
     AvailableLocalesEnum preferredLocale;
-    ballerina/lang.int:0.0.0:Signed32? approximatePresenceCount?;
+    @jsondata:Name {value: "approximate_presence_count"}
+    int:Signed32? approximatePresenceCount?;
+    @jsondata:Name {value: "default_message_notifications"}
     UserNotificationSettings defaultMessageNotifications;
+    @jsondata:Name {value: "owner_id"}
     string ownerId;
+    @jsondata:Name {value: "widget_channel_id"}
     anydata widgetChannelId?;
     GuildRoleResponse[] roles;
     string? icon?;
     string? description?;
+    @jsondata:Name {value: "system_channel_id"}
     anydata systemChannelId?;
+    @jsondata:Name {value: "rules_channel_id"}
     anydata rulesChannelId?;
+    @jsondata:Name {value: "afk_timeout"}
     AfkTimeouts afkTimeout;
     GuildFeatures[] features;
+    @jsondata:Name {value: "afk_channel_id"}
     anydata afkChannelId?;
-    ballerina/lang.int:0.0.0:Signed32? approximateMemberCount?;
-    ballerina/lang.int:0.0.0:Signed32? maxMembers?;
+    @jsondata:Name {value: "approximate_member_count"}
+    int:Signed32? approximateMemberCount?;
+    @jsondata:Name {value: "max_members"}
+    int:Signed32? maxMembers?;
     GuildStickerResponse[] stickers;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "widget_enabled"}
     boolean widgetEnabled;
-    ballerina/lang.int:0.0.0:Signed32? maxVideoChannelUsers?;
+    @jsondata:Name {value: "max_video_channel_users"}
+    int:Signed32? maxVideoChannelUsers?;
+    @jsondata:Name {value: "nsfw_level"}
     GuildNSFWContentLevel nsfwLevel;
+    @jsondata:Name {value: "safety_alerts_channel_id"}
     anydata safetyAlertsChannelId?;
     EmojiResponse[] emojis;
     boolean nsfw;
+    @jsondata:Name {value: "vanity_url_code"}
     string? vanityUrlCode?;
-    ballerina/lang.int:0.0.0:Signed32 systemChannelFlags;
-    ballerina/lang.int:0.0.0:Signed32? maxPresences?;
+    @jsondata:Name {value: "system_channel_flags"}
+    int:Signed32 systemChannelFlags;
+    @jsondata:Name {value: "max_presences"}
+    int:Signed32? maxPresences?;
+    @jsondata:Name {value: "premium_progress_bar_enabled"}
     boolean premiumProgressBarEnabled;
     string? banner?;
-    ballerina/lang.int:0.0.0:Signed32 premiumSubscriptionCount;
+    @jsondata:Name {value: "premium_subscription_count"}
+    int:Signed32 premiumSubscriptionCount;
+    @jsondata:Name {value: "public_updates_channel_id"}
     anydata publicUpdatesChannelId?;
+    @jsondata:Name {value: "application_id"}
     anydata applicationId?;
+    @jsondata:Name {value: "home_header"}
     string? homeHeader?;
+    @jsondata:Name {value: "verification_level"}
     VerificationLevels verificationLevel;
+    @jsondata:Name {value: "discovery_splash"}
     string? discoverySplash?;
+    @jsondata:Name {value: "explicit_content_filter"}
     GuildExplicitContentFilterTypes explicitContentFilter;
     string name;
+    @jsondata:Name {value: "mfa_level"}
     GuildMFALevel mfaLevel;
+    @jsondata:Name {value: "premium_tier"}
     PremiumGuildTiers premiumTier;
     string region;
     string? splash?;
@@ -4456,11 +5638,13 @@
 # Represents the Queries record for the operation: get_thread_member
 
 type GetThreadMemberQueries record {
+    @http:Query {name: "with_member"}
     boolean withMember?;
 };
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint.
     OAuth2ClientCredentialsGrantConfig|http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -4507,113 +5691,149 @@
 
 type ApiKeysConfig record {
     # Discord bot token
+    @display {label: "", kind: "password"}
     string authorization;
 };
 
 
 type RichEmbedImage record {
-    ballerina/lang.int:0.0.0:Signed32? width?;
-    ballerina/lang.int:0.0.0:Signed32? placeholderVersion?;
+    int:Signed32? width?;
+    @jsondata:Name {value: "placeholder_version"}
+    int:Signed32? placeholderVersion?;
     string? placeholder?;
     string? url?;
-    ballerina/lang.int:0.0.0:Signed32? height?;
+    int:Signed32? height?;
 };
 
 # Represents the Queries record for the operation: get_entitlements
 
 type GetEntitlementsQueries record {
+    @http:Query {name: "exclude_ended"}
     boolean excludeEnded?;
+    @http:Query {name: "user_id"}
     string userId?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string before?;
+    @http:Query {name: "sku_ids"}
     SkuIds skuIds;
+    @http:Query {name: "guild_id"}
     string guildId?;
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    @constraint:Int {minValue: 1, maxValue: 100}
+    int:Signed32 'limit?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string after?;
+    @http:Query {name: "only_active"}
     boolean onlyActive?;
 };
 
-// Unknown type: SkuIdsOneOf1
+type SkuIdsOneOf1 string;
 
-type SkuIds ballerinax/discord:2.0.1:SkuIdsOneOf1|ballerinax/discord:2.0.1:SkuIdsSkuIdsOneOf12;
+type SkuIds SkuIdsOneOf1|SkuIdsSkuIdsOneOf12;
 
-// Unknown type: CreatedThreadResponseAppliedtagsItemsString
+type CreatedThreadResponseAppliedtagsItemsString string;
 
 
 type UpdateDefaultReactionEmojiRequest record {
+    @jsondata:Name {value: "emoji_id"}
     anydata emojiId?;
+    @jsondata:Name {value: "emoji_name"}
     string? emojiName?;
 };
 
 
 type MessageReferenceResponse record {
+    @jsondata:Name {value: "guild_id"}
     anydata guildId?;
+    @jsondata:Name {value: "message_id"}
     anydata messageId?;
     anydata 'type?;
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
 
 type DefaultKeywordListUpsertRequestPartial record {
+    @jsondata:Name {value: "event_type"}
     AutomodEventType eventType?;
+    @jsondata:Name {value: "trigger_type"}
     AutomodTriggerType triggerType?;
+    @constraint:String {maxLength: 100}
     string name?;
+    @jsondata:Name {value: "exempt_roles"}
     DefaultKeywordListUpsertRequestPartialExemptrolesItemsString[]|() exemptRoles?;
+    @jsondata:Name {value: "exempt_channels"}
     DefaultKeywordListUpsertRequestPartialExemptchannelsItemsString[]|() exemptChannels?;
     DefaultKeywordListUpsertRequestPartialActions[]|() actions?;
     boolean? enabled?;
+    @jsondata:Name {value: "trigger_metadata"}
     DefaultKeywordListTriggerMetadata triggerMetadata?;
 };
 
-type DefaultKeywordListUpsertRequestPartialActions ballerinax/discord:2.0.1:BlockMessageAction|ballerinax/discord:2.0.1:FlagToChannelAction|ballerinax/discord:2.0.1:QuarantineUserAction|ballerinax/discord:2.0.1:UserCommunicationDisabledAction|anydata|();
+type DefaultKeywordListUpsertRequestPartialActions BlockMessageAction|FlagToChannelAction|QuarantineUserAction|UserCommunicationDisabledAction|anydata|();
 
-type RulesruleIdBody ballerinax/discord:2.0.1:DefaultKeywordListUpsertRequestPartial|ballerinax/discord:2.0.1:KeywordUpsertRequestPartial|ballerinax/discord:2.0.1:MLSpamUpsertRequestPartial|ballerinax/discord:2.0.1:MentionSpamUpsertRequestPartial;
+type RulesruleIdBody DefaultKeywordListUpsertRequestPartial|KeywordUpsertRequestPartial|MLSpamUpsertRequestPartial|MentionSpamUpsertRequestPartial;
 
 # Represents the Queries record for the operation: delete_webhook_message
 
 type DeleteWebhookMessageQueries record {
+    @http:Query {name: "thread_id"}
     string threadId?;
 };
 
 
 type DefaultReactionEmojiResponse record {
+    @jsondata:Name {value: "emoji_id"}
     anydata emojiId?;
+    @jsondata:Name {value: "emoji_name"}
     string? emojiName?;
 };
 
 
 type ApplicationCommandUpdateRequest record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
+    @jsondata:Name {value: "dm_permission"}
     boolean? dmPermission?;
+    @constraint:String {maxLength: 32, minLength: 1}
     string name;
     ApplicationCommandUpdateRequestOptions[]|() options?;
     string? description?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
-    ballerina/lang.int:0.0.0:Signed32? defaultMemberPermissions?;
+    @jsondata:Name {value: "default_member_permissions"}
+    int:Signed32? defaultMemberPermissions?;
     anydata id?;
     anydata 'type?;
 };
 
 
 type StickerPackResponse record {
+    @jsondata:Name {value: "banner_asset_id"}
     anydata bannerAssetId?;
+    @jsondata:Name {value: "cover_sticker_id"}
     anydata coverStickerId?;
     string name;
     string? description?;
+    @jsondata:Name {value: "sku_id"}
     string skuId;
     StandardStickerResponse[] stickers;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
 };
 
 
 type GuildsVoiceStatesRequest record {
     boolean? suppress?;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
 };
 
 
 type MessageEmbedImageResponse record {
     anydata width?;
+    @jsondata:Name {value: "placeholder_version"}
     anydata placeholderVersion?;
+    @jsondata:Name {value: "proxy_url"}
     string? proxyUrl?;
     string? placeholder?;
     string? url?;
@@ -4622,38 +5842,51 @@
 
 
 type MessageResponse record {
+    @jsondata:Name {value: "mention_everyone"}
     boolean mentionEveryone;
     BasicMessageResponseComponents[] components;
     boolean pinned;
     MessageAttachmentResponse[] attachments;
     anydata activity?;
-    ballerina/lang.int:0.0.0:Signed32 flags;
+    int:Signed32 flags;
     MessageType 'type;
+    @jsondata:Name {value: "mention_roles"}
     MessageResponseMentionrolesItemsString[] mentionRoles;
     string content;
+    @jsondata:Name {value: "edited_timestamp"}
     string? editedTimestamp?;
+    @jsondata:Name {value: "referenced_message"}
     anydata referencedMessage?;
     MessageResponseStickers[]|() stickers?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "message_reference"}
     anydata messageReference?;
+    @jsondata:Name {value: "sticker_items"}
     MessageStickerItemResponse[]|() stickerItems?;
     string timestamp;
     anydata resolved?;
+    @jsondata:Name {value: "role_subscription_data"}
     anydata roleSubscriptionData?;
     UserResponse author;
     anydata thread?;
+    @jsondata:Name {value: "application_id"}
     anydata applicationId?;
     anydata nonce?;
     anydata call?;
     boolean tts;
+    @jsondata:Name {value: "mention_channels"}
     MessageResponseMentionChannels[]|() mentionChannels?;
     anydata application?;
+    @jsondata:Name {value: "webhook_id"}
     anydata webhookId?;
     UserResponse[] mentions;
+    @jsondata:Name {value: "purchase_notification"}
     anydata purchaseNotification?;
     anydata interaction?;
     MessageReactionResponse[]|() reactions?;
-    ballerina/lang.int:0.0.0:Signed32? position?;
+    int:Signed32? position?;
+    @jsondata:Name {value: "channel_id"}
     string channelId;
     MessageEmbedResponse[] embeds;
 };
@@ -4666,83 +5899,105 @@
 
 
 type ChannelFollowerResponse record {
+    @jsondata:Name {value: "webhook_id"}
     string webhookId;
+    @jsondata:Name {value: "channel_id"}
     string channelId;
 };
 
-type InlineResponseItems2008 ballerinax/discord:2.0.1:FriendInviteResponse|ballerinax/discord:2.0.1:GroupDMInviteResponse|ballerinax/discord:2.0.1:GuildInviteResponse|anydata|();
+type InlineResponseItems2008 FriendInviteResponse|GroupDMInviteResponse|GuildInviteResponse|anydata|();
 
 type 200OneOf43 anydata|();
 
-type InlineResponseItems2006 ballerinax/discord:2.0.1:ApplicationIncomingWebhookResponse|ballerinax/discord:2.0.1:ChannelFollowerWebhookResponse|ballerinax/discord:2.0.1:GuildIncomingWebhookResponse|anydata|();
+type InlineResponseItems2006 ApplicationIncomingWebhookResponse|ChannelFollowerWebhookResponse|GuildIncomingWebhookResponse|anydata|();
 
 type 200OneOf5 anydata|();
 
-type InlineResponseItems2007 ballerinax/discord:2.0.1:GuildChannelResponse|ballerinax/discord:2.0.1:PrivateChannelResponse|ballerinax/discord:2.0.1:PrivateGroupChannelResponse|ballerinax/discord:2.0.1:ThreadResponse|anydata|();
+type InlineResponseItems2007 GuildChannelResponse|PrivateChannelResponse|PrivateGroupChannelResponse|ThreadResponse|anydata|();
 
 type 200OneOf41 anydata|();
 
-type InlineResponseItems2004 ballerinax/discord:2.0.1:ExternalScheduledEventResponse|ballerinax/discord:2.0.1:StageScheduledEventResponse|ballerinax/discord:2.0.1:VoiceScheduledEventResponse|anydata|();
+type InlineResponseItems2004 ExternalScheduledEventResponse|StageScheduledEventResponse|VoiceScheduledEventResponse|anydata|();
 
 
 type GatewayBotResponse record {
-    ballerina/lang.int:0.0.0:Signed32 shards;
+    int:Signed32 shards;
+    @jsondata:Name {value: "session_start_limit"}
     GatewayBotSessionStartLimitResponse sessionStartLimit;
     string url;
 };
 
 type 200OneOf42 anydata|();
 
-type InlineResponseItems2005 ballerinax/discord:2.0.1:DiscordIntegrationResponse|ballerinax/discord:2.0.1:ExternalConnectionIntegrationResponse|ballerinax/discord:2.0.1:GuildSubscriptionIntegrationResponse|anydata|();
+type InlineResponseItems2005 DiscordIntegrationResponse|ExternalConnectionIntegrationResponse|GuildSubscriptionIntegrationResponse|anydata|();
 
 
 type MessageEmbedAuthorResponse record {
+    @jsondata:Name {value: "icon_url"}
     string? iconUrl?;
     string name;
+    @jsondata:Name {value: "proxy_icon_url"}
     string? proxyIconUrl?;
     string? url?;
 };
 
 type 200OneOf4 anydata|();
 
-type InlineResponseItems2002 ballerinax/discord:2.0.1:ApplicationIncomingWebhookResponse|ballerinax/discord:2.0.1:ChannelFollowerWebhookResponse|ballerinax/discord:2.0.1:GuildIncomingWebhookResponse|anydata|();
+type InlineResponseItems2002 ApplicationIncomingWebhookResponse|ChannelFollowerWebhookResponse|GuildIncomingWebhookResponse|anydata|();
 
-type InlineResponseItems2003 ballerinax/discord:2.0.1:FriendInviteResponse|ballerinax/discord:2.0.1:GroupDMInviteResponse|ballerinax/discord:2.0.1:GuildInviteResponse|anydata|();
+type InlineResponseItems2003 FriendInviteResponse|GroupDMInviteResponse|GuildInviteResponse|anydata|();
 
 # Represents the Queries record for the operation: list_guild_scheduled_events
 
 type ListGuildScheduledEventsQueries record {
+    @http:Query {name: "with_user_count"}
     boolean withUserCount?;
 };
 
 
 type InlineResponseItems2001 record {
+    @jsondata:Name {value: "fulfilled_at"}
     string? fulfilledAt?;
     boolean? consumed?;
+    @jsondata:Name {value: "starts_at"}
     string? startsAt?;
     boolean deleted;
+    @jsondata:Name {value: "fulfillment_status"}
     anydata fulfillmentStatus?;
+    @jsondata:Name {value: "user_id"}
     string userId;
+    @jsondata:Name {value: "guild_id"}
     anydata guildId?;
+    @jsondata:Name {value: "sku_id"}
     string skuId;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "ends_at"}
     string? endsAt?;
     EntitlementTypes 'type;
+    @jsondata:Name {value: "application_id"}
     string applicationId;
 };
 
 
 type GuildTemplateResponse record {
-    ballerina/lang.int:0.0.0:Signed32 usageCount;
+    @jsondata:Name {value: "usage_count"}
+    int:Signed32 usageCount;
     anydata creator?;
     string code;
+    @jsondata:Name {value: "source_guild_id"}
     string sourceGuildId;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt;
+    @jsondata:Name {value: "serialized_source_guild"}
     GuildTemplateSnapshotResponse serializedSourceGuild;
     string name;
+    @jsondata:Name {value: "creator_id"}
     string creatorId;
     string? description?;
+    @jsondata:Name {value: "created_at"}
     string createdAt;
+    @jsondata:Name {value: "is_dirty"}
     boolean? isDirty?;
 };
 
@@ -4750,76 +6005,117 @@
 type ScheduledEventResponse record {
     string? image?;
     anydata creator?;
+    @jsondata:Name {value: "privacy_level"}
     GuildScheduledEventPrivacyLevels privacyLevel;
     string? description?;
+    @jsondata:Name {value: "entity_id"}
     anydata entityId?;
+    @jsondata:Name {value: "scheduled_end_time"}
     string? scheduledEndTime?;
+    @jsondata:Name {value: "entity_type"}
     GuildScheduledEventEntityTypes entityType;
+    @jsondata:Name {value: "user_rsvp"}
     anydata userRsvp?;
-    ballerina/lang.int:0.0.0:Signed32? userCount?;
+    @jsondata:Name {value: "user_count"}
+    int:Signed32? userCount?;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
     string name;
+    @jsondata:Name {value: "creator_id"}
     anydata creatorId?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "channel_id"}
     anydata channelId?;
+    @jsondata:Name {value: "scheduled_start_time"}
     string scheduledStartTime;
     GuildScheduledEventStatuses status;
 };
 
 
 type InviteApplicationResponse record {
+    @jsondata:Name {value: "rpc_origins"}
     string[]? rpcOrigins?;
+    @jsondata:Name {value: "privacy_policy_url"}
     string? privacyPolicyUrl?;
+    @jsondata:Name {value: "bot_require_code_grant"}
     boolean? botRequireCodeGrant?;
     anydata bot?;
     string? icon?;
-    ballerina/lang.int:0.0.0:Signed32 flags;
+    int:Signed32 flags;
     string description;
+    @jsondata:Name {value: "verify_key"}
     string verifyKey;
     anydata 'type?;
-    ballerina/lang.int:0.0.0:Signed32? maxParticipants?;
+    @jsondata:Name {value: "max_participants"}
+    int:Signed32? maxParticipants?;
     string[]? tags?;
+    @jsondata:Name {value: "custom_install_url"}
     string? customInstallUrl?;
+    @jsondata:Name {value: "install_params"}
     anydata installParams?;
     string name;
+    @jsondata:Name {value: "guild_id"}
     anydata guildId?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "cover_image"}
     string? coverImage?;
+    @jsondata:Name {value: "primary_sku_id"}
     anydata primarySkuId?;
     string? slug?;
+    @jsondata:Name {value: "bot_public"}
     boolean? botPublic?;
+    @jsondata:Name {value: "terms_of_service_url"}
     string? termsOfServiceUrl?;
 };
 
 
 type CreatedThreadResponse record {
+    @jsondata:Name {value: "last_pin_timestamp"}
     string? lastPinTimestamp?;
-    ballerina/lang.int:0.0.0:Signed32? rateLimitPerUser?;
+    @jsondata:Name {value: "rate_limit_per_user"}
+    int:Signed32? rateLimitPerUser?;
+    @jsondata:Name {value: "owner_id"}
     string ownerId;
-    ballerina/lang.int:0.0.0:Signed32 flags;
-    ballerina/lang.int:0.0.0:Signed32? bitrate?;
+    int:Signed32 flags;
+    int:Signed32? bitrate?;
     ChannelTypes 'type;
-    ballerina/lang.int:0.0.0:Signed32? userLimit?;
-    ballerina/lang.int:0.0.0:Signed32 messageCount;
-    ballerina/lang.int:0.0.0:Signed32 totalMessageSent;
+    @jsondata:Name {value: "user_limit"}
+    int:Signed32? userLimit?;
+    @jsondata:Name {value: "message_count"}
+    int:Signed32 messageCount;
+    @jsondata:Name {value: "total_message_sent"}
+    int:Signed32 totalMessageSent;
+    @jsondata:Name {value: "last_message_id"}
     anydata lastMessageId?;
+    @jsondata:Name {value: "rtc_region"}
     string? rtcRegion?;
+    @jsondata:Name {value: "parent_id"}
     anydata parentId?;
     string? permissions?;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
     string name;
     anydata member?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "thread_metadata"}
     anydata threadMetadata?;
-    ballerina/lang.int:0.0.0:Signed32 memberCount;
+    @jsondata:Name {value: "member_count"}
+    int:Signed32 memberCount;
+    @jsondata:Name {value: "video_quality_mode"}
     anydata videoQualityMode?;
+    @jsondata:Name {value: "applied_tags"}
     CreatedThreadResponseAppliedtagsItemsString[]|() appliedTags?;
 };
 
 
 type MessageEmbedVideoResponse record {
     anydata width?;
+    @jsondata:Name {value: "placeholder_version"}
     anydata placeholderVersion?;
+    @jsondata:Name {value: "proxy_url"}
     string? proxyUrl?;
     string? placeholder?;
     string? url?;
@@ -4828,25 +6124,29 @@
 
 
 type ScheduledEventUserResponse record {
+    @jsondata:Name {value: "user_id"}
     string userId;
     anydata member?;
+    @jsondata:Name {value: "guild_scheduled_event_id"}
     string guildScheduledEventId;
     anydata user?;
 };
 
 
 type ChannelsFollowersRequest record {
+    @jsondata:Name {value: "webhook_channel_id"}
     string webhookChannelId;
 };
 
 
 type VanityURLErrorResponse record {
-    ballerina/lang.int:0.0.0:Signed32 code;
+    int:Signed32 code;
     string message;
 };
 
 
 type ChannelsRecipientsRequest record {
+    @jsondata:Name {value: "access_token"}
     string? accessToken?;
     string? nick?;
 };
@@ -4855,7 +6155,8 @@
 type MessagesmessageIdBody1 record {
     ActionRow[]|() components?;
     MessageAttachmentRequest[]|() attachments?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
+    @jsondata:Name {value: "allowed_mentions"}
     anydata allowedMentions?;
     RichEmbed[]|() embeds?;
     string? content?;
@@ -4863,112 +6164,156 @@
 
 
 type ApplicationFormPartial record {
+    @jsondata:Name {value: "role_connections_verification_url"}
     string? roleConnectionsVerificationUrl?;
+    @jsondata:Name {value: "custom_install_url"}
     string? customInstallUrl?;
+    @jsondata:Name {value: "install_params"}
     anydata installParams?;
     record {|byte[] fileContent; string fileName; anydata...;|}? icon?;
-    ballerina/lang.int:0.0.0:Signed32? flags?;
+    int:Signed32? flags?;
     anydata description?;
+    @jsondata:Name {value: "interactions_endpoint_url"}
     string? interactionsEndpointUrl?;
+    @jsondata:Name {value: "cover_image"}
     record {|byte[] fileContent; string fileName; anydata...;|}? coverImage?;
+    @jsondata:Name {value: "team_id"}
     anydata teamId?;
     anydata 'type?;
-    ballerina/lang.int:0.0.0:Signed32? maxParticipants?;
+    @jsondata:Name {value: "max_participants"}
+    int:Signed32? maxParticipants?;
     ApplicationFormPartialTagsItemsString[]|() tags?;
 };
 
 
 type PrivateGuildMemberResponse record {
+    @jsondata:Name {value: "premium_since"}
     string? premiumSince?;
     boolean pending;
     PrivateGuildMemberResponseRolesItemsString[] roles;
-    ballerina/lang.int:0.0.0:Signed32 flags;
+    int:Signed32 flags;
     boolean deaf;
     string? banner?;
     boolean mute;
     string? avatar?;
+    @jsondata:Name {value: "joined_at"}
     string joinedAt;
     string? nick?;
+    @jsondata:Name {value: "communication_disabled_until"}
     string? communicationDisabledUntil?;
+    @jsondata:Name {value: "avatar_decoration_data"}
     anydata avatarDecorationData?;
     UserResponse user;
 };
 
 
 type ApplicationCommandCreateRequest record {
+    @jsondata:Name {value: "name_localizations"}
     record {|string...;|}? nameLocalizations?;
+    @jsondata:Name {value: "dm_permission"}
     boolean? dmPermission?;
+    @constraint:String {maxLength: 32, minLength: 1}
     string name;
     ApplicationCommandCreateRequestOptions[]|() options?;
     string? description?;
+    @jsondata:Name {value: "description_localizations"}
     record {|string...;|}? descriptionLocalizations?;
-    ballerina/lang.int:0.0.0:Signed32? defaultMemberPermissions?;
+    @jsondata:Name {value: "default_member_permissions"}
+    int:Signed32? defaultMemberPermissions?;
     anydata 'type?;
 };
 
 
 type CreateTextThreadWithMessageRequest record {
-    ballerina/lang.int:0.0.0:Signed32? rateLimitPerUser?;
+    @jsondata:Name {value: "rate_limit_per_user"}
+    int:Signed32? rateLimitPerUser?;
+    @constraint:String {maxLength: 100, minLength: 1}
     string name;
+    @jsondata:Name {value: "auto_archive_duration"}
     anydata autoArchiveDuration?;
 };
 
 # Represents the Queries record for the operation: list_thread_members
 
 type ListThreadMembersQueries record {
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    @constraint:Int {minValue: 1, maxValue: 100}
+    int:Signed32 'limit?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string after?;
+    @http:Query {name: "with_member"}
     boolean withMember?;
 };
 
 
 type PrivateApplicationResponse record {
+    @jsondata:Name {value: "privacy_policy_url"}
     string? privacyPolicyUrl?;
+    @jsondata:Name {value: "bot_require_code_grant"}
     boolean? botRequireCodeGrant?;
     anydata bot?;
     string? icon?;
-    ballerina/lang.int:0.0.0:Signed32 flags;
+    int:Signed32 flags;
     string description;
+    @jsondata:Name {value: "interactions_endpoint_url"}
     string? interactionsEndpointUrl?;
     anydata 'type?;
-    ballerina/lang.int:0.0.0:Signed32? maxParticipants?;
+    @jsondata:Name {value: "max_participants"}
+    int:Signed32? maxParticipants?;
+    @jsondata:Name {value: "custom_install_url"}
     string? customInstallUrl?;
+    @jsondata:Name {value: "install_params"}
     anydata installParams?;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
+    @jsondata:Name {value: "cover_image"}
     string? coverImage?;
     string? slug?;
+    @jsondata:Name {value: "bot_public"}
     boolean? botPublic?;
+    @jsondata:Name {value: "terms_of_service_url"}
     string? termsOfServiceUrl?;
+    @jsondata:Name {value: "rpc_origins"}
     string[]? rpcOrigins?;
     UserResponse owner;
+    @jsondata:Name {value: "role_connections_verification_url"}
     string? roleConnectionsVerificationUrl?;
+    @jsondata:Name {value: "verify_key"}
     string verifyKey;
+    @jsondata:Name {value: "redirect_uris"}
     string[] redirectUris;
     anydata team?;
     string[]? tags?;
-    ballerina/lang.int:0.0.0:Signed32? approximateGuildCount?;
+    @jsondata:Name {value: "approximate_guild_count"}
+    int:Signed32? approximateGuildCount?;
     string name;
+    @jsondata:Name {value: "guild_id"}
     anydata guildId?;
+    @jsondata:Name {value: "primary_sku_id"}
     anydata primarySkuId?;
 };
 
 type 200OneOf6 anydata|();
 
-type InlineResponseItems200 ballerinax/discord:2.0.1:DefaultKeywordRuleResponse|ballerinax/discord:2.0.1:KeywordRuleResponse|ballerinax/discord:2.0.1:MLSpamRuleResponse|ballerinax/discord:2.0.1:MentionSpamRuleResponse|ballerinax/discord:2.0.1:SpamLinkRuleResponse|anydata|();
+type InlineResponseItems200 DefaultKeywordRuleResponse|KeywordRuleResponse|MLSpamRuleResponse|MentionSpamRuleResponse|SpamLinkRuleResponse|anydata|();
 
 
 type ThreadMetadataResponse record {
     boolean archived;
+    @jsondata:Name {value: "archive_timestamp"}
     string? archiveTimestamp?;
+    @jsondata:Name {value: "create_timestamp"}
     string? createTimestamp?;
     boolean? invitable?;
     boolean locked;
+    @jsondata:Name {value: "auto_archive_duration"}
     ThreadAutoArchiveDuration autoArchiveDuration;
 };
 
 
 type UserGuildOnboardingResponse record {
+    @jsondata:Name {value: "default_channel_ids"}
     UserGuildOnboardingResponseDefaultchannelidsItemsString[] defaultChannelIds;
+    @jsondata:Name {value: "guild_id"}
     string guildId;
     OnboardingPromptResponse[] prompts;
     boolean enabled;
@@ -4976,12 +6321,14 @@
 
 
 type GuildsTemplatesRequest1 record {
+    @constraint:String {maxLength: 100, minLength: 1}
     string name?;
     string? description?;
 };
 
 
 type GuildsTemplatesRequest2 record {
+    @constraint:String {maxLength: 100, minLength: 1}
     string name;
     string? description?;
 };
@@ -4989,33 +6336,45 @@
 # Represents the Queries record for the operation: list_guild_members
 
 type ListGuildMembersQueries record {
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
-    ballerina/lang.int:0.0.0:Signed32 after?;
+    @constraint:Int {minValue: 1, maxValue: 1000}
+    int:Signed32 'limit?;
+    @constraint:Int {minValue: 0}
+    int:Signed32 after?;
 };
 
 
 type CreateEntitlementRequestData record {
+    @jsondata:Name {value: "owner_id"}
     string ownerId;
+    @jsondata:Name {value: "sku_id"}
     string skuId;
-    ballerina/lang.int:0.0.0:Signed32 ownerType;
+    @jsondata:Name {value: "owner_type"}
+    int:Signed32 ownerType;
 };
 
 
 type UserPIIResponse record {
     boolean? bot?;
+    @constraint:Int {minValue: -9007199254740991, maxValue: 9007199254740991}
     int flags;
     boolean? verified?;
     string? banner?;
     string? avatar?;
     AvailableLocalesEnum locale;
     string discriminator;
+    @jsondata:Name {value: "premium_type"}
     anydata premiumType?;
-    ballerina/lang.int:0.0.0:Signed32? accentColor?;
+    @jsondata:Name {value: "accent_color"}
+    int:Signed32? accentColor?;
     boolean? system?;
+    @jsondata:Name {value: "global_name"}
     string? globalName?;
+    @jsondata:Name {value: "mfa_enabled"}
     boolean mfaEnabled;
+    @constraint:String {pattern: re `^(0|[1-9][0-9]*)$`}
     string id;
-    ballerina/lang.int:0.0.0:Signed32 publicFlags;
+    @jsondata:Name {value: "public_flags"}
+    int:Signed32 publicFlags;
     string? email?;
     string username;
 };
@@ -5023,21 +6382,25 @@
 # Represents the Headers record for the operation: update_original_webhook_message
 
 type UpdateOriginalWebhookMessageHeaders record {
+    @http:Header {name: "Content-Type"}
     "application/x-www-form-urlencoded" contentType;
 };
 
 
 type GuildsBulkBanRequest record {
+    @jsondata:Name {value: "user_ids"}
     GuildsBulkBanRequestUseridsItemsString[] userIds;
-    ballerina/lang.int:0.0.0:Signed32? deleteMessageSeconds?;
+    @jsondata:Name {value: "delete_message_seconds"}
+    int:Signed32? deleteMessageSeconds?;
 };
 
 
 type StickerPackCollectionResponse record {
+    @jsondata:Name {value: "sticker_packs"}
     StickerPackResponse[] stickerPacks;
 };
 
-// Unknown type: IncluderolesItemsnull
+type IncluderolesItemsnull string;
 
 // --- Client ---
 
@@ -5059,7 +6422,7 @@
 
     # list_my_guilds
     # 
-    resource function get users/\@me/guilds(map<string|string[]> headers = {}, boolean withCounts = false, string before = "", int:Signed32 limit = 0, string after = "", anydata Additional Values, ListMyGuildsQueries queries) returns MyGuildResponse[]|error;
+    resource function get users/\@me/guilds(map<string|string[]> headers = {}, boolean withCounts = false, string before = "", int:Signed32 limit = 0, string after = "", ListMyGuildsQueries queries) returns MyGuildResponse[]|error;
 
     # get_my_application
     # 
@@ -5111,7 +6474,7 @@
 
     # list_my_private_archived_threads
     # 
-    resource function get channels/[string channelId]/users/\@me/threads/archived/'private(map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, anydata Additional Values, ListMyPrivateArchivedThreadsQueries queries) returns ThreadsResponse|error;
+    resource function get channels/[string channelId]/users/\@me/threads/archived/'private(map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, ListMyPrivateArchivedThreadsQueries queries) returns ThreadsResponse|error;
 
     # list_guild_application_command_permissions
     # 
@@ -5135,11 +6498,11 @@
 
     # list_private_archived_threads
     # 
-    resource function get channels/[string channelId]/threads/archived/'private(map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, anydata Additional Values, ListPrivateArchivedThreadsQueries queries) returns ThreadsResponse|error;
+    resource function get channels/[string channelId]/threads/archived/'private(map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, ListPrivateArchivedThreadsQueries queries) returns ThreadsResponse|error;
 
     # list_public_archived_threads
     # 
-    resource function get channels/[string channelId]/threads/archived/'public(map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, anydata Additional Values, ListPublicArchivedThreadsQueries queries) returns ThreadsResponse|error;
+    resource function get channels/[string channelId]/threads/archived/'public(map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, ListPublicArchivedThreadsQueries queries) returns ThreadsResponse|error;
 
     # get_application_user_role_connection
     # 
@@ -5179,7 +6542,7 @@
 
     # list_guild_application_commands
     # 
-    resource function get applications/[string applicationId]/guilds/[string guildId]/commands(map<string|string[]> headers = {}, boolean withLocalizations = false, anydata Additional Values, ListGuildApplicationCommandsQueries queries) returns ApplicationCommandResponse[]|error;
+    resource function get applications/[string applicationId]/guilds/[string guildId]/commands(map<string|string[]> headers = {}, boolean withLocalizations = false, ListGuildApplicationCommandsQueries queries) returns ApplicationCommandResponse[]|error;
 
     # bulk_set_guild_application_commands
     # 
@@ -5207,7 +6570,7 @@
 
     # list_message_reactions_by_emoji
     # 
-    resource function get channels/[string channelId]/messages/[string messageId]/reactions/[string emojiName](map<string|string[]> headers = {}, int:Signed32 limit = 0, string after = "", anydata Additional Values, ListMessageReactionsByEmojiQueries queries) returns UserResponse[]|error;
+    resource function get channels/[string channelId]/messages/[string messageId]/reactions/[string emojiName](map<string|string[]> headers = {}, int:Signed32 limit = 0, string after = "", ListMessageReactionsByEmojiQueries queries) returns UserResponse[]|error;
 
     # delete_all_message_reactions_by_emoji
     # 
@@ -5227,19 +6590,19 @@
 
     # get_original_webhook_message
     # 
-    resource function get webhooks/[string webhookId]/[string webhookToken]/messages/\@original(map<string|string[]> headers = {}, string threadId = "", anydata Additional Values, GetOriginalWebhookMessageQueries queries) returns MessageResponse|error;
+    resource function get webhooks/[string webhookId]/[string webhookToken]/messages/\@original(map<string|string[]> headers = {}, string threadId = "", GetOriginalWebhookMessageQueries queries) returns MessageResponse|error;
 
     # delete_original_webhook_message
     # 
-    resource function delete webhooks/[string webhookId]/[string webhookToken]/messages/\@original(map<string|string[]> headers = {}, string threadId = "", anydata Additional Values, DeleteOriginalWebhookMessageQueries queries) returns error?;
+    resource function delete webhooks/[string webhookId]/[string webhookToken]/messages/\@original(map<string|string[]> headers = {}, string threadId = "", DeleteOriginalWebhookMessageQueries queries) returns error?;
 
     # update_original_webhook_message
     # 
-    resource function patch webhooks/[string webhookId]/[string webhookToken]/messages/\@original(UpdateOriginalWebhookMessageHeaders headers, MessagesoriginalBody payload, string threadId = "", anydata Additional Values, UpdateOriginalWebhookMessageQueries queries) returns MessageResponse|error;
+    resource function patch webhooks/[string webhookId]/[string webhookToken]/messages/\@original(UpdateOriginalWebhookMessageHeaders headers, MessagesoriginalBody payload, string threadId = "", UpdateOriginalWebhookMessageQueries queries) returns MessageResponse|error;
 
     # list_guild_scheduled_event_users
     # 
-    resource function get guilds/[string guildId]/scheduled\-events/[string guildScheduledEventId]/users(map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, string after = "", boolean withMember = false, anydata Additional Values, ListGuildScheduledEventUsersQueries queries) returns ScheduledEventUserResponse[]|error;
+    resource function get guilds/[string guildId]/scheduled\-events/[string guildScheduledEventId]/users(map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, string after = "", boolean withMember = false, ListGuildScheduledEventUsersQueries queries) returns ScheduledEventUserResponse[]|error;
 
     # get_auto_moderation_rule
     # 
@@ -5267,7 +6630,7 @@
 
     # search_guild_members
     # 
-    resource function get guilds/[string guildId]/members/search(map<string|string[]> headers = {}, string query = "", int:Signed32 limit = 0, anydata Additional Values, SearchGuildMembersQueries queries) returns GuildMemberResponse[]|error;
+    resource function get guilds/[string guildId]/members/search(map<string|string[]> headers = {}, string query = "", int:Signed32 limit = 0, SearchGuildMembersQueries queries) returns GuildMemberResponse[]|error;
 
     # get_active_guild_threads
     # 
@@ -5299,7 +6662,7 @@
 
     # get_entitlements
     # 
-    resource function get applications/[string applicationId]/entitlements(map<string|string[]> headers = {}, boolean excludeEnded = false, string userId = "", string before = "", SkuIds skuIds = "", string guildId = "", int:Signed32 limit = 0, string after = "", boolean onlyActive = false, anydata Additional Values, GetEntitlementsQueries queries) returns InlineResponseItems2001[]|error;
+    resource function get applications/[string applicationId]/entitlements(map<string|string[]> headers = {}, boolean excludeEnded = false, string userId = "", string before = "", SkuIds skuIds = "", string guildId = "", int:Signed32 limit = 0, string after = "", boolean onlyActive = false, GetEntitlementsQueries queries) returns InlineResponseItems2001[]|error;
 
     # create_entitlement
     # 
@@ -5319,7 +6682,7 @@
 
     # list_application_commands
     # 
-    resource function get applications/[string applicationId]/commands(map<string|string[]> headers = {}, boolean withLocalizations = false, anydata Additional Values, ListApplicationCommandsQueries queries) returns ApplicationCommandResponse[]|error;
+    resource function get applications/[string applicationId]/commands(map<string|string[]> headers = {}, boolean withLocalizations = false, ListApplicationCommandsQueries queries) returns ApplicationCommandResponse[]|error;
 
     # bulk_set_application_commands
     # 
@@ -5335,7 +6698,7 @@
 
     # get_thread_member
     # 
-    resource function get channels/[string channelId]/thread\-members/[string userId](map<string|string[]> headers = {}, boolean withMember = false, anydata Additional Values, GetThreadMemberQueries queries) returns ThreadMemberResponse|error;
+    resource function get channels/[string channelId]/thread\-members/[string userId](map<string|string[]> headers = {}, boolean withMember = false, GetThreadMemberQueries queries) returns ThreadMemberResponse|error;
 
     # add_thread_member
     # 
@@ -5347,7 +6710,7 @@
 
     # list_thread_members
     # 
-    resource function get channels/[string channelId]/thread\-members(map<string|string[]> headers = {}, int:Signed32 limit = 0, string after = "", boolean withMember = false, anydata Additional Values, ListThreadMembersQueries queries) returns ThreadMemberResponse[]|error;
+    resource function get channels/[string channelId]/thread\-members(map<string|string[]> headers = {}, int:Signed32 limit = 0, string after = "", boolean withMember = false, ListThreadMembersQueries queries) returns ThreadMemberResponse[]|error;
 
     # set_channel_permission_overwrite
     # 
@@ -5383,7 +6746,7 @@
 
     # list_messages
     # 
-    resource function get channels/[string channelId]/messages(map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, string after = "", string around = "", anydata Additional Values, ListMessagesQueries queries) returns MessageResponse[]|error;
+    resource function get channels/[string channelId]/messages(map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, string after = "", string around = "", ListMessagesQueries queries) returns MessageResponse[]|error;
 
     # create_message
     # 
@@ -5427,23 +6790,23 @@
 
     # get_webhook_message
     # 
-    resource function get webhooks/[string webhookId]/[string webhookToken]/messages/[string messageId](map<string|string[]> headers = {}, string threadId = "", anydata Additional Values, GetWebhookMessageQueries queries) returns MessageResponse|error;
+    resource function get webhooks/[string webhookId]/[string webhookToken]/messages/[string messageId](map<string|string[]> headers = {}, string threadId = "", GetWebhookMessageQueries queries) returns MessageResponse|error;
 
     # delete_webhook_message
     # 
-    resource function delete webhooks/[string webhookId]/[string webhookToken]/messages/[string messageId](map<string|string[]> headers = {}, string threadId = "", anydata Additional Values, DeleteWebhookMessageQueries queries) returns error?;
+    resource function delete webhooks/[string webhookId]/[string webhookToken]/messages/[string messageId](map<string|string[]> headers = {}, string threadId = "", DeleteWebhookMessageQueries queries) returns error?;
 
     # update_webhook_message
     # 
-    resource function patch webhooks/[string webhookId]/[string webhookToken]/messages/[string messageId](UpdateWebhookMessageHeaders headers, MessagesmessageIdBody1 payload, string threadId = "", anydata Additional Values, UpdateWebhookMessageQueries queries) returns MessageResponse|error;
+    resource function patch webhooks/[string webhookId]/[string webhookToken]/messages/[string messageId](UpdateWebhookMessageHeaders headers, MessagesmessageIdBody1 payload, string threadId = "", UpdateWebhookMessageQueries queries) returns MessageResponse|error;
 
     # execute_github_compatible_webhook
     # 
-    resource function post webhooks/[string webhookId]/[string webhookToken]/github(GithubWebhook payload, map<string|string[]> headers = {}, boolean wait = false, string threadId = "", anydata Additional Values, ExecuteGithubCompatibleWebhookQueries queries) returns error?;
+    resource function post webhooks/[string webhookId]/[string webhookToken]/github(GithubWebhook payload, map<string|string[]> headers = {}, boolean wait = false, string threadId = "", ExecuteGithubCompatibleWebhookQueries queries) returns error?;
 
     # execute_slack_compatible_webhook
     # 
-    resource function post webhooks/[string webhookId]/[string webhookToken]/slack(ExecuteSlackCompatibleWebhookHeaders headers, WebhookTokenSlackBody payload, boolean wait = false, string threadId = "", anydata Additional Values, ExecuteSlackCompatibleWebhookQueries queries) returns string?|error;
+    resource function post webhooks/[string webhookId]/[string webhookToken]/slack(ExecuteSlackCompatibleWebhookHeaders headers, WebhookTokenSlackBody payload, boolean wait = false, string threadId = "", ExecuteSlackCompatibleWebhookQueries queries) returns string?|error;
 
     # get_guild_template
     # 
@@ -5459,7 +6822,7 @@
 
     # get_guild_scheduled_event
     # 
-    resource function get guilds/[string guildId]/scheduled\-events/[string guildScheduledEventId](map<string|string[]> headers = {}, boolean withUserCount = false, anydata Additional Values, GetGuildScheduledEventQueries queries) returns ExternalScheduledEventResponse|StageScheduledEventResponse|VoiceScheduledEventResponse|error;
+    resource function get guilds/[string guildId]/scheduled\-events/[string guildScheduledEventId](map<string|string[]> headers = {}, boolean withUserCount = false, GetGuildScheduledEventQueries queries) returns ExternalScheduledEventResponse|StageScheduledEventResponse|VoiceScheduledEventResponse|error;
 
     # delete_guild_scheduled_event
     # 
@@ -5471,7 +6834,7 @@
 
     # list_guild_scheduled_events
     # 
-    resource function get guilds/[string guildId]/scheduled\-events(map<string|string[]> headers = {}, boolean withUserCount = false, anydata Additional Values, ListGuildScheduledEventsQueries queries) returns InlineResponseItems2004[]|error;
+    resource function get guilds/[string guildId]/scheduled\-events(map<string|string[]> headers = {}, boolean withUserCount = false, ListGuildScheduledEventsQueries queries) returns InlineResponseItems2004[]|error;
 
     # create_guild_scheduled_event
     # 
@@ -5515,11 +6878,11 @@
 
     # list_guild_audit_log_entries
     # 
-    resource function get guilds/[string guildId]/audit\-logs(map<string|string[]> headers = {}, string userId = "", int:Signed32 actionType = 0, string before = "", int:Signed32 limit = 0, string targetId = "", string after = "", anydata Additional Values, ListGuildAuditLogEntriesQueries queries) returns GuildAuditLogResponse|error;
+    resource function get guilds/[string guildId]/audit\-logs(map<string|string[]> headers = {}, string userId = "", int:Signed32 actionType = 0, string before = "", int:Signed32 limit = 0, string targetId = "", string after = "", ListGuildAuditLogEntriesQueries queries) returns GuildAuditLogResponse|error;
 
     # get_guild_widget_png
     # 
-    resource function get guilds/[string guildId]/widget\.png(map<string|string[]> headers = {}, WidgetImageStyles style = "shield", anydata Additional Values, GetGuildWidgetPngQueries queries) returns byte[]|error;
+    resource function get guilds/[string guildId]/widget\.png(map<string|string[]> headers = {}, WidgetImageStyles style = "shield", GetGuildWidgetPngQueries queries) returns byte[]|error;
 
     # sync_guild_template
     # 
@@ -5599,7 +6962,7 @@
 
     # list_guild_members
     # 
-    resource function get guilds/[string guildId]/members(map<string|string[]> headers = {}, int:Signed32 limit = 0, int:Signed32 after = 0, anydata Additional Values, ListGuildMembersQueries queries) returns GuildMemberResponse[]|error;
+    resource function get guilds/[string guildId]/members(map<string|string[]> headers = {}, int:Signed32 limit = 0, int:Signed32 after = 0, ListGuildMembersQueries queries) returns GuildMemberResponse[]|error;
 
     # get_guild_preview
     # 
@@ -5663,7 +7026,7 @@
 
     # preview_prune_guild
     # 
-    resource function get guilds/[string guildId]/prune(map<string|string[]> headers = {}, int:Signed32 days = 0, IncludeRoles includeRoles = "", anydata Additional Values, PreviewPruneGuildQueries queries) returns GuildPruneResponse|error;
+    resource function get guilds/[string guildId]/prune(map<string|string[]> headers = {}, int:Signed32 days = 0, IncludeRoles includeRoles = "", PreviewPruneGuildQueries queries) returns GuildPruneResponse|error;
 
     # prune_guild
     # 
@@ -5683,7 +7046,7 @@
 
     # list_guild_bans
     # 
-    resource function get guilds/[string guildId]/bans(map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, string after = "", anydata Additional Values, ListGuildBansQueries queries) returns GuildBanResponse[]|error;
+    resource function get guilds/[string guildId]/bans(map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, string after = "", ListGuildBansQueries queries) returns GuildBanResponse[]|error;
 
     # set_guild_mfa_level
     # 
@@ -5715,7 +7078,7 @@
 
     # execute_webhook
     # 
-    resource function post webhooks/[string webhookId]/[string webhookToken](WebhookIdwebhookTokenBody payload, map<string|string[]> headers = {}, boolean wait = false, string threadId = "", anydata Additional Values, ExecuteWebhookQueries queries) returns MessageResponse|error|();
+    resource function post webhooks/[string webhookId]/[string webhookToken](WebhookIdwebhookTokenBody payload, map<string|string[]> headers = {}, boolean wait = false, string threadId = "", ExecuteWebhookQueries queries) returns MessageResponse|error|();
 
     # delete_webhook_by_token
     # 
@@ -5755,7 +7118,7 @@
 
     # invite_resolve
     # 
-    resource function get invites/[string code](map<string|string[]> headers = {}, boolean withCounts = false, string guildScheduledEventId = "", anydata Additional Values, InviteResolveQueries queries) returns FriendInviteResponse|GroupDMInviteResponse|GuildInviteResponse|error;
+    resource function get invites/[string code](map<string|string[]> headers = {}, boolean withCounts = false, string guildScheduledEventId = "", InviteResolveQueries queries) returns FriendInviteResponse|GroupDMInviteResponse|GuildInviteResponse|error;
 
     # invite_revoke
     # 
@@ -5763,7 +7126,7 @@
 
     # get_guild
     # 
-    resource function get guilds/[string guildId](map<string|string[]> headers = {}, boolean withCounts = false, anydata Additional Values, GetGuildQueries queries) returns GuildWithCountsResponse|error;
+    resource function get guilds/[string guildId](map<string|string[]> headers = {}, boolean withCounts = false, GetGuildQueries queries) returns GuildWithCountsResponse|error;
 
     # delete_guild
     # 
`````
