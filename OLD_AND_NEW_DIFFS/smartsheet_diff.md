# smartsheet — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `smartsheet` |
| **Old file** | `smartsheet/old/ballerinax_smartsheet.bal.txt` |
| **New file** | `smartsheet/new/ballerinax_smartsheet.bal.txt` |
| **Old lines** | 10516 |
| **New lines** | 10940 |
| **Lines added** | 704 |
| **Lines removed** | 280 |
| **Hunks** | 424 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 38 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 171 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (38)

- `type Columns`
- `type ContactOptions`
- `type FavoritesOneOf2`
- `type Format`
- `type Formula`
- `type GroupMembersAddArray`
- `type GroupsgroupIdmembersOneOf2`
- `type IcalEnabled`
- `type Id`
- `type Index`
- `type Locked`
- `type Name`
- `type Options`
- `type Permalink`
- `type Primary`
- `type PropertiesContactOptions`
- `type PropertiesId`
- `type PropertiesOptions`
- `type PropertiesSymbol`
- `type PropertiesTitle`
- `type ReadOnlyFullEnabled`
- `type ReadOnlyFullShowToolbar`
- `type ReadOnlyLiteEnabled`
- `type ReadWriteEnabled`
- `type ReadWriteShowToolbar`
- `type ReportsreportIdsharesOneOf2`
- `type SheetssheetIdrowsOneOf2`
- `type SheetssheetIdrowsOneOf21`
- `type SheetssheetIdsharesOneOf2`
- `type Symbol`
- `type TimestampDateTime`
- `type TimestampNumber`
- `type Title`
- `type UsersuserIdalternateemailsOneOf2`
- `type Validation`
- `type Version`
- `type Width`
- `type WorkspacesworkspaceIdsharesOneOf2`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 230–240 | 230–240 | Types | +3 | −3 |
| 2 | 356–362 | 356–362 | Types | +1 | −1 |
| 3 | 367–376 | 367–379 | Types | +3 | −0 |
| 4 | 393–402 | 396–407 | Types | +2 | −0 |
| 5 | 449–460 | 454–466 | Types | +2 | −1 |
| 6 | 462–469 | 468–477 | Types | +2 | −0 |
| 7 | 478–483 | 486–492 | Types | +1 | −0 |
| 8 | 485–494 | 494–507 | Types | +5 | −1 |
| 9 | 511–521 | 524–537 | Types | +6 | −3 |
| 10 | 531–538 | 547–556 | Types | +2 | −0 |
| 11 | 545–553 | 563–571 | Types | +2 | −2 |
| 12 | 782–800 | 800–821 | Types | +4 | −1 |
| 13 | 903–909 | 924–931 | Types | +2 | −1 |
| 14 | 967–974 | 989–998 | Types | +2 | −0 |
| 15 | 976–983 | 1000–1009 | Types | +2 | −0 |
| 16 | 988–995 | 1014–1023 | Types | +2 | −0 |
| 17 | 1016–1021 | 1044–1050 | Types | +1 | −0 |
| 18 | 1027–1032 | 1056–1062 | Types | +1 | −0 |
| 19 | 1130–1136 | 1160–1166 | Types | +1 | −1 |
| 20 | 1146–1151 | 1176–1182 | Types | +1 | −0 |
| 21 | 1153–1158 | 1184–1190 | Types | +1 | −0 |
| 22 | 1173–1180 | 1205–1214 | Types | +2 | −0 |
| 23 | 1259–1265 | 1293–1299 | Types | +1 | −1 |
| 24 | 1275–1281 | 1309–1315 | Types | +1 | −1 |
| 25 | 1291–1297 | 1325–1331 | Types | +1 | −1 |
| 26 | 1302–1311 | 1336–1348 | Types | +3 | −0 |
| 27 | 1364–1370 | 1401–1407 | Types | +1 | −1 |
| 28 | 1376–1382 | 1413–1419 | Types | +1 | −1 |
| 29 | 1425–1430 | 1462–1468 | Types | +1 | −0 |
| 30 | 1453–1458 | 1491–1497 | Types | +1 | −0 |
| 31 | 1466–1478 | 1505–1518 | Types | +3 | −2 |
| 32 | 1484–1490 | 1524–1530 | Types | +1 | −1 |
| 33 | 1544–1555 | 1584–1598 | Types | +3 | −0 |
| 34 | 1581–1587 | 1624–1630 | Types | +1 | −1 |
| 35 | 1592–1597 | 1635–1641 | Types | +1 | −0 |
| 36 | 1650–1672 | 1694–1722 | Types | +12 | −6 |
| 37 | 1677–1683 | 1727–1733 | Types | +1 | −1 |
| 38 | 1700–1707 | 1750–1759 | Types | +2 | −0 |
| 39 | 1806–1815 | 1858–1868 | Types | +2 | −1 |
| 40 | 1818–1825 | 1871–1880 | Types | +2 | −0 |
| 41 | 1838–1846 | 1893–1901 | Types | +2 | −2 |
| 42 | 1877–1890 | 1932–1948 | Types | +4 | −1 |
| 43 | 1892–1897 | 1950–1956 | Types | +1 | −0 |
| 44 | 1909–1916 | 1968–1977 | Types | +2 | −0 |
| 45 | 1937–1943 | 1998–2004 | Types | +1 | −1 |
| 46 | 1948–1953 | 2009–2015 | Types | +1 | −0 |
| 47 | 1957–1975 | 2019–2044 | Types | +8 | −1 |
| 48 | 1977–1982 | 2046–2052 | Types | +1 | −0 |
| 49 | 1984–1989 | 2054–2060 | Types | +1 | −0 |
| 50 | 1997–2003 | 2068–2074 | Types | +1 | −1 |
| 51 | 2013–2028 | 2084–2102 | Types | +5 | −2 |
| 52 | 2051–2060 | 2125–2137 | Types | +3 | −0 |
| 53 | 2259–2264 | 2336–2342 | Types | +1 | −0 |
| 54 | 2509–2528 | 2587–2611 | Types | +5 | −0 |
| 55 | 2548–2554 | 2631–2637 | Types | +1 | −1 |
| 56 | 2582–2588 | 2665–2671 | Types | +1 | −1 |
| 57 | 2608–2614 | 2691–2697 | Types | +1 | −1 |
| 58 | 2624–2630 | 2707–2713 | Types | +1 | −1 |
| 59 | 2640–2646 | 2723–2729 | Types | +1 | −1 |
| 60 | 2656–2662 | 2739–2745 | Types | +1 | −1 |
| 61 | 2672–2678 | 2755–2761 | Types | +1 | −1 |
| 62 | 2688–2694 | 2771–2777 | Types | +1 | −1 |
| 63 | 2704–2710 | 2787–2793 | Types | +1 | −1 |
| 64 | 2720–2726 | 2803–2809 | Types | +1 | −1 |
| 65 | 2731–2738 | 2814–2823 | Types | +2 | −0 |
| 66 | 2746–2752 | 2831–2837 | Types | +1 | −1 |
| 67 | 2757–2766 | 2842–2853 | Types | +2 | −0 |
| 68 | 2774–2780 | 2861–2867 | Types | +1 | −1 |
| 69 | 2785–2792 | 2872–2881 | Types | +2 | −0 |
| 70 | 2800–2806 | 2889–2895 | Types | +1 | −1 |
| 71 | 2816–2822 | 2905–2911 | Types | +1 | −1 |
| 72 | 2832–2838 | 2921–2927 | Types | +1 | −1 |
| 73 | 2848–2854 | 2937–2943 | Types | +1 | −1 |
| 74 | 2876–2882 | 2965–2971 | Types | +1 | −1 |
| 75 | 2891–2900 | 2980–2992 | Types | +3 | −0 |
| 76 | 2908–2914 | 3000–3006 | Types | +1 | −1 |
| 77 | 2923–2930 | 3015–3024 | Types | +2 | −0 |
| 78 | 2938–2944 | 3032–3038 | Types | +1 | −1 |
| 79 | 2953–2959 | 3047–3053 | Types | +1 | −1 |
| 80 | 2969–2975 | 3063–3069 | Types | +1 | −1 |
| 81 | 2985–2991 | 3079–3085 | Types | +1 | −1 |
| 82 | 3001–3007 | 3095–3101 | Types | +1 | −1 |
| 83 | 3012–3023 | 3106–3120 | Types | +3 | −0 |
| 84 | 3031–3037 | 3128–3134 | Types | +1 | −1 |
| 85 | 3047–3053 | 3144–3150 | Types | +1 | −1 |
| 86 | 3063–3069 | 3160–3166 | Types | +1 | −1 |
| 87 | 3074–3081 | 3171–3180 | Types | +2 | −0 |
| 88 | 3089–3095 | 3188–3194 | Types | +1 | −1 |
| 89 | 3100–3109 | 3199–3211 | Types | +3 | −0 |
| 90 | 3117–3123 | 3219–3225 | Types | +1 | −1 |
| 91 | 3128–3137 | 3230–3242 | Types | +3 | −0 |
| 92 | 3145–3151 | 3250–3256 | Types | +1 | −1 |
| 93 | 3161–3167 | 3266–3272 | Types | +1 | −1 |
| 94 | 3177–3183 | 3282–3288 | Types | +1 | −1 |
| 95 | 3193–3199 | 3298–3304 | Types | +1 | −1 |
| 96 | 3209–3215 | 3314–3320 | Types | +1 | −1 |
| 97 | 3225–3231 | 3330–3336 | Types | +1 | −1 |
| 98 | 3238–3251 | 3343–3360 | Types | +4 | −0 |
| 99 | 3259–3265 | 3368–3374 | Types | +1 | −1 |
| 100 | 3272–3287 | 3381–3401 | Types | +5 | −0 |
| 101 | 3295–3301 | 3409–3415 | Types | +1 | −1 |
| 102 | 3311–3317 | 3425–3431 | Types | +1 | −1 |
| 103 | 3322–3327 | 3436–3442 | Types | +1 | −0 |
| 104 | 3337–3343 | 3452–3458 | Types | +1 | −1 |
| 105 | 3361–3367 | 3476–3482 | Types | +1 | −1 |
| 106 | 3387–3393 | 3502–3508 | Types | +1 | −1 |
| 107 | 3403–3409 | 3518–3524 | Types | +1 | −1 |
| 108 | 3419–3425 | 3534–3540 | Types | +1 | −1 |
| 109 | 3435–3441 | 3550–3556 | Types | +1 | −1 |
| 110 | 3448–3453 | 3563–3569 | Types | +1 | −0 |
| 111 | 3461–3467 | 3577–3583 | Types | +1 | −1 |
| 112 | 3477–3483 | 3593–3599 | Types | +1 | −1 |
| 113 | 3493–3499 | 3609–3615 | Types | +1 | −1 |
| 114 | 3504–3509 | 3620–3626 | Types | +1 | −0 |
| 115 | 3526–3532 | 3643–3650 | Types | +2 | −1 |
| 116 | 3538–3544 | 3656–3662 | Types | +1 | −1 |
| 117 | 3554–3560 | 3672–3678 | Types | +1 | −1 |
| 118 | 3570–3576 | 3688–3694 | Types | +1 | −1 |
| 119 | 3581–3586 | 3699–3705 | Types | +1 | −0 |
| 120 | 3594–3600 | 3713–3719 | Types | +1 | −1 |
| 121 | 3605–3612 | 3724–3733 | Types | +2 | −0 |
| 122 | 3635–3641 | 3756–3762 | Types | +1 | −1 |
| 123 | 3650–3657 | 3771–3780 | Types | +2 | −0 |
| 124 | 3665–3671 | 3788–3794 | Types | +1 | −1 |
| 125 | 3680–3689 | 3803–3815 | Types | +3 | −0 |
| 126 | 3697–3703 | 3823–3829 | Types | +1 | −1 |
| 127 | 3712–3721 | 3838–3850 | Types | +3 | −0 |
| 128 | 3729–3735 | 3858–3864 | Types | +1 | −1 |
| 129 | 3744–3751 | 3873–3882 | Types | +2 | −0 |
| 130 | 3759–3765 | 3890–3896 | Types | +1 | −1 |
| 131 | 3775–3781 | 3906–3912 | Types | +1 | −1 |
| 132 | 3799–3805 | 3930–3936 | Types | +1 | −1 |
| 133 | 3815–3821 | 3946–3952 | Types | +1 | −1 |
| 134 | 3831–3837 | 3962–3968 | Types | +1 | −1 |
| 135 | 3842–3849 | 3973–3982 | Types | +2 | −0 |
| 136 | 3857–3863 | 3990–3996 | Types | +1 | −1 |
| 137 | 3868–3877 | 4001–4013 | Types | +3 | −0 |
| 138 | 3885–3891 | 4021–4027 | Types | +1 | −1 |
| 139 | 3901–3907 | 4037–4043 | Types | +1 | −1 |
| 140 | 3927–3933 | 4063–4069 | Types | +1 | −1 |
| 141 | 3943–3949 | 4079–4085 | Types | +1 | −1 |
| 142 | 3959–3965 | 4095–4101 | Types | +1 | −1 |
| 143 | 3970–3975 | 4106–4112 | Types | +1 | −0 |
| 144 | 3987–3993 | 4124–4130 | Types | +1 | −1 |
| 145 | 4000–4007 | 4137–4146 | Types | +2 | −0 |
| 146 | 4017–4023 | 4156–4162 | Types | +1 | −1 |
| 147 | 4033–4039 | 4172–4178 | Types | +1 | −1 |
| 148 | 4048–4055 | 4187–4196 | Types | +2 | −0 |
| 149 | 4063–4069 | 4204–4210 | Types | +1 | −1 |
| 150 | 4078–4087 | 4219–4231 | Types | +3 | −0 |
| 151 | 4095–4101 | 4239–4245 | Types | +1 | −1 |
| 152 | 4110–4119 | 4254–4266 | Types | +3 | −0 |
| 153 | 4127–4133 | 4274–4280 | Types | +1 | −1 |
| 154 | 4138–4149 | 4285–4299 | Types | +3 | −0 |
| 155 | 4159–4165 | 4309–4315 | Types | +1 | −1 |
| 156 | 4173–4182 | 4323–4335 | Types | +3 | −0 |
| 157 | 4190–4196 | 4343–4349 | Types | +1 | −1 |
| 158 | 4201–4206 | 4354–4360 | Types | +1 | −0 |
| 159 | 4214–4220 | 4368–4374 | Types | +1 | −1 |
| 160 | 4230–4236 | 4384–4390 | Types | +1 | −1 |
| 161 | 4254–4260 | 4408–4414 | Types | +1 | −1 |
| 162 | 4270–4276 | 4424–4430 | Types | +1 | −1 |
| 163 | 4281–4292 | 4435–4449 | Types | +3 | −0 |
| 164 | 4300–4306 | 4457–4463 | Types | +1 | −1 |
| 165 | 4313–4322 | 4470–4482 | Types | +3 | −0 |
| 166 | 4332–4338 | 4492–4498 | Types | +1 | −1 |
| 167 | 4348–4354 | 4508–4514 | Types | +1 | −1 |
| 168 | 4359–4366 | 4519–4528 | Types | +2 | −0 |
| 169 | 4374–4380 | 4536–4542 | Types | +1 | −1 |
| 170 | 4390–4396 | 4552–4558 | Types | +1 | −1 |
| 171 | 4416–4422 | 4578–4584 | Types | +1 | −1 |
| 172 | 4432–4438 | 4594–4600 | Types | +1 | −1 |
| 173 | 4448–4454 | 4610–4616 | Types | +1 | −1 |
| 174 | 4464–4470 | 4626–4632 | Types | +1 | −1 |
| 175 | 4480–4486 | 4642–4648 | Types | +1 | −1 |
| 176 | 4491–4496 | 4653–4659 | Types | +1 | −0 |
| 177 | 4508–4514 | 4671–4677 | Types | +1 | −1 |
| 178 | 4524–4530 | 4687–4693 | Types | +1 | −1 |
| 179 | 4540–4546 | 4703–4709 | Types | +1 | −1 |
| 180 | 4553–4560 | 4716–4725 | Types | +2 | −0 |
| 181 | 4570–4576 | 4735–4741 | Types | +1 | −1 |
| 182 | 4586–4592 | 4751–4757 | Types | +1 | −1 |
| 183 | 4612–4618 | 4777–4783 | Types | +1 | −1 |
| 184 | 4635–4641 | 4800–4806 | Types | +1 | −1 |
| 185 | 4651–4657 | 4816–4822 | Types | +1 | −1 |
| 186 | 4667–4673 | 4832–4838 | Types | +1 | −1 |
| 187 | 4683–4689 | 4848–4854 | Types | +1 | −1 |
| 188 | 4699–4705 | 4864–4870 | Types | +1 | −1 |
| 189 | 4715–4721 | 4880–4886 | Types | +1 | −1 |
| 190 | 4731–4737 | 4896–4902 | Types | +1 | −1 |
| 191 | 4747–4753 | 4912–4918 | Types | +1 | −1 |
| 192 | 4763–4769 | 4928–4934 | Types | +1 | −1 |
| 193 | 4779–4785 | 4944–4950 | Types | +1 | −1 |
| 194 | 4794–4801 | 4959–4968 | Types | +2 | −0 |
| 195 | 4809–4815 | 4976–4982 | Types | +1 | −1 |
| 196 | 4824–4831 | 4991–5000 | Types | +2 | −0 |
| 197 | 4839–4845 | 5008–5014 | Types | +1 | −1 |
| 198 | 4850–4855 | 5019–5025 | Types | +1 | −0 |
| 199 | 4865–4871 | 5035–5041 | Types | +1 | −1 |
| 200 | 4881–4887 | 5051–5057 | Types | +1 | −1 |
| 201 | 4897–4903 | 5067–5073 | Types | +1 | −1 |
| 202 | 4913–4919 | 5083–5089 | Types | +1 | −1 |
| 203 | 4937–4943 | 5107–5113 | Types | +1 | −1 |
| 204 | 4948–4955 | 5118–5127 | Types | +2 | −0 |
| 205 | 4963–4969 | 5135–5141 | Types | +1 | −1 |
| 206 | 4979–4985 | 5151–5157 | Types | +1 | −1 |
| 207 | 5005–5011 | 5177–5183 | Types | +1 | −1 |
| 208 | 5021–5027 | 5193–5199 | Types | +1 | −1 |
| 209 | 5037–5049 | 5209–5221 | Types | +2 | −2 |
| 210 | 5084–5089 | 5256–5262 | Types | +1 | −0 |
| 211 | 5106–5113 | 5279–5288 | Types | +2 | −0 |
| 212 | 5130–5135 | 5305–5311 | Types | +1 | −0 |
| 213 | 5152–5157 | 5328–5334 | Types | +1 | −0 |
| 214 | 5164–5170 | 5341–5348 | Types | +2 | −1 |
| 215 | 5194–5201 | 5372–5381 | Types | +2 | −0 |
| 216 | 5217–5222 | 5397–5403 | Types | +1 | −0 |
| 217 | 5292–5297 | 5473–5479 | Types | +1 | −0 |
| 218 | 5331–5342 | 5513–5526 | Types | +3 | −1 |
| 219 | 5358–5363 | 5542–5548 | Types | +1 | −0 |
| 220 | 5386–5401 | 5571–5588 | Types | +4 | −2 |
| 221 | 5413–5418 | 5600–5606 | Types | +1 | −0 |
| 222 | 5449–5456 | 5637–5646 | Types | +2 | −0 |
| 223 | 5497–5502 | 5687–5693 | Types | +1 | −0 |
| 224 | 5534–5539 | 5725–5731 | Types | +1 | −0 |
| 225 | 5575–5580 | 5767–5773 | Types | +1 | −0 |
| 226 | 5582–5587 | 5775–5781 | Types | +1 | −0 |
| 227 | 5589–5594 | 5783–5789 | Types | +1 | −0 |
| 228 | 5596–5605 | 5791–5802 | Types | +3 | −1 |
| 229 | 5642–5647 | 5839–5845 | Types | +1 | −0 |
| 230 | 5657–5670 | 5855–5872 | Types | +4 | −0 |
| 231 | 5727–5732 | 5929–5935 | Types | +1 | −0 |
| 232 | 5772–5777 | 5975–5981 | Types | +1 | −0 |
| 233 | 5779–5784 | 5983–5989 | Types | +1 | −0 |
| 234 | 5810–5817 | 6015–6024 | Types | +2 | −0 |
| 235 | 5855–5861 | 6062–6069 | Types | +2 | −1 |
| 236 | 5870–5877 | 6078–6087 | Types | +2 | −0 |
| 237 | 5978–5983 | 6188–6194 | Types | +1 | −0 |
| 238 | 6008–6013 | 6219–6225 | Types | +1 | −0 |
| 239 | 6053–6060 | 6265–6274 | Types | +2 | −0 |
| 240 | 6062–6067 | 6276–6282 | Types | +1 | −0 |
| 241 | 6087–6092 | 6302–6308 | Types | +1 | −0 |
| 242 | 6138–6151 | 6354–6370 | Types | +4 | −1 |
| 243 | 6220–6225 | 6439–6445 | Types | +1 | −0 |
| 244 | 6231–6236 | 6451–6457 | Types | +1 | −0 |
| 245 | 6348–6353 | 6569–6575 | Types | +1 | −0 |
| 246 | 6393–6400 | 6615–6624 | Types | +2 | −0 |
| 247 | 6402–6413 | 6626–6640 | Types | +3 | −0 |
| 248 | 6435–6440 | 6662–6668 | Types | +1 | −0 |
| 249 | 6474–6479 | 6702–6708 | Types | +1 | −0 |
| 250 | 6519–6524 | 6748–6754 | Types | +1 | −0 |
| 251 | 6526–6531 | 6756–6762 | Types | +1 | −0 |
| 252 | 6582–6589 | 6813–6822 | Types | +2 | −0 |
| 253 | 6614–6621 | 6847–6856 | Types | +2 | −0 |
| 254 | 6635–6640 | 6870–6876 | Types | +1 | −0 |
| 255 | 6749–6756 | 6985–6994 | Types | +2 | −0 |
| 256 | 6770–6775 | 7008–7014 | Types | +1 | −0 |
| 257 | 6823–6828 | 7062–7068 | Types | +1 | −0 |
| 258 | 6830–6835 | 7070–7076 | Types | +1 | −0 |
| 259 | 6837–6851 | 7078–7094 | Types | +3 | −1 |
| 260 | 6853–6858 | 7096–7102 | Types | +1 | −0 |
| 261 | 6860–6865 | 7104–7110 | Types | +1 | −0 |
| 262 | 6920–6925 | 7165–7171 | Types | +1 | −0 |
| 263 | 6959–6964 | 7205–7211 | Types | +1 | −0 |
| 264 | 7002–7008 | 7249–7256 | Types | +2 | −1 |
| 265 | 7015–7020 | 7263–7269 | Types | +1 | −0 |
| 266 | 7022–7027 | 7271–7277 | Types | +1 | −0 |
| 267 | 7057–7064 | 7307–7316 | Types | +2 | −0 |
| 268 | 7101–7108 | 7353–7362 | Types | +2 | −0 |
| 269 | 7160–7165 | 7414–7420 | Types | +1 | −0 |
| 270 | 7194–7199 | 7449–7455 | Types | +1 | −0 |
| 271 | 7201–7208 | 7457–7466 | Types | +2 | −0 |
| 272 | 7210–7215 | 7468–7474 | Types | +1 | −0 |
| 273 | 7260–7265 | 7519–7525 | Types | +1 | −0 |
| 274 | 7274–7283 | 7534–7545 | Types | +2 | −0 |
| 275 | 7285–7290 | 7547–7553 | Types | +1 | −0 |
| 276 | 7303–7308 | 7566–7572 | Types | +1 | −0 |
| 277 | 7324–7335 | 7588–7601 | Types | +3 | −1 |
| 278 | 7353–7358 | 7619–7625 | Types | +1 | −0 |
| 279 | 7368–7374 | 7635–7641 | Types | +1 | −1 |
| 280 | 7394–7399 | 7661–7667 | Types | +1 | −0 |
| 281 | 7440–7446 | 7708–7715 | Types | +2 | −1 |
| 282 | 7479–7486 | 7748–7757 | Types | +2 | −0 |
| 283 | 7507–7518 | 7778–7791 | Types | +4 | −2 |
| 284 | 7571–7579 | 7844–7854 | Types | +4 | −2 |
| 285 | 7588–7599 | 7863–7876 | Types | +3 | −1 |
| 286 | 7601–7606 | 7878–7884 | Types | +1 | −0 |
| 287 | 7608–7613 | 7886–7892 | Types | +1 | −0 |
| 288 | 7615–7620 | 7894–7900 | Types | +1 | −0 |
| 289 | 7638–7643 | 7918–7924 | Types | +1 | −0 |
| 290 | 7656–7661 | 7937–7943 | Types | +1 | −0 |
| 291 | 7663–7668 | 7945–7951 | Types | +1 | −0 |
| 292 | 7773–7778 | 8056–8062 | Types | +1 | −0 |
| 293 | 7789–7794 | 8073–8079 | Types | +1 | −0 |
| 294 | 7796–7801 | 8081–8087 | Types | +1 | −0 |
| 295 | 7803–7808 | 8089–8095 | Types | +1 | −0 |
| 296 | 7810–7815 | 8097–8103 | Types | +1 | −0 |
| 297 | 7877–7894 | 8165–8187 | Types | +5 | −0 |
| 298 | 7909–7916 | 8202–8211 | Types | +2 | −0 |
| 299 | 7931–7944 | 8226–8242 | Types | +4 | −1 |
| 300 | 7963–7974 | 8261–8273 | Types | +2 | −1 |
| 301 | 7976–7992 | 8275–8294 | Types | +4 | −1 |
| 302 | 8015–8020 | 8317–8323 | Types | +1 | −0 |
| 303 | 8054–8061 | 8357–8366 | Types | +2 | −0 |
| 304 | 8063–8068 | 8368–8374 | Types | +1 | −0 |
| 305 | 8084–8091 | 8390–8399 | Types | +2 | −0 |
| 306 | 8093–8100 | 8401–8410 | Types | +2 | −0 |
| 307 | 8102–8107 | 8412–8418 | Types | +1 | −0 |
| 308 | 8122–8127 | 8433–8439 | Types | +1 | −0 |
| 309 | 8140–8147 | 8452–8461 | Types | +2 | −0 |
| 310 | 8149–8154 | 8463–8469 | Types | +1 | −0 |
| 311 | 8156–8161 | 8471–8477 | Types | +1 | −0 |
| 312 | 8221–8226 | 8537–8543 | Types | +1 | −0 |
| 313 | 8228–8235 | 8545–8554 | Types | +2 | −0 |
| 314 | 8237–8242 | 8556–8562 | Types | +1 | −0 |
| 315 | 8284–8289 | 8604–8610 | Types | +1 | −0 |
| 316 | 8340–8345 | 8661–8667 | Types | +1 | −0 |
| 317 | 8415–8420 | 8737–8743 | Types | +1 | −0 |
| 318 | 8422–8427 | 8745–8751 | Types | +1 | −0 |
| 319 | 8461–8466 | 8785–8791 | Types | +1 | −0 |
| 320 | 8482–8489 | 8807–8816 | Types | +2 | −0 |
| 321 | 8491–8496 | 8818–8824 | Types | +1 | −0 |
| 322 | 8498–8503 | 8826–8832 | Types | +1 | −0 |
| 323 | 8507–8513 | 8836–8842 | Types | +1 | −1 |
| 324 | 8520–8527 | 8849–8858 | Types | +2 | −0 |
| 325 | 8529–8536 | 8860–8869 | Types | +2 | −0 |
| 326 | 8538–8543 | 8871–8877 | Types | +1 | −0 |
| 327 | 8545–8552 | 8879–8888 | Types | +2 | −0 |
| 328 | 8594–8604 | 8930–8942 | Types | +2 | −0 |
| 329 | 8668–8673 | 9006–9012 | Types | +1 | −0 |
| 330 | 8702–8718 | 9041–9060 | Types | +4 | −1 |
| 331 | 8720–8725 | 9062–9068 | Types | +1 | −0 |
| 332 | 8727–8734 | 9070–9079 | Types | +2 | −0 |
| 333 | 8736–8741 | 9081–9087 | Types | +1 | −0 |
| 334 | 8743–8748 | 9089–9095 | Types | +1 | −0 |
| 335 | 8750–8757 | 9097–9106 | Types | +2 | −0 |
| 336 | 8759–8766 | 9108–9117 | Types | +2 | −0 |
| 337 | 8817–8822 | 9168–9174 | Types | +1 | −0 |
| 338 | 8841–8849 | 9193–9201 | Types | +2 | −2 |
| 339 | 8896–8901 | 9248–9254 | Types | +1 | −0 |
| 340 | 8910–8915 | 9263–9269 | Types | +1 | −0 |
| 341 | 8917–8924 | 9271–9280 | Types | +2 | −0 |
| 342 | 8942–8947 | 9298–9304 | Types | +1 | −0 |
| 343 | 8949–8960 | 9306–9320 | Types | +3 | −0 |
| 344 | 8969–8976 | 9329–9338 | Types | +2 | −0 |
| 345 | 8987–8992 | 9349–9355 | Types | +1 | −0 |
| 346 | 8994–8999 | 9357–9363 | Types | +1 | −0 |
| 347 | 9001–9006 | 9365–9371 | Types | +1 | −0 |
| 348 | 9008–9015 | 9373–9382 | Types | +2 | −0 |
| 349 | 9017–9022 | 9384–9390 | Types | +1 | −0 |
| 350 | 9024–9033 | 9392–9403 | Types | +2 | −0 |
| 351 | 9055–9060 | 9425–9431 | Types | +1 | −0 |
| 352 | 9062–9067 | 9433–9439 | Types | +1 | −0 |
| 353 | 9069–9076 | 9441–9450 | Types | +2 | −0 |
| 354 | 9109–9114 | 9483–9489 | Types | +1 | −0 |
| 355 | 9142–9147 | 9517–9523 | Types | +1 | −0 |
| 356 | 9170–9175 | 9546–9552 | Types | +1 | −0 |
| 357 | 9177–9184 | 9554–9563 | Types | +2 | −0 |
| 358 | 9197–9204 | 9576–9585 | Types | +2 | −0 |
| 359 | 9227–9232 | 9608–9614 | Types | +1 | −0 |
| 360 | 9234–9241 | 9616–9625 | Types | +2 | −0 |
| 361 | 9243–9248 | 9627–9633 | Types | +1 | −0 |
| 362 | 9277–9283 | 9662–9669 | Types | +2 | −1 |
| 363 | 9317–9324 | 9703–9712 | Types | +2 | −0 |
| 364 | 9326–9333 | 9714–9723 | Types | +2 | −0 |
| 365 | 9335–9340 | 9725–9731 | Types | +1 | −0 |
| 366 | 9377–9382 | 9768–9774 | Types | +1 | −0 |
| 367 | 9384–9389 | 9776–9782 | Types | +1 | −0 |
| 368 | 9391–9396 | 9784–9790 | Types | +1 | −0 |
| 369 | 9423–9443 | 9817–9841 | Types | +5 | −1 |
| 370 | 9445–9452 | 9843–9852 | Types | +2 | −0 |
| 371 | 9454–9459 | 9854–9860 | Types | +1 | −0 |
| 372 | 9490–9497 | 9891–9900 | Types | +2 | −0 |
| 373 | 9506–9511 | 9909–9915 | Types | +1 | −0 |
| 374 | 9513–9522 | 9917–9927 | Types | +2 | −1 |
| 375 | 9528–9533 | 9933–9939 | Types | +1 | −0 |
| 376 | 9600–9605 | 10006–10012 | Types | +1 | −0 |
| 377 | 9607–9612 | 10014–10020 | Types | +1 | −0 |
| 378 | 9614–9627 | 10022–10039 | Types | +4 | −0 |
| 379 | 9629–9634 | 10041–10047 | Types | +1 | −0 |
| 380 | 9636–9641 | 10049–10055 | Types | +1 | −0 |
| 381 | 9643–9648 | 10057–10063 | Types | +1 | −0 |
| 382 | 9650–9657 | 10065–10074 | Types | +2 | −0 |
| 383 | 9688–9693 | 10105–10111 | Types | +1 | −0 |
| 384 | 9702–9709 | 10120–10129 | Types | +2 | −0 |
| 385 | 9711–9718 | 10131–10140 | Types | +2 | −0 |
| 386 | 9729–9734 | 10151–10157 | Types | +1 | −0 |
| 387 | 9736–9741 | 10159–10165 | Types | +1 | −0 |
| 388 | 9780–9798 | 10204–10222 | Client | +4 | −4 |
| 389 | 9800–9810 | 10224–10234 | Client | +2 | −2 |
| 390 | 9816–9822 | 10240–10246 | Client | +1 | −1 |
| 391 | 9828–9842 | 10252–10266 | Client | +3 | −3 |
| 392 | 9844–9862 | 10268–10286 | Client | +4 | −4 |
| 393 | 9884–9890 | 10308–10314 | Client | +1 | −1 |
| 394 | 9896–9906 | 10320–10330 | Client | +2 | −2 |
| 395 | 9916–9946 | 10340–10370 | Client | +7 | −7 |
| 396 | 9948–9970 | 10372–10394 | Client | +5 | −5 |
| 397 | 9972–9978 | 10396–10402 | Client | +1 | −1 |
| 398 | 9988–9994 | 10412–10418 | Client | +1 | −1 |
| 399 | 10000–10006 | 10424–10430 | Client | +1 | −1 |
| 400 | 10016–10022 | 10440–10446 | Client | +1 | −1 |
| 401 | 10024–10030 | 10448–10454 | Client | +1 | −1 |
| 402 | 10052–10062 | 10476–10486 | Client | +2 | −2 |
| 403 | 10068–10074 | 10492–10498 | Client | +1 | −1 |
| 404 | 10084–10090 | 10508–10514 | Client | +1 | −1 |
| 405 | 10100–10110 | 10524–10534 | Client | +2 | −2 |
| 406 | 10116–10122 | 10540–10546 | Client | +1 | −1 |
| 407 | 10124–10130 | 10548–10554 | Client | +1 | −1 |
| 408 | 10132–10138 | 10556–10562 | Client | +1 | −1 |
| 409 | 10144–10150 | 10568–10574 | Client | +1 | −1 |
| 410 | 10164–10178 | 10588–10602 | Client | +3 | −3 |
| 411 | 10180–10198 | 10604–10622 | Client | +4 | −4 |
| 412 | 10200–10214 | 10624–10638 | Client | +3 | −3 |
| 413 | 10220–10226 | 10644–10650 | Client | +1 | −1 |
| 414 | 10232–10262 | 10656–10686 | Client | +7 | −7 |
| 415 | 10276–10302 | 10700–10726 | Client | +6 | −6 |
| 416 | 10304–10318 | 10728–10742 | Client | +3 | −3 |
| 417 | 10336–10354 | 10760–10778 | Client | +4 | −4 |
| 418 | 10356–10390 | 10780–10814 | Client | +8 | −8 |
| 419 | 10396–10402 | 10820–10826 | Client | +1 | −1 |
| 420 | 10432–10438 | 10856–10862 | Client | +1 | −1 |
| 421 | 10456–10474 | 10880–10898 | Client | +4 | −4 |
| 422 | 10476–10486 | 10900–10910 | Client | +2 | −2 |
| 423 | 10488–10506 | 10912–10930 | Client | +4 | −4 |
| 424 | 10508–10516 | 10932–10940 | Client | +2 | −2 |

---

## Unified diff

`````diff
--- smartsheet/old/ballerinax_smartsheet.bal.txt	2026-08-12 12:57:30
+++ smartsheet/new/ballerinax_smartsheet.bal.txt	2026-08-12 13:19:19
@@ -230,11 +230,11 @@
     string url?;
 };
 
-// Unknown type: TimestampDateTime
+type TimestampDateTime string;
 
-// Unknown type: TimestampNumber
+type TimestampNumber decimal;
 
-type Timestamp ballerinax/smartsheet:1.0.2:TimestampDateTime|ballerinax/smartsheet:1.0.2:TimestampNumber;
+type Timestamp TimestampDateTime|TimestampNumber;
 
 
 type Discussion record {
@@ -356,7 +356,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -367,10 +367,13 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the sheet row containing the discussion. (this property is included only if the discussion is on a sheet row)
+    @constraint:Int {minValue: 0}
     int sheetRowId?;
     # Id of the sheet the discussion is on. (This property is included only if the `workspaceId` property below isn't included)
+    @constraint:Int {minValue: 0}
     int sheetId?;
     # Id of the workspace the discussion is directly on. (This property is included only if the `sheetId` property above isn't included)
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -393,10 +396,12 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the sheet that contains the attachment. (This property is included only if the `workspaceId` property below isn't included)
+    @constraint:Int {minValue: 0}
     int sheetId?;
     # Name of the compressed file containing the multiple attachments downloaded at once. (Only included if more than one attachment was selected to be downloaded in the same user action. Please notice that multi-attachment download action allows the user to specify the name of the zip file that shoud include all attachments, which is what is being provided here. The download of a single attachment uses the attachment name as the download file name and it cannot be changed, and it isn't provided in this event because it is provided in the ATTACHMENT-CREATE event or by querying Smartsheet API with the attachment ID)
     string multiFileDownloadName?;
     # Id of the workspace that directly contains the attachment. (This property is included only if the `sheetId` property above isn't included)
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -449,12 +454,13 @@
 };
 
 # Specifies the recipient of an email. The recipient may be either an individual or a group. To specify an individual, set the email attribute; to specify a group, set the groupId attribute. Either email and groupId may be set, but not both
-type Recipient ballerinax/smartsheet:1.0.2:RecipientIndividual|ballerinax/smartsheet:1.0.2:RecipientGroup;
+type Recipient RecipientIndividual|RecipientGroup;
 
 # Represents the Headers record for the operation: reactivate-user
 
 type ReactivateUserHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -462,8 +468,10 @@
 
 type RowsSortHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -478,6 +486,7 @@
 
 type DeleteWebhookHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -485,10 +494,14 @@
 
 type DeleteAlternateEmailHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
-// Unknown type: ReadOnlyFullShowToolbar
+# **Deprecated** Indicates whether the left nav toolbar is displayed. The default, or **true**, is to display the toolbar. If **false**, hides the toolbar
+# 
+@deprecated
+type ReadOnlyFullShowToolbar boolean;
 
 
 type WebhookListData record {
@@ -511,11 +524,14 @@
     Permalink permalink?;
 };
 
-// Unknown type: Name
+# Sheet name
+type Name string;
 
-// Unknown type: Id
+# Sheet Id
+type Id decimal;
 
-// Unknown type: Permalink
+# URL that represents a direct link to the sheet in Smartsheet
+type Permalink string;
 
 
 type WebhookListResponse record {
@@ -531,8 +547,10 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the new dashboard owner
+    @constraint:Int {minValue: 0}
     int newUserId?;
     # Id of the former dashboard owner
+    @constraint:Int {minValue: 0}
     int oldUserId?;
     # New access level of the former owner: `"ADMIN"`
     "ADMIN" oldAccessLevel?;
@@ -545,9 +563,9 @@
     decimal objectId?;
 };
 
-// Unknown type: FavoritesOneOf2
+type FavoritesOneOf2 Favorite[];
 
-type FavoritesBody ballerinax/smartsheet:1.0.2:Favorite|ballerinax/smartsheet:1.0.2:FavoritesOneOf2;
+type FavoritesBody Favorite|FavoritesOneOf2;
 
 # Represents the Queries record for the operation: attachments-listOnSheet
 
@@ -782,19 +800,22 @@
 };
 
 # The base object for values found in the **Cell.objectValue** attribute. Its **objectType** attribute indicates the type of the object. This object itself is not used directly
-type ObjectValue ballerinax/smartsheet:1.0.2:AbstractDatetimeObjectValue|ballerinax/smartsheet:1.0.2:CheckboxObjectValue|ballerinax/smartsheet:1.0.2:ContactObjectValue|ballerinax/smartsheet:1.0.2:DateObjectValue|ballerinax/smartsheet:1.0.2:DatetimeObjectValue|ballerinax/smartsheet:1.0.2:DurationObjectValue|ballerinax/smartsheet:1.0.2:MultiContactObjectValue|ballerinax/smartsheet:1.0.2:MultiPicklistObjectValue|ballerinax/smartsheet:1.0.2:PredecessorList;
+type ObjectValue AbstractDatetimeObjectValue|CheckboxObjectValue|ContactObjectValue|DateObjectValue|DatetimeObjectValue|DurationObjectValue|MultiContactObjectValue|MultiPicklistObjectValue|PredecessorList;
 
 
 type AttachmentSendAdditionalDetails record {
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the sheet that contains the attachment. (This property is included only if the `workspaceId` property below isn't included)
+    @constraint:Int {minValue: 0}
     int sheetId?;
     # Single ID of a user group explicitly included in the recipient list. (This property is included only if the `recipientEmail` property above isn't included)
+    @constraint:Int {minValue: 0}
     int recipientGroupId?;
     # Single email address either of a user explicitly included in the recipient list or of the sender (when *CC sender* is requested). (This property is included only if the recipientGroupId property below isn't included)
     string recipientEmail?;
     # Id of the workspace that directly contains the attachment. (This property is included only if the `sheetId` property above isn't included)
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -903,7 +924,8 @@
     string suffix?;
 };
 
-// Unknown type: Columns
+# An array of Column objects, each defining the properties and configuration of a column in a sheet. See the Column schema for details on individual column attributes
+type Columns Column[];
 
 # Sheet created from template
 
@@ -967,8 +989,10 @@
 
 type UpdaterequestsCreateHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -976,8 +1000,10 @@
 
 type AutomationruleUpdateHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -988,8 +1014,10 @@
     # The source object used to create the dashboard, currently only 'global_template' is valid
     string sourceType?;
     # Id of the global template that was used to create the dashboard. (Specific to `Create New` actions)
+    @constraint:Int {minValue: 0}
     int sourceGlobalTemplateId?;
     # Id of the source dashboard. (Specific to `Save As New` actions). 
+    @constraint:Int {minValue: 0}
     int sourceObjectId?;
     # Name of the newly created dashboard
     string dashboardName?;
@@ -1016,6 +1044,7 @@
     # Maximum number of events to return as response to this call.
 Must be between 1 through 10,000 (inclusive).
 Defaults to 1,000 if not specified
+    @constraint:Int {minValue: 1, maxValue: 10000}
     int maxCount?;
     # The earliest time from which events are included in the response. Events before this time are excluded. This field is intended for use when backfilling data at client startup or recovery--don't use it for fine-grained date-based queries. Therefore, resolution is limited to the nearest hour. The value is interpreted as ISO-8601 format, unless `numericDates` is specified (see details about `numericDates` below).
 
@@ -1027,6 +1056,7 @@
 
 type AttachmentsListOnSheetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -1130,7 +1160,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -1146,6 +1176,7 @@
 
 type ShareReportGetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -1153,6 +1184,7 @@
 
 type GetSheetPublishHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -1173,8 +1205,10 @@
 
 type ProofsCreateHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -1259,7 +1293,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -1275,7 +1309,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -1291,7 +1325,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -1302,10 +1336,13 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the group that the user was removed from
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of user that was removed from the group
+    @constraint:Int {minValue: 0}
     int userId?;
     # Id of the workspace that the group is shared to. (Specific to cases where the sheet is shared to the group via a workspace's sharing list)
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -1364,7 +1401,7 @@
     string email?;
 };
 
-// Unknown type: ReportsreportIdsharesOneOf2
+type ReportsreportIdsharesOneOf2 Share[];
 
 
 type GroupRename record {
@@ -1376,7 +1413,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -1425,6 +1462,7 @@
     # Row Id
     decimal id?;
     # Row number within the sheet
+    @constraint:Number {minValue: 1}
     decimal rowNumber?;
 };
 
@@ -1453,6 +1491,7 @@
     # Row Id
     decimal id?;
     # Row number within the sheet
+    @constraint:Number {minValue: 1}
     decimal rowNumber?;
 };
 
@@ -1466,13 +1505,14 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
 };
 
-// Unknown type: PropertiesOptions
+# When applicable for PICKLIST column type. Array of the options available for the field
+type PropertiesOptions string[];
 
 
 type DashboardSaveAsNew record {
@@ -1484,7 +1524,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -1544,12 +1584,15 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the parent container of the report. (Specific to move events where a folder containing the report is moved to a folder in a different workspace, indicates that the report has moved to a new workspace but is still within the same folder)
+    @constraint:Int {minValue: 0}
     int parentContainerId?;
     # Id of the destination folder for the move event. (Specific to actions where the report was moved to a different folder)
+    @constraint:Int {minValue: 0}
     int newParentContainerId?;
     # Name of the destination folder for the move event. (Specific to actions where the report was moved to a different folder)
     string folderName?;
     # Id of the workspace the report is currently in. If the move was between two workspaces the `workspaceId` will be the Id of the destination workspace
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -1581,7 +1624,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -1592,6 +1635,7 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the form's sheet
+    @constraint:Int {minValue: 0}
     int sheetId?;
 };
 
@@ -1650,23 +1694,29 @@
     Primary primary?;
 };
 
-// Unknown type: Symbol
+# When applicable for **CHECKBOX** or **PICKLIST** column types. See [Symbol Columns](/api/smartsheet/openapi/columns)
+type Symbol string;
 
-// Unknown type: ContactOptions
+# Array of ContactOption objects to specify a pre-defined list of values for the column. Column **type** must be **CONTACT_LIST**
+type ContactOptions ContactOption[];
 
-// Unknown type: Options
+# Array of the options available for the column
+type Options string[];
 
-// Unknown type: Width
+# Display width of the column in pixels
+type Width decimal;
 
 # See [System Columns](/api/smartsheet/openapi/columns)
 type SystemColumnType "AUTO_NUMBER"|"CREATED_BY"|"CREATED_DATE"|"MODIFIED_BY"|"MODIFIED_DATE";
 
-// Unknown type: Title
+# Column title
+type Title string;
 
 # See [Column Types](/api/smartsheet/openapi/columns)
 type Type "ABSTRACT_DATETIME"|"CHECKBOX"|"CONTACT_LIST"|"DATE"|"DATETIME"|"DURATION"|"MULTI_CONTACT_LIST"|"MULTI_PICKLIST"|"PICKLIST"|"PREDECESSOR"|"TEXT_NUMBER";
 
-// Unknown type: Primary
+# Returned only if the column is the Primary Column (value = **true**)
+type Primary boolean;
 
 # Sheet to create from template
 
@@ -1677,7 +1727,7 @@
     decimal fromId?;
 };
 
-type SheetsBody ballerinax/smartsheet:1.0.2:SheetToCreate|ballerinax/smartsheet:1.0.2:SheetToCreateFromTemplate;
+type SheetsBody SheetToCreate|SheetToCreateFromTemplate;
 
 
 type ShareCreateData record {
@@ -1700,8 +1750,10 @@
 
 type IsFavoriteHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # UserId of the user
+    @http:Header {name: "x-smar-sc-actor-id"}
     string xSmarScActorId?;
 };
 
@@ -1806,10 +1858,11 @@
     # Working days for a project sheet
     ("MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY"|"SATURDAY"|"SUNDAY")[] workingDays?;
     # Length of a workday for a project sheet
+    @constraint:Number {minValue: 1, maxValue: 24}
     decimal lengthOfDay?;
 };
 
-// Unknown type: WorkspacesworkspaceIdsharesOneOf2
+type WorkspacesworkspaceIdsharesOneOf2 Share[];
 
 
 type SheetSendRowAdditionalDetails record {
@@ -1818,8 +1871,10 @@
     # Indicates whether the row(s) were sent with their respective attachments
     boolean includeAttachments?;
     # Number of rows sent
+    @constraint:Int {minValue: 1}
     int rowCount?;
     # Single ID of a user group explicitly included in the recipient list. (This property is included only if the `recipientEmail` property above isn't included)
+    @constraint:Int {minValue: 0}
     int recipientGroupId?;
     # Single email address either of a user explicitly included in the recipient list or of the sender (when *CC sender* is requested). (This property is included only if the `recipientGroupId` property below isn't included)
     string recipientEmail?;
@@ -1838,9 +1893,9 @@
     decimal page?;
 };
 
-// Unknown type: SheetssheetIdsharesOneOf2
+type SheetssheetIdsharesOneOf2 Share[];
 
-type SheetIdSharesBody ballerinax/smartsheet:1.0.2:Share|ballerinax/smartsheet:1.0.2:SheetssheetIdsharesOneOf2;
+type SheetIdSharesBody Share|SheetssheetIdsharesOneOf2;
 
 
 type SearchResult record {
@@ -1877,14 +1932,17 @@
     boolean numericDates?;
 };
 
-// Unknown type: Validation
+# Indicates whether summary field values are restricted to the type
+type Validation boolean;
 
 # Represents the Headers record for the operation: getSheet
 
 type GetSheetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # The Accept request-header field can be used to specify certain media types which are acceptable for the response
+    @http:Header {name: "Accept"}
     string accept?;
 };
 
@@ -1892,6 +1950,7 @@
 
 type GetSightPublishStatusHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -1909,8 +1968,10 @@
 
 type CommentsCreateHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -1937,7 +1998,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -1948,6 +2009,7 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # The ID of the user who owns this token
+    @constraint:Int {minValue: 0}
     int tokenUserId?;
     # Four or more characters used as a mnemonic to represent this access token. Even though this value serves as a visual token differentiator, this value isn't an Id because it isn't guaranteed to be unique across all tokens. This value is the same displayed by Smartsheet UI for each access token listed under Apps & Integrations > API Access
     string tokenDisplayValue?;
@@ -1957,19 +2019,26 @@
 
 type ProofsDeleteVersionHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
-// Unknown type: ReadWriteShowToolbar
+# **Deprecated** Indicates whether the left nav toolbar is displayed. The default, or **true**, is to display the toolbar. If **false**, hides the toolbar
+# 
+@deprecated
+type ReadWriteShowToolbar boolean;
 
 # Represents the Headers record for the operation: add-favorite
 
 type AddFavoriteHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # UserId of the user
+    @http:Header {name: "x-smar-sc-actor-id"}
     string xSmarScActorId?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -1977,6 +2046,7 @@
 
 type GetCurrentUserHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -1984,6 +2054,7 @@
 
 type AttachmentsVersionsDeleteHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -1997,7 +2068,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2013,16 +2084,19 @@
     boolean sendCompletionEmail?;
 };
 
-type TimestampWriteable ballerinax/smartsheet:1.0.2:TimestampDateTime|ballerinax/smartsheet:1.0.2:TimestampNumber;
+type TimestampWriteable TimestampDateTime|TimestampNumber;
 
-// Unknown type: Locked
+# Indicates whether the field is locked
+type Locked boolean;
 
 # Represents the Headers record for the operation: copy-workspace
 
 type CopyWorkspaceHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -2051,10 +2125,13 @@
 Note that this access level represents the access level granted by this specific sharing action; it is not the group or user's effective access level for the dashboard
     "VIEWER"|"EDITOR"|"EDITOR_SHARE"|"ADMIN" accessLevel?;
     # Id of the group that the workspace was shared to. (Specific to share to group actions)
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that the workspace was shared to. (Specific to share to user actions)
+    @constraint:Int {minValue: 0}
     int userId?;
     # Id of the workspace that was shared to the group or user
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -2259,6 +2336,7 @@
     # Indicates whether the row is locked
     boolean locked?;
     # Row number within the sheet
+    @constraint:Number {minValue: 1}
     decimal rowNumber?;
     # Sibling Id
     decimal siblingId?;
@@ -2509,20 +2587,25 @@
 
 type TokensGetOrRefreshQueries record {
     # refresh_token value that came with the access token
+    @http:Query {name: "refresh_token"}
     string refreshToken?;
     # Authorization code acquired after user selects "Allow" in the Web login UI
     string code?;
     # Must be set to "authorization_code"
+    @http:Query {name: "grant_type"}
     "authorization_code"|"refresh_token" grantType;
     # (Optional) Must use either this value or hash. Plain text method for sending this value. For example, client_secret={app_secret}. Encryption occurs at the HTTPS level
+    @http:Query {name: "client_secret"}
     string clientSecret?;
     # The client Id you obtained when you registered your app
+    @http:Query {name: "client_id"}
     string clientId;
     # (Optional) Must use either this value or client_secret. SHA-256 hash of your app secret concatenated with a pipe and the authorization code. For example, hash={SHA_256(app_secret|code)}
     string hash?;
     # **Deprecated** If supplied, must match the redirect URI you registered for your app
 
     @deprecated
+    @http:Query {name: "redirect_url"}
     string redirectUrl?;
 };
 
@@ -2548,7 +2631,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2582,7 +2665,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2608,7 +2691,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2624,7 +2707,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2640,7 +2723,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2656,7 +2739,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2672,7 +2755,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2688,7 +2771,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2704,7 +2787,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2720,7 +2803,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2731,8 +2814,10 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the former main contact
+    @constraint:Int {minValue: 0}
     int oldContactUserId?;
     # Id of the new main contact
+    @constraint:Int {minValue: 0}
     int newContactUserId?;
 };
 
@@ -2746,7 +2831,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2757,10 +2842,12 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the sheet that contains the attachment. (This property is included only if the `workspaceId` property below isn't included)
+    @constraint:Int {minValue: 0}
     int sheetId?;
     # Name of the attachment
     string attachmentName?;
     # Id of the workspace that directly contains the attachment. (This property is included only if the `sheetId` property above isn't included)
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -2774,7 +2861,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2785,8 +2872,10 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the sheet that contains the attachment. (This property is included only if the `workspaceId` property below isn't included)
+    @constraint:Int {minValue: 0}
     int sheetId?;
     # Id of the workspace that directly contains the attachment. (This property is included only if the `sheetId` property above isn't included)
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -2800,7 +2889,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2816,7 +2905,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2832,7 +2921,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2848,7 +2937,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2876,7 +2965,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2891,10 +2980,13 @@
 Note that this access level represents the access level that has been granted to the user via group membership; it is not the user's effective access level for the dashboard
     "VIEWER"|"EDITOR"|"EDITOR_SHARE"|"ADMIN" accessLevel?;
     # Id of the group the user was added to
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that was added to the group
+    @constraint:Int {minValue: 0}
     int userId?;
     # Id of the workspace that the group is shared to. (Specific to cases where the dashboard is shared to the group via a workspace's sharing list)
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -2908,7 +3000,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2923,8 +3015,10 @@
 Note that this access level represents the access level granted by this specific sharing action; it is not the group or user's effective access level for the dashboard
     "VIEWER"|"EDITOR"|"EDITOR_SHARE"|"ADMIN" accessLevel?;
     # Id of the group that was added to the dashboard's sharing list. (Specific to share to group actions)
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that was added to the dashboard's sharing list. (Specific to share to user actions)
+    @constraint:Int {minValue: 0}
     int userId?;
 };
 
@@ -2938,7 +3032,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2953,7 +3047,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2969,7 +3063,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -2985,7 +3079,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3001,7 +3095,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3012,12 +3106,15 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the parent container of the dashboard. (Specific to move events where a folder containing the dashboard is moved to a folder in a different workspace, indicates that the dashboard has moved to a new workspace but is still within the same folder)
+    @constraint:Int {minValue: 0}
     int parentContainerId?;
     # Id of the destination folder for the move event. (Specific to actions where the dashboard was moved to a different folder)
+    @constraint:Int {minValue: 0}
     int newParentContainerId?;
     # Name of the destination folder for the move event. (Specific to actions where the dashboard was moved to a different folder)
     string folderName?;
     # Id of the workspace the dashboard is currently in. If the move was between two workspaces the `workspaceId` will be the Id of the destination workspace
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -3031,7 +3128,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3047,7 +3144,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3063,7 +3160,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3074,8 +3171,10 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the group that was removed from the dashboard's sharing list. (Specific to remove share from group actions)
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that was removed from the dashboard's sharing list. (Specific to remove share from user actions)
+    @constraint:Int {minValue: 0}
     int userId?;
 };
 
@@ -3089,7 +3188,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3100,10 +3199,13 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the group that the user was removed from
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of user that was removed from the group
+    @constraint:Int {minValue: 0}
     int userId?;
     # Id of the workspace that the group is shared to. (Specific to cases where the dashboard is shared to the group via a workspace's sharing list)
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -3117,7 +3219,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3128,10 +3230,13 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the group that was removed from the workspace. (Specific to remove share from group actions)
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that was removed from the workspace. (Specific to remove share from user actions)
+    @constraint:Int {minValue: 0}
     int userId?;
     # Id of the workspace the group or user was removed from
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -3145,7 +3250,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3161,7 +3266,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3177,7 +3282,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3193,7 +3298,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3209,7 +3314,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3225,7 +3330,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3238,14 +3343,18 @@
     # Indicates whether the discussion was sent with its respective attachments
     boolean includeAttachments?;
     # Id of the sheet row containing the discussion. (this property is included only if the discussion is on a sheet row)
+    @constraint:Int {minValue: 0}
     int sheetRowId?;
     # Id of the sheet the discussion is on. (This property is included only if the `workspaceId` property below isn't included)
+    @constraint:Int {minValue: 0}
     int sheetId?;
     # Single ID of a user group explicitly included in the recipient list. (This property is included only if the `recipientEmail` property above isn't included)
+    @constraint:Int {minValue: 0}
     int recipientGroupId?;
     # Single email address either of a user explicitly included in the recipient list or of the sender (when *CC sender* is requested). (This property is included only if the `recipientGroupId` property below isn't included)
     string recipientEmail?;
     # Id of the workspace the discussion is directly on. (This property is included only if the `sheetId` property above isn't included)
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -3259,7 +3368,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3272,16 +3381,21 @@
     # Indicates whether the discussion comment (or discussion comment reply) was sent with its respective attachments
     boolean includeAttachments?;
     # Id of the sheet row containing the discussion. (this property is included only if the discussion is on a sheet row)
+    @constraint:Int {minValue: 0}
     int sheetRowId?;
     # Id of the comment
+    @constraint:Int {minValue: 0}
     int commentId?;
     # Id of the sheet the discussion is on. (This property is included only if the `workspaceId` property below isn't included)
+    @constraint:Int {minValue: 0}
     int sheetId?;
     # Single ID of a user group explicitly included in the recipient list. (This property is included only if the `recipientEmail` property above isn't included)
+    @constraint:Int {minValue: 0}
     int recipientGroupId?;
     # Single email address either of a user explicitly included in the recipient list or of the sender (when *CC sender* is requested). (This property is included only if the `recipientGroupId` property below isn't included)
     string recipientEmail?;
     # Id of the workspace the discussion is directly on. (This property is included only if the `sheetId` property above isn't included)
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -3295,7 +3409,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3311,7 +3425,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3322,6 +3436,7 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of folder that was copied to create the new folder. (Only included if the folder was created as a result of a *save as new* or *copy*)
+    @constraint:Int {minValue: 0}
     int sourceFolderId?;
     # Name of the destination folder for the move event. (Specific to actions where the folder was moved to a different folder)
     string folderName?;
@@ -3337,7 +3452,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3361,7 +3476,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3387,7 +3502,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3403,7 +3518,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3419,7 +3534,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3435,7 +3550,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3448,6 +3563,7 @@
     # Name of the form
     string formName?;
     # Id of the form's sheet
+    @constraint:Int {minValue: 0}
     int sheetId?;
 };
 
@@ -3461,7 +3577,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3477,7 +3593,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3493,7 +3609,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3504,6 +3620,7 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the user that was added to the group
+    @constraint:Int {minValue: 0}
     int memberUserId?;
 };
 
@@ -3526,7 +3643,8 @@
     string email?;
 };
 
-// Unknown type: GroupMembersAddArray
+# An array of GroupMemberAdd objects, each specifying the email address of a user to be added to a group
+type GroupMembersAddArray GroupMemberAdd[];
 
 
 type GroupDelete record {
@@ -3538,7 +3656,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3554,7 +3672,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3570,7 +3688,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3581,6 +3699,7 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the user that was removed from the group
+    @constraint:Int {minValue: 0}
     int memberUserId?;
 };
 
@@ -3594,7 +3713,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3605,8 +3724,10 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the former group owner
+    @constraint:Int {minValue: 0}
     int oldOwnerUserId?;
     # Id of the new group owner
+    @constraint:Int {minValue: 0}
     int newOwnerUserId?;
 };
 
@@ -3635,7 +3756,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3650,8 +3771,10 @@
 Note that this access level represents the access level granted by this specific sharing action; it is not the group or user's effective access level for the report
     "VIEWER"|"EDITOR"|"EDITOR_SHARE"|"ADMIN" accessLevel?;
     # Id of the group that was added to the report's sharing list. (Specific to share to group actions)
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that was added to the report's sharing list. (Specific to share to user actions)
+    @constraint:Int {minValue: 0}
     int userId?;
 };
 
@@ -3665,7 +3788,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3680,10 +3803,13 @@
 Note that this access level represents the access level that has been granted to the user via group membership; it is not the user's effective access level for the report
     "VIEWER"|"EDITOR"|"EDITOR_SHARE"|"ADMIN" accessLevel?;
     # Id of the group the user was added to
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that was added to the group
+    @constraint:Int {minValue: 0}
     int userId?;
     # Id of the workspace that the group is shared to. (Specific to cases where the report is shared to the group via a workspace's sharing list)
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -3697,7 +3823,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3712,10 +3838,13 @@
 Note that this access level represents the access level granted by this specific sharing action; it is not the group or user's effective access level for the report
     "VIEWER"|"EDITOR"|"EDITOR_SHARE"|"ADMIN" accessLevel?;
     # Id of the group that the workspace was shared to. (Specific to share to group actions)
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that the workspace was shared to. (Specific to share to user actions)
+    @constraint:Int {minValue: 0}
     int userId?;
     # Id of the workspace that was shared to the group or user
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -3729,7 +3858,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3744,8 +3873,10 @@
     # Type of object used to create the new report
     "report"|"globale_template" sourceType?;
     # Id of report that was copied to create the new report. (Only included if the report was created as a result of a *copy* or *save as new*)
+    @constraint:Int {minValue: 0}
     int sourceObjectId?;
     # Id of the global template that was used to create the new report (Only included if the report was created using a global template. "New Blank Report" is a global template)
+    @constraint:Int {minValue: 0}
     int sourceGlobalTemplateId?;
 };
 
@@ -3759,7 +3890,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3775,7 +3906,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3799,7 +3930,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3815,7 +3946,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3831,7 +3962,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3842,8 +3973,10 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the group that was added to the report's sharing list. (Specific to share to group actions)
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that was added to the report's sharing list. (Specific to share to user actions)
+    @constraint:Int {minValue: 0}
     int userId?;
 };
 
@@ -3857,7 +3990,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3868,10 +4001,13 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the group that the user was removed from
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of user that was removed from the group
+    @constraint:Int {minValue: 0}
     int userId?;
     # Id of the workspace that the group is shared to. (Specific to cases where the report is shared to the group via a workspace's sharing list)
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -3885,7 +4021,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3901,7 +4037,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3927,7 +4063,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3943,7 +4079,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3959,7 +4095,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -3970,6 +4106,7 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Single ID of a user group explicitly included in the recipient list. (This property is included only if the `recipientEmail` property above isn't included)
+    @constraint:Int {minValue: 0}
     int recipientGroupId?;
     # The format in which the report was sent
     "excel"|"pdf"|"pdf_gantt"|"pdf_calendar" formatType?;
@@ -3987,7 +4124,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4000,8 +4137,10 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the new owner
+    @constraint:Int {minValue: 0}
     int newUserId?;
     # Id of the former owner
+    @constraint:Int {minValue: 0}
     int oldUserId?;
     # New access level of the former owner: `"ADMIN"`
     "ADMIN" oldAccessLevel?;
@@ -4017,7 +4156,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4033,7 +4172,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4048,8 +4187,10 @@
 Note that this access level represents the access level granted by this specific sharing action; it is not the group or user's effective access level for the sheet
     "VIEWER"|"EDITOR"|"EDITOR_SHARE"|"ADMIN" accessLevel?;
     # Id of the group that was added to the sheet's sharing list. (Specific to share to group actions)
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that was added to the sheet's sharing list. (Specific to share to user actions)
+    @constraint:Int {minValue: 0}
     int userId?;
 };
 
@@ -4063,7 +4204,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4078,10 +4219,13 @@
 Note that this access level represents the access level that has been granted to the user via group membership; it is not the user's effective access level for the sheet
     "VIEWER"|"EDITOR"|"EDITOR_SHARE"|"ADMIN" accessLevel?;
     # Id of the group the user was added to
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that was added to the group
+    @constraint:Int {minValue: 0}
     int userId?;
     # Id of the workspace that the group is shared to. (Specific to cases where the sheet is shared to the group via a workspace's sharing list)
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -4095,7 +4239,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4110,10 +4254,13 @@
 Note that this access level represents the access level granted by this specific sharing action; it is not the group or user's effective access level for the sheet
     "VIEWER"|"EDITOR"|"EDITOR_SHARE"|"ADMIN" accessLevel?;
     # Id of the group that the workspace was shared to. (Specific to share to group actions)
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that the workspace was shared to. (Specific to share to user actions)
+    @constraint:Int {minValue: 0}
     int userId?;
     # Id of the workspace that was shared to the group or user
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -4127,7 +4274,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4138,12 +4285,15 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Number of rows copied
+    @constraint:Int {minValue: 1}
     int rowsCopied?;
     # Indicates whether the row(s) were copied with their respective attachments
     boolean includeAttachments?;
     # Id of sheet from where the rows copied. (Only included when the `objectId` property contains the Id of the destination sheet)
+    @constraint:Int {minValue: 0}
     int sourceSheetId?;
     # Id of sheet to where the rows copied. (Only included when the `objectId` property contains the Id of the source sheet)
+    @constraint:Int {minValue: 0}
     int destinationSheetId?;
     # Indicates whether the row(s) were copied with their respective discussion comments
     boolean includeDiscussions?;
@@ -4159,7 +4309,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4173,10 +4323,13 @@
     string sheetName?;
     "sheet"|"template"|"globale_template"|"import" sourceType?;
     # Id of the template used to create the sheet. (Only included if the sheet was created using a template, that is not a global template)
+    @constraint:Int {minValue: 0}
     int sourceTemplateId?;
     # Id of sheet that was copied to create the new sheet. (Only included if the sheet was created as a result of a *copy* or *save as new*)
+    @constraint:Int {minValue: 0}
     int sourceObjectId?;
     # Id of the global template that was used to create the new sheet (Only included if the sheet was created using a global template)
+    @constraint:Int {minValue: 0}
     int sourceGlobalTemplateId?;
 };
 
@@ -4190,7 +4343,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4201,6 +4354,7 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of sheet referenced by the cell link
+    @constraint:Int {minValue: 0}
     int cellLinkSourceSheetId?;
 };
 
@@ -4214,7 +4368,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4230,7 +4384,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4254,7 +4408,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4270,7 +4424,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4281,12 +4435,15 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the parent container of the sheet. (Specific to move events where a folder containing the sheet is moved to a folder in a different workspace, indicates that the sheet has moved to a new workspace but is still within the same folder)
+    @constraint:Int {minValue: 0}
     int parentContainerId?;
     # Id of the destination folder for the move event. (Specific to actions where the sheet was moved to a different folder)
+    @constraint:Int {minValue: 0}
     int newParentContainerId?;
     # Name of the destination folder for the move event. (Specific to actions where the sheet was moved to a different folder)
     string folderName?;
     # Id of the workspace the sheet is currently in. If the move was between two workspaces the `workspaceId` will be the Id of the destination workspace
+    @constraint:Int {minValue: 0}
     int workspaceId?;
 };
 
@@ -4300,7 +4457,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4313,10 +4470,13 @@
     # Indicates whether the row(s) were moved with their respective attachments
     boolean includeAttachments?;
     # Id of sheet from where the rows moved. (Only included when the `objectId` property contains the Id of the destination sheet)
+    @constraint:Int {minValue: 0}
     int sourceSheetId?;
     # Number of rows moved
+    @constraint:Int {minValue: 1}
     int rowsMoved?;
     # Id of sheet to where the rows moved. (Only included when the `objectId` property contains the Id of the source sheet)
+    @constraint:Int {minValue: 0}
     int destinationSheetId?;
     # Indicates whether the row(s) were moved with their respective discussion comments
     boolean includeDiscussions?;
@@ -4332,7 +4492,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4348,7 +4508,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4359,8 +4519,10 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the group that was removed from the sheet's sharing list. (Specific to remove share from group actions)
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that was removed from the sheet's sharing list. (Specific to remove share from user actions)
+    @constraint:Int {minValue: 0}
     int userId?;
 };
 
@@ -4374,7 +4536,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4390,7 +4552,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4416,7 +4578,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4432,7 +4594,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4448,7 +4610,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4464,7 +4626,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4480,7 +4642,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4491,6 +4653,7 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Single ID of a user group explicitly included in the recipient list. (This property is included only if the `recipientEmail` property above isn't included)
+    @constraint:Int {minValue: 0}
     int recipientGroupId?;
     # The format in which the sheet was sent
     "excel"|"pdf"|"pdf_gantt"|"pdf_calendar" formatType?;
@@ -4508,7 +4671,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4524,7 +4687,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4540,7 +4703,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4553,8 +4716,10 @@
     # Indicates whether the row(s) were sent with their respective attachments
     boolean includeAttachments?;
     # Id of the sheet that owns the rows sent in the update request
+    @constraint:Int {minValue: 0}
     int sheetId?;
     # Number of rows sent in the update request
+    @constraint:Int {minValue: 1}
     int rowCount?;
     # Indicates whether the row(s) were sent with their respective discussion comments
     boolean includeDiscussions?;
@@ -4570,7 +4735,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4586,7 +4751,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4612,7 +4777,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4635,7 +4800,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4651,7 +4816,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4667,7 +4832,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4683,7 +4848,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4699,7 +4864,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4715,7 +4880,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4731,7 +4896,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4747,7 +4912,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4763,7 +4928,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4779,7 +4944,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4794,8 +4959,10 @@
 Note that this access level represents the access level granted by this specific sharing action; it is not the group or user's effective access level for the workspace
     "VIEWER"|"EDITOR"|"EDITOR_SHARE"|"ADMIN" accessLevel?;
     # Id of the group that was added to the workspace's sharing list. (Specific to share to group actions)
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that was added to the workspace's sharing list. (Specific to share to user actions)
+    @constraint:Int {minValue: 0}
     int userId?;
 };
 
@@ -4809,7 +4976,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4824,8 +4991,10 @@
 Note that this access level represents the access level that has been granted to the user via group membership; it is not the user's effective access level for the workspace
     "VIEWER"|"EDITOR"|"EDITOR_SHARE"|"ADMIN" accessLevel?;
     # Id of the group the user was added to
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that was added to the group
+    @constraint:Int {minValue: 0}
     int userId?;
 };
 
@@ -4839,7 +5008,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4850,6 +5019,7 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of workspace that was copied to create the new workspace. (Only included if the workspace was created as a result of a *save as new* or *copy*)
+    @constraint:Int {minValue: 0}
     int sourceWorkspaceId?;
     # Name of the workspace
     string workspaceName?;
@@ -4865,7 +5035,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4881,7 +5051,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4897,7 +5067,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4913,7 +5083,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4937,7 +5107,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4948,8 +5118,10 @@
     # Email address of the user responsible for the event
     string emailAddress;
     # Id of the group that was removed from the workspace's sharing list. (Specific to remove share from group actions)
+    @constraint:Int {minValue: 0}
     int groupId?;
     # Id of the user that was removed from the workspace's sharing list. (Specific to remove share from user actions)
+    @constraint:Int {minValue: 0}
     int userId?;
 };
 
@@ -4963,7 +5135,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -4979,7 +5151,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -5005,7 +5177,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -5021,7 +5193,7 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
@@ -5037,13 +5209,13 @@
     string eventId?;
     string accessTokenName?;
     decimal requestUserId?;
-    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" source?;
+    "WEB_APP"|"MOBILE_IOS"|"MOBILE_ANDROID"|"API_UNDEFINED_APP"|"API_INTEGRATED_APP"|"API_ODBC_DRIVER" 'source?;
     decimal userId?;
     string objectId?;
     string eventTimestamp?;
 };
 
-type EventUnionData ballerinax/smartsheet:1.0.2:AccesstokenAuthorize|ballerinax/smartsheet:1.0.2:AccesstokenRefresh|ballerinax/smartsheet:1.0.2:AccesstokenRevoke|ballerinax/smartsheet:1.0.2:AccountBulkUpdate|ballerinax/smartsheet:1.0.2:AccountDownloadLoginHistory|ballerinax/smartsheet:1.0.2:AccountDownloadPublishedItemsReport|ballerinax/smartsheet:1.0.2:AccountDownloadSheetAccessReport|ballerinax/smartsheet:1.0.2:AccountDownloadUserList|ballerinax/smartsheet:1.0.2:AccountImportUsers|ballerinax/smartsheet:1.0.2:AccountListSheets|ballerinax/smartsheet:1.0.2:AccountRename|ballerinax/smartsheet:1.0.2:AccountUpdateMainContact|ballerinax/smartsheet:1.0.2:AttachmentCreate|ballerinax/smartsheet:1.0.2:AttachmentDelete|ballerinax/smartsheet:1.0.2:AttachmentLoad|ballerinax/smartsheet:1.0.2:AttachmentSend|ballerinax/smartsheet:1.0.2:AttachmentUpdate|ballerinax/smartsheet:1.0.2:DashboardAddPublish|ballerinax/smartsheet:1.0.2:DashboardAddShare|ballerinax/smartsheet:1.0.2:DashboardAddShareMember|ballerinax/smartsheet:1.0.2:DashboardAddWorkspaceShare|ballerinax/smartsheet:1.0.2:DashboardCreate|ballerinax/smartsheet:1.0.2:DashboardDelete|ballerinax/smartsheet:1.0.2:DashboardLoad|ballerinax/smartsheet:1.0.2:DashboardMove|ballerinax/smartsheet:1.0.2:DashboardPurge|ballerinax/smartsheet:1.0.2:DashboardRemovePublish|ballerinax/smartsheet:1.0.2:DashboardRemoveShare|ballerinax/smartsheet:1.0.2:DashboardRemoveShareMember|ballerinax/smartsheet:1.0.2:DashboardRemoveWorkspaceShare|ballerinax/smartsheet:1.0.2:DashboardRename|ballerinax/smartsheet:1.0.2:DashboardRestore|ballerinax/smartsheet:1.0.2:DashboardSaveAsNew|ballerinax/smartsheet:1.0.2:DashboardTransferOwnership|ballerinax/smartsheet:1.0.2:DashboardUpdate|ballerinax/smartsheet:1.0.2:DiscussionCreate|ballerinax/smartsheet:1.0.2:DiscussionDelete|ballerinax/smartsheet:1.0.2:DiscussionSend|ballerinax/smartsheet:1.0.2:DiscussionSendcomment|ballerinax/smartsheet:1.0.2:DiscussionUpdate|ballerinax/smartsheet:1.0.2:FolderCreate|ballerinax/smartsheet:1.0.2:FolderDelete|ballerinax/smartsheet:1.0.2:FolderExport|ballerinax/smartsheet:1.0.2:FolderRename|ballerinax/smartsheet:1.0.2:FolderRequestBackup|ballerinax/smartsheet:1.0.2:FolderSaveAsNew|ballerinax/smartsheet:1.0.2:FormActivate|ballerinax/smartsheet:1.0.2:FormCreate|ballerinax/smartsheet:1.0.2:FormDeactivate|ballerinax/smartsheet:1.0.2:FormDelete|ballerinax/smartsheet:1.0.2:FormUpdate|ballerinax/smartsheet:1.0.2:GroupAddMember|ballerinax/smartsheet:1.0.2:GroupCreate1|ballerinax/smartsheet:1.0.2:GroupDelete|ballerinax/smartsheet:1.0.2:GroupDownloadSheetAccessReport|ballerinax/smartsheet:1.0.2:GroupRemoveMember|ballerinax/smartsheet:1.0.2:GroupRename|ballerinax/smartsheet:1.0.2:GroupTransferOwnership|ballerinax/smartsheet:1.0.2:GroupUpdate1|ballerinax/smartsheet:1.0.2:ReportAddShare|ballerinax/smartsheet:1.0.2:ReportAddShareMember|ballerinax/smartsheet:1.0.2:ReportAddWorkspaceShare|ballerinax/smartsheet:1.0.2:ReportCreate|ballerinax/smartsheet:1.0.2:ReportDelete|ballerinax/smartsheet:1.0.2:ReportExport|ballerinax/smartsheet:1.0.2:ReportLoad|ballerinax/smartsheet:1.0.2:ReportMove|ballerinax/smartsheet:1.0.2:ReportPurge|ballerinax/smartsheet:1.0.2:ReportRemoveShare|ballerinax/smartsheet:1.0.2:ReportRemoveShareMember|ballerinax/smartsheet:1.0.2:ReportRemoveWorkspaceShare|ballerinax/smartsheet:1.0.2:ReportRename|ballerinax/smartsheet:1.0.2:ReportRestore|ballerinax/smartsheet:1.0.2:ReportSaveAsNew|ballerinax/smartsheet:1.0.2:ReportSendAsAttachment|ballerinax/smartsheet:1.0.2:ReportTransferOwnership|ballerinax/smartsheet:1.0.2:ReportUpdate|ballerinax/smartsheet:1.0.2:SheetAddShare|ballerinax/smartsheet:1.0.2:SheetAddShareMember|ballerinax/smartsheet:1.0.2:SheetAddWorkspaceShare|ballerinax/smartsheet:1.0.2:SheetCopyRow|ballerinax/smartsheet:1.0.2:SheetCreate|ballerinax/smartsheet:1.0.2:SheetCreateCellLink|ballerinax/smartsheet:1.0.2:SheetDelete|ballerinax/smartsheet:1.0.2:SheetExport|ballerinax/smartsheet:1.0.2:SheetLoad|ballerinax/smartsheet:1.0.2:SheetMove|ballerinax/smartsheet:1.0.2:SheetMoveRow|ballerinax/smartsheet:1.0.2:SheetPurge|ballerinax/smartsheet:1.0.2:SheetRemoveShare|ballerinax/smartsheet:1.0.2:SheetRemoveShareMember|ballerinax/smartsheet:1.0.2:SheetRemoveWorkspaceShare|ballerinax/smartsheet:1.0.2:SheetRename|ballerinax/smartsheet:1.0.2:SheetRequestBackup|ballerinax/smartsheet:1.0.2:SheetRestore|ballerinax/smartsheet:1.0.2:SheetSaveAsNew|ballerinax/smartsheet:1.0.2:SheetSaveAsTemplate|ballerinax/smartsheet:1.0.2:SheetSendAsAttachment|ballerinax/smartsheet:1.0.2:SheetSendRow|ballerinax/smartsheet:1.0.2:SheetTransferOwnership|ballerinax/smartsheet:1.0.2:SheetUpdate|ballerinax/smartsheet:1.0.2:UpdateRequestCreate|ballerinax/smartsheet:1.0.2:UserAcceptInvite|ballerinax/smartsheet:1.0.2:UserAddToAccount|ballerinax/smartsheet:1.0.2:UserDeclineInvite|ballerinax/smartsheet:1.0.2:UserDownloadSheetAccessReport|ballerinax/smartsheet:1.0.2:UserRemoveFromAccount|ballerinax/smartsheet:1.0.2:UserRemoveFromGroups|ballerinax/smartsheet:1.0.2:UserRemoveShares|ballerinax/smartsheet:1.0.2:UserSendInvite|ballerinax/smartsheet:1.0.2:UserSendPasswordReset|ballerinax/smartsheet:1.0.2:UserTransferOwnedGroups|ballerinax/smartsheet:1.0.2:UserTransferOwnedItems|ballerinax/smartsheet:1.0.2:UserUpdateUser|ballerinax/smartsheet:1.0.2:WorkspaceAddShare|ballerinax/smartsheet:1.0.2:WorkspaceAddShareMember|ballerinax/smartsheet:1.0.2:WorkspaceCreate|ballerinax/smartsheet:1.0.2:WorkspaceCreateRecurringBackup|ballerinax/smartsheet:1.0.2:WorkspaceDelete|ballerinax/smartsheet:1.0.2:WorkspaceDeleteRecurringBackup|ballerinax/smartsheet:1.0.2:WorkspaceExport|ballerinax/smartsheet:1.0.2:WorkspaceRemoveShare|ballerinax/smartsheet:1.0.2:WorkspaceRemoveShareMember|ballerinax/smartsheet:1.0.2:WorkspaceRename|ballerinax/smartsheet:1.0.2:WorkspaceRequestBackup|ballerinax/smartsheet:1.0.2:WorkspaceSaveAsNew|ballerinax/smartsheet:1.0.2:WorkspaceTransferOwnership|ballerinax/smartsheet:1.0.2:WorkspaceUpdateRecurringBackup;
+type EventUnionData AccesstokenAuthorize|AccesstokenRefresh|AccesstokenRevoke|AccountBulkUpdate|AccountDownloadLoginHistory|AccountDownloadPublishedItemsReport|AccountDownloadSheetAccessReport|AccountDownloadUserList|AccountImportUsers|AccountListSheets|AccountRename|AccountUpdateMainContact|AttachmentCreate|AttachmentDelete|AttachmentLoad|AttachmentSend|AttachmentUpdate|DashboardAddPublish|DashboardAddShare|DashboardAddShareMember|DashboardAddWorkspaceShare|DashboardCreate|DashboardDelete|DashboardLoad|DashboardMove|DashboardPurge|DashboardRemovePublish|DashboardRemoveShare|DashboardRemoveShareMember|DashboardRemoveWorkspaceShare|DashboardRename|DashboardRestore|DashboardSaveAsNew|DashboardTransferOwnership|DashboardUpdate|DiscussionCreate|DiscussionDelete|DiscussionSend|DiscussionSendcomment|DiscussionUpdate|FolderCreate|FolderDelete|FolderExport|FolderRename|FolderRequestBackup|FolderSaveAsNew|FormActivate|FormCreate|FormDeactivate|FormDelete|FormUpdate|GroupAddMember|GroupCreate1|GroupDelete|GroupDownloadSheetAccessReport|GroupRemoveMember|GroupRename|GroupTransferOwnership|GroupUpdate1|ReportAddShare|ReportAddShareMember|ReportAddWorkspaceShare|ReportCreate|ReportDelete|ReportExport|ReportLoad|ReportMove|ReportPurge|ReportRemoveShare|ReportRemoveShareMember|ReportRemoveWorkspaceShare|ReportRename|ReportRestore|ReportSaveAsNew|ReportSendAsAttachment|ReportTransferOwnership|ReportUpdate|SheetAddShare|SheetAddShareMember|SheetAddWorkspaceShare|SheetCopyRow|SheetCreate|SheetCreateCellLink|SheetDelete|SheetExport|SheetLoad|SheetMove|SheetMoveRow|SheetPurge|SheetRemoveShare|SheetRemoveShareMember|SheetRemoveWorkspaceShare|SheetRename|SheetRequestBackup|SheetRestore|SheetSaveAsNew|SheetSaveAsTemplate|SheetSendAsAttachment|SheetSendRow|SheetTransferOwnership|SheetUpdate|UpdateRequestCreate|UserAcceptInvite|UserAddToAccount|UserDeclineInvite|UserDownloadSheetAccessReport|UserRemoveFromAccount|UserRemoveFromGroups|UserRemoveShares|UserSendInvite|UserSendPasswordReset|UserTransferOwnedGroups|UserTransferOwnedItems|UserUpdateUser|WorkspaceAddShare|WorkspaceAddShareMember|WorkspaceCreate|WorkspaceCreateRecurringBackup|WorkspaceDelete|WorkspaceDeleteRecurringBackup|WorkspaceExport|WorkspaceRemoveShare|WorkspaceRemoveShareMember|WorkspaceRename|WorkspaceRequestBackup|WorkspaceSaveAsNew|WorkspaceTransferOwnership|WorkspaceUpdateRecurringBackup;
 
 
 type ColumnUpdateData record {
@@ -5084,6 +5256,7 @@
 
 type SentupdaterequestsListHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -5106,8 +5279,10 @@
 
 type CopyRowsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -5130,6 +5305,7 @@
 
 type AddGroupMembersHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -5152,6 +5328,7 @@
 
 type ListSheetsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -5164,7 +5341,8 @@
     "PARTIAL_SUCCESS"|"SUCCESS" message?;
 };
 
-// Unknown type: ReadOnlyFullEnabled
+# If **true**, a rich version of the sheet is published with the ability to download row attachments and discussions
+type ReadOnlyFullEnabled boolean;
 
 # Represents the Queries record for the operation: list-sheets
 
@@ -5194,8 +5372,10 @@
 
 type SetSheetPublishHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -5217,6 +5397,7 @@
 
 type AttachmentsDeleteHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -5292,6 +5473,7 @@
     # **SUNSET** - The `sheetCount` attribute now holds the value `-1` and is included only if the retrieved user's `status` is `ACTIVE`
 
     @deprecated
+    @constraint:Number {minValue: -1, maxValue: -1}
     decimal sheetCount?;
     # User's primary email address
     string email?;
@@ -5331,12 +5513,14 @@
     boolean ignoreRowsNotFound?;
 };
 
-// Unknown type: IcalEnabled
+# If **true**, a webcal is available for the calendar in the sheet
+type IcalEnabled boolean;
 
 # Represents the Headers record for the operation: tokens-getOrRefresh
 
 type TokensGetOrRefreshHeaders record {
     # Required for POST and PUT requests. Defines the structure for the response
+    @http:Header {name: "Content-Type"}
     "application/x-www-form-urlencoded" contentType?;
 };
 
@@ -5358,6 +5542,7 @@
     # Row Id
     decimal id?;
     # Row number within the sheet
+    @constraint:Number {minValue: 1}
     decimal rowNumber?;
     # The row number of the parent
     decimal parentRowNumber?;
@@ -5386,16 +5571,18 @@
     decimal page?;
 };
 
-// Unknown type: SheetssheetIdrowsOneOf21
+type SheetssheetIdrowsOneOf21 Row[];
 
-type SheetIdRowsBody1 ballerinax/smartsheet:1.0.2:Row|ballerinax/smartsheet:1.0.2:SheetssheetIdrowsOneOf21;
+type SheetIdRowsBody1 Row|SheetssheetIdrowsOneOf21;
 
 # Represents the Headers record for the operation: proofs-createProofRequests
 
 type ProofsCreateProofRequestsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -5413,6 +5600,7 @@
 
 type ProofsDeleteProofRequestsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -5449,8 +5637,10 @@
 
 type SetReportPublishHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -5497,6 +5687,7 @@
 
 type AddAlternateEmailHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -5534,6 +5725,7 @@
 
 type DiscussionListAttachmentsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -5575,6 +5767,7 @@
 
 type GetContactHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -5582,6 +5775,7 @@
 
 type ShareWorkspaceGetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -5589,6 +5783,7 @@
 
 type GetFolderHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -5596,10 +5791,12 @@
 
 type UpdaterequestsListHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
-// Unknown type: Format
+# The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it
+type Format string;
 
 
 type SummaryData record {
@@ -5642,6 +5839,7 @@
 
 type ColumnsListOnSheetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -5657,14 +5855,18 @@
 
 type AddImageToCellHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Should be equal to "attachment" to tell the API that a file is in the body of the POST request, followed by a semicolon, followed by **filename=** and the URL-encoded filename in quotes
+    @http:Header {name: "Content-Disposition"}
     string contentDisposition?;
     # Must be set to the size of the file, in bytes. For example to determine file size using in UNIX:
 $ ls -l ProgressReport.docx
 5463 ProgressReport.docx
+    @http:Header {name: "Content-Length"}
     int contentLength?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -5727,6 +5929,7 @@
 
 type DiscussionDeleteHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -5772,6 +5975,7 @@
 
 type UpdateGroupHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -5779,6 +5983,7 @@
 
 type DeleteSummaryFieldsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -5810,8 +6015,10 @@
 
 type SetSightPublishStatusHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -5855,7 +6062,8 @@
     Version version?;
 };
 
-// Unknown type: Version
+# A number that is incremented every time a sheet is modified
+type Version decimal;
 
 
 type AlternateEmailListResponse record {
@@ -5870,8 +6078,10 @@
 
 type CreateWorkspaceHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -5978,6 +6188,7 @@
 
 type AttachmentsVersionListHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6008,6 +6219,7 @@
 
 type DeleteRowsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6053,8 +6265,10 @@
 
 type AttachmentsAttachToCommentHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -6062,6 +6276,7 @@
 
 type ListSightSharesHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6087,6 +6302,7 @@
 
 type UpdateSheetShareHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6138,14 +6354,17 @@
     string message?;
 };
 
-// Unknown type: PropertiesContactOptions
+# Array of ContactOption objects to specify a pre-defined list of values for the column. Column type must be CONTACT_LIST
+type PropertiesContactOptions ContactOption[];
 
 # Represents the Headers record for the operation: create-sheet-in-workspace
 
 type CreateSheetInWorkspaceHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -6220,6 +6439,7 @@
 
 type CreateWebhookRequest record {
     # ID of the object to subscribed to. Specified when a webhook is created and cannot be changed
+    @constraint:Int {minValue: 0}
     int scopeObjectId?;
     # Scope of the subscription. Currently, the only supported value is
 "sheet". Specified when a webhook is created and cannot be changed
@@ -6231,6 +6451,7 @@
     # Limits the webhook to monitor specific columns designated by an array of sheet column IDs. 
     CreateWebhookRequestSubscope subscope?;
     # Webhook version. Currently, the only supported value is 1. This attribute is intended to ensure backward compatibility as new webhook functionality is released. For example, a webhook with a version of 1 is guaranteed to always be sent callback objects that are compatible with the version 1 release of webhooks
+    @constraint:Number {minValue: 1, maxValue: 1}
     decimal version?;
     # Array of the events that are subscribed to. Currently, must be an array of size 1 that contains the string value '\*.\*' (asterisk period asterisk), which means "all objects" and "all events"
     string[] events?;
@@ -6348,6 +6569,7 @@
 
 type ShareSheetGetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6393,8 +6615,10 @@
 
 type AttachmentsVersionUploadHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -6402,12 +6626,15 @@
 
 type ImportSheetIntoWorkspaceHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Should be equal to "attachment" to tell the API that a file is in the body of the POST request, followed by a semicolon, followed by **filename=** and the URL-encoded filename in quotes
+    @http:Header {name: "Content-Disposition"}
     string contentDisposition?;
     # Required for POST request to import a sheet from CSV/XLSX file.
 * For CSV files, use: Content-Type: text/csv
 * For XLSX files, use: Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
+    @http:Header {name: "Content-Type"}
     "text/csv"|"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" contentType;
 };
 
@@ -6435,6 +6662,7 @@
 * **MONTHLY**
 
 For more details, refer to the Table of Schedule Object’s Attributes below
+    @constraint:Number {minValue: 1, maxValue: 31}
     decimal dayOfMonth?;
     # A string array consists of one or more of the following values:
 * **DAY**, **WEEKDAY**, **WEEKEND**
@@ -6474,6 +6702,7 @@
 
 This attribute is applicable to the following schedule types: **DAILY**, **WEEKLY**, **MONTHLY**, or **YEARLY**.
 For more details, refer to the Table of Schedule Object’s Attributes below
+    @constraint:Number {minValue: 1, maxValue: 99}
     decimal repeatEvery?;
     # Type of schedule
     "ONCE"|"DAILY"|"WEEKLY"|"MONTHLY"|"YEARLY" 'type?;
@@ -6519,6 +6748,7 @@
 
 type GetWebhookHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6526,6 +6756,7 @@
 
 type ListSheetSharesHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6582,8 +6813,10 @@
 
 type UpdateSightHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -6614,8 +6847,10 @@
 
 type CopyFolderHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -6635,6 +6870,7 @@
 
 type SentupdaterequestGetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6749,8 +6985,10 @@
 
 type MoveSightHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -6770,6 +7008,7 @@
 
 type GetCrosssheetReferenceHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6823,6 +7062,7 @@
 
 type RowDiscussionsListHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6830,6 +7070,7 @@
 
 type ListHomeContentsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6837,15 +7078,17 @@
 
 type ColumnDeleteHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
-type ReportIdSharesBody ballerinax/smartsheet:1.0.2:Share|ballerinax/smartsheet:1.0.2:ReportsreportIdsharesOneOf2;
+type ReportIdSharesBody Share|ReportsreportIdsharesOneOf2;
 
 # Represents the Headers record for the operation: proofs-delete
 
 type ProofsDeleteHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6853,6 +7096,7 @@
 
 type DeleteReportShareHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6860,6 +7104,7 @@
 
 type AutomationrulesListHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6920,6 +7165,7 @@
 
 type AddUserHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -6959,6 +7205,7 @@
 
 type GetSightHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7002,7 +7249,8 @@
     Share[] result?;
 };
 
-// Unknown type: Formula
+# The formula for a cell, if set
+type Formula string;
 
 
 type EventStreamResponse record {
@@ -7015,6 +7263,7 @@
 
 type ShareSheetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7022,6 +7271,7 @@
 
 type SentupdaterequestDeleteHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7057,8 +7307,10 @@
 
 type ResetSharedSecretHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -7101,8 +7353,10 @@
 
 type AttachmentsAttachToSheetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -7160,6 +7414,7 @@
 
 type ProofsListDiscussionsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7194,6 +7449,7 @@
 
 type ProofsListAttachmentsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7201,8 +7457,10 @@
 
 type MoveRowsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -7210,6 +7468,7 @@
 
 type DeleteSightHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7260,6 +7519,7 @@
 
 type ListWebhooksHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7274,10 +7534,12 @@
 
 type ListEventsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Strongly recommended to make sure payload is compressed. Must be set to one of the following values:
 * deflate
 * gzip
+    @http:Header {name: "Accept-Encoding"}
     "deflate"|"gzip" acceptEncoding?;
 };
 
@@ -7285,6 +7547,7 @@
 
 type DeleteGroupHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7303,6 +7566,7 @@
 
 type ProofsGetAllProofsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7324,12 +7588,14 @@
 
 type RowsAddToSheetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
-type WorkspaceIdSharesBody ballerinax/smartsheet:1.0.2:Share|ballerinax/smartsheet:1.0.2:WorkspacesworkspaceIdsharesOneOf2;
+type WorkspaceIdSharesBody Share|WorkspacesworkspaceIdsharesOneOf2;
 
 # Represents the Queries record for the operation: rows-addToSheet
 
@@ -7353,6 +7619,7 @@
 
 type GetReportPublishHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7368,7 +7635,7 @@
     string email?;
 };
 
-// Unknown type: UsersuserIdalternateemailsOneOf2
+type UsersuserIdalternateemailsOneOf2 AddAlternateEmail[];
 
 
 type WorkspaceFolderListData record {
@@ -7394,6 +7661,7 @@
     # Row Id
     decimal id?;
     # Row number within the sheet
+    @constraint:Number {minValue: 1}
     decimal rowNumber?;
     # Sheet version number that is incremented every time a sheet is modified
     decimal version?;
@@ -7440,7 +7708,8 @@
     # Maximum number of events to return as response to this call.
 Must be between 1 through 10,000 (inclusive).
 Defaults to 1,000 if not specified
-    ballerina/lang.int:0.0.0:Signed32 maxCount?;
+    @constraint:Int {minValue: 1, maxValue: 10000}
+    int:Signed32 maxCount?;
     # The earliest time from which events are included in the response. Events before this time are excluded.
 
 This parameter is required if `streamPosition` is not used.
@@ -7479,8 +7748,10 @@
 
 type ColumnsAddToSheetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -7507,12 +7778,14 @@
 
 type ListCrosssheetReferencesHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
-// Unknown type: Index
+# Field index or position. This number is zero-based
+type Index decimal;
 
-type FolderIdSheetsBody ballerinax/smartsheet:1.0.2:SheetToCreate|ballerinax/smartsheet:1.0.2:SheetToCreateFromTemplate;
+type FolderIdSheetsBody SheetToCreate|SheetToCreateFromTemplate;
 
 # Represents the Queries record for the operation: list-summary-fields
 
@@ -7571,9 +7844,11 @@
 # Only returned in the response if **readOnlyFullEnabled = true**
 type ReadOnlyFullAccessibleBy "ALL"|"ORG"|"SHARED";
 
-// Unknown type: ReadOnlyLiteEnabled
+# If **true**, a lightweight version of the sheet is published without row attachments and discussions
+type ReadOnlyLiteEnabled boolean;
 
-// Unknown type: ReadWriteEnabled
+# If **true**,a rich version of the sheet is published with the ability to edit cells and manage attachments and discussions
+type ReadWriteEnabled boolean;
 
 # Represents the Queries record for the operation: share-report
 
@@ -7588,12 +7863,14 @@
     SightListItem[] data?;
 };
 
-// Unknown type: PropertiesId
+# SummaryField Id
+type PropertiesId decimal;
 
 # Represents the Headers record for the operation: delete-sight-share
 
 type DeleteSightShareHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7601,6 +7878,7 @@
 
 type GetAlternateEmailHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7608,6 +7886,7 @@
 
 type GetReportsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7615,6 +7894,7 @@
 
 type UpdateUserHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7638,6 +7918,7 @@
 
 type DeactivateUserHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7656,6 +7937,7 @@
 
 type ListFoldersHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7663,6 +7945,7 @@
 
 type DiscussionGetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7773,6 +8056,7 @@
 
 type UpdateReportShareHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7789,6 +8073,7 @@
 
 type ColumnGetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7796,6 +8081,7 @@
 
 type AutomationruleDeleteHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7803,6 +8089,7 @@
 
 type ShareReportHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7810,6 +8097,7 @@
 
 type DeleteFolderHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7877,18 +8165,23 @@
 
 type ListUsersHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
 
 type Token record {
     # A credential that can be used by a client to access the Smartsheet API
+    @jsondata:Name {value: "access_token"}
     string accessToken?;
     # A credential tied to the access token that can be used to obtain a fresh access token with the same permissions, without further involvement from a user
+    @jsondata:Name {value: "refresh_token"}
     string refreshToken?;
     # How an access token will be generated and presented. Smartsheet uses the bearer parameter, which means essentially give access to the bearer of this token
+    @jsondata:Name {value: "token_type"}
     string tokenType?;
     # Number of seconds token is valid once issued
+    @jsondata:Name {value: "expires_in"}
     decimal expiresIn?;
 };
 
@@ -7909,8 +8202,10 @@
 
 type CreateSheetInFolderHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -7931,14 +8226,17 @@
     Sight result?;
 };
 
-// Unknown type: PropertiesSymbol
+# When applicable for PICKLIST column type
+type PropertiesSymbol string;
 
 # Represents the Headers record for the operation: move-folder
 
 type MoveFolderHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -7963,12 +8261,13 @@
     AlternateEmail[] data?;
 };
 
-type WorkspaceIdSheetsBody ballerinax/smartsheet:1.0.2:SheetToCreate|ballerinax/smartsheet:1.0.2:SheetToCreateFromTemplate;
+type WorkspaceIdSheetsBody SheetToCreate|SheetToCreateFromTemplate;
 
 # Represents the Headers record for the operation: list-alternate-emails
 
 type ListAlternateEmailsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -7976,17 +8275,20 @@
 
 type SheetSendHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
-// Unknown type: SheetssheetIdrowsOneOf2
+type SheetssheetIdrowsOneOf2 Row[];
 
 # Represents the Headers record for the operation: update-workspace
 
 type UpdateWorkspaceHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8015,6 +8317,7 @@
 
 type RemoveUserHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8054,8 +8357,10 @@
 
 type CopySheetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -8063,6 +8368,7 @@
 
 type AddSummaryFieldsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8084,8 +8390,10 @@
 
 type GetFavoritesHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # UserId of the user
+    @http:Header {name: "x-smar-sc-actor-id"}
     string xSmarScActorId?;
 };
 
@@ -8093,8 +8401,10 @@
 
 type CreateWorkspaceFolderHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -8102,6 +8412,7 @@
 
 type ListSummaryFieldsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8122,6 +8433,7 @@
 
 type UpdaterequestsDeleteHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8140,8 +8452,10 @@
 
 type RowsSendHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -8149,6 +8463,7 @@
 
 type DeleteGroupMembersHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8156,6 +8471,7 @@
 
 type ColumnUpdateColumnHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8221,6 +8537,7 @@
 
 type AttachmentsListOnRowHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8228,8 +8545,10 @@
 
 type GetReportHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # The Accept request-header field can be used to specify certain media types which are acceptable for the response
+    @http:Header {name: "Accept"}
     string accept?;
 };
 
@@ -8237,6 +8556,7 @@
 
 type ListSearchSheetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8284,6 +8604,7 @@
 
 type ProofsListRequestActionsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8340,6 +8661,7 @@
     # **SUNSET** - The `sheetCount` attribute now holds the value `-1` and is included only if the retrieved user's `status` is `ACTIVE`
 
     @deprecated
+    @constraint:Number {minValue: -1, maxValue: -1}
     decimal sheetCount?;
     Account account?;
     # Indicates whether the user is a licensed user (can create and own sheets)
@@ -8415,6 +8737,7 @@
 
 type ShareWorkspaceHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8422,6 +8745,7 @@
 
 type DeleteWorkspaceShareHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8461,6 +8785,7 @@
 
 type TokensDeleteHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8482,8 +8807,10 @@
 
 type ProofsCreateVersionHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -8491,6 +8818,7 @@
 
 type GetSheetVersionHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8498,6 +8826,7 @@
 
 type AddGroupHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8507,7 +8836,7 @@
     decimal version?;
 };
 
-type FavoriteResponse ballerinax/smartsheet:1.0.2:Sheet|ballerinax/smartsheet:1.0.2:SheetVersion;
+type FavoriteResponse Sheet|SheetVersion;
 
 
 type FolderCreateResponse record {
@@ -8520,8 +8849,10 @@
 
 type CreateFolderFolderHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -8529,8 +8860,10 @@
 
 type ProofsCreateDiscussionHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -8538,6 +8871,7 @@
 
 type ListWorkspaceSharesHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8545,8 +8879,10 @@
 
 type CopySightHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -8594,11 +8930,13 @@
 
 type UpdateFolderHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -8668,6 +9006,7 @@
 
 type GetWorkspaceHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8702,17 +9041,20 @@
 
 type AddCrosssheetReferenceHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
-type SheetIdRowsBody ballerinax/smartsheet:1.0.2:Row|ballerinax/smartsheet:1.0.2:SheetssheetIdrowsOneOf2;
+type SheetIdRowsBody Row|SheetssheetIdrowsOneOf2;
 
 # Represents the Headers record for the operation: update-sight-share
 
 type UpdateSightShareHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8720,6 +9062,7 @@
 
 type GetGroupHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8727,8 +9070,10 @@
 
 type CreateWebhookHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -8736,6 +9081,7 @@
 
 type DeleteWorkspaceHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8743,6 +9089,7 @@
 
 type ListReportSharesHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8750,8 +9097,10 @@
 
 type RowDiscussionsCreateHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -8759,8 +9108,10 @@
 
 type DeleteFavoritesByTypeAndIdHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # UserId of the user
+    @http:Header {name: "x-smar-sc-actor-id"}
     string xSmarScActorId?;
 };
 
@@ -8817,6 +9168,7 @@
 
 type ListSearchHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8841,9 +9193,9 @@
     string objectIds;
 };
 
-// Unknown type: GroupsgroupIdmembersOneOf2
+type GroupsgroupIdmembersOneOf2 GroupMember[];
 
-type GroupIdMembersBody ballerinax/smartsheet:1.0.2:GroupMember|ballerinax/smartsheet:1.0.2:GroupsgroupIdmembersOneOf2;
+type GroupIdMembersBody GroupMember|GroupsgroupIdmembersOneOf2;
 
 # CrossSheetReference object to create with specified cell range
 
@@ -8896,6 +9248,7 @@
 
 type UpdateSheetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8910,6 +9263,7 @@
 
 type ListSummaryFieldsPaginatedHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8917,8 +9271,10 @@
 
 type SendReportViaEmailHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -8942,6 +9298,7 @@
 
 type CellHistoryGetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8949,12 +9306,15 @@
 
 type ImportSheetIntoFolderHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Should be equal to "attachment" to tell the API that a file is in the body of the POST request, followed by a semicolon, followed by **filename=** and the URL-encoded filename in quotes
+    @http:Header {name: "Content-Disposition"}
     string contentDisposition?;
     # Required for POST request to import a sheet from CSV/XLSX file.
 * For CSV files, use: Content-Type: text/csv
 * For XLSX files, use: Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
+    @http:Header {name: "Content-Type"}
     "text/csv"|"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" contentType;
 };
 
@@ -8969,8 +9329,10 @@
 
 type MoveSheetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -8987,6 +9349,7 @@
 
 type GetWorkspaceFoldersHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -8994,6 +9357,7 @@
 
 type ProofsGetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9001,6 +9365,7 @@
 
 type UpdateSummaryFieldsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9008,8 +9373,10 @@
 
 type DiscussionsCreateHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -9017,6 +9384,7 @@
 
 type ListGroupsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9024,10 +9392,12 @@
 
 type ListFilteredEventsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Strongly recommended to make sure payload is compressed. Must be set to one of the following values:
 * deflate
 * gzip
+    @http:Header {name: "Accept-Encoding"}
     "deflate"|"gzip" acceptEncoding?;
 };
 
@@ -9055,6 +9425,7 @@
 
 type CommentGetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9062,6 +9433,7 @@
 
 type UpdateWorkspaceShareHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9069,8 +9441,10 @@
 
 type UpdateWebhookHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -9109,6 +9483,7 @@
 
 type ProofsUpdateHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9142,6 +9517,7 @@
 
 type RowGetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9170,6 +9546,7 @@
 
 type DeleteSheetShareHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9177,8 +9554,10 @@
 
 type CreateHomeFolderHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -9197,8 +9576,10 @@
 
 type ListImageUrlsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -9227,6 +9608,7 @@
 
 type AttachmentsGetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9234,8 +9616,10 @@
 
 type RowAttachmentsAttachFileHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -9243,6 +9627,7 @@
 
 type ListContactsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9277,7 +9662,8 @@
     Validation validation?;
 };
 
-// Unknown type: PropertiesTitle
+# Arbitrary name, must be unique within summary
+type PropertiesTitle string;
 
 # Specifies the type of a column property. Valid values include various column data types such as CHECKBOX, CONTACT_LIST, DATE, PICKLIST, and others
 type PropertiesType "ABSTRACT_DATETIME"|"CHECKBOX"|"CONTACT_LIST"|"DATE"|"DATETIME"|"DURATION"|"MULTI_CONTACT_LIST"|"MULTI_PICKLIST"|"PICKLIST"|"PREDECESSOR"|"TEXT_NUMBER";
@@ -9317,8 +9703,10 @@
 
 type UpdaterequestsUpdateHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -9326,8 +9714,10 @@
 
 type CreateSheetInSheetsFolderHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -9335,6 +9725,7 @@
 
 type ListWorkspacesHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9377,6 +9768,7 @@
 
 type TemplatesListPublicHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9384,6 +9776,7 @@
 
 type PromoteAlternateEmailHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9391,6 +9784,7 @@
 
 type ListOrgSheetsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9423,21 +9817,25 @@
 
 type ImportSheetIntoSheetsFolderHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Should be equal to "attachment" to tell the API that a file is in the body of the POST request, followed by a semicolon, followed by **filename=** and the URL-encoded filename in quotes
+    @http:Header {name: "Content-Disposition"}
     string contentDisposition?;
     # Required for POST request to import a sheet from CSV/XLSX file.
 * For CSV files, use: Content-Type: text/csv
 * For XLSX files, use: Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
+    @http:Header {name: "Content-Type"}
     "text/csv"|"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" contentType;
 };
 
-type UserIdAlternateemailsBody ballerinax/smartsheet:1.0.2:AddAlternateEmail|ballerinax/smartsheet:1.0.2:UsersuserIdalternateemailsOneOf2;
+type UserIdAlternateemailsBody AddAlternateEmail|UsersuserIdalternateemailsOneOf2;
 
 # Represents the Headers record for the operation: list-sights
 
 type ListSightsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9445,8 +9843,10 @@
 
 type ProofsAttachToProofHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -9454,6 +9854,7 @@
 
 type HomeListFoldersHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9490,8 +9891,10 @@
 
 type UpdateUserProfileImageHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -9506,6 +9909,7 @@
 
 type CommentDeleteHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9513,10 +9917,11 @@
 
 type DeleteSheetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
-type SheetIdCrosssheetreferencesBody ballerinax/smartsheet:1.0.2:CrossSheetReferenceRequestWithColumnIds|ballerinax/smartsheet:1.0.2:CrossSheetReferenceRequestWithRowIds|ballerinax/smartsheet:1.0.2:CrossSheetReferenceRequestWithColumnAndRowIds;
+type SheetIdCrosssheetreferencesBody CrossSheetReferenceRequestWithColumnIds|CrossSheetReferenceRequestWithRowIds|CrossSheetReferenceRequestWithColumnAndRowIds;
 
 
 type ProofDiscussionListData record {
@@ -9528,6 +9933,7 @@
 
 type GetUserHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9600,6 +10006,7 @@
 
 type ShareSightGetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9607,6 +10014,7 @@
 
 type RowsSortQueries record {
     # (Optional) Any of the relevant parameters or query parameters listed for [Get Sheet](/api/smartsheet/openapi/sheets/getsheet)
+    @http:Query {name: "include&exclude"}
     string includeExclude?;
 };
 
@@ -9614,14 +10022,18 @@
 
 type AddImageSummaryFieldHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Should be equal to "attachment" to tell the API that a file is in the body of the POST request, followed by a semicolon, followed by **filename=** and the URL-encoded filename in quotes
+    @http:Header {name: "Content-Disposition"}
     string contentDisposition?;
     # Must be set to the size of the file, in bytes. For example to determine file size using in UNIX:
 $ ls -l ProgressReport.docx
 5463 ProgressReport.docx
+    @http:Header {name: "Content-Length"}
     int contentLength?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -9629,6 +10041,7 @@
 
 type ProofsGetVersionsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9636,6 +10049,7 @@
 
 type DiscussionsListHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9643,6 +10057,7 @@
 
 type ShareSightHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9650,8 +10065,10 @@
 
 type UpdateRowsHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -9688,6 +10105,7 @@
 
 type UpdaterequestsGetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9702,8 +10120,10 @@
 
 type CommentEditHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # Required for POST and PUT requests. Defines the structure for the request body
+    @http:Header {name: "Content-Type"}
     string contentType?;
 };
 
@@ -9711,8 +10131,10 @@
 
 type DeleteFavoritesByTypeHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
     # UserId of the user
+    @http:Header {name: "x-smar-sc-actor-id"}
     string xSmarScActorId?;
 };
 
@@ -9729,6 +10151,7 @@
 
 type TemplatesListHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9736,6 +10159,7 @@
 
 type AutomationruleGetHeaders record {
     # API Access Token used to authenticate requests to Smartsheet APIs
+    @http:Header {name: "Authorization"}
     string authorization?;
 };
 
@@ -9780,19 +10204,19 @@
 
     # List Contacts
     # 
-    resource function get contacts(ListContactsHeaders headers = {}, Timestamp modifiedSince = "", boolean numericDates = false, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ListContactsQueries queries) returns ContactListResponse|error;
+    resource function get contacts(ListContactsHeaders headers = {}, Timestamp modifiedSince = "", boolean numericDates = false, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ListContactsQueries queries) returns ContactListResponse|error;
 
     # Get Contact
     # 
-    resource function get contacts/[decimal contactId](GetContactHeaders headers = {}, "profileImage" include = "profileImage", anydata Additional Values, GetContactQueries queries) returns Contact|error;
+    resource function get contacts/[decimal contactId](GetContactHeaders headers = {}, "profileImage" include = "profileImage", GetContactQueries queries) returns Contact|error;
 
     # List events
     # 
-    resource function get events(ListEventsHeaders headers = {}, decimal managedPlanId = 0.0d, string streamPosition = "", boolean numericDates = false, string to = "", int:Signed32 maxCount = 0, string since = "", anydata Additional Values, ListEventsQueries queries) returns EventStreamResponse|error;
+    resource function get events(ListEventsHeaders headers = {}, decimal managedPlanId = 0.0d, string streamPosition = "", boolean numericDates = false, string to = "", int:Signed32 maxCount = 0, string since = "", ListEventsQueries queries) returns EventStreamResponse|error;
 
     # Get Favorites
     # 
-    resource function get favorites(GetFavoritesHeaders headers = {}, "directId"|"name" include = "directId", decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, GetFavoritesQueries queries) returns ContactResponse|error;
+    resource function get favorites(GetFavoritesHeaders headers = {}, "directId"|"name" include = "directId", decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, GetFavoritesQueries queries) returns ContactResponse|error;
 
     # Add Favorites
     # 
@@ -9800,11 +10224,11 @@
 
     # Delete Multiple Favorites
     # 
-    resource function delete favorites/["folder"|"report"|"sheet"|"sight"|"template"|"workspace" favoriteType](DeleteFavoritesByTypeHeaders headers = {}, string objectIds = "", anydata Additional Values, DeleteFavoritesByTypeQueries queries) returns GenericResult|error;
+    resource function delete favorites/["folder"|"report"|"sheet"|"sight"|"template"|"workspace" favoriteType](DeleteFavoritesByTypeHeaders headers = {}, string objectIds = "", DeleteFavoritesByTypeQueries queries) returns GenericResult|error;
 
     # Is Favorite
     # 
-    resource function get favorites/["folder"|"report"|"sheet"|"sight"|"template"|"workspace" favoriteType]/[decimal favoriteId](IsFavoriteHeaders headers = {}, "directId"|"name" include = "directId", anydata Additional Values, IsFavoriteQueries queries) returns Favorite|error;
+    resource function get favorites/["folder"|"report"|"sheet"|"sight"|"template"|"workspace" favoriteType]/[decimal favoriteId](IsFavoriteHeaders headers = {}, "directId"|"name" include = "directId", IsFavoriteQueries queries) returns Favorite|error;
 
     # Delete Favorite
     # 
@@ -9816,7 +10240,7 @@
 
     # Get Folder
     # 
-    resource function get folders/[decimal folderId](GetFolderHeaders headers = {}, "source"|"distributionLink"|"ownerInfo"|"sheetVersion" include = "source", anydata Additional Values, GetFolderQueries queries) returns Folder|error;
+    resource function get folders/[decimal folderId](GetFolderHeaders headers = {}, "source"|"distributionLink"|"ownerInfo"|"sheetVersion" include = "source", GetFolderQueries queries) returns Folder|error;
 
     # Update Folder
     # 
@@ -9828,15 +10252,15 @@
 
     # Copy Folder
     # 
-    resource function post folders/[decimal folderId]/copy(FolderIdCopyBody payload, CopyFolderHeaders headers = {}, "attachments"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules"|"shares" include = "attachments", "cellLinks"|"reports"|"sheetHyperlinks"|"sights" skipRemap = "cellLinks", "sheetHyperlinks" exclude = "sheetHyperlinks", anydata Additional Values, CopyFolderQueries queries) returns ContainerDestinationForCopy|error;
+    resource function post folders/[decimal folderId]/copy(FolderIdCopyBody payload, CopyFolderHeaders headers = {}, "attachments"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules"|"shares" include = "attachments", "cellLinks"|"reports"|"sheetHyperlinks"|"sights" skipRemap = "cellLinks", "sheetHyperlinks" exclude = "sheetHyperlinks", CopyFolderQueries queries) returns ContainerDestinationForCopy|error;
 
     # List Folders
     # 
-    resource function get folders/[decimal folderId]/folders(ListFoldersHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ListFoldersQueries queries) returns SearchResponse|error;
+    resource function get folders/[decimal folderId]/folders(ListFoldersHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ListFoldersQueries queries) returns SearchResponse|error;
 
     # Create Folder
     # 
-    resource function post folders/[decimal folderId]/folders(FolderIdFoldersBody payload, CreateFolderFolderHeaders headers = {}, "attachments"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules"|"shares" include = "attachments", "cellLinks"|"reports"|"sheetHyperlinks"|"sights" skipRemap = "cellLinks", "sheetHyperlinks" exclude = "sheetHyperlinks", anydata Additional Values, CreateFolderFolderQueries queries) returns SharedSecretResponse|error;
+    resource function post folders/[decimal folderId]/folders(FolderIdFoldersBody payload, CreateFolderFolderHeaders headers = {}, "attachments"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules"|"shares" include = "attachments", "cellLinks"|"reports"|"sheetHyperlinks"|"sights" skipRemap = "cellLinks", "sheetHyperlinks" exclude = "sheetHyperlinks", CreateFolderFolderQueries queries) returns SharedSecretResponse|error;
 
     # Move Folder
     # 
@@ -9844,19 +10268,19 @@
 
     # Create Sheet in Folder
     # 
-    resource function post folders/[decimal folderId]/sheets(FolderIdSheetsBody payload, CreateSheetInFolderHeaders headers = {}, "attachments"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules" include = "attachments", anydata Additional Values, CreateSheetInFolderQueries queries) returns WebhookResponse|error;
+    resource function post folders/[decimal folderId]/sheets(FolderIdSheetsBody payload, CreateSheetInFolderHeaders headers = {}, "attachments"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules" include = "attachments", CreateSheetInFolderQueries queries) returns WebhookResponse|error;
 
     # Import Sheet into Folder
     # 
-    resource function post folders/[decimal folderId]/sheets/'import(ImportSheetIntoFolderHeaders headers, byte[] payload, string sheetName = "", decimal headerRowIndex = 0.0d, decimal primaryColumnIndex = 0.0d, anydata Additional Values, ImportSheetIntoFolderQueries queries) returns WebhookListResponse|error;
+    resource function post folders/[decimal folderId]/sheets/'import(ImportSheetIntoFolderHeaders headers, byte[] payload, string sheetName = "", decimal headerRowIndex = 0.0d, decimal primaryColumnIndex = 0.0d, ImportSheetIntoFolderQueries queries) returns WebhookListResponse|error;
 
     # List Contents
     # 
-    resource function get folders/personal(ListHomeContentsHeaders headers = {}, "source"|"distributionLink"|"ownerInfo"|"sheetVersion" include = "source", anydata Additional Values, ListHomeContentsQueries queries) returns Home|error;
+    resource function get folders/personal(ListHomeContentsHeaders headers = {}, "source"|"distributionLink"|"ownerInfo"|"sheetVersion" include = "source", ListHomeContentsQueries queries) returns Home|error;
 
     # List Org Groups
     # 
-    resource function get groups(ListGroupsHeaders headers = {}, Timestamp modifiedSince = "", boolean numericDates = false, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ListGroupsQueries queries) returns GroupResponse|error;
+    resource function get groups(ListGroupsHeaders headers = {}, Timestamp modifiedSince = "", boolean numericDates = false, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ListGroupsQueries queries) returns GroupResponse|error;
 
     # Add Group
     # 
@@ -9884,7 +10308,7 @@
 
     # List Folders in Home
     # 
-    resource function get home/folders(HomeListFoldersHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, HomeListFoldersQueries queries) returns SearchResponse|error;
+    resource function get home/folders(HomeListFoldersHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, HomeListFoldersQueries queries) returns SearchResponse|error;
 
     # Create Folder
     # 
@@ -9896,11 +10320,11 @@
 
     # List Reports
     # 
-    resource function get reports(GetReportsHeaders headers = {}, Timestamp modifiedSince = "", anydata Additional Values, GetReportsQueries queries) returns TemplateListResponse|error;
+    resource function get reports(GetReportsHeaders headers = {}, Timestamp modifiedSince = "", GetReportsQueries queries) returns TemplateListResponse|error;
 
     # Get Report
     # 
-    resource function get reports/[decimal reportId](GetReportHeaders headers = {}, decimal accessApiLevel = 0.0d, "attachments"|"discussions"|"proofs"|"format"|"objectValue"|"scope"|"source"|"sourceSheets" include = "attachments", int level = 0, decimal pageSize = 0.0d, "linkInFromCellDetails"|"linksOutToCellsDetails" exclude = "linkInFromCellDetails", decimal page = 0.0d, anydata Additional Values, GetReportQueries queries) returns Report|error;
+    resource function get reports/[decimal reportId](GetReportHeaders headers = {}, decimal accessApiLevel = 0.0d, "attachments"|"discussions"|"proofs"|"format"|"objectValue"|"scope"|"source"|"sourceSheets" include = "attachments", int level = 0, decimal pageSize = 0.0d, "linkInFromCellDetails"|"linksOutToCellsDetails" exclude = "linkInFromCellDetails", decimal page = 0.0d, GetReportQueries queries) returns Report|error;
 
     # Send report via email
     # 
@@ -9916,31 +10340,31 @@
 
     # List Report Shares
     # 
-    resource function get reports/[decimal reportId]/shares(ListReportSharesHeaders headers = {}, "ITEM"|"WORKSPACE" sharingInclude = "ITEM", decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ListReportSharesQueries queries) returns PublicTemplateListResponse|error;
+    resource function get reports/[decimal reportId]/shares(ListReportSharesHeaders headers = {}, "ITEM"|"WORKSPACE" sharingInclude = "ITEM", decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ListReportSharesQueries queries) returns PublicTemplateListResponse|error;
 
     # Share Report
     # 
-    resource function post reports/[decimal reportId]/shares(ReportIdSharesBody payload, ShareReportHeaders headers = {}, boolean sendEmail = false, anydata Additional Values, ShareReportQueries queries) returns TokenResponse|error;
+    resource function post reports/[decimal reportId]/shares(ReportIdSharesBody payload, ShareReportHeaders headers = {}, boolean sendEmail = false, ShareReportQueries queries) returns TokenResponse|error;
 
     # Get Report Share
     # 
-    resource function get reports/[decimal reportId]/shares/[string shareId](ShareReportGetHeaders headers = {}, decimal accessApiLevel = 0.0d, anydata Additional Values, ShareReportGetQueries queries) returns Share|error;
+    resource function get reports/[decimal reportId]/shares/[string shareId](ShareReportGetHeaders headers = {}, decimal accessApiLevel = 0.0d, ShareReportGetQueries queries) returns Share|error;
 
     # Update Report Share
     # 
-    resource function put reports/[decimal reportId]/shares/[string shareId](SharesshareIdBody payload, UpdateReportShareHeaders headers = {}, decimal accessApiLevel = 0.0d, anydata Additional Values, UpdateReportShareQueries queries) returns UserResponse|error;
+    resource function put reports/[decimal reportId]/shares/[string shareId](SharesshareIdBody payload, UpdateReportShareHeaders headers = {}, decimal accessApiLevel = 0.0d, UpdateReportShareQueries queries) returns UserResponse|error;
 
     # Delete Report Share
     # 
-    resource function delete reports/[decimal reportId]/shares/[string shareId](DeleteReportShareHeaders headers = {}, decimal accessApiLevel = 0.0d, anydata Additional Values, DeleteReportShareQueries queries) returns Result|error;
+    resource function delete reports/[decimal reportId]/shares/[string shareId](DeleteReportShareHeaders headers = {}, decimal accessApiLevel = 0.0d, DeleteReportShareQueries queries) returns Result|error;
 
     # Search Everything
     # 
-    resource function get search(ListSearchHeaders headers = {}, string include = "", Timestamp modifiedSince = "", string query = "", string location = "", ("attachments"|"cellData"|"comments"|"folderNames"|"reportNames"|"sheetNames"|"sightNames"|"summaryFields"|"templateNames"|"workspaceNames")[] scopes = [], anydata Additional Values, ListSearchQueries queries) returns UserCreateResponse|error;
+    resource function get search(ListSearchHeaders headers = {}, string include = "", Timestamp modifiedSince = "", string query = "", string location = "", ("attachments"|"cellData"|"comments"|"folderNames"|"reportNames"|"sheetNames"|"sightNames"|"summaryFields"|"templateNames"|"workspaceNames")[] scopes = [], ListSearchQueries queries) returns UserCreateResponse|error;
 
     # Search Sheet
     # 
-    resource function get search/sheets/[decimal sheetId](ListSearchSheetHeaders headers = {}, string query = "", anydata Additional Values, ListSearchSheetQueries queries) returns AlternateEmailResponse|error;
+    resource function get search/sheets/[decimal sheetId](ListSearchSheetHeaders headers = {}, string query = "", ListSearchSheetQueries queries) returns AlternateEmailResponse|error;
 
     # Gets application constants.
     # 
@@ -9948,23 +10372,23 @@
 
     # List Sheets
     # 
-    resource function get sheets(ListSheetsHeaders headers = {}, decimal accessApiLevel = 0.0d, "sheetVersion"|"source" include = "sheetVersion", Timestamp modifiedSince = "", boolean numericDates = false, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ListSheetsQueries queries) returns AlternateEmailListResponse|error;
+    resource function get sheets(ListSheetsHeaders headers = {}, decimal accessApiLevel = 0.0d, "sheetVersion"|"source" include = "sheetVersion", Timestamp modifiedSince = "", boolean numericDates = false, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ListSheetsQueries queries) returns AlternateEmailListResponse|error;
 
     # Create Sheet in "Sheets" Folder
     # 
-    resource function post sheets(SheetsBody payload, CreateSheetInSheetsFolderHeaders headers = {}, decimal accessApiLevel = 0.0d, "attachments"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules" include = "attachments", anydata Additional Values, CreateSheetInSheetsFolderQueries queries) returns WebhookResponse|error;
+    resource function post sheets(SheetsBody payload, CreateSheetInSheetsFolderHeaders headers = {}, decimal accessApiLevel = 0.0d, "attachments"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules" include = "attachments", CreateSheetInSheetsFolderQueries queries) returns WebhookResponse|error;
 
     # Import Sheet from CSV / XLSX
     # 
-    resource function post sheets/'import(ImportSheetIntoSheetsFolderHeaders headers, byte[] payload, string sheetName = "", decimal headerRowIndex = 0.0d, decimal primaryColumnIndex = 0.0d, anydata Additional Values, ImportSheetIntoSheetsFolderQueries queries) returns WebhookListResponse|error;
+    resource function post sheets/'import(ImportSheetIntoSheetsFolderHeaders headers, byte[] payload, string sheetName = "", decimal headerRowIndex = 0.0d, decimal primaryColumnIndex = 0.0d, ImportSheetIntoSheetsFolderQueries queries) returns WebhookListResponse|error;
 
     # Get Sheet
     # 
-    resource function get sheets/[decimal sheetId](GetSheetHeaders headers = {}, decimal accessApiLevel = 0.0d, "attachments"|"columnType"|"crossSheetReferences"|"discussions"|"filters"|"filterDefinitions"|"format"|"ganttConfig"|"objectValue"|"ownerInfo"|"rowPermalink"|"source"|"writerInfo" include = "attachments", int level = 0, string rowIds = "", decimal pageSize = 0.0d, "LETTER"|"LEGAL"|"WIDE"|"ARCHD"|"A4"|"A3"|"A2"|"A1"|"A0" paperSize = "LETTER", int ifVersionAfter = 0, string filterId = "", string columnIds = "", string rowNumbers = "", "filteredOutRows"|"linkInFromCellDetails"|"linksOutToCellsDetails"|"nonexistentCells" exclude = "filteredOutRows", decimal page = 0.0d, Timestamp rowsModifiedSince = "", anydata Additional Values, GetSheetQueries queries) returns Sheet|SheetVersion|error;
+    resource function get sheets/[decimal sheetId](GetSheetHeaders headers = {}, decimal accessApiLevel = 0.0d, "attachments"|"columnType"|"crossSheetReferences"|"discussions"|"filters"|"filterDefinitions"|"format"|"ganttConfig"|"objectValue"|"ownerInfo"|"rowPermalink"|"source"|"writerInfo" include = "attachments", int level = 0, string rowIds = "", decimal pageSize = 0.0d, "LETTER"|"LEGAL"|"WIDE"|"ARCHD"|"A4"|"A3"|"A2"|"A1"|"A0" paperSize = "LETTER", int ifVersionAfter = 0, string filterId = "", string columnIds = "", string rowNumbers = "", "filteredOutRows"|"linkInFromCellDetails"|"linksOutToCellsDetails"|"nonexistentCells" exclude = "filteredOutRows", decimal page = 0.0d, Timestamp rowsModifiedSince = "", GetSheetQueries queries) returns Sheet|SheetVersion|error;
 
     # Update Sheet
     # 
-    resource function put sheets/[decimal sheetId](UpdateSheet payload, UpdateSheetHeaders headers = {}, decimal accessApiLevel = 0.0d, anydata Additional Values, UpdateSheetQueries queries) returns AttachmentListResponse|error;
+    resource function put sheets/[decimal sheetId](UpdateSheet payload, UpdateSheetHeaders headers = {}, decimal accessApiLevel = 0.0d, UpdateSheetQueries queries) returns AttachmentListResponse|error;
 
     # Delete Sheet
     # 
@@ -9972,7 +10396,7 @@
 
     # List Attachments
     # 
-    resource function get sheets/[decimal sheetId]/attachments(AttachmentsListOnSheetHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, AttachmentsListOnSheetQueries queries) returns AttachmentVersionListResponse|error;
+    resource function get sheets/[decimal sheetId]/attachments(AttachmentsListOnSheetHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, AttachmentsListOnSheetQueries queries) returns AttachmentVersionListResponse|error;
 
     # Attach File or URL to Sheet
     # 
@@ -9988,7 +10412,7 @@
 
     # List Versions
     # 
-    resource function get sheets/[decimal sheetId]/attachments/[string attachmentId]/versions(AttachmentsVersionListHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, AttachmentsVersionListQueries queries) returns AttachmentVersionListResponse|error;
+    resource function get sheets/[decimal sheetId]/attachments/[string attachmentId]/versions(AttachmentsVersionListHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, AttachmentsVersionListQueries queries) returns AttachmentVersionListResponse|error;
 
     # Attach New version
     # 
@@ -10000,7 +10424,7 @@
 
     # List All Automation Rules
     # 
-    resource function get sheets/[decimal sheetId]/automationrules(AutomationrulesListHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, AutomationrulesListQueries queries) returns AutomationRuleListResponse|error;
+    resource function get sheets/[decimal sheetId]/automationrules(AutomationrulesListHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, AutomationrulesListQueries queries) returns AutomationRuleListResponse|error;
 
     # Get an Automation Rule
     # 
@@ -10016,7 +10440,7 @@
 
     # List Columns
     # 
-    resource function get sheets/[decimal sheetId]/columns(ColumnsListOnSheetHeaders headers = {}, int level = 0, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ColumnsListOnSheetQueries queries) returns ColumnListResponse|error;
+    resource function get sheets/[decimal sheetId]/columns(ColumnsListOnSheetHeaders headers = {}, int level = 0, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ColumnsListOnSheetQueries queries) returns ColumnListResponse|error;
 
     # Add Columns
     # 
@@ -10024,7 +10448,7 @@
 
     # Get Column
     # 
-    resource function get sheets/[decimal sheetId]/columns/[decimal columnId](ColumnGetHeaders headers = {}, int level = 0, anydata Additional Values, ColumnGetQueries queries) returns ColumnResponse|error;
+    resource function get sheets/[decimal sheetId]/columns/[decimal columnId](ColumnGetHeaders headers = {}, int level = 0, ColumnGetQueries queries) returns ColumnResponse|error;
 
     # Update Column
     # 
@@ -10052,11 +10476,11 @@
 
     # Copy Sheet
     # 
-    resource function post sheets/[decimal sheetId]/copy(ContainerDestinationForCopy payload, CopySheetHeaders headers = {}, "attachments"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules"|"shares" include = "attachments", "sheetHyperlinks" exclude = "sheetHyperlinks", anydata Additional Values, CopySheetQueries queries) returns CrossSheetReferenceListResponse|error;
+    resource function post sheets/[decimal sheetId]/copy(ContainerDestinationForCopy payload, CopySheetHeaders headers = {}, "attachments"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules"|"shares" include = "attachments", "sheetHyperlinks" exclude = "sheetHyperlinks", CopySheetQueries queries) returns CrossSheetReferenceListResponse|error;
 
     # List Cross-sheet References
     # 
-    resource function get sheets/[decimal sheetId]/crosssheetreferences(ListCrosssheetReferencesHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ListCrosssheetReferencesQueries queries) returns CrossSheetReferenceCreateResponse|error;
+    resource function get sheets/[decimal sheetId]/crosssheetreferences(ListCrosssheetReferencesHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ListCrosssheetReferencesQueries queries) returns CrossSheetReferenceCreateResponse|error;
 
     # Create Cross-sheet References
     # 
@@ -10068,7 +10492,7 @@
 
     # List Discussions
     # 
-    resource function get sheets/[decimal sheetId]/discussions(DiscussionsListHeaders headers = {}, "attachments"|"comments" include = "attachments", decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, DiscussionsListQueries queries) returns DiscussionCreateResponse|error;
+    resource function get sheets/[decimal sheetId]/discussions(DiscussionsListHeaders headers = {}, "attachments"|"comments" include = "attachments", decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, DiscussionsListQueries queries) returns DiscussionCreateResponse|error;
 
     # Create a Discussion
     # 
@@ -10084,7 +10508,7 @@
 
     # List Discussion Attachments
     # 
-    resource function get sheets/[decimal sheetId]/discussions/[string discussionId]/attachments(DiscussionListAttachmentsHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, DiscussionListAttachmentsQueries queries) returns AttachmentVersionListResponse|error;
+    resource function get sheets/[decimal sheetId]/discussions/[string discussionId]/attachments(DiscussionListAttachmentsHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, DiscussionListAttachmentsQueries queries) returns AttachmentVersionListResponse|error;
 
     # Create a comment
     # 
@@ -10100,11 +10524,11 @@
 
     # List Proofs
     # 
-    resource function get sheets/[decimal sheetId]/proofs(ProofsGetAllProofsHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ProofsGetAllProofsQueries queries) returns ProofDetailListResponse|error;
+    resource function get sheets/[decimal sheetId]/proofs(ProofsGetAllProofsHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ProofsGetAllProofsQueries queries) returns ProofDetailListResponse|error;
 
     # Get Proof
     # 
-    resource function get sheets/[decimal sheetId]/proofs/[string proofId](ProofsGetHeaders headers = {}, "attachments"|"discussions" include = "attachments", anydata Additional Values, ProofsGetQueries queries) returns ProofResponse|error;
+    resource function get sheets/[decimal sheetId]/proofs/[string proofId](ProofsGetHeaders headers = {}, "attachments"|"discussions" include = "attachments", ProofsGetQueries queries) returns ProofResponse|error;
 
     # Update Proof Status
     # 
@@ -10116,7 +10540,7 @@
 
     # List Proof Attachments
     # 
-    resource function get sheets/[decimal sheetId]/proofs/[string proofId]/attachments(ProofsListAttachmentsHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ProofsListAttachmentsQueries queries) returns ProofAttachmentListResponse|error;
+    resource function get sheets/[decimal sheetId]/proofs/[string proofId]/attachments(ProofsListAttachmentsHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ProofsListAttachmentsQueries queries) returns ProofAttachmentListResponse|error;
 
     # Attach File to Proof
     # 
@@ -10124,7 +10548,7 @@
 
     # List Proof Discussions
     # 
-    resource function get sheets/[decimal sheetId]/proofs/[string proofId]/discussions(ProofsListDiscussionsHeaders headers = {}, "attachments"|"comments" include = "attachments", decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ProofsListDiscussionsQueries queries) returns ProofDiscussionListResponse|error;
+    resource function get sheets/[decimal sheetId]/proofs/[string proofId]/discussions(ProofsListDiscussionsHeaders headers = {}, "attachments"|"comments" include = "attachments", decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ProofsListDiscussionsQueries queries) returns ProofDiscussionListResponse|error;
 
     # Create Proof Discussion
     # 
@@ -10132,7 +10556,7 @@
 
     # List Proof Request Actions
     # 
-    resource function get sheets/[decimal sheetId]/proofs/[string proofId]/requestactions(ProofsListRequestActionsHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ProofsListRequestActionsQueries queries) returns ProofRequestActionListResponse|error;
+    resource function get sheets/[decimal sheetId]/proofs/[string proofId]/requestactions(ProofsListRequestActionsHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ProofsListRequestActionsQueries queries) returns ProofRequestActionListResponse|error;
 
     # Create Proof Request
     # 
@@ -10144,7 +10568,7 @@
 
     # List Proof Versions
     # 
-    resource function get sheets/[decimal sheetId]/proofs/[string proofId]/versions(ProofsGetVersionsHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ProofsGetVersionsQueries queries) returns ProofVersionListResponse|error;
+    resource function get sheets/[decimal sheetId]/proofs/[string proofId]/versions(ProofsGetVersionsHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ProofsGetVersionsQueries queries) returns ProofVersionListResponse|error;
 
     # Create Proof Version
     # 
@@ -10164,15 +10588,15 @@
 
     # Update Rows
     # 
-    resource function put sheets/[decimal sheetId]/rows(SheetIdRowsBody payload, UpdateRowsHeaders headers = {}, decimal accessApiLevel = 0.0d, boolean allowPartialSuccess = false, boolean overrideValidation = false, anydata Additional Values, UpdateRowsQueries queries) returns RowCopyResponse|error;
+    resource function put sheets/[decimal sheetId]/rows(SheetIdRowsBody payload, UpdateRowsHeaders headers = {}, decimal accessApiLevel = 0.0d, boolean allowPartialSuccess = false, boolean overrideValidation = false, UpdateRowsQueries queries) returns RowCopyResponse|error;
 
     # Add Rows
     # 
-    resource function post sheets/[decimal sheetId]/rows(SheetIdRowsBody1 payload, RowsAddToSheetHeaders headers = {}, decimal accessApiLevel = 0.0d, boolean allowPartialSuccess = false, boolean overrideValidation = false, anydata Additional Values, RowsAddToSheetQueries queries) returns RowMoveResponse|error;
+    resource function post sheets/[decimal sheetId]/rows(SheetIdRowsBody1 payload, RowsAddToSheetHeaders headers = {}, decimal accessApiLevel = 0.0d, boolean allowPartialSuccess = false, boolean overrideValidation = false, RowsAddToSheetQueries queries) returns RowMoveResponse|error;
 
     # Delete Rows
     # 
-    resource function delete sheets/[decimal sheetId]/rows(DeleteRowsHeaders headers = {}, string ids = "", boolean ignoreRowsNotFound = false, anydata Additional Values, DeleteRowsQueries queries) returns RowListResponse|error;
+    resource function delete sheets/[decimal sheetId]/rows(DeleteRowsHeaders headers = {}, string ids = "", boolean ignoreRowsNotFound = false, DeleteRowsQueries queries) returns RowListResponse|error;
 
     # Send Rows via Email
     # 
@@ -10180,19 +10604,19 @@
 
     # Copy Rows to Another Sheet
     # 
-    resource function post sheets/[decimal sheetId]/rows/copy(CopyOrMoveRowDirective payload, CopyRowsHeaders headers = {}, "all"|"attachments"|"children"|"discussions" include = "all", boolean ignoreRowsNotFound = false, anydata Additional Values, CopyRowsQueries queries) returns CopyOrMoveRowResult|error;
+    resource function post sheets/[decimal sheetId]/rows/copy(CopyOrMoveRowDirective payload, CopyRowsHeaders headers = {}, "all"|"attachments"|"children"|"discussions" include = "all", boolean ignoreRowsNotFound = false, CopyRowsQueries queries) returns CopyOrMoveRowResult|error;
 
     # Move Rows to Another Sheet
     # 
-    resource function post sheets/[decimal sheetId]/rows/move(CopyOrMoveRowDirective payload, MoveRowsHeaders headers = {}, "attachments"|"discussions" include = "attachments", boolean ignoreRowsNotFound = false, anydata Additional Values, MoveRowsQueries queries) returns CopyOrMoveRowResult|error;
+    resource function post sheets/[decimal sheetId]/rows/move(CopyOrMoveRowDirective payload, MoveRowsHeaders headers = {}, "attachments"|"discussions" include = "attachments", boolean ignoreRowsNotFound = false, MoveRowsQueries queries) returns CopyOrMoveRowResult|error;
 
     # Get Row
     # 
-    resource function get sheets/[decimal sheetId]/rows/[decimal rowId](RowGetHeaders headers = {}, decimal accessApiLevel = 0.0d, "columns"|"filters" include = "columns", int level = 0, "filteredOutRows"|"linkInFromCellDetails"|"linksOutToCellsDetails"|"nonexistentCells" exclude = "filteredOutRows", anydata Additional Values, RowGetQueries queries) returns RowResponse|error;
+    resource function get sheets/[decimal sheetId]/rows/[decimal rowId](RowGetHeaders headers = {}, decimal accessApiLevel = 0.0d, "columns"|"filters" include = "columns", int level = 0, "filteredOutRows"|"linkInFromCellDetails"|"linksOutToCellsDetails"|"nonexistentCells" exclude = "filteredOutRows", RowGetQueries queries) returns RowResponse|error;
 
     # List Row Attachments
     # 
-    resource function get sheets/[decimal sheetId]/rows/[decimal rowId]/attachments(AttachmentsListOnRowHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, AttachmentsListOnRowQueries queries) returns AttachmentVersionListResponse|error;
+    resource function get sheets/[decimal sheetId]/rows/[decimal rowId]/attachments(AttachmentsListOnRowHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, AttachmentsListOnRowQueries queries) returns AttachmentVersionListResponse|error;
 
     # Attach File or URL to Row
     # 
@@ -10200,15 +10624,15 @@
 
     # Add Image to Cell
     # 
-    resource function post sheets/[decimal sheetId]/rows/[decimal rowId]/columns/[decimal columnId]/cellimages(byte[] payload, AddImageToCellHeaders headers = {}, string altText = "", boolean overrideValidation = false, anydata Additional Values, AddImageToCellQueries queries) returns RowCreateResponse|error;
+    resource function post sheets/[decimal sheetId]/rows/[decimal rowId]/columns/[decimal columnId]/cellimages(byte[] payload, AddImageToCellHeaders headers = {}, string altText = "", boolean overrideValidation = false, AddImageToCellQueries queries) returns RowCreateResponse|error;
 
     # List Cell History
     # 
-    resource function get sheets/[decimal sheetId]/rows/[decimal rowId]/columns/[decimal columnId]/history(CellHistoryGetHeaders headers = {}, "columnType"|"objectValue" include = "columnType", int level = 0, decimal pageSize = 0.0d, decimal page = 0.0d, anydata Additional Values, CellHistoryGetQueries queries) returns RowAttachmentListResponse|error;
+    resource function get sheets/[decimal sheetId]/rows/[decimal rowId]/columns/[decimal columnId]/history(CellHistoryGetHeaders headers = {}, "columnType"|"objectValue" include = "columnType", int level = 0, decimal pageSize = 0.0d, decimal page = 0.0d, CellHistoryGetQueries queries) returns RowAttachmentListResponse|error;
 
     # List Discussions with a Row
     # 
-    resource function get sheets/[decimal sheetId]/rows/[decimal rowId]/discussions(RowDiscussionsListHeaders headers = {}, "attachments"|"comments" include = "attachments", decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, RowDiscussionsListQueries queries) returns DiscussionCreateResponse|error;
+    resource function get sheets/[decimal sheetId]/rows/[decimal rowId]/discussions(RowDiscussionsListHeaders headers = {}, "attachments"|"comments" include = "attachments", decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, RowDiscussionsListQueries queries) returns DiscussionCreateResponse|error;
 
     # Create a Discussion on a Row
     # 
@@ -10220,7 +10644,7 @@
 
     # List Sent Update Requests
     # 
-    resource function get sheets/[decimal sheetId]/sentupdaterequests(SentupdaterequestsListHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, SentupdaterequestsListQueries queries) returns SentUpdateRequestListResponse|error;
+    resource function get sheets/[decimal sheetId]/sentupdaterequests(SentupdaterequestsListHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, SentupdaterequestsListQueries queries) returns SentUpdateRequestListResponse|error;
 
     # Get Sent Update Request
     # 
@@ -10232,31 +10656,31 @@
 
     # Get Sheet Summary
     # 
-    resource function get sheets/[decimal sheetId]/summary(ListSummaryFieldsHeaders headers = {}, "format"|"writerInfo" include = "format", "displayValue"|"image"|"imageAltText" exclude = "displayValue", anydata Additional Values, ListSummaryFieldsQueries queries) returns SheetSummary|error;
+    resource function get sheets/[decimal sheetId]/summary(ListSummaryFieldsHeaders headers = {}, "format"|"writerInfo" include = "format", "displayValue"|"image"|"imageAltText" exclude = "displayValue", ListSummaryFieldsQueries queries) returns SheetSummary|error;
 
     # Get Summary Fields
     # 
-    resource function get sheets/[decimal sheetId]/summary/fields(ListSummaryFieldsPaginatedHeaders headers = {}, "format"|"writerInfo" include = "format", decimal pageSize = 0.0d, boolean includeAll = false, "displayValue"|"image"|"imageAltText" exclude = "displayValue", decimal page = 0.0d, anydata Additional Values, ListSummaryFieldsPaginatedQueries queries) returns SummaryFieldListResponse|error;
+    resource function get sheets/[decimal sheetId]/summary/fields(ListSummaryFieldsPaginatedHeaders headers = {}, "format"|"writerInfo" include = "format", decimal pageSize = 0.0d, boolean includeAll = false, "displayValue"|"image"|"imageAltText" exclude = "displayValue", decimal page = 0.0d, ListSummaryFieldsPaginatedQueries queries) returns SummaryFieldListResponse|error;
 
     # Update Summary Fields
     # 
-    resource function put sheets/[decimal sheetId]/summary/fields(SummaryFieldUpdateRequest[] payload, UpdateSummaryFieldsHeaders headers = {}, boolean renameIfConflict = false, anydata Additional Values, UpdateSummaryFieldsQueries queries) returns SummaryFieldCreateResponse|error;
+    resource function put sheets/[decimal sheetId]/summary/fields(SummaryFieldUpdateRequest[] payload, UpdateSummaryFieldsHeaders headers = {}, boolean renameIfConflict = false, UpdateSummaryFieldsQueries queries) returns SummaryFieldCreateResponse|error;
 
     # Add Summary Fields
     # 
-    resource function post sheets/[decimal sheetId]/summary/fields(SummaryFieldCreateRequest[] payload, AddSummaryFieldsHeaders headers = {}, boolean renameIfConflict = false, anydata Additional Values, AddSummaryFieldsQueries queries) returns SummaryFieldBulkCreateResponse|error;
+    resource function post sheets/[decimal sheetId]/summary/fields(SummaryFieldCreateRequest[] payload, AddSummaryFieldsHeaders headers = {}, boolean renameIfConflict = false, AddSummaryFieldsQueries queries) returns SummaryFieldBulkCreateResponse|error;
 
     # Delete Summary Fields
     # 
-    resource function delete sheets/[decimal sheetId]/summary/fields(DeleteSummaryFieldsHeaders headers = {}, boolean ignoreSummaryFieldsNotFound = false, string ids = "", anydata Additional Values, DeleteSummaryFieldsQueries queries) returns SummaryFieldDeleteResponse|error;
+    resource function delete sheets/[decimal sheetId]/summary/fields(DeleteSummaryFieldsHeaders headers = {}, boolean ignoreSummaryFieldsNotFound = false, string ids = "", DeleteSummaryFieldsQueries queries) returns SummaryFieldDeleteResponse|error;
 
     # Add Image to Sheet Summary
     # 
-    resource function post sheets/[decimal sheetId]/summary/fields/[decimal fieldId]/images(byte[] payload, AddImageSummaryFieldHeaders headers = {}, string altText = "", boolean overrideValidation = false, anydata Additional Values, AddImageSummaryFieldQueries queries) returns SummaryResponse|error;
+    resource function post sheets/[decimal sheetId]/summary/fields/[decimal fieldId]/images(byte[] payload, AddImageSummaryFieldHeaders headers = {}, string altText = "", boolean overrideValidation = false, AddImageSummaryFieldQueries queries) returns SummaryResponse|error;
 
     # List Update Requests
     # 
-    resource function get sheets/[decimal sheetId]/updaterequests(UpdaterequestsListHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, UpdaterequestsListQueries queries) returns UpdateRequestListResponse|error;
+    resource function get sheets/[decimal sheetId]/updaterequests(UpdaterequestsListHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, UpdaterequestsListQueries queries) returns UpdateRequestListResponse|error;
 
     # Create an Update Request
     # 
@@ -10276,27 +10700,27 @@
 
     # List Sheet Shares
     # 
-    resource function get sheets/[decimal sheetId]/shares(ListSheetSharesHeaders headers = {}, decimal accessApiLevel = 0.0d, "ITEM"|"WORKSPACE" sharingInclude = "ITEM", decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ListSheetSharesQueries queries) returns PublicTemplateListResponse|error;
+    resource function get sheets/[decimal sheetId]/shares(ListSheetSharesHeaders headers = {}, decimal accessApiLevel = 0.0d, "ITEM"|"WORKSPACE" sharingInclude = "ITEM", decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ListSheetSharesQueries queries) returns PublicTemplateListResponse|error;
 
     # Share Sheet
     # 
-    resource function post sheets/[decimal sheetId]/shares(SheetIdSharesBody payload, ShareSheetHeaders headers = {}, decimal accessApiLevel = 0.0d, boolean sendEmail = false, anydata Additional Values, ShareSheetQueries queries) returns TokenResponse|error;
+    resource function post sheets/[decimal sheetId]/shares(SheetIdSharesBody payload, ShareSheetHeaders headers = {}, decimal accessApiLevel = 0.0d, boolean sendEmail = false, ShareSheetQueries queries) returns TokenResponse|error;
 
     # Get Sheet Share.
     # 
-    resource function get sheets/[decimal sheetId]/shares/[string shareId](ShareSheetGetHeaders headers = {}, decimal accessApiLevel = 0.0d, anydata Additional Values, ShareSheetGetQueries queries) returns Share|error;
+    resource function get sheets/[decimal sheetId]/shares/[string shareId](ShareSheetGetHeaders headers = {}, decimal accessApiLevel = 0.0d, ShareSheetGetQueries queries) returns Share|error;
 
     # Update Sheet Share.
     # 
-    resource function put sheets/[decimal sheetId]/shares/[string shareId](SharesshareIdBody payload, UpdateSheetShareHeaders headers = {}, decimal accessApiLevel = 0.0d, anydata Additional Values, UpdateSheetShareQueries queries) returns UserResponse|error;
+    resource function put sheets/[decimal sheetId]/shares/[string shareId](SharesshareIdBody payload, UpdateSheetShareHeaders headers = {}, decimal accessApiLevel = 0.0d, UpdateSheetShareQueries queries) returns UserResponse|error;
 
     # Delete Sheet Share
     # 
-    resource function delete sheets/[decimal sheetId]/shares/[string shareId](DeleteSheetShareHeaders headers = {}, decimal accessApiLevel = 0.0d, anydata Additional Values, DeleteSheetShareQueries queries) returns Result|error;
+    resource function delete sheets/[decimal sheetId]/shares/[string shareId](DeleteSheetShareHeaders headers = {}, decimal accessApiLevel = 0.0d, DeleteSheetShareQueries queries) returns Result|error;
 
     # Sort Rows in Sheet
     # 
-    resource function post sheets/[decimal sheetId]/sort(SortSpecifier payload, RowsSortHeaders headers = {}, string includeExclude = "", anydata Additional Values, RowsSortQueries queries) returns SheetResponse|error;
+    resource function post sheets/[decimal sheetId]/sort(SortSpecifier payload, RowsSortHeaders headers = {}, string includeExclude = "", RowsSortQueries queries) returns SheetResponse|error;
 
     # Get Sheet Version
     # 
@@ -10304,15 +10728,15 @@
 
     # List Dashboards
     # 
-    resource function get sights(ListSightsHeaders headers = {}, Timestamp modifiedSince = "", boolean numericDates = false, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ListSightsQueries queries) returns DashboardListResponse|error;
+    resource function get sights(ListSightsHeaders headers = {}, Timestamp modifiedSince = "", boolean numericDates = false, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ListSightsQueries queries) returns DashboardListResponse|error;
 
     # Get Dashboard
     # 
-    resource function get sights/[string sightId](GetSightHeaders headers = {}, decimal accessApiLevel = 0.0d, "objectValue"|"source" include = "objectValue", int level = 0, boolean numericDates = false, anydata Additional Values, GetSightQueries queries) returns Sight|error;
+    resource function get sights/[string sightId](GetSightHeaders headers = {}, decimal accessApiLevel = 0.0d, "objectValue"|"source" include = "objectValue", int level = 0, boolean numericDates = false, GetSightQueries queries) returns Sight|error;
 
     # Update Dashboard
     # 
-    resource function put sights/[string sightId](SightName payload, UpdateSightHeaders headers = {}, boolean numericDates = false, anydata Additional Values, UpdateSightQueries queries) returns ShareResponse|error;
+    resource function put sights/[string sightId](SightName payload, UpdateSightHeaders headers = {}, boolean numericDates = false, UpdateSightQueries queries) returns ShareResponse|error;
 
     # Delete Dashboard
     # 
@@ -10336,19 +10760,19 @@
 
     # List Dashboard Shares
     # 
-    resource function get sights/[string sightId]/shares(ListSightSharesHeaders headers = {}, decimal accessApiLevel = 0.0d, "ITEM"|"WORKSPACE" sharingInclude = "ITEM", decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ListSightSharesQueries queries) returns PublicTemplateListResponse|error;
+    resource function get sights/[string sightId]/shares(ListSightSharesHeaders headers = {}, decimal accessApiLevel = 0.0d, "ITEM"|"WORKSPACE" sharingInclude = "ITEM", decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ListSightSharesQueries queries) returns PublicTemplateListResponse|error;
 
     # Share Dashboard
     # 
-    resource function post sights/[string sightId]/shares(Share payload, ShareSightHeaders headers = {}, decimal accessApiLevel = 0.0d, boolean sendEmail = false, anydata Additional Values, ShareSightQueries queries) returns TokenResponse|error;
+    resource function post sights/[string sightId]/shares(Share payload, ShareSightHeaders headers = {}, decimal accessApiLevel = 0.0d, boolean sendEmail = false, ShareSightQueries queries) returns TokenResponse|error;
 
     # Get Dashboard Share
     # 
-    resource function get sights/[string sightId]/shares/[string shareId](ShareSightGetHeaders headers = {}, decimal accessApiLevel = 0.0d, anydata Additional Values, ShareSightGetQueries queries) returns Share|error;
+    resource function get sights/[string sightId]/shares/[string shareId](ShareSightGetHeaders headers = {}, decimal accessApiLevel = 0.0d, ShareSightGetQueries queries) returns Share|error;
 
     # Update Dashboard Share
     # 
-    resource function put sights/[string sightId]/shares/[string shareId](SharesshareIdBody payload, UpdateSightShareHeaders headers = {}, decimal accessApiLevel = 0.0d, anydata Additional Values, UpdateSightShareQueries queries) returns UserResponse|error;
+    resource function put sights/[string sightId]/shares/[string shareId](SharesshareIdBody payload, UpdateSightShareHeaders headers = {}, decimal accessApiLevel = 0.0d, UpdateSightShareQueries queries) returns UserResponse|error;
 
     # Delete Dashboard Share
     # 
@@ -10356,35 +10780,35 @@
 
     # List User-Created Templates
     # 
-    resource function get templates(TemplatesListHeaders headers = {}, decimal accessApiLevel = 0.0d, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, TemplatesListQueries queries) returns WorkspaceListResponse|error;
+    resource function get templates(TemplatesListHeaders headers = {}, decimal accessApiLevel = 0.0d, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, TemplatesListQueries queries) returns WorkspaceListResponse|error;
 
     # List Public Templates
     # 
-    resource function get templates/'public(TemplatesListPublicHeaders headers = {}, decimal accessApiLevel = 0.0d, 0|1 level = 0, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, TemplatesListPublicQueries queries) returns WorkspaceListResponse|error;
+    resource function get templates/'public(TemplatesListPublicHeaders headers = {}, decimal accessApiLevel = 0.0d, 0|1 level = 0, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, TemplatesListPublicQueries queries) returns WorkspaceListResponse|error;
 
     # Gets or Refreshes an Access Token
     # 
-    resource function post token(TokensGetOrRefreshHeaders headers = {}, string refreshToken = "", string code = "", "authorization_code"|"refresh_token" grantType = "authorization_code", string clientSecret = "", string clientId = "", string hash = "", string redirectUrl = "", anydata Additional Values, TokensGetOrRefreshQueries queries) returns Token|error;
+    resource function post token(TokensGetOrRefreshHeaders headers = {}, string refreshToken = "", string code = "", "authorization_code"|"refresh_token" grantType = "authorization_code", string clientSecret = "", string clientId = "", string hash = "", string redirectUrl = "", TokensGetOrRefreshQueries queries) returns Token|error;
 
     # Revoke Access Token
     # 
-    resource function delete token(TokensDeleteHeaders headers = {}, boolean deleteAllForApiClient = false, anydata Additional Values, TokensDeleteQueries queries) returns Result|error;
+    resource function delete token(TokensDeleteHeaders headers = {}, boolean deleteAllForApiClient = false, TokensDeleteQueries queries) returns Result|error;
 
     # List Users
     # 
-    resource function get users(ListUsersHeaders headers = {}, string include = "", boolean numericDates = false, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, string email = "", anydata Additional Values, ListUsersQueries queries) returns UserListResponse|error;
+    resource function get users(ListUsersHeaders headers = {}, string include = "", boolean numericDates = false, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, string email = "", ListUsersQueries queries) returns UserListResponse|error;
 
     # Add User
     # 
-    resource function post users(User payload, AddUserHeaders headers = {}, boolean sendEmail = false, anydata Additional Values, AddUserQueries queries) returns UserProfileResponse|error;
+    resource function post users(User payload, AddUserHeaders headers = {}, boolean sendEmail = false, AddUserQueries queries) returns UserProfileResponse|error;
 
     # Get Current User
     # 
-    resource function get users/me(GetCurrentUserHeaders headers = {}, "groups" include = "groups", anydata Additional Values, GetCurrentUserQueries queries) returns UserImgProfileResponse|error;
+    resource function get users/me(GetCurrentUserHeaders headers = {}, "groups" include = "groups", GetCurrentUserQueries queries) returns UserImgProfileResponse|error;
 
     # List Org Sheets
     # 
-    resource function get users/sheets(ListOrgSheetsHeaders headers = {}, Timestamp modifiedSince = "", anydata Additional Values, ListOrgSheetsQueries queries) returns HomeContentsResponse|error;
+    resource function get users/sheets(ListOrgSheetsHeaders headers = {}, Timestamp modifiedSince = "", ListOrgSheetsQueries queries) returns HomeContentsResponse|error;
 
     # Get User
     # 
@@ -10396,7 +10820,7 @@
 
     # Remove User
     # 
-    resource function delete users/[decimal userId](RemoveUserHeaders headers = {}, boolean removeFromSharing = false, boolean transferSheets = false, int transferTo = 0, anydata Additional Values, RemoveUserQueries queries) returns GenericResult|error;
+    resource function delete users/[decimal userId](RemoveUserHeaders headers = {}, boolean removeFromSharing = false, boolean transferSheets = false, int transferTo = 0, RemoveUserQueries queries) returns GenericResult|error;
 
     # List Alternate Emails
     # 
@@ -10432,7 +10856,7 @@
 
     # List Webhooks
     # 
-    resource function get webhooks(ListWebhooksHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ListWebhooksQueries queries) returns WorkspaceFolderListResponse|error;
+    resource function get webhooks(ListWebhooksHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ListWebhooksQueries queries) returns WorkspaceFolderListResponse|error;
 
     # Create Webhook
     # 
@@ -10456,19 +10880,19 @@
 
     # List Workspaces
     # 
-    resource function get workspaces(ListWorkspacesHeaders headers = {}, decimal accessApiLevel = 0.0d, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ListWorkspacesQueries queries) returns WorkspaceShareListResponse|error;
+    resource function get workspaces(ListWorkspacesHeaders headers = {}, decimal accessApiLevel = 0.0d, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ListWorkspacesQueries queries) returns WorkspaceShareListResponse|error;
 
     # Create Workspace
     # 
-    resource function post workspaces(WorkspacesBody payload, CreateWorkspaceHeaders headers = {}, decimal accessApiLevel = 0.0d, "all"|"attachments"|"brand"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules"|"shares" include = "all", "cellLinks"|"reports"|"sheetHyperlinks"|"sights" skipRemap = "cellLinks", anydata Additional Values, CreateWorkspaceQueries queries) returns WorkspaceResponse|error;
+    resource function post workspaces(WorkspacesBody payload, CreateWorkspaceHeaders headers = {}, decimal accessApiLevel = 0.0d, "all"|"attachments"|"brand"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules"|"shares" include = "all", "cellLinks"|"reports"|"sheetHyperlinks"|"sights" skipRemap = "cellLinks", CreateWorkspaceQueries queries) returns WorkspaceResponse|error;
 
     # Get Workspace
     # 
-    resource function get workspaces/[string workspaceId](GetWorkspaceHeaders headers = {}, decimal accessApiLevel = 0.0d, "source"|"distributionLink"|"ownerInfo"|"sheetVersion" include = "source", boolean loadAll = false, anydata Additional Values, GetWorkspaceQueries queries) returns Workspace|error;
+    resource function get workspaces/[string workspaceId](GetWorkspaceHeaders headers = {}, decimal accessApiLevel = 0.0d, "source"|"distributionLink"|"ownerInfo"|"sheetVersion" include = "source", boolean loadAll = false, GetWorkspaceQueries queries) returns Workspace|error;
 
     # Update Workspace
     # 
-    resource function put workspaces/[string workspaceId](WorkspacesworkspaceIdBody payload, UpdateWorkspaceHeaders headers = {}, decimal accessApiLevel = 0.0d, anydata Additional Values, UpdateWorkspaceQueries queries) returns WorkspaceCreateResponse|error;
+    resource function put workspaces/[string workspaceId](WorkspacesworkspaceIdBody payload, UpdateWorkspaceHeaders headers = {}, decimal accessApiLevel = 0.0d, UpdateWorkspaceQueries queries) returns WorkspaceCreateResponse|error;
 
     # Delete Workspace
     # 
@@ -10476,11 +10900,11 @@
 
     # Copy Workspace
     # 
-    resource function post workspaces/[string workspaceId]/copy(WorkspaceIdCopyBody payload, CopyWorkspaceHeaders headers = {}, "all"|"attachments"|"brand"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules"|"shares" include = "all", "cellLinks"|"reports"|"sheetHyperlinks"|"sights" skipRemap = "cellLinks", anydata Additional Values, CopyWorkspaceQueries queries) returns ContainerDestinationForCopy|error;
+    resource function post workspaces/[string workspaceId]/copy(WorkspaceIdCopyBody payload, CopyWorkspaceHeaders headers = {}, "all"|"attachments"|"brand"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules"|"shares" include = "all", "cellLinks"|"reports"|"sheetHyperlinks"|"sights" skipRemap = "cellLinks", CopyWorkspaceQueries queries) returns ContainerDestinationForCopy|error;
 
     # List Workspace Folders
     # 
-    resource function get workspaces/[string workspaceId]/folders(GetWorkspaceFoldersHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, GetWorkspaceFoldersQueries queries) returns FolderContentsResponse|error;
+    resource function get workspaces/[string workspaceId]/folders(GetWorkspaceFoldersHeaders headers = {}, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, GetWorkspaceFoldersQueries queries) returns FolderContentsResponse|error;
 
     # Create a Folder
     # 
@@ -10488,19 +10912,19 @@
 
     # List Workspace Shares
     # 
-    resource function get workspaces/[string workspaceId]/shares(ListWorkspaceSharesHeaders headers = {}, decimal accessApiLevel = 0.0d, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, anydata Additional Values, ListWorkspaceSharesQueries queries) returns PublicTemplateListResponse|error;
+    resource function get workspaces/[string workspaceId]/shares(ListWorkspaceSharesHeaders headers = {}, decimal accessApiLevel = 0.0d, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ListWorkspaceSharesQueries queries) returns PublicTemplateListResponse|error;
 
     # Share Workspace
     # 
-    resource function post workspaces/[string workspaceId]/shares(WorkspaceIdSharesBody payload, ShareWorkspaceHeaders headers = {}, decimal accessApiLevel = 0.0d, boolean sendEmail = false, anydata Additional Values, ShareWorkspaceQueries queries) returns TokenResponse|error;
+    resource function post workspaces/[string workspaceId]/shares(WorkspaceIdSharesBody payload, ShareWorkspaceHeaders headers = {}, decimal accessApiLevel = 0.0d, boolean sendEmail = false, ShareWorkspaceQueries queries) returns TokenResponse|error;
 
     # Get Workspace Share
     # 
-    resource function get workspaces/[string workspaceId]/shares/[string shareId](ShareWorkspaceGetHeaders headers = {}, decimal accessApiLevel = 0.0d, anydata Additional Values, ShareWorkspaceGetQueries queries) returns Share|error;
+    resource function get workspaces/[string workspaceId]/shares/[string shareId](ShareWorkspaceGetHeaders headers = {}, decimal accessApiLevel = 0.0d, ShareWorkspaceGetQueries queries) returns Share|error;
 
     # Update Workspace Share
     # 
-    resource function put workspaces/[string workspaceId]/shares/[string shareId](SharesshareIdBody payload, UpdateWorkspaceShareHeaders headers = {}, decimal accessApiLevel = 0.0d, anydata Additional Values, UpdateWorkspaceShareQueries queries) returns UserResponse|error;
+    resource function put workspaces/[string workspaceId]/shares/[string shareId](SharesshareIdBody payload, UpdateWorkspaceShareHeaders headers = {}, decimal accessApiLevel = 0.0d, UpdateWorkspaceShareQueries queries) returns UserResponse|error;
 
     # Delete Workspace Share
     # 
@@ -10508,9 +10932,9 @@
 
     # Create Sheet in Workspace
     # 
-    resource function post workspaces/[string workspaceId]/sheets(WorkspaceIdSheetsBody payload, CreateSheetInWorkspaceHeaders headers = {}, decimal accessApiLevel = 0.0d, "attachments"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules" include = "attachments", anydata Additional Values, CreateSheetInWorkspaceQueries queries) returns WebhookResponse|error;
+    resource function post workspaces/[string workspaceId]/sheets(WorkspaceIdSheetsBody payload, CreateSheetInWorkspaceHeaders headers = {}, decimal accessApiLevel = 0.0d, "attachments"|"cellLinks"|"data"|"discussions"|"filters"|"forms"|"ruleRecipients"|"rules" include = "attachments", CreateSheetInWorkspaceQueries queries) returns WebhookResponse|error;
 
     # Import Sheet into Workspace
     # 
-    resource function post workspaces/[string workspaceId]/sheets/'import(ImportSheetIntoWorkspaceHeaders headers, byte[] payload, string sheetName = "", decimal headerRowIndex = 0.0d, decimal primaryColumnIndex = 0.0d, anydata Additional Values, ImportSheetIntoWorkspaceQueries queries) returns WebhookListResponse|error;
+    resource function post workspaces/[string workspaceId]/sheets/'import(ImportSheetIntoWorkspaceHeaders headers, byte[] payload, string sheetName = "", decimal headerRowIndex = 0.0d, decimal primaryColumnIndex = 0.0d, ImportSheetIntoWorkspaceQueries queries) returns WebhookListResponse|error;
 }
`````
