# twilio — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `twilio` |
| **Old file** | `twilio/old/ballerinax_twilio.bal.txt` |
| **New file** | `twilio/new/ballerinax_twilio.bal.txt` |
| **Old lines** | 6220 |
| **New lines** | 6278 |
| **Lines added** | 64 |
| **Lines removed** | 6 |
| **Hunks** | 38 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 6 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (6)

- `type Conference_enum_update_status`
- `type Message_enum_schedule_type`
- `type Message_enum_traffic_type`
- `type Message_enum_update_status`
- `type Siprec_enum_update_status`
- `type Stream_enum_update_status`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 322–327 | 322–328 | Types | +1 | −0 |
| 2 | 358–363 | 359–365 | Types | +1 | −0 |
| 3 | 368–373 | 370–376 | Types | +1 | −0 |
| 4 | 398–403 | 401–407 | Types | +1 | −0 |
| 5 | 426–431 | 430–436 | Types | +1 | −0 |
| 6 | 1151–1156 | 1156–1162 | Types | +1 | −0 |
| 7 | 1165–1170 | 1171–1177 | Types | +1 | −0 |
| 8 | 1177–1192 | 1184–1204 | Types | +5 | −0 |
| 9 | 1422–1427 | 1434–1440 | Types | +1 | −0 |
| 10 | 1480–1485 | 1493–1499 | Types | +1 | −0 |
| 11 | 1494–1499 | 1508–1514 | Types | +1 | −0 |
| 12 | 1506–1521 | 1521–1541 | Types | +5 | −0 |
| 13 | 1660–1665 | 1680–1686 | Types | +1 | −0 |
| 14 | 1674–1679 | 1695–1701 | Types | +1 | −0 |
| 15 | 1687–1701 | 1709–1728 | Types | +5 | −0 |
| 16 | 1884–1889 | 1911–1917 | Types | +1 | −0 |
| 17 | 2352–2358 | 2380–2386 | Types | +1 | −1 |
| 18 | 2411–2416 | 2439–2445 | Types | +1 | −0 |
| 19 | 2425–2430 | 2454–2460 | Types | +1 | −0 |
| 20 | 2437–2452 | 2467–2487 | Types | +5 | −0 |
| 21 | 2520–2525 | 2555–2561 | Types | +1 | −0 |
| 22 | 3487–3492 | 3523–3529 | Types | +1 | −0 |
| 23 | 3608–3613 | 3645–3651 | Types | +1 | −0 |
| 24 | 3622–3627 | 3660–3666 | Types | +1 | −0 |
| 25 | 3781–3787 | 3820–3826 | Types | +1 | −1 |
| 26 | 3794–3805 | 3833–3846 | Types | +2 | −0 |
| 27 | 3814–3819 | 3855–3861 | Types | +1 | −0 |
| 28 | 3827–3841 | 3869–3888 | Types | +5 | −0 |
| 29 | 3930–3936 | 3977–3983 | Types | +1 | −1 |
| 30 | 4144–4149 | 4191–4197 | Types | +1 | −0 |
| 31 | 4330–4339 | 4378–4389 | Types | +2 | −0 |
| 32 | 4373–4379 | 4423–4429 | Types | +1 | −1 |
| 33 | 4484–4490 | 4534–4540 | Types | +1 | −1 |
| 34 | 4664–4671 | 4714–4723 | Types | +2 | −0 |
| 35 | 4846–4851 | 4898–4904 | Types | +1 | −0 |
| 36 | 4876–4893 | 4929–4948 | Types | +3 | −1 |
| 37 | 5322–5327 | 5377–5383 | Types | +1 | −0 |
| 38 | 5413–5420 | 5469–5478 | Types | +2 | −0 |

---

## Unified diff

`````diff
--- twilio/old/ballerinax_twilio.bal.txt	2026-08-12 12:57:30
+++ twilio/new/ballerinax_twilio.bal.txt	2026-08-12 13:19:20
@@ -322,6 +322,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     AuthTokenConfig|ApiKeyConfig auth;
@@ -358,6 +359,7 @@
 # Twilio Auth token Based Authentication configuration.
 # 
 
+@display {label: "Auth token based authentication config"}
 type AuthTokenConfig record {
     # Twilio account SID
     string accountSid;
@@ -368,6 +370,7 @@
 # Twilio API Key Based Authentication configurations.
 # 
 
+@display {label: "API Key Based authentication config"}
 type ApiKeyConfig record {
     # Twilio API key SID 
     string apiKey;
@@ -398,6 +401,7 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
@@ -426,6 +430,7 @@
     # Whether the participant is coaching another call. Can be: `true` or `false`. If not present, defaults to `false` unless `call_sid_to_coach` is defined. If `true`, `call_sid_to_coach` must be defined.
     boolean Coaching?;
     # The SID of the participant who is being `coached`. The participant being coached is the only participant who can hear the participant who is `coaching`.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^CA[0-9a-fA-F]{32}$`}
     string CallSidToCoach?;
 };
 
@@ -1151,6 +1156,7 @@
     # A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number.
     string FriendlyName?;
     # The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all `sms_*_url` values and use those of the application.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AP[0-9a-fA-F]{32}$`}
     string SmsApplicationSid?;
     # The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
     "HEAD"|"GET"|"POST"|"PATCH"|"PUT"|"DELETE" SmsFallbackMethod?;
@@ -1165,6 +1171,7 @@
     # The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
     "HEAD"|"GET"|"POST"|"PATCH"|"PUT"|"DELETE" StatusCallbackMethod?;
     # The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AP[0-9a-fA-F]{32}$`}
     string VoiceApplicationSid?;
     # Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`.
     boolean VoiceCallerIdLookup?;
@@ -1177,16 +1184,21 @@
     # The URL that we should call to answer a call to the new phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set.
     string VoiceUrl?;
     # The SID of the Identity resource that we should associate with the new phone number. Some regions require an Identity to meet local regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^RI[0-9a-fA-F]{32}$`}
     string IdentitySid?;
     # The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AD[0-9a-fA-F]{32}$`}
     string AddressSid?;
     Incoming_phone_number_toll_free_enum_emergency_status EmergencyStatus?;
     # The SID of the emergency address configuration to use for emergency calling from the new phone number.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AD[0-9a-fA-F]{32}$`}
     string EmergencyAddressSid?;
     # The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^TK[0-9a-fA-F]{32}$`}
     string TrunkSid?;
     Incoming_phone_number_toll_free_enum_voice_receive_mode VoiceReceiveMode?;
     # The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^BU[0-9a-fA-F]{32}$`}
     string BundleSid?;
 };
 
@@ -1422,6 +1434,7 @@
 
 type CreateSipAuthCallsCredentialListMappingRequest record {
     # The SID of the CredentialList resource to map to the SIP domain.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^CL[0-9a-fA-F]{32}$`}
     string CredentialListSid;
 };
 
@@ -1480,6 +1493,7 @@
     # A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, the is a formatted version of the phone number.
     string FriendlyName?;
     # The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those of the application.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AP[0-9a-fA-F]{32}$`}
     string SmsApplicationSid?;
     # The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
     "HEAD"|"GET"|"POST"|"PATCH"|"PUT"|"DELETE" SmsFallbackMethod?;
@@ -1494,6 +1508,7 @@
     # The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
     "HEAD"|"GET"|"POST"|"PATCH"|"PUT"|"DELETE" StatusCallbackMethod?;
     # The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AP[0-9a-fA-F]{32}$`}
     string VoiceApplicationSid?;
     # Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`.
     boolean VoiceCallerIdLookup?;
@@ -1506,16 +1521,21 @@
     # The URL that we should call to answer a call to the new phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set.
     string VoiceUrl?;
     # The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^RI[0-9a-fA-F]{32}$`}
     string IdentitySid?;
     # The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AD[0-9a-fA-F]{32}$`}
     string AddressSid?;
     Incoming_phone_number_mobile_enum_emergency_status EmergencyStatus?;
     # The SID of the emergency address configuration to use for emergency calling from the new phone number.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AD[0-9a-fA-F]{32}$`}
     string EmergencyAddressSid?;
     # The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^TK[0-9a-fA-F]{32}$`}
     string TrunkSid?;
     Incoming_phone_number_mobile_enum_voice_receive_mode VoiceReceiveMode?;
     # The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^BU[0-9a-fA-F]{32}$`}
     string BundleSid?;
 };
 
@@ -1660,6 +1680,7 @@
     # A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the new phone number.
     string FriendlyName?;
     # The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those set on the application.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AP[0-9a-fA-F]{32}$`}
     string SmsApplicationSid?;
     # The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
     "HEAD"|"GET"|"POST"|"PATCH"|"PUT"|"DELETE" SmsFallbackMethod?;
@@ -1674,6 +1695,7 @@
     # The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
     "HEAD"|"GET"|"POST"|"PATCH"|"PUT"|"DELETE" StatusCallbackMethod?;
     # The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AP[0-9a-fA-F]{32}$`}
     string VoiceApplicationSid?;
     # Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`.
     boolean VoiceCallerIdLookup?;
@@ -1687,15 +1709,20 @@
     string VoiceUrl?;
     Incoming_phone_number_enum_emergency_status EmergencyStatus?;
     # The SID of the emergency address configuration to use for emergency calling from the new phone number.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AD[0-9a-fA-F]{32}$`}
     string EmergencyAddressSid?;
     # The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^TK[0-9a-fA-F]{32}$`}
     string TrunkSid?;
     # The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^RI[0-9a-fA-F]{32}$`}
     string IdentitySid?;
     # The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AD[0-9a-fA-F]{32}$`}
     string AddressSid?;
     Incoming_phone_number_enum_voice_receive_mode VoiceReceiveMode?;
     # The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^BU[0-9a-fA-F]{32}$`}
     string BundleSid?;
     # The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
     string PhoneNumber?;
@@ -1884,6 +1911,7 @@
 
 type CreateSipIpAccessControlListMappingRequest record {
     # The unique id of the IP access control list to map to the SIP domain.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AL[0-9a-fA-F]{32}$`}
     string IpAccessControlListSid;
 };
 
@@ -2352,7 +2380,7 @@
     string? date_created?;
 };
 
-// Unknown type: Message_enum_traffic_type
+type Message_enum_traffic_type "free";
 
 type Usage_record_yesterday_enum_category "a2p-registration-fees"|"agent-conference"|"amazon-polly"|"answering-machine-detection"|"authy-authentications"|"authy-calls-outbound"|"authy-monthly-fees"|"authy-phone-intelligence"|"authy-phone-verifications"|"authy-sms-outbound"|"call-progess-events"|"calleridlookups"|"calls"|"calls-client"|"calls-globalconference"|"calls-inbound"|"calls-inbound-local"|"calls-inbound-mobile"|"calls-inbound-tollfree"|"calls-outbound"|"calls-pay-verb-transactions"|"calls-recordings"|"calls-sip"|"calls-sip-inbound"|"calls-sip-outbound"|"calls-transfers"|"carrier-lookups"|"conversations"|"conversations-api-requests"|"conversations-conversation-events"|"conversations-endpoint-connectivity"|"conversations-events"|"conversations-participant-events"|"conversations-participants"|"cps"|"flex-usage"|"fraud-lookups"|"group-rooms"|"group-rooms-data-track"|"group-rooms-encrypted-media-recorded"|"group-rooms-media-downloaded"|"group-rooms-media-recorded"|"group-rooms-media-routed"|"group-rooms-media-stored"|"group-rooms-participant-minutes"|"group-rooms-recorded-minutes"|"imp-v1-usage"|"lookups"|"marketplace"|"marketplace-algorithmia-named-entity-recognition"|"marketplace-cadence-transcription"|"marketplace-cadence-translation"|"marketplace-capio-speech-to-text"|"marketplace-convriza-ababa"|"marketplace-deepgram-phrase-detector"|"marketplace-digital-segment-business-info"|"marketplace-facebook-offline-conversions"|"marketplace-google-speech-to-text"|"marketplace-ibm-watson-message-insights"|"marketplace-ibm-watson-message-sentiment"|"marketplace-ibm-watson-recording-analysis"|"marketplace-ibm-watson-tone-analyzer"|"marketplace-icehook-systems-scout"|"marketplace-infogroup-dataaxle-bizinfo"|"marketplace-keen-io-contact-center-analytics"|"marketplace-marchex-cleancall"|"marketplace-marchex-sentiment-analysis-for-sms"|"marketplace-marketplace-nextcaller-social-id"|"marketplace-mobile-commons-opt-out-classifier"|"marketplace-nexiwave-voicemail-to-text"|"marketplace-nextcaller-advanced-caller-identification"|"marketplace-nomorobo-spam-score"|"marketplace-payfone-tcpa-compliance"|"marketplace-remeeting-automatic-speech-recognition"|"marketplace-tcpa-defense-solutions-blacklist-feed"|"marketplace-telo-opencnam"|"marketplace-truecnam-true-spam"|"marketplace-twilio-caller-name-lookup-us"|"marketplace-twilio-carrier-information-lookup"|"marketplace-voicebase-pci"|"marketplace-voicebase-transcription"|"marketplace-voicebase-transcription-custom-vocabulary"|"marketplace-whitepages-pro-caller-identification"|"marketplace-whitepages-pro-phone-intelligence"|"marketplace-whitepages-pro-phone-reputation"|"marketplace-wolfarm-spoken-results"|"marketplace-wolfram-short-answer"|"marketplace-ytica-contact-center-reporting-analytics"|"mediastorage"|"mms"|"mms-inbound"|"mms-inbound-longcode"|"mms-inbound-shortcode"|"mms-messages-carrierfees"|"mms-outbound"|"mms-outbound-longcode"|"mms-outbound-shortcode"|"monitor-reads"|"monitor-storage"|"monitor-writes"|"notify"|"notify-actions-attempts"|"notify-channels"|"number-format-lookups"|"pchat"|"pchat-users"|"peer-to-peer-rooms-participant-minutes"|"pfax"|"pfax-minutes"|"pfax-minutes-inbound"|"pfax-minutes-outbound"|"pfax-pages"|"phonenumbers"|"phonenumbers-cps"|"phonenumbers-emergency"|"phonenumbers-local"|"phonenumbers-mobile"|"phonenumbers-setups"|"phonenumbers-tollfree"|"premiumsupport"|"proxy"|"proxy-active-sessions"|"pstnconnectivity"|"pv"|"pv-composition-media-downloaded"|"pv-composition-media-encrypted"|"pv-composition-media-stored"|"pv-composition-minutes"|"pv-recording-compositions"|"pv-room-participants"|"pv-room-participants-au1"|"pv-room-participants-br1"|"pv-room-participants-ie1"|"pv-room-participants-jp1"|"pv-room-participants-sg1"|"pv-room-participants-us1"|"pv-room-participants-us2"|"pv-rooms"|"pv-sip-endpoint-registrations"|"recordings"|"recordingstorage"|"rooms-group-bandwidth"|"rooms-group-minutes"|"rooms-peer-to-peer-minutes"|"shortcodes"|"shortcodes-customerowned"|"shortcodes-mms-enablement"|"shortcodes-mps"|"shortcodes-random"|"shortcodes-uk"|"shortcodes-vanity"|"small-group-rooms"|"small-group-rooms-data-track"|"small-group-rooms-participant-minutes"|"sms"|"sms-inbound"|"sms-inbound-longcode"|"sms-inbound-shortcode"|"sms-messages-carrierfees"|"sms-messages-features"|"sms-messages-features-senderid"|"sms-outbound"|"sms-outbound-content-inspection"|"sms-outbound-longcode"|"sms-outbound-shortcode"|"speech-recognition"|"studio-engagements"|"sync"|"sync-actions"|"sync-endpoint-hours"|"sync-endpoint-hours-above-daily-cap"|"taskrouter-tasks"|"totalprice"|"transcriptions"|"trunking-cps"|"trunking-emergency-calls"|"trunking-origination"|"trunking-origination-local"|"trunking-origination-mobile"|"trunking-origination-tollfree"|"trunking-recordings"|"trunking-secure"|"trunking-termination"|"tts-google"|"turnmegabytes"|"turnmegabytes-australia"|"turnmegabytes-brasil"|"turnmegabytes-germany"|"turnmegabytes-india"|"turnmegabytes-ireland"|"turnmegabytes-japan"|"turnmegabytes-singapore"|"turnmegabytes-useast"|"turnmegabytes-uswest"|"twilio-interconnect"|"verify-push"|"verify-totp"|"verify-whatsapp-conversations-business-initiated"|"video-recordings"|"virtual-agent"|"voice-insights"|"voice-insights-client-insights-on-demand-minute"|"voice-insights-ptsn-insights-on-demand-minute"|"voice-insights-sip-interface-insights-on-demand-minute"|"voice-insights-sip-trunking-insights-on-demand-minute"|"voice-intelligence"|"voice-intelligence-transcription"|"voice-intelligence-operators"|"wireless"|"wireless-orders"|"wireless-orders-artwork"|"wireless-orders-bulk"|"wireless-orders-esim"|"wireless-orders-starter"|"wireless-usage"|"wireless-usage-commands"|"wireless-usage-commands-africa"|"wireless-usage-commands-asia"|"wireless-usage-commands-centralandsouthamerica"|"wireless-usage-commands-europe"|"wireless-usage-commands-home"|"wireless-usage-commands-northamerica"|"wireless-usage-commands-oceania"|"wireless-usage-commands-roaming"|"wireless-usage-data"|"wireless-usage-data-africa"|"wireless-usage-data-asia"|"wireless-usage-data-centralandsouthamerica"|"wireless-usage-data-custom-additionalmb"|"wireless-usage-data-custom-first5mb"|"wireless-usage-data-domestic-roaming"|"wireless-usage-data-europe"|"wireless-usage-data-individual-additionalgb"|"wireless-usage-data-individual-firstgb"|"wireless-usage-data-international-roaming-canada"|"wireless-usage-data-international-roaming-india"|"wireless-usage-data-international-roaming-mexico"|"wireless-usage-data-northamerica"|"wireless-usage-data-oceania"|"wireless-usage-data-pooled"|"wireless-usage-data-pooled-downlink"|"wireless-usage-data-pooled-uplink"|"wireless-usage-mrc"|"wireless-usage-mrc-custom"|"wireless-usage-mrc-individual"|"wireless-usage-mrc-pooled"|"wireless-usage-mrc-suspended"|"wireless-usage-sms"|"wireless-usage-voice";
 
@@ -2411,6 +2439,7 @@
     # A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number.
     string FriendlyName?;
     # The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those set on the application.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AP[0-9a-fA-F]{32}$`}
     string SmsApplicationSid?;
     # The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
     "HEAD"|"GET"|"POST"|"PATCH"|"PUT"|"DELETE" SmsFallbackMethod?;
@@ -2425,6 +2454,7 @@
     # The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
     "HEAD"|"GET"|"POST"|"PATCH"|"PUT"|"DELETE" StatusCallbackMethod?;
     # The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AP[0-9a-fA-F]{32}$`}
     string VoiceApplicationSid?;
     # Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`.
     boolean VoiceCallerIdLookup?;
@@ -2437,16 +2467,21 @@
     # The URL that we should call to answer a call to the new phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set.
     string VoiceUrl?;
     # The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^RI[0-9a-fA-F]{32}$`}
     string IdentitySid?;
     # The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AD[0-9a-fA-F]{32}$`}
     string AddressSid?;
     Incoming_phone_number_local_enum_emergency_status EmergencyStatus?;
     # The SID of the emergency address configuration to use for emergency calling from the new phone number.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AD[0-9a-fA-F]{32}$`}
     string EmergencyAddressSid?;
     # The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^TK[0-9a-fA-F]{32}$`}
     string TrunkSid?;
     Incoming_phone_number_local_enum_voice_receive_mode VoiceReceiveMode?;
     # The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^BU[0-9a-fA-F]{32}$`}
     string BundleSid?;
 };
 
@@ -2520,6 +2555,7 @@
 
 type CreateIncomingPhoneNumberAssignedAddOnRequest record {
     # The SID that identifies the Add-on installation.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^XE[0-9a-fA-F]{32}$`}
     string InstalledAddOnSid;
 };
 
@@ -3487,6 +3523,7 @@
 
 type CreateSipAuthRegistrationsCredentialListMappingRequest record {
     # The SID of the CredentialList resource to map to the SIP domain.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^CL[0-9a-fA-F]{32}$`}
     string CredentialListSid;
 };
 
@@ -3608,6 +3645,7 @@
     # The HTTP method we should use when calling the `async_amd_status_callback` URL. Can be: `GET` or `POST` and the default is `POST`.
     "HEAD"|"GET"|"POST"|"PATCH"|"PUT"|"DELETE" AsyncAmdStatusCallbackMethod?;
     # The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that `byoc` is only meaningful when `to` is a phone number; it will otherwise be ignored. (Beta)
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^BY[0-9a-fA-F]{32}$`}
     string Byoc?;
     # The Reason for the outgoing call. Use it to specify the purpose of the call that is presented on the called party's phone. (Branded Calls Beta)
     string CallReason?;
@@ -3622,6 +3660,7 @@
     # TwiML instructions for the call Twilio will use without fetching Twiml from url parameter. If both `twiml` and `url` are provided then `twiml` parameter will be ignored. Max 4000 characters.
     string Twiml?;
     # The SID of the Application resource that will handle the call, if the call will be handled by an application.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AP[0-9a-fA-F]{32}$`}
     string ApplicationSid?;
 };
 
@@ -3781,7 +3820,7 @@
     Message_enum_update_status Status?;
 };
 
-// Unknown type: Message_enum_update_status
+type Message_enum_update_status "canceled";
 
 type Incoming_phone_number_enum_emergency_address_status "registered"|"unregistered"|"pending-registration"|"registration-failure"|"pending-unregistration"|"unregistration-failure";
 
@@ -3794,12 +3833,14 @@
 
 type UpdateIncomingPhoneNumberRequest record {
     # The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to update.  For more information, see [Exchanging Numbers Between Subaccounts](https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers).
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AC[0-9a-fA-F]{32}$`}
     string AccountSid?;
     # The API version to use for incoming calls made to the phone number. The default is `2010-04-01`.
     string ApiVersion?;
     # A descriptive string that you created to describe this phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number.
     string FriendlyName?;
     # The SID of the application that should handle SMS messages sent to the number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those set on the application.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AP[0-9a-fA-F]{32}$`}
     string SmsApplicationSid?;
     # The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
     "HEAD"|"GET"|"POST"|"PATCH"|"PUT"|"DELETE" SmsFallbackMethod?;
@@ -3814,6 +3855,7 @@
     # The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
     "HEAD"|"GET"|"POST"|"PATCH"|"PUT"|"DELETE" StatusCallbackMethod?;
     # The SID of the application we should use to handle phone calls to the phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AP[0-9a-fA-F]{32}$`}
     string VoiceApplicationSid?;
     # Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`.
     boolean VoiceCallerIdLookup?;
@@ -3827,15 +3869,20 @@
     string VoiceUrl?;
     Incoming_phone_number_enum_emergency_status EmergencyStatus?;
     # The SID of the emergency address configuration to use for emergency calling from this phone number.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AD[0-9a-fA-F]{32}$`}
     string EmergencyAddressSid?;
     # The SID of the Trunk we should use to handle phone calls to the phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^TK[0-9a-fA-F]{32}$`}
     string TrunkSid?;
     Incoming_phone_number_enum_voice_receive_mode VoiceReceiveMode?;
     # The SID of the Identity resource that we should associate with the phone number. Some regions require an identity to meet local regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^RI[0-9a-fA-F]{32}$`}
     string IdentitySid?;
     # The SID of the Address resource we should associate with the phone number. Some regions require addresses to meet local regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AD[0-9a-fA-F]{32}$`}
     string AddressSid?;
     # The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^BU[0-9a-fA-F]{32}$`}
     string BundleSid?;
 };
 
@@ -3930,7 +3977,7 @@
     string StreetSecondary?;
 };
 
-// Unknown type: Siprec_enum_update_status
+type Siprec_enum_update_status "stopped";
 
 
 type ListDependentPhoneNumberResponse record {
@@ -4144,6 +4191,7 @@
 
 type CreateSipCredentialListMappingRequest record {
     # A 34 character string that uniquely identifies the CredentialList resource to map to the SIP domain.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^CL[0-9a-fA-F]{32}$`}
     string CredentialListSid;
 };
 
@@ -4330,10 +4378,12 @@
     # Whether the participant is coaching another call. Can be: `true` or `false`. If not present, defaults to `false` unless `call_sid_to_coach` is defined. If `true`, `call_sid_to_coach` must be defined.
     boolean Coaching?;
     # The SID of the participant who is being `coached`. The participant being coached is the only participant who can hear the participant who is `coaching`.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^CA[0-9a-fA-F]{32}$`}
     string CallSidToCoach?;
     # Jitter buffer size for the connecting participant. Twilio will use this setting to apply Jitter Buffer before participant's audio is mixed into the conference. Can be: `off`, `small`, `medium`, and `large`. Default to `large`.
     string JitterBufferSize?;
     # The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that `byoc` is only meaningful when `to` is a phone number; it will otherwise be ignored. (Beta)
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^BY[0-9a-fA-F]{32}$`}
     string Byoc?;
     # The phone number, Client identifier, or username portion of SIP address that made this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). Client identifiers are formatted `client:name`. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](https://www.twilio.com/docs/voice/api/outgoing-caller-ids) for your account. If the `to` parameter is a phone number, `callerId` must also be a phone number. If `to` is sip address, this value of `callerId` should be a username portion to be used to populate the From header that is passed to the SIP endpoint.
     string CallerId?;
@@ -4373,7 +4423,7 @@
     "HEAD"|"GET"|"POST"|"PATCH"|"PUT"|"DELETE" Method?;
 };
 
-// Unknown type: Stream_enum_update_status
+type Stream_enum_update_status "stopped";
 
 
 type CallSiprec record {
@@ -4484,7 +4534,7 @@
     "HEAD"|"GET"|"POST"|"PATCH"|"PUT"|"DELETE" AnnounceMethod?;
 };
 
-// Unknown type: Conference_enum_update_status
+type Conference_enum_update_status "completed";
 
 
 type CreateSipCredentialRequest record {
@@ -4664,8 +4714,10 @@
     # Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain.
     boolean Secure?;
     # The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^BY[0-9a-fA-F]{32}$`}
     string ByocTrunkSid?;
     # Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^PN[0-9a-fA-F]{32}$`}
     string EmergencyCallerSid?;
 };
 
@@ -4846,6 +4898,7 @@
     # The URL of the endpoint to which Twilio sends [Message status callback requests](https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url). URL must contain a valid hostname and underscores are not allowed. If you include this parameter with the `messaging_service_sid`, Twilio uses this URL instead of the Status Callback URL of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource). 
     string StatusCallback?;
     # The SID of the associated [TwiML Application](https://www.twilio.com/docs/usage/api/applications). If this parameter is provided, the `status_callback` parameter of this request is ignored; [Message status callback requests](https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url) are sent to the TwiML App's `message_status_callback` URL.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AP[0-9a-fA-F]{32}$`}
     string ApplicationSid?;
     # The maximum price in US dollars that you are willing to pay for this Message's delivery. The value can have up to four decimal places. When the `max_price` parameter is provided, the cost of a message is checked before it is sent. If the cost exceeds `max_price`, the message is not sent and the Message `status` is `failed`.
     decimal MaxPrice?;
@@ -4876,18 +4929,20 @@
     # The sender's Twilio phone number (in [E.164](https://en.wikipedia.org/wiki/E.164) format), [alphanumeric sender ID](https://www.twilio.com/docs/sms/send-messages#use-an-alphanumeric-sender-id), [Wireless SIM](https://www.twilio.com/docs/iot/wireless/programmable-wireless-send-machine-machine-sms-commands), [short code](https://www.twilio.com/docs/sms/api/short-code), or [channel address](https://www.twilio.com/docs/messaging/channels) (e.g., `whatsapp:+15554449999`). The value of the `from` parameter must be a sender that is hosted within Twilio and belongs to the Account creating the Message. If you are using `messaging_service_sid`, this parameter can be empty (Twilio assigns a `from` value from the Messaging Service's Sender Pool) or you can provide a specific sender from your Sender Pool.
     string From?;
     # The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services) you want to associate with the Message. When this parameter is provided and the `from` parameter is omitted, Twilio selects the optimal sender from the Messaging Service's Sender Pool. You may also provide a `from` parameter if you want to use a specific Sender from the Sender Pool.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^MG[0-9a-fA-F]{32}$`}
     string MessagingServiceSid?;
     # The text content of the outgoing message. Can be up to 1,600 characters in length. SMS only: If the `body` contains more than 160 [GSM-7](https://www.twilio.com/docs/glossary/what-is-gsm-7-character-encoding) characters (or 70 [UCS-2](https://www.twilio.com/docs/glossary/what-is-ucs-2-character-encoding) characters), the message is segmented and charged accordingly. For long `body` text, consider using the [send_as_mms parameter](https://www.twilio.com/blog/mms-for-long-text-messages).
     string Body?;
     # The URL of media to include in the Message content. `jpeg`, `jpg`, `gif`, and `png` file types are fully supported by Twilio and content is formatted for delivery on destination devices. The media size limit is 5 MB for supported file types (`jpeg`, `jpg`, `png`, `gif`) and 500 KB for [other types](https://www.twilio.com/docs/sms/accepted-mime-types) of accepted media. To send more than one image in the message, provide multiple `media_url` parameters in the POST request. You can include up to ten `media_url` parameters per message. [International](https://support.twilio.com/hc/en-us/articles/223179808-Sending-and-receiving-MMS-messages) and [carrier](https://support.twilio.com/hc/en-us/articles/223133707-Is-MMS-supported-for-all-carriers-in-US-and-Canada-) limits apply.
     string[] MediaUrl?;
     # For [Content Editor/API](https://www.twilio.com/docs/content) only: The SID of the Content Template to be used with the Message, e.g., `HXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`. If this parameter is not provided, a Content Template is not used. Find the SID in the Console on the Content Editor page. For Content API users, the SID is found in Twilio's response when [creating the Template](https://www.twilio.com/docs/content/content-api-resources#create-templates) or by [fetching your Templates](https://www.twilio.com/docs/content/content-api-resources#fetch-all-content-resources).
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^HX[0-9a-fA-F]{32}$`}
     string ContentSid?;
 };
 
 type Message_enum_content_retention "retain"|"discard";
 
-// Unknown type: Message_enum_schedule_type
+type Message_enum_schedule_type "fixed";
 
 
 type ListAuthorizedConnectAppResponse record {
@@ -5322,6 +5377,7 @@
 
 type CreateSipAuthCallsIpAccessControlListMappingRequest record {
     # The SID of the IpAccessControlList resource to map to the SIP domain.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^AL[0-9a-fA-F]{32}$`}
     string IpAccessControlListSid;
 };
 
@@ -5413,8 +5469,10 @@
     # Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain.
     boolean Secure?;
     # The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^BY[0-9a-fA-F]{32}$`}
     string ByocTrunkSid?;
     # Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call.
+    @constraint:String {maxLength: 34, minLength: 34, pattern: re `^PN[0-9a-fA-F]{32}$`}
     string EmergencyCallerSid?;
 };
 
`````
