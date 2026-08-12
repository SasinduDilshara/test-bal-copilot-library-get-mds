# jira — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `jira` |
| **Old file** | `jira/old/ballerinax_jira.bal.txt` |
| **New file** | `jira/new/ballerinax_jira.bal.txt` |
| **Old lines** | 16649 |
| **New lines** | 16749 |
| **Lines added** | 637 |
| **Lines removed** | 537 |
| **Hunks** | 407 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 6 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 327 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (6)

- `type BulkGetUsersQueriesAccountIdItemsString`
- `type CreatePrioritySchemeDetailsPriorityIdsItemsInteger`
- `type GetUserEmailBulkQueriesAccountIdItemsString`
- `type GetWorkflowTransitionRuleConfigurationsQueriesWithTagsItemsString`
- `type GetWorkflowTransitionRuleConfigurationsQueriesWorkflowNamesItemsString`
- `type JqlQueriesToParseQueriesItemsString`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 316–321 | 316–322 | Types | +1 | −0 |
| 2 | 327–332 | 328–334 | Types | +1 | −0 |
| 3 | 370–376 | 372–378 | Types | +1 | −1 |
| 4 | 385–390 | 387–393 | Types | +1 | −0 |
| 5 | 456–467 | 459–471 | Types | +2 | −1 |
| 6 | 588–593 | 592–598 | Types | +1 | −0 |
| 7 | 675–681 | 680–686 | Types | +1 | −1 |
| 8 | 688–694 | 693–699 | Types | +1 | −1 |
| 9 | 735–740 | 740–746 | Types | +1 | −0 |
| 10 | 748–754 | 754–760 | Types | +1 | −1 |
| 11 | 778–785 | 784–792 | Types | +3 | −2 |
| 12 | 829–835 | 836–842 | Types | +1 | −1 |
| 13 | 841–847 | 848–854 | Types | +1 | −1 |
| 14 | 865–871 | 872–878 | Types | +1 | −1 |
| 15 | 919–925 | 926–932 | Types | +1 | −1 |
| 16 | 948–955 | 955–963 | Types | +3 | −2 |
| 17 | 969–985 | 977–993 | Types | +3 | −3 |
| 18 | 1191–1197 | 1199–1205 | Types | +1 | −1 |
| 19 | 1240–1245 | 1248–1254 | Types | +1 | −0 |
| 20 | 1310–1316 | 1319–1325 | Types | +1 | −1 |
| 21 | 1337–1343 | 1346–1353 | Types | +2 | −1 |
| 22 | 1347–1353 | 1357–1363 | Types | +1 | −1 |
| 23 | 1600–1606 | 1610–1616 | Types | +1 | −1 |
| 24 | 1622–1635 | 1632–1645 | Types | +2 | −2 |
| 25 | 1815–1821 | 1825–1831 | Types | +1 | −1 |
| 26 | 1858–1864 | 1868–1874 | Types | +1 | −1 |
| 27 | 1872–1877 | 1882–1888 | Types | +1 | −0 |
| 28 | 1928–1940 | 1939–1951 | Types | +3 | −3 |
| 29 | 2026–2034 | 2037–2045 | Types | +2 | −2 |
| 30 | 2042–2047 | 2053–2059 | Types | +1 | −0 |
| 31 | 2204–2212 | 2216–2224 | Types | +2 | −2 |
| 32 | 2275–2281 | 2287–2293 | Types | +1 | −1 |
| 33 | 2298–2303 | 2310–2316 | Types | +1 | −0 |
| 34 | 2322–2328 | 2335–2341 | Types | +1 | −1 |
| 35 | 2385–2391 | 2398–2404 | Types | +1 | −1 |
| 36 | 2402–2408 | 2415–2421 | Types | +1 | −1 |
| 37 | 2468–2479 | 2481–2495 | Types | +4 | −1 |
| 38 | 2496–2502 | 2512–2519 | Types | +2 | −1 |
| 39 | 2505–2518 | 2522–2538 | Types | +5 | −2 |
| 40 | 2542–2548 | 2562–2568 | Types | +1 | −1 |
| 41 | 2578–2584 | 2598–2604 | Types | +1 | −1 |
| 42 | 2609–2619 | 2629–2639 | Types | +3 | −3 |
| 43 | 2674–2680 | 2694–2700 | Types | +1 | −1 |
| 44 | 2708–2714 | 2728–2734 | Types | +1 | −1 |
| 45 | 2753–2758 | 2773–2779 | Types | +1 | −0 |
| 46 | 2796–2802 | 2817–2823 | Types | +1 | −1 |
| 47 | 2814–2820 | 2835–2841 | Types | +1 | −1 |
| 48 | 2875–2881 | 2896–2902 | Types | +1 | −1 |
| 49 | 2884–2898 | 2905–2919 | Types | +3 | −3 |
| 50 | 2901–2907 | 2922–2928 | Types | +1 | −1 |
| 51 | 2914–2920 | 2935–2941 | Types | +1 | −1 |
| 52 | 2930–2935 | 2951–2957 | Types | +1 | −0 |
| 53 | 3071–3076 | 3093–3099 | Types | +1 | −0 |
| 54 | 3219–3225 | 3242–3248 | Types | +1 | −1 |
| 55 | 3261–3268 | 3284–3293 | Types | +4 | −2 |
| 56 | 3279–3285 | 3304–3310 | Types | +1 | −1 |
| 57 | 3422–3428 | 3447–3453 | Types | +1 | −1 |
| 58 | 3445–3451 | 3470–3476 | Types | +1 | −1 |
| 59 | 3491–3497 | 3516–3522 | Types | +1 | −1 |
| 60 | 3580–3586 | 3605–3611 | Types | +1 | −1 |
| 61 | 3595–3609 | 3620–3634 | Types | +3 | −3 |
| 62 | 3643–3649 | 3668–3674 | Types | +1 | −1 |
| 63 | 3667–3675 | 3692–3700 | Types | +2 | −2 |
| 64 | 3678–3684 | 3703–3709 | Types | +1 | −1 |
| 65 | 3704–3710 | 3729–3735 | Types | +1 | −1 |
| 66 | 4010–4016 | 4035–4041 | Types | +1 | −1 |
| 67 | 4098–4104 | 4123–4129 | Types | +1 | −1 |
| 68 | 4146–4152 | 4171–4177 | Types | +1 | −1 |
| 69 | 4186–4192 | 4211–4217 | Types | +1 | −1 |
| 70 | 4205–4211 | 4230–4236 | Types | +1 | −1 |
| 71 | 4219–4225 | 4244–4250 | Types | +1 | −1 |
| 72 | 4230–4236 | 4255–4261 | Types | +1 | −1 |
| 73 | 4259–4265 | 4284–4290 | Types | +1 | −1 |
| 74 | 4320–4326 | 4345–4351 | Types | +1 | −1 |
| 75 | 4337–4343 | 4362–4368 | Types | +1 | −1 |
| 76 | 4348–4358 | 4373–4383 | Types | +2 | −2 |
| 77 | 4444–4450 | 4469–4475 | Types | +1 | −1 |
| 78 | 4462–4468 | 4487–4493 | Types | +1 | −1 |
| 79 | 4510–4516 | 4535–4541 | Types | +1 | −1 |
| 80 | 4533–4545 | 4558–4571 | Types | +2 | −1 |
| 81 | 4549–4554 | 4575–4581 | Types | +1 | −0 |
| 82 | 4595–4600 | 4622–4628 | Types | +1 | −0 |
| 83 | 4608–4614 | 4636–4642 | Types | +1 | −1 |
| 84 | 4650–4656 | 4678–4684 | Types | +1 | −1 |
| 85 | 4691–4697 | 4719–4725 | Types | +1 | −1 |
| 86 | 4744–4750 | 4772–4778 | Types | +1 | −1 |
| 87 | 4819–4827 | 4847–4856 | Types | +2 | −1 |
| 88 | 4843–4849 | 4872–4878 | Types | +1 | −1 |
| 89 | 4892–4897 | 4921–4927 | Types | +1 | −0 |
| 90 | 5025–5031 | 5055–5061 | Types | +1 | −1 |
| 91 | 5054–5060 | 5084–5090 | Types | +1 | −1 |
| 92 | 5069–5076 | 5099–5108 | Types | +2 | −0 |
| 93 | 5085–5091 | 5117–5123 | Types | +1 | −1 |
| 94 | 5172–5178 | 5204–5210 | Types | +1 | −1 |
| 95 | 5210–5215 | 5242–5248 | Types | +1 | −0 |
| 96 | 5266–5272 | 5299–5305 | Types | +1 | −1 |
| 97 | 5387–5393 | 5420–5426 | Types | +1 | −1 |
| 98 | 5421–5427 | 5454–5460 | Types | +1 | −1 |
| 99 | 5456–5462 | 5489–5495 | Types | +1 | −1 |
| 100 | 5489–5495 | 5522–5528 | Types | +1 | −1 |
| 101 | 5533–5539 | 5566–5572 | Types | +1 | −1 |
| 102 | 5543–5549 | 5576–5582 | Types | +1 | −1 |
| 103 | 5609–5615 | 5642–5649 | Types | +2 | −1 |
| 104 | 5634–5640 | 5668–5674 | Types | +1 | −1 |
| 105 | 5705–5713 | 5739–5747 | Types | +2 | −2 |
| 106 | 5758–5763 | 5792–5798 | Types | +1 | −0 |
| 107 | 5776–5782 | 5811–5817 | Types | +1 | −1 |
| 108 | 5790–5796 | 5825–5831 | Types | +1 | −1 |
| 109 | 5807–5824 | 5842–5859 | Types | +4 | −4 |
| 110 | 5829–5835 | 5864–5870 | Types | +1 | −1 |
| 111 | 5870–5876 | 5905–5911 | Types | +1 | −1 |
| 112 | 5885–5893 | 5920–5929 | Types | +3 | −2 |
| 113 | 5924–5932 | 5960–5968 | Types | +2 | −2 |
| 114 | 5963–5971 | 5999–6007 | Types | +2 | −2 |
| 115 | 5976–5982 | 6012–6018 | Types | +1 | −1 |
| 116 | 6083–6089 | 6119–6125 | Types | +1 | −1 |
| 117 | 6267–6273 | 6303–6309 | Types | +1 | −1 |
| 118 | 6359–6365 | 6395–6401 | Types | +1 | −1 |
| 119 | 6378–6384 | 6414–6420 | Types | +1 | −1 |
| 120 | 6623–6629 | 6659–6665 | Types | +1 | −1 |
| 121 | 6649–6655 | 6685–6691 | Types | +1 | −1 |
| 122 | 6737–6743 | 6773–6779 | Types | +1 | −1 |
| 123 | 6761–6768 | 6797–6806 | Types | +2 | −0 |
| 124 | 6800–6812 | 6838–6853 | Types | +7 | −4 |
| 125 | 6841–6847 | 6882–6888 | Types | +1 | −1 |
| 126 | 6863–6873 | 6904–6914 | Types | +3 | −3 |
| 127 | 6900–6906 | 6941–6947 | Types | +1 | −1 |
| 128 | 6945–6950 | 6986–6992 | Types | +1 | −0 |
| 129 | 7003–7009 | 7045–7051 | Types | +1 | −1 |
| 130 | 7022–7028 | 7064–7070 | Types | +1 | −1 |
| 131 | 7048–7054 | 7090–7096 | Types | +1 | −1 |
| 132 | 7129–7135 | 7171–7177 | Types | +1 | −1 |
| 133 | 7137–7143 | 7179–7185 | Types | +1 | −1 |
| 134 | 7171–7177 | 7213–7219 | Types | +1 | −1 |
| 135 | 7184–7190 | 7226–7232 | Types | +1 | −1 |
| 136 | 7255–7260 | 7297–7303 | Types | +1 | −0 |
| 137 | 7300–7315 | 7343–7358 | Types | +3 | −3 |
| 138 | 7335–7341 | 7378–7384 | Types | +1 | −1 |
| 139 | 7392–7399 | 7435–7444 | Types | +2 | −0 |
| 140 | 7437–7443 | 7482–7488 | Types | +1 | −1 |
| 141 | 7556–7563 | 7601–7610 | Types | +2 | −0 |
| 142 | 7800–7814 | 7847–7861 | Types | +3 | −3 |
| 143 | 7817–7822 | 7864–7870 | Types | +1 | −0 |
| 144 | 7826–7832 | 7874–7880 | Types | +1 | −1 |
| 145 | 7842–7850 | 7890–7898 | Types | +2 | −2 |
| 146 | 7873–7878 | 7921–7927 | Types | +1 | −0 |
| 147 | 7912–7918 | 7961–7967 | Types | +1 | −1 |
| 148 | 7954–7960 | 8003–8009 | Types | +1 | −1 |
| 149 | 8004–8010 | 8053–8059 | Types | +1 | −1 |
| 150 | 8084–8090 | 8133–8139 | Types | +1 | −1 |
| 151 | 8101–8107 | 8150–8156 | Types | +1 | −1 |
| 152 | 8154–8166 | 8203–8218 | Types | +7 | −4 |
| 153 | 8169–8181 | 8221–8236 | Types | +8 | −5 |
| 154 | 8216–8223 | 8271–8280 | Types | +2 | −0 |
| 155 | 8229–8235 | 8286–8292 | Types | +1 | −1 |
| 156 | 8273–8279 | 8330–8336 | Types | +1 | −1 |
| 157 | 8385–8391 | 8442–8448 | Types | +1 | −1 |
| 158 | 8406–8412 | 8463–8469 | Types | +1 | −1 |
| 159 | 8712–8720 | 8769–8777 | Types | +2 | −2 |
| 160 | 8724–8730 | 8781–8787 | Types | +1 | −1 |
| 161 | 8768–8774 | 8825–8831 | Types | +1 | −1 |
| 162 | 8790–8796 | 8847–8853 | Types | +1 | −1 |
| 163 | 8843–8849 | 8900–8906 | Types | +1 | −1 |
| 164 | 8934–8940 | 8991–8997 | Types | +1 | −1 |
| 165 | 8956–8962 | 9013–9019 | Types | +1 | −1 |
| 166 | 8979–8985 | 9036–9042 | Types | +1 | −1 |
| 167 | 9022–9029 | 9079–9088 | Types | +2 | −0 |
| 168 | 9071–9079 | 9130–9138 | Types | +2 | −2 |
| 169 | 9097–9102 | 9156–9162 | Types | +1 | −0 |
| 170 | 9156–9162 | 9216–9222 | Types | +1 | −1 |
| 171 | 9188–9194 | 9248–9254 | Types | +1 | −1 |
| 172 | 9205–9211 | 9265–9271 | Types | +1 | −1 |
| 173 | 9237–9243 | 9297–9303 | Types | +1 | −1 |
| 174 | 9248–9255 | 9308–9317 | Types | +2 | −0 |
| 175 | 9305–9311 | 9367–9373 | Types | +1 | −1 |
| 176 | 9337–9343 | 9399–9405 | Types | +1 | −1 |
| 177 | 9367–9373 | 9429–9435 | Types | +1 | −1 |
| 178 | 9405–9410 | 9467–9473 | Types | +1 | −0 |
| 179 | 9448–9454 | 9511–9517 | Types | +1 | −1 |
| 180 | 9549–9555 | 9612–9618 | Types | +1 | −1 |
| 181 | 9562–9568 | 9625–9631 | Types | +1 | −1 |
| 182 | 9664–9672 | 9727–9736 | Types | +2 | −1 |
| 183 | 9692–9698 | 9756–9762 | Types | +1 | −1 |
| 184 | 9804–9810 | 9868–9874 | Types | +1 | −1 |
| 185 | 9822–9828 | 9886–9892 | Types | +1 | −1 |
| 186 | 9893–9899 | 9957–9963 | Types | +1 | −1 |
| 187 | 9934–9939 | 9998–10004 | Types | +1 | −0 |
| 188 | 9951–9957 | 10016–10022 | Types | +1 | −1 |
| 189 | 9974–9980 | 10039–10045 | Types | +1 | −1 |
| 190 | 10058–10064 | 10123–10129 | Types | +1 | −1 |
| 191 | 10088–10096 | 10153–10162 | Types | +3 | −2 |
| 192 | 10119–10124 | 10185–10191 | Types | +1 | −0 |
| 193 | 10144–10149 | 10211–10217 | Types | +1 | −0 |
| 194 | 10159–10165 | 10227–10233 | Types | +1 | −1 |
| 195 | 10289–10295 | 10357–10363 | Types | +1 | −1 |
| 196 | 10325–10331 | 10393–10399 | Types | +1 | −1 |
| 197 | 10343–10349 | 10411–10418 | Types | +2 | −1 |
| 198 | 10404–10410 | 10473–10479 | Types | +1 | −1 |
| 199 | 10442–10447 | 10511–10517 | Types | +1 | −0 |
| 200 | 10466–10478 | 10536–10548 | Types | +2 | −2 |
| 201 | 10606–10612 | 10676–10682 | Types | +1 | −1 |
| 202 | 10625–10631 | 10695–10701 | Types | +1 | −1 |
| 203 | 10678–10684 | 10748–10754 | Types | +1 | −1 |
| 204 | 10754–10764 | 10824–10834 | Types | +3 | −3 |
| 205 | 10772–10778 | 10842–10848 | Types | +1 | −1 |
| 206 | 11003–11009 | 11073–11079 | Types | +1 | −1 |
| 207 | 11040–11046 | 11110–11116 | Types | +1 | −1 |
| 208 | 11099–11105 | 11169–11175 | Types | +1 | −1 |
| 209 | 11153–11159 | 11223–11229 | Types | +1 | −1 |
| 210 | 11173–11179 | 11243–11249 | Types | +1 | −1 |
| 211 | 11204–11210 | 11274–11280 | Types | +1 | −1 |
| 212 | 11223–11229 | 11293–11299 | Types | +1 | −1 |
| 213 | 11238–11244 | 11308–11314 | Types | +1 | −1 |
| 214 | 11277–11284 | 11347–11356 | Types | +2 | −0 |
| 215 | 11301–11307 | 11373–11379 | Types | +1 | −1 |
| 216 | 11340–11346 | 11412–11418 | Types | +1 | −1 |
| 217 | 11387–11401 | 11459–11474 | Types | +3 | −2 |
| 218 | 11436–11442 | 11509–11515 | Types | +1 | −1 |
| 219 | 11516–11522 | 11589–11595 | Types | +1 | −1 |
| 220 | 11575–11581 | 11648–11654 | Types | +1 | −1 |
| 221 | 11653–11659 | 11726–11732 | Types | +1 | −1 |
| 222 | 11709–11715 | 11782–11788 | Types | +1 | −1 |
| 223 | 11727–11732 | 11800–11806 | Types | +1 | −0 |
| 224 | 11740–11748 | 11814–11822 | Types | +2 | −2 |
| 225 | 11813–11819 | 11887–11893 | Types | +1 | −1 |
| 226 | 11832–11838 | 11906–11912 | Types | +1 | −1 |
| 227 | 11917–11923 | 11991–11997 | Types | +1 | −1 |
| 228 | 11989–11995 | 12063–12069 | Types | +1 | −1 |
| 229 | 12004–12010 | 12078–12084 | Types | +1 | −1 |
| 230 | 12046–12052 | 12120–12126 | Types | +1 | −1 |
| 231 | 12119–12125 | 12193–12199 | Types | +1 | −1 |
| 232 | 12204–12210 | 12278–12284 | Types | +1 | −1 |
| 233 | 12313–12329 | 12387–12404 | Types | +3 | −2 |
| 234 | 12357–12362 | 12432–12438 | Types | +1 | −0 |
| 235 | 12418–12424 | 12494–12500 | Types | +1 | −1 |
| 236 | 12431–12436 | 12507–12513 | Types | +1 | −0 |
| 237 | 12445–12450 | 12522–12528 | Types | +1 | −0 |
| 238 | 12515–12521 | 12593–12599 | Types | +1 | −1 |
| 239 | 12526–12533 | 12604–12613 | Types | +2 | −0 |
| 240 | 12540–12545 | 12620–12626 | Types | +1 | −0 |
| 241 | 12611–12617 | 12692–12698 | Types | +1 | −1 |
| 242 | 12625–12631 | 12706–12712 | Types | +1 | −1 |
| 243 | 12752–12758 | 12833–12839 | Types | +1 | −1 |
| 244 | 12799–12805 | 12880–12886 | Types | +1 | −1 |
| 245 | 12820–12826 | 12901–12907 | Types | +1 | −1 |
| 246 | 12846–12852 | 12927–12933 | Types | +1 | −1 |
| 247 | 12860–12866 | 12941–12947 | Types | +1 | −1 |
| 248 | 12883–12903 | 12964–12984 | Types | +4 | −4 |
| 249 | 12918–12924 | 12999–13005 | Types | +1 | −1 |
| 250 | 12996–13002 | 13077–13083 | Types | +1 | −1 |
| 251 | 13011–13017 | 13092–13098 | Types | +1 | −1 |
| 252 | 13022–13034 | 13103–13116 | Types | +2 | −1 |
| 253 | 13037–13045 | 13119–13127 | Types | +2 | −2 |
| 254 | 13080–13086 | 13162–13168 | Types | +1 | −1 |
| 255 | 13132–13138 | 13214–13220 | Types | +1 | −1 |
| 256 | 13159–13164 | 13241–13247 | Types | +1 | −0 |
| 257 | 13175–13181 | 13258–13264 | Types | +1 | −1 |
| 258 | 13190–13196 | 13273–13279 | Types | +1 | −1 |
| 259 | 13212–13218 | 13295–13301 | Types | +1 | −1 |
| 260 | 13238–13244 | 13321–13327 | Types | +1 | −1 |
| 261 | 13257–13263 | 13340–13346 | Types | +1 | −1 |
| 262 | 13276–13282 | 13359–13365 | Types | +1 | −1 |
| 263 | 13291–13297 | 13374–13380 | Types | +1 | −1 |
| 264 | 13370–13376 | 13453–13460 | Types | +2 | −1 |
| 265 | 13409–13415 | 13493–13499 | Types | +1 | −1 |
| 266 | 13470–13484 | 13554–13569 | Types | +3 | −2 |
| 267 | 13491–13497 | 13576–13582 | Types | +1 | −1 |
| 268 | 13509–13515 | 13594–13600 | Types | +1 | −1 |
| 269 | 13561–13566 | 13646–13652 | Types | +1 | −0 |
| 270 | 13581–13587 | 13667–13673 | Types | +1 | −1 |
| 271 | 13660–13665 | 13746–13752 | Types | +1 | −0 |
| 272 | 13676–13681 | 13763–13769 | Types | +1 | −0 |
| 273 | 13689–13695 | 13777–13783 | Types | +1 | −1 |
| 274 | 13704–13713 | 13792–13803 | Types | +2 | −0 |
| 275 | 13724–13731 | 13814–13823 | Types | +2 | −0 |
| 276 | 13771–13776 | 13863–13869 | Types | +1 | −0 |
| 277 | 13805–13811 | 13898–13904 | Types | +1 | −1 |
| 278 | 13816–13822 | 13909–13915 | Types | +1 | −1 |
| 279 | 13838–13844 | 13931–13937 | Types | +1 | −1 |
| 280 | 13851–13858 | 13944–13952 | Types | +2 | −1 |
| 281 | 13907–13912 | 14001–14007 | Types | +1 | −0 |
| 282 | 13949–13957 | 14044–14052 | Types | +2 | −2 |
| 283 | 13982–13988 | 14077–14083 | Types | +1 | −1 |
| 284 | 14003–14010 | 14098–14107 | Types | +2 | −0 |
| 285 | 14143–14148 | 14240–14246 | Types | +1 | −0 |
| 286 | 14154–14160 | 14252–14258 | Types | +1 | −1 |
| 287 | 14188–14194 | 14286–14292 | Types | +1 | −1 |
| 288 | 14201–14207 | 14299–14305 | Types | +1 | −1 |
| 289 | 14216–14221 | 14314–14320 | Types | +1 | −0 |
| 290 | 14229–14234 | 14328–14334 | Types | +1 | −0 |
| 291 | 14249–14255 | 14349–14355 | Types | +1 | −1 |
| 292 | 14269–14275 | 14369–14375 | Types | +1 | −1 |
| 293 | 14301–14315 | 14401–14415 | Client | +3 | −3 |
| 294 | 14317–14327 | 14417–14427 | Client | +2 | −2 |
| 295 | 14341–14347 | 14441–14447 | Client | +1 | −1 |
| 296 | 14349–14355 | 14449–14455 | Client | +1 | −1 |
| 297 | 14369–14375 | 14469–14475 | Client | +1 | −1 |
| 298 | 14381–14387 | 14481–14487 | Client | +1 | −1 |
| 299 | 14393–14399 | 14493–14499 | Client | +1 | −1 |
| 300 | 14417–14427 | 14517–14527 | Client | +2 | −2 |
| 301 | 14441–14447 | 14541–14547 | Client | +1 | −1 |
| 302 | 14457–14463 | 14557–14563 | Client | +1 | −1 |
| 303 | 14493–14503 | 14593–14603 | Client | +2 | −2 |
| 304 | 14509–14519 | 14609–14619 | Client | +2 | −2 |
| 305 | 14549–14555 | 14649–14655 | Client | +1 | −1 |
| 306 | 14557–14563 | 14657–14663 | Client | +1 | −1 |
| 307 | 14565–14571 | 14665–14671 | Client | +1 | −1 |
| 308 | 14573–14587 | 14673–14687 | Client | +3 | −3 |
| 309 | 14601–14611 | 14701–14711 | Client | +2 | −2 |
| 310 | 14613–14619 | 14713–14719 | Client | +1 | −1 |
| 311 | 14621–14627 | 14721–14727 | Client | +1 | −1 |
| 312 | 14629–14643 | 14729–14743 | Client | +3 | −3 |
| 313 | 14657–14663 | 14757–14763 | Client | +1 | −1 |
| 314 | 14677–14683 | 14777–14783 | Client | +1 | −1 |
| 315 | 14689–14703 | 14789–14803 | Client | +3 | −3 |
| 316 | 14705–14715 | 14805–14815 | Client | +2 | −2 |
| 317 | 14725–14731 | 14825–14831 | Client | +1 | −1 |
| 318 | 14739–14745 | 14839–14845 | Client | +1 | −1 |
| 319 | 14755–14761 | 14855–14861 | Client | +1 | −1 |
| 320 | 14763–14769 | 14863–14869 | Client | +1 | −1 |
| 321 | 14771–14781 | 14871–14881 | Client | +2 | −2 |
| 322 | 14799–14805 | 14899–14905 | Client | +1 | −1 |
| 323 | 14811–14833 | 14911–14933 | Client | +5 | −5 |
| 324 | 14847–14857 | 14947–14957 | Client | +2 | −2 |
| 325 | 14875–14881 | 14975–14981 | Client | +1 | −1 |
| 326 | 14883–14913 | 14983–15013 | Client | +7 | −7 |
| 327 | 14915–14921 | 15015–15021 | Client | +1 | −1 |
| 328 | 14935–14957 | 15035–15057 | Client | +5 | −5 |
| 329 | 14979–14993 | 15079–15093 | Client | +3 | −3 |
| 330 | 14999–15005 | 15099–15105 | Client | +1 | −1 |
| 331 | 15007–15025 | 15107–15125 | Client | +4 | −4 |
| 332 | 15027–15033 | 15127–15133 | Client | +1 | −1 |
| 333 | 15051–15057 | 15151–15157 | Client | +1 | −1 |
| 334 | 15059–15065 | 15159–15165 | Client | +1 | −1 |
| 335 | 15075–15081 | 15175–15181 | Client | +1 | −1 |
| 336 | 15103–15137 | 15203–15237 | Client | +8 | −8 |
| 337 | 15195–15201 | 15295–15301 | Client | +1 | −1 |
| 338 | 15203–15213 | 15303–15313 | Client | +2 | −2 |
| 339 | 15215–15221 | 15315–15321 | Client | +1 | −1 |
| 340 | 15227–15233 | 15327–15333 | Client | +1 | −1 |
| 341 | 15243–15249 | 15343–15349 | Client | +1 | −1 |
| 342 | 15263–15269 | 15363–15369 | Client | +1 | −1 |
| 343 | 15275–15281 | 15375–15381 | Client | +1 | −1 |
| 344 | 15283–15289 | 15383–15389 | Client | +1 | −1 |
| 345 | 15303–15309 | 15403–15409 | Client | +1 | −1 |
| 346 | 15311–15321 | 15411–15421 | Client | +2 | −2 |
| 347 | 15343–15349 | 15443–15449 | Client | +1 | −1 |
| 348 | 15351–15361 | 15451–15461 | Client | +2 | −2 |
| 349 | 15383–15389 | 15483–15489 | Client | +1 | −1 |
| 350 | 15395–15413 | 15495–15513 | Client | +4 | −4 |
| 351 | 15415–15421 | 15515–15521 | Client | +1 | −1 |
| 352 | 15427–15433 | 15527–15533 | Client | +1 | −1 |
| 353 | 15439–15457 | 15539–15557 | Client | +4 | −4 |
| 354 | 15463–15473 | 15563–15573 | Client | +2 | −2 |
| 355 | 15475–15485 | 15575–15585 | Client | +2 | −2 |
| 356 | 15511–15529 | 15611–15629 | Client | +4 | −4 |
| 357 | 15531–15545 | 15631–15645 | Client | +3 | −3 |
| 358 | 15547–15565 | 15647–15665 | Client | +4 | −4 |
| 359 | 15571–15577 | 15671–15677 | Client | +1 | −1 |
| 360 | 15627–15633 | 15727–15733 | Client | +1 | −1 |
| 361 | 15643–15649 | 15743–15749 | Client | +1 | −1 |
| 362 | 15655–15661 | 15755–15761 | Client | +1 | −1 |
| 363 | 15667–15681 | 15767–15781 | Client | +3 | −3 |
| 364 | 15687–15697 | 15787–15797 | Client | +2 | −2 |
| 365 | 15711–15725 | 15811–15825 | Client | +3 | −3 |
| 366 | 15735–15741 | 15835–15841 | Client | +1 | −1 |
| 367 | 15755–15765 | 15855–15865 | Client | +2 | −2 |
| 368 | 15797–15803 | 15897–15903 | Client | +1 | −1 |
| 369 | 15809–15819 | 15909–15919 | Client | +2 | −2 |
| 370 | 15821–15831 | 15921–15931 | Client | +2 | −2 |
| 371 | 15845–15859 | 15945–15959 | Client | +3 | −3 |
| 372 | 15881–15895 | 15981–15995 | Client | +3 | −3 |
| 373 | 15917–15923 | 16017–16023 | Client | +1 | −1 |
| 374 | 15929–15935 | 16029–16035 | Client | +1 | −1 |
| 375 | 15953–15959 | 16053–16059 | Client | +1 | −1 |
| 376 | 15965–15975 | 16065–16075 | Client | +2 | −2 |
| 377 | 15981–15987 | 16081–16087 | Client | +1 | −1 |
| 378 | 15997–16003 | 16097–16103 | Client | +1 | −1 |
| 379 | 16013–16019 | 16113–16119 | Client | +1 | −1 |
| 380 | 16033–16039 | 16133–16139 | Client | +1 | −1 |
| 381 | 16049–16055 | 16149–16155 | Client | +1 | −1 |
| 382 | 16061–16067 | 16161–16167 | Client | +1 | −1 |
| 383 | 16101–16107 | 16201–16207 | Client | +1 | −1 |
| 384 | 16113–16135 | 16213–16235 | Client | +5 | −5 |
| 385 | 16141–16147 | 16241–16247 | Client | +1 | −1 |
| 386 | 16161–16167 | 16261–16267 | Client | +1 | −1 |
| 387 | 16169–16187 | 16269–16287 | Client | +4 | −4 |
| 388 | 16189–16291 | 16289–16391 | Client | +25 | −25 |
| 389 | 16293–16299 | 16393–16399 | Client | +1 | −1 |
| 390 | 16301–16307 | 16401–16407 | Client | +1 | −1 |
| 391 | 16341–16347 | 16441–16447 | Client | +1 | −1 |
| 392 | 16353–16359 | 16453–16459 | Client | +1 | −1 |
| 393 | 16361–16367 | 16461–16467 | Client | +1 | −1 |
| 394 | 16369–16375 | 16469–16475 | Client | +1 | −1 |
| 395 | 16381–16403 | 16481–16503 | Client | +5 | −5 |
| 396 | 16405–16427 | 16505–16527 | Client | +5 | −5 |
| 397 | 16437–16447 | 16537–16547 | Client | +2 | −2 |
| 398 | 16449–16455 | 16549–16555 | Client | +1 | −1 |
| 399 | 16457–16463 | 16557–16563 | Client | +1 | −1 |
| 400 | 16465–16471 | 16565–16571 | Client | +1 | −1 |
| 401 | 16477–16483 | 16577–16583 | Client | +1 | −1 |
| 402 | 16493–16499 | 16593–16599 | Client | +1 | −1 |
| 403 | 16501–16507 | 16601–16607 | Client | +1 | −1 |
| 404 | 16541–16563 | 16641–16663 | Client | +5 | −5 |
| 405 | 16565–16599 | 16665–16699 | Client | +8 | −8 |
| 406 | 16621–16627 | 16721–16727 | Client | +1 | −1 |
| 407 | 16637–16643 | 16737–16743 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- jira/old/ballerinax_jira.bal.txt	2026-08-12 12:57:30
+++ jira/new/ballerinax_jira.bal.txt	2026-08-12 13:19:19
@@ -316,6 +316,7 @@
 
 type ProjectRoleUser record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. Returns *unknown* if the record is deleted and corrupted, for example, as the result of a server import
+    @constraint:String {maxLength: 128}
     string accountId?;
 };
 
@@ -327,6 +328,7 @@
 
 type UserDetails record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string accountId?;
     # The email address of the user. Depending on the user’s privacy settings, this may be returned as null
     string emailAddress?;
@@ -370,7 +372,7 @@
 
 type GetContextsForFieldQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The list of context IDs. To include multiple contexts, separate IDs with ampersand: `contextId=10000&contextId=10001`
     int[] contextId?;
     # Whether to return contexts that apply to all issue types
@@ -385,6 +387,7 @@
 
 type UserKey record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. Returns *unknown* if the record is deleted and corrupted, for example, as the result of a server import
+    @constraint:String {maxLength: 128}
     string accountId?;
     # This property is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string 'key?;
@@ -456,12 +459,13 @@
 };
 
 # The workflow transition rule conditions tree
-type WorkflowCondition ballerinax/jira:2.0.2:WorkflowSimpleCondition|ballerinax/jira:2.0.2:WorkflowCompoundCondition;
+type WorkflowCondition WorkflowSimpleCondition|WorkflowCompoundCondition;
 
 # Represents the Queries record for the operation: getWorkflowSchemeProjectAssociations
 
 type GetWorkflowSchemeProjectAssociationsQueries record {
     # The ID of a project to return the workflow schemes for. To include multiple projects, provide an ampersand-Jim: oneseparated list. For example, `projectId=10000&projectId=10001`
+    @constraint:Array {maxLength: 100, minLength: 1}
     int[] projectId;
 };
 
@@ -588,6 +592,7 @@
 
 type CustomFieldConfigurations record {
     # The list of custom field configuration details
+    @constraint:Array {maxLength: 1000, minLength: 1}
     ContextualConfiguration[] configurations;
 };
 
@@ -675,7 +680,7 @@
     record {|anydata...;|} value?;
 };
 
-type CustomContextVariable ballerinax/jira:2.0.2:UserContextVariable|ballerinax/jira:2.0.2:IssueContextVariable|ballerinax/jira:2.0.2:JsonContextVariable;
+type CustomContextVariable UserContextVariable|IssueContextVariable|JsonContextVariable;
 
 # The JQL specifying the issues available in the evaluated Jira expression under the `issues` context variable. This bean will be replacing `JexpIssues` bean as part of new `evaluate` endpoint
 
@@ -688,7 +693,7 @@
 
 type JexpEvaluateCtxJqlIssues record {
     # The maximum number of issues to return from the JQL query. max results value considered may be lower than the number specific here
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The token for a page to fetch that is not the first page. The first page has a `nextPageToken` of `null`. Use the `nextPageToken` to fetch the next page of issues
     string nextPageToken?;
     # The JQL query, required to be bounded. Additionally, `orderBy` clause can contain a maximum of 7 fields
@@ -735,6 +740,7 @@
 
 type GetUserPropertyQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string accountId?;
     # This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string userKey?;
@@ -748,7 +754,7 @@
     # The cursor for pagination
     string nextPageToken?;
     # The maximum number of results to return. Must be an integer between 1 and 200
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
 };
 
 
@@ -778,8 +784,9 @@
 
 type SimpleListWrapperGroupName record {
     ListWrapperCallbackGroupName pagingCallback?;
-    ballerina/lang.int:0.0.0:Signed32 size?;
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 size?;
+    @jsondata:Name {value: "max-results"}
+    int:Signed32 maxResults?;
     ListWrapperCallbackGroupName callback?;
     GroupName[] items?;
 };
@@ -829,7 +836,7 @@
     boolean valueNode?;
     boolean long?;
     int longValue?;
-    ballerina/lang.int:0.0.0:Signed32 valueAsInt?;
+    int:Signed32 valueAsInt?;
     boolean missingNode?;
     boolean number?;
     string valueAsText?;
@@ -841,7 +848,7 @@
     boolean integralNumber?;
     string textValue?;
     boolean double?;
-    ballerina/lang.int:0.0.0:Signed32 intValue?;
+    int:Signed32 intValue?;
     boolean bigInteger?;
     decimal doubleValue?;
     boolean floatingPointNumber?;
@@ -865,7 +872,7 @@
     # The collection of FieldCreateMetaBeans.
     FieldCreateMetadata[] fields?;
     # The maximum number of items to return per page.
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     FieldCreateMetadata[] results?;
     # The index of the first item returned.
     int startAt?;
@@ -919,7 +926,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -948,8 +955,9 @@
 
 type SimpleListWrapperApplicationRole record {
     ListWrapperCallbackApplicationRole pagingCallback?;
-    ballerina/lang.int:0.0.0:Signed32 size?;
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 size?;
+    @jsondata:Name {value: "max-results"}
+    int:Signed32 maxResults?;
     ListWrapperCallbackApplicationRole callback?;
     ApplicationRole[] items?;
 };
@@ -969,17 +977,17 @@
     # The groups associated with the application role. As a group's name can change, use of `groupDetails` is recommended to identify a groups
     string[] groups?;
     # The count of users remaining on your license
-    ballerina/lang.int:0.0.0:Signed32 remainingSeats?;
+    int:Signed32 remainingSeats?;
     # Indicates if the application role belongs to Jira platform (`jira-core`)
     boolean platform?;
     # Determines whether this application role should be selected by default on user creation
     boolean selectedByDefault?;
     # The maximum count of users on your license
-    ballerina/lang.int:0.0.0:Signed32 numberOfSeats?;
+    int:Signed32 numberOfSeats?;
     # The groups that are granted default access for this application role
     GroupName[] defaultGroupsDetails?;
     # The number of users counting against your license
-    ballerina/lang.int:0.0.0:Signed32 userCount?;
+    int:Signed32 userCount?;
     # The [type of users](https://confluence.atlassian.com/x/lRW3Ng) being counted against your license
     string userCountDescription?;
     # The display name of the application role
@@ -1191,7 +1199,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -1240,6 +1248,7 @@
     # The permissions for the plan
     CreatePermissionRequest[] permissions?;
     # The plan name
+    @constraint:String {maxLength: 255, minLength: 1}
     string name;
     # The scheduling settings for the plan
     CreateSchedulingRequest scheduling;
@@ -1310,7 +1319,7 @@
     # The IDs of the releases to exclude from the plan
     int[] releaseIds?;
     # Issues completed this number of days ago will be excluded from the plan
-    ballerina/lang.int:0.0.0:Signed32 numberOfDaysToShowCompletedIssues?;
+    int:Signed32 numberOfDaysToShowCompletedIssues?;
     # The IDs of the issue types to exclude from the plan
     int[] issueTypeIds?;
     # The IDs of the work status categories to exclude from the plan
@@ -1337,7 +1346,8 @@
     decimal capacity?;
 };
 
-// Unknown type: BulkGetUsersQueriesAccountIdItemsString
+@constraint:String {maxLength: 128}
+type BulkGetUsersQueriesAccountIdItemsString string;
 
 # A page of items
 
@@ -1347,7 +1357,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -1600,7 +1610,7 @@
 };
 
 # An operand that can be part of a list operand
-type JqlQueryUnitaryOperand ballerinax/jira:2.0.2:ValueOperand|ballerinax/jira:2.0.2:FunctionOperand|ballerinax/jira:2.0.2:KeywordOperand;
+type JqlQueryUnitaryOperand ValueOperand|FunctionOperand|KeywordOperand;
 
 # The field configuration for an issue type
 
@@ -1622,14 +1632,14 @@
     # The ID of the level above this one in the hierarchy. This property is deprecated, see [Change notice: Removing hierarchy level IDs from next-gen APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-gen-apis/)
     int aboveLevelId?;
     # The level of this item in the hierarchy
-    ballerina/lang.int:0.0.0:Signed32 level?;
+    int:Signed32 level?;
     # The issue types available in this hierarchy level
     int[] issueTypeIds?;
     # The name of this hierarchy level
     string name?;
     # The ID of the hierarchy level. This property is deprecated, see [Change notice: Removing hierarchy level IDs from next-gen APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-gen-apis/)
     int id?;
-    ballerina/lang.int:0.0.0:Signed32 hierarchyLevelNumber?;
+    int:Signed32 hierarchyLevelNumber?;
     # The ID of the level below this one in the hierarchy. This property is deprecated, see [Change notice: Removing hierarchy level IDs from next-gen APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-gen-apis/)
     int belowLevelId?;
 };
@@ -1815,7 +1825,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -1858,7 +1868,7 @@
     # The transition name
     string name;
     # The transition ID
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
 };
 
 # Represents the Queries record for the operation: createDashboard
@@ -1872,6 +1882,7 @@
 
 type MigrationResourceWorkflowRuleSearchPostHeaders record {
     # The app migration transfer ID
+    @http:Header {name: "Atlassian-Transfer-Id"}
     string atlassianTransferId;
 };
 
@@ -1928,13 +1939,13 @@
 
 type PageOfChangelogs record {
     # The number of results on the page
-    ballerina/lang.int:0.0.0:Signed32 total?;
+    int:Signed32 total?;
     # The maximum number of results that could be on the page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The list of changelogs
     Changelog[] histories?;
     # The index of the first item returned on the page
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
 };
 
 # A log of changes made to issue fields. Changelogs related to workflow associations are currently being deprecated
@@ -2026,9 +2037,9 @@
 
 type GetChangeLogsQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
 };
 
 
@@ -2042,6 +2053,7 @@
 # The level of validation to return from the API. If no values are provided, the default would return `WARNING` and `ERROR` level validation results
 
 type ValidationOptionsForCreate record {
+    @constraint:Array {maxLength: 2}
     ("WARNING"|"ERROR")[] levels?;
 };
 
@@ -2204,9 +2216,9 @@
 
 type WorkflowTransitionLinks record {
     # The port that the transition starts from
-    ballerina/lang.int:0.0.0:Signed32? fromPort?;
+    int:Signed32? fromPort?;
     # The port that the transition goes to
-    ballerina/lang.int:0.0.0:Signed32? toPort?;
+    int:Signed32? toPort?;
     # The status that the transition starts from
     string? fromStatusReference?;
 };
@@ -2275,7 +2287,7 @@
     # Use [expand](#expansion) to include additional information about screens in the response. This parameter accepts `tab` which returns details about the screen tabs the field is used in
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
 };
@@ -2298,6 +2310,7 @@
 
 type StatusCreate record {
     # The name of the status
+    @constraint:String {maxLength: 255}
     string name;
     # The description of the status
     string description?;
@@ -2322,7 +2335,7 @@
     # This property is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string lastModifiedUser?;
     # The number of steps included in the workflow
-    ballerina/lang.int:0.0.0:Signed32 steps?;
+    int:Signed32 steps?;
 };
 
 # Bulk Edit Get Fields Response
@@ -2385,7 +2398,7 @@
     # Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts`properties`, which returns worklog properties
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The worklog start date and time, as a UNIX timestamp in milliseconds, after which worklogs are returned
     int startedAfter?;
     # The index of the first item to return in a page of results (page offset)
@@ -2402,7 +2415,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -2468,12 +2481,15 @@
 
 type BulkChangelogRequestBean record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @constraint:Int {minValue: 1, maxValue: 10000}
+    int:Signed32 maxResults?;
     # The cursor for pagination
     string nextPageToken?;
     # List of issue IDs/keys to fetch changelogs for
+    @constraint:Array {maxLength: 1000, minLength: 1}
     string[] issueIdsOrKeys;
     # List of field IDs to filter changelogs
+    @constraint:Array {maxLength: 10}
     string[] fieldIds?;
 };
 
@@ -2496,7 +2512,8 @@
     # Use [expand](#expansion) to include additional information in the response. This parameter accepts `transition`, which, for each rule, returns information about the transition the rule is assigned to
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @constraint:Int {maxValue: 50}
+    int:Signed32 maxResults?;
     # The transition rule class keys, as defined in the Connect or the Forge app descriptor, of the transition rules to return
     string[] keys?;
     # Whether draft or published workflows are returned. If not provided, both workflow types are returned
@@ -2505,14 +2522,17 @@
     int startAt?;
 };
 
-// Unknown type: GetWorkflowTransitionRuleConfigurationsQueriesWorkflowNamesItemsString
+@constraint:String {maxLength: 50}
+type GetWorkflowTransitionRuleConfigurationsQueriesWorkflowNamesItemsString string;
 
-// Unknown type: GetWorkflowTransitionRuleConfigurationsQueriesWithTagsItemsString
+@constraint:String {maxLength: 20}
+type GetWorkflowTransitionRuleConfigurationsQueriesWithTagsItemsString string;
 
 # Represents the Queries record for the operation: ServiceRegistryResource.services_get
 
 type ServiceRegistryResourceServicesGetQueries record {
     # The ID of the services (the strings starting with "b:" need to be decoded in Base64)
+    @constraint:Array {maxLength: 20, minLength: 1}
     string[] serviceIds;
 };
 
@@ -2542,7 +2562,7 @@
     # A [JQL](https://confluence.atlassian.com/x/egORLQ) expression
     string jql?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # Determines how to validate the JQL query and treat the validation results. Supported values:
 
 *  `strict` Returns a 400 response code if any errors are found, along with a list of all errors (and warnings).
@@ -2578,7 +2598,7 @@
     # A list of up to 5 issue properties to include in the results. This parameter accepts a comma-separated list
     string[] properties?;
     # The index of the first item to return in the page of results (page offset). The base index is `0`
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
 };
 
 # Represents the Queries record for the operation: updateDraftWorkflowMapping
@@ -2609,11 +2629,11 @@
 
 type StoreAvatarQueries record {
     # The length of each side of the crop region
-    ballerina/lang.int:0.0.0:Signed32 size?;
+    int:Signed32 size?;
     # The X coordinate of the top-left corner of the crop region
-    ballerina/lang.int:0.0.0:Signed32 x?;
+    int:Signed32 x?;
     # The Y coordinate of the top-left corner of the crop region
-    ballerina/lang.int:0.0.0:Signed32 y?;
+    int:Signed32 y?;
 };
 
 # List of changed worklogs
@@ -2674,7 +2694,7 @@
     # The description of the workflow scheme
     string description?;
     # The issue types available in Jira
-    record {|ballerinax/jira:2.0.2:IssueTypeDetails...;|} issueTypes?;
+    record {|IssueTypeDetails...;|} issueTypes?;
     # For draft workflow schemes, this property is the issue type to workflow mappings for the original workflow scheme, where each mapping is an issue type ID and workflow name pair. Note that an issue type can only be mapped to one workflow in a workflow scheme
     record {|string...;|} originalIssueTypeMappings?;
     # The name of the default workflow for the workflow scheme. The default workflow has *All Unassigned Issue Types* assigned to it in Jira. If `defaultWorkflow` is not specified when creating a workflow scheme, it is set to *Jira Workflow (jira)*
@@ -2708,7 +2728,7 @@
     # The ID of the issue type's avatar
     int avatarId?;
     # Hierarchy level of the issue type
-    ballerina/lang.int:0.0.0:Signed32 hierarchyLevel?;
+    int:Signed32 hierarchyLevel?;
     # Details of the next-gen projects the issue type is available in
     Scope scope?;
     # The name of the issue type
@@ -2753,6 +2773,7 @@
     # The locale of the user. Depending on the user’s privacy setting, this may be returned as null
     string locale?;
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. Required in requests
+    @constraint:String {maxLength: 128}
     string accountId?;
     # The email address of the user. Depending on the user’s privacy setting, this may be returned as null
     string emailAddress?;
@@ -2796,7 +2817,7 @@
     # The default timezone of the Jira server. In a format known as Olson Time Zones, IANA Time Zones or TZ Database Time Zones
     string serverTimeZone?;
     # The build number of the Jira version
-    ballerina/lang.int:0.0.0:Signed32 buildNumber?;
+    int:Signed32 buildNumber?;
     # The version of Jira
     string version?;
     # The display URL of the Jira instance
@@ -2814,7 +2835,7 @@
     # The name of the Jira instance
     string serverTitle?;
     # The major, minor, and revision version numbers of the Jira version
-    ballerina/lang.int:0.0.0:Signed32[] versionNumbers?;
+    int:Signed32[] versionNumbers?;
     # The display URL of Confluence
     string displayUrlConfluence?;
 };
@@ -2875,7 +2896,7 @@
     # The cursor for pagination
     string nextPageToken?;
     # The maximum number of results to return. Must be an integer between 1 and 200
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
 };
 
 # A page containing dashboard details
@@ -2884,15 +2905,15 @@
     # The URL of the next page of results, if any
     string next?;
     # The number of results on the page
-    ballerina/lang.int:0.0.0:Signed32 total?;
+    int:Signed32 total?;
     # The maximum number of results that could be on the page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The URL of the previous page of results, if any
     string prev?;
     # List of dashboards
     Dashboard[] dashboards?;
     # The index of the first item returned on the page
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
 };
 
 # Details of a dashboard
@@ -2901,7 +2922,7 @@
     # The owner of the dashboard
     UserBean owner?;
     # The automatic refresh interval for the dashboard in milliseconds
-    ballerina/lang.int:0.0.0:Signed32 automaticRefreshMs?;
+    int:Signed32 automaticRefreshMs?;
     string description?;
     # Whether the current user has permission to edit the dashboard
     boolean isWritable?;
@@ -2914,7 +2935,7 @@
     # The name of the dashboard
     string name?;
     # The rank of this dashboard
-    ballerina/lang.int:0.0.0:Signed32 rank?;
+    int:Signed32 rank?;
     # The URL of these dashboard details
     string self?;
     # Whether the current dashboard is system dashboard
@@ -2930,6 +2951,7 @@
 
 type UserBean record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string accountId?;
     # The avatars of the user
     UserBeanAvatarUrls avatarUrls?;
@@ -3071,6 +3093,7 @@
     # The key of the project the component is assigned to. Required when creating a component. Can't be updated
     string project?;
     # The accountId of the component's lead user. The accountId uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string leadAccountId?;
     # The user details for the component's lead user
     User lead?;
@@ -3219,7 +3242,7 @@
 # Details about the operations available in this version
 
 type SimpleLink record {
-    ballerina/lang.int:0.0.0:Signed32 weight?;
+    int:Signed32 weight?;
     string href?;
     string id?;
     string label?;
@@ -3261,8 +3284,10 @@
 # Details of a gadget position
 
 type DashboardGadgetPosition record {
-    ballerina/lang.int:0.0.0:Signed32 theColumnPositionOfTheGadget;
-    ballerina/lang.int:0.0.0:Signed32 theRowPositionOfTheGadget;
+    @jsondata:Name {value: "The column position of the gadget."}
+    int:Signed32 theColumnPositionOfTheGadget;
+    @jsondata:Name {value: "The row position of the gadget."}
+    int:Signed32 theRowPositionOfTheGadget;
 };
 
 # A page of issue types
@@ -3279,7 +3304,7 @@
 type GetTrashedFieldsPaginatedQueries record {
     "name"|"-name"|"+name"|"trashDate"|"-trashDate"|"+trashDate"|"plannedDeletionDate"|"-plannedDeletionDate"|"+plannedDeletionDate"|"projectsCount"|"-projectsCount"|"+projectsCount" expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # String used to perform a case-insensitive partial match with field names or descriptions
     string query?;
     # [Order](#ordering) the results by a field:
@@ -3422,7 +3447,7 @@
     # The ID of an issue type that returned users and groups must have permission to view. To include multiple issue types, provide an ampersand-separated list. For example, `issueTypeId=10000&issueTypeId=10001`. Special values, such as `-1` (all standard issue types) and `-2` (all subtask issue types), are supported. This parameter is only used when `fieldId` is present
     string[] issueTypeId?;
     # The maximum number of items to return in each list
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The search string
     string query;
     # Whether the search for groups should be case insensitive
@@ -3445,7 +3470,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -3491,7 +3516,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -3580,7 +3605,7 @@
     WarningCollection warningCollection?;
     # Error messages from an operation
     ErrorCollection errorCollection?;
-    ballerina/lang.int:0.0.0:Signed32 status?;
+    int:Signed32 status?;
 };
 
 
@@ -3595,15 +3620,15 @@
     string[] errorMessages?;
     # The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
     record {|string...;|} errors?;
-    ballerina/lang.int:0.0.0:Signed32 status?;
+    int:Signed32 status?;
 };
 
 
 type BulkOperationErrorResult record {
     # Error messages from an operation
     ErrorCollection elementErrors?;
-    ballerina/lang.int:0.0.0:Signed32 failedElementNumber?;
-    ballerina/lang.int:0.0.0:Signed32 status?;
+    int:Signed32 failedElementNumber?;
+    int:Signed32 status?;
 };
 
 # Represents the Queries record for the operation: getValidProjectKey
@@ -3643,7 +3668,7 @@
     # The statuses that the transition can be made from
     FromLayoutPayload[] 'from?;
     # The id of the transition
-    ballerina/lang.int:0.0.0:Signed32 id?;
+    int:Signed32 id?;
     # The payload for the layout details for the destination end of a transition
     ToLayoutPayload to?;
     # The payload for creating a condition group in a workflow
@@ -3667,9 +3692,9 @@
 
 type FromLayoutPayload record {
     # The port that the transition can be made from
-    ballerina/lang.int:0.0.0:Signed32 fromPort?;
+    int:Signed32 fromPort?;
     # The port that the transition goes to
-    ballerina/lang.int:0.0.0:Signed32 toPortOverride?;
+    int:Signed32 toPortOverride?;
     # Every project-created entity has an ID that must be unique within the scope of the project creation. PCRI (Project Create Resource Identifier) is a standard format for creating IDs and references to other project entities. PCRI format is defined as follows: pcri:\[entityType\]:\[type\]:\[entityId\] entityType - the type of an entity, e.g. status, role, workflow type - PCRI type, either `id` - The ID of an entity that already exists in the target site, or `ref` - A unique reference to an entity that is being created entityId - entity identifier, if type is `id` - must be an existing entity ID that exists in the Jira site, if `ref` - must be unique across all entities in the scope of this project template creation
     ProjectCreateResourceIdentifier status?;
 };
@@ -3678,7 +3703,7 @@
 
 type ToLayoutPayload record {
     # Defines where the transition line will be connected to a status. Port 0 to 7 are acceptable values
-    ballerina/lang.int:0.0.0:Signed32 port?;
+    int:Signed32 port?;
     # Every project-created entity has an ID that must be unique within the scope of the project creation. PCRI (Project Create Resource Identifier) is a standard format for creating IDs and references to other project entities. PCRI format is defined as follows: pcri:\[entityType\]:\[type\]:\[entityId\] entityType - the type of an entity, e.g. status, role, workflow type - PCRI type, either `id` - The ID of an entity that already exists in the target site, or `ref` - A unique reference to an entity that is being created entityId - entity identifier, if type is `id` - must be an existing entity ID that exists in the Jira site, if `ref` - must be unique across all entities in the scope of this project template creation
     ProjectCreateResourceIdentifier status?;
 };
@@ -3704,7 +3729,7 @@
     # The ID of the issue type to filter results by. Must be provided with `projectKeyOrId`. Can't be provided with `issueId`
     string issueTypeId?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The ID or key of the project to filter results by. Must be provided with `issueTypeId`. Can't be provided with `issueId`
     string projectKeyOrId?;
     # The list of configuration IDs. To include multiple configurations, separate IDs with an ampersand: `id=10000&id=10001`. Can't be provided with `fieldContextId`, `issueId`, `projectKeyOrId`, or `issueTypeId`
@@ -4010,7 +4035,7 @@
     string 'type;
 };
 
-type CustomFieldContextDefaultValue ballerinax/jira:2.0.2:CustomFieldContextDefaultValueCascadingOption|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueMultipleOption|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueSingleOption|ballerinax/jira:2.0.2:CustomFieldContextSingleUserPickerDefaults|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueMultiUserPicker|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueSingleGroupPicker|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueMultipleGroupPicker|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueDate|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueDateTime|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueURL|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueProject|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueFloat|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueLabels|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueTextField|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueTextArea|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueReadOnly|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueSingleVersionPicker|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueMultipleVersionPicker|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueForgeStringField|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueForgeMultiStringField|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueForgeObjectField|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueForgeDateTimeField|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueForgeGroupField|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueForgeMultiGroupField|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueForgeNumberField|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueForgeUserField|ballerinax/jira:2.0.2:CustomFieldContextDefaultValueForgeMultiUserField;
+type CustomFieldContextDefaultValue CustomFieldContextDefaultValueCascadingOption|CustomFieldContextDefaultValueMultipleOption|CustomFieldContextDefaultValueSingleOption|CustomFieldContextSingleUserPickerDefaults|CustomFieldContextDefaultValueMultiUserPicker|CustomFieldContextDefaultValueSingleGroupPicker|CustomFieldContextDefaultValueMultipleGroupPicker|CustomFieldContextDefaultValueDate|CustomFieldContextDefaultValueDateTime|CustomFieldContextDefaultValueURL|CustomFieldContextDefaultValueProject|CustomFieldContextDefaultValueFloat|CustomFieldContextDefaultValueLabels|CustomFieldContextDefaultValueTextField|CustomFieldContextDefaultValueTextArea|CustomFieldContextDefaultValueReadOnly|CustomFieldContextDefaultValueSingleVersionPicker|CustomFieldContextDefaultValueMultipleVersionPicker|CustomFieldContextDefaultValueForgeStringField|CustomFieldContextDefaultValueForgeMultiStringField|CustomFieldContextDefaultValueForgeObjectField|CustomFieldContextDefaultValueForgeDateTimeField|CustomFieldContextDefaultValueForgeGroupField|CustomFieldContextDefaultValueForgeMultiGroupField|CustomFieldContextDefaultValueForgeNumberField|CustomFieldContextDefaultValueForgeUserField|CustomFieldContextDefaultValueForgeMultiUserField;
 
 # Represents the Queries record for the operation: getIdsOfWorklogsDeletedSince
 
@@ -4098,7 +4123,7 @@
     # Every project-created entity has an ID that must be unique within the scope of the project creation. PCRI (Project Create Resource Identifier) is a standard format for creating IDs and references to other project entities. PCRI format is defined as follows: pcri:\[entityType\]:\[type\]:\[entityId\] entityType - the type of an entity, e.g. status, role, workflow type - PCRI type, either `id` - The ID of an entity that already exists in the target site, or `ref` - A unique reference to an entity that is being created entityId - entity identifier, if type is `id` - must be an existing entity ID that exists in the Jira site, if `ref` - must be unique across all entities in the scope of this project template creation
     ProjectCreateResourceIdentifier pcri?;
     # Association between issuetypes and workflows
-    record {|ballerinax/jira:2.0.2:ProjectCreateResourceIdentifier...;|} explicitMappings?;
+    record {|ProjectCreateResourceIdentifier...;|} explicitMappings?;
 };
 
 # Represents the Queries record for the operation: getValidProjectName
@@ -4146,7 +4171,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -4186,7 +4211,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -4205,7 +4230,7 @@
     # A group ID to exclude from the result. To exclude multiple groups, provide an ampersand-separated list. For example, `excludeId=group1-id&excludeId=group2-id`. This parameter cannot be used with the `excludeGroups` parameter
     string[] excludeId?;
     # The maximum number of groups to return. The maximum number of groups that can be returned is limited by the system property `jira.ajax.autocomplete.limit`
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The string to find in group names
     string query?;
     # Whether the search for groups should be case insensitive
@@ -4219,7 +4244,7 @@
 
 
 type ExpandPrioritySchemePage record {
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     int startAt?;
     int total?;
 };
@@ -4230,7 +4255,7 @@
     # Whether only options are returned
     boolean onlyOptions?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The ID of the option
     int optionId?;
     # The index of the first item to return in a page of results (page offset)
@@ -4259,7 +4284,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -4320,7 +4345,7 @@
 
 type GetAllFieldConfigurationSchemesQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The list of field configuration scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`
     int[] id?;
     # The index of the first item to return in a page of results (page offset)
@@ -4337,7 +4362,7 @@
 
 type GetAllIssueFieldOptionsQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
 };
@@ -4348,11 +4373,11 @@
     # The total number of audit items returned
     int total?;
     # The number of audit items skipped before the first item in this list
-    ballerina/lang.int:0.0.0:Signed32 offset?;
+    int:Signed32 offset?;
     # The list of audit items
     AuditRecordBean[] records?;
     # The requested or default limit on the number of audit items to be returned
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
 };
 
 # An audit record
@@ -4444,7 +4469,7 @@
     # The ID of the issue type's avatar
     int avatarId?;
     # Hierarchy level of the issue type
-    ballerina/lang.int:0.0.0:Signed32 hierarchyLevel?;
+    int:Signed32 hierarchyLevel?;
     # Details of the next-gen projects the issue type is available in
     Scope scope?;
     # The name of the issue type
@@ -4462,7 +4487,7 @@
     # Whether this issue type is used to create subtasks
     boolean subtask?;
     # List of the fields available when creating an issue for the issue type
-    record {|ballerinax/jira:2.0.2:FieldMetadata...;|} fields?;
+    record {|FieldMetadata...;|} fields?;
 };
 
 # The metadata describing an issue field
@@ -4510,7 +4535,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -4533,13 +4558,14 @@
     # Every project-created entity has an ID that must be unique within the scope of the project creation. PCRI (Project Create Resource Identifier) is a standard format for creating IDs and references to other project entities. PCRI format is defined as follows: pcri:\[entityType\]:\[type\]:\[entityId\] entityType - the type of an entity, e.g. status, role, workflow type - PCRI type, either `id` - The ID of an entity that already exists in the target site, or `ref` - A unique reference to an entity that is being created entityId - entity identifier, if type is `id` - must be an existing entity ID that exists in the Jira site, if `ref` - must be unique across all entities in the scope of this project template creation
     ProjectCreateResourceIdentifier pcri?;
     # There is a default configuration "fieldlayout" that is applied to all issue types using this scheme that don't have an explicit mapping users can create (or re-use existing) configurations for other issue types and map them to this scheme
-    record {|ballerinax/jira:2.0.2:ProjectCreateResourceIdentifier...;|} explicitMappings?;
+    record {|ProjectCreateResourceIdentifier...;|} explicitMappings?;
 };
 
 # Represents the Queries record for the operation: removeWatcher
 
 type RemoveWatcherQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. Required
+    @constraint:String {maxLength: 128}
     string accountId?;
     # This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string username?;
@@ -4549,6 +4575,7 @@
 
 type GetUserDefaultColumnsQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string accountId?;
     # This parameter is no longer available See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string username?;
@@ -4595,6 +4622,7 @@
     # This parameter is deprecated because of privacy changes. Use `accountId` instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. User name used to return dashboards with the matching `owner.name`. This parameter cannot be used with the `accountId` parameter
     string owner?;
     # User account ID used to return dashboards with the matching `owner.accountId`. This parameter cannot be used with the `owner` parameter
+    @constraint:String {maxLength: 128}
     string accountId?;
     # Use [expand](#expansion) to include additional information about dashboard in the response. This parameter accepts a comma-separated list. Expand options include:
 
@@ -4608,7 +4636,7 @@
 *  `isWritable` Returns whether the current user has permission to edit the dashboard
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # Group ID used to return dashboards that are shared with a group that matches `sharePermissions.group.groupId`. This parameter cannot be used with the `groupname` parameter
     string groupId?;
     # [Order](#ordering) the results by a field:
@@ -4650,7 +4678,7 @@
 
 type GetVisibleIssueFieldOptionsQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # Filters the results to options that are only available in the specified project
     int projectId?;
     # The index of the first item to return in a page of results (page offset)
@@ -4691,7 +4719,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -4744,7 +4772,7 @@
 };
 
 # Details of an operand in a JQL clause
-type JqlQueryClauseOperand ballerinax/jira:2.0.2:ListOperand|ballerinax/jira:2.0.2:ValueOperand|ballerinax/jira:2.0.2:FunctionOperand|ballerinax/jira:2.0.2:KeywordOperand;
+type JqlQueryClauseOperand ListOperand|ValueOperand|FunctionOperand|KeywordOperand;
 
 # Details about a failed webhook
 
@@ -4819,9 +4847,10 @@
 *  `workflowUsages` Returns the workflows that use the status
     string expand?;
     # Term to match status names against or null to search for all statuses in the search scope
+    @constraint:String {maxLength: 255}
     string searchString?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # Category of the status to filter by. The supported values are: `TODO`, `IN_PROGRESS`, and `DONE`
     string statusCategory?;
     # The project the status is part of or null for global statuses
@@ -4843,7 +4872,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -4892,6 +4921,7 @@
 
 type DeleteUserPropertyQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string accountId?;
     # This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string userKey?;
@@ -5025,7 +5055,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -5054,7 +5084,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -5069,8 +5099,10 @@
 
 type FieldConfigurationDetails record {
     # The name of the field configuration. Must be unique
+    @constraint:String {maxLength: 255}
     string name;
     # The description of the field configuration
+    @constraint:String {maxLength: 255}
     string description?;
 };
 
@@ -5085,7 +5117,7 @@
 
 type GetDefaultValuesQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The IDs of the contexts
     int[] contextId?;
     # The index of the first item to return in a page of results (page offset)
@@ -5172,7 +5204,7 @@
 *  `user` Returns information about the user who is granted the permission
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The list of issue security level IDs. To include multiple issue security levels separate IDs with ampersand: `issueSecurityLevelId=10000&issueSecurityLevelId=10001`
     string[] issueSecurityLevelId?;
     # The index of the first item to return in a page of results (page offset)
@@ -5210,6 +5242,7 @@
 
 type UpdateUserToGroupBean record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.
+    @constraint:String {maxLength: 128}
     string accountId?;
     # This property is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
     string name?;
@@ -5266,7 +5299,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -5387,7 +5420,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -5421,7 +5454,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -5456,7 +5489,7 @@
 
 type FoundGroups record {
     # The total number of groups found in the search
-    ballerina/lang.int:0.0.0:Signed32 total?;
+    int:Signed32 total?;
     FoundGroup[] groups?;
     # Header text indicating the number of groups in the response and the total number of groups found in the search
     string header?;
@@ -5489,7 +5522,7 @@
 
 type FoundUsers record {
     # The total number of users found in the search
-    ballerina/lang.int:0.0.0:Signed32 total?;
+    int:Signed32 total?;
     # Header text indicating the number of users in the response and the total number of users found in the search
     string header?;
     UserPickerUser[] users?;
@@ -5533,7 +5566,7 @@
 
 type SimplifiedIssueTransition record {
     # The unique ID of the transition
-    ballerina/lang.int:0.0.0:Signed32 transitionId?;
+    int:Signed32 transitionId?;
     # The issue status change of the transition
     IssueTransitionStatus to?;
     # The name of the transition
@@ -5543,7 +5576,7 @@
 
 type IssueTransitionStatus record {
     # The unique ID of the status
-    ballerina/lang.int:0.0.0:Signed32 statusId?;
+    int:Signed32 statusId?;
     # The name of the status
     string statusName?;
 };
@@ -5609,7 +5642,8 @@
     string[] statusIds?;
 };
 
-// Unknown type: JqlQueriesToParseQueriesItemsString
+@constraint:String {minLength: 1}
+type JqlQueriesToParseQueriesItemsString string;
 
 
 type SearchAndReconcileRequestBean record {
@@ -5634,7 +5668,7 @@
 Additionally, `orderBy` clause can contain a maximum of 7 fields
     string jql?;
     # The maximum number of items to return per page. To manage page size, API may return fewer items per page where a large number of fields are requested. The greatest number of items returned per page is achieved when requesting `id` or `key` only. It returns max 5000 issues
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The token for a page to fetch that is not the first page. The first page has a `nextPageToken` of `null`. Use the `nextPageToken` to fetch the next page of issues
     string nextPageToken?;
     # Reference fields by their key (rather than ID). The default is `false`
@@ -5705,9 +5739,9 @@
     # The ADF pointer indicating the position of the text to be redacted. This is only required when redacting from rich text(ADF) fields. For plain text fields, this field can be omitted
     string adfPointer?;
     # The start index(inclusive) for the redaction in specified content
-    ballerina/lang.int:0.0.0:Signed32 'from;
+    int:Signed32 'from;
     # The ending index(exclusive) for the redaction in specified content
-    ballerina/lang.int:0.0.0:Signed32 to;
+    int:Signed32 to;
 };
 
 # Represents the content to redact
@@ -5758,6 +5792,7 @@
 
 type RemoveUserFromGroupQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string accountId;
     # The ID of the group. This parameter cannot be used with the `groupName` parameter
     string groupId?;
@@ -5776,7 +5811,7 @@
     # The name of a group. To specify multiple names, pass multiple `groupName` parameters. For example, `groupName=administrators&groupName=jira-software-users`
     string[] groupName?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The ID of a group. To specify multiple IDs, pass multiple `groupId` parameters. For example, `groupId=5b10a2844c20165700ede21g&groupId=5b10ac8d82e05b22cc7d4ef5`
     string[] groupId?;
     # The application key of the product user groups to search for. Valid values: 'jira-servicedesk', 'jira-software', 'jira-product-discovery', 'jira-core'
@@ -5790,7 +5825,7 @@
 type CardLayoutField record {
     "PLAN"|"WORK" mode?;
     int id?;
-    ballerina/lang.int:0.0.0:Signed32 position?;
+    int:Signed32 position?;
     string fieldId?;
 };
 
@@ -5807,18 +5842,18 @@
     # The cursor for pagination
     string nextPageToken?;
     # The maximum number of results to return. Must be an integer between 1 and 200
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
 };
 
 # Represents the Queries record for the operation: createIssueTypeAvatar
 
 type CreateIssueTypeAvatarQueries record {
     # The length of each side of the crop region
-    ballerina/lang.int:0.0.0:Signed32 size;
+    int:Signed32 size;
     # The X coordinate of the top-left corner of the crop region
-    ballerina/lang.int:0.0.0:Signed32 x?;
+    int:Signed32 x?;
     # The Y coordinate of the top-left corner of the crop region
-    ballerina/lang.int:0.0.0:Signed32 y?;
+    int:Signed32 y?;
 };
 
 # A page of items
@@ -5829,7 +5864,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -5870,7 +5905,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -5885,9 +5920,10 @@
 
 type GetCreateIssueMetaIssueTypesQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @constraint:Int {maxValue: 200}
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
 };
 
 # Details about the mapping between an issue type and a workflow
@@ -5924,9 +5960,9 @@
     # Whether a default thumbnail is returned when the requested thumbnail is not found
     boolean fallbackToDefault?;
     # The maximum width to scale the thumbnail to
-    ballerina/lang.int:0.0.0:Signed32 width?;
+    int:Signed32 width?;
     # The maximum height to scale the thumbnail to
-    ballerina/lang.int:0.0.0:Signed32 height?;
+    int:Signed32 height?;
 };
 
 # Details of workflows and their transition rules to delete
@@ -5963,9 +5999,9 @@
 
 type GetAllUsersQueries record {
     # The maximum number of items to return (limited to 1000)
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
 };
 
 # A page of items
@@ -5976,7 +6012,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -6083,7 +6119,7 @@
 *  `projectKeys` Returns all project keys associated with the project
     string expand?;
     # Returns the user's most recently accessed projects. You may specify the number of results to return up to a maximum of 20. If access is anonymous, then the recently accessed projects are based on the current HTTP session
-    ballerina/lang.int:0.0.0:Signed32 recent?;
+    int:Signed32 recent?;
     # A list of project properties to return for the project. This parameter accepts a comma-separated list
     string[] properties?;
 };
@@ -6267,7 +6303,7 @@
 
 type GetSelectableIssueFieldOptionsQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # Filters the results to options that are only available in the specified project
     int projectId?;
     # The index of the first item to return in a page of results (page offset)
@@ -6359,7 +6395,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -6378,7 +6414,7 @@
     # The project changes in the scheme
     SuggestedMappingsForProjectsRequestBean projects?;
     # The maximum number of results that could be on the page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The id of the priority scheme
     int schemeId?;
     # The index of the first item returned on the page
@@ -6623,7 +6659,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -6649,7 +6685,7 @@
     # The cursor for pagination
     string nextPageToken?;
     # The maximum number of results to return. Must be an integer between 1 and 200
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
 };
 
 # List of project avatars
@@ -6737,7 +6773,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -6761,8 +6797,10 @@
     # The list of level members which should be added to the issue security scheme level
     SecuritySchemeLevelMemberBean[] members?;
     # The name of the issue security scheme level. Must be unique
+    @constraint:String {maxLength: 255}
     string name;
     # The description of the issue security scheme level
+    @constraint:String {maxLength: 4000}
     string description?;
 };
 
@@ -6800,13 +6838,16 @@
 
 type PagedListUserDetailsApplicationUser record {
     # The number of items on the page
-    ballerina/lang.int:0.0.0:Signed32 size?;
+    int:Signed32 size?;
     # The index of the last item returned on the page
-    ballerina/lang.int:0.0.0:Signed32 endIndex?;
+    @jsondata:Name {value: "end-index"}
+    int:Signed32 endIndex?;
     # The maximum number of results that could be on the page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @jsondata:Name {value: "max-results"}
+    int:Signed32 maxResults?;
     # The index of the first item returned on the page
-    ballerina/lang.int:0.0.0:Signed32 startIndex?;
+    @jsondata:Name {value: "start-index"}
+    int:Signed32 startIndex?;
     # The list of items
     UserDetails[] items?;
 };
@@ -6841,7 +6882,7 @@
 
 type GetDynamicWebhooksForAppQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
 };
@@ -6863,11 +6904,11 @@
 
 type CreateProjectAvatarQueries record {
     # The length of each side of the crop region
-    ballerina/lang.int:0.0.0:Signed32 size?;
+    int:Signed32 size?;
     # The X coordinate of the top-left corner of the crop region
-    ballerina/lang.int:0.0.0:Signed32 x?;
+    int:Signed32 x?;
     # The Y coordinate of the top-left corner of the crop region
-    ballerina/lang.int:0.0.0:Signed32 y?;
+    int:Signed32 y?;
 };
 
 # Represents the Queries record for the operation: getApplicationProperty
@@ -6900,7 +6941,7 @@
     # Use [expand](#expansion) include additional information in the response. This parameter accepts `issueTypeScreenSchemes` that, for each screen schemes, returns information about the issue type screen scheme the screen scheme is assigned to
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # [Order](#ordering) the results by a field:
 
 *  `id` Sorts by screen scheme ID.
@@ -6945,6 +6986,7 @@
 
 type ConfigurationsListParameters record {
     # List of IDs or keys of the custom fields. It can be a mix of IDs and keys in the same query
+    @constraint:Array {minLength: 1}
     string[] fieldIdsOrKeys;
 };
 
@@ -7003,7 +7045,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -7022,7 +7064,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -7048,7 +7090,7 @@
 
 type GetAllLabelsQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
 };
@@ -7129,7 +7171,7 @@
 };
 
 # A JQL query clause
-type JqlQueryClause ballerinax/jira:2.0.2:CompoundClause|ballerinax/jira:2.0.2:FieldValueClause|ballerinax/jira:2.0.2:FieldWasClause|ballerinax/jira:2.0.2:FieldChangedClause;
+type JqlQueryClause CompoundClause|FieldValueClause|FieldWasClause|FieldChangedClause;
 
 # Represents the Queries record for the operation: getComments
 
@@ -7137,7 +7179,7 @@
     # Use [expand](#expansion) to include additional information about comments in the response. This parameter accepts `renderedBody`, which returns the comment body rendered in HTML
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # [Order](#ordering) the results by a field. Accepts *created* to sort comments by their created date
     "created"|"-created"|"+created" orderBy?;
     # The index of the first item to return in a page of results (page offset)
@@ -7171,7 +7213,7 @@
 
 type JexpJqlIssues record {
     # The maximum number of issues to return from the JQL query. Inspect `meta.issues.jql.maxResults` in the response to ensure the maximum value has not been exceeded
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The JQL query
     string query?;
     # The index of the first issue to return from the JQL query
@@ -7184,7 +7226,7 @@
 
 type GetScreensQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The scope filter string. To filter by multiple scope, provide an ampersand-separated list. For example, `scope=GLOBAL&scope=PROJECT`
     ("GLOBAL"|"TEMPLATE"|"PROJECT")[] scope?;
     # [Order](#ordering) the results by a field:
@@ -7255,6 +7297,7 @@
 
 type FindUsersWithAllPermissionsQueries record {
     # A query string that is matched exactly against user `accountId`. Required, unless `query` is specified
+    @constraint:String {maxLength: 128}
     string accountId?;
     # The project key for the project (case sensitive)
     string projectKey?;
@@ -7300,16 +7343,16 @@
 *  WORK\_ISSUE
     string permissions;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # A query string that is matched against user attributes, such as `displayName` and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `accountId` is specified
     string query?;
     # The index of the first item to return in a page of results (page offset)
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
     # This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string username?;
 };
 
-// Unknown type: CreatePrioritySchemeDetailsPriorityIdsItemsInteger
+type CreatePrioritySchemeDetailsPriorityIdsItemsInteger int;
 
 
 type StreamingResponseBody record {
@@ -7335,7 +7378,7 @@
     # The cursor to start from. If not provided, the first page will be returned
     string cursor?;
     # The maximum number of plan teams to return per page. The maximum value is 50. The default value is 50
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
 };
 
 # An ordered list of custom field option IDs and information on where to move them
@@ -7392,8 +7435,10 @@
 
 type UpdateNotificationSchemeDetails record {
     # The description of the notification scheme.
+    @constraint:String {maxLength: 4000}
     string description?;
     # The name of the notification scheme. Must be unique.
+    @constraint:String {maxLength: 255}
     string name?;
 };
 
@@ -7437,7 +7482,7 @@
 
 type Permissions record {
     # List of permissions
-    record {|ballerinax/jira:2.0.2:UserPermission...;|} permissions?;
+    record {|UserPermission...;|} permissions?;
 };
 
 
@@ -7556,8 +7601,10 @@
     # The default priority of the scheme
     int defaultPriorityId?;
     # The name of the priority scheme. Must be unique
+    @constraint:String {maxLength: 255}
     string name?;
     # The description of the priority scheme
+    @constraint:String {maxLength: 4000}
     string description?;
 };
 
@@ -7800,15 +7847,15 @@
     # The ID of the issue
     int issueID?;
     # Entity properties to set on the issue. The maximum length of an issue property value is 32768 characters
-    record {|ballerinax/jira:2.0.2:JsonNode...;|} properties?;
+    record {|JsonNode...;|} properties?;
 };
 
 
 type JiraExpressionsComplexityValueBean record {
     # The maximum allowed complexity. The evaluation will fail if this value is exceeded
-    ballerina/lang.int:0.0.0:Signed32 'limit;
+    int:Signed32 'limit;
     # The complexity value of the current expression
-    ballerina/lang.int:0.0.0:Signed32 value;
+    int:Signed32 value;
 };
 
 # A rule configuration
@@ -7817,6 +7864,7 @@
     # Whether the rule is disabled
     boolean disabled?;
     # A tag used to filter rules in [Get workflow transition rule configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-get)
+    @constraint:String {maxLength: 255}
     string tag?;
     # Configuration of the rule, as it is stored by the Connect or the Forge app on the rule configuration page
     string value;
@@ -7826,7 +7874,7 @@
 
 type GetFieldConfigurationSchemeProjectMappingQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The list of project IDs. To include multiple projects, separate IDs with ampersand: `projectId=10000&projectId=10001`
     int[] projectId;
     # The index of the first item to return in a page of results (page offset)
@@ -7842,9 +7890,9 @@
     # The part of the expression in which the error occurred
     string expression?;
     # The text line in which the error occurred
-    ballerina/lang.int:0.0.0:Signed32 line?;
+    int:Signed32 line?;
     # The text column in which the error occurred
-    ballerina/lang.int:0.0.0:Signed32 column?;
+    int:Signed32 column?;
     # Details about the error
     string message;
     # The error type
@@ -7873,6 +7921,7 @@
 
 type GetUserEmailQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, `5b10ac8d82e05b22cc7d4ef5`
+    @constraint:String {maxLength: 128}
     string accountId;
 };
 
@@ -7912,7 +7961,7 @@
 
 type GetCustomFieldContextsForProjectsAndIssueTypesQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
 };
@@ -7954,7 +8003,7 @@
 *  `approvers` Returns a list containing the approvers for this version
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # Filter the results using a literal string. Versions with matching `name` or `description` are returned (case insensitive)
     string query?;
     # [Order](#ordering) the results by a field:
@@ -8004,7 +8053,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -8084,7 +8133,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -8101,7 +8150,7 @@
     # Use [expand](#expansion) to include additional information in the response. This parameter accepts `projects` that, for each issue type screen schemes, returns information about the projects the issue type screen scheme is assigned to
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # [Order](#ordering) the results by a field:
 
 *  `name` Sorts by issue type screen scheme name.
@@ -8154,13 +8203,16 @@
 
 type UserList record {
     # The number of items on the page
-    ballerina/lang.int:0.0.0:Signed32 size?;
+    int:Signed32 size?;
     # The index of the last item returned on the page
-    ballerina/lang.int:0.0.0:Signed32 endIndex?;
+    @jsondata:Name {value: "end-index"}
+    int:Signed32 endIndex?;
     # The maximum number of results that could be on the page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @jsondata:Name {value: "max-results"}
+    int:Signed32 maxResults?;
     # The index of the first item returned on the page
-    ballerina/lang.int:0.0.0:Signed32 startIndex?;
+    @jsondata:Name {value: "start-index"}
+    int:Signed32 startIndex?;
     # The list of items
     User[] items?;
 };
@@ -8169,13 +8221,16 @@
 
 type FilterSubscriptionsList record {
     # The number of items on the page
-    ballerina/lang.int:0.0.0:Signed32 size?;
-    # The index of the last item returned on the page
-    ballerina/lang.int:0.0.0:Signed32 endIndex?;
+    int:Signed32 size?;
+    # The index of the last item returned on the page
+    @jsondata:Name {value: "end-index"}
+    int:Signed32 endIndex?;
     # The maximum number of results that could be on the page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @jsondata:Name {value: "max-results"}
+    int:Signed32 maxResults?;
     # The index of the first item returned on the page
-    ballerina/lang.int:0.0.0:Signed32 startIndex?;
+    @jsondata:Name {value: "start-index"}
+    int:Signed32 startIndex?;
     # The list of items
     FilterSubscription[] items?;
 };
@@ -8216,8 +8271,10 @@
 
 type UpdateIssueSecurityLevelDetails record {
     # The description of the issue security scheme level.
+    @constraint:String {maxLength: 255}
     string description?;
     # The name of the issue security scheme level. Must be unique.
+    @constraint:String {maxLength: 60}
     string name?;
 };
 
@@ -8229,7 +8286,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -8273,7 +8330,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -8385,7 +8442,7 @@
     LinkGroup[] groups?;
     # Details about the operations available in this version
     SimpleLink header?;
-    ballerina/lang.int:0.0.0:Signed32 weight?;
+    int:Signed32 weight?;
     SimpleLink[] links?;
     string id?;
     string styleClass?;
@@ -8406,7 +8463,7 @@
     # The list of issue type screen scheme IDs. To include multiple issue type screen schemes, separate IDs with ampersand: `issueTypeScreenSchemeId=10000&issueTypeScreenSchemeId=10001`
     int[] issueTypeScreenSchemeId?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
 };
@@ -8712,9 +8769,9 @@
 
 type GetAllUsersDefaultQueries record {
     # The maximum number of items to return (limited to 1000)
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
 };
 
 
@@ -8724,7 +8781,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The URL of the next page of results, if any
     string nextPage?;
     # The list of items
@@ -8768,7 +8825,7 @@
 
 type AttachmentArchiveImpl record {
     # The number of items in the archive
-    ballerina/lang.int:0.0.0:Signed32 totalEntryCount?;
+    int:Signed32 totalEntryCount?;
     # The list of the items included in the archive
     AttachmentArchiveEntry[] entries?;
 };
@@ -8790,7 +8847,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -8843,7 +8900,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -8934,7 +8991,7 @@
     # The ID of the group, which uniquely identifies the group across all Atlassian products.For example, *952d12c3-5b5b-4d04-bb32-44d383afc4b2*. Cannot be provided with `groupname`
     string groupId?;
     # The rights for the share permission
-    ballerina/lang.int:0.0.0:Signed32 rights?;
+    int:Signed32 rights?;
     # The type of the share permission.Specify the type as follows:
 
 *  `user` Share with a user.
@@ -8956,7 +9013,7 @@
 
 type GetPrecomputationsQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # [Order](#ordering) the results by a field:
 
 *  `functionKey` Sorts by the functionKey.
@@ -8979,7 +9036,7 @@
     # Expand options that include additional transition details in the response.
     string expand?;
     # Details of the fields associated with the issue transition screen. Use this information to populate `fields` and `update` in a transition request.
-    record {|ballerinax/jira:2.0.2:FieldMetadata...;|} fields?;
+    record {|FieldMetadata...;|} fields?;
     # Whether there is a screen associated with the issue transition.
     boolean hasScreen?;
     # The ID of the issue transition. Required when specifying a transition to undertake.
@@ -9022,8 +9079,10 @@
     # The ID of the default priority for the priority scheme
     int defaultPriorityId;
     # The name of the priority scheme. Must be unique
+    @constraint:String {maxLength: 255}
     string name;
     # The description of the priority scheme
+    @constraint:String {maxLength: 4000}
     string description?;
     # The IDs of projects that will use the priority scheme
     int[] projectIds?;
@@ -9071,9 +9130,9 @@
     # Any warnings related to the JQL query. Present only if the validation mode was set to `warn`
     string[] validationWarnings?;
     # The maximum number of issues that could be loaded in this evaluation
-    ballerina/lang.int:0.0.0:Signed32 maxResults;
+    int:Signed32 maxResults;
     # The number of issues that were loaded in this evaluation
-    ballerina/lang.int:0.0.0:Signed32 count;
+    int:Signed32 count;
     # The total number of issues the JQL returned
     int totalCount;
     # The index of the first issue
@@ -9097,6 +9156,7 @@
 # The level of validation to return from the API. If no values are provided, the default would return `WARNING` and `ERROR` level validation results
 
 type ValidationOptionsForUpdate record {
+    @constraint:Array {maxLength: 2}
     ("WARNING"|"ERROR")[] levels?;
 };
 
@@ -9156,7 +9216,7 @@
 
 type IssueBean record {
     # The schema describing each field present on the issue
-    record {|ballerinax/jira:2.0.2:JsonTypeBean...;|} schema?;
+    record {|JsonTypeBean...;|} schema?;
     # The metadata for the fields on the issue that can be amended
     IssueUpdateMetadata editmeta?;
     IncludedFields fieldsToInclude?;
@@ -9188,7 +9248,7 @@
 # A list of editable field details
 
 type IssueUpdateMetadata record {
-    record {|ballerinax/jira:2.0.2:FieldMetadata...;|} fields?;
+    record {|FieldMetadata...;|} fields?;
 };
 
 # Represents the Queries record for the operation: getFieldsPaginated
@@ -9205,7 +9265,7 @@
 *  `searcherKey` returns the searcher key for each custom field
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # String used to perform a case-insensitive partial match with field names or descriptions
     string query?;
     # [Order](#ordering) the results by:
@@ -9237,7 +9297,7 @@
     # The description of the data classification object
     string description?;
     # The rank of the data classification object
-    ballerina/lang.int:0.0.0:Signed32 rank?;
+    int:Signed32 rank?;
     # The ID of the data classification object
     string id;
     # The status of the data classification object
@@ -9248,8 +9308,10 @@
 
 type CreateNotificationSchemeDetails record {
     # The description of the notification scheme.
+    @constraint:String {maxLength: 4000}
     string description?;
     # The name of the notification scheme. Must be unique (case-insensitive).
+    @constraint:String {maxLength: 255}
     string name;
     # The list of notifications which should be added to the notification scheme.
     NotificationSchemeEventDetails[] notificationSchemeEvents?;
@@ -9305,7 +9367,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -9337,7 +9399,7 @@
 *  If a user has hidden their email address in their user profile, partial matches of the email address will not find the user. An exact match is required
     string jql?;
     # The maximum number of items to return per page. To manage page size, Jira may return fewer items per page where a large number of fields or properties are requested. The greatest number of items returned per page is achieved when requesting `id` or `key` only
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # Determines how to validate the JQL query and treat the validation results. Supported values are:
 
 *  `strict` Returns a 400 response code if any errors are found, along with a list of all errors (and warnings).
@@ -9367,7 +9429,7 @@
 Note: All navigable fields are returned by default. This differs from [GET issue](#api-rest-api-3-issue-issueIdOrKey-get) where the default is all fields
     string[] fields?;
     # The index of the first item to return in a page of results (page offset)
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
     # A list of issue property keys for issue properties to include in the results. This parameter accepts a comma-separated list. Multiple properties can also be provided using an ampersand separated list. For example, `properties=prop1,prop2&properties=prop3`. A maximum of 5 issue property keys can be specified
     string[] properties?;
     # Whether to fail the request quickly in case of an error while loading fields for an issue. For `failFast=true`, if one field fails, the entire operation fails. For `failFast=false`, the operation will continue even if a field fails. It will return a valid response, but without values for the failed field(s)
@@ -9405,6 +9467,7 @@
     # The value of string type custom field when `_type` is `StringIssueField`
     string 'string?;
     # The type of custom field
+    @jsondata:Name {value: "_type"}
     "StringIssueField"|"NumberIssueField"|"RichTextIssueField"|"SingleSelectIssueField"|"MultiSelectIssueField"|"TextIssueField" 'type;
     # The value of single select and multiselect custom field type when `_type` is `SingleSelectIssueField` or `MultiSelectIssueField`
     string optionID?;
@@ -9448,7 +9511,7 @@
 
 type GetFieldConfigurationItemsQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
 };
@@ -9549,7 +9612,7 @@
     # If *true* returns default field configurations only
     boolean isDefault?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The query string used to match against field configuration names and descriptions
     string query?;
     # The list of field configuration IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`
@@ -9562,7 +9625,7 @@
 
 type ProjectIssueTypesHierarchyLevel record {
     # The level of the issue type hierarchy level
-    ballerina/lang.int:0.0.0:Signed32 level?;
+    int:Signed32 level?;
     # The name of the issue type hierarchy level
     string name?;
     # The ID of the issue type hierarchy level. This property is deprecated, see [Change notice: Removing hierarchy level IDs from next-gen APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-gen-apis/)
@@ -9664,9 +9727,10 @@
 
 type IssueEntityProperties record {
     # A list of entity property IDs
+    @constraint:Array {maxLength: 10000, minLength: 1}
     int[] entitiesIds?;
     # A list of entity property keys and values
-    record {|ballerinax/jira:2.0.2:JsonNode...;|} properties?;
+    record {|JsonNode...;|} properties?;
 };
 
 # A list of matched issues or errors for each JQL query, in the order the JQL queries were passed
@@ -9692,7 +9756,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -9804,7 +9868,7 @@
     # A list of ids of issues approaching the limit and their field count
     record {|record {|int...;|}...;|} issuesApproachingLimit?;
     # The fields and their defined limits
-    record {|ballerina/lang.int:0.0.0:Signed32...;|} limits?;
+    record {|int:Signed32...;|} limits?;
 };
 
 # Represents the Queries record for the operation: deleteActor
@@ -9822,7 +9886,7 @@
 
 type TargetMandatoryFields record {
     # Contains the value of mandatory fields
-    record {|ballerinax/jira:2.0.2:Fields1...;|} fields;
+    record {|Fields1...;|} fields;
 };
 
 # The update workflow scheme payload
@@ -9893,7 +9957,7 @@
 *  `operations` For each workflow, returns information about the actions that can be undertaken on the workflow
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # [Order](#ordering) the results by a field:
 
 *  `name` Sorts by workflow name.
@@ -9934,6 +9998,7 @@
     # EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be returned. Available to users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg)
     boolean overrideSharePermissions?;
     # User account ID used to return filters with the matching `owner.accountId`. This parameter cannot be used with `owner`
+    @constraint:String {maxLength: 128}
     string accountId?;
     # Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:
 
@@ -9951,7 +10016,7 @@
 *  `viewUrl` Returns a URL to view the filter
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # When `true` this will perform a case-insensitive substring match for the provided `filterName`. When `false` the filter name will be searched using [full text search syntax](https://support.atlassian.com/jira-software-cloud/docs/search-for-issues-using-the-text-field/)
     boolean isSubstringMatch?;
     # The list of filter IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`. Do not exceed 200 filter IDs
@@ -9974,7 +10039,7 @@
     # Every project-created entity has an ID that must be unique within the scope of the project creation. PCRI (Project Create Resource Identifier) is a standard format for creating IDs and references to other project entities. PCRI format is defined as follows: pcri:\[entityType\]:\[type\]:\[entityId\] entityType - the type of an entity, e.g. status, role, workflow type - PCRI type, either `id` - The ID of an entity that already exists in the target site, or `ref` - A unique reference to an entity that is being created entityId - entity identifier, if type is `id` - must be an existing entity ID that exists in the Jira site, if `ref` - must be unique across all entities in the scope of this project template creation
     ProjectCreateResourceIdentifier pcri?;
     # The IDs of the screen schemes for the issue type IDs and default. A default entry is required to create an issue type screen scheme, it defines the mapping for all issue types without a screen scheme
-    record {|ballerinax/jira:2.0.2:ProjectCreateResourceIdentifier...;|} explicitMappings?;
+    record {|ProjectCreateResourceIdentifier...;|} explicitMappings?;
 };
 
 # An object representing the mapping of issues and data related to destination entities, like fields and statuses, that are required during a bulk move
@@ -10058,7 +10123,7 @@
 *  ***Destination project*** (Required): ID or key of the project to which the issues are being moved.
 *  ***Destination issueType*** (Required): ID of the issueType to which the issues are being moved.
 *  ***Destination parent ID or key*** (Optional): ID or key of the issue which will become the parent of the issues being moved. Only required when the destination issueType is a subtask
-    record {|ballerinax/jira:2.0.2:TargetToSourcesMapping...;|} targetToSourcesMapping?;
+    record {|TargetToSourcesMapping...;|} targetToSourcesMapping?;
 };
 
 # The details of a workflow
@@ -10088,9 +10153,10 @@
 
 type GetCreateIssueMetaIssueTypeIdQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @constraint:Int {maxValue: 200}
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
 };
 
 # The details of a created custom field context
@@ -10119,6 +10185,7 @@
 
 type SetUserColumnsQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string accountId?;
 };
 
@@ -10144,6 +10211,7 @@
 
 type GetUserGroupsQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string accountId;
     # This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string 'key?;
@@ -10159,7 +10227,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # List of workflows
@@ -10289,7 +10357,7 @@
     # The IDs of the releases excluded from the plan
     int[] releaseIds?;
     # Issues completed this number of days ago are excluded from the plan
-    ballerina/lang.int:0.0.0:Signed32 numberOfDaysToShowCompletedIssues;
+    int:Signed32 numberOfDaysToShowCompletedIssues;
     # The IDs of the issue types excluded from the plan
     int[] issueTypeIds?;
     # The IDs of the work status categories excluded from the plan
@@ -10325,7 +10393,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -10343,7 +10411,8 @@
     GetUserEmailBulkQueriesAccountIdItemsString[] accountId;
 };
 
-// Unknown type: GetUserEmailBulkQueriesAccountIdItemsString
+@constraint:String {maxLength: 128}
+type GetUserEmailBulkQueriesAccountIdItemsString string;
 
 # List of updates for a custom fields
 
@@ -10404,7 +10473,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -10442,6 +10511,7 @@
 
 type MigrationResourceUpdateEntityPropertiesValuePutHeaders record {
     # The app migration transfer ID
+    @http:Header {name: "Atlassian-Transfer-Id"}
     string atlassianTransferId;
 };
 
@@ -10466,13 +10536,13 @@
 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters have fallback values
     User submittedBy?;
     # The number of issues that are either invalid or issues that the user doesn't have permission to view, regardless of the success or failure of the operation
-    ballerina/lang.int:0.0.0:Signed32 invalidOrInaccessibleIssueCount?;
+    int:Signed32 invalidOrInaccessibleIssueCount?;
     # Map of issue IDs for which the operation failed and that the user has permission to view, to their one or more reasons for failure. These reasons are open-ended text descriptions of the error and are not selected from a predefined list of standard reasons
     record {|string[]...;|} failedAccessibleIssues?;
     # A timestamp of when the task was submitted
     string created?;
     # The number of issues that the bulk operation was attempted on
-    ballerina/lang.int:0.0.0:Signed32 totalIssueCount?;
+    int:Signed32 totalIssueCount?;
     # Progress of the task as a percentage
     int progressPercent?;
     # A timestamp of when the task was started
@@ -10606,7 +10676,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -10625,7 +10695,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -10678,7 +10748,7 @@
     string cursor?;
     int total?;
     boolean last?;
-    ballerina/lang.int:0.0.0:Signed32 size?;
+    int:Signed32 size?;
     string nextPageCursor?;
     GetTeamResponseForPage[] values?;
 };
@@ -10754,11 +10824,11 @@
 
 type PageOfWorklogs record {
     # The maximum number of results that could be on the page.
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item returned on the page.
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
     # The number of results on the page.
-    ballerina/lang.int:0.0.0:Signed32 total?;
+    int:Signed32 total?;
     # List of worklogs.
     Worklog[] worklogs?;
 };
@@ -10772,7 +10842,7 @@
 *  `contexts` Returns UI modification contexts
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
 };
@@ -11003,7 +11073,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -11040,7 +11110,7 @@
 *  `values.transitions` Returns the transitions that each workflow is associated with
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The scope of the workflow. Global for company-managed projects and Project for team-managed projects
     string scope?;
     # [Order](#ordering) the results by a field:
@@ -11099,7 +11169,7 @@
 *  `0` for Base.
 
 Defaults to `0`
-    ballerina/lang.int:0.0.0:Signed32 hierarchyLevel?;
+    int:Signed32 hierarchyLevel?;
     # The unique name for the issue type. The maximum length is 60 characters
     string name;
     # The description of the issue type
@@ -11153,7 +11223,7 @@
 
 type GetIssueTypeScreenSchemeProjectAssociationsQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The list of project IDs. To include multiple projects, separate IDs with ampersand: `projectId=10000&projectId=10001`
     int[] projectId;
     # The index of the first item to return in a page of results (page offset)
@@ -11173,7 +11243,7 @@
 
 type GetProjectComponentsPaginatedQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # Filter the results using a literal string. Components with a matching `name` or `description` are returned (case insensitive)
     string query?;
     # [Order](#ordering) the results by a field:
@@ -11204,7 +11274,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -11223,7 +11293,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -11238,7 +11308,7 @@
 
 type GetAllWorkflowSchemesQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
 };
@@ -11277,8 +11347,10 @@
 
 type UpdateResolutionDetails record {
     # The description of the resolution.
+    @constraint:String {maxLength: 255}
     string description?;
     # The name of the resolution. Must be unique.
+    @constraint:String {maxLength: 60}
     string name;
 };
 
@@ -11301,7 +11373,7 @@
 
 type SearchAndReconcileResults record {
     # The schema describing the field types in the search results
-    record {|ballerinax/jira:2.0.2:JsonTypeBean...;|} schema?;
+    record {|JsonTypeBean...;|} schema?;
     # The ID and name of each field in the search results
     record {|string...;|} names?;
     # Indicates whether this is the last page of the paginated response
@@ -11340,7 +11412,7 @@
 Note: The `nextPageToken` field is **not included** in the response for the last page, indicating there is no next page
     string nextPageToken?;
     # The maximum number of items to return per page. To manage page size, API may return fewer items per page where a large number of fields or properties are requested. The greatest number of items returned per page is achieved when requesting `id` or `key` only. It returns max 5000 issues
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # Reference fields by their key (rather than ID). The default is `false`
     boolean fieldsByKeys?;
     # A list of fields to return for each issue, use it to retrieve a subset of fields. This parameter accepts a comma-separated list. Expand options include:
@@ -11387,15 +11459,16 @@
 
 type FindUsersQueries record {
     # A query string that is matched exactly against a user `accountId`. Required, unless `query` or `property` is specified
+    @constraint:String {maxLength: 128}
     string accountId?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # A query string that is matched against user attributes ( `displayName`, and `emailAddress`) to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `accountId` or `property` is specified
     string query?;
     # A query string used to search properties. Property keys are specified by path, so property keys containing dot (.) or equals (=) characters cannot be used. The query string cannot be specified using a JSON object. Example: To search for the value of `nested` from `{"something":{"nested":1,"other":2}}` use `thepropertykey.something.nested=1`. Required, unless `accountId` or `query` is specified
     string property?;
     # The index of the first item to return in a page of filtered results (page offset)
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
     string username?;
 };
 
@@ -11436,7 +11509,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -11516,7 +11589,7 @@
     # The list of comments.
     Comment[] comments?;
     # The maximum number of items that could be returned.
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item returned.
     int startAt?;
     # The number of items returned.
@@ -11575,7 +11648,7 @@
     # The list of tab IDs. To include multiple tab IDs, provide an ampersand-separated list. For example, `tabId=10000&tabId=10001`
     int[] tabId?;
     # The maximum number of items to return per page. The maximum number is 100,
-    ballerina/lang.int:0.0.0:Signed32 maxResult?;
+    int:Signed32 maxResult?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
 };
@@ -11653,7 +11726,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -11709,7 +11782,7 @@
 
 type GetIssueTypeMappingsForContextsQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The ID of the context. To include multiple contexts, provide an ampersand-separated list. For example, `contextId=10001&contextId=10002`
     int[] contextId?;
     # The index of the first item to return in a page of results (page offset)
@@ -11727,6 +11800,7 @@
 
 type RemoveUserQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string accountId;
     # This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string 'key?;
@@ -11740,9 +11814,9 @@
     # The strings to match with audit field content, space separated
     string filter?;
     # The number of records to skip before returning the first result
-    ballerina/lang.int:0.0.0:Signed32 offset?;
+    int:Signed32 offset?;
     # The maximum number of results to return
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The date and time on or after which returned audit records must have been created. If `to` is provided `from` must be before `to` or no audit records are returned
     string 'from?;
     # The date and time on or before which returned audit results must have been created. If `from` is provided `to` must be after `from` or no audit records are returned
@@ -11813,7 +11887,7 @@
 
 type ScreenSchemePayload record {
     # Similar to the field layout scheme those mappings allow users to set different screens for different operations: default - always there, applied to all operations that don't have an explicit mapping `create`, `view`, `edit` - specific operations that are available and users can assign a different screen for each one of them https://support.atlassian.com/jira-cloud-administration/docs/manage-screen-schemes/\#Associating-a-screen-with-an-issue-operation
-    record {|ballerinax/jira:2.0.2:ProjectCreateResourceIdentifier...;|} screens?;
+    record {|ProjectCreateResourceIdentifier...;|} screens?;
     # Every project-created entity has an ID that must be unique within the scope of the project creation. PCRI (Project Create Resource Identifier) is a standard format for creating IDs and references to other project entities. PCRI format is defined as follows: pcri:\[entityType\]:\[type\]:\[entityId\] entityType - the type of an entity, e.g. status, role, workflow type - PCRI type, either `id` - The ID of an entity that already exists in the target site, or `ref` - A unique reference to an entity that is being created entityId - entity identifier, if type is `id` - must be an existing entity ID that exists in the Jira site, if `ref` - must be unique across all entities in the scope of this project template creation
     ProjectCreateResourceIdentifier defaultScreen?;
     # The name of the screen scheme
@@ -11832,7 +11906,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -11917,7 +11991,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -11989,7 +12063,7 @@
     # The conflict strategy to use when the issue type already exists. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters
     "FAIL"|"USE"|"NEW" onConflict?;
     # The hierarchy level of the issue type. 0, 1, 2, 3 .. n; Negative values for subtasks
-    ballerina/lang.int:0.0.0:Signed32 hierarchyLevel?;
+    int:Signed32 hierarchyLevel?;
     # The name of the issue type
     string name?;
     # Every project-created entity has an ID that must be unique within the scope of the project creation. PCRI (Project Create Resource Identifier) is a standard format for creating IDs and references to other project entities. PCRI format is defined as follows: pcri:\[entityType\]:\[type\]:\[entityId\] entityType - the type of an entity, e.g. status, role, workflow type - PCRI type, either `id` - The ID of an entity that already exists in the target site, or `ref` - A unique reference to an entity that is being created entityId - entity identifier, if type is `id` - must be an existing entity ID that exists in the Jira site, if `ref` - must be unique across all entities in the scope of this project template creation
@@ -12004,7 +12078,7 @@
     # The conflict strategy to use when the issue type already exists. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters
     "FAIL"|"USE"|"NEW" onConflict?;
     # The hierarchy level of the issue type. 0, 1, 2, 3 .. n; Negative values for subtasks
-    ballerina/lang.int:0.0.0:Signed32 hierarchyLevel?;
+    int:Signed32 hierarchyLevel?;
     # The name of the issue type
     string name?;
     # The description of the issue type
@@ -12046,7 +12120,7 @@
     # The list of roles to create
     RolePayload[] roles?;
     # A map of role PCRI (can be ID or REF) to a list of user or group PCRI IDs to associate with the role and project
-    record {|ballerinax/jira:2.0.2:ProjectCreateResourceIdentifier[]...;|} roleToProjectActors?;
+    record {|ProjectCreateResourceIdentifier[]...;|} roleToProjectActors?;
 };
 
 # A project's sender email address
@@ -12119,7 +12193,7 @@
     # The cursor for pagination
     string nextPageToken?;
     # The maximum number of results to return. Must be an integer between 1 and 200
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
 };
 
 
@@ -12204,7 +12278,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -12313,17 +12387,18 @@
 
 type FindUsersWithBrowsePermissionQueries record {
     # A query string that is matched exactly against user `accountId`. Required, unless `query` is specified
+    @constraint:String {maxLength: 128}
     string accountId?;
     # The project key for the project (case sensitive). Required, unless `issueKey` is specified
     string projectKey?;
     # The issue key for the issue. Required, unless `projectKey` is specified
     string issueKey?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # A query string that is matched against user attributes, such as `displayName` and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `accountId` is specified
     string query?;
     # The index of the first item to return in a page of results (page offset)
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
     # This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string username?;
 };
@@ -12357,6 +12432,7 @@
     # A brief description of the project
     string description?;
     # The account ID of the project lead. Cannot be provided with `lead`
+    @constraint:String {maxLength: 128}
     string leadAccountId?;
     # This parameter is deprecated because of privacy changes. Use `leadAccountId` instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. The user name of the project lead. Cannot be provided with `leadAccountId`
     string lead?;
@@ -12418,7 +12494,7 @@
     # Whether the calling user is watching this issue
     boolean isWatching?;
     # The number of users watching this issue
-    ballerina/lang.int:0.0.0:Signed32 watchCount?;
+    int:Signed32 watchCount?;
 };
 
 
@@ -12431,6 +12507,7 @@
 
 type SetUserNavPropertyQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string accountId?;
 };
 
@@ -12445,6 +12522,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|http:CredentialsConfig auth; // Special Agent Note: BearerTokenConfig, CredentialsConfig FROM ballerina/http package
@@ -12515,7 +12593,7 @@
 
 type GetIssueTypeSchemeForProjectsQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The list of project IDs. To include multiple project IDs, provide an ampersand-separated list. For example, `projectId=10000&projectId=10001`
     int[] projectId;
     # The index of the first item to return in a page of results (page offset)
@@ -12526,8 +12604,10 @@
 
 type UpdateFieldConfigurationSchemeDetails record {
     # The name of the field configuration scheme. The name must be unique
+    @constraint:String {maxLength: 255}
     string name;
     # The description of the field configuration scheme
+    @constraint:String {maxLength: 1024}
     string description?;
 };
 
@@ -12540,6 +12620,7 @@
     # The ID of the issue source for the plan-only team
     int issueSourceId?;
     # The plan-only team name
+    @constraint:String {maxLength: 255, minLength: 1}
     string name;
     # The sprint length for the plan-only team
     int sprintLength?;
@@ -12611,7 +12692,7 @@
 
 type GetContextsForFieldDeprecatedQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
 };
@@ -12625,7 +12706,7 @@
 *  `issueTypes` For each issue type schemes, returns information about the issueTypes the issue type scheme have
     string expand?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # [Order](#ordering) the results by a field:
 
 *  `name` Sorts by issue type scheme name.
@@ -12752,7 +12833,7 @@
     # Include inactive users
     boolean includeInactiveUsers?;
     # The maximum number of items to return per page (number should be between 1 and 50)
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The ID of the group. This parameter cannot be used with the `groupName` parameter
     string groupId?;
     # As a group's name can change, use of `groupId` is recommended to identify a group.  
@@ -12799,7 +12880,7 @@
 
 type GetProjectsForIssueTypeScreenSchemeQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     string query?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
@@ -12820,7 +12901,7 @@
 
 type FindComponentsForProjectsQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # Filter the results using a literal string. Components with a matching `name` or `description` are returned (case insensitive)
     string query?;
     # The project IDs and/or project keys (case sensitive)
@@ -12846,7 +12927,7 @@
     # Details of a transition. Required when performing a transition, optional when creating or editing an issue.
     IssueTransition transition?;
     # A Map containing the field field name and a list of operations to perform on the issue screen field. Note that fields included in here cannot be included in `fields`.
-    record {|ballerinax/jira:2.0.2:FieldUpdateOperation[]...;|} update?;
+    record {|FieldUpdateOperation[]...;|} update?;
 };
 
 # A list of issue link type beans
@@ -12860,7 +12941,7 @@
 
 type GetIssueTypeSchemesMappingQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The list of issue type scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `issueTypeSchemeId=10000&issueTypeSchemeId=10001`
     int[] issueTypeSchemeId?;
     # The index of the first item to return in a page of results (page offset)
@@ -12883,21 +12964,21 @@
 
 type SearchResults record {
     # The schema describing the field types in the search results
-    record {|ballerinax/jira:2.0.2:JsonTypeBean...;|} schema?;
+    record {|JsonTypeBean...;|} schema?;
     # Any warnings related to the JQL query
     string[] warningMessages?;
     # Expand options that include additional search result details in the response
     string expand?;
     # The number of results on the page
-    ballerina/lang.int:0.0.0:Signed32 total?;
+    int:Signed32 total?;
     # The ID and name of each field in the search results
     record {|string...;|} names?;
     # The maximum number of results that could be on the page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The list of issues found by the search
     IssueBean[] issues?;
     # The index of the first item returned on the page
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
 };
 
 # Represents the Queries record for the operation: setFavouriteForFilter
@@ -12918,7 +12999,7 @@
     # Whether to include archived plans in the results
     boolean includeArchived?;
     # The maximum number of plans to return per page. The maximum value is 50. The default value is 50
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # Whether to include trashed plans in the results
     boolean includeTrashed?;
 };
@@ -12996,7 +13077,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -13011,7 +13092,7 @@
 
 type FindUserKeysByQueryQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResult?;
+    int:Signed32 maxResult?;
     # The search query
     string query;
     # The index of the first item to return in a page of results (page offset)
@@ -13022,13 +13103,14 @@
 
 type FindAssignableUsersQueries record {
     # A query string that is matched exactly against user `accountId`. Required, unless `query` is specified
+    @constraint:String {maxLength: 128}
     string accountId?;
     # The ID of the issue. Required, unless `issueKey` or `project` is specified
     string issueId?;
     # The key of the issue. Required, unless `issueId` or `project` is specified
     string issueKey?;
     # The maximum number of items to return. This operation may return less than the maximum number of items even if more are available. The operation fetches users up to the maximum and then, from the fetched users, returns only the users that can be assigned to the issue
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # A query string that is matched against user attributes, such as `displayName`, and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `username` or `accountId` is specified
     string query?;
     # The project ID or project key (case sensitive). Required, unless `issueKey` or `issueId` is specified
@@ -13037,9 +13119,9 @@
     # The sessionId of this request. SessionId is the same until the assignee is set
     string sessionId?;
     # The index of the first item to return in a page of results (page offset)
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
     # The ID of the transition
-    ballerina/lang.int:0.0.0:Signed32 actionDescriptorId?;
+    int:Signed32 actionDescriptorId?;
     # This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string username?;
 };
@@ -13080,7 +13162,7 @@
 
 type GetFailedWebhooksQueries record {
     # The maximum number of webhooks to return per page. If obeying the maxResults directive would result in records with the same failure time being split across pages, the directive is ignored and all records with the same failure time included on the page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The time after which any webhook failure must have occurred for the record to be returned, expressed as milliseconds since the UNIX epoch
     int after?;
 };
@@ -13132,7 +13214,7 @@
     # The cursor for pagination
     string nextPageToken?;
     # The maximum number of results to return. Must be an integer between 1 and 200
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
 };
 
 # Identifiers for a project
@@ -13159,6 +13241,7 @@
 
 type GetUserPropertyKeysQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string accountId?;
     # This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string userKey?;
@@ -13175,7 +13258,7 @@
 
 type GetProjectContextMappingQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The list of context IDs. To include multiple context, separate IDs with ampersand: `contextId=10000&contextId=10001`
     int[] contextId?;
     # The index of the first item to return in a page of results (page offset)
@@ -13190,7 +13273,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -13212,7 +13295,7 @@
 
 type BulkGetUsersMigrationQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
     # Key of a user. To specify multiple users, pass multiple copies of this parameter. For example, `key=fred&key=barney`. Required if `username` isn't provided. Cannot be provided if `username` is present
@@ -13238,7 +13321,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -13257,7 +13340,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -13276,7 +13359,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -13291,7 +13374,7 @@
 
 type FindUsersByQueryQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The search query
     string query;
     # The index of the first item to return in a page of results (page offset)
@@ -13370,7 +13453,8 @@
 *  `insight` EXPERIMENTAL. Returns the insight details of total issue count and last issue update time for the project
     string expand?;
     # The maximum number of items to return per page. Must be less than or equal to 100. If a value greater than 100 is provided, the `maxResults` parameter will default to 100
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    @constraint:Int {maxValue: 100}
+    int:Signed32 maxResults?;
     # Filter results by projects for which the user can:
 
 *  `view` the project, meaning that they have one of the following permissions:
@@ -13409,7 +13493,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -13470,15 +13554,16 @@
 
 type FindBulkAssignableUsersQueries record {
     # A query string that is matched exactly against user `accountId`. Required, unless `query` is specified
+    @constraint:String {maxLength: 128}
     string accountId?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # A query string that is matched against user attributes, such as `displayName` and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `accountId` is specified
     string query?;
     # A list of project keys (case sensitive). This parameter accepts a comma-separated list
     string projectKeys;
     # The index of the first item to return in a page of results (page offset)
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
     # This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string username?;
 };
@@ -13491,7 +13576,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -13509,7 +13594,7 @@
     # The list of CreateMetaIssueType.
     IssueTypeIssueCreateMetadata[] issueTypes?;
     # The maximum number of items to return per page.
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item returned.
     int startAt?;
     # The total number of items in all pages.
@@ -13561,6 +13646,7 @@
 
 type GetUserQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. Required
+    @constraint:String {maxLength: 128}
     string accountId?;
     # Use [expand](#expansion) to include additional information about users in the response. This parameter accepts a comma-separated list. Expand options include:
 
@@ -13581,7 +13667,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -13660,6 +13746,7 @@
 
 type AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutHeaders record {
     # The ID of the transfer
+    @http:Header {name: "Atlassian-Transfer-Id"}
     string atlassianTransferId;
 };
 
@@ -13676,6 +13763,7 @@
     # Use expand to include additional information in the response. This parameter accepts `transition` which, for each rule, returns information about the transition the rule is assigned to
     string expand?;
     # The list of workflow rule IDs
+    @constraint:Array {maxLength: 10, minLength: 1}
     string[] ruleIds;
     # The workflow ID
     string workflowEntityId;
@@ -13689,7 +13777,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -13704,10 +13792,12 @@
 
 type CreateIssueSecuritySchemeDetails record {
     # The description of the issue security scheme.
+    @constraint:String {maxLength: 255}
     string description?;
     # The list of scheme levels which should be added to the security scheme.
     SecuritySchemeLevelBean[] levels?;
     # The name of the issue security scheme. Must be unique (case-insensitive).
+    @constraint:String {maxLength: 60}
     string name;
 };
 
@@ -13724,8 +13814,10 @@
 
 type CreateResolutionDetails record {
     # The description of the resolution.
+    @constraint:String {maxLength: 255}
     string description?;
     # The name of the resolution. Must be unique (case-insensitive).
+    @constraint:String {maxLength: 60}
     string name;
 };
 
@@ -13771,6 +13863,7 @@
 
 type SetUserPropertyQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string accountId?;
     # This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string userKey?;
@@ -13805,7 +13898,7 @@
 
 type BulkEditShareableEntityResponse record {
     # The mapping dashboard id to errors if any
-    record {|ballerinax/jira:2.0.2:BulkEditActionError...;|} entityErrors?;
+    record {|BulkEditActionError...;|} entityErrors?;
     # Allowed action for bulk edit shareable entity
     "changeOwner"|"changePermission"|"addPermission"|"removePermission" action;
 };
@@ -13816,7 +13909,7 @@
     # The URL to the next page of results. Present only if the request returned at least one result.The next page may be empty at the time of receiving the response, but new failed webhooks may appear in time. You can save the URL to the next page and query for new results periodically (for example, every hour)
     string next?;
     # The maximum number of items on the page. If the list of values is shorter than this number, then there are no more pages
-    ballerina/lang.int:0.0.0:Signed32 maxResults;
+    int:Signed32 maxResults;
     # The list of webhooks
     FailedWebhook[] values;
 };
@@ -13838,7 +13931,7 @@
     # The ID of the issue type to filter results by. Must be provided with `projectKeyOrId`. Can't be provided with `issueId`
     string issueTypeId?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The ID or key of the project to filter results by. Must be provided with `issueTypeId`. Can't be provided with `issueId`
     string projectKeyOrId?;
     # The list of configuration IDs. To include multiple configurations, separate IDs with an ampersand: `id=10000&id=10001`. Can't be provided with `fieldContextId`, `issueId`, `projectKeyOrId`, or `issueTypeId`
@@ -13851,8 +13944,9 @@
 
 type GetFieldConfigurationSchemeMappingsQueries record {
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The list of field configuration scheme IDs. To include multiple field configuration schemes separate IDs with ampersand: `fieldConfigurationSchemeId=10000&fieldConfigurationSchemeId=10001`
+    @constraint:Array {maxLength: 50, minLength: 1}
     int[] fieldConfigurationSchemeId?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
@@ -13907,6 +14001,7 @@
     # A brief description of the project
     string description?;
     # The account ID of the project lead. Either `lead` or `leadAccountId` must be set when creating a project. Cannot be provided with `lead`
+    @constraint:String {maxLength: 128}
     string leadAccountId?;
     # This parameter is deprecated because of privacy changes. Use `leadAccountId` instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. The user name of the project lead. Either `lead` or `leadAccountId` must be set when creating a project. Cannot be provided with `leadAccountId`
     string lead?;
@@ -13949,9 +14044,9 @@
 *  `my` Returns dashboards owned by the user
     "my"|"favourite" filter?;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
-    ballerina/lang.int:0.0.0:Signed32 startAt?;
+    int:Signed32 startAt?;
 };
 
 # Various counts of issues within a version
@@ -13982,7 +14077,7 @@
     # The account ID of a user. To specify multiple users, pass multiple `accountId` parameters. For example, `accountId=5b10a2844c20165700ede21g&accountId=5b10ac8d82e05b22cc7d4ef5`
     BulkGetUsersQueriesAccountIdItemsString[] accountId;
     # The maximum number of items to return per page
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # The index of the first item to return in a page of results (page offset)
     int startAt?;
     # This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
@@ -14003,8 +14098,10 @@
 
 type UpdateIssueSecuritySchemeRequestBean record {
     # The name of the security scheme scheme. Must be unique
+    @constraint:String {maxLength: 60}
     string name?;
     # The description of the security scheme scheme
+    @constraint:String {maxLength: 255}
     string description?;
 };
 
@@ -14143,6 +14240,7 @@
 
 type ResetUserColumnsQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string accountId?;
     # This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
     string username?;
@@ -14154,7 +14252,7 @@
     # A list of account IDs to exclude from the search results. This parameter accepts a comma-separated list. Multiple account IDs can also be provided using an ampersand-separated list. For example, `excludeAccountIds=5b10a2844c20165700ede21g,5b10a0effa615349cb016cd8&excludeAccountIds=5b10ac8d82e05b22cc7d4ef5`. Cannot be provided with `exclude`
     string[] excludeAccountIds?;
     # The maximum number of items to return. The total number of matched users is returned in `total`
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # A query string that is matched against user attributes, such as `displayName`, and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*
     string query;
     # This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details
@@ -14188,7 +14286,7 @@
     string cursor?;
     int total?;
     boolean last?;
-    ballerina/lang.int:0.0.0:Signed32 size?;
+    int:Signed32 size?;
     string nextPageCursor?;
     GetPlanResponseForPage[] values?;
 };
@@ -14201,7 +14299,7 @@
     # Whether this is the last page
     boolean isLast?;
     # The maximum number of items that could be returned
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
     # If there is another page of results, the URL of the next page
     string nextPage?;
     # The list of items
@@ -14216,6 +14314,7 @@
 
 type GetUserNavPropertyQueries record {
     # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*
+    @constraint:String {maxLength: 128}
     string accountId?;
 };
 
@@ -14229,6 +14328,7 @@
     # The URL of an icon for the priority. Accepted protocols are HTTP and HTTPS. Built in icons can also be used. Either the iconUrl or avatarId must be defined, but not both.
     "/images/icons/priorities/trivial_new.png"?|"/images/icons/priorities/blocker.png"|"/images/icons/priorities/critical.png"|"/images/icons/priorities/high.png"|"/images/icons/priorities/highest.png"|"/images/icons/priorities/low.png"|"/images/icons/priorities/lowest.png"|"/images/icons/priorities/major.png"|"/images/icons/priorities/medium.png"|"/images/icons/priorities/minor.png"|"/images/icons/priorities/trivial.png"|"/images/icons/priorities/blocker_new.png"|"/images/icons/priorities/critical_new.png"|"/images/icons/priorities/high_new.png"|"/images/icons/priorities/highest_new.png"|"/images/icons/priorities/low_new.png"|"/images/icons/priorities/lowest_new.png"|"/images/icons/priorities/major_new.png"|"/images/icons/priorities/medium_new.png"|"/images/icons/priorities/minor_new.png" iconUrl?;
     # The name of the priority. Must be unique.
+    @constraint:String {maxLength: 60}
     string name;
     # The status color of the priority in 3-digit or 6-digit hexadecimal format.
     string statusColor;
@@ -14249,7 +14349,7 @@
 *  `-1` for Subtask.
 *  `0` for Base.
 *  `1` for Epic
-    ballerina/lang.int:0.0.0:Signed32 level?;
+    int:Signed32 level?;
     # The ID of the project
     int projectId;
 };
@@ -14269,7 +14369,7 @@
     # The cursor for pagination
     string nextPageToken?;
     # The maximum number of results to return. Must be an integer between 1 and 200
-    ballerina/lang.int:0.0.0:Signed32 maxResults?;
+    int:Signed32 maxResults?;
 };
 
 # Represents the Queries record for the operation: searchSecuritySchemes
@@ -14301,15 +14401,15 @@
 
     # Bulk get custom field configurations
     # 
-    resource function post api/'3/app/'field/context/configuration/list(ConfigurationsListParameters payload, map<string|string[]> headers = {}, int[] fieldContextId = [], int issueId = 0, string issueTypeId = "", int:Signed32 maxResults = 0, string projectKeyOrId = "", int[] id = [], int startAt = 0, anydata Additional Values, GetCustomFieldsConfigurationsQueries queries) returns PageBeanBulkContextualConfiguration|error;
+    resource function post api/'3/app/'field/context/configuration/list(ConfigurationsListParameters payload, map<string|string[]> headers = {}, int[] fieldContextId = [], int issueId = 0, string issueTypeId = "", int:Signed32 maxResults = 0, string projectKeyOrId = "", int[] id = [], int startAt = 0, GetCustomFieldsConfigurationsQueries queries) returns PageBeanBulkContextualConfiguration|error;
 
     # Update custom fields
     # 
-    resource function post api/'3/app/'field/value(MultipleCustomFieldValuesUpdateDetails payload, map<string|string[]> headers = {}, boolean generateChangelog = false, anydata Additional Values, UpdateMultipleCustomFieldValuesQueries queries) returns json|error;
+    resource function post api/'3/app/'field/value(MultipleCustomFieldValuesUpdateDetails payload, map<string|string[]> headers = {}, boolean generateChangelog = false, UpdateMultipleCustomFieldValuesQueries queries) returns json|error;
 
     # Get custom field configurations
     # 
-    resource function get api/'3/app/'field/[string fieldIdOrKey]/context/configuration(map<string|string[]> headers = {}, int[] fieldContextId = [], int issueId = 0, string issueTypeId = "", int:Signed32 maxResults = 0, string projectKeyOrId = "", int[] id = [], int startAt = 0, anydata Additional Values, GetCustomFieldConfigurationQueries queries) returns PageBeanContextualConfiguration|error;
+    resource function get api/'3/app/'field/[string fieldIdOrKey]/context/configuration(map<string|string[]> headers = {}, int[] fieldContextId = [], int issueId = 0, string issueTypeId = "", int:Signed32 maxResults = 0, string projectKeyOrId = "", int[] id = [], int startAt = 0, GetCustomFieldConfigurationQueries queries) returns PageBeanContextualConfiguration|error;
 
     # Update custom field configurations
     # 
@@ -14317,11 +14417,11 @@
 
     # Update custom field value
     # 
-    resource function put api/'3/app/'field/[string fieldIdOrKey]/value(CustomFieldValueUpdateDetails payload, map<string|string[]> headers = {}, boolean generateChangelog = false, anydata Additional Values, UpdateCustomFieldValueQueries queries) returns json|error;
+    resource function put api/'3/app/'field/[string fieldIdOrKey]/value(CustomFieldValueUpdateDetails payload, map<string|string[]> headers = {}, boolean generateChangelog = false, UpdateCustomFieldValueQueries queries) returns json|error;
 
     # Get application property
     # 
-    resource function get api/'3/application\-properties(map<string|string[]> headers = {}, string permissionLevel = "", string keyFilter = "", string key = "", anydata Additional Values, GetApplicationPropertyQueries queries) returns ApplicationProperty[]|error;
+    resource function get api/'3/application\-properties(map<string|string[]> headers = {}, string permissionLevel = "", string keyFilter = "", string key = "", GetApplicationPropertyQueries queries) returns ApplicationProperty[]|error;
 
     # Get advanced settings
     # 
@@ -14341,7 +14441,7 @@
 
     # Get attachment content
     # 
-    resource function get api/'3/attachment/content/[string id](map<string|string[]> headers = {}, boolean redirect = false, anydata Additional Values, GetAttachmentContentQueries queries) returns anydata[]|error?;
+    resource function get api/'3/attachment/content/[string id](map<string|string[]> headers = {}, boolean redirect = false, GetAttachmentContentQueries queries) returns anydata[]|error?;
 
     # Get Jira attachment settings
     # 
@@ -14349,7 +14449,7 @@
 
     # Get attachment thumbnail
     # 
-    resource function get api/'3/attachment/thumbnail/[string id](map<string|string[]> headers = {}, boolean redirect = false, boolean fallbackToDefault = false, int:Signed32 width = 0, int:Signed32 height = 0, anydata Additional Values, GetAttachmentThumbnailQueries queries) returns anydata[]|error?;
+    resource function get api/'3/attachment/thumbnail/[string id](map<string|string[]> headers = {}, boolean redirect = false, boolean fallbackToDefault = false, int:Signed32 width = 0, int:Signed32 height = 0, GetAttachmentThumbnailQueries queries) returns anydata[]|error?;
 
     # Get attachment metadata
     # 
@@ -14369,7 +14469,7 @@
 
     # Get audit records
     # 
-    resource function get api/'3/auditing/'record(map<string|string[]> headers = {}, string filter = "", int:Signed32 offset = 0, int:Signed32 limit = 0, string from = "", string to = "", anydata Additional Values, GetAuditRecordsQueries queries) returns AuditRecords|error;
+    resource function get api/'3/auditing/'record(map<string|string[]> headers = {}, string filter = "", int:Signed32 offset = 0, int:Signed32 limit = 0, string from = "", string to = "", GetAuditRecordsQueries queries) returns AuditRecords|error;
 
     # Get system avatars by type
     # 
@@ -14381,7 +14481,7 @@
 
     # Get bulk editable fields
     # 
-    resource function get api/'3/bulk/issues/fields(map<string|string[]> headers = {}, string searchText = "", string startingAfter = "", string issueIdsOrKeys = "", string endingBefore = "", anydata Additional Values, GetBulkEditableFieldsQueries queries) returns BulkEditGetFields|error;
+    resource function get api/'3/bulk/issues/fields(map<string|string[]> headers = {}, string searchText = "", string startingAfter = "", string issueIdsOrKeys = "", string endingBefore = "", GetBulkEditableFieldsQueries queries) returns BulkEditGetFields|error;
 
     # Bulk edit issues
     # 
@@ -14393,7 +14493,7 @@
 
     # Get available transitions
     # 
-    resource function get api/'3/bulk/issues/transition(map<string|string[]> headers = {}, string startingAfter = "", string issueIdsOrKeys = "", string endingBefore = "", anydata Additional Values, GetAvailableTransitionsQueries queries) returns BulkTransitionGetAvailableTransitions|error;
+    resource function get api/'3/bulk/issues/transition(map<string|string[]> headers = {}, string startingAfter = "", string issueIdsOrKeys = "", string endingBefore = "", GetAvailableTransitionsQueries queries) returns BulkTransitionGetAvailableTransitions|error;
 
     # Bulk transition issue statuses
     # 
@@ -14417,11 +14517,11 @@
 
     # Get all classification levels
     # 
-    resource function get api/'3/classification\-levels(map<string|string[]> headers = {}, "rank"|"-rank"|"+rank" orderBy = "rank", ("PUBLISHED"|"ARCHIVED"|"DRAFT")[] status = [], anydata Additional Values, GetAllUserDataClassificationLevelsQueries queries) returns DataClassificationLevelsBean|error;
+    resource function get api/'3/classification\-levels(map<string|string[]> headers = {}, "rank"|"-rank"|"+rank" orderBy = "rank", ("PUBLISHED"|"ARCHIVED"|"DRAFT")[] status = [], GetAllUserDataClassificationLevelsQueries queries) returns DataClassificationLevelsBean|error;
 
     # Get comments by IDs
     # 
-    resource function post api/'3/comment/list(IssueCommentListRequestBean payload, map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetCommentsByIdsQueries queries) returns PageBeanComment|error;
+    resource function post api/'3/comment/list(IssueCommentListRequestBean payload, map<string|string[]> headers = {}, string expand = "", GetCommentsByIdsQueries queries) returns PageBeanComment|error;
 
     # Get comment property keys
     # 
@@ -14441,7 +14541,7 @@
 
     # Find components for projects
     # 
-    resource function get api/'3/component(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, string query = "", string[] projectIdsOrKeys = [], "description"|"-description"|"+description"|"name"|"-name"|"+name" orderBy = "description", int startAt = 0, anydata Additional Values, FindComponentsForProjectsQueries queries) returns PageBean2ComponentJsonBean|error;
+    resource function get api/'3/component(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, string query = "", string[] projectIdsOrKeys = [], "description"|"-description"|"+description"|"name"|"-name"|"+name" orderBy = "description", int startAt = 0, FindComponentsForProjectsQueries queries) returns PageBean2ComponentJsonBean|error;
 
     # Create component
     # 
@@ -14457,7 +14557,7 @@
 
     # Delete component
     # 
-    resource function delete api/'3/component/[string id](map<string|string[]> headers = {}, string moveIssuesTo = "", anydata Additional Values, DeleteComponentQueries queries) returns error?;
+    resource function delete api/'3/component/[string id](map<string|string[]> headers = {}, string moveIssuesTo = "", DeleteComponentQueries queries) returns error?;
 
     # Get component issues count
     # 
@@ -14493,11 +14593,11 @@
 
     # Get all dashboards
     # 
-    resource function get api/'3/dashboard(map<string|string[]> headers = {}, "my"|"favourite" filter = "my", int:Signed32 maxResults = 0, int:Signed32 startAt = 0, anydata Additional Values, GetAllDashboardsQueries queries) returns PageOfDashboards|error;
+    resource function get api/'3/dashboard(map<string|string[]> headers = {}, "my"|"favourite" filter = "my", int:Signed32 maxResults = 0, int:Signed32 startAt = 0, GetAllDashboardsQueries queries) returns PageOfDashboards|error;
 
     # Create dashboard
     # 
-    resource function post api/'3/dashboard(DashboardDetails payload, map<string|string[]> headers = {}, boolean extendAdminPermissions = false, anydata Additional Values, CreateDashboardQueries queries) returns Dashboard|error;
+    resource function post api/'3/dashboard(DashboardDetails payload, map<string|string[]> headers = {}, boolean extendAdminPermissions = false, CreateDashboardQueries queries) returns Dashboard|error;
 
     # Bulk edit dashboards
     # 
@@ -14509,11 +14609,11 @@
 
     # Search for dashboards
     # 
-    resource function get api/'3/dashboard/search(map<string|string[]> headers = {}, string owner = "", string accountId = "", string expand = "", int:Signed32 maxResults = 0, string groupId = "", "description"|"-description"|"+description"|"favorite_count"|"-favorite_count"|"+favorite_count"|"id"|"-id"|"+id"|"is_favorite"|"-is_favorite"|"+is_favorite"|"name"|"-name"|"+name"|"owner"|"-owner"|"+owner" orderBy = "description", string groupname = "", int projectId = 0, int startAt = 0, string dashboardName = "", "active"|"archived"|"deleted" status = "active", anydata Additional Values, GetDashboardsPaginatedQueries queries) returns PageBeanDashboard|error;
+    resource function get api/'3/dashboard/search(map<string|string[]> headers = {}, string owner = "", string accountId = "", string expand = "", int:Signed32 maxResults = 0, string groupId = "", "description"|"-description"|"+description"|"favorite_count"|"-favorite_count"|"+favorite_count"|"id"|"-id"|"+id"|"is_favorite"|"-is_favorite"|"+is_favorite"|"name"|"-name"|"+name"|"owner"|"-owner"|"+owner" orderBy = "description", string groupname = "", int projectId = 0, int startAt = 0, string dashboardName = "", "active"|"archived"|"deleted" status = "active", GetDashboardsPaginatedQueries queries) returns PageBeanDashboard|error;
 
     # Get gadgets
     # 
-    resource function get api/'3/dashboard/[int dashboardId]/gadget(map<string|string[]> headers = {}, int[] gadgetId = [], string[] uri = [], string[] moduleKey = [], anydata Additional Values, GetAllGadgetsQueries queries) returns DashboardGadgetResponse|error;
+    resource function get api/'3/dashboard/[int dashboardId]/gadget(map<string|string[]> headers = {}, int[] gadgetId = [], string[] uri = [], string[] moduleKey = [], GetAllGadgetsQueries queries) returns DashboardGadgetResponse|error;
 
     # Add gadget to dashboard
     # 
@@ -14549,7 +14649,7 @@
 
     # Update dashboard
     # 
-    resource function put api/'3/dashboard/[string id](DashboardDetails payload, map<string|string[]> headers = {}, boolean extendAdminPermissions = false, anydata Additional Values, UpdateDashboardQueries queries) returns Dashboard|error;
+    resource function put api/'3/dashboard/[string id](DashboardDetails payload, map<string|string[]> headers = {}, boolean extendAdminPermissions = false, UpdateDashboardQueries queries) returns Dashboard|error;
 
     # Delete dashboard
     # 
@@ -14557,7 +14657,7 @@
 
     # Copy dashboard
     # 
-    resource function post api/'3/dashboard/[string id]/copy(DashboardDetails payload, map<string|string[]> headers = {}, boolean extendAdminPermissions = false, anydata Additional Values, CopyDashboardQueries queries) returns Dashboard|error;
+    resource function post api/'3/dashboard/[string id]/copy(DashboardDetails payload, map<string|string[]> headers = {}, boolean extendAdminPermissions = false, CopyDashboardQueries queries) returns Dashboard|error;
 
     # Get data policy for the workspace
     # 
@@ -14565,7 +14665,7 @@
 
     # Get data policy for projects
     # 
-    resource function get api/'3/data\-policy/project(map<string|string[]> headers = {}, string ids = "", anydata Additional Values, GetPoliciesQueries queries) returns ProjectDataPolicies|error;
+    resource function get api/'3/data\-policy/project(map<string|string[]> headers = {}, string ids = "", GetPoliciesQueries queries) returns ProjectDataPolicies|error;
 
     # Get events
     # 
@@ -14573,15 +14673,15 @@
 
     # Analyse Jira expression
     # 
-    resource function post api/'3/expression/analyse(JiraExpressionForAnalysis payload, map<string|string[]> headers = {}, "syntax"|"type"|"complexity" check = "syntax", anydata Additional Values, AnalyseExpressionQueries queries) returns JiraExpressionsAnalysis|error;
+    resource function post api/'3/expression/analyse(JiraExpressionForAnalysis payload, map<string|string[]> headers = {}, "syntax"|"type"|"complexity" check = "syntax", AnalyseExpressionQueries queries) returns JiraExpressionsAnalysis|error;
 
     # Currently being removed. Evaluate Jira expression
     # 
-    resource function post api/'3/expression/eval(JiraExpressionEvalRequestBean payload, map<string|string[]> headers = {}, string expand = "", anydata Additional Values, EvaluateJiraExpressionQueries queries) returns JiraExpressionResult|error;
+    resource function post api/'3/expression/eval(JiraExpressionEvalRequestBean payload, map<string|string[]> headers = {}, string expand = "", EvaluateJiraExpressionQueries queries) returns JiraExpressionResult|error;
 
     # Evaluate Jira expression using enhanced search API
     # 
-    resource function post api/'3/expression/evaluate(JiraExpressionEvaluateRequestBean payload, map<string|string[]> headers = {}, string expand = "", anydata Additional Values, EvaluateJSISJiraExpressionQueries queries) returns JExpEvaluateJiraExpressionResultBean|error;
+    resource function post api/'3/expression/evaluate(JiraExpressionEvaluateRequestBean payload, map<string|string[]> headers = {}, string expand = "", EvaluateJSISJiraExpressionQueries queries) returns JExpEvaluateJiraExpressionResultBean|error;
 
     # Get fields
     # 
@@ -14601,11 +14701,11 @@
 
     # Get fields paginated
     # 
-    resource function get api/'3/'field/search(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, string query = "", "contextsCount"|"-contextsCount"|"+contextsCount"|"lastUsed"|"-lastUsed"|"+lastUsed"|"name"|"-name"|"+name"|"screensCount"|"-screensCount"|"+screensCount"|"projectsCount"|"-projectsCount"|"+projectsCount" orderBy = "contextsCount", string[] id = [], int[] projectIds = [], ("custom"|"system")[] type = [], int startAt = 0, anydata Additional Values, GetFieldsPaginatedQueries queries) returns PageBeanField|error;
+    resource function get api/'3/'field/search(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, string query = "", "contextsCount"|"-contextsCount"|"+contextsCount"|"lastUsed"|"-lastUsed"|"+lastUsed"|"name"|"-name"|"+name"|"screensCount"|"-screensCount"|"+screensCount"|"projectsCount"|"-projectsCount"|"+projectsCount" orderBy = "contextsCount", string[] id = [], int[] projectIds = [], ("custom"|"system")[] type = [], int startAt = 0, GetFieldsPaginatedQueries queries) returns PageBeanField|error;
 
     # Get fields in trash paginated
     # 
-    resource function get api/'3/'field/search/trashed(map<string|string[]> headers = {}, "name"|"-name"|"+name"|"trashDate"|"-trashDate"|"+trashDate"|"plannedDeletionDate"|"-plannedDeletionDate"|"+plannedDeletionDate"|"projectsCount"|"-projectsCount"|"+projectsCount" expand = "name", int:Signed32 maxResults = 0, string query = "", string orderBy = "", string[] id = [], int startAt = 0, anydata Additional Values, GetTrashedFieldsPaginatedQueries queries) returns PageBeanField|error;
+    resource function get api/'3/'field/search/trashed(map<string|string[]> headers = {}, "name"|"-name"|"+name"|"trashDate"|"-trashDate"|"+trashDate"|"plannedDeletionDate"|"-plannedDeletionDate"|"+plannedDeletionDate"|"projectsCount"|"-projectsCount"|"+projectsCount" expand = "name", int:Signed32 maxResults = 0, string query = "", string orderBy = "", string[] id = [], int startAt = 0, GetTrashedFieldsPaginatedQueries queries) returns PageBeanField|error;
 
     # Update custom field
     # 
@@ -14613,7 +14713,7 @@
 
     # Get custom field contexts
     # 
-    resource function get api/'3/'field/[string fieldId]/context(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] contextId = [], boolean isAnyIssueType = false, boolean isGlobalContext = false, int startAt = 0, anydata Additional Values, GetContextsForFieldQueries queries) returns PageBeanCustomFieldContext|error;
+    resource function get api/'3/'field/[string fieldId]/context(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] contextId = [], boolean isAnyIssueType = false, boolean isGlobalContext = false, int startAt = 0, GetContextsForFieldQueries queries) returns PageBeanCustomFieldContext|error;
 
     # Create custom field context
     # 
@@ -14621,7 +14721,7 @@
 
     # Get custom field contexts default values
     # 
-    resource function get api/'3/'field/[string fieldId]/context/defaultValue(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] contextId = [], int startAt = 0, anydata Additional Values, GetDefaultValuesQueries queries) returns PageBeanCustomFieldContextDefaultValue|error;
+    resource function get api/'3/'field/[string fieldId]/context/defaultValue(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] contextId = [], int startAt = 0, GetDefaultValuesQueries queries) returns PageBeanCustomFieldContextDefaultValue|error;
 
     # Set custom field contexts default values
     # 
@@ -14629,15 +14729,15 @@
 
     # Get issue types for custom field context
     # 
-    resource function get api/'3/'field/[string fieldId]/context/issuetypemapping(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] contextId = [], int startAt = 0, anydata Additional Values, GetIssueTypeMappingsForContextsQueries queries) returns PageBeanIssueTypeToContextMapping|error;
+    resource function get api/'3/'field/[string fieldId]/context/issuetypemapping(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] contextId = [], int startAt = 0, GetIssueTypeMappingsForContextsQueries queries) returns PageBeanIssueTypeToContextMapping|error;
 
     # Get custom field contexts for projects and issue types
     # 
-    resource function post api/'3/'field/[string fieldId]/context/mapping(ProjectIssueTypeMappings payload, map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, anydata Additional Values, GetCustomFieldContextsForProjectsAndIssueTypesQueries queries) returns PageBeanContextForProjectAndIssueType|error;
+    resource function post api/'3/'field/[string fieldId]/context/mapping(ProjectIssueTypeMappings payload, map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, GetCustomFieldContextsForProjectsAndIssueTypesQueries queries) returns PageBeanContextForProjectAndIssueType|error;
 
     # Get project mappings for custom field context
     # 
-    resource function get api/'3/'field/[string fieldId]/context/projectmapping(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] contextId = [], int startAt = 0, anydata Additional Values, GetProjectContextMappingQueries queries) returns PageBeanCustomFieldContextProjectMapping|error;
+    resource function get api/'3/'field/[string fieldId]/context/projectmapping(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] contextId = [], int startAt = 0, GetProjectContextMappingQueries queries) returns PageBeanCustomFieldContextProjectMapping|error;
 
     # Update custom field context
     # 
@@ -14657,7 +14757,7 @@
 
     # Get custom field options (context)
     # 
-    resource function get api/'3/'field/[string fieldId]/context/[int contextId]/option(map<string|string[]> headers = {}, boolean onlyOptions = false, int:Signed32 maxResults = 0, int optionId = 0, int startAt = 0, anydata Additional Values, GetOptionsForContextQueries queries) returns PageBeanCustomFieldContextOption|error;
+    resource function get api/'3/'field/[string fieldId]/context/[int contextId]/option(map<string|string[]> headers = {}, boolean onlyOptions = false, int:Signed32 maxResults = 0, int optionId = 0, int startAt = 0, GetOptionsForContextQueries queries) returns PageBeanCustomFieldContextOption|error;
 
     # Update custom field options (context)
     # 
@@ -14677,7 +14777,7 @@
 
     # Replace custom field options
     # 
-    resource function delete api/'3/'field/[string fieldId]/context/[int contextId]/option/[int optionId]/issue(map<string|string[]> headers = {}, string jql = "", int replaceWith = 0, anydata Additional Values, ReplaceCustomFieldOptionQueries queries) returns http:Response|error; // Special Agent Note: Response FROM ballerina/http package
+    resource function delete api/'3/'field/[string fieldId]/context/[int contextId]/option/[int optionId]/issue(map<string|string[]> headers = {}, string jql = "", int replaceWith = 0, ReplaceCustomFieldOptionQueries queries) returns http:Response|error; // Special Agent Note: Response FROM ballerina/http package
 
     # Assign custom field context to projects
     # 
@@ -14689,15 +14789,15 @@
 
     # Get contexts for a field
     # 
-    resource function get api/'3/'field/[string fieldId]/contexts(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, anydata Additional Values, GetContextsForFieldDeprecatedQueries queries) returns PageBeanContext|error;
+    resource function get api/'3/'field/[string fieldId]/contexts(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, GetContextsForFieldDeprecatedQueries queries) returns PageBeanContext|error;
 
     # Get screens for a field
     # 
-    resource function get api/'3/'field/[string fieldId]/screens(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, int startAt = 0, anydata Additional Values, GetScreensForFieldQueries queries) returns PageBeanScreenWithTab|error;
+    resource function get api/'3/'field/[string fieldId]/screens(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, int startAt = 0, GetScreensForFieldQueries queries) returns PageBeanScreenWithTab|error;
 
     # Get all issue field options
     # 
-    resource function get api/'3/'field/[string fieldKey]/option(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, anydata Additional Values, GetAllIssueFieldOptionsQueries queries) returns PageBeanIssueFieldOption|error;
+    resource function get api/'3/'field/[string fieldKey]/option(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, GetAllIssueFieldOptionsQueries queries) returns PageBeanIssueFieldOption|error;
 
     # Create issue field option
     # 
@@ -14705,11 +14805,11 @@
 
     # Get selectable issue field options
     # 
-    resource function get api/'3/'field/[string fieldKey]/option/suggestions/edit(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int projectId = 0, int startAt = 0, anydata Additional Values, GetSelectableIssueFieldOptionsQueries queries) returns PageBeanIssueFieldOption|error;
+    resource function get api/'3/'field/[string fieldKey]/option/suggestions/edit(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int projectId = 0, int startAt = 0, GetSelectableIssueFieldOptionsQueries queries) returns PageBeanIssueFieldOption|error;
 
     # Get visible issue field options
     # 
-    resource function get api/'3/'field/[string fieldKey]/option/suggestions/search(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int projectId = 0, int startAt = 0, anydata Additional Values, GetVisibleIssueFieldOptionsQueries queries) returns PageBeanIssueFieldOption|error;
+    resource function get api/'3/'field/[string fieldKey]/option/suggestions/search(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int projectId = 0, int startAt = 0, GetVisibleIssueFieldOptionsQueries queries) returns PageBeanIssueFieldOption|error;
 
     # Get issue field option
     # 
@@ -14725,7 +14825,7 @@
 
     # Replace issue field option
     # 
-    resource function delete api/'3/'field/[string fieldKey]/option/[int optionId]/issue(map<string|string[]> headers = {}, string jql = "", boolean overrideScreenSecurity = false, boolean overrideEditableFlag = false, int replaceWith = 0, anydata Additional Values, ReplaceIssueFieldOptionQueries queries) returns http:Response|error; // Special Agent Note: Response FROM ballerina/http package
+    resource function delete api/'3/'field/[string fieldKey]/option/[int optionId]/issue(map<string|string[]> headers = {}, string jql = "", boolean overrideScreenSecurity = false, boolean overrideEditableFlag = false, int replaceWith = 0, ReplaceIssueFieldOptionQueries queries) returns http:Response|error; // Special Agent Note: Response FROM ballerina/http package
 
     # Delete custom field
     # 
@@ -14739,7 +14839,7 @@
 
     # Get all field configurations
     # 
-    resource function get api/'3/fieldconfiguration(map<string|string[]> headers = {}, boolean isDefault = false, int:Signed32 maxResults = 0, string query = "", int[] id = [], int startAt = 0, anydata Additional Values, GetAllFieldConfigurationsQueries queries) returns PageBeanFieldConfigurationDetails|error;
+    resource function get api/'3/fieldconfiguration(map<string|string[]> headers = {}, boolean isDefault = false, int:Signed32 maxResults = 0, string query = "", int[] id = [], int startAt = 0, GetAllFieldConfigurationsQueries queries) returns PageBeanFieldConfigurationDetails|error;
 
     # Create field configuration
     # 
@@ -14755,7 +14855,7 @@
 
     # Get field configuration items
     # 
-    resource function get api/'3/fieldconfiguration/[int id]/fields(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, anydata Additional Values, GetFieldConfigurationItemsQueries queries) returns PageBeanFieldConfigurationItem|error;
+    resource function get api/'3/fieldconfiguration/[int id]/fields(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, GetFieldConfigurationItemsQueries queries) returns PageBeanFieldConfigurationItem|error;
 
     # Update field configuration items
     # 
@@ -14763,7 +14863,7 @@
 
     # Get all field configuration schemes
     # 
-    resource function get api/'3/fieldconfigurationscheme(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] id = [], int startAt = 0, anydata Additional Values, GetAllFieldConfigurationSchemesQueries queries) returns PageBeanFieldConfigurationScheme|error;
+    resource function get api/'3/fieldconfigurationscheme(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] id = [], int startAt = 0, GetAllFieldConfigurationSchemesQueries queries) returns PageBeanFieldConfigurationScheme|error;
 
     # Create field configuration scheme
     # 
@@ -14771,11 +14871,11 @@
 
     # Get field configuration issue type items
     # 
-    resource function get api/'3/fieldconfigurationscheme/mapping(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] fieldConfigurationSchemeId = [], int startAt = 0, anydata Additional Values, GetFieldConfigurationSchemeMappingsQueries queries) returns PageBeanFieldConfigurationIssueTypeItem|error;
+    resource function get api/'3/fieldconfigurationscheme/mapping(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] fieldConfigurationSchemeId = [], int startAt = 0, GetFieldConfigurationSchemeMappingsQueries queries) returns PageBeanFieldConfigurationIssueTypeItem|error;
 
     # Get field configuration schemes for projects
     # 
-    resource function get api/'3/fieldconfigurationscheme/project(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] projectId = [], int startAt = 0, anydata Additional Values, GetFieldConfigurationSchemeProjectMappingQueries queries) returns PageBeanFieldConfigurationSchemeProjects|error;
+    resource function get api/'3/fieldconfigurationscheme/project(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] projectId = [], int startAt = 0, GetFieldConfigurationSchemeProjectMappingQueries queries) returns PageBeanFieldConfigurationSchemeProjects|error;
 
     # Assign field configuration scheme to project
     # 
@@ -14799,7 +14899,7 @@
 
     # Create filter
     # 
-    resource function post api/'3/filter(Filter payload, map<string|string[]> headers = {}, boolean overrideSharePermissions = false, string expand = "", anydata Additional Values, CreateFilterQueries queries) returns Filter|error;
+    resource function post api/'3/filter(Filter payload, map<string|string[]> headers = {}, boolean overrideSharePermissions = false, string expand = "", CreateFilterQueries queries) returns Filter|error;
 
     # Get default share scope
     # 
@@ -14811,23 +14911,23 @@
 
     # Get favorite filters
     # 
-    resource function get api/'3/filter/favourite(map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetFavouriteFiltersQueries queries) returns Filter[]|error;
+    resource function get api/'3/filter/favourite(map<string|string[]> headers = {}, string expand = "", GetFavouriteFiltersQueries queries) returns Filter[]|error;
 
     # Get my filters
     # 
-    resource function get api/'3/filter/my(map<string|string[]> headers = {}, string expand = "", boolean includeFavourites = false, anydata Additional Values, GetMyFiltersQueries queries) returns Filter[]|error;
+    resource function get api/'3/filter/my(map<string|string[]> headers = {}, string expand = "", boolean includeFavourites = false, GetMyFiltersQueries queries) returns Filter[]|error;
 
     # Search for filters
     # 
-    resource function get api/'3/filter/search(map<string|string[]> headers = {}, string owner = "", string groupId = "", string filterName = "", "description"|"-description"|"+description"|"favourite_count"|"-favourite_count"|"+favourite_count"|"id"|"-id"|"+id"|"is_favourite"|"-is_favourite"|"+is_favourite"|"name"|"-name"|"+name"|"owner"|"-owner"|"+owner"|"is_shared"|"-is_shared"|"+is_shared" orderBy = "description", string groupname = "", boolean overrideSharePermissions = false, string accountId = "", string expand = "", int:Signed32 maxResults = 0, boolean isSubstringMatch = false, int[] id = [], int projectId = 0, int startAt = 0, anydata Additional Values, GetFiltersPaginatedQueries queries) returns PageBeanFilterDetails|error;
+    resource function get api/'3/filter/search(map<string|string[]> headers = {}, string owner = "", string groupId = "", string filterName = "", "description"|"-description"|"+description"|"favourite_count"|"-favourite_count"|"+favourite_count"|"id"|"-id"|"+id"|"is_favourite"|"-is_favourite"|"+is_favourite"|"name"|"-name"|"+name"|"owner"|"-owner"|"+owner"|"is_shared"|"-is_shared"|"+is_shared" orderBy = "description", string groupname = "", boolean overrideSharePermissions = false, string accountId = "", string expand = "", int:Signed32 maxResults = 0, boolean isSubstringMatch = false, int[] id = [], int projectId = 0, int startAt = 0, GetFiltersPaginatedQueries queries) returns PageBeanFilterDetails|error;
 
     # Get filter
     # 
-    resource function get api/'3/filter/[int id](map<string|string[]> headers = {}, boolean overrideSharePermissions = false, string expand = "", anydata Additional Values, GetFilterQueries queries) returns Filter|error;
+    resource function get api/'3/filter/[int id](map<string|string[]> headers = {}, boolean overrideSharePermissions = false, string expand = "", GetFilterQueries queries) returns Filter|error;
 
     # Update filter
     # 
-    resource function put api/'3/filter/[int id](Filter payload, map<string|string[]> headers = {}, boolean overrideSharePermissions = false, string expand = "", anydata Additional Values, UpdateFilterQueries queries) returns Filter|error;
+    resource function put api/'3/filter/[int id](Filter payload, map<string|string[]> headers = {}, boolean overrideSharePermissions = false, string expand = "", UpdateFilterQueries queries) returns Filter|error;
 
     # Delete filter
     # 
@@ -14847,11 +14947,11 @@
 
     # Add filter as favorite
     # 
-    resource function put api/'3/filter/[int id]/favourite(map<string|string[]> headers = {}, string expand = "", anydata Additional Values, SetFavouriteForFilterQueries queries) returns Filter|error;
+    resource function put api/'3/filter/[int id]/favourite(map<string|string[]> headers = {}, string expand = "", SetFavouriteForFilterQueries queries) returns Filter|error;
 
     # Remove filter as favorite
     # 
-    resource function delete api/'3/filter/[int id]/favourite(map<string|string[]> headers = {}, string expand = "", anydata Additional Values, DeleteFavouriteForFilterQueries queries) returns Filter|error;
+    resource function delete api/'3/filter/[int id]/favourite(map<string|string[]> headers = {}, string expand = "", DeleteFavouriteForFilterQueries queries) returns Filter|error;
 
     # Change filter owner
     # 
@@ -14875,7 +14975,7 @@
 
     # Get group
     # 
-    resource function get api/'3/group(map<string|string[]> headers = {}, string expand = "", string groupId = "", string groupname = "", anydata Additional Values, GetGroupQueries queries) returns Group|error;
+    resource function get api/'3/group(map<string|string[]> headers = {}, string expand = "", string groupId = "", string groupname = "", GetGroupQueries queries) returns Group|error;
 
     # Create group
     # 
@@ -14883,31 +14983,31 @@
 
     # Remove group
     # 
-    resource function delete api/'3/group(map<string|string[]> headers = {}, string swapGroupId = "", string groupId = "", string groupname = "", string swapGroup = "", anydata Additional Values, RemoveGroupQueries queries) returns error?;
+    resource function delete api/'3/group(map<string|string[]> headers = {}, string swapGroupId = "", string groupId = "", string groupname = "", string swapGroup = "", RemoveGroupQueries queries) returns error?;
 
     # Bulk get groups
     # 
-    resource function get api/'3/group/bulk(map<string|string[]> headers = {}, string accessType = "", string[] groupName = [], int:Signed32 maxResults = 0, string[] groupId = [], string applicationKey = "", int startAt = 0, anydata Additional Values, BulkGetGroupsQueries queries) returns PageBeanGroupDetails|error;
+    resource function get api/'3/group/bulk(map<string|string[]> headers = {}, string accessType = "", string[] groupName = [], int:Signed32 maxResults = 0, string[] groupId = [], string applicationKey = "", int startAt = 0, BulkGetGroupsQueries queries) returns PageBeanGroupDetails|error;
 
     # Get users from group
     # 
-    resource function get api/'3/group/member(map<string|string[]> headers = {}, boolean includeInactiveUsers = false, int:Signed32 maxResults = 0, string groupId = "", string groupname = "", int startAt = 0, anydata Additional Values, GetUsersFromGroupQueries queries) returns PageBeanUserDetails|error;
+    resource function get api/'3/group/member(map<string|string[]> headers = {}, boolean includeInactiveUsers = false, int:Signed32 maxResults = 0, string groupId = "", string groupname = "", int startAt = 0, GetUsersFromGroupQueries queries) returns PageBeanUserDetails|error;
 
     # Add user to group
     # 
-    resource function post api/'3/group/user(UpdateUserToGroupBean payload, map<string|string[]> headers = {}, string groupId = "", string groupname = "", anydata Additional Values, AddUserToGroupQueries queries) returns Group|error;
+    resource function post api/'3/group/user(UpdateUserToGroupBean payload, map<string|string[]> headers = {}, string groupId = "", string groupname = "", AddUserToGroupQueries queries) returns Group|error;
 
     # Remove user from group
     # 
-    resource function delete api/'3/group/user(map<string|string[]> headers = {}, string accountId = "", string groupId = "", string groupname = "", string username = "", anydata Additional Values, RemoveUserFromGroupQueries queries) returns error?;
+    resource function delete api/'3/group/user(map<string|string[]> headers = {}, string accountId = "", string groupId = "", string groupname = "", string username = "", RemoveUserFromGroupQueries queries) returns error?;
 
     # Find groups
     # 
-    resource function get api/'3/groups/picker(map<string|string[]> headers = {}, string accountId = "", string[] excludeId = [], int:Signed32 maxResults = 0, string query = "", boolean caseInsensitive = false, string[] exclude = [], string userName = "", anydata Additional Values, FindGroupsQueries queries) returns FoundGroups|error;
+    resource function get api/'3/groups/picker(map<string|string[]> headers = {}, string accountId = "", string[] excludeId = [], int:Signed32 maxResults = 0, string query = "", boolean caseInsensitive = false, string[] exclude = [], string userName = "", FindGroupsQueries queries) returns FoundGroups|error;
 
     # Find users and groups
     # 
-    resource function get api/'3/groupuserpicker(map<string|string[]> headers = {}, boolean excludeConnectAddons = false, string[] issueTypeId = [], int:Signed32 maxResults = 0, string query = "", boolean caseInsensitive = false, boolean showAvatar = false, string[] projectId = [], "xsmall"|"xsmall@2x"|"xsmall@3x"|"small"|"small@2x"|"small@3x"|"medium"|"medium@2x"|"medium@3x"|"large"|"large@2x"|"large@3x"|"xlarge"|"xlarge@2x"|"xlarge@3x"|"xxlarge"|"xxlarge@2x"|"xxlarge@3x"|"xxxlarge"|"xxxlarge@2x"|"xxxlarge@3x" avatarSize = "xsmall", string fieldId = "", anydata Additional Values, FindUsersAndGroupsQueries queries) returns FoundUsersAndGroups|error;
+    resource function get api/'3/groupuserpicker(map<string|string[]> headers = {}, boolean excludeConnectAddons = false, string[] issueTypeId = [], int:Signed32 maxResults = 0, string query = "", boolean caseInsensitive = false, boolean showAvatar = false, string[] projectId = [], "xsmall"|"xsmall@2x"|"xsmall@3x"|"small"|"small@2x"|"small@3x"|"medium"|"medium@2x"|"medium@3x"|"large"|"large@2x"|"large@3x"|"xlarge"|"xlarge@2x"|"xlarge@3x"|"xxlarge"|"xxlarge@2x"|"xxlarge@3x"|"xxxlarge"|"xxxlarge@2x"|"xxxlarge@3x" avatarSize = "xsmall", string fieldId = "", FindUsersAndGroupsQueries queries) returns FoundUsersAndGroups|error;
 
     # Get license
     # 
@@ -14915,7 +15015,7 @@
 
     # Create issue
     # 
-    resource function post api/'3/issue(IssueUpdateDetails payload, map<string|string[]> headers = {}, boolean updateHistory = false, anydata Additional Values, CreateIssueQueries queries) returns CreatedIssue|error;
+    resource function post api/'3/issue(IssueUpdateDetails payload, map<string|string[]> headers = {}, boolean updateHistory = false, CreateIssueQueries queries) returns CreatedIssue|error;
 
     # Archive issue(s) by issue ID/key
     # 
@@ -14935,23 +15035,23 @@
 
     # Get create issue metadata
     # 
-    resource function get api/'3/issue/createmeta(map<string|string[]> headers = {}, string expand = "", string[] issuetypeNames = [], string[] projectIds = [], string[] projectKeys = [], string[] issuetypeIds = [], anydata Additional Values, GetCreateIssueMetaQueries queries) returns IssueCreateMetadata|error;
+    resource function get api/'3/issue/createmeta(map<string|string[]> headers = {}, string expand = "", string[] issuetypeNames = [], string[] projectIds = [], string[] projectKeys = [], string[] issuetypeIds = [], GetCreateIssueMetaQueries queries) returns IssueCreateMetadata|error;
 
     # Get create metadata issue types for a project
     # 
-    resource function get api/'3/issue/createmeta/[string projectIdOrKey]/issuetypes(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int:Signed32 startAt = 0, anydata Additional Values, GetCreateIssueMetaIssueTypesQueries queries) returns PageOfCreateMetaIssueTypes|error;
+    resource function get api/'3/issue/createmeta/[string projectIdOrKey]/issuetypes(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int:Signed32 startAt = 0, GetCreateIssueMetaIssueTypesQueries queries) returns PageOfCreateMetaIssueTypes|error;
 
     # Get create field metadata for a project and issue type id
     # 
-    resource function get api/'3/issue/createmeta/[string projectIdOrKey]/issuetypes/[string issueTypeId](map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int:Signed32 startAt = 0, anydata Additional Values, GetCreateIssueMetaIssueTypeIdQueries queries) returns PageOfCreateMetaIssueTypeWithField|error;
+    resource function get api/'3/issue/createmeta/[string projectIdOrKey]/issuetypes/[string issueTypeId](map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int:Signed32 startAt = 0, GetCreateIssueMetaIssueTypeIdQueries queries) returns PageOfCreateMetaIssueTypeWithField|error;
 
     # Get issue limit report
     # 
-    resource function get api/'3/issue/'limit/report(map<string|string[]> headers = {}, boolean isReturningKeys = false, anydata Additional Values, GetIssueLimitReportQueries queries) returns IssueLimitReportResponseBean|error;
+    resource function get api/'3/issue/'limit/report(map<string|string[]> headers = {}, boolean isReturningKeys = false, GetIssueLimitReportQueries queries) returns IssueLimitReportResponseBean|error;
 
     # Get issue picker suggestions
     # 
-    resource function get api/'3/issue/picker(map<string|string[]> headers = {}, string currentProjectId = "", string query = "", string currentIssueKey = "", string currentJQL = "", boolean showSubTasks = false, boolean showSubTaskParent = false, anydata Additional Values, GetIssuePickerResourceQueries queries) returns IssuePickerSuggestions|error;
+    resource function get api/'3/issue/picker(map<string|string[]> headers = {}, string currentProjectId = "", string query = "", string currentIssueKey = "", string currentJQL = "", boolean showSubTasks = false, boolean showSubTaskParent = false, GetIssuePickerResourceQueries queries) returns IssuePickerSuggestions|error;
 
     # Bulk set issues properties by list
     # 
@@ -14979,15 +15079,15 @@
 
     # Get issue
     # 
-    resource function get api/'3/issue/[string issueIdOrKey](map<string|string[]> headers = {}, string expand = "", boolean fieldsByKeys = false, string[] fields = [], string[] properties = [], boolean updateHistory = false, boolean failFast = false, anydata Additional Values, GetIssueQueries queries) returns IssueBean|error;
+    resource function get api/'3/issue/[string issueIdOrKey](map<string|string[]> headers = {}, string expand = "", boolean fieldsByKeys = false, string[] fields = [], string[] properties = [], boolean updateHistory = false, boolean failFast = false, GetIssueQueries queries) returns IssueBean|error;
 
     # Edit issue
     # 
-    resource function put api/'3/issue/[string issueIdOrKey](IssueUpdateDetails payload, map<string|string[]> headers = {}, string expand = "", boolean overrideScreenSecurity = false, boolean overrideEditableFlag = false, boolean returnIssue = false, boolean notifyUsers = false, anydata Additional Values, EditIssueQueries queries) returns json|error;
+    resource function put api/'3/issue/[string issueIdOrKey](IssueUpdateDetails payload, map<string|string[]> headers = {}, string expand = "", boolean overrideScreenSecurity = false, boolean overrideEditableFlag = false, boolean returnIssue = false, boolean notifyUsers = false, EditIssueQueries queries) returns json|error;
 
     # Delete issue
     # 
-    resource function delete api/'3/issue/[string issueIdOrKey](map<string|string[]> headers = {}, "true"|"false" deleteSubtasks = "true", anydata Additional Values, DeleteIssueQueries queries) returns error?;
+    resource function delete api/'3/issue/[string issueIdOrKey](map<string|string[]> headers = {}, "true"|"false" deleteSubtasks = "true", DeleteIssueQueries queries) returns error?;
 
     # Assign issue
     # 
@@ -14999,7 +15099,7 @@
 
     # Get changelogs
     # 
-    resource function get api/'3/issue/[string issueIdOrKey]/changelog(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int:Signed32 startAt = 0, anydata Additional Values, GetChangeLogsQueries queries) returns PageBeanChangelog|error;
+    resource function get api/'3/issue/[string issueIdOrKey]/changelog(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int:Signed32 startAt = 0, GetChangeLogsQueries queries) returns PageBeanChangelog|error;
 
     # Get changelogs by IDs
     # 
@@ -15007,19 +15107,19 @@
 
     # Get comments
     # 
-    resource function get api/'3/issue/[string issueIdOrKey]/comment(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, "created"|"-created"|"+created" orderBy = "created", int startAt = 0, anydata Additional Values, GetCommentsQueries queries) returns PageOfComments|error;
+    resource function get api/'3/issue/[string issueIdOrKey]/comment(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, "created"|"-created"|"+created" orderBy = "created", int startAt = 0, GetCommentsQueries queries) returns PageOfComments|error;
 
     # Add comment
     # 
-    resource function post api/'3/issue/[string issueIdOrKey]/comment(Comment payload, map<string|string[]> headers = {}, string expand = "", anydata Additional Values, AddCommentQueries queries) returns Comment|error;
+    resource function post api/'3/issue/[string issueIdOrKey]/comment(Comment payload, map<string|string[]> headers = {}, string expand = "", AddCommentQueries queries) returns Comment|error;
 
     # Get comment
     # 
-    resource function get api/'3/issue/[string issueIdOrKey]/comment/[string id](map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetCommentQueries queries) returns Comment|error;
+    resource function get api/'3/issue/[string issueIdOrKey]/comment/[string id](map<string|string[]> headers = {}, string expand = "", GetCommentQueries queries) returns Comment|error;
 
     # Update comment
     # 
-    resource function put api/'3/issue/[string issueIdOrKey]/comment/[string id](Comment payload, map<string|string[]> headers = {}, string expand = "", boolean overrideEditableFlag = false, boolean notifyUsers = false, anydata Additional Values, UpdateCommentQueries queries) returns Comment|error;
+    resource function put api/'3/issue/[string issueIdOrKey]/comment/[string id](Comment payload, map<string|string[]> headers = {}, string expand = "", boolean overrideEditableFlag = false, boolean notifyUsers = false, UpdateCommentQueries queries) returns Comment|error;
 
     # Delete comment
     # 
@@ -15027,7 +15127,7 @@
 
     # Get edit issue metadata
     # 
-    resource function get api/'3/issue/[string issueIdOrKey]/editmeta(map<string|string[]> headers = {}, boolean overrideScreenSecurity = false, boolean overrideEditableFlag = false, anydata Additional Values, GetEditIssueMetaQueries queries) returns IssueUpdateMetadata|error;
+    resource function get api/'3/issue/[string issueIdOrKey]/editmeta(map<string|string[]> headers = {}, boolean overrideScreenSecurity = false, boolean overrideEditableFlag = false, GetEditIssueMetaQueries queries) returns IssueUpdateMetadata|error;
 
     # Send notification for issue
     # 
@@ -15051,7 +15151,7 @@
 
     # Get remote issue links
     # 
-    resource function get api/'3/issue/[string issueIdOrKey]/remotelink(map<string|string[]> headers = {}, string globalId = "", anydata Additional Values, GetRemoteIssueLinksQueries queries) returns RemoteIssueLink|error;
+    resource function get api/'3/issue/[string issueIdOrKey]/remotelink(map<string|string[]> headers = {}, string globalId = "", GetRemoteIssueLinksQueries queries) returns RemoteIssueLink|error;
 
     # Create or update remote issue link
     # 
@@ -15059,7 +15159,7 @@
 
     # Delete remote issue link by global ID
     # 
-    resource function delete api/'3/issue/[string issueIdOrKey]/remotelink(map<string|string[]> headers = {}, string globalId = "", anydata Additional Values, DeleteRemoteIssueLinkByGlobalIdQueries queries) returns error?;
+    resource function delete api/'3/issue/[string issueIdOrKey]/remotelink(map<string|string[]> headers = {}, string globalId = "", DeleteRemoteIssueLinkByGlobalIdQueries queries) returns error?;
 
     # Get remote issue link by ID
     # 
@@ -15075,7 +15175,7 @@
 
     # Get transitions
     # 
-    resource function get api/'3/issue/[string issueIdOrKey]/transitions(map<string|string[]> headers = {}, string expand = "", boolean skipRemoteOnlyCondition = false, string transitionId = "", boolean includeUnavailableTransitions = false, boolean sortByOpsBarAndStatus = false, anydata Additional Values, GetTransitionsQueries queries) returns Transitions|error;
+    resource function get api/'3/issue/[string issueIdOrKey]/transitions(map<string|string[]> headers = {}, string expand = "", boolean skipRemoteOnlyCondition = false, string transitionId = "", boolean includeUnavailableTransitions = false, boolean sortByOpsBarAndStatus = false, GetTransitionsQueries queries) returns Transitions|error;
 
     # Transition issue
     # 
@@ -15103,35 +15203,35 @@
 
     # Delete watcher
     # 
-    resource function delete api/'3/issue/[string issueIdOrKey]/watchers(map<string|string[]> headers = {}, string accountId = "", string username = "", anydata Additional Values, RemoveWatcherQueries queries) returns error?;
+    resource function delete api/'3/issue/[string issueIdOrKey]/watchers(map<string|string[]> headers = {}, string accountId = "", string username = "", RemoveWatcherQueries queries) returns error?;
 
     # Get issue worklogs
     # 
-    resource function get api/'3/issue/[string issueIdOrKey]/worklog(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, int startedAfter = 0, int startAt = 0, int startedBefore = 0, anydata Additional Values, GetIssueWorklogQueries queries) returns PageOfWorklogs|error;
+    resource function get api/'3/issue/[string issueIdOrKey]/worklog(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, int startedAfter = 0, int startAt = 0, int startedBefore = 0, GetIssueWorklogQueries queries) returns PageOfWorklogs|error;
 
     # Add worklog
     # 
-    resource function post api/'3/issue/[string issueIdOrKey]/worklog(Worklog payload, map<string|string[]> headers = {}, string newEstimate = "", "new"|"leave"|"manual"|"auto" adjustEstimate = "new", string reduceBy = "", string expand = "", boolean overrideEditableFlag = false, boolean notifyUsers = false, anydata Additional Values, AddWorklogQueries queries) returns Worklog|error;
+    resource function post api/'3/issue/[string issueIdOrKey]/worklog(Worklog payload, map<string|string[]> headers = {}, string newEstimate = "", "new"|"leave"|"manual"|"auto" adjustEstimate = "new", string reduceBy = "", string expand = "", boolean overrideEditableFlag = false, boolean notifyUsers = false, AddWorklogQueries queries) returns Worklog|error;
 
     # Bulk delete worklogs
     # 
-    resource function delete api/'3/issue/[string issueIdOrKey]/worklog(WorklogIdsRequestBean payload, map<string|string[]> headers = {}, "leave"|"auto" adjustEstimate = "leave", boolean overrideEditableFlag = false, anydata Additional Values, BulkDeleteWorklogsQueries queries) returns error?;
+    resource function delete api/'3/issue/[string issueIdOrKey]/worklog(WorklogIdsRequestBean payload, map<string|string[]> headers = {}, "leave"|"auto" adjustEstimate = "leave", boolean overrideEditableFlag = false, BulkDeleteWorklogsQueries queries) returns error?;
 
     # Bulk move worklogs
     # 
-    resource function post api/'3/issue/[string issueIdOrKey]/worklog/move(WorklogsMoveRequestBean payload, map<string|string[]> headers = {}, "leave"|"auto" adjustEstimate = "leave", boolean overrideEditableFlag = false, anydata Additional Values, BulkMoveWorklogsQueries queries) returns error?;
+    resource function post api/'3/issue/[string issueIdOrKey]/worklog/move(WorklogsMoveRequestBean payload, map<string|string[]> headers = {}, "leave"|"auto" adjustEstimate = "leave", boolean overrideEditableFlag = false, BulkMoveWorklogsQueries queries) returns error?;
 
     # Get worklog
     # 
-    resource function get api/'3/issue/[string issueIdOrKey]/worklog/[string id](map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetWorklogQueries queries) returns Worklog|error;
+    resource function get api/'3/issue/[string issueIdOrKey]/worklog/[string id](map<string|string[]> headers = {}, string expand = "", GetWorklogQueries queries) returns Worklog|error;
 
     # Update worklog
     # 
-    resource function put api/'3/issue/[string issueIdOrKey]/worklog/[string id](Worklog payload, map<string|string[]> headers = {}, string newEstimate = "", "new"|"leave"|"manual"|"auto" adjustEstimate = "new", string expand = "", boolean overrideEditableFlag = false, boolean notifyUsers = false, anydata Additional Values, UpdateWorklogQueries queries) returns Worklog|error;
+    resource function put api/'3/issue/[string issueIdOrKey]/worklog/[string id](Worklog payload, map<string|string[]> headers = {}, string newEstimate = "", "new"|"leave"|"manual"|"auto" adjustEstimate = "new", string expand = "", boolean overrideEditableFlag = false, boolean notifyUsers = false, UpdateWorklogQueries queries) returns Worklog|error;
 
     # Delete worklog
     # 
-    resource function delete api/'3/issue/[string issueIdOrKey]/worklog/[string id](map<string|string[]> headers = {}, string newEstimate = "", "new"|"leave"|"manual"|"auto" adjustEstimate = "new", boolean overrideEditableFlag = false, boolean notifyUsers = false, string increaseBy = "", anydata Additional Values, DeleteWorklogQueries queries) returns error?;
+    resource function delete api/'3/issue/[string issueIdOrKey]/worklog/[string id](map<string|string[]> headers = {}, string newEstimate = "", "new"|"leave"|"manual"|"auto" adjustEstimate = "new", boolean overrideEditableFlag = false, boolean notifyUsers = false, string increaseBy = "", DeleteWorklogQueries queries) returns error?;
 
     # Get worklog property keys
     # 
@@ -15195,7 +15295,7 @@
 
     # Get issue security levels
     # 
-    resource function get api/'3/issuesecurityschemes/level(map<string|string[]> headers = {}, boolean onlyDefault = false, string maxResults = "", string[] schemeId = [], string[] id = [], string startAt = "", anydata Additional Values, GetSecurityLevelsQueries queries) returns PageBeanSecurityLevel|error;
+    resource function get api/'3/issuesecurityschemes/level(map<string|string[]> headers = {}, boolean onlyDefault = false, string maxResults = "", string[] schemeId = [], string[] id = [], string startAt = "", GetSecurityLevelsQueries queries) returns PageBeanSecurityLevel|error;
 
     # Set default issue security levels
     # 
@@ -15203,11 +15303,11 @@
 
     # Get issue security level members
     # 
-    resource function get api/'3/issuesecurityschemes/level/member(map<string|string[]> headers = {}, string expand = "", string maxResults = "", string[] levelId = [], string[] schemeId = [], string[] id = [], string startAt = "", anydata Additional Values, GetSecurityLevelMembersQueries queries) returns PageBeanSecurityLevelMember|error;
+    resource function get api/'3/issuesecurityschemes/level/member(map<string|string[]> headers = {}, string expand = "", string maxResults = "", string[] levelId = [], string[] schemeId = [], string[] id = [], string startAt = "", GetSecurityLevelMembersQueries queries) returns PageBeanSecurityLevelMember|error;
 
     # Get projects using issue security schemes
     # 
-    resource function get api/'3/issuesecurityschemes/project(map<string|string[]> headers = {}, string[] issueSecuritySchemeId = [], string maxResults = "", string[] projectId = [], string startAt = "", anydata Additional Values, SearchProjectsUsingSecuritySchemesQueries queries) returns PageBeanIssueSecuritySchemeToProjectMapping|error;
+    resource function get api/'3/issuesecurityschemes/project(map<string|string[]> headers = {}, string[] issueSecuritySchemeId = [], string maxResults = "", string[] projectId = [], string startAt = "", SearchProjectsUsingSecuritySchemesQueries queries) returns PageBeanIssueSecuritySchemeToProjectMapping|error;
 
     # Associate security scheme to project
     # 
@@ -15215,7 +15315,7 @@
 
     # Search issue security schemes
     # 
-    resource function get api/'3/issuesecurityschemes/search(map<string|string[]> headers = {}, string maxResults = "", string[] id = [], string[] projectId = [], string startAt = "", anydata Additional Values, SearchSecuritySchemesQueries queries) returns PageBeanSecuritySchemeWithProjects|error;
+    resource function get api/'3/issuesecurityschemes/search(map<string|string[]> headers = {}, string maxResults = "", string[] id = [], string[] projectId = [], string startAt = "", SearchSecuritySchemesQueries queries) returns PageBeanSecuritySchemeWithProjects|error;
 
     # Get issue security scheme
     # 
@@ -15227,7 +15327,7 @@
 
     # Get issue security level members by issue security scheme
     # 
-    resource function get api/'3/issuesecurityschemes/[int issueSecuritySchemeId]/members(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, string[] issueSecurityLevelId = [], int startAt = 0, anydata Additional Values, GetIssueSecurityLevelMembersQueries queries) returns PageBeanIssueSecurityLevelMember|error;
+    resource function get api/'3/issuesecurityschemes/[int issueSecuritySchemeId]/members(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, string[] issueSecurityLevelId = [], int startAt = 0, GetIssueSecurityLevelMembersQueries queries) returns PageBeanIssueSecurityLevelMember|error;
 
     # Delete issue security scheme
     # 
@@ -15243,7 +15343,7 @@
 
     # Remove issue security level
     # 
-    resource function delete api/'3/issuesecurityschemes/[string schemeId]/level/[string levelId](map<string|string[]> headers = {}, string replaceWith = "", anydata Additional Values, RemoveLevelQueries queries) returns http:Response|error; // Special Agent Note: Response FROM ballerina/http package
+    resource function delete api/'3/issuesecurityschemes/[string schemeId]/level/[string levelId](map<string|string[]> headers = {}, string replaceWith = "", RemoveLevelQueries queries) returns http:Response|error; // Special Agent Note: Response FROM ballerina/http package
 
     # Add issue security level members
     # 
@@ -15263,7 +15363,7 @@
 
     # Get issue types for project
     # 
-    resource function get api/'3/issuetype/project(map<string|string[]> headers = {}, int:Signed32 level = 0, int projectId = 0, anydata Additional Values, GetIssueTypesForProjectQueries queries) returns IssueTypeDetails[]|error;
+    resource function get api/'3/issuetype/project(map<string|string[]> headers = {}, int:Signed32 level = 0, int projectId = 0, GetIssueTypesForProjectQueries queries) returns IssueTypeDetails[]|error;
 
     # Get issue type
     # 
@@ -15275,7 +15375,7 @@
 
     # Delete issue type
     # 
-    resource function delete api/'3/issuetype/[string id](map<string|string[]> headers = {}, string alternativeIssueTypeId = "", anydata Additional Values, DeleteIssueTypeQueries queries) returns error?;
+    resource function delete api/'3/issuetype/[string id](map<string|string[]> headers = {}, string alternativeIssueTypeId = "", DeleteIssueTypeQueries queries) returns error?;
 
     # Get alternative issue types
     # 
@@ -15283,7 +15383,7 @@
 
     # Load issue type avatar
     # 
-    resource function post api/'3/issuetype/[string id]/avatar2(http:Request request, map<string|string[]> headers = {}, int:Signed32 size = 0, int:Signed32 x = 0, int:Signed32 y = 0, anydata Additional Values, CreateIssueTypeAvatarQueries queries) returns Avatar|error; // Special Agent Note: Request FROM ballerina/http package
+    resource function post api/'3/issuetype/[string id]/avatar2(http:Request request, map<string|string[]> headers = {}, int:Signed32 size = 0, int:Signed32 x = 0, int:Signed32 y = 0, CreateIssueTypeAvatarQueries queries) returns Avatar|error; // Special Agent Note: Request FROM ballerina/http package
 
     # Get issue type property keys
     # 
@@ -15303,7 +15403,7 @@
 
     # Get all issue type schemes
     # 
-    resource function get api/'3/issuetypescheme(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, "name"|"-name"|"+name"|"id"|"-id"|"+id" orderBy = "name", int[] id = [], string queryString = "", int startAt = 0, anydata Additional Values, GetAllIssueTypeSchemesQueries queries) returns PageBeanIssueTypeScheme|error;
+    resource function get api/'3/issuetypescheme(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, "name"|"-name"|"+name"|"id"|"-id"|"+id" orderBy = "name", int[] id = [], string queryString = "", int startAt = 0, GetAllIssueTypeSchemesQueries queries) returns PageBeanIssueTypeScheme|error;
 
     # Create issue type scheme
     # 
@@ -15311,11 +15411,11 @@
 
     # Get issue type scheme items
     # 
-    resource function get api/'3/issuetypescheme/mapping(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] issueTypeSchemeId = [], int startAt = 0, anydata Additional Values, GetIssueTypeSchemesMappingQueries queries) returns PageBeanIssueTypeSchemeMapping|error;
+    resource function get api/'3/issuetypescheme/mapping(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] issueTypeSchemeId = [], int startAt = 0, GetIssueTypeSchemesMappingQueries queries) returns PageBeanIssueTypeSchemeMapping|error;
 
     # Get issue type schemes for projects
     # 
-    resource function get api/'3/issuetypescheme/project(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] projectId = [], int startAt = 0, anydata Additional Values, GetIssueTypeSchemeForProjectsQueries queries) returns PageBeanIssueTypeSchemeProjects|error;
+    resource function get api/'3/issuetypescheme/project(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] projectId = [], int startAt = 0, GetIssueTypeSchemeForProjectsQueries queries) returns PageBeanIssueTypeSchemeProjects|error;
 
     # Assign issue type scheme to project
     # 
@@ -15343,7 +15443,7 @@
 
     # Get issue type screen schemes
     # 
-    resource function get api/'3/issuetypescreenscheme(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, "name"|"-name"|"+name"|"id"|"-id"|"+id" orderBy = "name", int[] id = [], string queryString = "", int startAt = 0, anydata Additional Values, GetIssueTypeScreenSchemesQueries queries) returns PageBeanIssueTypeScreenScheme|error;
+    resource function get api/'3/issuetypescreenscheme(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, "name"|"-name"|"+name"|"id"|"-id"|"+id" orderBy = "name", int[] id = [], string queryString = "", int startAt = 0, GetIssueTypeScreenSchemesQueries queries) returns PageBeanIssueTypeScreenScheme|error;
 
     # Create issue type screen scheme
     # 
@@ -15351,11 +15451,11 @@
 
     # Get issue type screen scheme items
     # 
-    resource function get api/'3/issuetypescreenscheme/mapping(map<string|string[]> headers = {}, int[] issueTypeScreenSchemeId = [], int:Signed32 maxResults = 0, int startAt = 0, anydata Additional Values, GetIssueTypeScreenSchemeMappingsQueries queries) returns PageBeanIssueTypeScreenSchemeItem|error;
+    resource function get api/'3/issuetypescreenscheme/mapping(map<string|string[]> headers = {}, int[] issueTypeScreenSchemeId = [], int:Signed32 maxResults = 0, int startAt = 0, GetIssueTypeScreenSchemeMappingsQueries queries) returns PageBeanIssueTypeScreenSchemeItem|error;
 
     # Get issue type screen schemes for projects
     # 
-    resource function get api/'3/issuetypescreenscheme/project(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] projectId = [], int startAt = 0, anydata Additional Values, GetIssueTypeScreenSchemeProjectAssociationsQueries queries) returns PageBeanIssueTypeScreenSchemesProjects|error;
+    resource function get api/'3/issuetypescreenscheme/project(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int[] projectId = [], int startAt = 0, GetIssueTypeScreenSchemeProjectAssociationsQueries queries) returns PageBeanIssueTypeScreenSchemesProjects|error;
 
     # Assign issue type screen scheme to project
     # 
@@ -15383,7 +15483,7 @@
 
     # Get issue type screen scheme projects
     # 
-    resource function get api/'3/issuetypescreenscheme/[int issueTypeScreenSchemeId]/project(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, string query = "", int startAt = 0, anydata Additional Values, GetProjectsForIssueTypeScreenSchemeQueries queries) returns PageBeanProjectDetails|error;
+    resource function get api/'3/issuetypescreenscheme/[int issueTypeScreenSchemeId]/project(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, string query = "", int startAt = 0, GetProjectsForIssueTypeScreenSchemeQueries queries) returns PageBeanProjectDetails|error;
 
     # Get field reference data (GET)
     # 
@@ -15395,19 +15495,19 @@
 
     # Get field auto complete suggestions
     # 
-    resource function get api/'3/jql/autocompletedata/suggestions(map<string|string[]> headers = {}, string predicateValue = "", string fieldName = "", string predicateName = "", string fieldValue = "", anydata Additional Values, GetFieldAutoCompleteForQueryStringQueries queries) returns AutoCompleteSuggestions|error;
+    resource function get api/'3/jql/autocompletedata/suggestions(map<string|string[]> headers = {}, string predicateValue = "", string fieldName = "", string predicateName = "", string fieldValue = "", GetFieldAutoCompleteForQueryStringQueries queries) returns AutoCompleteSuggestions|error;
 
     # Get precomputations (apps)
     # 
-    resource function get api/'3/jql/'function/computation(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, string orderBy = "", string[] functionKey = [], int startAt = 0, anydata Additional Values, GetPrecomputationsQueries queries) returns PageBean2JqlFunctionPrecomputationBean|error;
+    resource function get api/'3/jql/'function/computation(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, string orderBy = "", string[] functionKey = [], int startAt = 0, GetPrecomputationsQueries queries) returns PageBean2JqlFunctionPrecomputationBean|error;
 
     # Update precomputations (apps)
     # 
-    resource function post api/'3/jql/'function/computation(JqlFunctionPrecomputationUpdateRequestBean payload, map<string|string[]> headers = {}, boolean skipNotFoundPrecomputations = false, anydata Additional Values, UpdatePrecomputationsQueries queries) returns JqlFunctionPrecomputationUpdateResponse|json|error;
+    resource function post api/'3/jql/'function/computation(JqlFunctionPrecomputationUpdateRequestBean payload, map<string|string[]> headers = {}, boolean skipNotFoundPrecomputations = false, UpdatePrecomputationsQueries queries) returns JqlFunctionPrecomputationUpdateResponse|json|error;
 
     # Get precomputations by ID (apps)
     # 
-    resource function post api/'3/jql/'function/computation/search(JqlFunctionPrecomputationGetByIdRequest payload, map<string|string[]> headers = {}, string orderBy = "", anydata Additional Values, GetPrecomputationsByIDQueries queries) returns JqlFunctionPrecomputationGetByIdResponse|error;
+    resource function post api/'3/jql/'function/computation/search(JqlFunctionPrecomputationGetByIdRequest payload, map<string|string[]> headers = {}, string orderBy = "", GetPrecomputationsByIDQueries queries) returns JqlFunctionPrecomputationGetByIdResponse|error;
 
     # Check issues against JQL
     # 
@@ -15415,7 +15515,7 @@
 
     # Parse JQL query
     # 
-    resource function post api/'3/jql/parse(JqlQueriesToParse payload, map<string|string[]> headers = {}, "strict"|"warn"|"none" validation = "strict", anydata Additional Values, ParseJqlQueriesQueries queries) returns ParsedJqlQueries|error;
+    resource function post api/'3/jql/parse(JqlQueriesToParse payload, map<string|string[]> headers = {}, "strict"|"warn"|"none" validation = "strict", ParseJqlQueriesQueries queries) returns ParsedJqlQueries|error;
 
     # Convert user identifiers to account IDs in JQL queries
     # 
@@ -15427,7 +15527,7 @@
 
     # Get all labels
     # 
-    resource function get api/'3/label(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, anydata Additional Values, GetAllLabelsQueries queries) returns PageBeanString|error;
+    resource function get api/'3/label(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, GetAllLabelsQueries queries) returns PageBeanString|error;
 
     # Get approximate license count
     # 
@@ -15439,19 +15539,19 @@
 
     # Get my permissions
     # 
-    resource function get api/'3/mypermissions(map<string|string[]> headers = {}, string projectKey = "", string issueId = "", string issueKey = "", string permissions = "", string projectConfigurationUuid = "", string commentId = "", string projectId = "", string projectUuid = "", anydata Additional Values, GetMyPermissionsQueries queries) returns Permissions|error;
+    resource function get api/'3/mypermissions(map<string|string[]> headers = {}, string projectKey = "", string issueId = "", string issueKey = "", string permissions = "", string projectConfigurationUuid = "", string commentId = "", string projectId = "", string projectUuid = "", GetMyPermissionsQueries queries) returns Permissions|error;
 
     # Get preference
     # 
-    resource function get api/'3/mypreferences(map<string|string[]> headers = {}, string key = "", anydata Additional Values, GetPreferenceQueries queries) returns string|error;
+    resource function get api/'3/mypreferences(map<string|string[]> headers = {}, string key = "", GetPreferenceQueries queries) returns string|error;
 
     # Set preference
     # 
-    resource function put api/'3/mypreferences(string payload, map<string|string[]> headers = {}, string key = "", anydata Additional Values, SetPreferenceQueries queries) returns json|error;
+    resource function put api/'3/mypreferences(string payload, map<string|string[]> headers = {}, string key = "", SetPreferenceQueries queries) returns json|error;
 
     # Delete preference
     # 
-    resource function delete api/'3/mypreferences(map<string|string[]> headers = {}, string key = "", anydata Additional Values, RemovePreferenceQueries queries) returns error?;
+    resource function delete api/'3/mypreferences(map<string|string[]> headers = {}, string key = "", RemovePreferenceQueries queries) returns error?;
 
     # Get locale
     # 
@@ -15463,11 +15563,11 @@
 
     # Get current user
     # 
-    resource function get api/'3/myself(map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetCurrentUserQueries queries) returns User|error;
+    resource function get api/'3/myself(map<string|string[]> headers = {}, string expand = "", GetCurrentUserQueries queries) returns User|error;
 
     # Get notification schemes paginated
     # 
-    resource function get api/'3/notificationscheme(map<string|string[]> headers = {}, string expand = "", boolean onlyDefault = false, string maxResults = "", string[] id = [], string[] projectId = [], string startAt = "", anydata Additional Values, GetNotificationSchemesQueries queries) returns PageBeanNotificationScheme|error;
+    resource function get api/'3/notificationscheme(map<string|string[]> headers = {}, string expand = "", boolean onlyDefault = false, string maxResults = "", string[] id = [], string[] projectId = [], string startAt = "", GetNotificationSchemesQueries queries) returns PageBeanNotificationScheme|error;
 
     # Create notification scheme
     # 
@@ -15475,11 +15575,11 @@
 
     # Get projects using notification schemes paginated
     # 
-    resource function get api/'3/notificationscheme/project(map<string|string[]> headers = {}, string[] notificationSchemeId = [], string maxResults = "", string[] projectId = [], string startAt = "", anydata Additional Values, GetNotificationSchemeToProjectMappingsQueries queries) returns PageBeanNotificationSchemeAndProjectMappingJsonBean|error;
+    resource function get api/'3/notificationscheme/project(map<string|string[]> headers = {}, string[] notificationSchemeId = [], string maxResults = "", string[] projectId = [], string startAt = "", GetNotificationSchemeToProjectMappingsQueries queries) returns PageBeanNotificationSchemeAndProjectMappingJsonBean|error;
 
     # Get notification scheme
     # 
-    resource function get api/'3/notificationscheme/[int id](map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetNotificationSchemeQueries queries) returns NotificationScheme|error;
+    resource function get api/'3/notificationscheme/[int id](map<string|string[]> headers = {}, string expand = "", GetNotificationSchemeQueries queries) returns NotificationScheme|error;
 
     # Update notification scheme
     # 
@@ -15511,19 +15611,19 @@
 
     # Get all permission schemes
     # 
-    resource function get api/'3/permissionscheme(map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetAllPermissionSchemesQueries queries) returns PermissionSchemes|error;
+    resource function get api/'3/permissionscheme(map<string|string[]> headers = {}, string expand = "", GetAllPermissionSchemesQueries queries) returns PermissionSchemes|error;
 
     # Create permission scheme
     # 
-    resource function post api/'3/permissionscheme(PermissionScheme payload, map<string|string[]> headers = {}, string expand = "", anydata Additional Values, CreatePermissionSchemeQueries queries) returns PermissionScheme|error;
+    resource function post api/'3/permissionscheme(PermissionScheme payload, map<string|string[]> headers = {}, string expand = "", CreatePermissionSchemeQueries queries) returns PermissionScheme|error;
 
     # Get permission scheme
     # 
-    resource function get api/'3/permissionscheme/[int schemeId](map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetPermissionSchemeQueries queries) returns PermissionScheme|error;
+    resource function get api/'3/permissionscheme/[int schemeId](map<string|string[]> headers = {}, string expand = "", GetPermissionSchemeQueries queries) returns PermissionScheme|error;
 
     # Update permission scheme
     # 
-    resource function put api/'3/permissionscheme/[int schemeId](PermissionScheme payload, map<string|string[]> headers = {}, string expand = "", anydata Additional Values, UpdatePermissionSchemeQueries queries) returns PermissionScheme|error;
+    resource function put api/'3/permissionscheme/[int schemeId](PermissionScheme payload, map<string|string[]> headers = {}, string expand = "", UpdatePermissionSchemeQueries queries) returns PermissionScheme|error;
 
     # Delete permission scheme
     # 
@@ -15531,15 +15631,15 @@
 
     # Get permission scheme grants
     # 
-    resource function get api/'3/permissionscheme/[int schemeId]/permission(map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetPermissionSchemeGrantsQueries queries) returns PermissionGrants|error;
+    resource function get api/'3/permissionscheme/[int schemeId]/permission(map<string|string[]> headers = {}, string expand = "", GetPermissionSchemeGrantsQueries queries) returns PermissionGrants|error;
 
     # Create permission grant
     # 
-    resource function post api/'3/permissionscheme/[int schemeId]/permission(PermissionGrant payload, map<string|string[]> headers = {}, string expand = "", anydata Additional Values, CreatePermissionGrantQueries queries) returns PermissionGrant|error;
+    resource function post api/'3/permissionscheme/[int schemeId]/permission(PermissionGrant payload, map<string|string[]> headers = {}, string expand = "", CreatePermissionGrantQueries queries) returns PermissionGrant|error;
 
     # Get permission scheme grant
     # 
-    resource function get api/'3/permissionscheme/[int schemeId]/permission/[int permissionId](map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetPermissionSchemeGrantQueries queries) returns PermissionGrant|error;
+    resource function get api/'3/permissionscheme/[int schemeId]/permission/[int permissionId](map<string|string[]> headers = {}, string expand = "", GetPermissionSchemeGrantQueries queries) returns PermissionGrant|error;
 
     # Delete permission scheme grant
     # 
@@ -15547,19 +15647,19 @@
 
     # Get plans paginated
     # 
-    resource function get api/'3/plans/plan(map<string|string[]> headers = {}, string cursor = "", boolean includeArchived = false, int:Signed32 maxResults = 0, boolean includeTrashed = false, anydata Additional Values, GetPlansQueries queries) returns PageWithCursorGetPlanResponseForPage|error;
+    resource function get api/'3/plans/plan(map<string|string[]> headers = {}, string cursor = "", boolean includeArchived = false, int:Signed32 maxResults = 0, boolean includeTrashed = false, GetPlansQueries queries) returns PageWithCursorGetPlanResponseForPage|error;
 
     # Create plan
     # 
-    resource function post api/'3/plans/plan(CreatePlanRequest payload, map<string|string[]> headers = {}, boolean useGroupId = false, anydata Additional Values, CreatePlanQueries queries) returns int|error;
+    resource function post api/'3/plans/plan(CreatePlanRequest payload, map<string|string[]> headers = {}, boolean useGroupId = false, CreatePlanQueries queries) returns int|error;
 
     # Get plan
     # 
-    resource function get api/'3/plans/plan/[int planId](map<string|string[]> headers = {}, boolean useGroupId = false, anydata Additional Values, GetPlanQueries queries) returns GetPlanResponse|error;
+    resource function get api/'3/plans/plan/[int planId](map<string|string[]> headers = {}, boolean useGroupId = false, GetPlanQueries queries) returns GetPlanResponse|error;
 
     # Update plan
     # 
-    resource function put api/'3/plans/plan/[int planId](record {|anydata...;|} payload, map<string|string[]> headers = {}, boolean useGroupId = false, anydata Additional Values, UpdatePlanQueries queries) returns json|error;
+    resource function put api/'3/plans/plan/[int planId](record {|anydata...;|} payload, map<string|string[]> headers = {}, boolean useGroupId = false, UpdatePlanQueries queries) returns json|error;
 
     # Archive plan
     # 
@@ -15571,7 +15671,7 @@
 
     # Get teams in plan paginated
     # 
-    resource function get api/'3/plans/plan/[int planId]/team(map<string|string[]> headers = {}, string cursor = "", int:Signed32 maxResults = 0, anydata Additional Values, GetTeamsQueries queries) returns PageWithCursorGetTeamResponseForPage|error;
+    resource function get api/'3/plans/plan/[int planId]/team(map<string|string[]> headers = {}, string cursor = "", int:Signed32 maxResults = 0, GetTeamsQueries queries) returns PageWithCursorGetTeamResponseForPage|error;
 
     # Add Atlassian team to plan
     # 
@@ -15627,7 +15727,7 @@
 
     # Search priorities
     # 
-    resource function get api/'3/priority/search(map<string|string[]> headers = {}, string priorityName = "", string expand = "", boolean onlyDefault = false, string maxResults = "", string[] id = [], string[] projectId = [], string startAt = "", anydata Additional Values, SearchPrioritiesQueries queries) returns PageBeanPriority|error;
+    resource function get api/'3/priority/search(map<string|string[]> headers = {}, string priorityName = "", string expand = "", boolean onlyDefault = false, string maxResults = "", string[] id = [], string[] projectId = [], string startAt = "", SearchPrioritiesQueries queries) returns PageBeanPriority|error;
 
     # Get priority
     # 
@@ -15643,7 +15743,7 @@
 
     # Get priority schemes
     # 
-    resource function get api/'3/priorityscheme(map<string|string[]> headers = {}, string expand = "", boolean onlyDefault = false, string maxResults = "", string schemeName = "", "name"|"+name"|"-name" orderBy = "name", int[] schemeId = [], string startAt = "", int[] priorityId = [], anydata Additional Values, GetPrioritySchemesQueries queries) returns PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects|error;
+    resource function get api/'3/priorityscheme(map<string|string[]> headers = {}, string expand = "", boolean onlyDefault = false, string maxResults = "", string schemeName = "", "name"|"+name"|"-name" orderBy = "name", int[] schemeId = [], string startAt = "", int[] priorityId = [], GetPrioritySchemesQueries queries) returns PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects|error;
 
     # Create priority scheme
     # 
@@ -15655,7 +15755,7 @@
 
     # Get available priorities by priority scheme
     # 
-    resource function get api/'3/priorityscheme/priorities/available(map<string|string[]> headers = {}, string maxResults = "", string query = "", string schemeId = "", string[] exclude = [], string startAt = "", anydata Additional Values, GetAvailablePrioritiesByPrioritySchemeQueries queries) returns PageBeanPriorityWithSequence|error;
+    resource function get api/'3/priorityscheme/priorities/available(map<string|string[]> headers = {}, string maxResults = "", string query = "", string schemeId = "", string[] exclude = [], string startAt = "", GetAvailablePrioritiesByPrioritySchemeQueries queries) returns PageBeanPriorityWithSequence|error;
 
     # Update priority scheme
     # 
@@ -15667,15 +15767,15 @@
 
     # Get priorities by priority scheme
     # 
-    resource function get api/'3/priorityscheme/[string schemeId]/priorities(map<string|string[]> headers = {}, string maxResults = "", string startAt = "", anydata Additional Values, GetPrioritiesByPrioritySchemeQueries queries) returns PageBeanPriorityWithSequence|error;
+    resource function get api/'3/priorityscheme/[string schemeId]/priorities(map<string|string[]> headers = {}, string maxResults = "", string startAt = "", GetPrioritiesByPrioritySchemeQueries queries) returns PageBeanPriorityWithSequence|error;
 
     # Get projects by priority scheme
     # 
-    resource function get api/'3/priorityscheme/[string schemeId]/projects(map<string|string[]> headers = {}, string maxResults = "", string query = "", int[] projectId = [], string startAt = "", anydata Additional Values, GetProjectsByPrioritySchemeQueries queries) returns PageBeanProject|error;
+    resource function get api/'3/priorityscheme/[string schemeId]/projects(map<string|string[]> headers = {}, string maxResults = "", string query = "", int[] projectId = [], string startAt = "", GetProjectsByPrioritySchemeQueries queries) returns PageBeanProject|error;
 
     # Get all projects
     # 
-    resource function get api/'3/project(map<string|string[]> headers = {}, string expand = "", int:Signed32 recent = 0, string[] properties = [], anydata Additional Values, GetAllProjectsQueries queries) returns Project[]|error;
+    resource function get api/'3/project(map<string|string[]> headers = {}, string expand = "", int:Signed32 recent = 0, string[] properties = [], GetAllProjectsQueries queries) returns Project[]|error;
 
     # Create project
     # 
@@ -15687,11 +15787,11 @@
 
     # Get recent projects
     # 
-    resource function get api/'3/project/recent(map<string|string[]> headers = {}, string expand = "", StringList[] properties = [], anydata Additional Values, GetRecentQueries queries) returns Project[]|error;
+    resource function get api/'3/project/recent(map<string|string[]> headers = {}, string expand = "", StringList[] properties = [], GetRecentQueries queries) returns Project[]|error;
 
     # Get projects paginated
     # 
-    resource function get api/'3/project/search(map<string|string[]> headers = {}, string typeKey = "", string[] keys = [], string query = "", "category"|"-category"|"+category"|"key"|"-key"|"+key"|"name"|"-name"|"+name"|"owner"|"-owner"|"+owner"|"issueCount"|"-issueCount"|"+issueCount"|"lastIssueUpdatedDate"|"-lastIssueUpdatedDate"|"+lastIssueUpdatedDate"|"archivedDate"|"+archivedDate"|"-archivedDate"|"deletedDate"|"+deletedDate"|"-deletedDate" orderBy = "category", string propertyQuery = "", string expand = "", int:Signed32 maxResults = 0, "view"|"browse"|"edit"|"create" action = "view", int[] id = [], int startAt = 0, int categoryId = 0, StringList[] properties = [], ("live"|"archived"|"deleted")[] status = [], anydata Additional Values, SearchProjectsQueries queries) returns PageBeanProject|error;
+    resource function get api/'3/project/search(map<string|string[]> headers = {}, string typeKey = "", string[] keys = [], string query = "", "category"|"-category"|"+category"|"key"|"-key"|"+key"|"name"|"-name"|"+name"|"owner"|"-owner"|"+owner"|"issueCount"|"-issueCount"|"+issueCount"|"lastIssueUpdatedDate"|"-lastIssueUpdatedDate"|"+lastIssueUpdatedDate"|"archivedDate"|"+archivedDate"|"-archivedDate"|"deletedDate"|"+deletedDate"|"-deletedDate" orderBy = "category", string propertyQuery = "", string expand = "", int:Signed32 maxResults = 0, "view"|"browse"|"edit"|"create" action = "view", int[] id = [], int startAt = 0, int categoryId = 0, StringList[] properties = [], ("live"|"archived"|"deleted")[] status = [], SearchProjectsQueries queries) returns PageBeanProject|error;
 
     # Get all project types
     # 
@@ -15711,15 +15811,15 @@
 
     # Get project
     # 
-    resource function get api/'3/project/[string projectIdOrKey](map<string|string[]> headers = {}, string expand = "", string[] properties = [], anydata Additional Values, GetProjectQueries queries) returns Project|error;
+    resource function get api/'3/project/[string projectIdOrKey](map<string|string[]> headers = {}, string expand = "", string[] properties = [], GetProjectQueries queries) returns Project|error;
 
     # Update project
     # 
-    resource function put api/'3/project/[string projectIdOrKey](UpdateProjectDetails payload, map<string|string[]> headers = {}, string expand = "", anydata Additional Values, UpdateProjectQueries queries) returns Project|error;
+    resource function put api/'3/project/[string projectIdOrKey](UpdateProjectDetails payload, map<string|string[]> headers = {}, string expand = "", UpdateProjectQueries queries) returns Project|error;
 
     # Delete project
     # 
-    resource function delete api/'3/project/[string projectIdOrKey](map<string|string[]> headers = {}, boolean enableUndo = false, anydata Additional Values, DeleteProjectQueries queries) returns error?;
+    resource function delete api/'3/project/[string projectIdOrKey](map<string|string[]> headers = {}, boolean enableUndo = false, DeleteProjectQueries queries) returns error?;
 
     # Archive project
     # 
@@ -15735,7 +15835,7 @@
 
     # Load project avatar
     # 
-    resource function post api/'3/project/[string projectIdOrKey]/avatar2(http:Request request, map<string|string[]> headers = {}, int:Signed32 size = 0, int:Signed32 x = 0, int:Signed32 y = 0, anydata Additional Values, CreateProjectAvatarQueries queries) returns Avatar|error; // Special Agent Note: Request FROM ballerina/http package
+    resource function post api/'3/project/[string projectIdOrKey]/avatar2(http:Request request, map<string|string[]> headers = {}, int:Signed32 size = 0, int:Signed32 x = 0, int:Signed32 y = 0, CreateProjectAvatarQueries queries) returns Avatar|error; // Special Agent Note: Request FROM ballerina/http package
 
     # Get all project avatars
     # 
@@ -15755,11 +15855,11 @@
 
     # Get project components paginated
     # 
-    resource function get api/'3/project/[string projectIdOrKey]/component(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, string query = "", "description"|"-description"|"+description"|"issueCount"|"-issueCount"|"+issueCount"|"lead"|"-lead"|"+lead"|"name"|"-name"|"+name" orderBy = "description", int startAt = 0, "jira"|"compass"|"auto" componentSource = "jira", anydata Additional Values, GetProjectComponentsPaginatedQueries queries) returns PageBeanComponentWithIssueCount|error;
+    resource function get api/'3/project/[string projectIdOrKey]/component(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, string query = "", "description"|"-description"|"+description"|"issueCount"|"-issueCount"|"+issueCount"|"lead"|"-lead"|"+lead"|"name"|"-name"|"+name" orderBy = "description", int startAt = 0, "jira"|"compass"|"auto" componentSource = "jira", GetProjectComponentsPaginatedQueries queries) returns PageBeanComponentWithIssueCount|error;
 
     # Get project components
     # 
-    resource function get api/'3/project/[string projectIdOrKey]/components(map<string|string[]> headers = {}, "jira"|"compass"|"auto" componentSource = "jira", anydata Additional Values, GetProjectComponentsQueries queries) returns ProjectComponent[]|error;
+    resource function get api/'3/project/[string projectIdOrKey]/components(map<string|string[]> headers = {}, "jira"|"compass"|"auto" componentSource = "jira", GetProjectComponentsQueries queries) returns ProjectComponent[]|error;
 
     # Delete project asynchronously
     # 
@@ -15797,7 +15897,7 @@
 
     # Get project role for project
     # 
-    resource function get api/'3/project/[string projectIdOrKey]/role/[int id](map<string|string[]> headers = {}, boolean excludeInactiveUsers = false, anydata Additional Values, GetProjectRoleQueries queries) returns ProjectRole|error;
+    resource function get api/'3/project/[string projectIdOrKey]/role/[int id](map<string|string[]> headers = {}, boolean excludeInactiveUsers = false, GetProjectRoleQueries queries) returns ProjectRole|error;
 
     # Set actors for project role
     # 
@@ -15809,11 +15909,11 @@
 
     # Delete actors from project role
     # 
-    resource function delete api/'3/project/[string projectIdOrKey]/role/[int id](map<string|string[]> headers = {}, string groupId = "", string user = "", string group = "", anydata Additional Values, DeleteActorQueries queries) returns error?;
+    resource function delete api/'3/project/[string projectIdOrKey]/role/[int id](map<string|string[]> headers = {}, string groupId = "", string user = "", string group = "", DeleteActorQueries queries) returns error?;
 
     # Get project role details
     # 
-    resource function get api/'3/project/[string projectIdOrKey]/roledetails(map<string|string[]> headers = {}, boolean currentMember = false, boolean excludeConnectAddons = false, anydata Additional Values, GetProjectRoleDetailsQueries queries) returns ProjectRoleDetails[]|error;
+    resource function get api/'3/project/[string projectIdOrKey]/roledetails(map<string|string[]> headers = {}, boolean currentMember = false, boolean excludeConnectAddons = false, GetProjectRoleDetailsQueries queries) returns ProjectRoleDetails[]|error;
 
     # Get all statuses for project
     # 
@@ -15821,11 +15921,11 @@
 
     # Get project versions paginated
     # 
-    resource function get api/'3/project/[string projectIdOrKey]/version(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, string query = "", "description"|"-description"|"+description"|"name"|"-name"|"+name"|"releaseDate"|"-releaseDate"|"+releaseDate"|"sequence"|"-sequence"|"+sequence"|"startDate"|"-startDate"|"+startDate" orderBy = "description", int startAt = 0, string status = "", anydata Additional Values, GetProjectVersionsPaginatedQueries queries) returns PageBeanVersion|error;
+    resource function get api/'3/project/[string projectIdOrKey]/version(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, string query = "", "description"|"-description"|"+description"|"name"|"-name"|"+name"|"releaseDate"|"-releaseDate"|"+releaseDate"|"sequence"|"-sequence"|"+sequence"|"startDate"|"-startDate"|"+startDate" orderBy = "description", int startAt = 0, string status = "", GetProjectVersionsPaginatedQueries queries) returns PageBeanVersion|error;
 
     # Get project versions
     # 
-    resource function get api/'3/project/[string projectIdOrKey]/versions(map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetProjectVersionsQueries queries) returns Version[]|error;
+    resource function get api/'3/project/[string projectIdOrKey]/versions(map<string|string[]> headers = {}, string expand = "", GetProjectVersionsQueries queries) returns Version[]|error;
 
     # Get project's sender email
     # 
@@ -15845,15 +15945,15 @@
 
     # Get project notification scheme
     # 
-    resource function get api/'3/project/[string projectKeyOrId]/notificationscheme(map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetNotificationSchemeForProjectQueries queries) returns NotificationScheme|error;
+    resource function get api/'3/project/[string projectKeyOrId]/notificationscheme(map<string|string[]> headers = {}, string expand = "", GetNotificationSchemeForProjectQueries queries) returns NotificationScheme|error;
 
     # Get assigned permission scheme
     # 
-    resource function get api/'3/project/[string projectKeyOrId]/permissionscheme(map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetAssignedPermissionSchemeQueries queries) returns PermissionScheme|error;
+    resource function get api/'3/project/[string projectKeyOrId]/permissionscheme(map<string|string[]> headers = {}, string expand = "", GetAssignedPermissionSchemeQueries queries) returns PermissionScheme|error;
 
     # Assign permission scheme
     # 
-    resource function put api/'3/project/[string projectKeyOrId]/permissionscheme(IdBean payload, map<string|string[]> headers = {}, string expand = "", anydata Additional Values, AssignPermissionSchemeQueries queries) returns PermissionScheme|error;
+    resource function put api/'3/project/[string projectKeyOrId]/permissionscheme(IdBean payload, map<string|string[]> headers = {}, string expand = "", AssignPermissionSchemeQueries queries) returns PermissionScheme|error;
 
     # Get project issue security levels
     # 
@@ -15881,15 +15981,15 @@
 
     # Validate project key
     # 
-    resource function get api/'3/projectvalidate/'key(map<string|string[]> headers = {}, string key = "", anydata Additional Values, ValidateProjectKeyQueries queries) returns ErrorCollection|error;
+    resource function get api/'3/projectvalidate/'key(map<string|string[]> headers = {}, string key = "", ValidateProjectKeyQueries queries) returns ErrorCollection|error;
 
     # Get valid project key
     # 
-    resource function get api/'3/projectvalidate/validProjectKey(map<string|string[]> headers = {}, string key = "", anydata Additional Values, GetValidProjectKeyQueries queries) returns string|error;
+    resource function get api/'3/projectvalidate/validProjectKey(map<string|string[]> headers = {}, string key = "", GetValidProjectKeyQueries queries) returns string|error;
 
     # Get valid project name
     # 
-    resource function get api/'3/projectvalidate/validProjectName(map<string|string[]> headers = {}, string name = "", anydata Additional Values, GetValidProjectNameQueries queries) returns string|error;
+    resource function get api/'3/projectvalidate/validProjectName(map<string|string[]> headers = {}, string name = "", GetValidProjectNameQueries queries) returns string|error;
 
     # Redact
     # 
@@ -15917,7 +16017,7 @@
 
     # Search resolutions
     # 
-    resource function get api/'3/resolution/search(map<string|string[]> headers = {}, boolean onlyDefault = false, string maxResults = "", string[] id = [], string startAt = "", anydata Additional Values, SearchResolutionsQueries queries) returns PageBeanResolutionJsonBean|error;
+    resource function get api/'3/resolution/search(map<string|string[]> headers = {}, boolean onlyDefault = false, string maxResults = "", string[] id = [], string startAt = "", SearchResolutionsQueries queries) returns PageBeanResolutionJsonBean|error;
 
     # Get resolution
     # 
@@ -15929,7 +16029,7 @@
 
     # Delete resolution
     # 
-    resource function delete api/'3/resolution/[string id](map<string|string[]> headers = {}, string replaceWith = "", anydata Additional Values, DeleteResolutionQueries queries) returns http:Response|error; // Special Agent Note: Response FROM ballerina/http package
+    resource function delete api/'3/resolution/[string id](map<string|string[]> headers = {}, string replaceWith = "", DeleteResolutionQueries queries) returns http:Response|error; // Special Agent Note: Response FROM ballerina/http package
 
     # Get all project roles
     # 
@@ -15953,7 +16053,7 @@
 
     # Delete project role
     # 
-    resource function delete api/'3/role/[int id](map<string|string[]> headers = {}, int swap = 0, anydata Additional Values, DeleteProjectRoleQueries queries) returns error?;
+    resource function delete api/'3/role/[int id](map<string|string[]> headers = {}, int swap = 0, DeleteProjectRoleQueries queries) returns error?;
 
     # Get default actors for project role
     # 
@@ -15965,11 +16065,11 @@
 
     # Delete default actors from project role
     # 
-    resource function delete api/'3/role/[int id]/actors(map<string|string[]> headers = {}, string groupId = "", string user = "", string group = "", anydata Additional Values, DeleteProjectRoleActorsFromRoleQueries queries) returns ProjectRole|error;
+    resource function delete api/'3/role/[int id]/actors(map<string|string[]> headers = {}, string groupId = "", string user = "", string group = "", DeleteProjectRoleActorsFromRoleQueries queries) returns ProjectRole|error;
 
     # Get screens
     # 
-    resource function get api/'3/screens(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, ("GLOBAL"|"TEMPLATE"|"PROJECT")[] scope = [], "name"|"-name"|"+name"|"id"|"-id"|"+id" orderBy = "name", int[] id = [], string queryString = "", int startAt = 0, anydata Additional Values, GetScreensQueries queries) returns PageBeanScreen|error;
+    resource function get api/'3/screens(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, ("GLOBAL"|"TEMPLATE"|"PROJECT")[] scope = [], "name"|"-name"|"+name"|"id"|"-id"|"+id" orderBy = "name", int[] id = [], string queryString = "", int startAt = 0, GetScreensQueries queries) returns PageBeanScreen|error;
 
     # Create screen
     # 
@@ -15981,7 +16081,7 @@
 
     # Get bulk screen tabs
     # 
-    resource function get api/'3/screens/tabs(map<string|string[]> headers = {}, int[] screenId = [], int[] tabId = [], int:Signed32 maxResult = 0, int startAt = 0, anydata Additional Values, GetBulkScreenTabsQueries queries) returns json|error;
+    resource function get api/'3/screens/tabs(map<string|string[]> headers = {}, int[] screenId = [], int[] tabId = [], int:Signed32 maxResult = 0, int startAt = 0, GetBulkScreenTabsQueries queries) returns json|error;
 
     # Update screen
     # 
@@ -15997,7 +16097,7 @@
 
     # Get all screen tabs
     # 
-    resource function get api/'3/screens/[int screenId]/tabs(map<string|string[]> headers = {}, string projectKey = "", anydata Additional Values, GetAllScreenTabsQueries queries) returns ScreenableTab[]|error;
+    resource function get api/'3/screens/[int screenId]/tabs(map<string|string[]> headers = {}, string projectKey = "", GetAllScreenTabsQueries queries) returns ScreenableTab[]|error;
 
     # Create screen tab
     # 
@@ -16013,7 +16113,7 @@
 
     # Get all screen tab fields
     # 
-    resource function get api/'3/screens/[int screenId]/tabs/[int tabId]/fields(map<string|string[]> headers = {}, string projectKey = "", anydata Additional Values, GetAllScreenTabFieldsQueries queries) returns ScreenableField[]|error;
+    resource function get api/'3/screens/[int screenId]/tabs/[int tabId]/fields(map<string|string[]> headers = {}, string projectKey = "", GetAllScreenTabFieldsQueries queries) returns ScreenableField[]|error;
 
     # Add screen tab field
     # 
@@ -16033,7 +16133,7 @@
 
     # Get screen schemes
     # 
-    resource function get api/'3/screenscheme(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, "name"|"-name"|"+name"|"id"|"-id"|"+id" orderBy = "name", int[] id = [], string queryString = "", int startAt = 0, anydata Additional Values, GetScreenSchemesQueries queries) returns PageBeanScreenScheme|error;
+    resource function get api/'3/screenscheme(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, "name"|"-name"|"+name"|"id"|"-id"|"+id" orderBy = "name", int[] id = [], string queryString = "", int startAt = 0, GetScreenSchemesQueries queries) returns PageBeanScreenScheme|error;
 
     # Create screen scheme
     # 
@@ -16049,7 +16149,7 @@
 
     # Currently being removed. Search for issues using JQL (GET)
     # 
-    resource function get api/'3/search(map<string|string[]> headers = {}, string expand = "", string jql = "", int:Signed32 maxResults = 0, "strict"|"warn"|"none"|"true"|"false" validateQuery = "strict", boolean fieldsByKeys = false, string[] fields = [], int:Signed32 startAt = 0, string[] properties = [], boolean failFast = false, anydata Additional Values, SearchForIssuesUsingJqlQueries queries) returns SearchResults|error;
+    resource function get api/'3/search(map<string|string[]> headers = {}, string expand = "", string jql = "", int:Signed32 maxResults = 0, "strict"|"warn"|"none"|"true"|"false" validateQuery = "strict", boolean fieldsByKeys = false, string[] fields = [], int:Signed32 startAt = 0, string[] properties = [], boolean failFast = false, SearchForIssuesUsingJqlQueries queries) returns SearchResults|error;
 
     # Currently being removed. Search for issues using JQL (POST)
     # 
@@ -16061,7 +16161,7 @@
 
     # Search for issues using JQL enhanced search (GET)
     # 
-    resource function get api/'3/search/jql(map<string|string[]> headers = {}, string expand = "", string jql = "", string nextPageToken = "", int:Signed32 maxResults = 0, boolean fieldsByKeys = false, string[] fields = [], int[] reconcileIssues = [], string[] properties = [], boolean failFast = false, anydata Additional Values, SearchAndReconsileIssuesUsingJqlQueries queries) returns SearchAndReconcileResults|error;
+    resource function get api/'3/search/jql(map<string|string[]> headers = {}, string expand = "", string jql = "", string nextPageToken = "", int:Signed32 maxResults = 0, boolean fieldsByKeys = false, string[] fields = [], int[] reconcileIssues = [], string[] properties = [], boolean failFast = false, SearchAndReconsileIssuesUsingJqlQueries queries) returns SearchAndReconcileResults|error;
 
     # Search for issues using JQL enhanced search (POST)
     # 
@@ -16101,7 +16201,7 @@
 
     # Bulk get statuses
     # 
-    resource function get api/'3/statuses(map<string|string[]> headers = {}, string expand = "", string[] id = [], anydata Additional Values, GetStatusesByIdQueries queries) returns JiraStatus[]|error;
+    resource function get api/'3/statuses(map<string|string[]> headers = {}, string expand = "", string[] id = [], GetStatusesByIdQueries queries) returns JiraStatus[]|error;
 
     # Bulk update statuses
     # 
@@ -16113,23 +16213,23 @@
 
     # Bulk delete Statuses
     # 
-    resource function delete api/'3/statuses(map<string|string[]> headers = {}, string[] id = [], anydata Additional Values, DeleteStatusesByIdQueries queries) returns json|error;
+    resource function delete api/'3/statuses(map<string|string[]> headers = {}, string[] id = [], DeleteStatusesByIdQueries queries) returns json|error;
 
     # Search statuses paginated
     # 
-    resource function get api/'3/statuses/search(map<string|string[]> headers = {}, string expand = "", string searchString = "", int:Signed32 maxResults = 0, string statusCategory = "", string projectId = "", int startAt = 0, anydata Additional Values, SearchQueries queries) returns PageOfStatuses|error;
+    resource function get api/'3/statuses/search(map<string|string[]> headers = {}, string expand = "", string searchString = "", int:Signed32 maxResults = 0, string statusCategory = "", string projectId = "", int startAt = 0, SearchQueries queries) returns PageOfStatuses|error;
 
     # Get issue type usages by status and project
     # 
-    resource function get api/'3/statuses/[string statusId]/project/[string projectId]/issueTypeUsages(map<string|string[]> headers = {}, string nextPageToken = "", int:Signed32 maxResults = 0, anydata Additional Values, GetProjectIssueTypeUsagesForStatusQueries queries) returns StatusProjectIssueTypeUsageDTO|error;
+    resource function get api/'3/statuses/[string statusId]/project/[string projectId]/issueTypeUsages(map<string|string[]> headers = {}, string nextPageToken = "", int:Signed32 maxResults = 0, GetProjectIssueTypeUsagesForStatusQueries queries) returns StatusProjectIssueTypeUsageDTO|error;
 
     # Get project usages by status
     # 
-    resource function get api/'3/statuses/[string statusId]/projectUsages(map<string|string[]> headers = {}, string nextPageToken = "", int:Signed32 maxResults = 0, anydata Additional Values, GetProjectUsagesForStatusQueries queries) returns StatusProjectUsageDTO|error;
+    resource function get api/'3/statuses/[string statusId]/projectUsages(map<string|string[]> headers = {}, string nextPageToken = "", int:Signed32 maxResults = 0, GetProjectUsagesForStatusQueries queries) returns StatusProjectUsageDTO|error;
 
     # Get workflow usages by status
     # 
-    resource function get api/'3/statuses/[string statusId]/workflowUsages(map<string|string[]> headers = {}, string nextPageToken = "", int:Signed32 maxResults = 0, anydata Additional Values, GetWorkflowUsagesForStatusQueries queries) returns StatusWorkflowUsageDTO|error;
+    resource function get api/'3/statuses/[string statusId]/workflowUsages(map<string|string[]> headers = {}, string nextPageToken = "", int:Signed32 maxResults = 0, GetWorkflowUsagesForStatusQueries queries) returns StatusWorkflowUsageDTO|error;
 
     # Get task
     # 
@@ -16141,7 +16241,7 @@
 
     # Get UI modifications
     # 
-    resource function get api/'3/uiModifications(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, int startAt = 0, anydata Additional Values, GetUiModificationsQueries queries) returns PageBeanUiModificationDetails|error;
+    resource function get api/'3/uiModifications(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, int startAt = 0, GetUiModificationsQueries queries) returns PageBeanUiModificationDetails|error;
 
     # Create UI modification
     # 
@@ -16161,7 +16261,7 @@
 
     # Load avatar
     # 
-    resource function post api/'3/universal_avatar/'type/["project"|"issuetype"|"priority" 'type]/owner/[string entityId](http:Request request, map<string|string[]> headers = {}, int:Signed32 size = 0, int:Signed32 x = 0, int:Signed32 y = 0, anydata Additional Values, StoreAvatarQueries queries) returns Avatar|error; // Special Agent Note: Request FROM ballerina/http package
+    resource function post api/'3/universal_avatar/'type/["project"|"issuetype"|"priority" 'type]/owner/[string entityId](http:Request request, map<string|string[]> headers = {}, int:Signed32 size = 0, int:Signed32 x = 0, int:Signed32 y = 0, StoreAvatarQueries queries) returns Avatar|error; // Special Agent Note: Request FROM ballerina/http package
 
     # Delete avatar
     # 
@@ -16169,19 +16269,19 @@
 
     # Get avatar image by type
     # 
-    resource function get api/'3/universal_avatar/view/'type/["issuetype"|"project"|"priority" 'type](map<string|string[]> headers = {}, "xsmall"|"small"|"medium"|"large"|"xlarge" size = "xsmall", "png"|"svg" format = "png", anydata Additional Values, GetAvatarImageByTypeQueries queries) returns StreamingResponseBody|error;
+    resource function get api/'3/universal_avatar/view/'type/["issuetype"|"project"|"priority" 'type](map<string|string[]> headers = {}, "xsmall"|"small"|"medium"|"large"|"xlarge" size = "xsmall", "png"|"svg" format = "png", GetAvatarImageByTypeQueries queries) returns StreamingResponseBody|error;
 
     # Get avatar image by ID
     # 
-    resource function get api/'3/universal_avatar/view/'type/["issuetype"|"project"|"priority" 'type]/avatar/[int id](map<string|string[]> headers = {}, "xsmall"|"small"|"medium"|"large"|"xlarge" size = "xsmall", "png"|"svg" format = "png", anydata Additional Values, GetAvatarImageByIDQueries queries) returns StreamingResponseBody|error;
+    resource function get api/'3/universal_avatar/view/'type/["issuetype"|"project"|"priority" 'type]/avatar/[int id](map<string|string[]> headers = {}, "xsmall"|"small"|"medium"|"large"|"xlarge" size = "xsmall", "png"|"svg" format = "png", GetAvatarImageByIDQueries queries) returns StreamingResponseBody|error;
 
     # Get avatar image by owner
     # 
-    resource function get api/'3/universal_avatar/view/'type/["issuetype"|"project"|"priority" 'type]/owner/[string entityId](map<string|string[]> headers = {}, "xsmall"|"small"|"medium"|"large"|"xlarge" size = "xsmall", "png"|"svg" format = "png", anydata Additional Values, GetAvatarImageByOwnerQueries queries) returns StreamingResponseBody|error;
+    resource function get api/'3/universal_avatar/view/'type/["issuetype"|"project"|"priority" 'type]/owner/[string entityId](map<string|string[]> headers = {}, "xsmall"|"small"|"medium"|"large"|"xlarge" size = "xsmall", "png"|"svg" format = "png", GetAvatarImageByOwnerQueries queries) returns StreamingResponseBody|error;
 
     # Get user
     # 
-    resource function get api/'3/user(map<string|string[]> headers = {}, string accountId = "", string expand = "", string key = "", string username = "", anydata Additional Values, GetUserQueries queries) returns User|error;
+    resource function get api/'3/user(map<string|string[]> headers = {}, string accountId = "", string expand = "", string key = "", string username = "", GetUserQueries queries) returns User|error;
 
     # Create user
     # 
@@ -16189,103 +16289,103 @@
 
     # Delete user
     # 
-    resource function delete api/'3/user(map<string|string[]> headers = {}, string accountId = "", string key = "", string username = "", anydata Additional Values, RemoveUserQueries queries) returns error?;
+    resource function delete api/'3/user(map<string|string[]> headers = {}, string accountId = "", string key = "", string username = "", RemoveUserQueries queries) returns error?;
 
     # Find users assignable to projects
     # 
-    resource function get api/'3/user/assignable/multiProjectSearch(map<string|string[]> headers = {}, string accountId = "", int:Signed32 maxResults = 0, string query = "", string projectKeys = "", int:Signed32 startAt = 0, string username = "", anydata Additional Values, FindBulkAssignableUsersQueries queries) returns User[]|error;
+    resource function get api/'3/user/assignable/multiProjectSearch(map<string|string[]> headers = {}, string accountId = "", int:Signed32 maxResults = 0, string query = "", string projectKeys = "", int:Signed32 startAt = 0, string username = "", FindBulkAssignableUsersQueries queries) returns User[]|error;
 
     # Find users assignable to issues
     # 
-    resource function get api/'3/user/assignable/search(map<string|string[]> headers = {}, string accountId = "", string issueId = "", string issueKey = "", int:Signed32 maxResults = 0, string query = "", string project = "", boolean recommend = false, string sessionId = "", int:Signed32 startAt = 0, int:Signed32 actionDescriptorId = 0, string username = "", anydata Additional Values, FindAssignableUsersQueries queries) returns User[]|error;
+    resource function get api/'3/user/assignable/search(map<string|string[]> headers = {}, string accountId = "", string issueId = "", string issueKey = "", int:Signed32 maxResults = 0, string query = "", string project = "", boolean recommend = false, string sessionId = "", int:Signed32 startAt = 0, int:Signed32 actionDescriptorId = 0, string username = "", FindAssignableUsersQueries queries) returns User[]|error;
 
     # Bulk get users
     # 
-    resource function get api/'3/user/bulk(map<string|string[]> headers = {}, BulkGetUsersQueriesAccountIdItemsString[] accountId = [], int:Signed32 maxResults = 0, int startAt = 0, string[] key = [], string[] username = [], anydata Additional Values, BulkGetUsersQueries queries) returns PageBeanUser|error;
+    resource function get api/'3/user/bulk(map<string|string[]> headers = {}, BulkGetUsersQueriesAccountIdItemsString[] accountId = [], int:Signed32 maxResults = 0, int startAt = 0, string[] key = [], string[] username = [], BulkGetUsersQueries queries) returns PageBeanUser|error;
 
     # Get account IDs for users
     # 
-    resource function get api/'3/user/bulk/migration(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, string[] key = [], string[] username = [], anydata Additional Values, BulkGetUsersMigrationQueries queries) returns UserMigrationBean[]|error;
+    resource function get api/'3/user/bulk/migration(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, string[] key = [], string[] username = [], BulkGetUsersMigrationQueries queries) returns UserMigrationBean[]|error;
 
     # Get user default columns
     # 
-    resource function get api/'3/user/columns(map<string|string[]> headers = {}, string accountId = "", string username = "", anydata Additional Values, GetUserDefaultColumnsQueries queries) returns ColumnItem[]|error;
+    resource function get api/'3/user/columns(map<string|string[]> headers = {}, string accountId = "", string username = "", GetUserDefaultColumnsQueries queries) returns ColumnItem[]|error;
 
     # Set user default columns
     # 
-    resource function put api/'3/user/columns(http:Request request, map<string|string[]> headers = {}, string accountId = "", anydata Additional Values, SetUserColumnsQueries queries) returns json|error; // Special Agent Note: Request FROM ballerina/http package
+    resource function put api/'3/user/columns(http:Request request, map<string|string[]> headers = {}, string accountId = "", SetUserColumnsQueries queries) returns json|error; // Special Agent Note: Request FROM ballerina/http package
 
     # Reset user default columns
     # 
-    resource function delete api/'3/user/columns(map<string|string[]> headers = {}, string accountId = "", string username = "", anydata Additional Values, ResetUserColumnsQueries queries) returns error?;
+    resource function delete api/'3/user/columns(map<string|string[]> headers = {}, string accountId = "", string username = "", ResetUserColumnsQueries queries) returns error?;
 
     # Get user email
     # 
-    resource function get api/'3/user/email(map<string|string[]> headers = {}, string accountId = "", anydata Additional Values, GetUserEmailQueries queries) returns UnrestrictedUserEmail|error;
+    resource function get api/'3/user/email(map<string|string[]> headers = {}, string accountId = "", GetUserEmailQueries queries) returns UnrestrictedUserEmail|error;
 
     # Get user email bulk
     # 
-    resource function get api/'3/user/email/bulk(map<string|string[]> headers = {}, GetUserEmailBulkQueriesAccountIdItemsString[] accountId = [], anydata Additional Values, GetUserEmailBulkQueries queries) returns UnrestrictedUserEmail|error;
+    resource function get api/'3/user/email/bulk(map<string|string[]> headers = {}, GetUserEmailBulkQueriesAccountIdItemsString[] accountId = [], GetUserEmailBulkQueries queries) returns UnrestrictedUserEmail|error;
 
     # Get user groups
     # 
-    resource function get api/'3/user/groups(map<string|string[]> headers = {}, string accountId = "", string key = "", string username = "", anydata Additional Values, GetUserGroupsQueries queries) returns GroupName[]|error;
+    resource function get api/'3/user/groups(map<string|string[]> headers = {}, string accountId = "", string key = "", string username = "", GetUserGroupsQueries queries) returns GroupName[]|error;
 
     # Get user nav property
     # 
-    resource function get api/'3/user/nav4\-opt\-property/[string propertyKey](map<string|string[]> headers = {}, string accountId = "", anydata Additional Values, GetUserNavPropertyQueries queries) returns UserNavPropertyJsonBean|error;
+    resource function get api/'3/user/nav4\-opt\-property/[string propertyKey](map<string|string[]> headers = {}, string accountId = "", GetUserNavPropertyQueries queries) returns UserNavPropertyJsonBean|error;
 
     # Set user nav property
     # 
-    resource function put api/'3/user/nav4\-opt\-property/[string propertyKey](json payload, map<string|string[]> headers = {}, string accountId = "", anydata Additional Values, SetUserNavPropertyQueries queries) returns json|error;
+    resource function put api/'3/user/nav4\-opt\-property/[string propertyKey](json payload, map<string|string[]> headers = {}, string accountId = "", SetUserNavPropertyQueries queries) returns json|error;
 
     # Find users with permissions
     # 
-    resource function get api/'3/user/permission/search(map<string|string[]> headers = {}, string accountId = "", string projectKey = "", string issueKey = "", string permissions = "", int:Signed32 maxResults = 0, string query = "", int:Signed32 startAt = 0, string username = "", anydata Additional Values, FindUsersWithAllPermissionsQueries queries) returns User[]|error;
+    resource function get api/'3/user/permission/search(map<string|string[]> headers = {}, string accountId = "", string projectKey = "", string issueKey = "", string permissions = "", int:Signed32 maxResults = 0, string query = "", int:Signed32 startAt = 0, string username = "", FindUsersWithAllPermissionsQueries queries) returns User[]|error;
 
     # Find users for picker
     # 
-    resource function get api/'3/user/picker(map<string|string[]> headers = {}, string[] excludeAccountIds = [], int:Signed32 maxResults = 0, string query = "", string[] exclude = [], boolean showAvatar = false, boolean excludeConnectUsers = false, string avatarSize = "", anydata Additional Values, FindUsersForPickerQueries queries) returns FoundUsers|error;
+    resource function get api/'3/user/picker(map<string|string[]> headers = {}, string[] excludeAccountIds = [], int:Signed32 maxResults = 0, string query = "", string[] exclude = [], boolean showAvatar = false, boolean excludeConnectUsers = false, string avatarSize = "", FindUsersForPickerQueries queries) returns FoundUsers|error;
 
     # Get user property keys
     # 
-    resource function get api/'3/user/properties(map<string|string[]> headers = {}, string accountId = "", string userKey = "", string username = "", anydata Additional Values, GetUserPropertyKeysQueries queries) returns PropertyKeys|error;
+    resource function get api/'3/user/properties(map<string|string[]> headers = {}, string accountId = "", string userKey = "", string username = "", GetUserPropertyKeysQueries queries) returns PropertyKeys|error;
 
     # Get user property
     # 
-    resource function get api/'3/user/properties/[string propertyKey](map<string|string[]> headers = {}, string accountId = "", string userKey = "", string username = "", anydata Additional Values, GetUserPropertyQueries queries) returns EntityProperty|error;
+    resource function get api/'3/user/properties/[string propertyKey](map<string|string[]> headers = {}, string accountId = "", string userKey = "", string username = "", GetUserPropertyQueries queries) returns EntityProperty|error;
 
     # Set user property
     # 
-    resource function put api/'3/user/properties/[string propertyKey](json payload, map<string|string[]> headers = {}, string accountId = "", string userKey = "", string username = "", anydata Additional Values, SetUserPropertyQueries queries) returns json|error;
+    resource function put api/'3/user/properties/[string propertyKey](json payload, map<string|string[]> headers = {}, string accountId = "", string userKey = "", string username = "", SetUserPropertyQueries queries) returns json|error;
 
     # Delete user property
     # 
-    resource function delete api/'3/user/properties/[string propertyKey](map<string|string[]> headers = {}, string accountId = "", string userKey = "", string username = "", anydata Additional Values, DeleteUserPropertyQueries queries) returns error?;
+    resource function delete api/'3/user/properties/[string propertyKey](map<string|string[]> headers = {}, string accountId = "", string userKey = "", string username = "", DeleteUserPropertyQueries queries) returns error?;
 
     # Find users
     # 
-    resource function get api/'3/user/search(map<string|string[]> headers = {}, string accountId = "", int:Signed32 maxResults = 0, string query = "", string property = "", int:Signed32 startAt = 0, string username = "", anydata Additional Values, FindUsersQueries queries) returns User[]|error;
+    resource function get api/'3/user/search(map<string|string[]> headers = {}, string accountId = "", int:Signed32 maxResults = 0, string query = "", string property = "", int:Signed32 startAt = 0, string username = "", FindUsersQueries queries) returns User[]|error;
 
     # Find users by query
     # 
-    resource function get api/'3/user/search/query(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, string query = "", int startAt = 0, anydata Additional Values, FindUsersByQueryQueries queries) returns PageBeanUser|error;
+    resource function get api/'3/user/search/query(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, string query = "", int startAt = 0, FindUsersByQueryQueries queries) returns PageBeanUser|error;
 
     # Find user keys by query
     # 
-    resource function get api/'3/user/search/query/'key(map<string|string[]> headers = {}, int:Signed32 maxResult = 0, string query = "", int startAt = 0, anydata Additional Values, FindUserKeysByQueryQueries queries) returns PageBeanUserKey|error;
+    resource function get api/'3/user/search/query/'key(map<string|string[]> headers = {}, int:Signed32 maxResult = 0, string query = "", int startAt = 0, FindUserKeysByQueryQueries queries) returns PageBeanUserKey|error;
 
     # Find users with browse permission
     # 
-    resource function get api/'3/user/viewissue/search(map<string|string[]> headers = {}, string accountId = "", string projectKey = "", string issueKey = "", int:Signed32 maxResults = 0, string query = "", int:Signed32 startAt = 0, string username = "", anydata Additional Values, FindUsersWithBrowsePermissionQueries queries) returns User[]|error;
+    resource function get api/'3/user/viewissue/search(map<string|string[]> headers = {}, string accountId = "", string projectKey = "", string issueKey = "", int:Signed32 maxResults = 0, string query = "", int:Signed32 startAt = 0, string username = "", FindUsersWithBrowsePermissionQueries queries) returns User[]|error;
 
     # Get all users default
     # 
-    resource function get api/'3/users(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int:Signed32 startAt = 0, anydata Additional Values, GetAllUsersDefaultQueries queries) returns User[]|error;
+    resource function get api/'3/users(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int:Signed32 startAt = 0, GetAllUsersDefaultQueries queries) returns User[]|error;
 
     # Get all users
     # 
-    resource function get api/'3/users/search(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int:Signed32 startAt = 0, anydata Additional Values, GetAllUsersQueries queries) returns User[]|error;
+    resource function get api/'3/users/search(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int:Signed32 startAt = 0, GetAllUsersQueries queries) returns User[]|error;
 
     # Create version
     # 
@@ -16293,7 +16393,7 @@
 
     # Get version
     # 
-    resource function get api/'3/version/[string id](map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetVersionQueries queries) returns Version|error;
+    resource function get api/'3/version/[string id](map<string|string[]> headers = {}, string expand = "", GetVersionQueries queries) returns Version|error;
 
     # Update version
     # 
@@ -16301,7 +16401,7 @@
 
     # Delete version
     # 
-    resource function delete api/'3/version/[string id](map<string|string[]> headers = {}, string moveAffectedIssuesTo = "", string moveFixIssuesTo = "", anydata Additional Values, DeleteVersionQueries queries) returns error?;
+    resource function delete api/'3/version/[string id](map<string|string[]> headers = {}, string moveAffectedIssuesTo = "", string moveFixIssuesTo = "", DeleteVersionQueries queries) returns error?;
 
     # Merge versions
     # 
@@ -16341,7 +16441,7 @@
 
     # Get dynamic webhooks for app
     # 
-    resource function get api/'3/webhook(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, anydata Additional Values, GetDynamicWebhooksForAppQueries queries) returns PageBeanWebhook|error;
+    resource function get api/'3/webhook(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, GetDynamicWebhooksForAppQueries queries) returns PageBeanWebhook|error;
 
     # Register dynamic webhooks
     # 
@@ -16353,7 +16453,7 @@
 
     # Get failed webhooks
     # 
-    resource function get api/'3/webhook/failed(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int after = 0, anydata Additional Values, GetFailedWebhooksQueries queries) returns FailedWebhooks|error;
+    resource function get api/'3/webhook/failed(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int after = 0, GetFailedWebhooksQueries queries) returns FailedWebhooks|error;
 
     # Extend webhook life
     # 
@@ -16361,7 +16461,7 @@
 
     # Get all workflows
     # 
-    resource function get api/'3/workflow(map<string|string[]> headers = {}, string workflowName = "", anydata Additional Values, GetAllWorkflowsQueries queries) returns DeprecatedWorkflow[]|error;
+    resource function get api/'3/workflow(map<string|string[]> headers = {}, string workflowName = "", GetAllWorkflowsQueries queries) returns DeprecatedWorkflow[]|error;
 
     # Create workflow
     # 
@@ -16369,7 +16469,7 @@
 
     # Get workflow transition rule configurations
     # 
-    resource function get api/'3/workflow/rule/config(map<string|string[]> headers = {}, GetWorkflowTransitionRuleConfigurationsQueriesWorkflowNamesItemsString[] workflowNames = [], ("postfunction"|"condition"|"validator")[] types = [], GetWorkflowTransitionRuleConfigurationsQueriesWithTagsItemsString[] withTags = [], string expand = "", int:Signed32 maxResults = 0, string[] keys = [], boolean draft = false, int startAt = 0, anydata Additional Values, GetWorkflowTransitionRuleConfigurationsQueries queries) returns PageBeanWorkflowTransitionRules|error;
+    resource function get api/'3/workflow/rule/config(map<string|string[]> headers = {}, GetWorkflowTransitionRuleConfigurationsQueriesWorkflowNamesItemsString[] workflowNames = [], ("postfunction"|"condition"|"validator")[] types = [], GetWorkflowTransitionRuleConfigurationsQueriesWithTagsItemsString[] withTags = [], string expand = "", int:Signed32 maxResults = 0, string[] keys = [], boolean draft = false, int startAt = 0, GetWorkflowTransitionRuleConfigurationsQueries queries) returns PageBeanWorkflowTransitionRules|error;
 
     # Update workflow transition rule configurations
     # 
@@ -16381,23 +16481,23 @@
 
     # Get workflows paginated
     # 
-    resource function get api/'3/workflow/search(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, "name"|"-name"|"+name"|"created"|"-created"|"+created"|"updated"|"+updated"|"-updated" orderBy = "name", string[] workflowName = [], string queryString = "", boolean isActive = false, int startAt = 0, anydata Additional Values, GetWorkflowsPaginatedQueries queries) returns PageBeanWorkflow|error;
+    resource function get api/'3/workflow/search(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, "name"|"-name"|"+name"|"created"|"-created"|"+created"|"updated"|"+updated"|"-updated" orderBy = "name", string[] workflowName = [], string queryString = "", boolean isActive = false, int startAt = 0, GetWorkflowsPaginatedQueries queries) returns PageBeanWorkflow|error;
 
     # Get workflow transition properties
     # 
-    resource function get api/'3/workflow/transitions/[int transitionId]/properties(map<string|string[]> headers = {}, "live"|"draft" workflowMode = "live", string workflowName = "", boolean includeReservedKeys = false, string key = "", anydata Additional Values, GetWorkflowTransitionPropertiesQueries queries) returns WorkflowTransitionProperty|error;
+    resource function get api/'3/workflow/transitions/[int transitionId]/properties(map<string|string[]> headers = {}, "live"|"draft" workflowMode = "live", string workflowName = "", boolean includeReservedKeys = false, string key = "", GetWorkflowTransitionPropertiesQueries queries) returns WorkflowTransitionProperty|error;
 
     # Update workflow transition property
     # 
-    resource function put api/'3/workflow/transitions/[int transitionId]/properties(WorkflowTransitionProperty payload, map<string|string[]> headers = {}, "live"|"draft" workflowMode = "live", string workflowName = "", string key = "", anydata Additional Values, UpdateWorkflowTransitionPropertyQueries queries) returns WorkflowTransitionProperty|error|();
+    resource function put api/'3/workflow/transitions/[int transitionId]/properties(WorkflowTransitionProperty payload, map<string|string[]> headers = {}, "live"|"draft" workflowMode = "live", string workflowName = "", string key = "", UpdateWorkflowTransitionPropertyQueries queries) returns WorkflowTransitionProperty|error|();
 
     # Create workflow transition property
     # 
-    resource function post api/'3/workflow/transitions/[int transitionId]/properties(WorkflowTransitionProperty payload, map<string|string[]> headers = {}, "live"|"draft" workflowMode = "live", string workflowName = "", string key = "", anydata Additional Values, CreateWorkflowTransitionPropertyQueries queries) returns WorkflowTransitionProperty|error;
+    resource function post api/'3/workflow/transitions/[int transitionId]/properties(WorkflowTransitionProperty payload, map<string|string[]> headers = {}, "live"|"draft" workflowMode = "live", string workflowName = "", string key = "", CreateWorkflowTransitionPropertyQueries queries) returns WorkflowTransitionProperty|error;
 
     # Delete workflow transition property
     # 
-    resource function delete api/'3/workflow/transitions/[int transitionId]/properties(map<string|string[]> headers = {}, "live"|"draft" workflowMode = "live", string workflowName = "", string key = "", anydata Additional Values, DeleteWorkflowTransitionPropertyQueries queries) returns error?;
+    resource function delete api/'3/workflow/transitions/[int transitionId]/properties(map<string|string[]> headers = {}, "live"|"draft" workflowMode = "live", string workflowName = "", string key = "", DeleteWorkflowTransitionPropertyQueries queries) returns error?;
 
     # Delete inactive workflow
     # 
@@ -16405,23 +16505,23 @@
 
     # Get issue types in a project that are using a given workflow
     # 
-    resource function get api/'3/workflow/[string workflowId]/project/[int projectId]/issueTypeUsages(map<string|string[]> headers = {}, string nextPageToken = "", int:Signed32 maxResults = 0, anydata Additional Values, GetWorkflowProjectIssueTypeUsagesQueries queries) returns WorkflowProjectIssueTypeUsageDTO|error;
+    resource function get api/'3/workflow/[string workflowId]/project/[int projectId]/issueTypeUsages(map<string|string[]> headers = {}, string nextPageToken = "", int:Signed32 maxResults = 0, GetWorkflowProjectIssueTypeUsagesQueries queries) returns WorkflowProjectIssueTypeUsageDTO|error;
 
     # Get projects using a given workflow
     # 
-    resource function get api/'3/workflow/[string workflowId]/projectUsages(map<string|string[]> headers = {}, string nextPageToken = "", int:Signed32 maxResults = 0, anydata Additional Values, GetProjectUsagesForWorkflowQueries queries) returns WorkflowProjectUsageDTO|error;
+    resource function get api/'3/workflow/[string workflowId]/projectUsages(map<string|string[]> headers = {}, string nextPageToken = "", int:Signed32 maxResults = 0, GetProjectUsagesForWorkflowQueries queries) returns WorkflowProjectUsageDTO|error;
 
     # Get workflow schemes which are using a given workflow
     # 
-    resource function get api/'3/workflow/[string workflowId]/workflowSchemes(map<string|string[]> headers = {}, string nextPageToken = "", int:Signed32 maxResults = 0, anydata Additional Values, GetWorkflowSchemeUsagesForWorkflowQueries queries) returns WorkflowSchemeUsageDTO|error;
+    resource function get api/'3/workflow/[string workflowId]/workflowSchemes(map<string|string[]> headers = {}, string nextPageToken = "", int:Signed32 maxResults = 0, GetWorkflowSchemeUsagesForWorkflowQueries queries) returns WorkflowSchemeUsageDTO|error;
 
     # Bulk get workflows
     # 
-    resource function post api/'3/workflows(WorkflowReadRequest payload, map<string|string[]> headers = {}, string expand = "", boolean useApprovalConfiguration = false, anydata Additional Values, ReadWorkflowsQueries queries) returns WorkflowReadResponse|error;
+    resource function post api/'3/workflows(WorkflowReadRequest payload, map<string|string[]> headers = {}, string expand = "", boolean useApprovalConfiguration = false, ReadWorkflowsQueries queries) returns WorkflowReadResponse|error;
 
     # Get available workflow capabilities
     # 
-    resource function get api/'3/workflows/capabilities(map<string|string[]> headers = {}, string issueTypeId = "", string projectId = "", string workflowId = "", anydata Additional Values, WorkflowCapabilitiesQueries queries) returns WorkflowCapabilities|error;
+    resource function get api/'3/workflows/capabilities(map<string|string[]> headers = {}, string issueTypeId = "", string projectId = "", string workflowId = "", WorkflowCapabilitiesQueries queries) returns WorkflowCapabilities|error;
 
     # Bulk create workflows
     # 
@@ -16437,11 +16537,11 @@
 
     # Search workflows
     # 
-    resource function get api/'3/workflows/search(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, string scope = "", string orderBy = "", string queryString = "", boolean isActive = false, int startAt = 0, anydata Additional Values, SearchWorkflowsQueries queries) returns WorkflowSearchResponse|error;
+    resource function get api/'3/workflows/search(map<string|string[]> headers = {}, string expand = "", int:Signed32 maxResults = 0, string scope = "", string orderBy = "", string queryString = "", boolean isActive = false, int startAt = 0, SearchWorkflowsQueries queries) returns WorkflowSearchResponse|error;
 
     # Bulk update workflows
     # 
-    resource function post api/'3/workflows/update(WorkflowUpdateRequest payload, map<string|string[]> headers = {}, string expand = "", anydata Additional Values, UpdateWorkflowsQueries queries) returns WorkflowUpdateResponse|error;
+    resource function post api/'3/workflows/update(WorkflowUpdateRequest payload, map<string|string[]> headers = {}, string expand = "", UpdateWorkflowsQueries queries) returns WorkflowUpdateResponse|error;
 
     # Validate update workflows
     # 
@@ -16449,7 +16549,7 @@
 
     # Get all workflow schemes
     # 
-    resource function get api/'3/workflowscheme(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, anydata Additional Values, GetAllWorkflowSchemesQueries queries) returns PageBeanWorkflowScheme|error;
+    resource function get api/'3/workflowscheme(map<string|string[]> headers = {}, int:Signed32 maxResults = 0, int startAt = 0, GetAllWorkflowSchemesQueries queries) returns PageBeanWorkflowScheme|error;
 
     # Create workflow scheme
     # 
@@ -16457,7 +16557,7 @@
 
     # Get workflow scheme project associations
     # 
-    resource function get api/'3/workflowscheme/project(map<string|string[]> headers = {}, int[] projectId = [], anydata Additional Values, GetWorkflowSchemeProjectAssociationsQueries queries) returns ContainerOfWorkflowSchemeAssociations|error;
+    resource function get api/'3/workflowscheme/project(map<string|string[]> headers = {}, int[] projectId = [], GetWorkflowSchemeProjectAssociationsQueries queries) returns ContainerOfWorkflowSchemeAssociations|error;
 
     # Assign workflow scheme to project
     # 
@@ -16465,7 +16565,7 @@
 
     # Bulk get workflow schemes
     # 
-    resource function post api/'3/workflowscheme/read(WorkflowSchemeReadRequest payload, map<string|string[]> headers = {}, string expand = "", anydata Additional Values, ReadWorkflowSchemesQueries queries) returns WorkflowSchemeReadResponse[]|error;
+    resource function post api/'3/workflowscheme/read(WorkflowSchemeReadRequest payload, map<string|string[]> headers = {}, string expand = "", ReadWorkflowSchemesQueries queries) returns WorkflowSchemeReadResponse[]|error;
 
     # Update workflow scheme
     # 
@@ -16477,7 +16577,7 @@
 
     # Get workflow scheme
     # 
-    resource function get api/'3/workflowscheme/[int id](map<string|string[]> headers = {}, boolean returnDraftIfExists = false, anydata Additional Values, GetWorkflowSchemeQueries queries) returns WorkflowScheme|error;
+    resource function get api/'3/workflowscheme/[int id](map<string|string[]> headers = {}, boolean returnDraftIfExists = false, GetWorkflowSchemeQueries queries) returns WorkflowScheme|error;
 
     # Classic update workflow scheme
     # 
@@ -16493,7 +16593,7 @@
 
     # Get default workflow
     # 
-    resource function get api/'3/workflowscheme/[int id]/default(map<string|string[]> headers = {}, boolean returnDraftIfExists = false, anydata Additional Values, GetDefaultWorkflowQueries queries) returns DefaultWorkflow|error;
+    resource function get api/'3/workflowscheme/[int id]/default(map<string|string[]> headers = {}, boolean returnDraftIfExists = false, GetDefaultWorkflowQueries queries) returns DefaultWorkflow|error;
 
     # Update default workflow
     # 
@@ -16501,7 +16601,7 @@
 
     # Delete default workflow
     # 
-    resource function delete api/'3/workflowscheme/[int id]/default(map<string|string[]> headers = {}, boolean updateDraftIfNeeded = false, anydata Additional Values, DeleteDefaultWorkflowQueries queries) returns WorkflowScheme|error;
+    resource function delete api/'3/workflowscheme/[int id]/default(map<string|string[]> headers = {}, boolean updateDraftIfNeeded = false, DeleteDefaultWorkflowQueries queries) returns WorkflowScheme|error;
 
     # Get draft workflow scheme
     # 
@@ -16541,23 +16641,23 @@
 
     # Publish draft workflow scheme
     # 
-    resource function post api/'3/workflowscheme/[int id]/draft/publish(PublishDraftWorkflowScheme payload, map<string|string[]> headers = {}, boolean validateOnly = false, anydata Additional Values, PublishDraftWorkflowSchemeQueries queries) returns error?;
+    resource function post api/'3/workflowscheme/[int id]/draft/publish(PublishDraftWorkflowScheme payload, map<string|string[]> headers = {}, boolean validateOnly = false, PublishDraftWorkflowSchemeQueries queries) returns error?;
 
     # Get issue types for workflows in draft workflow scheme
     # 
-    resource function get api/'3/workflowscheme/[int id]/draft/workflow(map<string|string[]> headers = {}, string workflowName = "", anydata Additional Values, GetDraftWorkflowQueries queries) returns IssueTypesWorkflowMapping|error;
+    resource function get api/'3/workflowscheme/[int id]/draft/workflow(map<string|string[]> headers = {}, string workflowName = "", GetDraftWorkflowQueries queries) returns IssueTypesWorkflowMapping|error;
 
     # Set issue types for workflow in workflow scheme
     # 
-    resource function put api/'3/workflowscheme/[int id]/draft/workflow(IssueTypesWorkflowMapping payload, map<string|string[]> headers = {}, string workflowName = "", anydata Additional Values, UpdateDraftWorkflowMappingQueries queries) returns WorkflowScheme|error;
+    resource function put api/'3/workflowscheme/[int id]/draft/workflow(IssueTypesWorkflowMapping payload, map<string|string[]> headers = {}, string workflowName = "", UpdateDraftWorkflowMappingQueries queries) returns WorkflowScheme|error;
 
     # Delete issue types for workflow in draft workflow scheme
     # 
-    resource function delete api/'3/workflowscheme/[int id]/draft/workflow(map<string|string[]> headers = {}, string workflowName = "", anydata Additional Values, DeleteDraftWorkflowMappingQueries queries) returns error?;
+    resource function delete api/'3/workflowscheme/[int id]/draft/workflow(map<string|string[]> headers = {}, string workflowName = "", DeleteDraftWorkflowMappingQueries queries) returns error?;
 
     # Get workflow for issue type in workflow scheme
     # 
-    resource function get api/'3/workflowscheme/[int id]/issuetype/[string issueType](map<string|string[]> headers = {}, boolean returnDraftIfExists = false, anydata Additional Values, GetWorkflowSchemeIssueTypeQueries queries) returns IssueTypeWorkflowMapping|error;
+    resource function get api/'3/workflowscheme/[int id]/issuetype/[string issueType](map<string|string[]> headers = {}, boolean returnDraftIfExists = false, GetWorkflowSchemeIssueTypeQueries queries) returns IssueTypeWorkflowMapping|error;
 
     # Set workflow for issue type in workflow scheme
     # 
@@ -16565,35 +16665,35 @@
 
     # Delete workflow for issue type in workflow scheme
     # 
-    resource function delete api/'3/workflowscheme/[int id]/issuetype/[string issueType](map<string|string[]> headers = {}, boolean updateDraftIfNeeded = false, anydata Additional Values, DeleteWorkflowSchemeIssueTypeQueries queries) returns WorkflowScheme|error;
+    resource function delete api/'3/workflowscheme/[int id]/issuetype/[string issueType](map<string|string[]> headers = {}, boolean updateDraftIfNeeded = false, DeleteWorkflowSchemeIssueTypeQueries queries) returns WorkflowScheme|error;
 
     # Get issue types for workflows in workflow scheme
     # 
-    resource function get api/'3/workflowscheme/[int id]/workflow(map<string|string[]> headers = {}, string workflowName = "", boolean returnDraftIfExists = false, anydata Additional Values, GetWorkflowQueries queries) returns IssueTypesWorkflowMapping|error;
+    resource function get api/'3/workflowscheme/[int id]/workflow(map<string|string[]> headers = {}, string workflowName = "", boolean returnDraftIfExists = false, GetWorkflowQueries queries) returns IssueTypesWorkflowMapping|error;
 
     # Set issue types for workflow in workflow scheme
     # 
-    resource function put api/'3/workflowscheme/[int id]/workflow(IssueTypesWorkflowMapping payload, map<string|string[]> headers = {}, string workflowName = "", anydata Additional Values, UpdateWorkflowMappingQueries queries) returns WorkflowScheme|error;
+    resource function put api/'3/workflowscheme/[int id]/workflow(IssueTypesWorkflowMapping payload, map<string|string[]> headers = {}, string workflowName = "", UpdateWorkflowMappingQueries queries) returns WorkflowScheme|error;
 
     # Delete issue types for workflow in workflow scheme
     # 
-    resource function delete api/'3/workflowscheme/[int id]/workflow(map<string|string[]> headers = {}, boolean updateDraftIfNeeded = false, string workflowName = "", anydata Additional Values, DeleteWorkflowMappingQueries queries) returns error?;
+    resource function delete api/'3/workflowscheme/[int id]/workflow(map<string|string[]> headers = {}, boolean updateDraftIfNeeded = false, string workflowName = "", DeleteWorkflowMappingQueries queries) returns error?;
 
     # Get projects which are using a given workflow scheme
     # 
-    resource function get api/'3/workflowscheme/[string workflowSchemeId]/projectUsages(map<string|string[]> headers = {}, string nextPageToken = "", int:Signed32 maxResults = 0, anydata Additional Values, GetProjectUsagesForWorkflowSchemeQueries queries) returns WorkflowSchemeProjectUsageDTO|error;
+    resource function get api/'3/workflowscheme/[string workflowSchemeId]/projectUsages(map<string|string[]> headers = {}, string nextPageToken = "", int:Signed32 maxResults = 0, GetProjectUsagesForWorkflowSchemeQueries queries) returns WorkflowSchemeProjectUsageDTO|error;
 
     # Get IDs of deleted worklogs
     # 
-    resource function get api/'3/worklog/deleted(map<string|string[]> headers = {}, int since = 0, anydata Additional Values, GetIdsOfWorklogsDeletedSinceQueries queries) returns ChangedWorklogs|error;
+    resource function get api/'3/worklog/deleted(map<string|string[]> headers = {}, int since = 0, GetIdsOfWorklogsDeletedSinceQueries queries) returns ChangedWorklogs|error;
 
     # Get worklogs
     # 
-    resource function post api/'3/worklog/list(WorklogIdsRequestBean payload, map<string|string[]> headers = {}, string expand = "", anydata Additional Values, GetWorklogsForIdsQueries queries) returns Worklog[]|error;
+    resource function post api/'3/worklog/list(WorklogIdsRequestBean payload, map<string|string[]> headers = {}, string expand = "", GetWorklogsForIdsQueries queries) returns Worklog[]|error;
 
     # Get IDs of updated worklogs
     # 
-    resource function get api/'3/worklog/updated(map<string|string[]> headers = {}, string expand = "", int since = 0, anydata Additional Values, GetIdsOfWorklogsModifiedSinceQueries queries) returns ChangedWorklogs|error;
+    resource function get api/'3/worklog/updated(map<string|string[]> headers = {}, string expand = "", int since = 0, GetIdsOfWorklogsModifiedSinceQueries queries) returns ChangedWorklogs|error;
 
     # Get app properties
     # 
@@ -16621,7 +16721,7 @@
 
     # Remove modules
     # 
-    resource function delete atlassian\-connect/'1/app/module/dynamic(map<string|string[]> headers = {}, string[] moduleKey = [], anydata Additional Values, DynamicModulesResourceRemoveModulesDeleteQueries queries) returns error?;
+    resource function delete atlassian\-connect/'1/app/module/dynamic(map<string|string[]> headers = {}, string[] moduleKey = [], DynamicModulesResourceRemoveModulesDeleteQueries queries) returns error?;
 
     # Bulk update custom field value
     # 
@@ -16637,7 +16737,7 @@
 
     # Retrieve the attributes of service registries
     # 
-    resource function get atlassian\-connect/'1/service\-registry(map<string|string[]> headers = {}, string[] serviceIds = [], anydata Additional Values, ServiceRegistryResourceServicesGetQueries queries) returns ServiceRegistry[]|error;
+    resource function get atlassian\-connect/'1/service\-registry(map<string|string[]> headers = {}, string[] serviceIds = [], ServiceRegistryResourceServicesGetQueries queries) returns ServiceRegistry[]|error;
 
     # Set app property (Forge)
     # 
`````
