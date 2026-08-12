# shopify.admin — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `shopify.admin` |
| **Old file** | `shopify.admin/old/ballerinax_shopify.admin.bal.txt` |
| **New file** | `shopify.admin/new/ballerinax_shopify.admin.bal.txt` |
| **Old lines** | 11780 |
| **New lines** | 15280 |
| **Lines added** | 3603 |
| **Lines removed** | 103 |
| **Hunks** | 442 |

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
| 1 | 154–166 | 154–173 | Types | +7 | −0 |
| 2 | 172–214 | 179–252 | Types | +31 | −0 |
| 3 | 222–266 | 260–327 | Types | +23 | −0 |
| 4 | 279–284 | 340–346 | Types | +1 | −0 |
| 5 | 290–317 | 352–396 | Types | +17 | −0 |
| 6 | 323–344 | 402–430 | Types | +7 | −0 |
| 7 | 349–359 | 435–450 | Types | +5 | −0 |
| 8 | 367–423 | 458–535 | Types | +21 | −0 |
| 9 | 426–437 | 538–551 | Types | +2 | −0 |
| 10 | 443–454 | 557–570 | Types | +2 | −0 |
| 11 | 460–465 | 576–582 | Types | +1 | −0 |
| 12 | 467–478 | 584–599 | Types | +4 | −0 |
| 13 | 483–564 | 604–720 | Types | +35 | −0 |
| 14 | 577–611 | 733–787 | Types | +20 | −0 |
| 15 | 613–632 | 789–817 | Types | +9 | −0 |
| 16 | 637–642 | 822–828 | Types | +1 | −0 |
| 17 | 658–670 | 844–860 | Types | +4 | −0 |
| 18 | 672–681 | 862–875 | Types | +4 | −0 |
| 19 | 684–689 | 878–884 | Types | +1 | −0 |
| 20 | 696–701 | 891–897 | Types | +1 | −0 |
| 21 | 703–724 | 899–929 | Types | +9 | −0 |
| 22 | 728–757 | 933–976 | Types | +14 | −0 |
| 23 | 764–774 | 983–995 | Types | +2 | −0 |
| 24 | 793–808 | 1014–1038 | Types | +9 | −0 |
| 25 | 816–836 | 1046–1074 | Types | +8 | −0 |
| 26 | 838–843 | 1076–1082 | Types | +1 | −0 |
| 27 | 845–856 | 1084–1098 | Types | +3 | −0 |
| 28 | 858–863 | 1100–1106 | Types | +1 | −0 |
| 29 | 868–873 | 1111–1117 | Types | +1 | −0 |
| 30 | 887–899 | 1131–1149 | Types | +6 | −0 |
| 31 | 905–915 | 1155–1167 | Types | +2 | −0 |
| 32 | 918–923 | 1170–1176 | Types | +1 | −0 |
| 33 | 925–950 | 1178–1212 | Types | +9 | −0 |
| 34 | 952–963 | 1214–1228 | Types | +3 | −0 |
| 35 | 970–1016 | 1235–1307 | Types | +26 | −0 |
| 36 | 1019–1024 | 1310–1316 | Types | +1 | −0 |
| 37 | 1027–1046 | 1319–1347 | Types | +9 | −0 |
| 38 | 1058–1076 | 1359–1386 | Types | +9 | −0 |
| 39 | 1079–1092 | 1389–1406 | Types | +4 | −0 |
| 40 | 1094–1121 | 1408–1447 | Types | +12 | −0 |
| 41 | 1124–1129 | 1450–1456 | Types | +1 | −0 |
| 42 | 1142–1182 | 1469–1533 | Types | +24 | −0 |
| 43 | 1185–1190 | 1536–1542 | Types | +1 | −0 |
| 44 | 1198–1210 | 1550–1567 | Types | +5 | −0 |
| 45 | 1214–1245 | 1571–1616 | Types | +14 | −0 |
| 46 | 1254–1267 | 1625–1644 | Types | +6 | −0 |
| 47 | 1270–1307 | 1647–1699 | Types | +15 | −0 |
| 48 | 1329–1402 | 1721–1849 | Types | +55 | −0 |
| 49 | 1404–1433 | 1851–1896 | Types | +16 | −0 |
| 50 | 1436–1466 | 1899–1936 | Types | +7 | −0 |
| 51 | 1474–1522 | 1944–2007 | Types | +15 | −0 |
| 52 | 1535–1553 | 2020–2047 | Types | +9 | −0 |
| 53 | 1556–1613 | 2050–2137 | Types | +30 | −0 |
| 54 | 1615–1658 | 2139–2204 | Types | +22 | −0 |
| 55 | 1665–1714 | 2211–2286 | Types | +26 | −0 |
| 56 | 1721–1744 | 2293–2327 | Types | +11 | −0 |
| 57 | 1748–1774 | 2331–2368 | Types | +11 | −0 |
| 58 | 1782–1802 | 2376–2404 | Types | +8 | −0 |
| 59 | 1804–1893 | 2406–2548 | Types | +53 | −0 |
| 60 | 1898–1936 | 2553–2607 | Types | +16 | −0 |
| 61 | 1939–1992 | 2610–2690 | Types | +27 | −0 |
| 62 | 2001–2015 | 2699–2721 | Types | +8 | −0 |
| 63 | 2018–2070 | 2724–2799 | Types | +23 | −0 |
| 64 | 2087–2160 | 2816–2944 | Types | +55 | −0 |
| 65 | 2164–2169 | 2948–2954 | Types | +1 | −0 |
| 66 | 2173–2194 | 2958–2988 | Types | +9 | −0 |
| 67 | 2199–2226 | 2993–3036 | Types | +16 | −0 |
| 68 | 2232–2272 | 3042–3097 | Types | +15 | −0 |
| 69 | 2285–2358 | 3110–3238 | Types | +55 | −0 |
| 70 | 2366–2375 | 3246–3260 | Types | +5 | −0 |
| 71 | 2382–2397 | 3267–3286 | Types | +4 | −0 |
| 72 | 2403–2415 | 3292–3309 | Types | +5 | −0 |
| 73 | 2421–2448 | 3315–3352 | Types | +10 | −0 |
| 74 | 2463–2478 | 3367–3390 | Types | +8 | −0 |
| 75 | 2488–2577 | 3400–3547 | Types | +58 | −0 |
| 76 | 2582–2616 | 3552–3600 | Types | +14 | −0 |
| 77 | 2619–2655 | 3603–3656 | Types | +17 | −0 |
| 78 | 2663–2700 | 3664–3716 | Types | +15 | −0 |
| 79 | 2703–2744 | 3719–3778 | Types | +18 | −0 |
| 80 | 2752–2789 | 3786–3838 | Types | +15 | −0 |
| 81 | 2795–2825 | 3844–3890 | Types | +16 | −0 |
| 82 | 2827–2832 | 3892–3898 | Types | +1 | −0 |
| 83 | 2837–2844 | 3903–3912 | Types | +2 | −0 |
| 84 | 2849–2854 | 3917–3923 | Types | +1 | −0 |
| 85 | 2858–2892 | 3927–3981 | Types | +20 | −0 |
| 86 | 2901–2918 | 3990–4015 | Types | +8 | −0 |
| 87 | 2927–2936 | 4024–4035 | Types | +2 | −0 |
| 88 | 2941–2952 | 4040–4055 | Types | +4 | −0 |
| 89 | 2955–2960 | 4058–4064 | Types | +1 | −0 |
| 90 | 2964–2989 | 4068–4102 | Types | +9 | −0 |
| 91 | 2994–3017 | 4107–4137 | Types | +7 | −0 |
| 92 | 3032–3037 | 4152–4158 | Types | +1 | −0 |
| 93 | 3045–3089 | 4166–4239 | Types | +29 | −0 |
| 94 | 3097–3110 | 4247–4264 | Types | +4 | −0 |
| 95 | 3117–3126 | 4271–4284 | Types | +4 | −0 |
| 96 | 3131–3142 | 4289–4303 | Types | +3 | −0 |
| 97 | 3144–3161 | 4305–4328 | Types | +6 | −0 |
| 98 | 3164–3175 | 4331–4348 | Types | +6 | −0 |
| 99 | 3178–3195 | 4351–4373 | Types | +5 | −0 |
| 100 | 3197–3215 | 4375–4402 | Types | +9 | −0 |
| 101 | 3217–3226 | 4404–4417 | Types | +4 | −0 |
| 102 | 3229–3252 | 4420–4448 | Types | +5 | −0 |
| 103 | 3262–3343 | 4458–4596 | Types | +57 | −0 |
| 104 | 3345–3350 | 4598–4604 | Types | +1 | −0 |
| 105 | 3367–3374 | 4621–4631 | Types | +3 | −0 |
| 106 | 3377–3397 | 4634–4664 | Types | +10 | −0 |
| 107 | 3401–3413 | 4668–4687 | Types | +7 | −0 |
| 108 | 3420–3432 | 4694–4712 | Types | +6 | −0 |
| 109 | 3434–3440 | 4714–4722 | Types | +2 | −0 |
| 110 | 3444–3467 | 4726–4757 | Types | +8 | −0 |
| 111 | 3472–3491 | 4762–4793 | Types | +12 | −0 |
| 112 | 3496–3524 | 4798–4838 | Types | +12 | −0 |
| 113 | 3533–3614 | 4847–4985 | Types | +57 | −0 |
| 114 | 3616–3630 | 4987–5008 | Types | +7 | −0 |
| 115 | 3640–3648 | 5018–5028 | Types | +2 | −0 |
| 116 | 3656–3670 | 5036–5053 | Types | +3 | −0 |
| 117 | 3677–3686 | 5060–5072 | Types | +3 | −0 |
| 118 | 3692–3703 | 5078–5095 | Types | +6 | −0 |
| 119 | 3706–3740 | 5098–5145 | Types | +13 | −0 |
| 120 | 3745–3765 | 5150–5176 | Types | +6 | −0 |
| 121 | 3769–3780 | 5180–5195 | Types | +4 | −0 |
| 122 | 3784–3866 | 5199–5337 | Types | +56 | −0 |
| 123 | 3871–3883 | 5342–5358 | Types | +4 | −0 |
| 124 | 3888–3938 | 5363–5441 | Types | +28 | −0 |
| 125 | 3952–3957 | 5455–5461 | Types | +1 | −0 |
| 126 | 3972–4059 | 5476–5609 | Types | +46 | −0 |
| 127 | 4063–4074 | 5613–5626 | Types | +2 | −0 |
| 128 | 4079–4094 | 5631–5654 | Types | +8 | −0 |
| 129 | 4098–4121 | 5658–5688 | Types | +7 | −0 |
| 130 | 4123–4144 | 5690–5722 | Types | +11 | −0 |
| 131 | 4152–4188 | 5730–5783 | Types | +17 | −0 |
| 132 | 4196–4204 | 5791–5801 | Types | +2 | −0 |
| 133 | 4212–4227 | 5809–5832 | Types | +8 | −0 |
| 134 | 4235–4319 | 5840–5960 | Types | +36 | −0 |
| 135 | 4322–4327 | 5963–5969 | Types | +1 | −0 |
| 136 | 4331–4343 | 5973–5990 | Types | +5 | −0 |
| 137 | 4354–4399 | 6001–6059 | Types | +13 | −0 |
| 138 | 4404–4417 | 6064–6082 | Types | +5 | −0 |
| 139 | 4430–4446 | 6095–6118 | Types | +7 | −0 |
| 140 | 4454–4463 | 6126–6140 | Types | +5 | −0 |
| 141 | 4475–4480 | 6152–6158 | Types | +1 | −0 |
| 142 | 4484–4496 | 6162–6179 | Types | +5 | −0 |
| 143 | 4498–4515 | 6181–6205 | Types | +7 | −0 |
| 144 | 4517–4528 | 6207–6224 | Types | +6 | −0 |
| 145 | 4540–4558 | 6236–6263 | Types | +9 | −0 |
| 146 | 4560–4585 | 6265–6299 | Types | +9 | −0 |
| 147 | 4588–4597 | 6302–6313 | Types | +2 | −0 |
| 148 | 4622–4627 | 6338–6344 | Types | +1 | −0 |
| 149 | 4636–4642 | 6353–6361 | Types | +2 | −0 |
| 150 | 4652–4662 | 6371–6384 | Types | +3 | −0 |
| 151 | 4667–4674 | 6389–6398 | Types | +2 | −0 |
| 152 | 4688–4693 | 6412–6418 | Types | +1 | −0 |
| 153 | 4696–4705 | 6421–6433 | Types | +3 | −0 |
| 154 | 4707–4712 | 6435–6441 | Types | +1 | −0 |
| 155 | 4721–4768 | 6450–6517 | Types | +20 | −0 |
| 156 | 4770–4775 | 6519–6525 | Types | +1 | −0 |
| 157 | 4777–4796 | 6527–6551 | Types | +5 | −0 |
| 158 | 4802–4812 | 6557–6569 | Types | +2 | −0 |
| 159 | 4830–4896 | 6587–6703 | Types | +50 | −0 |
| 160 | 4898–4914 | 6705–6727 | Types | +6 | −0 |
| 161 | 4950–4955 | 6763–6769 | Types | +1 | −0 |
| 162 | 4960–4972 | 6774–6790 | Types | +4 | −0 |
| 163 | 4977–4993 | 6795–6815 | Types | +4 | −0 |
| 164 | 5010–5018 | 6832–6844 | Types | +4 | −0 |
| 165 | 5022–5105 | 6848–6989 | Types | +58 | −0 |
| 166 | 5108–5128 | 6992–7022 | Types | +10 | −0 |
| 167 | 5132–5146 | 7026–7045 | Types | +5 | −0 |
| 168 | 5150–5166 | 7049–7072 | Types | +7 | −0 |
| 169 | 5171–5223 | 7077–7153 | Types | +24 | −0 |
| 170 | 5229–5242 | 7159–7177 | Types | +5 | −0 |
| 171 | 5249–5254 | 7184–7190 | Types | +1 | −0 |
| 172 | 5271–5276 | 7207–7213 | Types | +1 | −0 |
| 173 | 5285–5294 | 7222–7234 | Types | +3 | −0 |
| 174 | 5296–5313 | 7236–7260 | Types | +7 | −0 |
| 175 | 5318–5405 | 7265–7411 | Types | +59 | −0 |
| 176 | 5413–5483 | 7419–7526 | Types | +37 | −0 |
| 177 | 5489–5505 | 7532–7554 | Types | +6 | −0 |
| 178 | 5510–5535 | 7559–7593 | Types | +9 | −0 |
| 179 | 5539–5549 | 7597–7611 | Types | +4 | −0 |
| 180 | 5551–5564 | 7613–7630 | Types | +4 | −0 |
| 181 | 5566–5573 | 7632–7641 | Types | +2 | −0 |
| 182 | 5576–5581 | 7644–7650 | Types | +1 | −0 |
| 183 | 5583–5615 | 7652–7697 | Types | +13 | −0 |
| 184 | 5618–5632 | 7700–7722 | Types | +8 | −0 |
| 185 | 5635–5685 | 7725–7796 | Types | +21 | −0 |
| 186 | 5693–5722 | 7804–7852 | Types | +19 | −0 |
| 187 | 5727–5760 | 7857–7903 | Types | +13 | −0 |
| 188 | 5767–5783 | 7910–7933 | Types | +7 | −0 |
| 189 | 5803–5811 | 7953–7963 | Types | +2 | −0 |
| 190 | 5834–5869 | 7986–8040 | Types | +19 | −0 |
| 191 | 5876–5912 | 8047–8098 | Types | +15 | −0 |
| 192 | 5936–5943 | 8122–8131 | Types | +2 | −0 |
| 193 | 5952–5962 | 8140–8154 | Types | +4 | −0 |
| 194 | 5980–5991 | 8172–8189 | Types | +6 | −0 |
| 195 | 6004–6028 | 8202–8235 | Types | +9 | −0 |
| 196 | 6036–6042 | 8243–8251 | Types | +2 | −0 |
| 197 | 6056–6070 | 8265–8287 | Types | +8 | −0 |
| 198 | 6073–6088 | 8290–8313 | Types | +8 | −0 |
| 199 | 6103–6172 | 8328–8427 | Types | +30 | −0 |
| 200 | 6175–6196 | 8430–8460 | Types | +9 | −0 |
| 201 | 6198–6203 | 8462–8468 | Types | +1 | −0 |
| 202 | 6209–6230 | 8474–8503 | Types | +8 | −0 |
| 203 | 6234–6254 | 8507–8535 | Types | +8 | −0 |
| 204 | 6257–6262 | 8538–8544 | Types | +1 | −0 |
| 205 | 6273–6320 | 8555–8619 | Types | +17 | −0 |
| 206 | 6327–6336 | 8626–8639 | Types | +4 | −0 |
| 207 | 6339–6344 | 8642–8648 | Types | +1 | −0 |
| 208 | 6364–6395 | 8668–8713 | Types | +14 | −0 |
| 209 | 6403–6434 | 8721–8765 | Types | +13 | −0 |
| 210 | 6442–6450 | 8773–8783 | Types | +2 | −0 |
| 211 | 6460–6483 | 8793–8823 | Types | +7 | −0 |
| 212 | 6487–6520 | 8827–8871 | Types | +11 | −0 |
| 213 | 6522–6527 | 8873–8879 | Types | +1 | −0 |
| 214 | 6530–6564 | 8882–8932 | Types | +16 | −0 |
| 215 | 6567–6592 | 8935–8969 | Types | +9 | −0 |
| 216 | 6594–6619 | 8971–9004 | Types | +8 | −0 |
| 217 | 6628–6642 | 9013–9034 | Types | +7 | −0 |
| 218 | 6649–6658 | 9041–9053 | Types | +3 | −0 |
| 219 | 6664–6680 | 9059–9081 | Types | +6 | −0 |
| 220 | 6695–6700 | 9096–9102 | Types | +1 | −0 |
| 221 | 6703–6708 | 9105–9111 | Types | +1 | −0 |
| 222 | 6713–6720 | 9116–9125 | Types | +2 | −0 |
| 223 | 6723–6742 | 9128–9153 | Types | +6 | −0 |
| 224 | 6756–6771 | 9167–9187 | Types | +5 | −0 |
| 225 | 6781–6801 | 9197–9225 | Types | +8 | −0 |
| 226 | 6806–6817 | 9230–9246 | Types | +5 | −0 |
| 227 | 6820–6836 | 9249–9272 | Types | +7 | −0 |
| 228 | 6842–6860 | 9278–9305 | Types | +9 | −0 |
| 229 | 6867–6892 | 9312–9350 | Types | +13 | −0 |
| 230 | 6897–6902 | 9355–9361 | Types | +1 | −0 |
| 231 | 6914–6922 | 9373–9383 | Types | +2 | −0 |
| 232 | 6930–6938 | 9391–9403 | Types | +4 | −0 |
| 233 | 6942–6987 | 9407–9481 | Types | +29 | −0 |
| 234 | 6995–7025 | 9489–9533 | Types | +14 | −0 |
| 235 | 7032–7069 | 9540–9589 | Types | +12 | −0 |
| 236 | 7072–7096 | 9592–9628 | Types | +12 | −0 |
| 237 | 7100–7117 | 9632–9656 | Types | +7 | −0 |
| 238 | 7127–7144 | 9666–9690 | Types | +7 | −0 |
| 239 | 7146–7155 | 9692–9703 | Types | +2 | −0 |
| 240 | 7160–7172 | 9708–9725 | Types | +5 | −0 |
| 241 | 7180–7195 | 9733–9751 | Types | +3 | −0 |
| 242 | 7200–7220 | 9756–9788 | Types | +12 | −0 |
| 243 | 7223–7267 | 9791–9851 | Types | +16 | −0 |
| 244 | 7274–7289 | 9858–9879 | Types | +6 | −0 |
| 245 | 7297–7302 | 9887–9893 | Types | +1 | −0 |
| 246 | 7311–7326 | 9902–9926 | Types | +9 | −0 |
| 247 | 7328–7333 | 9928–9934 | Types | +1 | −0 |
| 248 | 7335–7340 | 9936–9942 | Types | +1 | −0 |
| 249 | 7362–7367 | 9964–9970 | Types | +1 | −0 |
| 250 | 7374–7403 | 9977–10022 | Types | +16 | −0 |
| 251 | 7409–7414 | 10028–10034 | Types | +1 | −0 |
| 252 | 7431–7493 | 10051–10147 | Types | +34 | −0 |
| 253 | 7504–7540 | 10158–10209 | Types | +15 | −0 |
| 254 | 7543–7574 | 10212–10261 | Types | +18 | −0 |
| 255 | 7580–7585 | 10267–10273 | Types | +1 | −0 |
| 256 | 7587–7592 | 10275–10281 | Types | +1 | −0 |
| 257 | 7636–7651 | 10325–10343 | Types | +3 | −0 |
| 258 | 7653–7658 | 10345–10351 | Types | +1 | −0 |
| 259 | 7662–7682 | 10355–10383 | Types | +8 | −0 |
| 260 | 7687–7720 | 10388–10432 | Types | +11 | −0 |
| 261 | 7725–7741 | 10437–10460 | Types | +7 | −0 |
| 262 | 7747–7755 | 10466–10477 | Types | +3 | −0 |
| 263 | 7760–7765 | 10482–10488 | Types | +1 | −0 |
| 264 | 7774–7790 | 10497–10520 | Types | +7 | −0 |
| 265 | 7796–7815 | 10526–10552 | Types | +7 | −0 |
| 266 | 7817–7822 | 10554–10560 | Types | +1 | −0 |
| 267 | 7832–7837 | 10570–10576 | Types | +1 | −0 |
| 268 | 7842–7870 | 10581–10617 | Types | +8 | −0 |
| 269 | 7881–7897 | 10628–10650 | Types | +6 | −0 |
| 270 | 7907–7912 | 10660–10666 | Types | +1 | −0 |
| 271 | 7916–7921 | 10670–10676 | Types | +1 | −0 |
| 272 | 7923–7938 | 10678–10697 | Types | +4 | −0 |
| 273 | 7948–7963 | 10707–10730 | Types | +8 | −0 |
| 274 | 7971–7991 | 10738–10766 | Types | +8 | −0 |
| 275 | 7999–8018 | 10774–10797 | Types | +4 | −0 |
| 276 | 8025–8038 | 10804–10822 | Types | +5 | −0 |
| 277 | 8040–8050 | 10824–10836 | Types | +2 | −0 |
| 278 | 8055–8070 | 10841–10864 | Types | +8 | −0 |
| 279 | 8072–8077 | 10866–10872 | Types | +1 | −0 |
| 280 | 8088–8093 | 10883–10889 | Types | +1 | −0 |
| 281 | 8108–8113 | 10904–10910 | Types | +1 | −0 |
| 282 | 8120–8136 | 10917–10942 | Types | +9 | −0 |
| 283 | 8139–8150 | 10945–10958 | Types | +2 | −0 |
| 284 | 8160–8174 | 10968–10986 | Types | +4 | −0 |
| 285 | 8177–8187 | 10989–11001 | Types | +2 | −0 |
| 286 | 8191–8196 | 11005–11011 | Types | +1 | −0 |
| 287 | 8198–8203 | 11013–11019 | Types | +1 | −0 |
| 288 | 8217–8240 | 11033–11063 | Types | +7 | −0 |
| 289 | 8251–8306 | 11074–11162 | Types | +33 | −0 |
| 290 | 8340–8363 | 11196–11229 | Types | +10 | −0 |
| 291 | 8365–8370 | 11231–11237 | Types | +1 | −0 |
| 292 | 8375–8391 | 11242–11264 | Types | +6 | −0 |
| 293 | 8401–8416 | 11274–11297 | Types | +8 | −0 |
| 294 | 8423–8432 | 11304–11318 | Types | +5 | −0 |
| 295 | 8437–8442 | 11323–11329 | Types | +1 | −0 |
| 296 | 8461–8472 | 11348–11363 | Types | +4 | −0 |
| 297 | 8480–8494 | 11371–11393 | Types | +8 | −0 |
| 298 | 8497–8541 | 11396–11458 | Types | +18 | −0 |
| 299 | 8560–8578 | 11477–11500 | Types | +5 | −0 |
| 300 | 8583–8603 | 11505–11529 | Types | +4 | −0 |
| 301 | 8613–8649 | 11539–11593 | Types | +18 | −0 |
| 302 | 8660–8667 | 11604–11614 | Types | +3 | −0 |
| 303 | 8676–8704 | 11623–11670 | Types | +19 | −0 |
| 304 | 8706–8733 | 11672–11716 | Types | +17 | −0 |
| 305 | 8743–8748 | 11726–11732 | Types | +1 | −0 |
| 306 | 8753–8758 | 11737–11743 | Types | +1 | −0 |
| 307 | 8765–8796 | 11750–11799 | Types | +18 | −0 |
| 308 | 8812–8882 | 11815–11925 | Types | +40 | −0 |
| 309 | 8906–8911 | 11949–11955 | Types | +1 | −0 |
| 310 | 8929–8938 | 11973–11986 | Types | +4 | −0 |
| 311 | 8941–8959 | 11989–12016 | Types | +9 | −0 |
| 312 | 8978–8983 | 12035–12041 | Types | +1 | −0 |
| 313 | 8997–9006 | 12055–12069 | Types | +5 | −0 |
| 314 | 9013–9035 | 12076–12104 | Types | +6 | −0 |
| 315 | 9041–9046 | 12110–12116 | Types | +1 | −0 |
| 316 | 9052–9065 | 12122–12140 | Types | +5 | −0 |
| 317 | 9077–9082 | 12152–12158 | Types | +1 | −0 |
| 318 | 9084–9100 | 12160–12181 | Types | +5 | −0 |
| 319 | 9112–9117 | 12193–12199 | Types | +1 | −0 |
| 320 | 9123–9128 | 12205–12211 | Types | +1 | −0 |
| 321 | 9130–9189 | 12213–12319 | Types | +47 | −0 |
| 322 | 9196–9211 | 12326–12346 | Types | +5 | −0 |
| 323 | 9213–9226 | 12348–12365 | Types | +4 | −0 |
| 324 | 9229–9234 | 12368–12374 | Types | +1 | −0 |
| 325 | 9241–9254 | 12381–12399 | Types | +5 | −0 |
| 326 | 9257–9268 | 12402–12415 | Types | +2 | −0 |
| 327 | 9273–9297 | 12420–12450 | Types | +6 | −0 |
| 328 | 9302–9307 | 12455–12461 | Types | +1 | −0 |
| 329 | 9319–9333 | 12473–12494 | Types | +7 | −0 |
| 330 | 9335–9360 | 12496–12530 | Types | +9 | −0 |
| 331 | 9366–9379 | 12536–12554 | Types | +5 | −0 |
| 332 | 9404–9426 | 12579–12619 | Types | +18 | −0 |
| 333 | 9431–9528 | 12624–12788 | Types | +67 | −0 |
| 334 | 9566–9583 | 12826–12849 | Types | +6 | −0 |
| 335 | 9589–9602 | 12855–12873 | Types | +5 | −0 |
| 336 | 9607–9617 | 12878–12890 | Types | +2 | −0 |
| 337 | 9635–9640 | 12908–12914 | Types | +1 | −0 |
| 338 | 9645–9650 | 12919–12925 | Types | +1 | −0 |
| 339 | 9655–9670 | 12930–12950 | Types | +5 | −0 |
| 340 | 9680–9753 | 12960–13088 | Types | +55 | −0 |
| 341 | 9770–9785 | 13105–13129 | Types | +9 | −0 |
| 342 | 9793–9813 | 13137–13165 | Types | +8 | −0 |
| 343 | 9820–9852 | 13172–13212 | Types | +8 | −0 |
| 344 | 9857–9862 | 13217–13223 | Types | +1 | −0 |
| 345 | 9869–9898 | 13230–13270 | Types | +11 | −0 |
| 346 | 9910–9920 | 13282–13294 | Types | +2 | −0 |
| 347 | 9925–9940 | 13299–13319 | Types | +5 | −0 |
| 348 | 9942–10001 | 13321–13427 | Types | +47 | −0 |
| 349 | 10008–10023 | 13434–13458 | Types | +9 | −0 |
| 350 | 10036–10046 | 13471–13483 | Types | +2 | −0 |
| 351 | 10048–10063 | 13485–13506 | Types | +6 | −0 |
| 352 | 10069–10082 | 13512–13528 | Types | +3 | −0 |
| 353 | 10085–10090 | 13531–13537 | Types | +1 | −0 |
| 354 | 10114–10119 | 13561–13567 | Types | +1 | −0 |
| 355 | 10124–10129 | 13572–13578 | Types | +1 | −0 |
| 356 | 10148–10153 | 13597–13603 | Types | +1 | −0 |
| 357 | 10160–10165 | 13610–13616 | Types | +1 | −0 |
| 358 | 10186–10195 | 13637–13649 | Types | +3 | −0 |
| 359 | 10216–10231 | 13670–13688 | Types | +3 | −0 |
| 360 | 10242–10257 | 13699–13717 | Types | +3 | −0 |
| 361 | 10263–10270 | 13723–13732 | Types | +2 | −0 |
| 362 | 10272–10277 | 13734–13740 | Types | +1 | −0 |
| 363 | 10298–10313 | 13761–13782 | Types | +6 | −0 |
| 364 | 10315–10347 | 13784–13826 | Types | +10 | −0 |
| 365 | 10352–10367 | 13831–13849 | Types | +3 | −0 |
| 366 | 10377–10382 | 13859–13865 | Types | +1 | −0 |
| 367 | 10389–10400 | 13872–13887 | Types | +4 | −0 |
| 368 | 10403–10408 | 13890–13896 | Types | +1 | −0 |
| 369 | 10412–10417 | 13900–13906 | Types | +1 | −0 |
| 370 | 10432–10454 | 13921–13951 | Types | +8 | −0 |
| 371 | 10464–10474 | 13961–13973 | Types | +2 | −0 |
| 372 | 10484–10489 | 13983–13989 | Types | +1 | −0 |
| 373 | 10520–10526 | 14020–14026 | Client | +1 | −1 |
| 374 | 10528–10546 | 14028–14046 | Client | +4 | −4 |
| 375 | 10548–10554 | 14048–14054 | Client | +1 | −1 |
| 376 | 10556–10566 | 14056–14066 | Client | +2 | −2 |
| 377 | 10568–10578 | 14068–14078 | Client | +2 | −2 |
| 378 | 10588–10594 | 14088–14094 | Client | +1 | −1 |
| 379 | 10608–10614 | 14108–14114 | Client | +1 | −1 |
| 380 | 10652–10658 | 14152–14158 | Client | +1 | −1 |
| 381 | 10680–10686 | 14180–14186 | Client | +1 | −1 |
| 382 | 10704–10722 | 14204–14222 | Client | +4 | −4 |
| 383 | 10728–10734 | 14228–14234 | Client | +1 | −1 |
| 384 | 10736–10750 | 14236–14250 | Client | +3 | −3 |
| 385 | 10768–10774 | 14268–14274 | Client | +1 | −1 |
| 386 | 10792–10798 | 14292–14298 | Client | +1 | −1 |
| 387 | 10820–10826 | 14320–14326 | Client | +1 | −1 |
| 388 | 10828–10834 | 14328–14334 | Client | +1 | −1 |
| 389 | 10836–10842 | 14336–14342 | Client | +1 | −1 |
| 390 | 10848–10854 | 14348–14354 | Client | +1 | −1 |
| 391 | 10888–10894 | 14388–14394 | Client | +1 | −1 |
| 392 | 10900–10910 | 14400–14410 | Client | +2 | −2 |
| 393 | 10916–10930 | 14416–14430 | Client | +3 | −3 |
| 394 | 10936–10942 | 14436–14442 | Client | +1 | −1 |
| 395 | 10944–10950 | 14444–14450 | Client | +1 | −1 |
| 396 | 10960–10966 | 14460–14466 | Client | +1 | −1 |
| 397 | 10988–10994 | 14488–14494 | Client | +1 | −1 |
| 398 | 10996–11006 | 14496–14506 | Client | +2 | −2 |
| 399 | 11008–11014 | 14508–14514 | Client | +1 | −1 |
| 400 | 11020–11030 | 14520–14530 | Client | +2 | −2 |
| 401 | 11032–11038 | 14532–14538 | Client | +1 | −1 |
| 402 | 11044–11054 | 14544–14554 | Client | +2 | −2 |
| 403 | 11056–11062 | 14556–14562 | Client | +1 | −1 |
| 404 | 11068–11078 | 14568–14578 | Client | +2 | −2 |
| 405 | 11080–11086 | 14580–14586 | Client | +1 | −1 |
| 406 | 11092–11102 | 14592–14602 | Client | +2 | −2 |
| 407 | 11104–11110 | 14604–14610 | Client | +1 | −1 |
| 408 | 11116–11122 | 14616–14622 | Client | +1 | −1 |
| 409 | 11128–11134 | 14628–14634 | Client | +1 | −1 |
| 410 | 11136–11142 | 14636–14642 | Client | +1 | −1 |
| 411 | 11168–11174 | 14668–14674 | Client | +1 | −1 |
| 412 | 11192–11198 | 14692–14698 | Client | +1 | −1 |
| 413 | 11204–11214 | 14704–14714 | Client | +2 | −2 |
| 414 | 11216–11222 | 14716–14722 | Client | +1 | −1 |
| 415 | 11236–11242 | 14736–14742 | Client | +1 | −1 |
| 416 | 11244–11250 | 14744–14750 | Client | +1 | −1 |
| 417 | 11256–11270 | 14756–14770 | Client | +3 | −3 |
| 418 | 11272–11278 | 14772–14778 | Client | +1 | −1 |
| 419 | 11284–11294 | 14784–14794 | Client | +2 | −2 |
| 420 | 11296–11302 | 14796–14802 | Client | +1 | −1 |
| 421 | 11308–11318 | 14808–14818 | Client | +2 | −2 |
| 422 | 11320–11326 | 14820–14826 | Client | +1 | −1 |
| 423 | 11332–11342 | 14832–14842 | Client | +2 | −2 |
| 424 | 11348–11354 | 14848–14854 | Client | +1 | −1 |
| 425 | 11360–11366 | 14860–14866 | Client | +1 | −1 |
| 426 | 11368–11374 | 14868–14874 | Client | +1 | −1 |
| 427 | 11380–11386 | 14880–14886 | Client | +1 | −1 |
| 428 | 11404–11414 | 14904–14914 | Client | +2 | −2 |
| 429 | 11444–11450 | 14944–14950 | Client | +1 | −1 |
| 430 | 11464–11470 | 14964–14970 | Client | +1 | −1 |
| 431 | 11476–11482 | 14976–14982 | Client | +1 | −1 |
| 432 | 11528–11542 | 15028–15042 | Client | +3 | −3 |
| 433 | 11608–11614 | 15108–15114 | Client | +1 | −1 |
| 434 | 11636–11642 | 15136–15142 | Client | +1 | −1 |
| 435 | 11660–11666 | 15160–15166 | Client | +1 | −1 |
| 436 | 11668–11678 | 15168–15178 | Client | +2 | −2 |
| 437 | 11680–11686 | 15180–15186 | Client | +1 | −1 |
| 438 | 11704–11714 | 15204–15214 | Client | +2 | −2 |
| 439 | 11720–11738 | 15220–15238 | Client | +4 | −4 |
| 440 | 11740–11746 | 15240–15246 | Client | +1 | −1 |
| 441 | 11752–11762 | 15252–15262 | Client | +2 | −2 |
| 442 | 11764–11770 | 15264–15270 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- shopify.admin/old/ballerinax_shopify.admin.bal.txt	2026-08-12 12:57:30
+++ shopify.admin/new/ballerinax_shopify.admin.bal.txt	2026-08-12 13:19:19
@@ -154,13 +154,20 @@
 
 
 type AdminapiapiVersionmarketingEventsJsonMarketingEvent record {
+    @jsondata:Name {value: "event_type"}
     string eventType?;
+    @jsondata:Name {value: "utm_campaign"}
     string utmCampaign?;
+    @jsondata:Name {value: "utm_medium"}
     string utmMedium?;
     boolean paid?;
+    @jsondata:Name {value: "started_at"}
     string startedAt?;
+    @jsondata:Name {value: "marketing_channel"}
     string marketingChannel?;
+    @jsondata:Name {value: "referring_domain"}
     string referringDomain?;
+    @jsondata:Name {value: "utm_source"}
     string utmSource?;
 };
 
@@ -172,43 +179,74 @@
 
 type AbandonedCheckoutsCheckouts record {
     anydata? note?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "billing_address"}
     ReopenCloseOrderOrderBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     AbandonedCheckoutsLineItems[] lineItems?;
     anydata? 'source?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "buyer_accepts_marketing"}
     boolean buyerAcceptsMarketing?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "total_weight"}
     int totalWeight?;
+    @jsondata:Name {value: "landing_site"}
     anydata? landingSite?;
+    @jsondata:Name {value: "source_identifier"}
     anydata? sourceIdentifier?;
+    @jsondata:Name {value: "total_discounts"}
     string totalDiscounts?;
+    @jsondata:Name {value: "referring_site"}
     anydata? referringSite?;
+    @jsondata:Name {value: "tax_lines"}
     AbandonedCheckoutsTaxLines[] taxLines?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "customer_locale"}
     anydata? customerLocale?;
     string currency?;
+    @jsondata:Name {value: "abandoned_checkout_url"}
     string abandonedCheckoutUrl?;
     int id?;
+    @jsondata:Name {value: "shipping_address"}
     ReopenCloseOrderOrderBillingAddress|() shippingAddress?;
     string email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "closed_at"}
     anydata? closedAt?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
     string token?;
+    @jsondata:Name {value: "completed_at"}
     string? completedAt?;
+    @jsondata:Name {value: "shipping_lines"}
     AbandonedCheckoutsShippingLines[] shippingLines?;
     anydata? phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     ReopenCloseOrderOrderNoteAttributes[] noteAttributes?;
     string name?;
+    @jsondata:Name {value: "cart_token"}
     string cartToken?;
+    @jsondata:Name {value: "discount_codes"}
     anydata[] discountCodes?;
     string? gateway?;
     AbandonedCheckoutsCustomer customer?;
@@ -222,45 +260,68 @@
     string city?;
     string address1?;
     decimal latitude?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     string province?;
     string phone?;
     string name?;
     anydata? company?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     decimal longitude?;
 };
 
 
 type AbandonedCheckoutsLineItems record {
+    @jsondata:Name {value: "variant_title"}
     string? variantTitle?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
     string title?;
+    @jsondata:Name {value: "origin_location_id"}
     anydata? originLocationId?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
     string price?;
     string vendor?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     int grams?;
     string? sku?;
     int 'key?;
+    @jsondata:Name {value: "line_price"}
     string linePrice?;
+    @jsondata:Name {value: "unit_price_measurement"}
     anydata? unitPriceMeasurement?;
+    @jsondata:Name {value: "compare_at_price"}
     anydata? compareAtPrice?;
     int quantity?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
+    @jsondata:Name {value: "variant_price"}
     anydata? variantPrice?;
+    @jsondata:Name {value: "country_hs_codes"}
     anydata[] countryHsCodes?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "destination_location_id"}
     anydata? destinationLocationId?;
+    @jsondata:Name {value: "province_code_of_origin"}
     anydata? provinceCodeOfOrigin?;
+    @jsondata:Name {value: "country_code_of_origin"}
     anydata? countryCodeOfOrigin?;
+    @jsondata:Name {value: "harmonized_system_code"}
     anydata? harmonizedSystemCode?;
+    @jsondata:Name {value: "applied_discounts"}
     anydata[] appliedDiscounts?;
     anydata? properties?;
 };
@@ -279,6 +340,7 @@
     string id?;
     string 'source?;
     string title?;
+    @jsondata:Name {value: "applied_discounts"}
     anydata[] appliedDiscounts?;
 };
 
@@ -290,28 +352,45 @@
 
 
 type AbandonedCheckoutsCustomer record {
+    @jsondata:Name {value: "total_spent"}
     string totalSpent?;
     anydata? note?;
+    @jsondata:Name {value: "last_order_name"}
     string lastOrderName?;
+    @jsondata:Name {value: "last_order_id"}
     int lastOrderId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "multipass_identifier"}
     anydata? multipassIdentifier?;
+    @jsondata:Name {value: "verified_email"}
     boolean verifiedEmail?;
+    @jsondata:Name {value: "accepts_marketing_updated_at"}
     string acceptsMarketingUpdatedAt?;
     string tags?;
+    @jsondata:Name {value: "orders_count"}
     int ordersCount?;
+    @jsondata:Name {value: "default_address"}
     ReopenCloseOrderOrderCustomerDefaultAddress defaultAddress?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "accepts_marketing"}
     boolean acceptsMarketing?;
     anydata? phone?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "tax_exemptions"}
     anydata[] taxExemptions?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "marketing_opt_in_level"}
     anydata? marketingOptInLevel?;
     string state?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
@@ -323,22 +402,29 @@
     string address2?;
     string city?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     anydata? lastName?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     boolean default?;
     string province?;
     string phone?;
+    @jsondata:Name {value: "country_name"}
     string countryName?;
     string name?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
+    @jsondata:Name {value: "first_name"}
     anydata? firstName?;
 };
 
 
 type FulfillmentRequestRejectJsonBody record {
+    @jsondata:Name {value: "fulfillment_request"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdfulfillmentRequestrejectJsonFulfillmentRequest fulfillmentRequest?;
 };
 
@@ -349,11 +435,16 @@
 
 
 type ImageAssetAsset record {
+    @jsondata:Name {value: "public_url"}
     string? publicUrl?;
+    @jsondata:Name {value: "content_type"}
     string contentType?;
     int size?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "theme_id"}
     int themeId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'key?;
 };
@@ -367,57 +458,78 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
 
 
 type ProductListingAppResponse record {
+    @jsondata:Name {value: "product_listing"}
     ProductListingAppResponseProductListing productListing?;
 };
 
 
 type ProductListingAppResponseProductListing record {
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     anydata[] images?;
     boolean available?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     ProductListingAppResponseProductListingVariants[] variants?;
     string title?;
     string tags?;
+    @jsondata:Name {value: "product_type"}
     string productType?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string vendor?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     ProductListingAppResponseProductListingOptions[] options?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
 };
 
 
 type ProductListingAppResponseProductListingVariants record {
+    @jsondata:Name {value: "formatted_price"}
     string formattedPrice?;
+    @jsondata:Name {value: "inventory_quantity"}
     int inventoryQuantity?;
+    @jsondata:Name {value: "compare_at_price"}
     anydata? compareAtPrice?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
+    @jsondata:Name {value: "inventory_management"}
     string inventoryManagement?;
     boolean taxable?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "option_values"}
     ProductListingAppResponseProductListingOptionValues[] optionValues?;
     boolean available?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     decimal weight?;
     string title?;
+    @jsondata:Name {value: "inventory_policy"}
     string inventoryPolicy?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "weight_unit"}
     string weightUnit?;
     string price?;
     int id?;
     int position?;
     int grams?;
+    @jsondata:Name {value: "image_id"}
     anydata? imageId?;
     string? sku?;
     string barcode?;
@@ -426,12 +538,14 @@
 
 type ProductListingAppResponseProductListingOptionValues record {
     string name?;
+    @jsondata:Name {value: "option_id"}
     int optionId?;
     string value?;
 };
 
 
 type ProductListingAppResponseProductListingOptions record {
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     string[] values?;
     string name?;
@@ -443,12 +557,14 @@
 
 type PresentmentPrices record {
     # A list of the variant's presentment prices and compare-at prices in each of the shop's enabled presentment currencies
+    @jsondata:Name {value: "presentment_prices"}
     PresentmentPrice[] presentmentPrices?;
 };
 
 # The variant's presentment prices and compare-at prices in each of the shop's enabled presentment currencies
 
 type PresentmentPrice record {
+    @jsondata:Name {value: "compare_at_price"}
     Price compareAtPrice?;
     # The price object
     Price price?;
@@ -460,6 +576,7 @@
     # The variant's price or compare-at price in the presentment currency
     string amount?;
     # The three-letter code (ISO 4217 format) for one of the shop's enabled presentment currencies
+    @jsondata:Name {value: "currency_code"}
     string currencyCode?;
 };
 
@@ -467,12 +584,16 @@
 
 type RetrieveACountOfFulfillmentsAssociatedWithASpecificOrderQueries record {
     # Count fulfillments created after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Count fulfillments created before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Count fulfillments last updated before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Count fulfillments last updated after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
 };
 
@@ -483,82 +604,117 @@
 
 
 type CreateFulfillmentOrderFulfillment record {
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "line_items"}
     CreateFulfillmentOrderFulfillmentLineItems[] lineItems?;
+    @jsondata:Name {value: "tracking_company"}
     string trackingCompany?;
+    @jsondata:Name {value: "tracking_urls"}
     string[] trackingUrls?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string 'service?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string name?;
+    @jsondata:Name {value: "tracking_number"}
     string trackingNumber?;
     record {|anydata...;|} receipt?;
     int id?;
+    @jsondata:Name {value: "tracking_numbers"}
     string[] trackingNumbers?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "tracking_url"}
     string trackingUrl?;
+    @jsondata:Name {value: "shipment_status"}
     anydata? shipmentStatus?;
     string status?;
 };
 
 
 type CreateFulfillmentOrderFulfillmentLineItems record {
+    @jsondata:Name {value: "variant_title"}
     string? variantTitle?;
+    @jsondata:Name {value: "fulfillment_status"}
     string fulfillmentStatus?;
+    @jsondata:Name {value: "total_discount"}
     string totalDiscount?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "total_discount_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalDiscountSet?;
     string title?;
+    @jsondata:Name {value: "product_exists"}
     boolean productExists?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
     string price?;
     anydata? vendor?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     int id?;
     int grams?;
     string? sku?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
     int quantity?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
+    @jsondata:Name {value: "discount_allocations"}
     anydata[] discountAllocations?;
+    @jsondata:Name {value: "variant_inventory_management"}
     anydata? variantInventoryManagement?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string name?;
+    @jsondata:Name {value: "price_set"}
     ReopenCloseOrderOrderTotalDiscountsSet priceSet?;
     anydata[] properties?;
 };
 
 
 type ReopenCloseOrderOrderTotalDiscountSet record {
+    @jsondata:Name {value: "shop_money"}
     ReopenCloseOrderOrderTotalDiscountSetPresentmentMoney shopMoney?;
+    @jsondata:Name {value: "presentment_money"}
     ReopenCloseOrderOrderTotalDiscountSetPresentmentMoney presentmentMoney?;
 };
 
 
 type ReopenCloseOrderOrderTotalDiscountSetPresentmentMoney record {
     string amount?;
+    @jsondata:Name {value: "currency_code"}
     string currencyCode?;
 };
 
 
 type ReopenCloseOrderOrderTotalDiscountsSet record {
+    @jsondata:Name {value: "shop_money"}
     ReopenCloseOrderOrderTotalDiscountsSetPresentmentMoney shopMoney?;
+    @jsondata:Name {value: "presentment_money"}
     ReopenCloseOrderOrderTotalDiscountsSetPresentmentMoney presentmentMoney?;
 };
 
 
 type ReopenCloseOrderOrderTotalDiscountsSetPresentmentMoney record {
     string amount?;
+    @jsondata:Name {value: "currency_code"}
     string currencyCode?;
 };
 
 
 type AdminapiapiVersionthemesthemeIdassetsJsonAsset record {
     string 'key?;
+    @jsondata:Name {value: "source_key"}
     string sourceKey?;
 };
 
@@ -577,35 +733,55 @@
 
 
 type CreateDraftOrder record {
+    @jsondata:Name {value: "draft_order"}
     CreateDraftOrderDraftOrder draftOrder?;
 };
 
 
 type CreateDraftOrderDraftOrder record {
     anydata? note?;
+    @jsondata:Name {value: "applied_discount"}
     record {|anydata...;|}? appliedDiscount?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "billing_address"}
     record {|anydata...;|}? billingAddress?;
+    @jsondata:Name {value: "line_items"}
     CreateDraftOrderDraftOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "tax_lines"}
     CreateDraftOrderDraftOrderTaxLines[] taxLines?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "shipping_address"}
     record {|anydata...;|}? shippingAddress?;
     string? email?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "invoice_sent_at"}
     anydata? invoiceSentAt?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
     string tags?;
+    @jsondata:Name {value: "completed_at"}
     anydata? completedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "note_attributes"}
     anydata[] noteAttributes?;
     string name?;
+    @jsondata:Name {value: "shipping_line"}
     anydata? shippingLine?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
+    @jsondata:Name {value: "invoice_url"}
     string invoiceUrl?;
     record {|anydata...;|}? customer?;
     string status?;
@@ -613,20 +789,29 @@
 
 
 type CreateDraftOrderDraftOrderLineItems record {
+    @jsondata:Name {value: "variant_title"}
     anydata? variantTitle?;
     int quantity?;
+    @jsondata:Name {value: "applied_discount"}
     CreateDraftOrderDraftOrderAppliedDiscount|() appliedDiscount?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
     boolean taxable?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
     boolean custom?;
     string title?;
+    @jsondata:Name {value: "variant_id"}
     anydata? variantId?;
+    @jsondata:Name {value: "tax_lines"}
     CreateDraftOrderDraftOrderTaxLines[] taxLines?;
     string price?;
     anydata? vendor?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "product_id"}
     anydata? productId?;
     string name?;
     int grams?;
@@ -637,6 +822,7 @@
 
 type CreateDraftOrderDraftOrderAppliedDiscount record {
     string amount?;
+    @jsondata:Name {value: "value_type"}
     string valueType?;
     string description?;
     string title?;
@@ -658,13 +844,17 @@
     string city?;
     string address1?;
     anydata? latitude?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     string province?;
     string phone?;
     string name?;
     anydata? company?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     anydata? longitude?;
 };
@@ -672,10 +862,14 @@
 
 type PublishThemeResponseTheme record {
     string role?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "theme_store_id"}
     anydata? themeStoreId?;
     string name?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     boolean processing?;
     int id?;
@@ -684,6 +878,7 @@
 
 
 type ApiVersionApplicationChargesJsonBody record {
+    @jsondata:Name {value: "application_charge"}
     AdminapiapiVersionapplicationChargesJsonApplicationCharge applicationCharge?;
 };
 
@@ -696,6 +891,7 @@
 
 type ReceiveAListOfAllCountriesQueries record {
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show only certain fields, specified by a comma-separated list of field names. 
     string fields?;
@@ -703,22 +899,31 @@
 
 
 type ApiVersionRecurringApplicationChargesJsonBody record {
+    @jsondata:Name {value: "recurring_application_charge"}
     AdminapiapiVersionapplicationChargesJsonApplicationCharge recurringApplicationCharge?;
 };
 
 
 type DisputeEvidenceFiles record {
+    @jsondata:Name {value: "customer_communication_file_id"}
     int customerCommunicationFileId?;
+    @jsondata:Name {value: "refund_policy_file_id"}
     int? refundPolicyFileId?;
+    @jsondata:Name {value: "cancellation_policy_file_id"}
     int? cancellationPolicyFileId?;
+    @jsondata:Name {value: "shipping_documentation_file_id"}
     int shippingDocumentationFileId?;
+    @jsondata:Name {value: "customer_signature_file_id"}
     int customerSignatureFileId?;
+    @jsondata:Name {value: "uncategorized_file_id"}
     int uncategorizedFileId?;
+    @jsondata:Name {value: "service_documentation_file_id"}
     int? serviceDocumentationFileId?;
 };
 
 
 type ProductListingsOptions record {
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     string[] values?;
     string name?;
@@ -728,30 +933,44 @@
 
 
 type ApplicationChargeResultApplicationCharge record {
+    @jsondata:Name {value: "charge_type"}
     anydata? chargeType?;
+    @jsondata:Name {value: "api_client_id"}
     int apiClientId?;
     anydata? test?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string price?;
     string name?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "return_url"}
     string returnUrl?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "decorated_return_url"}
     string decoratedReturnUrl?;
     string status?;
 };
 
 
 type MobilePlatformApplicationsMobilePlatformApplications record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "sha256_cert_fingerprints"}
     anydata[] sha256CertFingerprints?;
+    @jsondata:Name {value: "enabled_app_clips"}
     boolean enabledAppClips?;
+    @jsondata:Name {value: "enabled_universal_or_app_links"}
     boolean enabledUniversalOrAppLinks?;
     int id?;
+    @jsondata:Name {value: "app_clip_application_id"}
     anydata? appClipApplicationId?;
+    @jsondata:Name {value: "enabled_shared_webcredentials"}
     boolean enabledSharedWebcredentials?;
+    @jsondata:Name {value: "application_id"}
     string applicationId?;
     string platform?;
 };
@@ -764,11 +983,13 @@
 
 type AdminapiapiVersionreportsJsonReport record {
     string name?;
+    @jsondata:Name {value: "shopify_ql"}
     string shopifyQl?;
 };
 
 
 type ApiVersionSmartCollectionsJsonBody record {
+    @jsondata:Name {value: "smart_collection"}
     AdminapiapiVersionsmartCollectionsJsonSmartCollection smartCollection?;
 };
 
@@ -793,16 +1014,25 @@
 
 
 type FulfillmentOrdersListFulfillmentOrders record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     FulfillmentOrdersListDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     FulfillmentOrdersListLineItems[] lineItems?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     string[] supportedActions?;
+    @jsondata:Name {value: "assigned_location"}
     FulfillmentOrdersAssignedLocation assignedLocation?;
+    @jsondata:Name {value: "merchant_requests"}
     anydata[] merchantRequests?;
     string status?;
 };
@@ -816,21 +1046,29 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
 
 
 type FulfillmentOrdersListLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
@@ -838,6 +1076,7 @@
 
 type FulfillmentOrdersAssignedLocation record {
     anydata? zip?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     anydata? province?;
     anydata? address2?;
@@ -845,12 +1084,15 @@
     anydata? phone?;
     anydata? address1?;
     string name?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
 };
 
 
 type OriginalFulfillmentOrderSubmittedFulfillmentOrderOutgoingRequests record {
+    @jsondata:Name {value: "sent_at"}
     string sentAt?;
+    @jsondata:Name {value: "request_options"}
     OriginalFulfillmentOrderSubmittedFulfillmentOrderRequestOptions requestOptions?;
     string kind?;
     string message?;
@@ -858,6 +1100,7 @@
 
 
 type OriginalFulfillmentOrderSubmittedFulfillmentOrderRequestOptions record {
+    @jsondata:Name {value: "notify_customer"}
     boolean notifyCustomer?;
 };
 
@@ -868,6 +1111,7 @@
 
 
 type CurrenciesListCurrencies record {
+    @jsondata:Name {value: "rate_updated_at"}
     string rateUpdatedAt?;
     string currency?;
     boolean enabled?;
@@ -887,13 +1131,19 @@
     string? city?;
     string? address1?;
     boolean active?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "province_code"}
     string? provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     string? province?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     anydata? phone?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "country_name"}
     string countryName?;
     string name?;
     int id?;
@@ -905,11 +1155,13 @@
     # Show only certain fields, specified by a comma-separated list of field names. 
     string fields?;
     # Show amounts in the shop currency for the underlying transaction.(default: false) 
+    @http:Query {name: "in_shop_currency"}
     string inShopCurrency?;
 };
 
 
 type DisputeIdDisputeFileUploadsJsonBody record {
+    @jsondata:Name {value: "dispute_file_upload"}
     AdminapiapiVersionshopifyPaymentsdisputesdisputeIddisputeFileUploadsJsonDisputeFileUpload disputeFileUpload?;
 };
 
@@ -918,6 +1170,7 @@
     string filename?;
     string data?;
     string mimetype?;
+    @jsondata:Name {value: "document_type"}
     string documentType?;
 };
 
@@ -925,26 +1178,35 @@
 
 type RetrieveACountOfDiscountCodesForAShopQueries record {
     # Show discount codes used greater than or equal to this value
+    @http:Query {name: "times_used_max"}
     string timesUsedMax?;
     # Show discount codes used less than or equal to this value
+    @http:Query {name: "times_used_min"}
     string timesUsedMin?;
     # Show discount codes with times used
+    @http:Query {name: "times_used"}
     string timesUsed?;
 };
 
 
 type SingleUsageCharge record {
+    @jsondata:Name {value: "usage_charge"}
     SingleUsageChargeUsageCharge usageCharge?;
 };
 
 
 type SingleUsageChargeUsageCharge record {
+    @jsondata:Name {value: "risk_level"}
     decimal riskLevel?;
     string price?;
+    @jsondata:Name {value: "balance_used"}
     decimal balanceUsed?;
+    @jsondata:Name {value: "balance_remaining"}
     decimal balanceRemaining?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string description?;
+    @jsondata:Name {value: "billing_on"}
     anydata? billingOn?;
     string currency?;
     int id?;
@@ -952,12 +1214,15 @@
 
 
 type DraftOrderIdSendInvoiceJsonBody record {
+    @jsondata:Name {value: "draft_order_invoice"}
     record {|anydata...;|} draftOrderInvoice?;
 };
 
 
 type AdminapiapiVersionfulfillmentsfulfillmentIdupdateTrackingJsonFulfillment record {
+    @jsondata:Name {value: "tracking_info"}
     AdminapiapiVersionfulfillmentsfulfillmentIdupdateTrackingJsonFulfillmentTrackingInfo trackingInfo?;
+    @jsondata:Name {value: "notify_customer"}
     boolean notifyCustomer?;
 };
 
@@ -970,47 +1235,73 @@
 
 
 type MoveFulfillmentOrderResponseMovedFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
 
 
 type ModifyDraftOrder record {
+    @jsondata:Name {value: "draft_order"}
     ModifyDraftOrderDraftOrder draftOrder?;
 };
 
 
 type ModifyDraftOrderDraftOrder record {
     string? note?;
+    @jsondata:Name {value: "applied_discount"}
     ModifyDraftOrderDraftOrderAppliedDiscount|() appliedDiscount?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "billing_address"}
     ReopenCloseOrderOrderBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     ModifyDraftOrderDraftOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "shipping_address"}
     ReopenCloseOrderOrderBillingAddress|() shippingAddress?;
     string email?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "invoice_sent_at"}
     anydata? invoiceSentAt?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
     string tags?;
+    @jsondata:Name {value: "completed_at"}
     anydata? completedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "note_attributes"}
     anydata[] noteAttributes?;
     string name?;
+    @jsondata:Name {value: "shipping_line"}
     ModifyDraftOrderDraftOrderShippingLine|() shippingLine?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
+    @jsondata:Name {value: "invoice_url"}
     string invoiceUrl?;
     AbandonedCheckoutsCustomer customer?;
     string status?;
@@ -1019,6 +1310,7 @@
 
 type ModifyDraftOrderDraftOrderAppliedDiscount record {
     string amount?;
+    @jsondata:Name {value: "value_type"}
     string valueType?;
     string description?;
     string? title?;
@@ -1027,20 +1319,29 @@
 
 
 type ModifyDraftOrderDraftOrderLineItems record {
+    @jsondata:Name {value: "variant_title"}
     string? variantTitle?;
     int quantity?;
+    @jsondata:Name {value: "applied_discount"}
     anydata? appliedDiscount?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
     boolean taxable?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
     boolean custom?;
     string title?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
     string price?;
     anydata? vendor?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     string name?;
     int grams?;
@@ -1058,19 +1359,28 @@
 
 
 type DiscountCode record {
+    @jsondata:Name {value: "discount_code_creation"}
     DiscountCodeDiscountCodeCreation discountCodeCreation?;
 };
 
 
 type DiscountCodeDiscountCodeCreation record {
+    @jsondata:Name {value: "completed_at"}
     anydata? completedAt?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "imported_count"}
     int importedCount?;
+    @jsondata:Name {value: "price_rule_id"}
     int priceRuleId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "started_at"}
     anydata? startedAt?;
+    @jsondata:Name {value: "failed_count"}
     int failedCount?;
     int id?;
+    @jsondata:Name {value: "codes_count"}
     int codesCount?;
     string status?;
 };
@@ -1079,14 +1389,18 @@
 
 type RetrieveAListOfTenderTransactionsQueries record {
     # Show tender transactions processed\_at or after the specified date. 
+    @http:Query {name: "processed_at_min"}
     string processedAtMin?;
     # The maximum number of results to retrieve.(default: 50)(maximum: 250) 
     string 'limit?;
     # Show tender transactions processed at the specified date. 
+    @http:Query {name: "processed_at"}
     string processedAt?;
     # Retrieve only transactions after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show tender transactions processed\_at or before the specified date. 
+    @http:Query {name: "processed_at_max"}
     string processedAtMax?;
     # Show tender transactions ordered by processed\_at in ascending or descending order. 
     string 'order?;
@@ -1094,28 +1408,40 @@
 
 
 type InventoryLevelsInventoryLevels record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int available?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
 };
 
 
 type SmartCollectionResponseSmartCollection record {
     UpdateCustomCollectionCustomCollectionImage image?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
+    @jsondata:Name {value: "products_count"}
     int productsCount?;
     string 'handle?;
     SmartCollectionResponseSmartCollectionRules[] rules?;
     string title?;
+    @jsondata:Name {value: "published_scope"}
     string publishedScope?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     boolean disjunctive?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
+    @jsondata:Name {value: "sort_order"}
     string sortOrder?;
 };
 
@@ -1124,6 +1450,7 @@
     string src?;
     string alt?;
     int width?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int height?;
 };
@@ -1142,41 +1469,65 @@
 
 
 type CollectResponseCollect record {
+    @jsondata:Name {value: "collection_id"}
     int collectionId?;
+    @jsondata:Name {value: "updated_at"}
     anydata? updatedAt?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
+    @jsondata:Name {value: "created_at"}
     anydata? createdAt?;
     int id?;
     int position?;
+    @jsondata:Name {value: "sort_value"}
     string sortValue?;
 };
 
 
 type SingleDraftOrderDraftOrder record {
     string? note?;
+    @jsondata:Name {value: "applied_discount"}
     CompleteDraftOrderDraftOrderAppliedDiscount|() appliedDiscount?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "billing_address"}
     ReopenCloseOrderOrderBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     ModifyDraftOrderDraftOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "shipping_address"}
     ReopenCloseOrderOrderBillingAddress|() shippingAddress?;
     string email?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "invoice_sent_at"}
     anydata? invoiceSentAt?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
     string tags?;
+    @jsondata:Name {value: "completed_at"}
     anydata? completedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "note_attributes"}
     anydata[] noteAttributes?;
     string name?;
+    @jsondata:Name {value: "shipping_line"}
     ModifyDraftOrderDraftOrderShippingLine|() shippingLine?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
+    @jsondata:Name {value: "invoice_url"}
     string invoiceUrl?;
     AbandonedCheckoutsCustomer customer?;
     string status?;
@@ -1185,6 +1536,7 @@
 
 type CompleteDraftOrderDraftOrderAppliedDiscount record {
     string amount?;
+    @jsondata:Name {value: "value_type"}
     string valueType?;
     string description?;
     anydata? title?;
@@ -1198,13 +1550,18 @@
 
 
 type ProductImagesImages record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string src?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     anydata? alt?;
     int width?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "variant_ids"}
     anydata[] variantIds?;
     int id?;
     int position?;
@@ -1214,32 +1571,46 @@
 
 type CreateRefundRefundTransactions record {
     string amount?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
     boolean test?;
     string kind?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string message?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
     anydata? authorization?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "parent_id"}
     int parentId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
     string currency?;
+    @jsondata:Name {value: "error_code"}
     anydata? errorCode?;
     record {|anydata...;|} receipt?;
     int id?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
     string gateway?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
     string status?;
 };
 
 
 type StorefrontAccessTokensStorefrontAccessTokens record {
+    @jsondata:Name {value: "access_token"}
     string accessToken?;
+    @jsondata:Name {value: "access_scope"}
     string accessScope?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int id?;
     string title?;
@@ -1254,14 +1625,20 @@
 type SingleDisputeDispute record {
     string reason?;
     string amount?;
+    @jsondata:Name {value: "evidence_due_by"}
     string evidenceDueBy?;
+    @jsondata:Name {value: "finalized_on"}
     anydata? finalizedOn?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "initiated_at"}
     string initiatedAt?;
     string 'type?;
+    @jsondata:Name {value: "network_reason_code"}
     string networkReasonCode?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "evidence_sent_on"}
     anydata? evidenceSentOn?;
     string status?;
 };
@@ -1270,38 +1647,53 @@
 
 type RetrieveAListOfPriceRulesQueries record {
     # Show price rules created after date (format 2017-03-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show price rules starting after date (format 2017-03-25T16:15:47-04:00). 
+    @http:Query {name: "starts_at_min"}
     string startsAtMin?;
     # Show price rules created before date (format 2017-03-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Show price rules last updated before date (format 2017-03-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show price rules starting before date (format 2017-03-25T16:15:47-04:00). 
+    @http:Query {name: "starts_at_max"}
     string startsAtMax?;
     # Show price rules last updated after date (format 2017-03-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # The maximum number of results to retrieve.(default: 50)(maximum: 250) 
     string 'limit?;
     # Show price rules with times used. 
+    @http:Query {name: "times_used"}
     string timesUsed?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show price rules ending after date (format 2017-03-25T16:15:47-04:00). 
+    @http:Query {name: "ends_at_min"}
     string endsAtMin?;
     # Show price rules ending before date (format 2017-03-25T16:15:47-04:00). 
+    @http:Query {name: "ends_at_max"}
     string endsAtMax?;
 };
 
 
 type ProductsResponseImages record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string src?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     anydata? alt?;
     int width?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "variant_ids"}
     anydata[] variantIds?;
     int id?;
     int position?;
@@ -1329,74 +1721,129 @@
 
 
 type UpdateOrderResponseOrder record {
+    @jsondata:Name {value: "cancelled_at"}
     anydata? cancelledAt?;
+    @jsondata:Name {value: "fulfillment_status"}
     anydata? fulfillmentStatus?;
+    @jsondata:Name {value: "total_price_usd"}
     string totalPriceUsd?;
+    @jsondata:Name {value: "billing_address"}
     ReopenCloseOrderOrderBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     ReopenCloseOrderOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "total_discounts_set"}
     ReopenCloseOrderOrderTotalDiscountsSet totalDiscountsSet?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "landing_site"}
     string landingSite?;
+    @jsondata:Name {value: "source_identifier"}
     string sourceIdentifier?;
     string reference?;
     int number?;
+    @jsondata:Name {value: "checkout_id"}
     int checkoutId?;
+    @jsondata:Name {value: "checkout_token"}
     string checkoutToken?;
+    @jsondata:Name {value: "tax_lines"}
     ReopenCloseOrderOrderTaxLines1[] taxLines?;
+    @jsondata:Name {value: "customer_locale"}
     anydata? customerLocale?;
     int id?;
+    @jsondata:Name {value: "app_id"}
     anydata? appId?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "closed_at"}
     anydata? closedAt?;
+    @jsondata:Name {value: "order_status_url"}
     string orderStatusUrl?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
     boolean test?;
+    @jsondata:Name {value: "total_shipping_price_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalShippingPriceSet?;
+    @jsondata:Name {value: "subtotal_price_set"}
     ReopenCloseOrderOrderSubtotalPriceSet subtotalPriceSet?;
+    @jsondata:Name {value: "payment_gateway_names"}
     string[] paymentGatewayNames?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
     string tags?;
+    @jsondata:Name {value: "processing_method"}
     string processingMethod?;
+    @jsondata:Name {value: "shipping_lines"}
     ReopenCloseOrderOrderShippingLines[] shippingLines?;
     string phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     UpdateOrderResponseOrderNoteAttributes[] noteAttributes?;
     string name?;
+    @jsondata:Name {value: "cart_token"}
     string cartToken?;
+    @jsondata:Name {value: "total_tax_set"}
     ReopenCloseOrderOrderPriceSet2 totalTaxSet?;
+    @jsondata:Name {value: "landing_site_ref"}
     string landingSiteRef?;
+    @jsondata:Name {value: "discount_codes"}
     ReopenCloseOrderOrderDiscountCodes[] discountCodes?;
     string? note?;
+    @jsondata:Name {value: "payment_details"}
     ReopenCloseOrderOrderPaymentDetails paymentDetails?;
+    @jsondata:Name {value: "order_number"}
     int orderNumber?;
+    @jsondata:Name {value: "discount_applications"}
     ReopenCloseOrderOrderDiscountApplications[] discountApplications?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "total_line_items_price_set"}
     ReopenCloseOrderOrderSubtotalPriceSet totalLineItemsPriceSet?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "buyer_accepts_marketing"}
     boolean buyerAcceptsMarketing?;
     boolean confirmed?;
+    @jsondata:Name {value: "total_weight"}
     int totalWeight?;
+    @jsondata:Name {value: "contact_email"}
     string contactEmail?;
     ReopenCloseOrderOrderRefunds[] refunds?;
+    @jsondata:Name {value: "total_discounts"}
     string totalDiscounts?;
     ReopenCloseOrderOrderFulfillments[] fulfillments?;
+    @jsondata:Name {value: "client_details"}
     ReopenCloseOrderOrderClientDetails clientDetails?;
+    @jsondata:Name {value: "referring_site"}
     string referringSite?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
     string currency?;
+    @jsondata:Name {value: "shipping_address"}
     ReopenCloseOrderOrderBillingAddress|() shippingAddress?;
+    @jsondata:Name {value: "browser_ip"}
     string browserIp?;
     string email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "total_price_set"}
     ReopenCloseOrderOrderTotalPriceSet totalPriceSet?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
     string token?;
+    @jsondata:Name {value: "cancel_reason"}
     anydata? cancelReason?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "financial_status"}
     string financialStatus?;
     string gateway?;
     ReopenCloseOrderOrderCustomer customer?;
@@ -1404,30 +1851,46 @@
 
 
 type ReopenCloseOrderOrderLineItems record {
+    @jsondata:Name {value: "variant_title"}
     string? variantTitle?;
+    @jsondata:Name {value: "fulfillment_status"}
     anydata? fulfillmentStatus?;
+    @jsondata:Name {value: "total_discount"}
     string totalDiscount?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "total_discount_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalDiscountSet?;
     string title?;
+    @jsondata:Name {value: "product_exists"}
     boolean productExists?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "tax_lines"}
     ReopenCloseOrderOrderTaxLines[] taxLines?;
     string price?;
     anydata? vendor?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     int id?;
     int grams?;
     string? sku?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
     int quantity?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
+    @jsondata:Name {value: "discount_allocations"}
     anydata[] discountAllocations?;
+    @jsondata:Name {value: "variant_inventory_management"}
     string variantInventoryManagement?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string name?;
+    @jsondata:Name {value: "price_set"}
     ReopenCloseOrderOrderPriceSet priceSet?;
     ReopenCloseOrderOrderProperties[] properties?;
 };
@@ -1436,31 +1899,38 @@
 type ReopenCloseOrderOrderTaxLines record {
     decimal rate?;
     string price?;
+    @jsondata:Name {value: "price_set"}
     ReopenCloseOrderOrderPriceSet1 priceSet?;
     string title?;
 };
 
 
 type ReopenCloseOrderOrderPriceSet1 record {
+    @jsondata:Name {value: "shop_money"}
     ReopenCloseOrderOrderPriceSet1PresentmentMoney shopMoney?;
+    @jsondata:Name {value: "presentment_money"}
     ReopenCloseOrderOrderPriceSet1PresentmentMoney presentmentMoney?;
 };
 
 
 type ReopenCloseOrderOrderPriceSet1PresentmentMoney record {
     string amount?;
+    @jsondata:Name {value: "currency_code"}
     string currencyCode?;
 };
 
 
 type ReopenCloseOrderOrderPriceSet record {
+    @jsondata:Name {value: "shop_money"}
     ReopenCloseOrderOrderPriceSetPresentmentMoney shopMoney?;
+    @jsondata:Name {value: "presentment_money"}
     ReopenCloseOrderOrderPriceSetPresentmentMoney presentmentMoney?;
 };
 
 
 type ReopenCloseOrderOrderPriceSetPresentmentMoney record {
     string amount?;
+    @jsondata:Name {value: "currency_code"}
     string currencyCode?;
 };
 
@@ -1474,49 +1944,64 @@
 type ReopenCloseOrderOrderTaxLines1 record {
     decimal rate?;
     string price?;
+    @jsondata:Name {value: "price_set"}
     ReopenCloseOrderOrderPriceSet2 priceSet?;
     string title?;
 };
 
 
 type ReopenCloseOrderOrderPriceSet2 record {
+    @jsondata:Name {value: "shop_money"}
     ReopenCloseOrderOrderPriceSet2PresentmentMoney shopMoney?;
+    @jsondata:Name {value: "presentment_money"}
     ReopenCloseOrderOrderPriceSet2PresentmentMoney presentmentMoney?;
 };
 
 
 type ReopenCloseOrderOrderPriceSet2PresentmentMoney record {
     string amount?;
+    @jsondata:Name {value: "currency_code"}
     string currencyCode?;
 };
 
 
 type ReopenCloseOrderOrderSubtotalPriceSet record {
+    @jsondata:Name {value: "shop_money"}
     ReopenCloseOrderOrderSubtotalPriceSetPresentmentMoney shopMoney?;
+    @jsondata:Name {value: "presentment_money"}
     ReopenCloseOrderOrderSubtotalPriceSetPresentmentMoney presentmentMoney?;
 };
 
 
 type ReopenCloseOrderOrderSubtotalPriceSetPresentmentMoney record {
     string amount?;
+    @jsondata:Name {value: "currency_code"}
     string currencyCode?;
 };
 
 
 type ReopenCloseOrderOrderShippingLines record {
     string code?;
+    @jsondata:Name {value: "delivery_category"}
     anydata? deliveryCategory?;
     string 'source?;
+    @jsondata:Name {value: "discount_allocations"}
     anydata[] discountAllocations?;
     string title?;
+    @jsondata:Name {value: "carrier_identifier"}
     anydata? carrierIdentifier?;
+    @jsondata:Name {value: "discounted_price_set"}
     ReopenCloseOrderOrderTotalDiscountSet discountedPriceSet?;
+    @jsondata:Name {value: "discounted_price"}
     string discountedPrice?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
     anydata? phone?;
     string price?;
     int id?;
+    @jsondata:Name {value: "price_set"}
     ReopenCloseOrderOrderTotalDiscountSet priceSet?;
+    @jsondata:Name {value: "requested_fulfillment_service_id"}
     anydata? requestedFulfillmentServiceId?;
 };
 
@@ -1535,19 +2020,28 @@
 
 
 type ReopenCloseOrderOrderPaymentDetails record {
+    @jsondata:Name {value: "credit_card_number"}
     string creditCardNumber?;
+    @jsondata:Name {value: "avs_result_code"}
     anydata? avsResultCode?;
+    @jsondata:Name {value: "cvv_result_code"}
     anydata? cvvResultCode?;
+    @jsondata:Name {value: "credit_card_bin"}
     anydata? creditCardBin?;
+    @jsondata:Name {value: "credit_card_company"}
     string creditCardCompany?;
 };
 
 
 type ReopenCloseOrderOrderDiscountApplications record {
+    @jsondata:Name {value: "allocation_method"}
     string allocationMethod?;
+    @jsondata:Name {value: "value_type"}
     string valueType?;
     string code?;
+    @jsondata:Name {value: "target_type"}
     string targetType?;
+    @jsondata:Name {value: "target_selection"}
     string targetSelection?;
     string 'type?;
     string value?;
@@ -1556,58 +2050,88 @@
 
 type ReopenCloseOrderOrderRefunds record {
     string? note?;
+    @jsondata:Name {value: "refund_line_items"}
     ReopenCloseOrderOrderRefundLineItems[] refundLineItems?;
+    @jsondata:Name {value: "user_id"}
     int userId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "order_adjustments"}
     anydata[] orderAdjustments?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
     boolean restock?;
     int id?;
     ReopenCloseOrderOrderTransactions[] transactions?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
 };
 
 
 type ReopenCloseOrderOrderRefundLineItems record {
+    @jsondata:Name {value: "line_item"}
     ReopenCloseOrderOrderLineItem lineItem?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
     decimal subtotal?;
+    @jsondata:Name {value: "total_tax_set"}
     ReopenCloseOrderOrderPriceSet1 totalTaxSet?;
     int id?;
+    @jsondata:Name {value: "subtotal_set"}
     ReopenCloseOrderOrderPriceSet subtotalSet?;
+    @jsondata:Name {value: "total_tax"}
     decimal totalTax?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
+    @jsondata:Name {value: "restock_type"}
     string restockType?;
 };
 
 
 type ReopenCloseOrderOrderLineItem record {
+    @jsondata:Name {value: "variant_title"}
     string? variantTitle?;
+    @jsondata:Name {value: "fulfillment_status"}
     anydata? fulfillmentStatus?;
+    @jsondata:Name {value: "total_discount"}
     string totalDiscount?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "total_discount_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalDiscountSet?;
     string title?;
+    @jsondata:Name {value: "product_exists"}
     boolean productExists?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "tax_lines"}
     ReopenCloseOrderOrderTaxLines[] taxLines?;
     string price?;
     anydata? vendor?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     int id?;
     int grams?;
     string? sku?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
     int quantity?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
+    @jsondata:Name {value: "discount_allocations"}
     anydata[] discountAllocations?;
+    @jsondata:Name {value: "variant_inventory_management"}
     string variantInventoryManagement?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string name?;
+    @jsondata:Name {value: "price_set"}
     ReopenCloseOrderOrderPriceSet priceSet?;
     anydata[] properties?;
 };
@@ -1615,44 +2139,66 @@
 
 type ReopenCloseOrderOrderTransactions record {
     string amount?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
     boolean test?;
     string kind?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     anydata? message?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
     string authorization?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "parent_id"}
     int parentId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
     string currency?;
+    @jsondata:Name {value: "error_code"}
     anydata? errorCode?;
     record {|anydata...;|} receipt?;
     int id?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
     string gateway?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
     string status?;
 };
 
 
 type ReopenCloseOrderOrderFulfillments record {
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "line_items"}
     ReopenCloseOrderOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "tracking_company"}
     string trackingCompany?;
+    @jsondata:Name {value: "tracking_urls"}
     string[] trackingUrls?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string 'service?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string name?;
+    @jsondata:Name {value: "tracking_number"}
     string trackingNumber?;
     ReopenCloseOrderOrderReceipt receipt?;
     int id?;
+    @jsondata:Name {value: "tracking_numbers"}
     string[] trackingNumbers?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "tracking_url"}
     string trackingUrl?;
+    @jsondata:Name {value: "shipment_status"}
     anydata? shipmentStatus?;
     string status?;
 };
@@ -1665,50 +2211,76 @@
 
 
 type ReopenCloseOrderOrderClientDetails record {
+    @jsondata:Name {value: "session_hash"}
     anydata? sessionHash?;
+    @jsondata:Name {value: "accept_language"}
     anydata? acceptLanguage?;
+    @jsondata:Name {value: "browser_width"}
     anydata? browserWidth?;
+    @jsondata:Name {value: "browser_height"}
     anydata? browserHeight?;
+    @jsondata:Name {value: "browser_ip"}
     string browserIp?;
+    @jsondata:Name {value: "user_agent"}
     anydata? userAgent?;
 };
 
 
 type ReopenCloseOrderOrderTotalPriceSet record {
+    @jsondata:Name {value: "shop_money"}
     ReopenCloseOrderOrderTotalPriceSetPresentmentMoney shopMoney?;
+    @jsondata:Name {value: "presentment_money"}
     ReopenCloseOrderOrderTotalPriceSetPresentmentMoney presentmentMoney?;
 };
 
 
 type ReopenCloseOrderOrderTotalPriceSetPresentmentMoney record {
     string amount?;
+    @jsondata:Name {value: "currency_code"}
     string currencyCode?;
 };
 
 
 type ReopenCloseOrderOrderCustomer record {
+    @jsondata:Name {value: "total_spent"}
     string totalSpent?;
     anydata? note?;
+    @jsondata:Name {value: "last_order_name"}
     string lastOrderName?;
+    @jsondata:Name {value: "last_order_id"}
     int lastOrderId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "multipass_identifier"}
     anydata? multipassIdentifier?;
+    @jsondata:Name {value: "verified_email"}
     boolean verifiedEmail?;
+    @jsondata:Name {value: "accepts_marketing_updated_at"}
     string acceptsMarketingUpdatedAt?;
     string tags?;
+    @jsondata:Name {value: "orders_count"}
     int ordersCount?;
+    @jsondata:Name {value: "default_address"}
     ReopenCloseOrderOrderCustomerDefaultAddress defaultAddress?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "accepts_marketing"}
     boolean acceptsMarketing?;
     anydata? phone?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "tax_exemptions"}
     anydata[] taxExemptions?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "marketing_opt_in_level"}
     anydata? marketingOptInLevel?;
     string state?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
@@ -1721,24 +2293,35 @@
 
 type TransactionObjectTransaction record {
     string amount?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
     boolean test?;
     string kind?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string message?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
     anydata? authorization?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "parent_id"}
     int parentId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "currency_exchange_adjustment"}
     anydata? currencyExchangeAdjustment?;
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
     string currency?;
+    @jsondata:Name {value: "error_code"}
     anydata? errorCode?;
     record {|anydata...;|} receipt?;
     int id?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
     string gateway?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
     string status?;
 };
@@ -1748,27 +2331,38 @@
     string src?;
     string alt?;
     int width?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int height?;
 };
 
 
 type FulfillmentOrders record {
+    @jsondata:Name {value: "fulfillment_orders"}
     FulfillmentOrdersFulfillmentOrders[] fulfillmentOrders?;
 };
 
 
 type FulfillmentOrdersFulfillmentOrders record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     FulfillmentOrdersDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     FulfillmentOrdersLineItems[] lineItems?;
+    @jsondata:Name {value: "outgoing_requests"}
     anydata[] outgoingRequests?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     string[] supportedActions?;
+    @jsondata:Name {value: "assigned_location"}
     FulfillmentOrdersAssignedLocation assignedLocation?;
     string status?;
 };
@@ -1782,21 +2376,29 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
 
 
 type FulfillmentOrdersLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
@@ -1804,90 +2406,143 @@
 
 type ShopConfigurationsShop record {
     string country?;
+    @jsondata:Name {value: "has_gift_cards"}
     boolean hasGiftCards?;
+    @jsondata:Name {value: "multi_location_enabled"}
     boolean multiLocationEnabled?;
     anydata? 'source?;
+    @jsondata:Name {value: "money_with_currency_in_emails_format"}
     string moneyWithCurrencyInEmailsFormat?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "plan_display_name"}
     string planDisplayName?;
     string province?;
+    @jsondata:Name {value: "eligible_for_payments"}
     boolean eligibleForPayments?;
     int id?;
     decimal longitude?;
+    @jsondata:Name {value: "has_discounts"}
     boolean hasDiscounts?;
     string zip?;
+    @jsondata:Name {value: "force_ssl"}
     boolean forceSsl?;
+    @jsondata:Name {value: "password_enabled"}
     boolean passwordEnabled?;
+    @jsondata:Name {value: "eligible_for_card_reader_giveaway"}
     boolean eligibleForCardReaderGiveaway?;
+    @jsondata:Name {value: "iana_timezone"}
     string ianaTimezone?;
+    @jsondata:Name {value: "enabled_presentment_currencies"}
     string[] enabledPresentmentCurrencies?;
+    @jsondata:Name {value: "plan_name"}
     string planName?;
+    @jsondata:Name {value: "requires_extra_payments_agreement"}
     boolean requiresExtraPaymentsAgreement?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
+    @jsondata:Name {value: "cookie_consent_level"}
     string cookieConsentLevel?;
+    @jsondata:Name {value: "weight_unit"}
     string weightUnit?;
     string phone?;
+    @jsondata:Name {value: "customer_email"}
     string customerEmail?;
     string domain?;
+    @jsondata:Name {value: "county_taxes"}
     boolean countyTaxes?;
+    @jsondata:Name {value: "money_with_currency_format"}
     string moneyWithCurrencyFormat?;
     string name?;
+    @jsondata:Name {value: "money_in_emails_format"}
     string moneyInEmailsFormat?;
     boolean finances?;
+    @jsondata:Name {value: "shop_owner"}
     string shopOwner?;
+    @jsondata:Name {value: "pre_launch_enabled"}
     boolean preLaunchEnabled?;
     string city?;
     string timezone?;
     decimal latitude?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "checkout_api_supported"}
     boolean checkoutApiSupported?;
+    @jsondata:Name {value: "taxes_included"}
     anydata? taxesIncluded?;
+    @jsondata:Name {value: "setup_required"}
     boolean setupRequired?;
+    @jsondata:Name {value: "money_format"}
     string moneyFormat?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "country_name"}
     string countryName?;
     string currency?;
     string email?;
+    @jsondata:Name {value: "primary_location_id"}
     int primaryLocationId?;
+    @jsondata:Name {value: "google_apps_login_enabled"}
     anydata? googleAppsLoginEnabled?;
     string address2?;
     string address1?;
+    @jsondata:Name {value: "primary_locale"}
     string primaryLocale?;
+    @jsondata:Name {value: "has_storefront"}
     boolean hasStorefront?;
+    @jsondata:Name {value: "tax_shipping"}
     anydata? taxShipping?;
+    @jsondata:Name {value: "google_apps_domain"}
     anydata? googleAppsDomain?;
+    @jsondata:Name {value: "myshopify_domain"}
     string myshopifyDomain?;
 };
 
 
 type SingleCustomCollectionCustomCollection record {
+    @jsondata:Name {value: "published_scope"}
     string publishedScope?;
     UpdateCustomCollectionCustomCollectionImage image?;
+    @jsondata:Name {value: "body_html"}
     string? bodyHtml?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "products_count"}
     int productsCount?;
     string 'handle?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
     string title?;
+    @jsondata:Name {value: "sort_order"}
     string sortOrder?;
 };
 
 
 type InventoryItemInventoryItem record {
     string cost?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "province_code_of_origin"}
     anydata? provinceCodeOfOrigin?;
     boolean tracked?;
+    @jsondata:Name {value: "country_code_of_origin"}
     anydata? countryCodeOfOrigin?;
     int id?;
     string? sku?;
+    @jsondata:Name {value: "country_harmonized_system_codes"}
     anydata[] countryHarmonizedSystemCodes?;
+    @jsondata:Name {value: "harmonized_system_code"}
     anydata? harmonizedSystemCode?;
 };
 
@@ -1898,39 +2553,55 @@
 
 
 type CollectionListingResponse record {
+    @jsondata:Name {value: "collection_listings"}
     CollectionListingResponseCollectionListings[] collectionListings?;
 };
 
 
 type CollectionListingResponseCollectionListings record {
+    @jsondata:Name {value: "collection_id"}
     int collectionId?;
     CollectionListingResponseImage|() image?;
+    @jsondata:Name {value: "body_html"}
     string? bodyHtml?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string 'handle?;
+    @jsondata:Name {value: "default_product_image"}
     record {|anydata...;|}? defaultProductImage?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
     string title?;
+    @jsondata:Name {value: "sort_order"}
     string sortOrder?;
 };
 
 
 type CollectionListingResponseImage record {
     string src?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
 };
 
 
 type ModifyProductVariantVariant record {
+    @jsondata:Name {value: "presentment_prices"}
     ProductVariantsPresentmentPrices[] presentmentPrices?;
+    @jsondata:Name {value: "inventory_management"}
     string inventoryManagement?;
+    @jsondata:Name {value: "old_inventory_quantity"}
     int oldInventoryQuantity?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string title?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     string price?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     anydata? option3?;
     string option1?;
@@ -1939,54 +2610,81 @@
     int grams?;
     string? sku?;
     string barcode?;
+    @jsondata:Name {value: "inventory_quantity"}
     int inventoryQuantity?;
+    @jsondata:Name {value: "compare_at_price"}
     anydata? compareAtPrice?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
     decimal weight?;
+    @jsondata:Name {value: "inventory_policy"}
     string inventoryPolicy?;
+    @jsondata:Name {value: "weight_unit"}
     string weightUnit?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int position?;
+    @jsondata:Name {value: "image_id"}
     int imageId?;
 };
 
 
 type ProductVariantsPresentmentPrices record {
+    @jsondata:Name {value: "compare_at_price"}
     anydata? compareAtPrice?;
     ReopenCloseOrderOrderPriceSetPresentmentMoney price?;
 };
 
 
 type PayoutsListSummary record {
+    @jsondata:Name {value: "charges_gross_amount"}
     string chargesGrossAmount?;
+    @jsondata:Name {value: "reserved_funds_gross_amount"}
     string reservedFundsGrossAmount?;
+    @jsondata:Name {value: "retried_payouts_gross_amount"}
     string retriedPayoutsGrossAmount?;
+    @jsondata:Name {value: "charges_fee_amount"}
     string chargesFeeAmount?;
+    @jsondata:Name {value: "adjustments_gross_amount"}
     string adjustmentsGrossAmount?;
+    @jsondata:Name {value: "reserved_funds_fee_amount"}
     string reservedFundsFeeAmount?;
+    @jsondata:Name {value: "refunds_fee_amount"}
     string refundsFeeAmount?;
+    @jsondata:Name {value: "retried_payouts_fee_amount"}
     string retriedPayoutsFeeAmount?;
+    @jsondata:Name {value: "adjustments_fee_amount"}
     string adjustmentsFeeAmount?;
+    @jsondata:Name {value: "refunds_gross_amount"}
     string refundsGrossAmount?;
 };
 
 
 type DraftOrdersLineItems record {
+    @jsondata:Name {value: "variant_title"}
     string? variantTitle?;
     int quantity?;
+    @jsondata:Name {value: "applied_discount"}
     anydata? appliedDiscount?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
     boolean taxable?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
     boolean custom?;
     string title?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
     string price?;
     anydata? vendor?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     string name?;
     int grams?;
@@ -2001,15 +2699,23 @@
 
 
 type ProductVariantsVariants record {
+    @jsondata:Name {value: "presentment_prices"}
     ProductVariantsPresentmentPrices[] presentmentPrices?;
+    @jsondata:Name {value: "inventory_management"}
     string inventoryManagement?;
+    @jsondata:Name {value: "old_inventory_quantity"}
     int oldInventoryQuantity?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string title?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     string price?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     anydata? option3?;
     string option1?;
@@ -2018,53 +2724,76 @@
     int grams?;
     string? sku?;
     string barcode?;
+    @jsondata:Name {value: "inventory_quantity"}
     int inventoryQuantity?;
+    @jsondata:Name {value: "compare_at_price"}
     anydata? compareAtPrice?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
     decimal weight?;
+    @jsondata:Name {value: "inventory_policy"}
     string inventoryPolicy?;
+    @jsondata:Name {value: "weight_unit"}
     string weightUnit?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int position?;
+    @jsondata:Name {value: "image_id"}
     int? imageId?;
 };
 
 
 type ApiVersionMobilePlatformApplicationsJsonBody record {
+    @jsondata:Name {value: "mobile_platform_application"}
     AdminapiapiVersionmobilePlatformApplicationsJsonMobilePlatformApplication mobilePlatformApplication?;
 };
 
 
 type AdminapiapiVersionmobilePlatformApplicationsJsonMobilePlatformApplication record {
+    @jsondata:Name {value: "sha256_cert_fingerprints"}
     string[] sha256CertFingerprints?;
+    @jsondata:Name {value: "enabled_universal_or_app_links"}
     boolean enabledUniversalOrAppLinks?;
+    @jsondata:Name {value: "application_id"}
     string applicationId?;
     string platform?;
 };
 
 
 type SingleCharge record {
+    @jsondata:Name {value: "recurring_application_charge"}
     SingleChargeRecurringApplicationCharge recurringApplicationCharge?;
 };
 
 
 type SingleChargeRecurringApplicationCharge record {
+    @jsondata:Name {value: "api_client_id"}
     int apiClientId?;
     anydata? test?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "cancelled_on"}
     anydata? cancelledOn?;
+    @jsondata:Name {value: "trial_days"}
     int trialDays?;
+    @jsondata:Name {value: "decorated_return_url"}
     string decoratedReturnUrl?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "confirmation_url"}
     string confirmationUrl?;
     string price?;
+    @jsondata:Name {value: "trial_ends_on"}
     anydata? trialEndsOn?;
     string name?;
+    @jsondata:Name {value: "return_url"}
     string returnUrl?;
+    @jsondata:Name {value: "billing_on"}
     string billingOn?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "activated_on"}
     anydata? activatedOn?;
     string status?;
 };
@@ -2087,74 +2816,129 @@
 
 
 type CloseOrderResponseOrder record {
+    @jsondata:Name {value: "cancelled_at"}
     anydata? cancelledAt?;
+    @jsondata:Name {value: "fulfillment_status"}
     anydata? fulfillmentStatus?;
+    @jsondata:Name {value: "total_price_usd"}
     string totalPriceUsd?;
+    @jsondata:Name {value: "billing_address"}
     ReopenCloseOrderOrderBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     ReopenCloseOrderOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "total_discounts_set"}
     ReopenCloseOrderOrderTotalDiscountsSet totalDiscountsSet?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "landing_site"}
     string landingSite?;
+    @jsondata:Name {value: "source_identifier"}
     string sourceIdentifier?;
     string reference?;
     int number?;
+    @jsondata:Name {value: "checkout_id"}
     int checkoutId?;
+    @jsondata:Name {value: "checkout_token"}
     string checkoutToken?;
+    @jsondata:Name {value: "tax_lines"}
     ReopenCloseOrderOrderTaxLines1[] taxLines?;
+    @jsondata:Name {value: "customer_locale"}
     anydata? customerLocale?;
     int id?;
+    @jsondata:Name {value: "app_id"}
     anydata? appId?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "closed_at"}
     string closedAt?;
+    @jsondata:Name {value: "order_status_url"}
     string orderStatusUrl?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
     boolean test?;
+    @jsondata:Name {value: "total_shipping_price_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalShippingPriceSet?;
+    @jsondata:Name {value: "subtotal_price_set"}
     ReopenCloseOrderOrderSubtotalPriceSet subtotalPriceSet?;
+    @jsondata:Name {value: "payment_gateway_names"}
     string[] paymentGatewayNames?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
     string tags?;
+    @jsondata:Name {value: "processing_method"}
     string processingMethod?;
+    @jsondata:Name {value: "shipping_lines"}
     ReopenCloseOrderOrderShippingLines[] shippingLines?;
     string phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     ReopenCloseOrderOrderNoteAttributes[] noteAttributes?;
     string name?;
+    @jsondata:Name {value: "cart_token"}
     string cartToken?;
+    @jsondata:Name {value: "total_tax_set"}
     ReopenCloseOrderOrderPriceSet2 totalTaxSet?;
+    @jsondata:Name {value: "landing_site_ref"}
     string landingSiteRef?;
+    @jsondata:Name {value: "discount_codes"}
     ReopenCloseOrderOrderDiscountCodes[] discountCodes?;
     anydata? note?;
+    @jsondata:Name {value: "payment_details"}
     ReopenCloseOrderOrderPaymentDetails paymentDetails?;
+    @jsondata:Name {value: "order_number"}
     int orderNumber?;
+    @jsondata:Name {value: "discount_applications"}
     ReopenCloseOrderOrderDiscountApplications[] discountApplications?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "total_line_items_price_set"}
     ReopenCloseOrderOrderSubtotalPriceSet totalLineItemsPriceSet?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "buyer_accepts_marketing"}
     boolean buyerAcceptsMarketing?;
     boolean confirmed?;
+    @jsondata:Name {value: "total_weight"}
     int totalWeight?;
+    @jsondata:Name {value: "contact_email"}
     string contactEmail?;
     ReopenCloseOrderOrderRefunds[] refunds?;
+    @jsondata:Name {value: "total_discounts"}
     string totalDiscounts?;
     ReopenCloseOrderOrderFulfillments[] fulfillments?;
+    @jsondata:Name {value: "client_details"}
     ReopenCloseOrderOrderClientDetails clientDetails?;
+    @jsondata:Name {value: "referring_site"}
     string referringSite?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
     string currency?;
+    @jsondata:Name {value: "shipping_address"}
     ReopenCloseOrderOrderBillingAddress|() shippingAddress?;
+    @jsondata:Name {value: "browser_ip"}
     string browserIp?;
     string email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "total_price_set"}
     ReopenCloseOrderOrderTotalPriceSet totalPriceSet?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
     string token?;
+    @jsondata:Name {value: "cancel_reason"}
     anydata? cancelReason?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "financial_status"}
     string financialStatus?;
     string gateway?;
     ReopenCloseOrderOrderCustomer customer?;
@@ -2164,6 +2948,7 @@
 type UpdateCountryTaxRateCountry record {
     UpdateCountryTaxRateCountryProvinces[] provinces?;
     string code?;
+    @jsondata:Name {value: "tax_name"}
     string taxName?;
     string name?;
     decimal tax?;
@@ -2173,22 +2958,31 @@
 
 type UpdateCountryTaxRateCountryProvinces record {
     string code?;
+    @jsondata:Name {value: "tax_type"}
     string? taxType?;
+    @jsondata:Name {value: "tax_name"}
     string taxName?;
     string name?;
+    @jsondata:Name {value: "tax_percentage"}
     decimal taxPercentage?;
     decimal tax?;
     int id?;
+    @jsondata:Name {value: "shipping_zone_id"}
     anydata? shippingZoneId?;
+    @jsondata:Name {value: "country_id"}
     int countryId?;
 };
 
 
 type AvailableInventoryInventoryLevel record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int available?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
 };
 
@@ -2199,28 +2993,44 @@
 
 
 type Customer record {
+    @jsondata:Name {value: "total_spent"}
     string totalSpent?;
     string? note?;
     Address[] addresses?;
+    @jsondata:Name {value: "last_order_name"}
     string? lastOrderName?;
+    @jsondata:Name {value: "last_order_id"}
     int? lastOrderId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "email_marketing_consent"}
     CustomerEmailMarketingConsent|() emailMarketingConsent?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "last_name"}
     string? lastName?;
+    @jsondata:Name {value: "multipass_identifier"}
     string? multipassIdentifier?;
+    @jsondata:Name {value: "verified_email"}
     boolean verifiedEmail?;
     string tags?;
+    @jsondata:Name {value: "orders_count"}
     int ordersCount?;
+    @jsondata:Name {value: "sms_marketing_consent"}
     CustomerSmsMarketingConsent|() smsMarketingConsent?;
+    @jsondata:Name {value: "default_address"}
     Address defaultAddress?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string? phone?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string? adminGraphqlApiId?;
+    @jsondata:Name {value: "tax_exemptions"}
     string[] taxExemptions?;
     string? currency?;
     int id?;
     string state?;
+    @jsondata:Name {value: "first_name"}
     string? firstName?;
     string? email?;
 };
@@ -2232,41 +3042,56 @@
     string? address2?;
     string? city?;
     string? address1?;
+    @jsondata:Name {value: "last_name"}
     string? lastName?;
+    @jsondata:Name {value: "province_code"}
     string? provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string? countryCode?;
     boolean default?;
     string? province?;
     string? phone?;
     string? name?;
+    @jsondata:Name {value: "country_name"}
     string? countryName?;
     string? company?;
     int id?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
+    @jsondata:Name {value: "first_name"}
     string? firstName?;
 };
 
 
 type CustomerEmailMarketingConsent record {
+    @jsondata:Name {value: "consent_updated_at"}
     string consentUpdatedAt?;
     string state?;
+    @jsondata:Name {value: "opt_in_level"}
     string optInLevel?;
 };
 
 
 type CustomerSmsMarketingConsent record {
+    @jsondata:Name {value: "consent_updated_at"}
     string consentUpdatedAt?;
+    @jsondata:Name {value: "consent_collected_from"}
     string consentCollectedFrom?;
     string state?;
+    @jsondata:Name {value: "opt_in_level"}
     string optInLevel?;
 };
 
 
 type InventoryListResponseInventoryLevels record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int available?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
 };
 
@@ -2285,74 +3110,129 @@
 
 
 type ReopenCloseOrderOrder record {
+    @jsondata:Name {value: "cancelled_at"}
     anydata? cancelledAt?;
+    @jsondata:Name {value: "fulfillment_status"}
     anydata? fulfillmentStatus?;
+    @jsondata:Name {value: "total_price_usd"}
     string totalPriceUsd?;
+    @jsondata:Name {value: "billing_address"}
     ReopenCloseOrderOrderBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     ReopenCloseOrderOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "total_discounts_set"}
     ReopenCloseOrderOrderTotalDiscountsSet totalDiscountsSet?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "landing_site"}
     string landingSite?;
+    @jsondata:Name {value: "source_identifier"}
     string sourceIdentifier?;
     string reference?;
     int number?;
+    @jsondata:Name {value: "checkout_id"}
     int checkoutId?;
+    @jsondata:Name {value: "checkout_token"}
     string checkoutToken?;
+    @jsondata:Name {value: "tax_lines"}
     ReopenCloseOrderOrderTaxLines1[] taxLines?;
+    @jsondata:Name {value: "customer_locale"}
     anydata? customerLocale?;
     int id?;
+    @jsondata:Name {value: "app_id"}
     anydata? appId?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "closed_at"}
     anydata? closedAt?;
+    @jsondata:Name {value: "order_status_url"}
     string orderStatusUrl?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
     boolean test?;
+    @jsondata:Name {value: "total_shipping_price_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalShippingPriceSet?;
+    @jsondata:Name {value: "subtotal_price_set"}
     ReopenCloseOrderOrderSubtotalPriceSet subtotalPriceSet?;
+    @jsondata:Name {value: "payment_gateway_names"}
     string[] paymentGatewayNames?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
     string tags?;
+    @jsondata:Name {value: "processing_method"}
     string processingMethod?;
+    @jsondata:Name {value: "shipping_lines"}
     ReopenCloseOrderOrderShippingLines[] shippingLines?;
     string phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     ReopenCloseOrderOrderNoteAttributes[] noteAttributes?;
     string name?;
+    @jsondata:Name {value: "cart_token"}
     string cartToken?;
+    @jsondata:Name {value: "total_tax_set"}
     ReopenCloseOrderOrderPriceSet2 totalTaxSet?;
+    @jsondata:Name {value: "landing_site_ref"}
     string landingSiteRef?;
+    @jsondata:Name {value: "discount_codes"}
     ReopenCloseOrderOrderDiscountCodes[] discountCodes?;
     anydata? note?;
+    @jsondata:Name {value: "payment_details"}
     ReopenCloseOrderOrderPaymentDetails paymentDetails?;
+    @jsondata:Name {value: "order_number"}
     int orderNumber?;
+    @jsondata:Name {value: "discount_applications"}
     ReopenCloseOrderOrderDiscountApplications[] discountApplications?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "total_line_items_price_set"}
     ReopenCloseOrderOrderSubtotalPriceSet totalLineItemsPriceSet?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "buyer_accepts_marketing"}
     boolean buyerAcceptsMarketing?;
     boolean confirmed?;
+    @jsondata:Name {value: "total_weight"}
     int totalWeight?;
+    @jsondata:Name {value: "contact_email"}
     string contactEmail?;
     ReopenCloseOrderOrderRefunds[] refunds?;
+    @jsondata:Name {value: "total_discounts"}
     string totalDiscounts?;
     ReopenCloseOrderOrderFulfillments[] fulfillments?;
+    @jsondata:Name {value: "client_details"}
     ReopenCloseOrderOrderClientDetails clientDetails?;
+    @jsondata:Name {value: "referring_site"}
     string referringSite?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
     string currency?;
+    @jsondata:Name {value: "shipping_address"}
     ReopenCloseOrderOrderBillingAddress|() shippingAddress?;
+    @jsondata:Name {value: "browser_ip"}
     string browserIp?;
     string email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "total_price_set"}
     ReopenCloseOrderOrderTotalPriceSet totalPriceSet?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
     string token?;
+    @jsondata:Name {value: "cancel_reason"}
     anydata? cancelReason?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "financial_status"}
     string financialStatus?;
     string gateway?;
     ReopenCloseOrderOrderCustomer customer?;
@@ -2366,10 +3246,15 @@
 
 type UpdateBlogResponseBlog record {
     anydata? feedburner?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "feedburner_location"}
     anydata? feedburnerLocation?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     int id?;
@@ -2382,16 +3267,20 @@
 
 type ProductImage record {
     # The date and time when the product image was last modified. The API returns this value in ISO 8601 format
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     # Specifies the location of the product image. This parameter supports URL filters that you can use to retrieve modified copies of the image. For example, add _small, to the filename to retrieve a scaled copy of the image at 100 x 100 px (for example, ipod-nano_small.png), or add _2048x2048 to retrieve a copy of the image constrained at 2048 x 2048 px resolution (for example, ipod-nano_2048x2048.png)
     string src?;
     # The id of the product associated with the image
+    @jsondata:Name {value: "product_id"}
     int productId?;
     # Width dimension of the image which is determined on upload
     int width?;
     # The date and time when the product image was created. The API returns this value in ISO 8601 formatting
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     # An array of variant ids associated with the image
+    @jsondata:Name {value: "variant_ids"}
     int[] variantIds?;
     # A unique numeric identifier for the product image
     int id?;
@@ -2403,13 +3292,18 @@
 
 
 type CreateProductImageImage record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string src?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     anydata? alt?;
     int width?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "variant_ids"}
     anydata[] variantIds?;
     int id?;
     int position?;
@@ -2421,28 +3315,38 @@
     string author?;
     int id?;
     string body?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
     string email?;
 };
 
 
 type InventoryLevelsConnectJsonBody record {
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
 };
 
 
 type UpdateCustomCollectionCustomCollection record {
+    @jsondata:Name {value: "published_scope"}
     string publishedScope?;
     UpdateCustomCollectionCustomCollectionImage image?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string 'handle?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string? publishedAt?;
     string title?;
+    @jsondata:Name {value: "sort_order"}
     string sortOrder?;
 };
 
@@ -2463,16 +3367,24 @@
     anydata? city?;
     anydata? address1?;
     anydata? latitude?;
+    @jsondata:Name {value: "happened_at"}
     string happenedAt?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "estimated_delivery_at"}
     anydata? estimatedDeliveryAt?;
     anydata? message?;
+    @jsondata:Name {value: "fulfillment_id"}
     int fulfillmentId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     anydata? province?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int id?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
     anydata? longitude?;
     string status?;
@@ -2488,90 +3400,148 @@
 
 type SingleOrderRiskRisk record {
     string score?;
+    @jsondata:Name {value: "checkout_id"}
     anydata? checkoutId?;
     boolean display?;
     string recommendation?;
+    @jsondata:Name {value: "cause_cancel"}
     boolean causeCancel?;
+    @jsondata:Name {value: "merchant_message"}
     string merchantMessage?;
     int id?;
     string 'source?;
     string message?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
 };
 
 
 type ApproveCommentResponse record {
+    @jsondata:Name {value: "blog_id"}
     int blogId?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     string author?;
     string ip?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string body?;
+    @jsondata:Name {value: "article_id"}
     int articleId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
     string email?;
+    @jsondata:Name {value: "user_agent"}
     string userAgent?;
     string status?;
 };
 
 
 type CompleteCheckoutResponseCheckout record {
+    @jsondata:Name {value: "privacy_policy_url"}
     anydata? privacyPolicyUrl?;
+    @jsondata:Name {value: "payment_url"}
     string paymentUrl?;
+    @jsondata:Name {value: "refund_policy_url"}
     anydata? refundPolicyUrl?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "terms_of_sale_url"}
     anydata? termsOfSaleUrl?;
+    @jsondata:Name {value: "billing_address"}
     SinglePaymentResponsePaymentCheckoutBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     CompleteCheckoutResponseCheckoutLineItems[] lineItems?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "reservation_time_left"}
     int reservationTimeLeft?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "payment_due"}
     string paymentDue?;
+    @jsondata:Name {value: "source_identifier"}
     anydata? sourceIdentifier?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
+    @jsondata:Name {value: "customer_locale"}
     anydata? customerLocale?;
+    @jsondata:Name {value: "tax_manipulations"}
     anydata[] taxManipulations?;
     anydata? 'order?;
+    @jsondata:Name {value: "terms_of_service_url"}
     anydata? termsOfServiceUrl?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "subscription_policy_url"}
     anydata? subscriptionPolicyUrl?;
+    @jsondata:Name {value: "order_status_url"}
     anydata? orderStatusUrl?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "discount_code"}
     anydata? discountCode?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
+    @jsondata:Name {value: "completed_at"}
     anydata? completedAt?;
+    @jsondata:Name {value: "shipping_rate"}
     anydata? shippingRate?;
     anydata? phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     SinglePaymentResponsePaymentCheckoutNoteAttributes noteAttributes?;
     string name?;
+    @jsondata:Name {value: "shipping_line"}
     anydata? shippingLine?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
     string? note?;
+    @jsondata:Name {value: "applied_discount"}
     anydata? appliedDiscount?;
     anydata[] payments?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "shopify_payments_account_id"}
     anydata? shopifyPaymentsAccountId?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string currency?;
+    @jsondata:Name {value: "shipping_address"}
     SinglePaymentResponsePaymentCheckoutBillingAddress|() shippingAddress?;
     string email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "legal_notice_url"}
     anydata? legalNoticeUrl?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
+    @jsondata:Name {value: "reservation_time"}
     anydata? reservationTime?;
+    @jsondata:Name {value: "total_tip_received"}
     string totalTipReceived?;
     string token?;
+    @jsondata:Name {value: "credit_card"}
     anydata? creditCard?;
+    @jsondata:Name {value: "gift_cards"}
     anydata[] giftCards?;
+    @jsondata:Name {value: "web_url"}
     string webUrl?;
+    @jsondata:Name {value: "shipping_policy_url"}
     anydata? shippingPolicyUrl?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
 };
 
@@ -2582,35 +3552,49 @@
     string address2?;
     string city?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     string province?;
     string phone?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
 };
 
 
 type CompleteCheckoutResponseCheckoutLineItems record {
+    @jsondata:Name {value: "variant_title"}
     string? variantTitle?;
+    @jsondata:Name {value: "line_price"}
     string linePrice?;
+    @jsondata:Name {value: "compare_at_price"}
     anydata? compareAtPrice?;
     int quantity?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
     boolean taxable?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "image_url"}
     string imageUrl?;
     string title?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
     string price?;
     string vendor?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     int id?;
     int grams?;
     string? sku?;
+    @jsondata:Name {value: "applied_discounts"}
     anydata[] appliedDiscounts?;
     int 'key?;
     record {|anydata...;|} properties?;
@@ -2619,37 +3603,54 @@
 
 type SinglePaymentResponsePaymentCheckoutNoteAttributes record {
     string colour?;
+    @jsondata:Name {value: "custom engraving"}
     string customEngraving?;
 };
 
 
 type UpdateFulfillmentServiceFulfillmentService record {
+    @jsondata:Name {value: "callback_url"}
     string callbackUrl?;
+    @jsondata:Name {value: "inventory_management"}
     boolean inventoryManagement?;
+    @jsondata:Name {value: "service_name"}
     string serviceName?;
+    @jsondata:Name {value: "fulfillment_orders_opt_in"}
     boolean fulfillmentOrdersOptIn?;
     string name?;
+    @jsondata:Name {value: "provider_id"}
     anydata? providerId?;
     string 'handle?;
     int id?;
+    @jsondata:Name {value: "include_pending_stock"}
     boolean includePendingStock?;
     anydata? email?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
+    @jsondata:Name {value: "tracking_support"}
     boolean trackingSupport?;
 };
 
 
 type OriginalFulfillmentOrderUnsubmittedFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     FulfillmentOrdersAssignedLocation origin?;
     OriginalFulfillmentOrderUnsubmittedFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     OriginalFulfillmentOrderUnsubmittedFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "outgoing_requests"}
     anydata[] outgoingRequests?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     string[] supportedActions?;
     string status?;
 };
@@ -2663,38 +3664,53 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
 
 
 type OriginalFulfillmentOrderUnsubmittedFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
 
 
 type ResourceFeedbackList record {
+    @jsondata:Name {value: "resource_feedback"}
     ResourceFeedbackListResourceFeedback[] resourceFeedback?;
 };
 
 
 type ResourceFeedbackListResourceFeedback record {
+    @jsondata:Name {value: "resource_updated_at"}
     anydata? resourceUpdatedAt?;
+    @jsondata:Name {value: "feedback_generated_at"}
     string feedbackGeneratedAt?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "resource_type"}
     string resourceType?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string[] messages?;
+    @jsondata:Name {value: "resource_id"}
     int resourceId?;
     string state?;
 };
@@ -2703,42 +3719,60 @@
 type CompleteCheckoutCheckoutOrder record {
     string name?;
     int id?;
+    @jsondata:Name {value: "status_url"}
     string statusUrl?;
 };
 
 
 type CreateFulfillmentServiceFulfillmentService record {
+    @jsondata:Name {value: "callback_url"}
     string callbackUrl?;
+    @jsondata:Name {value: "inventory_management"}
     boolean inventoryManagement?;
+    @jsondata:Name {value: "service_name"}
     string serviceName?;
+    @jsondata:Name {value: "fulfillment_orders_opt_in"}
     boolean fulfillmentOrdersOptIn?;
     string name?;
+    @jsondata:Name {value: "provider_id"}
     anydata? providerId?;
     string 'handle?;
     int id?;
+    @jsondata:Name {value: "include_pending_stock"}
     boolean includePendingStock?;
     anydata? email?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
+    @jsondata:Name {value: "tracking_support"}
     boolean trackingSupport?;
 };
 
 
 type AdminapiapiVersionshopifyPaymentsdisputesdisputeIddisputeEvidencesJsonDisputeEvidence record {
+    @jsondata:Name {value: "submit_evidence"}
     boolean submitEvidence?;
 };
 
 
 type OriginalFulfillmentOrderSubmittedFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     FulfillmentOrdersAssignedLocation origin?;
     OriginalFulfillmentOrderSubmittedFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     OriginalFulfillmentOrderSubmittedFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "outgoing_requests"}
     OriginalFulfillmentOrderSubmittedFulfillmentOrderOutgoingRequests[] outgoingRequests?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     string[] supportedActions?;
     string status?;
 };
@@ -2752,38 +3786,53 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
 
 
 type OriginalFulfillmentOrderSubmittedFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
 
 
 type SpamCommentResponse record {
+    @jsondata:Name {value: "blog_id"}
     int blogId?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     string author?;
     string ip?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string body?;
+    @jsondata:Name {value: "article_id"}
     int articleId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     anydata? publishedAt?;
     string email?;
+    @jsondata:Name {value: "user_agent"}
     string userAgent?;
     string status?;
 };
@@ -2795,31 +3844,47 @@
 
 
 type CappedAmountChargeRecurringApplicationCharge record {
+    @jsondata:Name {value: "update_capped_amount_url"}
     string updateCappedAmountUrl?;
+    @jsondata:Name {value: "api_client_id"}
     int apiClientId?;
     anydata? test?;
+    @jsondata:Name {value: "balance_used"}
     decimal balanceUsed?;
+    @jsondata:Name {value: "balance_remaining"}
     decimal balanceRemaining?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "cancelled_on"}
     anydata? cancelledOn?;
+    @jsondata:Name {value: "trial_days"}
     int trialDays?;
+    @jsondata:Name {value: "decorated_return_url"}
     string decoratedReturnUrl?;
+    @jsondata:Name {value: "capped_amount"}
     string cappedAmount?;
+    @jsondata:Name {value: "risk_level"}
     decimal riskLevel?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string price?;
+    @jsondata:Name {value: "trial_ends_on"}
     string trialEndsOn?;
     string name?;
+    @jsondata:Name {value: "return_url"}
     string returnUrl?;
+    @jsondata:Name {value: "billing_on"}
     anydata? billingOn?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "activated_on"}
     string activatedOn?;
     string status?;
 };
 
 
 type RecurringApplicationChargeIdUsageChargesJsonBody record {
+    @jsondata:Name {value: "usage_charge"}
     AdminapiapiVersionrecurringApplicationChargesrecurringApplicationChargeIdusageChargesJsonUsageCharge usageCharge?;
 };
 
@@ -2827,6 +3892,7 @@
 
 type OrderAdjustment record {
     # The taxes that are added to amount, such as applicable shipping taxes added to a shipping refund
+    @jsondata:Name {value: "tax_amount"}
     string taxAmount?;
     # The reason for the order adjustment. To set this value, include discrepancy_reason when you create a refund
     string reason?;
@@ -2837,8 +3903,10 @@
     # The unique identifier for the order adjustment
     int id?;
     # The unique identifier for the order that the order adjustment is associated with
+    @jsondata:Name {value: "order_id"}
     int orderId?;
     # The unique identifier for the refund that the order adjustment is associated with
+    @jsondata:Name {value: "refund_id"}
     int refundId?;
 };
 
@@ -2849,6 +3917,7 @@
 
 
 type AdminapiapiVersionblogsblogIdarticlesJsonArticle record {
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     string author?;
     boolean published?;
@@ -2858,35 +3927,55 @@
 
 
 type CompleteDraftOrder record {
+    @jsondata:Name {value: "draft_order"}
     CompleteDraftOrderDraftOrder draftOrder?;
 };
 
 
 type CompleteDraftOrderDraftOrder record {
     string? note?;
+    @jsondata:Name {value: "applied_discount"}
     CompleteDraftOrderDraftOrderAppliedDiscount|() appliedDiscount?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "billing_address"}
     ReopenCloseOrderOrderBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     ModifyDraftOrderDraftOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "shipping_address"}
     ReopenCloseOrderOrderBillingAddress|() shippingAddress?;
     string email?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "invoice_sent_at"}
     anydata? invoiceSentAt?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
     string tags?;
+    @jsondata:Name {value: "completed_at"}
     string completedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "note_attributes"}
     anydata[] noteAttributes?;
     string name?;
+    @jsondata:Name {value: "shipping_line"}
     ModifyDraftOrderDraftOrderShippingLine|() shippingLine?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "invoice_url"}
     string invoiceUrl?;
     AbandonedCheckoutsCustomer customer?;
     string status?;
@@ -2901,18 +3990,26 @@
 type SingleUserUser record {
     anydata? im?;
     anydata? bio?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     string locale?;
+    @jsondata:Name {value: "account_owner"}
     boolean accountOwner?;
     string url?;
+    @jsondata:Name {value: "receive_announcements"}
     int receiveAnnouncements?;
+    @jsondata:Name {value: "user_type"}
     string userType?;
     anydata? phone?;
+    @jsondata:Name {value: "screen_name"}
     anydata? screenName?;
     string[] permissions?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "tfa_enabled?"}
     boolean tfaEnabled?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
@@ -2927,10 +4024,12 @@
 
 type Product record {
     # A description of the product. Supports HTML formatting
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     # A list of product image objects, each one representing an image associated with the product
     ProductImage[] images?;
     # The date and time (ISO 8601 format) when the product was created
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     # A unique human-friendly string for the product. Automatically generated from the product's title. Used by the Liquid templating language to refer to objects
     string 'handle?;
@@ -2941,12 +4040,16 @@
     # A string of comma-separated tags that are used for filtering and search. A product can have up to 250 tags. Each tag can have up to 255 characters
     string tags?;
     # Whether the product is published to the Point of Sale channel
+    @jsondata:Name {value: "published_scope"}
     string publishedScope?;
     # A categorization for the product used for filtering and searching products
+    @jsondata:Name {value: "product_type"}
     string productType?;
     # The suffix of the Liquid template used for the product page. If this property is specified, then the product page uses a template called "product.suffix.liquid", where "suffix" is the value of this property. If this property is "" or null, then the product page uses the default template "product.liquid". (default is null)
+    @jsondata:Name {value: "template_suffix"}
     string templateSuffix?;
     # The date and time (ISO 8601 format) when the product was last modified. A product's updated_at value can change for different reasons. For example, if an order is placed for a product that has inventory tracking set up, then the inventory adjustment is counted as an update
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     # The name of the product's vendor
     string vendor?;
@@ -2955,6 +4058,7 @@
     # An unsigned 64-bit integer that's used as a unique identifier for the product. Each id is unique across the Shopify system. No two products will have the same id, even if they're from different shops
     int id?;
     # The date and time (ISO 8601 format) when the product was published. Can be set to null to unpublish the product from the Online Store channel
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
     # The status of the product
     string status?;
@@ -2964,26 +4068,35 @@
 
 type ProductVariant record {
     # A list of the variant's presentment prices and compare-at prices in each of the shop's enabled presentment currencies.
+    @jsondata:Name {value: "presentment_prices"}
     PresentmentPrices presentmentPrices?;
     # The fulfillment service that tracks the number of items in stock for the product variant
+    @jsondata:Name {value: "inventory_management"}
     string inventoryManagement?;
     # This property is deprecated. Use the InventoryLevel resource instead
+    @jsondata:Name {value: "old_inventory_quantity"}
     int oldInventoryQuantity?;
     # This property is deprecated. Use the `requires_shipping` property on the InventoryItem resource instead
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
     # The date and time (ISO 8601 format) when the product variant was created
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     # The title of the product variant. The title field is a concatenation of the option1, option2, and option3 fields. You can only update title indirectly using the option fields
     string title?;
     # This property is deprecated. Use the InventoryLevel resource instead
+    @jsondata:Name {value: "inventory_quantity_adjustment"}
     int inventoryQuantityAdjustment?;
     # The date and time when the product variant was last modified. Gets returned in ISO 8601 formatting
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     # The unique identifier for the inventory item, which is used in the Inventory API to query for inventory information
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     # The price of the product variant
     string price?;
     # The unique numeric identifier for the product
+    @jsondata:Name {value: "product_id"}
     int productId?;
     # The unique numeric identifier for the product variant
     int id?;
@@ -2994,24 +4107,31 @@
     # The barcode, UPC, or ISBN number for the product
     string barcode?;
     # An aggregate of inventory across all locations. To adjust inventory at a specific location, use the InventoryLevel resource
+    @jsondata:Name {value: "inventory_quantity"}
     int inventoryQuantity?;
     # The original price of the item before an adjustment or a sale
+    @jsondata:Name {value: "compare_at_price"}
     string compareAtPrice?;
     # The fulfillment service associated with the product variant. Valid values are manual or the handle of a fulfillment service
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     # Whether a tax is charged when the product variant is sold
     boolean taxable?;
     # The weight of the product variant in the unit system specified with weight_unit
     int weight?;
     # Whether customers are allowed to place an order for the product variant when it's out of stock
+    @jsondata:Name {value: "inventory_policy"}
     string inventoryPolicy?;
     # This parameter applies only to the stores that have the Avalara AvaTax app installed. Specifies the Avalara tax code for the product variant
+    @jsondata:Name {value: "tax_code"}
     string taxCode?;
     # The unit of measurement that applies to the product variant's weight. If you don't specify a value for weight_unit, then the shop's default unit of measurement is applied. Valid values are g, kg, oz, and lb
+    @jsondata:Name {value: "weight_unit"}
     string weightUnit?;
     # The order of the product variant in the list of product variants. The first position in the list is 1. The position of variants is indicated by the order in which they are listed
     int position?;
     # The unique numeric identifier for a product's image. The image must be associated to the same product as the variant
+    @jsondata:Name {value: "image_id"}
     int imageId?;
     # The custom properties that a shop owner uses to define product variants. You can define three options for a product variant are option1, option2, option3. Default value is Default Title. The title field is a concatenation of the option1, option2, and option3 fields. Updating the option fields updates the title field
     Option option?;
@@ -3032,6 +4152,7 @@
 
 type ProductOption record {
     # Product option product ID
+    @jsondata:Name {value: "product_id"}
     int productId?;
     # Product option values
     string[] values?;
@@ -3045,45 +4166,74 @@
 
 
 type SinglePriceRulePriceRule record {
+    @jsondata:Name {value: "once_per_customer"}
     boolean oncePerCustomer?;
+    @jsondata:Name {value: "starts_at"}
     string startsAt?;
+    @jsondata:Name {value: "usage_limit"}
     anydata? usageLimit?;
+    @jsondata:Name {value: "value_type"}
     string valueType?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "prerequisite_customer_ids"}
     anydata[] prerequisiteCustomerIds?;
     string title?;
+    @jsondata:Name {value: "entitled_collection_ids"}
     anydata[] entitledCollectionIds?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "prerequisite_product_ids"}
     anydata[] prerequisiteProductIds?;
+    @jsondata:Name {value: "prerequisite_shipping_price_range"}
     anydata? prerequisiteShippingPriceRange?;
+    @jsondata:Name {value: "entitled_country_ids"}
     anydata[] entitledCountryIds?;
+    @jsondata:Name {value: "entitled_variant_ids"}
     anydata[] entitledVariantIds?;
+    @jsondata:Name {value: "ends_at"}
     string? endsAt?;
     int id?;
     string value?;
+    @jsondata:Name {value: "prerequisite_subtotal_range"}
     anydata? prerequisiteSubtotalRange?;
+    @jsondata:Name {value: "allocation_method"}
     string allocationMethod?;
+    @jsondata:Name {value: "prerequisite_to_entitlement_quantity_ratio"}
     UpdatePriceRulePriceRulePrerequisiteToEntitlementQuantityRatio prerequisiteToEntitlementQuantityRatio?;
+    @jsondata:Name {value: "prerequisite_quantity_range"}
     anydata? prerequisiteQuantityRange?;
+    @jsondata:Name {value: "allocation_limit"}
     anydata? allocationLimit?;
+    @jsondata:Name {value: "target_type"}
     string targetType?;
+    @jsondata:Name {value: "entitled_product_ids"}
     anydata[] entitledProductIds?;
+    @jsondata:Name {value: "customer_selection"}
     string customerSelection?;
+    @jsondata:Name {value: "prerequisite_saved_search_ids"}
     anydata[] prerequisiteSavedSearchIds?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "prerequisite_variant_ids"}
     anydata[] prerequisiteVariantIds?;
+    @jsondata:Name {value: "target_selection"}
     string targetSelection?;
+    @jsondata:Name {value: "prerequisite_collection_ids"}
     anydata[] prerequisiteCollectionIds?;
 };
 
 
 type UpdatePriceRulePriceRulePrerequisiteToEntitlementQuantityRatio record {
+    @jsondata:Name {value: "prerequisite_quantity"}
     anydata? prerequisiteQuantity?;
+    @jsondata:Name {value: "entitled_quantity"}
     anydata? entitledQuantity?;
 };
 
 
 type FulfillmentOrdersList record {
+    @jsondata:Name {value: "fulfillment_orders"}
     FulfillmentOrdersListFulfillmentOrders[] fulfillmentOrders?;
 };
 
@@ -3097,14 +4247,18 @@
 
 type CreateOrderRiskRisk record {
     string score?;
+    @jsondata:Name {value: "checkout_id"}
     int checkoutId?;
     boolean display?;
     string recommendation?;
+    @jsondata:Name {value: "cause_cancel"}
     boolean causeCancel?;
+    @jsondata:Name {value: "merchant_message"}
     string merchantMessage?;
     int id?;
     string 'source?;
     string message?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
 };
 
@@ -3117,10 +4271,14 @@
 
 type ThemesListThemes record {
     string role?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "theme_store_id"}
     int? themeStoreId?;
     string name?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     boolean processing?;
     int id?;
@@ -3131,12 +4289,15 @@
 
 type ReturnAListOfAllDisputesQueries record {
     # Return only disputes before the specified ID. 
+    @http:Query {name: "last_id"}
     string lastId?;
     # Return only disputes after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Return only disputes with the specified `initiated_at` date ([ISO 8601][1] format). 
 
 [1]: https://en.wikipedia.org/wiki/ISO_8601
+    @http:Query {name: "initiated_at"}
     string initiatedAt?;
     # Return only disputes with the specified status. 
     string status?;
@@ -3144,18 +4305,24 @@
 
 
 type ShippingRates record {
+    @jsondata:Name {value: "shipping_rates"}
     anydata[] shippingRates?;
 };
 
 
 type UpdateProductProductImages record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string src?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     anydata? alt?;
     int width?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "variant_ids"}
     anydata[] variantIds?;
     int id?;
     int position?;
@@ -3164,12 +4331,18 @@
 
 
 type AcceptFulfillmentResponseFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
@@ -3178,18 +4351,23 @@
 
 type RetrieveAListOfAllScriptTagsQueries record {
     # Show script tags created after this date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show script tags created before this date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Show script tags last updated before this date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show script tags last updated after this date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Show script tags with this URL. 
     string src?;
     # The number of results to return.(default: 50)(maximum: 250) 
     string 'limit?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # A comma-separated list of fields to include in the response. 
     string fields?;
@@ -3197,19 +4375,28 @@
 
 
 type MobilePlatformApplicationResponse record {
+    @jsondata:Name {value: "mobile_platform_application"}
     MobilePlatformApplicationResponseMobilePlatformApplication mobilePlatformApplication?;
 };
 
 
 type MobilePlatformApplicationResponseMobilePlatformApplication record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "sha256_cert_fingerprints"}
     anydata[] sha256CertFingerprints?;
+    @jsondata:Name {value: "enabled_app_clips"}
     boolean enabledAppClips?;
+    @jsondata:Name {value: "enabled_universal_or_app_links"}
     boolean enabledUniversalOrAppLinks?;
     int id?;
+    @jsondata:Name {value: "app_clip_application_id"}
     anydata? appClipApplicationId?;
+    @jsondata:Name {value: "enabled_shared_webcredentials"}
     boolean enabledSharedWebcredentials?;
+    @jsondata:Name {value: "application_id"}
     string applicationId?;
     string platform?;
 };
@@ -3217,10 +4404,14 @@
 
 type DeleteThemeResponse record {
     string role?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "theme_store_id"}
     anydata? themeStoreId?;
     string name?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     boolean processing?;
     int id?;
@@ -3229,24 +4420,29 @@
 
 
 type AdminapiapiVersionordersorderIdrefundscalculateJsonRefund record {
+    @jsondata:Name {value: "refund_line_items"}
     AdminapiapiVersionordersorderIdrefundscalculateJsonRefundRefundLineItems[] refundLineItems?;
     AdminapiapiVersionordersorderIdrefundscalculateJsonRefundShipping shipping?;
 };
 
 
 type AdminapiapiVersionordersorderIdrefundscalculateJsonRefundRefundLineItems record {
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "restock_type"}
     string restockType?;
 };
 
 
 type AdminapiapiVersionordersorderIdrefundscalculateJsonRefundShipping record {
+    @jsondata:Name {value: "full_refund"}
     boolean fullRefund?;
 };
 
 
 type MobilePlatformApplications record {
+    @jsondata:Name {value: "mobile_platform_applications"}
     MobilePlatformApplicationsMobilePlatformApplications[] mobilePlatformApplications?;
 };
 
@@ -3262,82 +4458,139 @@
 
 
 type SinglePaymentResponsePaymentCheckout record {
+    @jsondata:Name {value: "privacy_policy_url"}
     anydata? privacyPolicyUrl?;
+    @jsondata:Name {value: "payment_url"}
     string paymentUrl?;
+    @jsondata:Name {value: "refund_policy_url"}
     anydata? refundPolicyUrl?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "terms_of_sale_url"}
     anydata? termsOfSaleUrl?;
+    @jsondata:Name {value: "billing_address"}
     SinglePaymentResponsePaymentCheckoutBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     SinglePaymentResponsePaymentCheckoutLineItems[] lineItems?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "reservation_time_left"}
     int reservationTimeLeft?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "payment_due"}
     string paymentDue?;
+    @jsondata:Name {value: "source_identifier"}
     anydata? sourceIdentifier?;
+    @jsondata:Name {value: "tax_lines"}
     SinglePaymentResponsePaymentCheckoutTaxLines[] taxLines?;
+    @jsondata:Name {value: "customer_locale"}
     anydata? customerLocale?;
+    @jsondata:Name {value: "tax_manipulations"}
     anydata[] taxManipulations?;
     anydata? 'order?;
+    @jsondata:Name {value: "terms_of_service_url"}
     anydata? termsOfServiceUrl?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "subscription_policy_url"}
     anydata? subscriptionPolicyUrl?;
+    @jsondata:Name {value: "order_status_url"}
     anydata? orderStatusUrl?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "discount_code"}
     anydata? discountCode?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
+    @jsondata:Name {value: "completed_at"}
     anydata? completedAt?;
+    @jsondata:Name {value: "shipping_rate"}
     SinglePaymentResponsePaymentCheckoutShippingRate shippingRate?;
     anydata? phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     SinglePaymentResponsePaymentCheckoutNoteAttributes noteAttributes?;
     string name?;
+    @jsondata:Name {value: "shipping_line"}
     SinglePaymentResponsePaymentCheckoutShippingLine|() shippingLine?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
     string? note?;
+    @jsondata:Name {value: "applied_discount"}
     anydata? appliedDiscount?;
     SinglePaymentResponsePaymentCheckoutPayments[] payments?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "shopify_payments_account_id"}
     anydata? shopifyPaymentsAccountId?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string currency?;
+    @jsondata:Name {value: "shipping_address"}
     SinglePaymentResponsePaymentCheckoutBillingAddress|() shippingAddress?;
     string email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "legal_notice_url"}
     anydata? legalNoticeUrl?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
+    @jsondata:Name {value: "reservation_time"}
     anydata? reservationTime?;
+    @jsondata:Name {value: "total_tip_received"}
     string totalTipReceived?;
     string token?;
+    @jsondata:Name {value: "credit_card"}
     SinglePaymentResponsePaymentCheckoutCreditCard creditCard?;
+    @jsondata:Name {value: "gift_cards"}
     anydata[] giftCards?;
+    @jsondata:Name {value: "web_url"}
     string webUrl?;
+    @jsondata:Name {value: "shipping_policy_url"}
     anydata? shippingPolicyUrl?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
 };
 
 
 type SinglePaymentResponsePaymentCheckoutLineItems record {
+    @jsondata:Name {value: "variant_title"}
     string? variantTitle?;
+    @jsondata:Name {value: "line_price"}
     string linePrice?;
+    @jsondata:Name {value: "compare_at_price"}
     anydata? compareAtPrice?;
     int quantity?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
     boolean taxable?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "image_url"}
     string imageUrl?;
     string title?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
     string price?;
     string vendor?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     string id?;
     int grams?;
     string? sku?;
+    @jsondata:Name {value: "applied_discounts"}
     anydata[] appliedDiscounts?;
     string 'key?;
     record {|anydata...;|} properties?;
@@ -3345,6 +4598,7 @@
 
 
 type SinglePaymentResponsePaymentCheckoutTaxLines record {
+    @jsondata:Name {value: "compare_at"}
     decimal compareAt?;
     decimal rate?;
     string price?;
@@ -3367,8 +4621,11 @@
 
 
 type SinglePaymentResponsePaymentCheckoutPayments record {
+    @jsondata:Name {value: "unique_token"}
     string uniqueToken?;
+    @jsondata:Name {value: "credit_card"}
     anydata? creditCard?;
+    @jsondata:Name {value: "payment_processing_error_message"}
     anydata? paymentProcessingErrorMessage?;
     int id?;
     SinglePaymentResponsePaymentCheckoutTransaction 'transaction?;
@@ -3377,21 +4634,31 @@
 
 
 type SinglePaymentResponsePaymentCheckoutTransaction record {
+    @jsondata:Name {value: "amount_in"}
     anydata? amountIn?;
     string amount?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
     boolean test?;
     string kind?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     anydata? message?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "amount_out"}
     anydata? amountOut?;
     anydata? authorization?;
+    @jsondata:Name {value: "transaction_group_id"}
     anydata? transactionGroupId?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "parent_id"}
     anydata? parentId?;
+    @jsondata:Name {value: "amount_rounding"}
     anydata? amountRounding?;
     string currency?;
+    @jsondata:Name {value: "error_code"}
     anydata? errorCode?;
     record {|anydata...;|} receipt?;
     int id?;
@@ -3401,13 +4668,20 @@
 
 
 type SinglePaymentResponsePaymentCheckoutCreditCard record {
+    @jsondata:Name {value: "expiry_month"}
     int expiryMonth?;
+    @jsondata:Name {value: "first_digits"}
     string firstDigits?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "customer_id"}
     anydata? customerId?;
     string brand?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
+    @jsondata:Name {value: "last_digits"}
     string lastDigits?;
+    @jsondata:Name {value: "expiry_year"}
     int expiryYear?;
 };
 
@@ -3420,13 +4694,19 @@
     anydata? city?;
     anydata? address1?;
     boolean active?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "province_code"}
     anydata? provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     anydata? province?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     anydata? phone?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "country_name"}
     string countryName?;
     string name?;
     int id?;
@@ -3434,7 +4714,9 @@
 
 
 type AdminapiapiVersionproductsproductIdresourceFeedbackJsonResourceFeedback record {
+    @jsondata:Name {value: "resource_updated_at"}
     string resourceUpdatedAt?;
+    @jsondata:Name {value: "feedback_generated_at"}
     string feedbackGeneratedAt?;
     string[] messages?;
     string state?;
@@ -3444,24 +4726,32 @@
 
 type RetrieveAListOfPagesQueries record {
     # Show pages created after date (format: 2008-12-31). 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show pages created before date (format: 2008-12-31). 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Show pages last updated before date (format: 2008-12-31). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show pages last updated after date (format: 2008-12-31). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Show pages published after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_min"}
     string publishedAtMin?;
     # The maximum number of results to show.(default: 50)(maximum: 250) 
     string 'limit?;
     # Show pages published before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_max"}
     string publishedAtMax?;
     # Retrieve a page with a given handle. 
     string 'handle?;
     # Restrict results to pages with a given published status:(default: any) 
+    @http:Query {name: "published_status"}
     string publishedStatus?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Retrieve pages with a given title. 
     string title?;
@@ -3472,20 +4762,32 @@
 
 type GiftCardSearchGiftCards record {
     anydata? note?;
+    @jsondata:Name {value: "initial_value"}
     string initialValue?;
+    @jsondata:Name {value: "line_item_id"}
     anydata? lineItemId?;
+    @jsondata:Name {value: "api_client_id"}
     anydata? apiClientId?;
+    @jsondata:Name {value: "disabled_at"}
     anydata? disabledAt?;
+    @jsondata:Name {value: "expires_on"}
     anydata? expiresOn?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
     string balance?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "customer_id"}
     anydata? customerId?;
+    @jsondata:Name {value: "last_characters"}
     string lastCharacters?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
 };
 
@@ -3496,29 +4798,41 @@
 
 
 type AdminapiapiVersioncheckoutstokenpaymentsJsonPaymentRequestDetails record {
+    @jsondata:Name {value: "accept_language"}
     string acceptLanguage?;
+    @jsondata:Name {value: "ip_address"}
     string ipAddress?;
+    @jsondata:Name {value: "user_agent"}
     string userAgent?;
 };
 
 
 type SinglePriceRule record {
+    @jsondata:Name {value: "price_rule"}
     SinglePriceRulePriceRule priceRule?;
 };
 
 
 type UpdateInventoryItemInventoryItem record {
     string cost?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "province_code_of_origin"}
     anydata? provinceCodeOfOrigin?;
     boolean tracked?;
+    @jsondata:Name {value: "country_code_of_origin"}
     anydata? countryCodeOfOrigin?;
     int id?;
     string? sku?;
+    @jsondata:Name {value: "country_harmonized_system_codes"}
     anydata[] countryHarmonizedSystemCodes?;
+    @jsondata:Name {value: "harmonized_system_code"}
     anydata? harmonizedSystemCode?;
 };
 
@@ -3533,82 +4847,139 @@
 
 
 type CreateCheckoutResponseCheckout record {
+    @jsondata:Name {value: "privacy_policy_url"}
     anydata? privacyPolicyUrl?;
+    @jsondata:Name {value: "payment_url"}
     string paymentUrl?;
+    @jsondata:Name {value: "refund_policy_url"}
     anydata? refundPolicyUrl?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "terms_of_sale_url"}
     anydata? termsOfSaleUrl?;
+    @jsondata:Name {value: "billing_address"}
     anydata? billingAddress?;
+    @jsondata:Name {value: "line_items"}
     CreateCheckoutResponseCheckoutLineItems[] lineItems?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "reservation_time_left"}
     int reservationTimeLeft?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "payment_due"}
     string paymentDue?;
+    @jsondata:Name {value: "source_identifier"}
     anydata? sourceIdentifier?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
+    @jsondata:Name {value: "customer_locale"}
     string customerLocale?;
+    @jsondata:Name {value: "tax_manipulations"}
     anydata[] taxManipulations?;
     anydata? 'order?;
+    @jsondata:Name {value: "terms_of_service_url"}
     anydata? termsOfServiceUrl?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "subscription_policy_url"}
     anydata? subscriptionPolicyUrl?;
+    @jsondata:Name {value: "order_status_url"}
     anydata? orderStatusUrl?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "discount_code"}
     anydata? discountCode?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
+    @jsondata:Name {value: "completed_at"}
     anydata? completedAt?;
+    @jsondata:Name {value: "shipping_rate"}
     anydata? shippingRate?;
     anydata? phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     record {|anydata...;|} noteAttributes?;
     string name?;
+    @jsondata:Name {value: "shipping_line"}
     anydata? shippingLine?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
     string? note?;
+    @jsondata:Name {value: "applied_discount"}
     anydata? appliedDiscount?;
     anydata[] payments?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "shopify_payments_account_id"}
     anydata? shopifyPaymentsAccountId?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string currency?;
+    @jsondata:Name {value: "shipping_address"}
     anydata? shippingAddress?;
     string? email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "legal_notice_url"}
     anydata? legalNoticeUrl?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
+    @jsondata:Name {value: "reservation_time"}
     anydata? reservationTime?;
+    @jsondata:Name {value: "total_tip_received"}
     string totalTipReceived?;
     string token?;
+    @jsondata:Name {value: "credit_card"}
     anydata? creditCard?;
+    @jsondata:Name {value: "gift_cards"}
     anydata[] giftCards?;
+    @jsondata:Name {value: "web_url"}
     string webUrl?;
+    @jsondata:Name {value: "shipping_policy_url"}
     anydata? shippingPolicyUrl?;
+    @jsondata:Name {value: "customer_id"}
     int? customerId?;
 };
 
 
 type CreateCheckoutResponseCheckoutLineItems record {
+    @jsondata:Name {value: "variant_title"}
     string? variantTitle?;
+    @jsondata:Name {value: "line_price"}
     string linePrice?;
+    @jsondata:Name {value: "compare_at_price"}
     anydata? compareAtPrice?;
     int quantity?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
     boolean taxable?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "image_url"}
     string imageUrl?;
     string title?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
     string price?;
     string vendor?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     string id?;
     int grams?;
     string? sku?;
+    @jsondata:Name {value: "applied_discounts"}
     anydata[] appliedDiscounts?;
     string 'key?;
     record {|anydata...;|} properties?;
@@ -3616,15 +4987,22 @@
 
 
 type ApplicationChargesListApplicationCharges record {
+    @jsondata:Name {value: "charge_type"}
     string? chargeType?;
+    @jsondata:Name {value: "api_client_id"}
     int apiClientId?;
     anydata? test?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "external_id"}
     anydata? externalId?;
+    @jsondata:Name {value: "decorated_return_url"}
     string decoratedReturnUrl?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string price?;
     string name?;
+    @jsondata:Name {value: "return_url"}
     string returnUrl?;
     string currency?;
     int id?;
@@ -3640,9 +5018,11 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
@@ -3656,15 +5036,18 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
 
 
 type AdminapiapiVersionproductListingsproductListingIdJsonProductListing record {
+    @jsondata:Name {value: "product_id"}
     int? productId?;
 };
 
@@ -3677,10 +5060,13 @@
 
 type RetrieveProductListingsThatArePublishedToYourAppQueries record {
     # Filter by products belonging to a particular collection 
+    @http:Query {name: "collection_id"}
     string collectionId?;
     # A comma-separated list of product ids 
+    @http:Query {name: "product_ids"}
     string productIds?;
     # Filter by products last updated after a certain date and time (formatted in ISO 8601) 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Amount of results(default: 50)(maximum: 1000) 
     string 'limit?;
@@ -3692,12 +5078,18 @@
 
 
 type CancelFulfillmentOrderReplacementFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
@@ -3706,35 +5098,48 @@
 type AdminapiapiVersionreportsreportIdJsonReport record {
     string name?;
     int id?;
+    @jsondata:Name {value: "shopify_ql"}
     string shopifyQl?;
 };
 
 
 type ProductListingsOptionValues record {
     string name?;
+    @jsondata:Name {value: "option_id"}
     int optionId?;
     string value?;
 };
 
 
 type MarketingEventsmarketingEventIdJsonBody record {
+    @jsondata:Name {value: "marketing_event"}
     AdminapiapiVersionmarketingEventsmarketingEventIdJsonMarketingEvent marketingEvent?;
 };
 
 
 type AdminapiapiVersionmarketingEventsmarketingEventIdJsonMarketingEvent record {
+    @jsondata:Name {value: "utm_campaign"}
     string utmCampaign?;
+    @jsondata:Name {value: "remote_id"}
     string remoteId?;
+    @jsondata:Name {value: "utm_medium"}
     string utmMedium?;
+    @jsondata:Name {value: "event_type"}
     string eventType?;
+    @jsondata:Name {value: "started_at"}
     string startedAt?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "scheduled_to_end_at"}
     string scheduledToEndAt?;
+    @jsondata:Name {value: "budget_type"}
     string budgetType?;
+    @jsondata:Name {value: "ended_at"}
     string endedAt?;
     string budget?;
+    @jsondata:Name {value: "referring_domain"}
     string referringDomain?;
+    @jsondata:Name {value: "utm_source"}
     string utmSource?;
 };
 
@@ -3745,21 +5150,27 @@
 
 
 type Metafield record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt;
+    @jsondata:Name {value: "owner_id"}
     int ownerId;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId;
     string namespace;
     string? description?;
+    @jsondata:Name {value: "created_at"}
     string createdAt;
     int id;
     string 'type;
     string value;
+    @jsondata:Name {value: "owner_resource"}
     string ownerResource;
     string 'key;
 };
 
 
 type LocationsList record {
+    @jsondata:Name {value: "locations_for_move"}
     LocationsListLocationsForMove[] locationsForMove?;
 };
 
@@ -3769,12 +5180,16 @@
     # Filter response to payouts on the specified date. 
     string date?;
     # Filter response to payouts inclusively after the specified date. 
+    @http:Query {name: "date_min"}
     string dateMin?;
     # Filter response to payouts inclusively before the specified date. 
+    @http:Query {name: "date_max"}
     string dateMax?;
     # Filter response to payouts exclusively before the specified ID 
+    @http:Query {name: "last_id"}
     string lastId?;
     # Filter response to payouts exclusively after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Filter response to payouts with the specified status 
     string status?;
@@ -3784,83 +5199,139 @@
 
 type RetrieveACountOfProductsQueries record {
     # Filter results by collection ID. 
+    @http:Query {name: "collection_id"}
     string collectionId?;
     # Show products created after date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show products created before date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Show products last updated before date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Filter results by product type. 
+    @http:Query {name: "product_type"}
     string productType?;
     # Show products last updated after date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Filter results by product vendor. 
     string vendor?;
     # Show products published after date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "published_at_min"}
     string publishedAtMin?;
     # Show products published before date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "published_at_max"}
     string publishedAtMax?;
     # Return products by their published status(default: any) 
+    @http:Query {name: "published_status"}
     string publishedStatus?;
 };
 
 
 type CompleteCheckoutCheckout record {
+    @jsondata:Name {value: "privacy_policy_url"}
     anydata? privacyPolicyUrl?;
+    @jsondata:Name {value: "payment_url"}
     string paymentUrl?;
+    @jsondata:Name {value: "refund_policy_url"}
     anydata? refundPolicyUrl?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "terms_of_sale_url"}
     anydata? termsOfSaleUrl?;
+    @jsondata:Name {value: "billing_address"}
     SinglePaymentResponsePaymentCheckoutBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     SinglePaymentResponsePaymentCheckoutLineItems[] lineItems?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "reservation_time_left"}
     int reservationTimeLeft?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "payment_due"}
     string paymentDue?;
+    @jsondata:Name {value: "source_identifier"}
     anydata? sourceIdentifier?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
+    @jsondata:Name {value: "customer_locale"}
     anydata? customerLocale?;
+    @jsondata:Name {value: "tax_manipulations"}
     anydata[] taxManipulations?;
     CompleteCheckoutCheckoutOrder 'order?;
+    @jsondata:Name {value: "terms_of_service_url"}
     anydata? termsOfServiceUrl?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "subscription_policy_url"}
     anydata? subscriptionPolicyUrl?;
+    @jsondata:Name {value: "order_status_url"}
     string orderStatusUrl?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "discount_code"}
     anydata? discountCode?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
+    @jsondata:Name {value: "completed_at"}
     string completedAt?;
+    @jsondata:Name {value: "shipping_rate"}
     SinglePaymentResponsePaymentCheckoutShippingRate shippingRate?;
     anydata? phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     SinglePaymentResponsePaymentCheckoutNoteAttributes noteAttributes?;
     string name?;
+    @jsondata:Name {value: "shipping_line"}
     SinglePaymentResponsePaymentCheckoutShippingLine|() shippingLine?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
     string? note?;
+    @jsondata:Name {value: "applied_discount"}
     anydata? appliedDiscount?;
     anydata[] payments?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "shopify_payments_account_id"}
     anydata? shopifyPaymentsAccountId?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string currency?;
+    @jsondata:Name {value: "shipping_address"}
     CompleteCheckoutCheckoutShippingAddress shippingAddress?;
     string email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "legal_notice_url"}
     anydata? legalNoticeUrl?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
+    @jsondata:Name {value: "reservation_time"}
     anydata? reservationTime?;
+    @jsondata:Name {value: "total_tip_received"}
     string totalTipReceived?;
     string token?;
+    @jsondata:Name {value: "credit_card"}
     anydata? creditCard?;
+    @jsondata:Name {value: "gift_cards"}
     anydata[] giftCards?;
+    @jsondata:Name {value: "web_url"}
     string webUrl?;
+    @jsondata:Name {value: "shipping_policy_url"}
     anydata? shippingPolicyUrl?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
 };
 
@@ -3871,13 +5342,17 @@
     string address2?;
     string city?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     string province?;
     string phone?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
 };
 
@@ -3888,51 +5363,79 @@
 
 
 type FulfillmentListFulfillments record {
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "line_items"}
     FulfillmentListLineItems[] lineItems?;
+    @jsondata:Name {value: "tracking_company"}
     string trackingCompany?;
+    @jsondata:Name {value: "tracking_urls"}
     string[] trackingUrls?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string 'service?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string name?;
+    @jsondata:Name {value: "tracking_number"}
     string trackingNumber?;
     record {|anydata...;|} receipt?;
     int id?;
+    @jsondata:Name {value: "tracking_numbers"}
     string[] trackingNumbers?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "tracking_url"}
     string trackingUrl?;
+    @jsondata:Name {value: "shipment_status"}
     anydata? shipmentStatus?;
     string status?;
 };
 
 
 type FulfillmentListLineItems record {
+    @jsondata:Name {value: "variant_title"}
     string? variantTitle?;
+    @jsondata:Name {value: "fulfillment_status"}
     string fulfillmentStatus?;
+    @jsondata:Name {value: "total_discount"}
     string totalDiscount?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "total_discount_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalDiscountSet?;
     string title?;
+    @jsondata:Name {value: "product_exists"}
     boolean productExists?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
     string price?;
     anydata? vendor?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     int id?;
     int grams?;
     string? sku?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
     int quantity?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
+    @jsondata:Name {value: "discount_allocations"}
     anydata[] discountAllocations?;
+    @jsondata:Name {value: "variant_inventory_management"}
     anydata? variantInventoryManagement?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string name?;
+    @jsondata:Name {value: "price_set"}
     ReopenCloseOrderOrderTotalDiscountsSet priceSet?;
     anydata[] properties?;
 };
@@ -3952,6 +5455,7 @@
 
 
 type AdminapiapiVersionblogsJsonBlogMetafields record {
+    @jsondata:Name {value: "value_type"}
     string valueType?;
     string namespace?;
     string value?;
@@ -3972,88 +5476,134 @@
 
 type CreateRefundRefund record {
     string? note?;
+    @jsondata:Name {value: "refund_line_items"}
     CreateRefundRefundRefundLineItems[] refundLineItems?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "order_adjustments"}
     anydata[] orderAdjustments?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
     boolean restock?;
     int id?;
     CreateRefundRefundTransactions[] transactions?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
 };
 
 
 type CreateRefundRefundRefundLineItems record {
+    @jsondata:Name {value: "line_item"}
     CreateRefundRefundLineItem lineItem?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
     decimal subtotal?;
+    @jsondata:Name {value: "total_tax_set"}
     ReopenCloseOrderOrderPriceSet1 totalTaxSet?;
     int id?;
+    @jsondata:Name {value: "subtotal_set"}
     ReopenCloseOrderOrderPriceSet subtotalSet?;
+    @jsondata:Name {value: "total_tax"}
     decimal totalTax?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
+    @jsondata:Name {value: "restock_type"}
     string restockType?;
 };
 
 
 type CreateRefundRefundLineItem record {
+    @jsondata:Name {value: "variant_title"}
     string? variantTitle?;
+    @jsondata:Name {value: "fulfillment_status"}
     anydata? fulfillmentStatus?;
+    @jsondata:Name {value: "total_discount"}
     string totalDiscount?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "total_discount_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalDiscountSet?;
     string title?;
+    @jsondata:Name {value: "product_exists"}
     boolean productExists?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "tax_lines"}
     ReopenCloseOrderOrderTaxLines[] taxLines?;
     string price?;
     anydata? vendor?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     int id?;
     int grams?;
     string? sku?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
     int quantity?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
+    @jsondata:Name {value: "discount_allocations"}
     anydata[] discountAllocations?;
+    @jsondata:Name {value: "variant_inventory_management"}
     string variantInventoryManagement?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string name?;
+    @jsondata:Name {value: "price_set"}
     ReopenCloseOrderOrderPriceSet priceSet?;
     anydata[] properties?;
 };
 
 
 type CancelFulfillmentFulfillmentLineItems record {
+    @jsondata:Name {value: "variant_title"}
     string? variantTitle?;
+    @jsondata:Name {value: "fulfillment_status"}
     anydata? fulfillmentStatus?;
+    @jsondata:Name {value: "total_discount"}
     string totalDiscount?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "total_discount_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalDiscountSet?;
     string title?;
+    @jsondata:Name {value: "product_exists"}
     boolean productExists?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
     string price?;
     anydata? vendor?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     int id?;
     int grams?;
     string? sku?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
     int quantity?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
+    @jsondata:Name {value: "discount_allocations"}
     anydata[] discountAllocations?;
+    @jsondata:Name {value: "variant_inventory_management"}
     anydata? variantInventoryManagement?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string name?;
+    @jsondata:Name {value: "price_set"}
     ReopenCloseOrderOrderTotalDiscountsSet priceSet?;
     anydata[] properties?;
 };
@@ -4063,12 +5613,14 @@
     string src?;
     string alt?;
     int width?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int height?;
 };
 
 
 type FulfillmentEvents record {
+    @jsondata:Name {value: "fulfillment_events"}
     FulfillmentEventsFulfillmentEvents[] fulfillmentEvents?;
 };
 
@@ -4079,16 +5631,24 @@
     anydata? city?;
     anydata? address1?;
     anydata? latitude?;
+    @jsondata:Name {value: "happened_at"}
     string happenedAt?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "estimated_delivery_at"}
     anydata? estimatedDeliveryAt?;
     anydata? message?;
+    @jsondata:Name {value: "fulfillment_id"}
     int fulfillmentId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     anydata? province?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int id?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
     anydata? longitude?;
     string status?;
@@ -4098,24 +5658,31 @@
 
 type RetrievesAListOfFulfillmentOrdersAssignedToTheShopLocationsThatAreOwnedByTheAppQueries record {
     # The assignment status of the fulfillment orders that should be returned. If assignment_status parameter isn't provided, then the query will return all assigned fulfillment orders, except those with the CLOSED status
+    @http:Query {name: "assignment_status"}
     string assignmentStatus?;
     # he IDs of the assigned locations of the fulfillment orders that should be returned.
 If the location_ids parameter isn't provided, then all fulfillment orders assigned to the shop locations that are managed by the app will be returned
+    @http:Query {name: "location_ids"}
     string locationIds?;
 };
 
 
 type CreateCarrierService record {
+    @jsondata:Name {value: "carrier_service"}
     CreateCarrierServiceCarrierService carrierService?;
 };
 
 
 type CreateCarrierServiceCarrierService record {
+    @jsondata:Name {value: "callback_url"}
     string callbackUrl?;
+    @jsondata:Name {value: "carrier_service_type"}
     string carrierServiceType?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string format?;
     string name?;
+    @jsondata:Name {value: "service_discovery"}
     boolean serviceDiscovery?;
     boolean active?;
     int id?;
@@ -4123,22 +5690,33 @@
 
 
 type CancelFulfillmentOrder record {
+    @jsondata:Name {value: "fulfillment_order"}
     CancelFulfillmentOrderFulfillmentOrder fulfillmentOrder?;
+    @jsondata:Name {value: "replacement_fulfillment_order"}
     CancelFulfillmentOrderReplacementFulfillmentOrder replacementFulfillmentOrder?;
 };
 
 
 type CancelFulfillmentOrderFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     CancelFulfillmentOrderFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     CancelFulfillmentOrderFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     anydata[] supportedActions?;
+    @jsondata:Name {value: "assigned_location"}
     FulfillmentOrdersAssignedLocation assignedLocation?;
+    @jsondata:Name {value: "merchant_requests"}
     anydata[] merchantRequests?;
     string status?;
 };
@@ -4152,37 +5730,54 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
 
 
 type CancelFulfillmentOrderFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
 
 
 type CancelFulfillmentOrderReplacementFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     CancelFulfillmentOrderReplacementFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     CancelFulfillmentOrderReplacementFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     string[] supportedActions?;
+    @jsondata:Name {value: "assigned_location"}
     FulfillmentOrdersAssignedLocation assignedLocation?;
+    @jsondata:Name {value: "merchant_requests"}
     anydata[] merchantRequests?;
     string status?;
 };
@@ -4196,9 +5791,11 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
@@ -4212,16 +5809,24 @@
 
 
 type RejectFulfillmentResponseFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     FulfillmentOrdersAssignedLocation origin?;
     RejectFulfillmentResponseFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     RejectFulfillmentResponseFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "outgoing_requests"}
     anydata[] outgoingRequests?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     string[] supportedActions?;
     string status?;
 };
@@ -4235,85 +5840,121 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
 
 
 type RejectFulfillmentResponseFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
 
 
 type ArticleCommentComment record {
+    @jsondata:Name {value: "blog_id"}
     int blogId?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     string author?;
     string ip?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string body?;
+    @jsondata:Name {value: "article_id"}
     int articleId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     anydata? publishedAt?;
     string email?;
+    @jsondata:Name {value: "user_agent"}
     anydata? userAgent?;
     string status?;
 };
 
 
 type FulfillmentServicesList record {
+    @jsondata:Name {value: "fulfillment_services"}
     SingleFulfillmentServiceFulfillmentService[] fulfillmentServices?;
 };
 
 
 type SingleFulfillmentServiceFulfillmentService record {
+    @jsondata:Name {value: "callback_url"}
     string callbackUrl?;
+    @jsondata:Name {value: "inventory_management"}
     boolean inventoryManagement?;
+    @jsondata:Name {value: "service_name"}
     string serviceName?;
+    @jsondata:Name {value: "fulfillment_orders_opt_in"}
     boolean fulfillmentOrdersOptIn?;
     string name?;
+    @jsondata:Name {value: "provider_id"}
     anydata? providerId?;
     string 'handle?;
     int id?;
+    @jsondata:Name {value: "include_pending_stock"}
     boolean includePendingStock?;
     anydata? email?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
+    @jsondata:Name {value: "tracking_support"}
     boolean trackingSupport?;
 };
 
 
 type TransactionResponseTransaction record {
     string amount?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
+    @jsondata:Name {value: "payment_details"}
     ReopenCloseOrderOrderPaymentDetails paymentDetails?;
     boolean test?;
     string kind?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     anydata? message?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
     string authorization?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "parent_id"}
     anydata? parentId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "currency_exchange_adjustment"}
     anydata? currencyExchangeAdjustment?;
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
     string currency?;
+    @jsondata:Name {value: "error_code"}
     anydata? errorCode?;
     ReopenCloseOrderOrderReceipt receipt?;
     int id?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
     string gateway?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
     string status?;
 };
@@ -4322,6 +5963,7 @@
 type CountryResponseCountry record {
     CountryResponseCountryProvinces[] provinces?;
     string code?;
+    @jsondata:Name {value: "tax_name"}
     string taxName?;
     string name?;
     decimal tax?;
@@ -4331,13 +5973,18 @@
 
 type CountryResponseCountryProvinces record {
     string code?;
+    @jsondata:Name {value: "tax_type"}
     string? taxType?;
+    @jsondata:Name {value: "tax_name"}
     string? taxName?;
     string name?;
+    @jsondata:Name {value: "tax_percentage"}
     decimal taxPercentage?;
     decimal tax?;
     int id?;
+    @jsondata:Name {value: "shipping_zone_id"}
     anydata? shippingZoneId?;
+    @jsondata:Name {value: "country_id"}
     int countryId?;
 };
 
@@ -4354,46 +6001,59 @@
     # Destination URI to which the webhook subscription should send the POST request when an event occurs
     string address?;
     # Optional array of namespaces for any metafields that should be included with each webhook
+    @jsondata:Name {value: "metafield_namespaces"}
     string[] metafieldNamespaces?;
     # Date and time when the webhook subscription was updated. The API returns this value in ISO 8601 format
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     # Format in which the webhook subscription should send the data. Valid values are JSON and XML. Defaults to JSON
     string format?;
     # Date and time when the webhook subscription was created. The API returns this value in ISO 8601 format
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     # Event that triggers the webhook. Valid values are app/uninstalled, bulk_operations/finish, carts/create, carts/update, checkouts/create, checkouts/delete, checkouts/update, collection_listings/add, collection_listings/remove, collection_listings/update, collections/create, collections/delete, collections/update, customer_groups/create, customer_groups/delete, customer_groups/update, customer_payment_methods/create, customer_payment_methods/revoke, customer_payment_methods/update, customers/create, customers/delete, customers/disable, customers/enable, customers/update, customers_marketing_consent/update, disputes/create, disputes/update, domains/create, domains/destroy, domains/update, draft_orders/create, draft_orders/delete, draft_orders/update, fulfillment_events/create, fulfillment_events/delete, fulfillments/create, fulfillments/update, inventory_items/create, inventory_items/delete, inventory_items/update, inventory_levels/connect, inventory_levels/disconnect, inventory_levels/update, locales/create, locales/update, locations/create, locations/delete, locations/update, order_transactions/create, orders/cancelled, orders/create, orders/delete, orders/edited, orders/fulfilled, orders/paid, orders/partially_fulfilled, orders/updated, product_listings/add, product_listings/remove, product_listings/update, products/create, products/delete, products/update, profiles/create, profiles/delete, profiles/update, refunds/create, selling_plan_groups/create, selling_plan_groups/delete, selling_plan_groups/update, shop/update, subscription_billing_attempts/challenged, subscription_billing_attempts/failure, subscription_billing_attempts/success, subscription_contracts/create, subscription_contracts/update, tender_transactions/create, themes/create, themes/delete, themes/publish, themes/update
     string topic?;
     # Unique numeric identifier for the webhook subscription
     int id?;
     # The Admin API version that Shopify uses to serialize webhook events. This value is inherited from the app that created the webhook subscription
+    @jsondata:Name {value: "api_version"}
     string apiVersion?;
     # An optional array of top-level resource fields that should be serialized and sent in the POST request. If absent, all fields will be sent
     string[] fields?;
     # Optional array of namespaces for any private metafields that should be included with each webhook
+    @jsondata:Name {value: "private_metafield_namespaces"}
     string[] privateMetafieldNamespaces?;
 };
 
 
 type CollectionListing record {
+    @jsondata:Name {value: "collection_listing"}
     CollectionListingCollectionListing collectionListing?;
 };
 
 
 type CollectionListingCollectionListing record {
+    @jsondata:Name {value: "collection_id"}
     int collectionId?;
     CollectionListingCollectionListingImage image?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string 'handle?;
+    @jsondata:Name {value: "default_product_image"}
     anydata? defaultProductImage?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
     string title?;
+    @jsondata:Name {value: "sort_order"}
     string sortOrder?;
 };
 
 
 type CollectionListingCollectionListingImage record {
     string src?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
 };
 
@@ -4404,14 +6064,19 @@
     string address2?;
     string city?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     string province?;
     string phone?;
+    @jsondata:Name {value: "country_name"}
     string countryName?;
     string name?;
     string company?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
 };
 
@@ -4430,17 +6095,24 @@
 
 type CreatSmartCollectionSmartCollection record {
     CreatSmartCollectionSmartCollectionImage image?;
+    @jsondata:Name {value: "body_html"}
     anydata? bodyHtml?;
     string 'handle?;
     CreatSmartCollectionSmartCollectionRules[] rules?;
     string title?;
+    @jsondata:Name {value: "published_scope"}
     string publishedScope?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     boolean disjunctive?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string? publishedAt?;
+    @jsondata:Name {value: "sort_order"}
     string sortOrder?;
 };
 
@@ -4454,10 +6126,15 @@
 
 type SingleBlogBlog record {
     anydata? feedburner?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "feedburner_location"}
     anydata? feedburnerLocation?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     int id?;
@@ -4475,6 +6152,7 @@
 type CountriesListCountries record {
     CountriesListProvinces[] provinces?;
     string code?;
+    @jsondata:Name {value: "tax_name"}
     string taxName?;
     string name?;
     decimal tax?;
@@ -4484,13 +6162,18 @@
 
 type CountriesListProvinces record {
     string code?;
+    @jsondata:Name {value: "tax_type"}
     anydata? taxType?;
+    @jsondata:Name {value: "tax_name"}
     anydata? taxName?;
     string name?;
+    @jsondata:Name {value: "tax_percentage"}
     decimal taxPercentage?;
     decimal tax?;
     int id?;
+    @jsondata:Name {value: "shipping_zone_id"}
     int? shippingZoneId?;
+    @jsondata:Name {value: "country_id"}
     int countryId?;
 };
 
@@ -4498,18 +6181,25 @@
 
 type RetrieveACountOfCommentsQueries record {
     # Count comments created after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Count comments created before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Count comments last updated before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Count comments last updated after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Count comments published after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_min"}
     string publishedAtMin?;
     # Count comments published before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_max"}
     string publishedAtMax?;
     # Retrieve a count of comments with a given published status.(default: any) 
+    @http:Query {name: "published_status"}
     string publishedStatus?;
     # Retrieve a count of comments with a given status. 
     string status?;
@@ -4517,12 +6207,18 @@
 
 
 type FulfillmentOrderFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
@@ -4540,19 +6236,28 @@
 
 
 type ArticlesArticles record {
+    @jsondata:Name {value: "blog_id"}
     int blogId?;
+    @jsondata:Name {value: "body_html"}
     string? bodyHtml?;
     string author?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     string title?;
     string tags?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     anydata? publishedAt?;
+    @jsondata:Name {value: "summary_html"}
     anydata? summaryHtml?;
 };
 
@@ -4560,26 +6265,35 @@
 
 type RetrieveAListOfProductsQueries record {
     # Show products created after date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show products last updated before date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show products published after date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "published_at_min"}
     string publishedAtMin?;
     # Filter results by product handle. 
     string 'handle?;
     # Return products by their published status(default: any) 
+    @http:Query {name: "published_status"}
     string publishedStatus?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Filter results by product title. 
     string title?;
     # Filter results by product collection ID. 
+    @http:Query {name: "collection_id"}
     string collectionId?;
     # Show products created before date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Filter results by product type. 
+    @http:Query {name: "product_type"}
     string productType?;
     # Show products last updated after date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Filter results by product vendor. 
     string vendor?;
@@ -4588,10 +6302,12 @@
     # Return presentment prices in only certain currencies, specified by a comma-separated list of [ISO 4217][1] currency codes. 
 
 [1]: https://en.wikipedia.org/wiki/ISO_4217
+    @http:Query {name: "presentment_currencies"}
     string presentmentCurrencies?;
     # Return only products specified by a comma-separated list of product IDs. 
     string ids?;
     # Show products published before date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "published_at_max"}
     string publishedAtMax?;
     # Show only certain fields, specified by a comma-separated list of field names. 
     string fields?;
@@ -4622,6 +6338,7 @@
 
 
 type CreateProductResponseProductOptions record {
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     string[] values?;
     string name?;
@@ -4636,7 +6353,9 @@
 
 
 type AdminapiapiVersioncollectsJsonCollect record {
+    @jsondata:Name {value: "collection_id"}
     int collectionId?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
 };
 
@@ -4652,11 +6371,14 @@
 
 
 type SingleEventEvent record {
+    @jsondata:Name {value: "subject_id"}
     int subjectId?;
     string path?;
+    @jsondata:Name {value: "subject_type"}
     string subjectType?;
     string author?;
     string verb?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string description?;
     string[] arguments?;
@@ -4667,8 +6389,10 @@
 
 
 type InventoryLevelsSetJsonBody record {
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int available?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
 };
 
@@ -4688,6 +6412,7 @@
 
 type RefundLineItem record {
     # The ID of the related line item in the order
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     # The quantity of the associated line item that was returned
     int quantity?;
@@ -4696,10 +6421,13 @@
     # The unique identifier of the line item in the refund
     int id?;
     # The total tax on the refund line item
+    @jsondata:Name {value: "total_tax"}
     decimal totalTax?;
     # The unique identifier of the location where the items will be restocked. Required when restock_type has the value return or cancel
+    @jsondata:Name {value: "location_id"}
     int locationId?;
     # How this refund line item affects inventory levels
+    @jsondata:Name {value: "restock_type"}
     string restockType?;
 };
 
@@ -4707,6 +6435,7 @@
 
 type ReceiveAListOfAllProductImagesQueries record {
     # Restrict results to after the specified ID 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # comma-separated list of fields to include in the response 
     string fields?;
@@ -4721,48 +6450,68 @@
 
 
 type ScriptTagResponse record {
+    @jsondata:Name {value: "script_tag"}
     ScriptTagResponseScriptTag scriptTag?;
 };
 
 
 type ScriptTagResponseScriptTag record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string src?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int id?;
+    @jsondata:Name {value: "display_scope"}
     string displayScope?;
     string event?;
 };
 
 
 type UpdateCustomCollection record {
+    @jsondata:Name {value: "custom_collection"}
     UpdateCustomCollectionCustomCollection customCollection?;
 };
 
 
 type AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdcancelJsonFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdcancelJsonFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdcancelJsonFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     string[] supportedActions?;
+    @jsondata:Name {value: "assigned_location"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdcancelJsonFulfillmentOrderAssignedLocation assignedLocation?;
+    @jsondata:Name {value: "merchant_requests"}
     anydata[] merchantRequests?;
     string status?;
 };
 
 
 type AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdcancelJsonFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
@@ -4770,6 +6519,7 @@
 
 type AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdcancelJsonFulfillmentOrderAssignedLocation record {
     anydata? zip?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     anydata? province?;
     anydata? address2?;
@@ -4777,20 +6527,25 @@
     anydata? phone?;
     anydata? address1?;
     string name?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
 };
 
 
 type SingleScriptTag record {
+    @jsondata:Name {value: "script_tag"}
     SingleScriptTagScriptTag scriptTag?;
 };
 
 
 type SingleScriptTagScriptTag record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string src?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int id?;
+    @jsondata:Name {value: "display_scope"}
     string displayScope?;
     string event?;
 };
@@ -4802,11 +6557,13 @@
 
 
 type AdminapiapiVersioncommentsJsonComment record {
+    @jsondata:Name {value: "article_id"}
     int articleId?;
 };
 
 
 type CancellationRequestAcceptJsonBody record {
+    @jsondata:Name {value: "cancellation_request"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdcancellationRequestacceptJsonCancellationRequest cancellationRequest?;
 };
 
@@ -4830,67 +6587,117 @@
 
 
 type PaymentsResponseCheckout record {
+    @jsondata:Name {value: "privacy_policy_url"}
     anydata? privacyPolicyUrl?;
+    @jsondata:Name {value: "payment_url"}
     string paymentUrl?;
+    @jsondata:Name {value: "refund_policy_url"}
     anydata? refundPolicyUrl?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "terms_of_sale_url"}
     anydata? termsOfSaleUrl?;
+    @jsondata:Name {value: "billing_address"}
     SinglePaymentResponsePaymentCheckoutBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     SinglePaymentResponsePaymentCheckoutLineItems[] lineItems?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "reservation_time_left"}
     int reservationTimeLeft?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "payment_due"}
     string paymentDue?;
+    @jsondata:Name {value: "source_identifier"}
     anydata? sourceIdentifier?;
+    @jsondata:Name {value: "tax_lines"}
     SinglePaymentResponsePaymentCheckoutTaxLines[] taxLines?;
+    @jsondata:Name {value: "customer_locale"}
     anydata? customerLocale?;
+    @jsondata:Name {value: "tax_manipulations"}
     anydata[] taxManipulations?;
     anydata? 'order?;
+    @jsondata:Name {value: "terms_of_service_url"}
     anydata? termsOfServiceUrl?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "subscription_policy_url"}
     anydata? subscriptionPolicyUrl?;
+    @jsondata:Name {value: "order_status_url"}
     anydata? orderStatusUrl?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "discount_code"}
     anydata? discountCode?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
+    @jsondata:Name {value: "completed_at"}
     anydata? completedAt?;
+    @jsondata:Name {value: "shipping_rate"}
     SinglePaymentResponsePaymentCheckoutShippingRate shippingRate?;
     anydata? phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     SinglePaymentResponsePaymentCheckoutNoteAttributes noteAttributes?;
     string name?;
+    @jsondata:Name {value: "shipping_line"}
     SinglePaymentResponsePaymentCheckoutShippingLine|() shippingLine?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
     string? note?;
+    @jsondata:Name {value: "applied_discount"}
     anydata? appliedDiscount?;
     PaymentsResponseCheckoutPayments[] payments?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "shopify_payments_account_id"}
     anydata? shopifyPaymentsAccountId?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string currency?;
+    @jsondata:Name {value: "shipping_address"}
     SinglePaymentResponsePaymentCheckoutBillingAddress|() shippingAddress?;
     string email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "legal_notice_url"}
     anydata? legalNoticeUrl?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
+    @jsondata:Name {value: "reservation_time"}
     anydata? reservationTime?;
+    @jsondata:Name {value: "total_tip_received"}
     string totalTipReceived?;
     string token?;
+    @jsondata:Name {value: "credit_card"}
     SinglePaymentResponsePaymentCheckoutCreditCard creditCard?;
+    @jsondata:Name {value: "gift_cards"}
     anydata[] giftCards?;
+    @jsondata:Name {value: "web_url"}
     string webUrl?;
+    @jsondata:Name {value: "shipping_policy_url"}
     anydata? shippingPolicyUrl?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
 };
 
 
 type PaymentsResponseCheckoutPayments record {
+    @jsondata:Name {value: "unique_token"}
     string uniqueToken?;
+    @jsondata:Name {value: "credit_card"}
     anydata? creditCard?;
+    @jsondata:Name {value: "payment_processing_error_message"}
     anydata? paymentProcessingErrorMessage?;
     int id?;
     PaymentsResponseCheckoutTransaction 'transaction?;
@@ -4898,17 +6705,23 @@
 
 
 type PaymentsResponseCheckoutTransaction record {
+    @jsondata:Name {value: "amount_in"}
     anydata? amountIn?;
     string amount?;
     boolean test?;
     string kind?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     anydata? message?;
+    @jsondata:Name {value: "amount_out"}
     anydata? amountOut?;
     string authorization?;
+    @jsondata:Name {value: "parent_id"}
     anydata? parentId?;
+    @jsondata:Name {value: "amount_rounding"}
     anydata? amountRounding?;
     string currency?;
+    @jsondata:Name {value: "error_code"}
     anydata? errorCode?;
     int id?;
     string gateway?;
@@ -4950,6 +6763,7 @@
 
 
 type ApplicationChargeResult record {
+    @jsondata:Name {value: "application_charge"}
     ApplicationChargeResultApplicationCharge applicationCharge?;
 };
 
@@ -4960,13 +6774,17 @@
     string address2?;
     string city?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     string province?;
     string phone?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
 };
 
@@ -4977,17 +6795,21 @@
 
 
 type CreateCustomerCustomerEmailMarketingConsent record {
+    @jsondata:Name {value: "consent_updated_at"}
     anydata? consentUpdatedAt?;
     string state?;
+    @jsondata:Name {value: "opt_in_level"}
     string optInLevel?;
 };
 
 
 type ReportResponseReport record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string name?;
     int id?;
     string category?;
+    @jsondata:Name {value: "shopify_ql"}
     string shopifyQl?;
 };
 
@@ -5010,9 +6832,13 @@
 
 
 type CreateAuthorizationResponsePayment record {
+    @jsondata:Name {value: "unique_token"}
     string uniqueToken?;
+    @jsondata:Name {value: "credit_card"}
     CreateAuthorizationResponsePaymentCheckoutCreditCard creditCard?;
+    @jsondata:Name {value: "payment_processing_error_message"}
     anydata? paymentProcessingErrorMessage?;
+    @jsondata:Name {value: "next_action"}
     SinglePaymentResponsePaymentNextAction nextAction?;
     int id?;
     CreateAuthorizationResponsePaymentCheckout checkout?;
@@ -5022,84 +6848,142 @@
 
 
 type CreateAuthorizationResponsePaymentCheckoutCreditCard record {
+    @jsondata:Name {value: "expiry_month"}
     int expiryMonth?;
+    @jsondata:Name {value: "first_digits"}
     string firstDigits?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
     string brand?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
+    @jsondata:Name {value: "last_digits"}
     string lastDigits?;
+    @jsondata:Name {value: "expiry_year"}
     int expiryYear?;
 };
 
 
 type SinglePaymentResponsePaymentNextAction record {
+    @jsondata:Name {value: "redirect_url"}
     anydata? redirectUrl?;
 };
 
 
 type CreateAuthorizationResponsePaymentCheckout record {
+    @jsondata:Name {value: "privacy_policy_url"}
     anydata? privacyPolicyUrl?;
+    @jsondata:Name {value: "payment_url"}
     string paymentUrl?;
+    @jsondata:Name {value: "refund_policy_url"}
     anydata? refundPolicyUrl?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "terms_of_sale_url"}
     anydata? termsOfSaleUrl?;
+    @jsondata:Name {value: "billing_address"}
     SinglePaymentResponsePaymentCheckoutBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     SinglePaymentResponsePaymentCheckoutLineItems[] lineItems?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "reservation_time_left"}
     int reservationTimeLeft?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "payment_due"}
     string paymentDue?;
+    @jsondata:Name {value: "source_identifier"}
     anydata? sourceIdentifier?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
+    @jsondata:Name {value: "customer_locale"}
     anydata? customerLocale?;
+    @jsondata:Name {value: "tax_manipulations"}
     anydata[] taxManipulations?;
     anydata? 'order?;
+    @jsondata:Name {value: "terms_of_service_url"}
     anydata? termsOfServiceUrl?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "subscription_policy_url"}
     anydata? subscriptionPolicyUrl?;
+    @jsondata:Name {value: "order_status_url"}
     anydata? orderStatusUrl?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "discount_code"}
     anydata? discountCode?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
+    @jsondata:Name {value: "completed_at"}
     anydata? completedAt?;
+    @jsondata:Name {value: "shipping_rate"}
     SinglePaymentResponsePaymentCheckoutShippingRate shippingRate?;
     anydata? phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     SinglePaymentResponsePaymentCheckoutNoteAttributes noteAttributes?;
     string name?;
+    @jsondata:Name {value: "shipping_line"}
     SinglePaymentResponsePaymentCheckoutShippingLine|() shippingLine?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
     string? note?;
+    @jsondata:Name {value: "applied_discount"}
     anydata? appliedDiscount?;
     CreateAuthorizationResponsePaymentCheckoutPayments[] payments?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "shopify_payments_account_id"}
     anydata? shopifyPaymentsAccountId?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string currency?;
+    @jsondata:Name {value: "shipping_address"}
     SinglePaymentResponsePaymentCheckoutBillingAddress|() shippingAddress?;
     string email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "legal_notice_url"}
     anydata? legalNoticeUrl?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
+    @jsondata:Name {value: "reservation_time"}
     anydata? reservationTime?;
+    @jsondata:Name {value: "total_tip_received"}
     string totalTipReceived?;
     string token?;
+    @jsondata:Name {value: "credit_card"}
     CreateAuthorizationResponsePaymentCheckoutCreditCard creditCard?;
+    @jsondata:Name {value: "gift_cards"}
     anydata[] giftCards?;
+    @jsondata:Name {value: "web_url"}
     string webUrl?;
+    @jsondata:Name {value: "shipping_policy_url"}
     anydata? shippingPolicyUrl?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
 };
 
 
 type CreateAuthorizationResponsePaymentCheckoutPayments record {
+    @jsondata:Name {value: "unique_token"}
     string uniqueToken?;
+    @jsondata:Name {value: "credit_card"}
     record {|anydata...;|}? creditCard?;
+    @jsondata:Name {value: "payment_processing_error_message"}
     anydata? paymentProcessingErrorMessage?;
     int id?;
     CreateAuthorizationResponsePaymentCheckoutTransaction|() 'transaction?;
@@ -5108,21 +6992,31 @@
 
 
 type CreateAuthorizationResponsePaymentCheckoutTransaction record {
+    @jsondata:Name {value: "amount_in"}
     anydata? amountIn?;
     string amount?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
     boolean test?;
     string kind?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     anydata? message?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "amount_out"}
     anydata? amountOut?;
     string authorization?;
+    @jsondata:Name {value: "transaction_group_id"}
     anydata? transactionGroupId?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "parent_id"}
     anydata? parentId?;
+    @jsondata:Name {value: "amount_rounding"}
     anydata? amountRounding?;
     string currency?;
+    @jsondata:Name {value: "error_code"}
     anydata? errorCode?;
     ReopenCloseOrderOrderReceipt receipt?;
     int id?;
@@ -5132,15 +7026,20 @@
 
 
 type ProductListingsproductListingIdJsonBody record {
+    @jsondata:Name {value: "product_listing"}
     AdminapiapiVersionproductListingsproductListingIdJsonProductListing productListing?;
 };
 
 
 type UsageChargeResponseUsageCharge record {
+    @jsondata:Name {value: "risk_level"}
     decimal riskLevel?;
     string price?;
+    @jsondata:Name {value: "balance_used"}
     decimal balanceUsed?;
+    @jsondata:Name {value: "balance_remaining"}
     decimal balanceRemaining?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string description?;
     string currency?;
@@ -5150,17 +7049,24 @@
 
 type UpdateSmartCollectionSmartCollection record {
     UpdateCustomCollectionCustomCollectionImage image?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     string 'handle?;
     SmartCollectionResponseSmartCollectionRules[] rules?;
     string title?;
+    @jsondata:Name {value: "published_scope"}
     string publishedScope?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     boolean disjunctive?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string? publishedAt?;
+    @jsondata:Name {value: "sort_order"}
     string sortOrder?;
 };
 
@@ -5171,53 +7077,77 @@
     string address2?;
     string city?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     boolean default?;
     string province?;
     string phone?;
+    @jsondata:Name {value: "country_name"}
     string countryName?;
     string name?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
 };
 
 
 type DisableGiftCard record {
+    @jsondata:Name {value: "gift_card"}
     DisableGiftCardGiftCard giftCard?;
 };
 
 
 type DisableGiftCardGiftCard record {
     anydata? note?;
+    @jsondata:Name {value: "initial_value"}
     string initialValue?;
+    @jsondata:Name {value: "line_item_id"}
     anydata? lineItemId?;
+    @jsondata:Name {value: "api_client_id"}
     anydata? apiClientId?;
+    @jsondata:Name {value: "disabled_at"}
     string disabledAt?;
+    @jsondata:Name {value: "expires_on"}
     anydata? expiresOn?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
     string balance?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "customer_id"}
     anydata? customerId?;
+    @jsondata:Name {value: "last_characters"}
     string lastCharacters?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
 };
 
 
 type AssetsListAsset record {
+    @jsondata:Name {value: "public_url"}
     string? publicUrl?;
     string attachment?;
+    @jsondata:Name {value: "content_type"}
     string contentType?;
     int size?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "theme_id"}
     int themeId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string value?;
     string 'key?;
@@ -5229,14 +7159,19 @@
     # An optional note attached to a refund
     string note?;
     # A list of refunded line items
+    @jsondata:Name {value: "refund_line_items"}
     RefundLineItem[] refundLineItems?;
     # The unique identifier of the user who performed the refund
+    @jsondata:Name {value: "user_id"}
     int userId?;
     # A list of order adjustments attached to the refund. Order adjustments are generated to account for refunded shipping costs and differences between calculated and actual refund amounts
+    @jsondata:Name {value: "order_adjustments"}
     OrderAdjustment[] orderAdjustments?;
     # The date and time (ISO 8601 format) when the refund was created
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     # The date and time (ISO 8601 format) when the refund was imported. This value can be set to a date in the past when importing from other systems. If no value is provided, then it will be auto-generated as the current time in Shopify. Public apps need to be granted permission by Shopify to import orders with the processed_at timestamp set to a value earlier the created_at timestamp. Private apps can't be granted permission by Shopify
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
     # The unique identifier for the refund
     int id?;
@@ -5249,6 +7184,7 @@
 
 
 type ProductIdResourceFeedbackJsonBody record {
+    @jsondata:Name {value: "resource_feedback"}
     AdminapiapiVersionproductsproductIdresourceFeedbackJsonResourceFeedback resourceFeedback?;
 };
 
@@ -5271,6 +7207,7 @@
 
 type UpdateTheCappedAmountOfARecurringApplicationChargeQueries record {
     # The new maximum amount that can be charged to the store. Must be greater than or equal to the current capped amount.
+    @http:Query {name: "recurring_application_charge[capped_amount]"}
     string recurringApplicationChargeCappedAmount?;
 };
 
@@ -5285,10 +7222,13 @@
 
 type ReceiveACountOfAllDraftOrdersQueries record {
     # Count draft orders last updated before the specified date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Count draft orders last updated after the specified date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Count draft orders after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Count draft orders that have a given status.(default: open) 
     string status?;
@@ -5296,18 +7236,25 @@
 
 
 type OriginalFulfillmentOrderOriginalFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
 
 
 type PostalCodeResult record {
+    @jsondata:Name {value: "customer_address"}
     PostalCodeResultCustomerAddress customerAddress?;
 };
 
@@ -5318,88 +7265,147 @@
     string address2?;
     string city?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     anydata? lastName?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     boolean default?;
     string province?;
     string phone?;
+    @jsondata:Name {value: "country_name"}
     string countryName?;
     string name?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
+    @jsondata:Name {value: "first_name"}
     anydata? firstName?;
 };
 
 
 type OrderResponseOrder record {
+    @jsondata:Name {value: "cancelled_at"}
     anydata? cancelledAt?;
+    @jsondata:Name {value: "fulfillment_status"}
     string? fulfillmentStatus?;
+    @jsondata:Name {value: "total_price_usd"}
     string totalPriceUsd?;
+    @jsondata:Name {value: "billing_address"}
     OrderResponseOrderBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     OrderResponseOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "total_discounts_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalDiscountsSet?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "landing_site"}
     anydata? landingSite?;
+    @jsondata:Name {value: "source_identifier"}
     anydata? sourceIdentifier?;
     anydata? reference?;
     int number?;
+    @jsondata:Name {value: "checkout_id"}
     anydata? checkoutId?;
+    @jsondata:Name {value: "checkout_token"}
     anydata? checkoutToken?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
+    @jsondata:Name {value: "customer_locale"}
     anydata? customerLocale?;
     int id?;
+    @jsondata:Name {value: "app_id"}
     int appId?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "closed_at"}
     anydata? closedAt?;
+    @jsondata:Name {value: "order_status_url"}
     string orderStatusUrl?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
     boolean test?;
+    @jsondata:Name {value: "total_shipping_price_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalShippingPriceSet?;
+    @jsondata:Name {value: "subtotal_price_set"}
     ReopenCloseOrderOrderPriceSet subtotalPriceSet?;
+    @jsondata:Name {value: "payment_gateway_names"}
     string[] paymentGatewayNames?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
     string tags?;
+    @jsondata:Name {value: "processing_method"}
     string processingMethod?;
+    @jsondata:Name {value: "shipping_lines"}
     anydata[] shippingLines?;
     anydata? phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     anydata[] noteAttributes?;
     string name?;
+    @jsondata:Name {value: "cart_token"}
     anydata? cartToken?;
+    @jsondata:Name {value: "total_tax_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalTaxSet?;
+    @jsondata:Name {value: "landing_site_ref"}
     anydata? landingSiteRef?;
+    @jsondata:Name {value: "discount_codes"}
     anydata[] discountCodes?;
     anydata? note?;
+    @jsondata:Name {value: "order_number"}
     int orderNumber?;
+    @jsondata:Name {value: "discount_applications"}
     anydata[] discountApplications?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "total_line_items_price_set"}
     ReopenCloseOrderOrderPriceSet totalLineItemsPriceSet?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "buyer_accepts_marketing"}
     boolean buyerAcceptsMarketing?;
     boolean confirmed?;
+    @jsondata:Name {value: "total_weight"}
     int totalWeight?;
+    @jsondata:Name {value: "contact_email"}
     string? contactEmail?;
     anydata[] refunds?;
+    @jsondata:Name {value: "total_discounts"}
     string totalDiscounts?;
     anydata[] fulfillments?;
+    @jsondata:Name {value: "referring_site"}
     anydata? referringSite?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
     string currency?;
+    @jsondata:Name {value: "shipping_address"}
     OrderResponseOrderShippingAddress|() shippingAddress?;
+    @jsondata:Name {value: "browser_ip"}
     anydata? browserIp?;
     string email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "total_price_set"}
     ReopenCloseOrderOrderPriceSet totalPriceSet?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
     string token?;
+    @jsondata:Name {value: "cancel_reason"}
     anydata? cancelReason?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "financial_status"}
     string financialStatus?;
     string gateway?;
     OrderResponseOrderCustomer customer?;
@@ -5413,71 +7419,108 @@
     string city?;
     string address1?;
     anydata? latitude?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     string province?;
     string phone?;
     string name?;
     anydata? company?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     anydata? longitude?;
 };
 
 
 type OrderResponseOrderLineItems record {
+    @jsondata:Name {value: "variant_title"}
     string? variantTitle?;
+    @jsondata:Name {value: "fulfillment_status"}
     anydata? fulfillmentStatus?;
+    @jsondata:Name {value: "total_discount"}
     string totalDiscount?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "total_discount_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalDiscountSet?;
     string title?;
+    @jsondata:Name {value: "product_exists"}
     boolean productExists?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
     string price?;
     string vendor?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     int id?;
     int grams?;
     string? sku?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
     int quantity?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
+    @jsondata:Name {value: "discount_allocations"}
     anydata[] discountAllocations?;
+    @jsondata:Name {value: "variant_inventory_management"}
     string variantInventoryManagement?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string name?;
+    @jsondata:Name {value: "price_set"}
     ReopenCloseOrderOrderPriceSet priceSet?;
     anydata[] properties?;
 };
 
 
 type OrderResponseOrderCustomer record {
+    @jsondata:Name {value: "total_spent"}
     string totalSpent?;
     anydata? note?;
+    @jsondata:Name {value: "last_order_name"}
     string lastOrderName?;
+    @jsondata:Name {value: "last_order_id"}
     int lastOrderId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "last_name"}
     string? lastName?;
+    @jsondata:Name {value: "multipass_identifier"}
     anydata? multipassIdentifier?;
+    @jsondata:Name {value: "verified_email"}
     boolean verifiedEmail?;
+    @jsondata:Name {value: "accepts_marketing_updated_at"}
     string acceptsMarketingUpdatedAt?;
     string tags?;
+    @jsondata:Name {value: "orders_count"}
     int ordersCount?;
+    @jsondata:Name {value: "default_address"}
     OrderResponseOrderCustomerDefaultAddress defaultAddress?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "accepts_marketing"}
     boolean acceptsMarketing?;
     anydata? phone?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "tax_exemptions"}
     anydata[] taxExemptions?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "marketing_opt_in_level"}
     anydata? marketingOptInLevel?;
     string state?;
+    @jsondata:Name {value: "first_name"}
     string? firstName?;
     string email?;
 };
@@ -5489,17 +7532,23 @@
     string? address2?;
     string city?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string? lastName?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     boolean default?;
     string province?;
     string phone?;
+    @jsondata:Name {value: "country_name"}
     string countryName?;
     string name?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
+    @jsondata:Name {value: "first_name"}
     string? firstName?;
 };
 
@@ -5510,26 +7559,35 @@
 
 
 type PageResponsePage record {
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string author?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string? publishedAt?;
     string title?;
 };
 
 
 type InvoiceResponse record {
+    @jsondata:Name {value: "draft_order_invoice"}
     InvoiceResponseDraftOrderInvoice draftOrderInvoice?;
 };
 
 
 type InvoiceResponseDraftOrderInvoice record {
+    @jsondata:Name {value: "custom_message"}
     string customMessage?;
     string[] bcc?;
     string subject?;
@@ -5539,11 +7597,15 @@
 
 
 type CarrierServiceListCarrierServices record {
+    @jsondata:Name {value: "callback_url"}
     string callbackUrl?;
+    @jsondata:Name {value: "carrier_service_type"}
     string carrierServiceType?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string format?;
     string name?;
+    @jsondata:Name {value: "service_discovery"}
     boolean serviceDiscovery?;
     boolean active?;
     int id?;
@@ -5551,14 +7613,18 @@
 
 
 type ApiVersionGiftCardsJsonBody record {
+    @jsondata:Name {value: "gift_card"}
     AdminapiapiVersiongiftCardsJsonGiftCard giftCard?;
 };
 
 
 type AdminapiapiVersiongiftCardsJsonGiftCard record {
+    @jsondata:Name {value: "initial_value"}
     string initialValue?;
+    @jsondata:Name {value: "send_on"}
     string sendOn?;
     string message?;
+    @jsondata:Name {value: "recipient_id"}
     int recipientId?;
 };
 
@@ -5566,8 +7632,10 @@
 
 type RetrieveAListOfDraftOrdersQueries record {
     # Show orders last updated before date (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show orders last updated after date (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Amount of results(default: 50)(maximum: 250) 
     string 'limit?;
@@ -5576,6 +7644,7 @@
     # A comma-separated list of fields to include in the response 
     string fields?;
     # Restrict results to after the specified ID 
+    @http:Query {name: "since_id"}
     string sinceId?;
     string status?;
 };
@@ -5583,33 +7652,46 @@
 
 type UpdateProductProduct record {
     UpdateProductProductImage|() image?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     UpdateProductProductImages[] images?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     SingleProductProductVariants[] variants?;
     string title?;
     string tags?;
+    @jsondata:Name {value: "published_scope"}
     string publishedScope?;
+    @jsondata:Name {value: "product_type"}
     string productType?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string vendor?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     ProductListingsOptions[] options?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string? publishedAt?;
 };
 
 
 type UpdateProductProductImage record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string src?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     anydata? alt?;
     int width?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "variant_ids"}
     anydata[] variantIds?;
     int id?;
     int position?;
@@ -5618,15 +7700,23 @@
 
 
 type SingleProductProductVariants record {
+    @jsondata:Name {value: "presentment_prices"}
     ProductVariantsPresentmentPrices[] presentmentPrices?;
+    @jsondata:Name {value: "inventory_management"}
     string inventoryManagement?;
+    @jsondata:Name {value: "old_inventory_quantity"}
     int oldInventoryQuantity?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string title?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     string price?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     anydata? option3?;
     string option1?;
@@ -5635,51 +7725,72 @@
     int grams?;
     string? sku?;
     string barcode?;
+    @jsondata:Name {value: "inventory_quantity"}
     int inventoryQuantity?;
+    @jsondata:Name {value: "compare_at_price"}
     anydata? compareAtPrice?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
     decimal weight?;
+    @jsondata:Name {value: "inventory_policy"}
     string inventoryPolicy?;
+    @jsondata:Name {value: "weight_unit"}
     string weightUnit?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int position?;
+    @jsondata:Name {value: "image_id"}
     int? imageId?;
 };
 
 
 type AvailableShippingRatesShippingRates record {
     string price?;
+    @jsondata:Name {value: "delivery_range"}
     anydata? deliveryRange?;
     string 'handle?;
     string id?;
     string title?;
     AvailableShippingRatesCheckout checkout?;
+    @jsondata:Name {value: "phone_required"}
     boolean phoneRequired?;
 };
 
 
 type AvailableShippingRatesCheckout record {
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
 };
 
 
 type DiscountCodeResponse record {
+    @jsondata:Name {value: "discount_code_creation"}
     DiscountCodeResponseDiscountCodeCreation discountCodeCreation?;
 };
 
 
 type DiscountCodeResponseDiscountCodeCreation record {
+    @jsondata:Name {value: "completed_at"}
     anydata? completedAt?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "imported_count"}
     int importedCount?;
+    @jsondata:Name {value: "price_rule_id"}
     int priceRuleId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "started_at"}
     anydata? startedAt?;
+    @jsondata:Name {value: "failed_count"}
     int failedCount?;
     int id?;
+    @jsondata:Name {value: "codes_count"}
     int codesCount?;
     string status?;
 };
@@ -5693,30 +7804,49 @@
 type CreateCustomerCustomer record {
     anydata? note?;
     CreateCustomerCustomerAddresses[] addresses?;
+    @jsondata:Name {value: "last_order_name"}
     anydata? lastOrderName?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "multipass_identifier"}
     anydata? multipassIdentifier?;
+    @jsondata:Name {value: "accepts_marketing_updated_at"}
     string acceptsMarketingUpdatedAt?;
+    @jsondata:Name {value: "default_address"}
     CreateCustomerCustomerAddresses defaultAddress?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "accepts_marketing"}
     boolean acceptsMarketing?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "marketing_opt_in_level"}
     anydata? marketingOptInLevel?;
     string state?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
+    @jsondata:Name {value: "total_spent"}
     string totalSpent?;
+    @jsondata:Name {value: "last_order_id"}
     anydata? lastOrderId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "email_marketing_consent"}
     CreateCustomerCustomerEmailMarketingConsent emailMarketingConsent?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "verified_email"}
     boolean verifiedEmail?;
     string tags?;
+    @jsondata:Name {value: "orders_count"}
     int ordersCount?;
+    @jsondata:Name {value: "sms_marketing_consent"}
     CreateCustomerCustomerSmsMarketingConsent smsMarketingConsent?;
     string phone?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "tax_exemptions"}
     anydata[] taxExemptions?;
 };
 
@@ -5727,34 +7857,47 @@
     anydata? address2?;
     string city?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     boolean default?;
     string province?;
     string phone?;
+    @jsondata:Name {value: "country_name"}
     string countryName?;
     string name?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
 };
 
 
 type CreateCustomerCustomerSmsMarketingConsent record {
+    @jsondata:Name {value: "consent_updated_at"}
     anydata? consentUpdatedAt?;
+    @jsondata:Name {value: "consent_collected_from"}
     string consentCollectedFrom?;
     string state?;
+    @jsondata:Name {value: "opt_in_level"}
     string optInLevel?;
 };
 
 
 type InventoryLevelInventoryLevel record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int available?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
 };
 
@@ -5767,17 +7910,24 @@
 
 
 type UpdateCommentResponseComment record {
+    @jsondata:Name {value: "blog_id"}
     int blogId?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     string author?;
     string ip?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string body?;
+    @jsondata:Name {value: "article_id"}
     int articleId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
     string email?;
+    @jsondata:Name {value: "user_agent"}
     string userAgent?;
     string status?;
 };
@@ -5803,9 +7953,11 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
@@ -5834,36 +7986,55 @@
 
 type SingleGiftCardGiftCard record {
     anydata? note?;
+    @jsondata:Name {value: "initial_value"}
     string initialValue?;
+    @jsondata:Name {value: "line_item_id"}
     anydata? lineItemId?;
+    @jsondata:Name {value: "api_client_id"}
     anydata? apiClientId?;
+    @jsondata:Name {value: "disabled_at"}
     anydata? disabledAt?;
+    @jsondata:Name {value: "expires_on"}
     anydata? expiresOn?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
     string balance?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "customer_id"}
     anydata? customerId?;
+    @jsondata:Name {value: "last_characters"}
     string lastCharacters?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
 };
 
 
 type MarkCommentResponse record {
+    @jsondata:Name {value: "blog_id"}
     int blogId?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     string author?;
     string ip?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string body?;
+    @jsondata:Name {value: "article_id"}
     int articleId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
     string email?;
+    @jsondata:Name {value: "user_agent"}
     string userAgent?;
     string status?;
 };
@@ -5876,37 +8047,52 @@
 
 type TransactionsListTransactions record {
     string amount?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
+    @jsondata:Name {value: "payment_details"}
     ReopenCloseOrderOrderPaymentDetails paymentDetails?;
     boolean test?;
     string kind?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     anydata? message?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
     string authorization?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "parent_id"}
     int? parentId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "currency_exchange_adjustment"}
     anydata? currencyExchangeAdjustment?;
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
     string currency?;
+    @jsondata:Name {value: "error_code"}
     anydata? errorCode?;
     ReopenCloseOrderOrderReceipt receipt?;
     int id?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
     string gateway?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
     string status?;
 };
 
 
 type TenderTransactionsPaymentDetails record {
+    @jsondata:Name {value: "credit_card_number"}
     string creditCardNumber?;
+    @jsondata:Name {value: "credit_card_company"}
     string creditCardCompany?;
 };
 
 
 type ShippingZonesList record {
+    @jsondata:Name {value: "shipping_zones"}
     DeliveryZone[] shippingZones?;
 };
 
@@ -5936,8 +8122,10 @@
 
 type RetrieveACountOfEventsQueries record {
     # Count only events created at or after this date and time. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Count only events created at or before this date and time. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
 };
 
@@ -5952,11 +8140,15 @@
 
 
 type SingleCarrierServiceCarrierService record {
+    @jsondata:Name {value: "callback_url"}
     string callbackUrl?;
+    @jsondata:Name {value: "carrier_service_type"}
     string carrierServiceType?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string format?;
     string name?;
+    @jsondata:Name {value: "service_discovery"}
     boolean serviceDiscovery?;
     boolean active?;
     int id?;
@@ -5980,12 +8172,18 @@
 
 
 type CancellationResponseFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
@@ -6004,25 +8202,34 @@
 
 type ProductsListProducts record {
     ProductsResponseImages image?;
+    @jsondata:Name {value: "body_html"}
     string? bodyHtml?;
     ProductsResponseImages[] images?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     string title?;
     string tags?;
+    @jsondata:Name {value: "published_scope"}
     string publishedScope?;
+    @jsondata:Name {value: "product_type"}
     string productType?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string vendor?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     ProductsListOptions[] options?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
 };
 
 
 type ProductsListOptions record {
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     string name?;
     int id?;
@@ -6036,7 +8243,9 @@
 
 
 type ShopPoliciesListPolicies record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     string body?;
@@ -6056,15 +8265,23 @@
 
 
 type ProductVariantResponseVariant record {
+    @jsondata:Name {value: "presentment_prices"}
     ProductVariantsPresentmentPrices[] presentmentPrices?;
+    @jsondata:Name {value: "inventory_management"}
     string inventoryManagement?;
+    @jsondata:Name {value: "old_inventory_quantity"}
     int oldInventoryQuantity?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string title?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     string price?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     anydata? option3?;
     string option1?;
@@ -6073,16 +8290,24 @@
     int grams?;
     string? sku?;
     string barcode?;
+    @jsondata:Name {value: "inventory_quantity"}
     int inventoryQuantity?;
+    @jsondata:Name {value: "compare_at_price"}
     anydata? compareAtPrice?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
     decimal weight?;
+    @jsondata:Name {value: "inventory_policy"}
     string inventoryPolicy?;
+    @jsondata:Name {value: "tax_code"}
     string taxCode?;
+    @jsondata:Name {value: "weight_unit"}
     string weightUnit?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int position?;
+    @jsondata:Name {value: "image_id"}
     int imageId?;
 };
 
@@ -6103,70 +8328,100 @@
     string src?;
     string? alt?;
     int width?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int height?;
 };
 
 
 type InventoryLevelsAdjustJsonBody record {
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
+    @jsondata:Name {value: "available_adjustment"}
     int availableAdjustment?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
 };
 
 
 type ApiVersionCarrierServicesJsonBody record {
+    @jsondata:Name {value: "carrier_service"}
     AdminapiapiVersioncarrierServicesJsonCarrierService carrierService?;
 };
 
 
 type AdminapiapiVersioncarrierServicesJsonCarrierService record {
+    @jsondata:Name {value: "callback_url"}
     string callbackUrl?;
     string name?;
+    @jsondata:Name {value: "service_discovery"}
     boolean serviceDiscovery?;
 };
 
 
 type UpdateGiftCard record {
+    @jsondata:Name {value: "gift_card"}
     UpdateGiftCardGiftCard giftCard?;
 };
 
 
 type UpdateGiftCardGiftCard record {
     string? note?;
+    @jsondata:Name {value: "initial_value"}
     string initialValue?;
+    @jsondata:Name {value: "line_item_id"}
     anydata? lineItemId?;
+    @jsondata:Name {value: "api_client_id"}
     anydata? apiClientId?;
+    @jsondata:Name {value: "disabled_at"}
     anydata? disabledAt?;
+    @jsondata:Name {value: "expires_on"}
     string? expiresOn?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
     string balance?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "customer_id"}
     anydata? customerId?;
+    @jsondata:Name {value: "last_characters"}
     string lastCharacters?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
 };
 
 
 type RecurringApplicationChargesRecurringApplicationCharges record {
+    @jsondata:Name {value: "api_client_id"}
     int apiClientId?;
     anydata? test?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "cancelled_on"}
     anydata? cancelledOn?;
+    @jsondata:Name {value: "trial_days"}
     int trialDays?;
+    @jsondata:Name {value: "decorated_return_url"}
     string decoratedReturnUrl?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string price?;
+    @jsondata:Name {value: "trial_ends_on"}
     anydata? trialEndsOn?;
     string name?;
+    @jsondata:Name {value: "return_url"}
     string returnUrl?;
+    @jsondata:Name {value: "billing_on"}
     string billingOn?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "activated_on"}
     anydata? activatedOn?;
     string status?;
 };
@@ -6175,22 +8430,31 @@
 
 type RetrieveAListOfOrdersQueries record {
     # Show orders created at or after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show orders last updated at or before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Filter orders by their fulfillment status.(default: any) 
+    @http:Query {name: "fulfillment_status"}
     string fulfillmentStatus?;
     # Show orders after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show orders imported at or before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "processed_at_max"}
     string processedAtMax?;
     # Show orders imported at or after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "processed_at_min"}
     string processedAtMin?;
     # Show orders created at or before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Show orders last updated at or after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Filter orders by their financial status.(default: any) 
+    @http:Query {name: "financial_status"}
     string financialStatus?;
     string name?;
     # The maximum number of results to show on a page.(default: 50)(maximum: 250) 
@@ -6198,6 +8462,7 @@
     # Retrieve only orders specified by a comma-separated list of order IDs. 
     string ids?;
     # Show orders attributed to a certain app, specified by the app ID. Set as `current` to show orders for the app currently consuming the API. 
+    @http:Query {name: "attribution_app_id"}
     string attributionAppId?;
     # Retrieve only certain fields, specified by a comma-separated list of fields names. 
     string fields?;
@@ -6209,22 +8474,30 @@
 
 type RetrieveAListOfCommentsQueries record {
     # Show comments created after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show comments created before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Show comments last updated before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show comments last updated after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Show comments published after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_min"}
     string publishedAtMin?;
     # The maximum number of results to retrieve.(default: 50)(maximum: 250) 
     string 'limit?;
     # Show comments published before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_max"}
     string publishedAtMax?;
     # Filter results by their published status.(default: any) 
+    @http:Query {name: "published_status"}
     string publishedStatus?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show only certain fields, specified by a comma-separated list of field names. 
     string fields?;
@@ -6234,21 +8507,29 @@
 
 
 type CustomerIdSendInviteJsonBody record {
+    @jsondata:Name {value: "customer_invite"}
     record {|anydata...;|} customerInvite?;
 };
 
 
 type CreateCollectionCustomCollection record {
+    @jsondata:Name {value: "published_scope"}
     string publishedScope?;
     CreateCollectionCustomCollectionImage image?;
+    @jsondata:Name {value: "body_html"}
     anydata? bodyHtml?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string 'handle?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string? publishedAt?;
     string title?;
+    @jsondata:Name {value: "sort_order"}
     string sortOrder?;
 };
 
@@ -6257,6 +8538,7 @@
     string src?;
     string alt?;
     int width?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int height?;
 };
@@ -6273,48 +8555,65 @@
 
 
 type AdminapiapiVersionproductsproductIdimagesimageIdJsonImage record {
+    @jsondata:Name {value: "variant_ids"}
     decimal[] variantIds?;
     int id?;
 };
 
 
 type DiscountCodeList record {
+    @jsondata:Name {value: "discount_codes"}
     DiscountCodeListDiscountCodes[] discountCodes?;
 };
 
 
 type SmartCollectionResponse record {
+    @jsondata:Name {value: "smart_collection"}
     SmartCollectionResponseSmartCollection smartCollection?;
 };
 
 
 type GiftCard record {
+    @jsondata:Name {value: "gift_card"}
     GiftCardGiftCard giftCard?;
 };
 
 
 type GiftCardGiftCard record {
     string? note?;
+    @jsondata:Name {value: "initial_value"}
     string initialValue?;
     string code?;
+    @jsondata:Name {value: "line_item_id"}
     anydata? lineItemId?;
+    @jsondata:Name {value: "api_client_id"}
     int apiClientId?;
+    @jsondata:Name {value: "disabled_at"}
     anydata? disabledAt?;
+    @jsondata:Name {value: "expires_on"}
     anydata? expiresOn?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "template_suffix"}
     string? templateSuffix?;
     string balance?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "customer_id"}
     anydata? customerId?;
+    @jsondata:Name {value: "last_characters"}
     string lastCharacters?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
 };
 
 
 type ScriptTagsscriptTagIdJsonBody record {
+    @jsondata:Name {value: "script_tag"}
     AdminapiapiVersionscriptTagsscriptTagIdJsonScriptTag scriptTag?;
 };
 
@@ -6327,10 +8626,14 @@
 
 type CreateThemeResponseTheme record {
     string role?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "theme_store_id"}
     anydata? themeStoreId?;
     string name?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     boolean processing?;
     int id?;
@@ -6339,6 +8642,7 @@
 
 
 type AvailableInventory record {
+    @jsondata:Name {value: "inventory_level"}
     AvailableInventoryInventoryLevel inventoryLevel?;
 };
 
@@ -6364,32 +8668,46 @@
 
 
 type ProductToCollectionResponseCollect record {
+    @jsondata:Name {value: "collection_id"}
     int collectionId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int id?;
     int position?;
+    @jsondata:Name {value: "sort_value"}
     string sortValue?;
 };
 
 
 type AcceptFulfillmentResponse record {
+    @jsondata:Name {value: "fulfillment_order"}
     AcceptFulfillmentResponseFulfillmentOrder fulfillmentOrder?;
 };
 
 
 type AcceptFulfillmentResponseFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     FulfillmentOrdersAssignedLocation origin?;
     AcceptFulfillmentResponseFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     AcceptFulfillmentResponseFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "outgoing_requests"}
     anydata[] outgoingRequests?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     string[] supportedActions?;
     string status?;
 };
@@ -6403,32 +8721,45 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
 
 
 type OriginalFulfillmentOrder record {
+    @jsondata:Name {value: "submitted_fulfillment_order"}
     OriginalFulfillmentOrderSubmittedFulfillmentOrder submittedFulfillmentOrder?;
+    @jsondata:Name {value: "original_fulfillment_order"}
     OriginalFulfillmentOrderOriginalFulfillmentOrder originalFulfillmentOrder?;
+    @jsondata:Name {value: "unsubmitted_fulfillment_order"}
     OriginalFulfillmentOrderUnsubmittedFulfillmentOrder|() unsubmittedFulfillmentOrder?;
 };
 
 
 type OriginalFulfillmentOrderOriginalFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     FulfillmentOrdersAssignedLocation origin?;
     OriginalFulfillmentOrderOriginalFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     OriginalFulfillmentOrderOriginalFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "outgoing_requests"}
     anydata[] outgoingRequests?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     anydata[] supportedActions?;
     string status?;
 };
@@ -6442,9 +8773,11 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
@@ -6460,24 +8793,31 @@
 
 type RetrieveAListOfCustomCollectionsQueries record {
     # Show custom collections last updated before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show custom collections last updated after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Show custom collections that include a given product. 
+    @http:Query {name: "product_id"}
     string productId?;
     # Show custom collections published after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_min"}
     string publishedAtMin?;
     # The maximum number of results to retrieve.(default: 50)(maximum: 250) 
     string 'limit?;
     # Show only collections specified by a comma-separated list of IDs. 
     string ids?;
     # Show custom collections published before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_max"}
     string publishedAtMax?;
     # Filter by custom collection handle. 
     string 'handle?;
     # Show custom collectsion with a given published status.(default: any) 
+    @http:Query {name: "published_status"}
     string publishedStatus?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show custom collections with a given title. 
     string title?;
@@ -6487,34 +8827,45 @@
 
 
 type ApplicationChargesList record {
+    @jsondata:Name {value: "application_charges"}
     ApplicationChargesListApplicationCharges[] applicationCharges?;
 };
 
 
 type DiscountCodesDiscountCodes record {
+    @jsondata:Name {value: "usage_count"}
     int usageCount?;
     string code?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "price_rule_id"}
     int priceRuleId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int id?;
 };
 
 
 type ApiVersionScriptTagsJsonBody record {
+    @jsondata:Name {value: "script_tag"}
     AdminapiapiVersionredirectsJsonRedirect scriptTag?;
 };
 
 
 type StorefrontAccessToken record {
+    @jsondata:Name {value: "storefront_access_token"}
     StorefrontAccessTokenStorefrontAccessToken storefrontAccessToken?;
 };
 
 
 type StorefrontAccessTokenStorefrontAccessToken record {
+    @jsondata:Name {value: "access_token"}
     string accessToken?;
+    @jsondata:Name {value: "access_scope"}
     string accessScope?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int id?;
     string title?;
@@ -6522,6 +8873,7 @@
 
 
 type AdminapiapiVersionpagesJsonPage record {
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     boolean published?;
     string title?;
@@ -6530,35 +8882,51 @@
 
 type CreateProductResponseProduct record {
     record {|anydata...;|}? image?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     anydata[] images?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     CreateProductResponseProductVariants[] variants?;
     string title?;
     string tags?;
+    @jsondata:Name {value: "published_scope"}
     string publishedScope?;
+    @jsondata:Name {value: "product_type"}
     string productType?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string vendor?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     CreateProductResponseProductOptions[] options?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string? publishedAt?;
 };
 
 
 type CreateProductResponseProductVariants record {
+    @jsondata:Name {value: "presentment_prices"}
     CreateProductResponseProductPresentmentPrices[] presentmentPrices?;
+    @jsondata:Name {value: "inventory_management"}
     anydata? inventoryManagement?;
+    @jsondata:Name {value: "old_inventory_quantity"}
     int oldInventoryQuantity?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string title?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     string price?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     anydata? option3?;
     string option1?;
@@ -6567,26 +8935,35 @@
     int grams?;
     string? sku?;
     anydata? barcode?;
+    @jsondata:Name {value: "inventory_quantity"}
     int inventoryQuantity?;
+    @jsondata:Name {value: "compare_at_price"}
     anydata? compareAtPrice?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
     decimal weight?;
+    @jsondata:Name {value: "inventory_policy"}
     string inventoryPolicy?;
+    @jsondata:Name {value: "weight_unit"}
     string weightUnit?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int position?;
+    @jsondata:Name {value: "image_id"}
     anydata? imageId?;
 };
 
 
 type CreateProductResponseProductPresentmentPrices record {
+    @jsondata:Name {value: "compare_at_price"}
     anydata? compareAtPrice?;
     ReopenCloseOrderOrderTotalDiscountSetPresentmentMoney price?;
 };
 
 
 type InventoryListResponse record {
+    @jsondata:Name {value: "inventory_levels"}
     InventoryListResponseInventoryLevels[] inventoryLevels?;
 };
 
@@ -6594,26 +8971,34 @@
 
 type RetrieveAListOfAllArticlesFromABlogQueries record {
     # Show articles created after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show articles last updated before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Filter articles by article author. 
     string author?;
     # Show articles published after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_min"}
     string publishedAtMin?;
     # Retrieve an article with a specific handle. 
     string 'handle?;
     # Retrieve results based on their published status.(default: any) 
+    @http:Query {name: "published_status"}
     string publishedStatus?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show articles created before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Show articles last updated after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # The maximum number of results to retrieve.(default: 50)(maximum: 250) 
     string 'limit?;
     # Show articles published before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_max"}
     string publishedAtMax?;
     # Filter articles with a specific tag. 
     string tag?;
@@ -6628,15 +9013,22 @@
 
 
 type UpdatePageResponsePage record {
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string author?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string? publishedAt?;
     string title?;
 };
@@ -6649,10 +9041,13 @@
 
 
 type UpdateScriptTagResponseScriptTag record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string src?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int id?;
+    @jsondata:Name {value: "display_scope"}
     string displayScope?;
     string event?;
 };
@@ -6664,17 +9059,23 @@
 
 
 type CollectsListCollects record {
+    @jsondata:Name {value: "collection_id"}
     int collectionId?;
+    @jsondata:Name {value: "updated_at"}
     anydata? updatedAt?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
+    @jsondata:Name {value: "created_at"}
     anydata? createdAt?;
     int id?;
     int position?;
+    @jsondata:Name {value: "sort_value"}
     string sortValue?;
 };
 
 
 type GiftCardSearch record {
+    @jsondata:Name {value: "gift_cards"}
     GiftCardSearchGiftCards[] giftCards?;
 };
 
@@ -6695,6 +9096,7 @@
 
 type AdminapiapiVersiondraftOrdersJsonDraftOrderLineItems record {
     int quantity?;
+    @jsondata:Name {value: "applied_discount"}
     AdminapiapiVersiondraftOrdersJsonDraftOrderAppliedDiscount appliedDiscount?;
     string price?;
     string title?;
@@ -6703,6 +9105,7 @@
 
 type AdminapiapiVersiondraftOrdersJsonDraftOrderAppliedDiscount record {
     string amount?;
+    @jsondata:Name {value: "value_type"}
     string valueType?;
     string description?;
     string title?;
@@ -6713,8 +9116,10 @@
 
 type RetrieveAListOfReportsQueries record {
     # Show reports last updated before date. (format: 2014-04-25T16:15:47-04:00)
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show reports last updated after date. (format: 2014-04-25T16:15:47-04:00)
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # The amount of results to return
     string 'limit?;
@@ -6723,20 +9128,26 @@
     # A comma-separated list of fields to include in the response
     string fields?;
     # Restrict results to after the specified ID
+    @http:Query {name: "since_id"}
     string sinceId?;
 };
 
 
 type CreateDiscountCode record {
+    @jsondata:Name {value: "discount_code"}
     CreateDiscountCodeDiscountCode discountCode?;
 };
 
 
 type CreateDiscountCodeDiscountCode record {
+    @jsondata:Name {value: "usage_count"}
     int usageCount?;
     string code?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "price_rule_id"}
     int priceRuleId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int id?;
 };
@@ -6756,16 +9167,21 @@
 
 type RetrieveAListOfAbandonedCheckoutsQueries record {
     # Show checkouts created after the specified date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show checkouts created before the specified date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Show checkouts last updated before the specified date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show checkouts last updated after the specified date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # The maximum number of results to show.(default: 50)(maximum: 250) 
     string 'limit?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show only checkouts with a given status.(default: open) 
     string status?;
@@ -6781,21 +9197,29 @@
     string amount?;
     boolean test?;
     string fee?;
+    @jsondata:Name {value: "source_order_id"}
     int? sourceOrderId?;
+    @jsondata:Name {value: "source_type"}
     string? sourceType?;
     string 'type?;
+    @jsondata:Name {value: "payout_id"}
     int payoutId?;
+    @jsondata:Name {value: "payout_status"}
     string payoutStatus?;
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
+    @jsondata:Name {value: "source_order_transaction_id"}
     int? sourceOrderTransactionId?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "source_id"}
     int? sourceId?;
     string net?;
 };
 
 
 type ApiVersionStorefrontAccessTokensJsonBody record {
+    @jsondata:Name {value: "storefront_access_token"}
     AdminapiapiVersionstorefrontAccessTokensJsonStorefrontAccessToken storefrontAccessToken?;
 };
 
@@ -6806,12 +9230,17 @@
 
 
 type UsageChargeListUsageCharges record {
+    @jsondata:Name {value: "risk_level"}
     decimal riskLevel?;
     string price?;
+    @jsondata:Name {value: "balance_used"}
     decimal balanceUsed?;
+    @jsondata:Name {value: "balance_remaining"}
     decimal balanceRemaining?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string description?;
+    @jsondata:Name {value: "billing_on"}
     anydata? billingOn?;
     string currency?;
     int id?;
@@ -6820,17 +9249,24 @@
 
 type SmartCollectionListSmartCollections record {
     UpdateCustomCollectionCustomCollectionImage image?;
+    @jsondata:Name {value: "body_html"}
     string? bodyHtml?;
     string 'handle?;
     SmartCollectionResponseSmartCollectionRules[] rules?;
     string title?;
+    @jsondata:Name {value: "published_scope"}
     string publishedScope?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     boolean disjunctive?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
+    @jsondata:Name {value: "sort_order"}
     string sortOrder?;
 };
 
@@ -6842,19 +9278,28 @@
 
 type ArticleArticle record {
     ArticleArticleImage image?;
+    @jsondata:Name {value: "blog_id"}
     int blogId?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     string author?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     string title?;
     string tags?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string? publishedAt?;
+    @jsondata:Name {value: "summary_html"}
     anydata? summaryHtml?;
 };
 
@@ -6867,26 +9312,39 @@
 
 
 type GiftCardsList record {
+    @jsondata:Name {value: "gift_cards"}
     GiftCardsListGiftCards[] giftCards?;
 };
 
 
 type GiftCardsListGiftCards record {
     anydata? note?;
+    @jsondata:Name {value: "initial_value"}
     string initialValue?;
+    @jsondata:Name {value: "line_item_id"}
     anydata? lineItemId?;
+    @jsondata:Name {value: "api_client_id"}
     anydata? apiClientId?;
+    @jsondata:Name {value: "disabled_at"}
     anydata? disabledAt?;
+    @jsondata:Name {value: "expires_on"}
     string? expiresOn?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
     string balance?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "customer_id"}
     anydata? customerId?;
+    @jsondata:Name {value: "last_characters"}
     string lastCharacters?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
 };
 
@@ -6897,6 +9355,7 @@
 
 
 type ApiVersionMarketingEventsJsonBody record {
+    @jsondata:Name {value: "marketing_event"}
     AdminapiapiVersionmarketingEventsJsonMarketingEvent marketingEvent?;
 };
 
@@ -6914,9 +9373,11 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
@@ -6930,9 +9391,13 @@
 
 
 type SinglePaymentResponsePayment record {
+    @jsondata:Name {value: "unique_token"}
     string uniqueToken?;
+    @jsondata:Name {value: "credit_card"}
     anydata? creditCard?;
+    @jsondata:Name {value: "payment_processing_error_message"}
     anydata? paymentProcessingErrorMessage?;
+    @jsondata:Name {value: "next_action"}
     SinglePaymentResponsePaymentNextAction nextAction?;
     int id?;
     SinglePaymentResponsePaymentCheckout checkout?;
@@ -6942,46 +9407,75 @@
 
 
 type PriceRulePriceRule record {
+    @jsondata:Name {value: "once_per_customer"}
     boolean oncePerCustomer?;
+    @jsondata:Name {value: "starts_at"}
     string startsAt?;
+    @jsondata:Name {value: "usage_limit"}
     int? usageLimit?;
+    @jsondata:Name {value: "value_type"}
     string valueType?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "prerequisite_customer_ids"}
     anydata[] prerequisiteCustomerIds?;
     string title?;
+    @jsondata:Name {value: "entitled_collection_ids"}
     int[] entitledCollectionIds?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "prerequisite_product_ids"}
     anydata[] prerequisiteProductIds?;
+    @jsondata:Name {value: "prerequisite_shipping_price_range"}
     anydata? prerequisiteShippingPriceRange?;
+    @jsondata:Name {value: "entitled_country_ids"}
     anydata[] entitledCountryIds?;
+    @jsondata:Name {value: "entitled_variant_ids"}
     anydata[] entitledVariantIds?;
+    @jsondata:Name {value: "ends_at"}
     anydata? endsAt?;
     int id?;
     string value?;
+    @jsondata:Name {value: "prerequisite_subtotal_range"}
     record {|anydata...;|}? prerequisiteSubtotalRange?;
+    @jsondata:Name {value: "allocation_method"}
     string allocationMethod?;
+    @jsondata:Name {value: "prerequisite_to_entitlement_quantity_ratio"}
     PriceRulePriceRulePrerequisiteToEntitlementQuantityRatio prerequisiteToEntitlementQuantityRatio?;
+    @jsondata:Name {value: "prerequisite_quantity_range"}
     anydata? prerequisiteQuantityRange?;
+    @jsondata:Name {value: "allocation_limit"}
     int? allocationLimit?;
+    @jsondata:Name {value: "target_type"}
     string targetType?;
+    @jsondata:Name {value: "entitled_product_ids"}
     anydata[] entitledProductIds?;
+    @jsondata:Name {value: "customer_selection"}
     string customerSelection?;
+    @jsondata:Name {value: "prerequisite_saved_search_ids"}
     anydata[] prerequisiteSavedSearchIds?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "prerequisite_variant_ids"}
     anydata[] prerequisiteVariantIds?;
+    @jsondata:Name {value: "target_selection"}
     string targetSelection?;
+    @jsondata:Name {value: "prerequisite_collection_ids"}
     anydata[] prerequisiteCollectionIds?;
 };
 
 
 type PriceRulePriceRulePrerequisiteToEntitlementQuantityRatio record {
+    @jsondata:Name {value: "prerequisite_quantity"}
     int? prerequisiteQuantity?;
+    @jsondata:Name {value: "entitled_quantity"}
     int? entitledQuantity?;
 };
 
 
 type CustomerInviteCustomerInvite record {
     # Custom message included in the invitation email
+    @jsondata:Name {value: "custom_message"}
     string customMessage;
     # Blind carbon copy recipients
     string[] bcc?;
@@ -6995,31 +9489,45 @@
 
 
 type PagesListResponsePages record {
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "body_html"}
     string? bodyHtml?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string author?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
     string title?;
 };
 
 
 type CollectionListCustomCollections record {
+    @jsondata:Name {value: "published_scope"}
     string publishedScope?;
     UpdateCustomCollectionCustomCollectionImage image?;
+    @jsondata:Name {value: "body_html"}
     string? bodyHtml?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string 'handle?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
     string title?;
+    @jsondata:Name {value: "sort_order"}
     string sortOrder?;
 };
 
@@ -7032,38 +9540,50 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
 
 
 type ProductListingsProductListings record {
+    @jsondata:Name {value: "body_html"}
     string? bodyHtml?;
     ProductListingsImages[] images?;
     boolean available?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     ProductListingsVariants[] variants?;
     string title?;
     string tags?;
+    @jsondata:Name {value: "product_type"}
     string productType?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string vendor?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     ProductListingsOptions[] options?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
 };
 
 
 type ProductListingsImages record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string src?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     int width?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "variant_ids"}
     anydata[] variantIds?;
     int id?;
     int position?;
@@ -7072,25 +9592,37 @@
 
 
 type ProductListingsVariants record {
+    @jsondata:Name {value: "formatted_price"}
     string formattedPrice?;
+    @jsondata:Name {value: "inventory_quantity"}
     int inventoryQuantity?;
+    @jsondata:Name {value: "compare_at_price"}
     anydata? compareAtPrice?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
+    @jsondata:Name {value: "inventory_management"}
     string inventoryManagement?;
     boolean taxable?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "option_values"}
     ProductListingsOptionValues[] optionValues?;
     boolean available?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     decimal weight?;
     string title?;
+    @jsondata:Name {value: "inventory_policy"}
     string inventoryPolicy?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "weight_unit"}
     string weightUnit?;
     string price?;
     int id?;
     int position?;
     int grams?;
+    @jsondata:Name {value: "image_id"}
     int? imageId?;
     string? sku?;
     string barcode?;
@@ -7100,18 +9632,25 @@
 
 type RetrieveACountOfAllArticlesFromABlogQueries record {
     # Count articles created after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Count articles created before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Count articles last updated before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Count articles last updated after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Count articles published after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_min"}
     string publishedAtMin?;
     # Count articles published before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_max"}
     string publishedAtMax?;
     # Count articles with a given published status.(default: any) 
+    @http:Query {name: "published_status"}
     string publishedStatus?;
 };
 
@@ -7127,18 +9666,25 @@
 
 type RetrieveAPageCountQueries record {
     # Count pages created after date (format: 2008-12-31). 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Count pages created before date (format: 2008-12-31). 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Count pages last updated before date (format: 2008-12-31). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Count pages last updated after date (format: 2008-12-31). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Show pages published after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_min"}
     string publishedAtMin?;
     # Show pages published before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_max"}
     string publishedAtMax?;
     # Count pages with a given published status:(default: any) 
+    @http:Query {name: "published_status"}
     string publishedStatus?;
     # Count pages with a given title. 
     string title?;
@@ -7146,10 +9692,12 @@
 
 
 type ReportListReports record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string name?;
     int id?;
     string category?;
+    @jsondata:Name {value: "shopify_ql"}
     string shopifyQl?;
 };
 
@@ -7160,13 +9708,18 @@
 
 
 type ModifyProductImageImage record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string src?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     string? alt?;
     int width?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "variant_ids"}
     anydata[] variantIds?;
     int id?;
     int position?;
@@ -7180,16 +9733,19 @@
 
 
 type SmartCollectionList record {
+    @jsondata:Name {value: "smart_collections"}
     SmartCollectionListSmartCollections[] smartCollections?;
 };
 
 
 type ApiVersionDraftOrdersJsonBody record {
+    @jsondata:Name {value: "draft_order"}
     AdminapiapiVersiondraftOrdersJsonDraftOrder draftOrder?;
 };
 
 
 type AdminapiapiVersiondraftOrdersJsonDraftOrder record {
+    @jsondata:Name {value: "line_items"}
     AdminapiapiVersiondraftOrdersJsonDraftOrderLineItems[] lineItems?;
 };
 
@@ -7200,21 +9756,33 @@
 
 
 type SingleFulfillmentFulfillment record {
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "line_items"}
     ReopenCloseOrderOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "tracking_company"}
     string trackingCompany?;
+    @jsondata:Name {value: "tracking_urls"}
     string[] trackingUrls?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string 'service?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string name?;
+    @jsondata:Name {value: "tracking_number"}
     string trackingNumber?;
     ReopenCloseOrderOrderReceipt receipt?;
     int id?;
+    @jsondata:Name {value: "tracking_numbers"}
     string[] trackingNumbers?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "tracking_url"}
     string trackingUrl?;
+    @jsondata:Name {value: "shipment_status"}
     anydata? shipmentStatus?;
     string status?;
 };
@@ -7223,45 +9791,61 @@
 type DisputesDisputes record {
     string reason?;
     string amount?;
+    @jsondata:Name {value: "evidence_due_by"}
     string evidenceDueBy?;
+    @jsondata:Name {value: "finalized_on"}
     anydata? finalizedOn?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "initiated_at"}
     string initiatedAt?;
     string 'type?;
+    @jsondata:Name {value: "network_reason_code"}
     string networkReasonCode?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "evidence_sent_on"}
     string? evidenceSentOn?;
     string status?;
 };
 
 
 type OrdersListOrders record {
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
     string name?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int id?;
 };
 
 
 type SingleFulfillmentOrderFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
 
 
 type FulfillmentOrderIdRescheduleJsonBody record {
+    @jsondata:Name {value: "fulfillment_order"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdholdJsonFulfillmentOrder fulfillmentOrder?;
 };
 
 
 type AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdholdJsonFulfillmentOrder record {
+    @jsondata:Name {value: "new_location_id"}
     int newLocationId?;
 };
 
@@ -7274,16 +9858,22 @@
 
 type RetrieveAnOrderCountQueries record {
     # Count orders created after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Count orders created before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Count orders last updated before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Filter orders by their fulfillment status.(default: any) 
+    @http:Query {name: "fulfillment_status"}
     string fulfillmentStatus?;
     # Count orders last updated after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Count orders of a given financial status.(default: any) 
+    @http:Query {name: "financial_status"}
     string financialStatus?;
     # Count orders of a given status.(default: open) 
     string status?;
@@ -7297,6 +9887,7 @@
     # The maximum number of results to show.(default: 50)(maximum: 250) 
     string 'limit?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show only certain fields, specified by a comma-separated list of field names. 
     string fields?;
@@ -7311,16 +9902,25 @@
 
 
 type MoveFulfillmentOrderResponseMovedFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     MoveFulfillmentOrderResponseMovedFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     MoveFulfillmentOrderResponseMovedFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     string[] supportedActions?;
+    @jsondata:Name {value: "assigned_location"}
     MoveFulfillmentOrderResponseMovedFulfillmentOrderAssignedLocation assignedLocation?;
+    @jsondata:Name {value: "merchant_requests"}
     anydata[] merchantRequests?;
     string status?;
 };
@@ -7328,6 +9928,7 @@
 
 type MoveFulfillmentOrderResponseMovedFulfillmentOrderAssignedLocation record {
     string zip?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     string province?;
     anydata? address2?;
@@ -7335,6 +9936,7 @@
     anydata? phone?;
     string address1?;
     string name?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
 };
 
@@ -7362,6 +9964,7 @@
 
 
 type CreatSmartCollection record {
+    @jsondata:Name {value: "smart_collection"}
     CreatSmartCollectionSmartCollection smartCollection?;
 };
 
@@ -7374,30 +9977,46 @@
 
 
 type ApplicationChargeResponse record {
+    @jsondata:Name {value: "recurring_application_charge"}
     ApplicationChargeResponseRecurringApplicationCharge recurringApplicationCharge?;
 };
 
 
 type ApplicationChargeResponseRecurringApplicationCharge record {
+    @jsondata:Name {value: "api_client_id"}
     int apiClientId?;
     boolean? test?;
+    @jsondata:Name {value: "balance_used"}
     decimal balanceUsed?;
+    @jsondata:Name {value: "balance_remaining"}
     decimal balanceRemaining?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "cancelled_on"}
     anydata? cancelledOn?;
+    @jsondata:Name {value: "trial_days"}
     int trialDays?;
+    @jsondata:Name {value: "decorated_return_url"}
     string decoratedReturnUrl?;
+    @jsondata:Name {value: "capped_amount"}
     string cappedAmount?;
+    @jsondata:Name {value: "risk_level"}
     decimal riskLevel?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "confirmation_url"}
     string confirmationUrl?;
     string price?;
+    @jsondata:Name {value: "trial_ends_on"}
     anydata? trialEndsOn?;
     string name?;
+    @jsondata:Name {value: "return_url"}
     string returnUrl?;
+    @jsondata:Name {value: "billing_on"}
     anydata? billingOn?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "activated_on"}
     anydata? activatedOn?;
     string status?;
 };
@@ -7409,6 +10028,7 @@
 
 
 type AdminapiapiVersionresourceFeedbackJsonResourceFeedback record {
+    @jsondata:Name {value: "feedback_generated_at"}
     string feedbackGeneratedAt?;
     string state?;
 };
@@ -7431,63 +10051,97 @@
 
 
 type FulfillmentFulfillment record {
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "line_items"}
     FulfillmentFulfillmentLineItems[] lineItems?;
+    @jsondata:Name {value: "tracking_company"}
     string trackingCompany?;
+    @jsondata:Name {value: "tracking_urls"}
     string[] trackingUrls?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string 'service?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string name?;
+    @jsondata:Name {value: "tracking_number"}
     string trackingNumber?;
     record {|anydata...;|} receipt?;
     int id?;
+    @jsondata:Name {value: "tracking_numbers"}
     string[] trackingNumbers?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "tracking_url"}
     string trackingUrl?;
+    @jsondata:Name {value: "shipment_status"}
     anydata? shipmentStatus?;
     string status?;
 };
 
 
 type FulfillmentFulfillmentLineItems record {
+    @jsondata:Name {value: "variant_title"}
     string? variantTitle?;
+    @jsondata:Name {value: "fulfillment_status"}
     string fulfillmentStatus?;
+    @jsondata:Name {value: "total_discount"}
     string totalDiscount?;
+    @jsondata:Name {value: "gift_card"}
     boolean giftCard?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "total_discount_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalDiscountSet?;
     string title?;
+    @jsondata:Name {value: "product_exists"}
     boolean productExists?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
     string price?;
     anydata? vendor?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     int id?;
     int grams?;
     string? sku?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
     int quantity?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
+    @jsondata:Name {value: "discount_allocations"}
     anydata[] discountAllocations?;
+    @jsondata:Name {value: "variant_inventory_management"}
     anydata? variantInventoryManagement?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string name?;
+    @jsondata:Name {value: "price_set"}
     ReopenCloseOrderOrderTotalDiscountsSet priceSet?;
     anydata[] properties?;
 };
 
 
 type TransitionFulfillmentOrderFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
@@ -7504,37 +10158,52 @@
 
 
 type CreateShopFeedback record {
+    @jsondata:Name {value: "resource_feedback"}
     CreateShopFeedbackResourceFeedback resourceFeedback?;
 };
 
 
 type CreateShopFeedbackResourceFeedback record {
+    @jsondata:Name {value: "resource_updated_at"}
     anydata? resourceUpdatedAt?;
+    @jsondata:Name {value: "feedback_generated_at"}
     string feedbackGeneratedAt?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "resource_type"}
     string resourceType?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     anydata[] messages?;
+    @jsondata:Name {value: "resource_id"}
     int resourceId?;
     string state?;
 };
 
 
 type ApplicationCharge record {
+    @jsondata:Name {value: "application_charge"}
     ApplicationChargeApplicationCharge applicationCharge?;
 };
 
 
 type ApplicationChargeApplicationCharge record {
+    @jsondata:Name {value: "charge_type"}
     anydata? chargeType?;
+    @jsondata:Name {value: "api_client_id"}
     int apiClientId?;
     boolean? test?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "decorated_return_url"}
     string decoratedReturnUrl?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "confirmation_url"}
     string confirmationUrl?;
     string price?;
     string name?;
+    @jsondata:Name {value: "return_url"}
     string returnUrl?;
     string currency?;
     int id?;
@@ -7543,32 +10212,50 @@
 
 
 type MarketingEvents record {
+    @jsondata:Name {value: "marketing_events"}
     MarketingEventMarketingEvent[] marketingEvents?;
 };
 
 
 type MarketingEventMarketingEvent record {
+    @jsondata:Name {value: "manage_url"}
     anydata? manageUrl?;
+    @jsondata:Name {value: "utm_campaign"}
     string utmCampaign?;
+    @jsondata:Name {value: "remote_id"}
     string remoteId?;
+    @jsondata:Name {value: "utm_medium"}
     string utmMedium?;
     anydata? description?;
+    @jsondata:Name {value: "breadcrumb_id"}
     anydata? breadcrumbId?;
+    @jsondata:Name {value: "event_type"}
     string eventType?;
+    @jsondata:Name {value: "preview_url"}
     anydata? previewUrl?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     boolean paid?;
+    @jsondata:Name {value: "marketing_activity_id"}
     anydata? marketingActivityId?;
+    @jsondata:Name {value: "started_at"}
     string startedAt?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "marketing_channel"}
     string marketingChannel?;
+    @jsondata:Name {value: "marketed_resources"}
     anydata[] marketedResources?;
+    @jsondata:Name {value: "scheduled_to_end_at"}
     anydata? scheduledToEndAt?;
+    @jsondata:Name {value: "budget_type"}
     string budgetType?;
+    @jsondata:Name {value: "ended_at"}
     anydata? endedAt?;
     string budget?;
+    @jsondata:Name {value: "referring_domain"}
     string referringDomain?;
+    @jsondata:Name {value: "utm_source"}
     string utmSource?;
 };
 
@@ -7580,6 +10267,7 @@
 
 
 type RejectFulfillmentResponse record {
+    @jsondata:Name {value: "fulfillment_order"}
     RejectFulfillmentResponseFulfillmentOrder fulfillmentOrder?;
 };
 
@@ -7587,6 +10275,7 @@
 type CreateCountryCountry record {
     anydata[] provinces?;
     string code?;
+    @jsondata:Name {value: "tax_name"}
     string taxName?;
     string name?;
     decimal tax?;
@@ -7636,16 +10325,19 @@
 
 type RetrieveAListOfEventsQueries record {
     # Show events created at or after this date and time. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show events specified in this filter. 
     string filter?;
     # Show events created at or before this date and time. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # The number of results to show.(default: 50)(maximum: 250) 
     string 'limit?;
     # Show events of a certain type. 
     string verb?;
     # Show only results after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show only certain fields, specified by a comma-separated list of field names. 
     string fields?;
@@ -7653,6 +10345,7 @@
 
 
 type RecurringApplicationCharges record {
+    @jsondata:Name {value: "recurring_application_charges"}
     RecurringApplicationChargesRecurringApplicationCharges[] recurringApplicationCharges?;
 };
 
@@ -7662,21 +10355,29 @@
     # A comma-separated list of fields to include in the response. 
     string fields?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
 };
 
 
 type InventoryLevels record {
+    @jsondata:Name {value: "inventory_levels"}
     InventoryLevelsInventoryLevels[] inventoryLevels?;
 };
 
 
 type AdminapiapiVersionmarketingEventsmarketingEventIdengagementsJsonEngagements record {
+    @jsondata:Name {value: "is_cumulative"}
     boolean isCumulative?;
+    @jsondata:Name {value: "ad_spend"}
     decimal adSpend?;
+    @jsondata:Name {value: "occurred_on"}
     string occurredOn?;
+    @jsondata:Name {value: "favorites_count"}
     int favoritesCount?;
+    @jsondata:Name {value: "clicks_count"}
     int clicksCount?;
+    @jsondata:Name {value: "views_count"}
     int viewsCount?;
 };
 
@@ -7687,34 +10388,45 @@
 
 
 type UpdateReportResponseReport record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string name?;
     int id?;
     string category?;
+    @jsondata:Name {value: "shopify_ql"}
     string shopifyQl?;
 };
 
 
 type CarrierServicescarrierServiceIdJsonBody record {
+    @jsondata:Name {value: "carrier_service"}
     AdminapiapiVersioncarrierServicescarrierServiceIdJsonCarrierService carrierService?;
 };
 
 
 type CalculateRefundRefundRefundLineItems record {
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
     string price?;
     string subtotal?;
+    @jsondata:Name {value: "discounted_total_price"}
     string discountedTotalPrice?;
+    @jsondata:Name {value: "total_cart_discount_amount"}
     string totalCartDiscountAmount?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "discounted_price"}
     string discountedPrice?;
+    @jsondata:Name {value: "restock_type"}
     string restockType?;
 };
 
 
 type FulfillmentOrderIdCancellationRequestJsonBody record {
+    @jsondata:Name {value: "cancellation_request"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdcancellationRequestJsonCancellationRequest cancellationRequest?;
 };
 
@@ -7725,17 +10437,24 @@
 
 
 type ArticleCommentsComments record {
+    @jsondata:Name {value: "blog_id"}
     int blogId?;
+    @jsondata:Name {value: "body_html"}
     string? bodyHtml?;
     string author?;
     string ip?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string body?;
+    @jsondata:Name {value: "article_id"}
     int articleId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     anydata? publishedAt?;
     string email?;
+    @jsondata:Name {value: "user_agent"}
     string userAgent?;
     string status?;
 };
@@ -7747,9 +10466,12 @@
 
 
 type AdminapiapiVersioncheckoutstokenpaymentsJsonPayment record {
+    @jsondata:Name {value: "unique_token"}
     string uniqueToken?;
     string amount?;
+    @jsondata:Name {value: "session_id"}
     string sessionId?;
+    @jsondata:Name {value: "request_details"}
     AdminapiapiVersioncheckoutstokenpaymentsJsonPaymentRequestDetails requestDetails?;
 };
 
@@ -7760,6 +10482,7 @@
 
 
 type ApplicationCredit record {
+    @jsondata:Name {value: "application_credit"}
     ApplicationCreditApplicationCredit applicationCredit?;
 };
 
@@ -7774,17 +10497,24 @@
 
 
 type SingleCommentResponseComment record {
+    @jsondata:Name {value: "blog_id"}
     int blogId?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     string author?;
     string ip?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string body?;
+    @jsondata:Name {value: "article_id"}
     int articleId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     anydata? publishedAt?;
     string email?;
+    @jsondata:Name {value: "user_agent"}
     string userAgent?;
     string status?;
 };
@@ -7796,20 +10526,27 @@
 
 
 type TenderTransactions record {
+    @jsondata:Name {value: "tender_transactions"}
     TenderTransactionsTenderTransactions[] tenderTransactions?;
 };
 
 
 type TenderTransactionsTenderTransactions record {
     string amount?;
+    @jsondata:Name {value: "payment_details"}
     TenderTransactionsPaymentDetails paymentDetails?;
     boolean test?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "remote_reference"}
     string remoteReference?;
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "payment_method"}
     string paymentMethod?;
 };
 
@@ -7817,6 +10554,7 @@
 
 type RetrieveAListOfProvincesForACountryQueries record {
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show only certain fields, specified by a comma-separated list of fields names. 
     string fields?;
@@ -7832,6 +10570,7 @@
 
 type ReceiveACountOfAllProductImagesQueries record {
     # Restrict results to after the specified ID 
+    @http:Query {name: "since_id"}
     string sinceId?;
 };
 
@@ -7842,29 +10581,37 @@
 
 
 type CappedAmountCharge record {
+    @jsondata:Name {value: "recurring_application_charge"}
     CappedAmountChargeRecurringApplicationCharge recurringApplicationCharge?;
 };
 
 
 type ProductIds record {
+    @jsondata:Name {value: "product_ids"}
     int[] productIds?;
 };
 
 
 type SingleProvinceProvince record {
     string code?;
+    @jsondata:Name {value: "tax_type"}
     string taxType?;
+    @jsondata:Name {value: "tax_name"}
     string taxName?;
     string name?;
+    @jsondata:Name {value: "tax_percentage"}
     decimal taxPercentage?;
     decimal tax?;
     int id?;
+    @jsondata:Name {value: "shipping_zone_id"}
     anydata? shippingZoneId?;
+    @jsondata:Name {value: "country_id"}
     int countryId?;
 };
 
 
 type UpdateFulfillmentService record {
+    @jsondata:Name {value: "fulfillment_service"}
     UpdateFulfillmentServiceFulfillmentService fulfillmentService?;
 };
 
@@ -7881,17 +10628,23 @@
 
 
 type AssetsListAssets record {
+    @jsondata:Name {value: "public_url"}
     string? publicUrl?;
+    @jsondata:Name {value: "content_type"}
     string contentType?;
     int size?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "theme_id"}
     int themeId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'key?;
 };
 
 
 type ApplicationCredits record {
+    @jsondata:Name {value: "application_credits"}
     ApplicationCreditApplicationCredit[] applicationCredits?;
 };
 
@@ -7907,6 +10660,7 @@
 
 
 type CalculateRefundRefund record {
+    @jsondata:Name {value: "refund_line_items"}
     CalculateRefundRefundRefundLineItems[] refundLineItems?;
     CalculateRefundRefundShipping shipping?;
     string currency?;
@@ -7916,6 +10670,7 @@
 
 type CalculateRefundRefundShipping record {
     string amount?;
+    @jsondata:Name {value: "maximum_refundable"}
     string maximumRefundable?;
     string tax?;
 };
@@ -7923,16 +10678,20 @@
 
 type CalculateRefundRefundTransactions record {
     string amount?;
+    @jsondata:Name {value: "maximum_refundable"}
     string maximumRefundable?;
     string kind?;
+    @jsondata:Name {value: "parent_id"}
     int parentId?;
     string currency?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
     string gateway?;
 };
 
 
 type FulfillmentOrderIdCancelJsonBody record {
+    @jsondata:Name {value: "fulfillment_order"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdcancelJsonFulfillmentOrder fulfillmentOrder?;
 };
 
@@ -7948,16 +10707,24 @@
 
 
 type RejectCancellationRequestResponseFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     FulfillmentOrdersAssignedLocation origin?;
     RejectCancellationRequestResponseFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     RejectCancellationRequestResponseFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "outgoing_requests"}
     anydata[] outgoingRequests?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     string[] supportedActions?;
     string status?;
 };
@@ -7971,21 +10738,29 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
 
 
 type RejectCancellationRequestResponseFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
@@ -7999,20 +10774,24 @@
 
 type RetrieveAListOfTransactionsQueries record {
     # Retrieve only transactions after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show only certain fields, specifed by a comma-separated list of fields names. 
     string fields?;
     # Show amounts in the shop currency.(default: false) 
+    @http:Query {name: "in_shop_currency"}
     string inShopCurrency?;
 };
 
 
 type FulfillmentOrderIdCloseJsonBody record {
+    @jsondata:Name {value: "fulfillment_order"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdcloseJsonFulfillmentOrder fulfillmentOrder?;
 };
 
 
 type PriceRuleIdDiscountCodesJsonBody record {
+    @jsondata:Name {value: "discount_code"}
     AdminapiapiVersionpriceRulespriceRuleIddiscountCodesJsonDiscountCode discountCode?;
 };
 
@@ -8025,14 +10804,19 @@
 
 type RetrieveACountOfCheckoutsQueries record {
     # Count checkouts created after the specified date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Count checkouts created before the specified date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Count checkouts last updated before the specified date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Count checkouts last updated after the specified date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Count checkouts with a given status.(default: open) 
     string status?;
@@ -8040,11 +10824,13 @@
 
 
 type CustomCollectionscustomCollectionIdJsonBody record {
+    @jsondata:Name {value: "custom_collection"}
     AdminapiapiVersioncustomCollectionscustomCollectionIdJsonCustomCollection customCollection?;
 };
 
 
 type CreateFulfillmentEvent record {
+    @jsondata:Name {value: "fulfillment_event"}
     CreateFulfillmentEventFulfillmentEvent fulfillmentEvent?;
 };
 
@@ -8055,16 +10841,24 @@
     anydata? city?;
     anydata? address1?;
     anydata? latitude?;
+    @jsondata:Name {value: "happened_at"}
     string happenedAt?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "estimated_delivery_at"}
     anydata? estimatedDeliveryAt?;
     anydata? message?;
+    @jsondata:Name {value: "fulfillment_id"}
     int fulfillmentId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     anydata? province?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int id?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
     anydata? longitude?;
     string status?;
@@ -8072,6 +10866,7 @@
 
 
 type FulfillmentOrderIdOpenJsonBody record {
+    @jsondata:Name {value: "fulfillment_order"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdholdJsonFulfillmentOrder fulfillmentOrder?;
 };
 
@@ -8088,6 +10883,7 @@
     # The maximum number of results to show.(default: 50)(maximum: 250) 
     string 'limit?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show only certain fields, specified by a comma-separated list of field names. 
     string fields?;
@@ -8108,6 +10904,7 @@
 
 
 type GiftCardsgiftCardIdJsonBody record {
+    @jsondata:Name {value: "gift_card"}
     AdminapiapiVersiongiftCardsgiftCardIdJsonGiftCard giftCard?;
 };
 
@@ -8120,17 +10917,26 @@
 
 type SingleCollectionCollection record {
     SingleCollectionCollectionImage image?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
+    @jsondata:Name {value: "products_count"}
     int productsCount?;
     string 'handle?;
     string title?;
+    @jsondata:Name {value: "collection_type"}
     string collectionType?;
+    @jsondata:Name {value: "published_scope"}
     string publishedScope?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
+    @jsondata:Name {value: "sort_order"}
     string sortOrder?;
 };
 
@@ -8139,12 +10945,14 @@
     string src?;
     string alt?;
     int width?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int height?;
 };
 
 
 type CancellationRequestRejectJsonBody record {
+    @jsondata:Name {value: "cancellation_request"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdcancellationRequestrejectJsonCancellationRequest cancellationRequest?;
 };
 
@@ -8160,15 +10968,19 @@
 type RetrieveAListOfCustomersQueries record {
     # Show customers created after a specified date.  
 (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show customers created before a specified date.  
 (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Show customers last updated before a specified date.  
 (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show customers last updated after a specified date.  
 (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # The maximum number of results to show.(default: 50)(maximum: 250) 
     string 'limit?;
@@ -8177,11 +10989,13 @@
     # Show only certain fields, specified by a comma-separated list of field names. 
     string fields?;
     # Restrict results to those after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
 };
 
 
 type UpdateInventoryItem record {
+    @jsondata:Name {value: "inventory_item"}
     UpdateInventoryItemInventoryItem inventoryItem?;
 };
 
@@ -8191,6 +11005,7 @@
     # The maximum number of results to show.(default: 50)(maximum: 250) 
     string 'limit?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show only certain fields, specified by a comma-separated list of field names. 
     string fields?;
@@ -8198,6 +11013,7 @@
 
 
 type AccountActivationUrl record {
+    @jsondata:Name {value: "account_activation_url"}
     string accountActivationUrl?;
 };
 
@@ -8217,24 +11033,31 @@
 
 type RetrieveAListOfSmartCollectionsQueries record {
     # Show smart collections last updated before this date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show smart collections last updated after this date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Show smart collections that includes the specified product. 
+    @http:Query {name: "product_id"}
     string productId?;
     # Show smart collections published after this date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "published_at_min"}
     string publishedAtMin?;
     # The number of results to show.(default: 50)(maximum: 250) 
     string 'limit?;
     # Show only the smart collections specified by a comma-separated list of IDs. 
     string ids?;
     # Show smart collections published before this date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "published_at_max"}
     string publishedAtMax?;
     # Filter results by smart collection handle. 
     string 'handle?;
     # Filter results based on the published status of smart collections.(default: any) 
+    @http:Query {name: "published_status"}
     string publishedStatus?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # Show smart collections with the specified title. 
     string title?;
@@ -8251,56 +11074,89 @@
 
 
 type CreateMarketingEventMarketingEvent record {
+    @jsondata:Name {value: "manage_url"}
     anydata? manageUrl?;
+    @jsondata:Name {value: "utm_campaign"}
     string utmCampaign?;
+    @jsondata:Name {value: "remote_id"}
     anydata? remoteId?;
+    @jsondata:Name {value: "utm_medium"}
     string utmMedium?;
     anydata? description?;
+    @jsondata:Name {value: "breadcrumb_id"}
     anydata? breadcrumbId?;
+    @jsondata:Name {value: "event_type"}
     string eventType?;
+    @jsondata:Name {value: "preview_url"}
     anydata? previewUrl?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     boolean paid?;
+    @jsondata:Name {value: "marketing_activity_id"}
     int marketingActivityId?;
+    @jsondata:Name {value: "started_at"}
     string startedAt?;
     anydata? currency?;
     int id?;
+    @jsondata:Name {value: "marketing_channel"}
     string marketingChannel?;
+    @jsondata:Name {value: "marketed_resources"}
     anydata[] marketedResources?;
+    @jsondata:Name {value: "scheduled_to_end_at"}
     anydata? scheduledToEndAt?;
+    @jsondata:Name {value: "budget_type"}
     anydata? budgetType?;
+    @jsondata:Name {value: "ended_at"}
     anydata? endedAt?;
     anydata? budget?;
+    @jsondata:Name {value: "referring_domain"}
     string referringDomain?;
+    @jsondata:Name {value: "utm_source"}
     string utmSource?;
 };
 
 
 type ConnectInventoryItemInventoryLevel record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int available?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
 };
 
 
 type CancelFulfillmentFulfillment record {
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "line_items"}
     CancelFulfillmentFulfillmentLineItems[] lineItems?;
+    @jsondata:Name {value: "tracking_company"}
     string trackingCompany?;
+    @jsondata:Name {value: "tracking_urls"}
     string[] trackingUrls?;
+    @jsondata:Name {value: "location_id"}
     int locationId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string 'service?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string name?;
+    @jsondata:Name {value: "tracking_number"}
     string trackingNumber?;
     record {|anydata...;|} receipt?;
     int id?;
+    @jsondata:Name {value: "tracking_numbers"}
     string[] trackingNumbers?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "tracking_url"}
     string trackingUrl?;
+    @jsondata:Name {value: "shipment_status"}
     anydata? shipmentStatus?;
     string status?;
 };
@@ -8340,24 +11196,34 @@
 
 type OrderRisksRisks record {
     string score?;
+    @jsondata:Name {value: "checkout_id"}
     int? checkoutId?;
     boolean display?;
     string recommendation?;
+    @jsondata:Name {value: "cause_cancel"}
     boolean causeCancel?;
+    @jsondata:Name {value: "merchant_message"}
     string merchantMessage?;
     int id?;
     string 'source?;
     string message?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
 };
 
 
 type AdminapiapiVersionpriceRulesJsonPriceRule record {
+    @jsondata:Name {value: "allocation_method"}
     string allocationMethod?;
+    @jsondata:Name {value: "customer_selection"}
     string customerSelection?;
+    @jsondata:Name {value: "starts_at"}
     string startsAt?;
+    @jsondata:Name {value: "value_type"}
     string valueType?;
+    @jsondata:Name {value: "target_type"}
     string targetType?;
+    @jsondata:Name {value: "target_selection"}
     string targetSelection?;
     string title?;
     string value?;
@@ -8365,6 +11231,7 @@
 
 
 type CustomerAddress record {
+    @jsondata:Name {value: "customer_address"}
     CustomerAddressCustomerAddress customerAddress?;
 };
 
@@ -8375,17 +11242,23 @@
     string address2?;
     string city?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     boolean default?;
     string province?;
     string phone?;
+    @jsondata:Name {value: "country_name"}
     string countryName?;
     string name?;
     string company?;
     int id?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
 };
 
@@ -8401,16 +11274,24 @@
 
 
 type FulfillmentOrderFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     FulfillmentOrdersAssignedLocation origin?;
     FulfillmentOrderFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     FulfillmentOrderFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "outgoing_requests"}
     anydata[] outgoingRequests?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     string[] supportedActions?;
     string status?;
 };
@@ -8423,10 +11304,15 @@
 
 type CreateBlogResponseBlog record {
     anydata? feedburner?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "feedburner_location"}
     anydata? feedburnerLocation?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     int id?;
@@ -8437,6 +11323,7 @@
 
 
 type FulfillmentOrderIdMoveJsonBody record {
+    @jsondata:Name {value: "fulfillment_order"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdholdJsonFulfillmentOrder fulfillmentOrder?;
 };
 
@@ -8461,12 +11348,16 @@
 
 type SearchForGiftCardsQueries record {
     # Show gift cards created at or after date
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show gift cards created at or before date
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Show gift cards last updated at or before date
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show gift cards last updated at or after date
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # The text to search for. 
     string query?;
@@ -8480,15 +11371,23 @@
 
 
 type CreateProductVariantVariant record {
+    @jsondata:Name {value: "presentment_prices"}
     CreateProductResponseProductPresentmentPrices[] presentmentPrices?;
+    @jsondata:Name {value: "inventory_management"}
     string inventoryManagement?;
+    @jsondata:Name {value: "old_inventory_quantity"}
     int oldInventoryQuantity?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string title?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     string price?;
+    @jsondata:Name {value: "product_id"}
     int? productId?;
     anydata? option3?;
     string option1?;
@@ -8497,45 +11396,63 @@
     int grams?;
     string? sku?;
     anydata? barcode?;
+    @jsondata:Name {value: "inventory_quantity"}
     int inventoryQuantity?;
+    @jsondata:Name {value: "compare_at_price"}
     anydata? compareAtPrice?;
+    @jsondata:Name {value: "fulfillment_service"}
     string fulfillmentService?;
     boolean taxable?;
     decimal weight?;
+    @jsondata:Name {value: "inventory_policy"}
     string inventoryPolicy?;
+    @jsondata:Name {value: "weight_unit"}
     string weightUnit?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int position?;
+    @jsondata:Name {value: "image_id"}
     int? imageId?;
 };
 
 
 type CustomerDefaultAddress record {
+    @jsondata:Name {value: "customer_address"}
     CustomerDefaultAddressCustomerAddress customerAddress?;
 };
 
 
 type InventoryItemsinventoryItemIdJsonBody record {
+    @jsondata:Name {value: "inventory_item"}
     AdminapiapiVersioninventoryItemsinventoryItemIdJsonInventoryItem inventoryItem?;
 };
 
 
 type DisputeFileUpload record {
+    @jsondata:Name {value: "shop_id"}
     int shopId;
+    @jsondata:Name {value: "original_filename"}
     string originalFilename;
     string filename;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt;
+    @jsondata:Name {value: "file_type"}
     string fileType;
+    @jsondata:Name {value: "created_at"}
     string createdAt;
+    @jsondata:Name {value: "dispute_evidence_id"}
     int disputeEvidenceId;
+    @jsondata:Name {value: "dispute_evidence_type"}
     string disputeEvidenceType;
     int id;
+    @jsondata:Name {value: "file_size"}
     int fileSize;
     string url;
 };
 
 
 type FulfillmentRequestAcceptJsonBody record {
+    @jsondata:Name {value: "fulfillment_request"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdfulfillmentRequestacceptJsonFulfillmentRequest fulfillmentRequest?;
 };
 
@@ -8560,19 +11477,24 @@
 
 type ReturnAListOfAllBalanceTransactionsQueries record {
     # Filter response to transactions paid out in the specified payout. 
+    @http:Query {name: "payout_id"}
     string payoutId?;
     # Filter response to transactions placed in test mode. 
     string test?;
     # Filter response to transactions with the specified payout status 
+    @http:Query {name: "payout_status"}
     string payoutStatus?;
     # Filter response to transactions exclusively before the specified ID 
+    @http:Query {name: "last_id"}
     string lastId?;
     # Filter response to transactions exclusively after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
 };
 
 
 type FulfillmentOrderIdFulfillmentRequestJsonBody record {
+    @jsondata:Name {value: "fulfillment_request"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdfulfillmentRequestJsonFulfillmentRequest fulfillmentRequest?;
 };
 
@@ -8583,21 +11505,25 @@
 
 
 type CollectionListingscollectionListingIdJsonBody record {
+    @jsondata:Name {value: "collection_listing"}
     AdminapiapiVersioncollectionListingscollectionListingIdJsonCollectionListing collectionListing?;
 };
 
 
 type AdminapiapiVersioncollectionListingscollectionListingIdJsonCollectionListing record {
+    @jsondata:Name {value: "collection_id"}
     int collectionId?;
 };
 
 
 type AccountInvite record {
+    @jsondata:Name {value: "customer_invite"}
     AccountInviteCustomerInvite customerInvite?;
 };
 
 
 type AccountInviteCustomerInvite record {
+    @jsondata:Name {value: "custom_message"}
     string customMessage?;
     string[] bcc?;
     string subject?;
@@ -8613,37 +11539,55 @@
 
 
 type TransitionFulfillmentOrder record {
+    @jsondata:Name {value: "fulfillment_order"}
     TransitionFulfillmentOrderFulfillmentOrder fulfillmentOrder?;
 };
 
 
 type TransitionFulfillmentOrderFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     TransitionFulfillmentOrderFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     TransitionFulfillmentOrderFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     string[] supportedActions?;
+    @jsondata:Name {value: "assigned_location"}
     FulfillmentOrdersAssignedLocation assignedLocation?;
+    @jsondata:Name {value: "merchant_requests"}
     anydata[] merchantRequests?;
     string status?;
 };
 
 
 type CancellationResponseFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     FulfillmentOrdersAssignedLocation origin?;
     CancellationResponseFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     CancellationResponseFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "outgoing_requests"}
     anydata[] outgoingRequests?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     string[] supportedActions?;
     string status?;
 };
@@ -8660,8 +11604,11 @@
 
 
 type PaymentsResponsePayments record {
+    @jsondata:Name {value: "unique_token"}
     string uniqueToken?;
+    @jsondata:Name {value: "credit_card"}
     anydata? creditCard?;
+    @jsondata:Name {value: "payment_processing_error_message"}
     anydata? paymentProcessingErrorMessage?;
     int id?;
     PaymentsResponseCheckout checkout?;
@@ -8676,29 +11623,48 @@
 
 type DraftOrdersDraftOrders record {
     string? note?;
+    @jsondata:Name {value: "applied_discount"}
     record {|anydata...;|}? appliedDiscount?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "billing_address"}
     ReopenCloseOrderOrderBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     DraftOrdersLineItems[] lineItems?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "shipping_address"}
     ReopenCloseOrderOrderBillingAddress|() shippingAddress?;
     string email?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "invoice_sent_at"}
     string? invoiceSentAt?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
     string tags?;
+    @jsondata:Name {value: "completed_at"}
     string? completedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "note_attributes"}
     anydata[] noteAttributes?;
     string name?;
+    @jsondata:Name {value: "shipping_line"}
     record {|anydata...;|}? shippingLine?;
+    @jsondata:Name {value: "order_id"}
     int? orderId?;
+    @jsondata:Name {value: "invoice_url"}
     string invoiceUrl?;
     DraftOrdersCustomer|() customer?;
     string status?;
@@ -8706,28 +11672,45 @@
 
 
 type DraftOrdersCustomer record {
+    @jsondata:Name {value: "total_spent"}
     string totalSpent?;
     anydata? note?;
+    @jsondata:Name {value: "last_order_name"}
     string lastOrderName?;
+    @jsondata:Name {value: "last_order_id"}
     int lastOrderId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "multipass_identifier"}
     anydata? multipassIdentifier?;
+    @jsondata:Name {value: "verified_email"}
     boolean verifiedEmail?;
+    @jsondata:Name {value: "accepts_marketing_updated_at"}
     string acceptsMarketingUpdatedAt?;
     string tags?;
+    @jsondata:Name {value: "orders_count"}
     int ordersCount?;
+    @jsondata:Name {value: "default_address"}
     ReopenCloseOrderOrderCustomerDefaultAddress defaultAddress?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "accepts_marketing"}
     boolean acceptsMarketing?;
     anydata? phone?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "tax_exemptions"}
     anydata[] taxExemptions?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "marketing_opt_in_level"}
     anydata? marketingOptInLevel?;
     string state?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
@@ -8743,6 +11726,7 @@
 
 
 type CustomerInvite record {
+    @jsondata:Name {value: "customer_invite"}
     CustomerInviteCustomerInvite customerInvite;
 };
 
@@ -8753,6 +11737,7 @@
 
 
 type SingleFulfillmentService record {
+    @jsondata:Name {value: "fulfillment_service"}
     SingleFulfillmentServiceFulfillmentService fulfillmentService?;
 };
 
@@ -8765,32 +11750,50 @@
 
 
 type UpdateMarketingEvent record {
+    @jsondata:Name {value: "marketing_event"}
     UpdateMarketingEventMarketingEvent marketingEvent?;
 };
 
 
 type UpdateMarketingEventMarketingEvent record {
+    @jsondata:Name {value: "manage_url"}
     anydata? manageUrl?;
+    @jsondata:Name {value: "utm_campaign"}
     string utmCampaign?;
+    @jsondata:Name {value: "remote_id"}
     string remoteId?;
+    @jsondata:Name {value: "utm_medium"}
     string utmMedium?;
     anydata? description?;
+    @jsondata:Name {value: "breadcrumb_id"}
     anydata? breadcrumbId?;
+    @jsondata:Name {value: "event_type"}
     string eventType?;
+    @jsondata:Name {value: "preview_url"}
     anydata? previewUrl?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     boolean paid?;
+    @jsondata:Name {value: "marketing_activity_id"}
     anydata? marketingActivityId?;
+    @jsondata:Name {value: "started_at"}
     string startedAt?;
     string currency?;
     int id?;
+    @jsondata:Name {value: "marketing_channel"}
     string marketingChannel?;
+    @jsondata:Name {value: "marketed_resources"}
     anydata[] marketedResources?;
+    @jsondata:Name {value: "scheduled_to_end_at"}
     string scheduledToEndAt?;
+    @jsondata:Name {value: "budget_type"}
     string budgetType?;
+    @jsondata:Name {value: "ended_at"}
     string endedAt?;
     string budget?;
+    @jsondata:Name {value: "referring_domain"}
     string referringDomain?;
+    @jsondata:Name {value: "utm_source"}
     string utmSource?;
 };
 
@@ -8812,71 +11815,111 @@
 
 type UpdateOrderRiskRisk record {
     string score?;
+    @jsondata:Name {value: "checkout_id"}
     anydata? checkoutId?;
     boolean display?;
     string recommendation?;
+    @jsondata:Name {value: "cause_cancel"}
     boolean causeCancel?;
+    @jsondata:Name {value: "merchant_message"}
     string merchantMessage?;
     int id?;
     string 'source?;
     string message?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
 };
 
 
 type MobilePlatformApplicationsmobilePlatformApplicationIdJsonBody record {
+    @jsondata:Name {value: "mobile_platform_application"}
     AdminapiapiVersionmobilePlatformApplicationsmobilePlatformApplicationIdJsonMobilePlatformApplication mobilePlatformApplication?;
 };
 
 
 type AdminapiapiVersionmobilePlatformApplicationsmobilePlatformApplicationIdJsonMobilePlatformApplication record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "sha256_cert_fingerprints"}
     string[] sha256CertFingerprints?;
+    @jsondata:Name {value: "enabled_app_clips"}
     boolean enabledAppClips?;
+    @jsondata:Name {value: "enabled_universal_or_app_links"}
     boolean enabledUniversalOrAppLinks?;
     int id?;
+    @jsondata:Name {value: "app_clip_application_id"}
     anydata? appClipApplicationId?;
+    @jsondata:Name {value: "enabled_shared_webcredentials"}
     boolean enabledSharedWebcredentials?;
+    @jsondata:Name {value: "application_id"}
     string applicationId?;
     string platform?;
 };
 
 
 type UpdatePriceRule record {
+    @jsondata:Name {value: "price_rule"}
     UpdatePriceRulePriceRule priceRule?;
 };
 
 
 type UpdatePriceRulePriceRule record {
+    @jsondata:Name {value: "once_per_customer"}
     boolean oncePerCustomer?;
+    @jsondata:Name {value: "starts_at"}
     string startsAt?;
+    @jsondata:Name {value: "usage_limit"}
     anydata? usageLimit?;
+    @jsondata:Name {value: "value_type"}
     string valueType?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "prerequisite_customer_ids"}
     anydata[] prerequisiteCustomerIds?;
     string title?;
+    @jsondata:Name {value: "entitled_collection_ids"}
     anydata[] entitledCollectionIds?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "prerequisite_product_ids"}
     anydata[] prerequisiteProductIds?;
+    @jsondata:Name {value: "prerequisite_shipping_price_range"}
     anydata? prerequisiteShippingPriceRange?;
+    @jsondata:Name {value: "entitled_country_ids"}
     anydata[] entitledCountryIds?;
+    @jsondata:Name {value: "entitled_variant_ids"}
     anydata[] entitledVariantIds?;
+    @jsondata:Name {value: "ends_at"}
     string? endsAt?;
     int id?;
     string value?;
+    @jsondata:Name {value: "prerequisite_subtotal_range"}
     anydata? prerequisiteSubtotalRange?;
+    @jsondata:Name {value: "allocation_method"}
     string allocationMethod?;
+    @jsondata:Name {value: "prerequisite_to_entitlement_quantity_ratio"}
     UpdatePriceRulePriceRulePrerequisiteToEntitlementQuantityRatio prerequisiteToEntitlementQuantityRatio?;
+    @jsondata:Name {value: "prerequisite_quantity_range"}
     anydata? prerequisiteQuantityRange?;
+    @jsondata:Name {value: "allocation_limit"}
     anydata? allocationLimit?;
+    @jsondata:Name {value: "target_type"}
     string targetType?;
+    @jsondata:Name {value: "entitled_product_ids"}
     anydata[] entitledProductIds?;
+    @jsondata:Name {value: "customer_selection"}
     string customerSelection?;
+    @jsondata:Name {value: "prerequisite_saved_search_ids"}
     anydata[] prerequisiteSavedSearchIds?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "prerequisite_variant_ids"}
     anydata[] prerequisiteVariantIds?;
+    @jsondata:Name {value: "target_selection"}
     string targetSelection?;
+    @jsondata:Name {value: "prerequisite_collection_ids"}
     anydata[] prerequisiteCollectionIds?;
 };
 
@@ -8906,6 +11949,7 @@
 
 
 type FulfillmentOrderIdHoldJsonBody record {
+    @jsondata:Name {value: "fulfillment_order"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdholdJsonFulfillmentOrder fulfillmentOrder?;
 };
 
@@ -8929,10 +11973,14 @@
 
 type SingleThemeTheme record {
     string role?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "theme_store_id"}
     anydata? themeStoreId?;
     string name?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     boolean processing?;
     int id?;
@@ -8941,19 +11989,28 @@
 
 
 type DiscountCodes record {
+    @jsondata:Name {value: "discount_codes"}
     DiscountCodesDiscountCodes[] discountCodes?;
 };
 
 
 type MobilePlatformApplicationMobilePlatformApplication record {
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "sha256_cert_fingerprints"}
     string[] sha256CertFingerprints?;
+    @jsondata:Name {value: "enabled_app_clips"}
     boolean enabledAppClips?;
+    @jsondata:Name {value: "enabled_universal_or_app_links"}
     boolean enabledUniversalOrAppLinks?;
     int id?;
+    @jsondata:Name {value: "app_clip_application_id"}
     anydata? appClipApplicationId?;
+    @jsondata:Name {value: "enabled_shared_webcredentials"}
     boolean enabledSharedWebcredentials?;
+    @jsondata:Name {value: "application_id"}
     string applicationId?;
     string platform?;
 };
@@ -8978,6 +12035,7 @@
 
 
 type SingleCustomerAddress record {
+    @jsondata:Name {value: "customer_address"}
     ReopenCloseOrderOrderCustomerDefaultAddress customerAddress?;
 };
 
@@ -8997,10 +12055,15 @@
 
 type BlogsBlogs record {
     anydata? feedburner?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "feedburner_location"}
     anydata? feedburnerLocation?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     int id?;
@@ -9013,23 +12076,29 @@
 
 type RetrieveFulfillmentsAssociatedWithAnOrderQueries record {
     # Show fulfillments created after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show fulfillments created before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Show fulfillments last updated before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show fulfillments last updated after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Limit the amount of results.(default: 50)(maximum: 250) 
     string 'limit?;
     # A comma-separated list of fields to include in the response. 
     string fields?;
     # Restrict results to after the specified ID. 
+    @http:Query {name: "since_id"}
     string sinceId?;
 };
 
 
 type SingleGiftCard record {
+    @jsondata:Name {value: "gift_card"}
     SingleGiftCardGiftCard giftCard?;
 };
 
@@ -9041,6 +12110,7 @@
     # Show only certain fields, specified by a comma-separated list of field names. 
     string fields?;
     # Show amounts in the shop currency for the underlying transaction.(default: false) 
+    @http:Query {name: "in_shop_currency"}
     string inShopCurrency?;
 };
 
@@ -9052,14 +12122,19 @@
 
 type SubscribeOrderCreationWebhook record {
     string address?;
+    @jsondata:Name {value: "metafield_namespaces"}
     anydata[] metafieldNamespaces?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string format?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string topic?;
     int id?;
+    @jsondata:Name {value: "api_version"}
     string apiVersion?;
     anydata[] fields?;
+    @jsondata:Name {value: "private_metafield_namespaces"}
     anydata[] privateMetafieldNamespaces?;
 };
 
@@ -9077,6 +12152,7 @@
 
 
 type AdminapiapiVersioncheckoutstokenJsonCheckout record {
+    @jsondata:Name {value: "shipping_address"}
     AdminapiapiVersioncheckoutstokenJsonCheckoutShippingAddress shippingAddress?;
     string token?;
 };
@@ -9084,17 +12160,22 @@
 
 type AdminapiapiVersioncheckoutstokenJsonCheckoutShippingAddress record {
     string zip?;
+    @jsondata:Name {value: "country_code"}
     string countryCode?;
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
+    @jsondata:Name {value: "province_code"}
     string provinceCode?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
 };
 
 
 type FulfillmentEventResponse record {
+    @jsondata:Name {value: "fulfillment_event"}
     FulfillmentEventResponseFulfillmentEvent fulfillmentEvent?;
 };
 
@@ -9112,6 +12193,7 @@
 
 
 type UsageChargeResponse record {
+    @jsondata:Name {value: "usage_charge"}
     UsageChargeResponseUsageCharge usageCharge?;
 };
 
@@ -9123,6 +12205,7 @@
     # Filter by blog handle 
     string 'handle?;
     # Restrict results to after the specified ID 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # comma-separated list of fields to include in the response 
     string fields?;
@@ -9130,60 +12213,107 @@
 
 
 type CheckoutResponseCheckout record {
+    @jsondata:Name {value: "privacy_policy_url"}
     anydata? privacyPolicyUrl?;
+    @jsondata:Name {value: "payment_url"}
     string paymentUrl?;
+    @jsondata:Name {value: "refund_policy_url"}
     anydata? refundPolicyUrl?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "terms_of_sale_url"}
     anydata? termsOfSaleUrl?;
+    @jsondata:Name {value: "billing_address"}
     SinglePaymentResponsePaymentCheckoutBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     SinglePaymentResponsePaymentCheckoutLineItems[] lineItems?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "reservation_time_left"}
     int reservationTimeLeft?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "payment_due"}
     string paymentDue?;
+    @jsondata:Name {value: "source_identifier"}
     anydata? sourceIdentifier?;
+    @jsondata:Name {value: "tax_lines"}
     SinglePaymentResponsePaymentCheckoutTaxLines[] taxLines?;
+    @jsondata:Name {value: "customer_locale"}
     anydata? customerLocale?;
+    @jsondata:Name {value: "tax_manipulations"}
     anydata[] taxManipulations?;
     anydata? 'order?;
+    @jsondata:Name {value: "terms_of_service_url"}
     anydata? termsOfServiceUrl?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "subscription_policy_url"}
     anydata? subscriptionPolicyUrl?;
+    @jsondata:Name {value: "order_status_url"}
     anydata? orderStatusUrl?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "discount_code"}
     anydata? discountCode?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
+    @jsondata:Name {value: "completed_at"}
     anydata? completedAt?;
+    @jsondata:Name {value: "shipping_rate"}
     CheckoutResponseCheckoutShippingRate shippingRate?;
     anydata? phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     SinglePaymentResponsePaymentCheckoutNoteAttributes noteAttributes?;
     string name?;
+    @jsondata:Name {value: "shipping_line"}
     CheckoutResponseCheckoutShippingLine|() shippingLine?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
     string? note?;
+    @jsondata:Name {value: "applied_discount"}
     anydata? appliedDiscount?;
     anydata[] payments?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "shopify_payments_account_id"}
     anydata? shopifyPaymentsAccountId?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string currency?;
+    @jsondata:Name {value: "shipping_address"}
     SinglePaymentResponsePaymentCheckoutBillingAddress|() shippingAddress?;
     string email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "legal_notice_url"}
     anydata? legalNoticeUrl?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
+    @jsondata:Name {value: "reservation_time"}
     anydata? reservationTime?;
+    @jsondata:Name {value: "total_tip_received"}
     string totalTipReceived?;
     string token?;
+    @jsondata:Name {value: "credit_card"}
     record {|anydata...;|}? creditCard?;
+    @jsondata:Name {value: "gift_cards"}
     anydata[] giftCards?;
+    @jsondata:Name {value: "web_url"}
     string webUrl?;
+    @jsondata:Name {value: "shipping_policy_url"}
     anydata? shippingPolicyUrl?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
 };
 
@@ -9196,16 +12326,21 @@
 
 
 type UpdateDiscountCodeDiscountCode record {
+    @jsondata:Name {value: "usage_count"}
     int usageCount?;
     string code?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "price_rule_id"}
     int priceRuleId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int id?;
 };
 
 
 type FulfillmentOrdersSetFulfillmentOrdersDeadlineJsonBody record {
+    @jsondata:Name {value: "fulfillment_order"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdholdJsonFulfillmentOrder fulfillmentOrder?;
 };
 
@@ -9213,14 +12348,18 @@
 
 type RetrieveAListOfWebhooksQueries record {
     # Retrieve webhook subscriptions that were created after a given date and time (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Retrieve webhook subscriptions that were created before a given date and time (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Retrieve webhooks that were updated after a given date and time (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Retrieve webhook subscriptions that send the POST request to this URI. 
     string address?;
     # Retrieve webhooks that were updated before a given date and time (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Maximum number of webhook subscriptions that should be returned. Setting this parameter outside the maximum range will return an error.(default: 50)(maximum: 250) 
     string 'limit?;
@@ -9229,6 +12368,7 @@
     # Comma-separated list of the properties you want returned for each item in the result list. Use this parameter to restrict the returned list of items to only those properties you specify. 
     string fields?;
     # Restrict the returned list to webhook subscriptions whose id is greater than the specified since\_id. 
+    @http:Query {name: "since_id"}
     string sinceId?;
 };
 
@@ -9241,14 +12381,19 @@
 
 type ShopRetrieveAListOfMetafieldsFromTheResourceSEndpointQueries record {
     # Show metafields created after date (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show metafields created before date (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Show metafields last updated before date (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Filter by the resource ID on which the metafield is attached to
+    @http:Query {name: "metafield[owner_id]"}
     string metafieldOwnerId?;
     # Show metafields last updated after date (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Amount of results(default: 50)(maximum: 250) 
     string 'limit?;
@@ -9257,12 +12402,14 @@
     # comma-separated list of fields to include in the response 
     string fields?;
     # Restrict results to after the specified ID 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # The type of data that the metafield stores in the `value` field. Refer to the list of supported types
     string 'type?;
     # Show metafields with given key 
     string 'key?;
     # Filter by the resource name on which the metafield is attached to
+    @http:Query {name: "metafield[owner_resource]"}
     string metafieldOwnerResource?;
 };
 
@@ -9273,25 +12420,31 @@
 
 
 type DisputeIdDisputeEvidencesJsonBody record {
+    @jsondata:Name {value: "dispute_evidence"}
     AdminapiapiVersionshopifyPaymentsdisputesdisputeIddisputeEvidencesJsonDisputeEvidence disputeEvidence?;
 };
 
 
 type DiscountCodesdiscountCodeIdJsonBody record {
+    @jsondata:Name {value: "discount_code"}
     AdminapiapiVersionpriceRulespriceRuleIddiscountCodesdiscountCodeIdJsonDiscountCode discountCode?;
 };
 
 
 type AdminapiapiVersionpriceRulespriceRuleIddiscountCodesdiscountCodeIdJsonDiscountCode record {
+    @jsondata:Name {value: "usage_count"}
     int usageCount?;
     string code?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     int id?;
 };
 
 
 type ProductListings record {
+    @jsondata:Name {value: "product_listings"}
     ProductListingsProductListings[] productListings?;
 };
 
@@ -9302,6 +12455,7 @@
 
 
 type RejectCancellationRequestResponse record {
+    @jsondata:Name {value: "fulfillment_order"}
     RejectCancellationRequestResponseFulfillmentOrder fulfillmentOrder?;
 };
 
@@ -9319,15 +12473,22 @@
 
 
 type SinglePageResponsePage record {
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string author?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
     string title?;
 };
@@ -9335,26 +12496,35 @@
 
 type SingleProductProduct record {
     ProductsResponseImages image?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     ProductsResponseImages[] images?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     SingleProductProductVariants[] variants?;
     string title?;
     string tags?;
+    @jsondata:Name {value: "published_scope"}
     string publishedScope?;
+    @jsondata:Name {value: "product_type"}
     string productType?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string vendor?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     ProductListingsOptions[] options?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
 };
 
 
 type SingleDiscountCode record {
+    @jsondata:Name {value: "discount_code"}
     DiscountCodesDiscountCodes discountCode?;
 };
 
@@ -9366,14 +12536,19 @@
 
 type SingleWebhookWebhook record {
     string address?;
+    @jsondata:Name {value: "metafield_namespaces"}
     anydata[] metafieldNamespaces?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string format?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string topic?;
     int id?;
+    @jsondata:Name {value: "api_version"}
     string apiVersion?;
     anydata[] fields?;
+    @jsondata:Name {value: "private_metafield_namespaces"}
     anydata[] privateMetafieldNamespaces?;
 };
 
@@ -9404,23 +12579,41 @@
 
 
 type EngagementsEngagements record {
+    @jsondata:Name {value: "is_cumulative"}
     boolean isCumulative?;
+    @jsondata:Name {value: "utc_offset"}
     anydata? utcOffset?;
+    @jsondata:Name {value: "ad_spend"}
     string? adSpend?;
+    @jsondata:Name {value: "occurred_on"}
     string occurredOn?;
+    @jsondata:Name {value: "favorites_count"}
     int? favoritesCount?;
+    @jsondata:Name {value: "unique_views_count"}
     anydata? uniqueViewsCount?;
+    @jsondata:Name {value: "clicks_count"}
     int clicksCount?;
+    @jsondata:Name {value: "unsubscribes_count"}
     anydata? unsubscribesCount?;
+    @jsondata:Name {value: "currency_code"}
     anydata? currencyCode?;
+    @jsondata:Name {value: "shares_count"}
     anydata? sharesCount?;
+    @jsondata:Name {value: "fetched_at"}
     anydata? fetchedAt?;
+    @jsondata:Name {value: "comments_count"}
     anydata? commentsCount?;
+    @jsondata:Name {value: "fails_count"}
     anydata? failsCount?;
+    @jsondata:Name {value: "impressions_count"}
     anydata? impressionsCount?;
+    @jsondata:Name {value: "sends_count"}
     anydata? sendsCount?;
+    @jsondata:Name {value: "views_count"}
     int viewsCount?;
+    @jsondata:Name {value: "complaints_count"}
     anydata? complaintsCount?;
+    @jsondata:Name {value: "unique_clicks_count"}
     anydata? uniqueClicksCount?;
 };
 
@@ -9431,98 +12624,165 @@
 
 
 type DisputeEvidenceResponse record {
+    @jsondata:Name {value: "dispute_evidence"}
     DisputeEvidence disputeEvidence?;
 };
 
 
 type DisputeEvidence record {
+    @jsondata:Name {value: "refund_refusal_explanation"}
     string? refundRefusalExplanation?;
+    @jsondata:Name {value: "customer_first_name"}
     string customerFirstName?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "dispute_evidence_files"}
     DisputeEvidenceFiles disputeEvidenceFiles?;
+    @jsondata:Name {value: "billing_address"}
     Address billingAddress?;
+    @jsondata:Name {value: "refund_policy_disclosure"}
     string? refundPolicyDisclosure?;
+    @jsondata:Name {value: "access_activity_log"}
     string? accessActivityLog?;
+    @jsondata:Name {value: "uncategorized_text"}
     string uncategorizedText?;
     Fulfillment[] fulfillments?;
+    @jsondata:Name {value: "payments_dispute_id"}
     int paymentsDisputeId?;
+    @jsondata:Name {value: "customer_last_name"}
     string customerLastName?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "cancellation_policy_disclosure"}
     string? cancellationPolicyDisclosure?;
+    @jsondata:Name {value: "cancellation_rebuttal"}
     string? cancellationRebuttal?;
+    @jsondata:Name {value: "submitted_by_merchant_on"}
     string submittedByMerchantOn?;
     int id?;
+    @jsondata:Name {value: "shipping_address"}
     Address shippingAddress?;
+    @jsondata:Name {value: "product_description"}
     string productDescription?;
+    @jsondata:Name {value: "customer_email_address"}
     string customerEmailAddress?;
 };
 
 
 type CreateCollection record {
+    @jsondata:Name {value: "custom_collection"}
     CreateCollectionCustomCollection customCollection?;
 };
 
 
 type ShippingRateResponseCheckout record {
+    @jsondata:Name {value: "privacy_policy_url"}
     anydata? privacyPolicyUrl?;
+    @jsondata:Name {value: "payment_url"}
     string paymentUrl?;
+    @jsondata:Name {value: "refund_policy_url"}
     anydata? refundPolicyUrl?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "terms_of_sale_url"}
     anydata? termsOfSaleUrl?;
+    @jsondata:Name {value: "billing_address"}
     SinglePaymentResponsePaymentCheckoutBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     SinglePaymentResponsePaymentCheckoutLineItems[] lineItems?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "reservation_time_left"}
     int reservationTimeLeft?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "payment_due"}
     string paymentDue?;
+    @jsondata:Name {value: "source_identifier"}
     anydata? sourceIdentifier?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
+    @jsondata:Name {value: "customer_locale"}
     anydata? customerLocale?;
+    @jsondata:Name {value: "tax_manipulations"}
     anydata[] taxManipulations?;
     anydata? 'order?;
+    @jsondata:Name {value: "terms_of_service_url"}
     anydata? termsOfServiceUrl?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "subscription_policy_url"}
     anydata? subscriptionPolicyUrl?;
+    @jsondata:Name {value: "order_status_url"}
     anydata? orderStatusUrl?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "discount_code"}
     anydata? discountCode?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
+    @jsondata:Name {value: "completed_at"}
     anydata? completedAt?;
+    @jsondata:Name {value: "shipping_rate"}
     SinglePaymentResponsePaymentCheckoutShippingRate shippingRate?;
     anydata? phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     SinglePaymentResponsePaymentCheckoutNoteAttributes noteAttributes?;
     string name?;
+    @jsondata:Name {value: "shipping_line"}
     SinglePaymentResponsePaymentCheckoutShippingLine|() shippingLine?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
     string? note?;
+    @jsondata:Name {value: "applied_discount"}
     anydata? appliedDiscount?;
     anydata[] payments?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "shopify_payments_account_id"}
     anydata? shopifyPaymentsAccountId?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string currency?;
+    @jsondata:Name {value: "shipping_address"}
     SinglePaymentResponsePaymentCheckoutBillingAddress|() shippingAddress?;
     string email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "legal_notice_url"}
     anydata? legalNoticeUrl?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
+    @jsondata:Name {value: "reservation_time"}
     anydata? reservationTime?;
+    @jsondata:Name {value: "total_tip_received"}
     string totalTipReceived?;
     string token?;
+    @jsondata:Name {value: "credit_card"}
     anydata? creditCard?;
+    @jsondata:Name {value: "gift_cards"}
     anydata[] giftCards?;
+    @jsondata:Name {value: "web_url"}
     string webUrl?;
+    @jsondata:Name {value: "shipping_policy_url"}
     anydata? shippingPolicyUrl?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
 };
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # The HTTP version understood by the client
     http:HttpVersion httpVersion?; // Special Agent Note: HttpVersion FROM ballerina/http package
@@ -9566,18 +12826,24 @@
 
 type UpdateProvinceResponseProvince record {
     string code?;
+    @jsondata:Name {value: "tax_type"}
     string taxType?;
+    @jsondata:Name {value: "tax_name"}
     string taxName?;
     string name?;
+    @jsondata:Name {value: "tax_percentage"}
     decimal taxPercentage?;
     decimal tax?;
     int id?;
+    @jsondata:Name {value: "shipping_zone_id"}
     anydata? shippingZoneId?;
+    @jsondata:Name {value: "country_id"}
     int countryId?;
 };
 
 
 type SingleCarrierService record {
+    @jsondata:Name {value: "carrier_service"}
     SingleCarrierServiceCarrierService carrierService?;
 };
 
@@ -9589,14 +12855,19 @@
 
 type UpdateWebhookWebhook record {
     string address?;
+    @jsondata:Name {value: "metafield_namespaces"}
     anydata[] metafieldNamespaces?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string format?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string topic?;
     int id?;
+    @jsondata:Name {value: "api_version"}
     string apiVersion?;
     anydata[] fields?;
+    @jsondata:Name {value: "private_metafield_namespaces"}
     anydata[] privateMetafieldNamespaces?;
 };
 
@@ -9607,11 +12878,13 @@
 
 
 type MarketingEvent record {
+    @jsondata:Name {value: "marketing_event"}
     MarketingEventMarketingEvent marketingEvent?;
 };
 
 
 type DraftOrdersdraftOrderIdJsonBody record {
+    @jsondata:Name {value: "draft_order"}
     AdminapiapiVersiondraftOrdersdraftOrderIdJsonDraftOrder draftOrder?;
 };
 
@@ -9635,6 +12908,7 @@
 
 
 type CancellationResponse record {
+    @jsondata:Name {value: "fulfillment_order"}
     CancellationResponseFulfillmentOrder fulfillmentOrder?;
 };
 
@@ -9645,6 +12919,7 @@
 
 
 type ProductIdAppResponse record {
+    @jsondata:Name {value: "product_ids"}
     decimal[] productIds?;
 };
 
@@ -9655,16 +12930,21 @@
 
 
 type AdminapiapiVersionfulfillmentServicesJsonFulfillmentService record {
+    @jsondata:Name {value: "callback_url"}
     string callbackUrl?;
+    @jsondata:Name {value: "inventory_management"}
     boolean inventoryManagement?;
+    @jsondata:Name {value: "requires_shipping_method"}
     boolean requiresShippingMethod?;
     string format?;
     string name?;
+    @jsondata:Name {value: "tracking_support"}
     boolean trackingSupport?;
 };
 
 
 type GiftCardIdDisableJsonBody record {
+    @jsondata:Name {value: "gift_card"}
     AdminapiapiVersiongiftCardsgiftCardIddisableJsonGiftCard giftCard?;
 };
 
@@ -9680,74 +12960,129 @@
 
 
 type SingleOrderResponseOrder record {
+    @jsondata:Name {value: "cancelled_at"}
     anydata? cancelledAt?;
+    @jsondata:Name {value: "fulfillment_status"}
     anydata? fulfillmentStatus?;
+    @jsondata:Name {value: "total_price_usd"}
     string totalPriceUsd?;
+    @jsondata:Name {value: "billing_address"}
     ReopenCloseOrderOrderBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     ReopenCloseOrderOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "total_discounts_set"}
     ReopenCloseOrderOrderTotalDiscountsSet totalDiscountsSet?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "landing_site"}
     string landingSite?;
+    @jsondata:Name {value: "source_identifier"}
     string sourceIdentifier?;
     string reference?;
     int number?;
+    @jsondata:Name {value: "checkout_id"}
     int checkoutId?;
+    @jsondata:Name {value: "checkout_token"}
     string checkoutToken?;
+    @jsondata:Name {value: "tax_lines"}
     ReopenCloseOrderOrderTaxLines1[] taxLines?;
+    @jsondata:Name {value: "customer_locale"}
     anydata? customerLocale?;
     int id?;
+    @jsondata:Name {value: "app_id"}
     anydata? appId?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "closed_at"}
     anydata? closedAt?;
+    @jsondata:Name {value: "order_status_url"}
     string orderStatusUrl?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
     boolean test?;
+    @jsondata:Name {value: "total_shipping_price_set"}
     ReopenCloseOrderOrderTotalDiscountSet totalShippingPriceSet?;
+    @jsondata:Name {value: "subtotal_price_set"}
     ReopenCloseOrderOrderSubtotalPriceSet subtotalPriceSet?;
+    @jsondata:Name {value: "payment_gateway_names"}
     string[] paymentGatewayNames?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
     string tags?;
+    @jsondata:Name {value: "processing_method"}
     string processingMethod?;
+    @jsondata:Name {value: "shipping_lines"}
     ReopenCloseOrderOrderShippingLines[] shippingLines?;
     string phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     ReopenCloseOrderOrderNoteAttributes[] noteAttributes?;
     string name?;
+    @jsondata:Name {value: "cart_token"}
     string cartToken?;
+    @jsondata:Name {value: "total_tax_set"}
     ReopenCloseOrderOrderPriceSet2 totalTaxSet?;
+    @jsondata:Name {value: "landing_site_ref"}
     string landingSiteRef?;
+    @jsondata:Name {value: "discount_codes"}
     ReopenCloseOrderOrderDiscountCodes[] discountCodes?;
     anydata? note?;
+    @jsondata:Name {value: "payment_details"}
     ReopenCloseOrderOrderPaymentDetails paymentDetails?;
+    @jsondata:Name {value: "order_number"}
     int orderNumber?;
+    @jsondata:Name {value: "discount_applications"}
     ReopenCloseOrderOrderDiscountApplications[] discountApplications?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "total_line_items_price_set"}
     ReopenCloseOrderOrderSubtotalPriceSet totalLineItemsPriceSet?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "buyer_accepts_marketing"}
     boolean buyerAcceptsMarketing?;
     boolean confirmed?;
+    @jsondata:Name {value: "total_weight"}
     int totalWeight?;
+    @jsondata:Name {value: "contact_email"}
     string contactEmail?;
     ReopenCloseOrderOrderRefunds[] refunds?;
+    @jsondata:Name {value: "total_discounts"}
     string totalDiscounts?;
     ReopenCloseOrderOrderFulfillments[] fulfillments?;
+    @jsondata:Name {value: "client_details"}
     ReopenCloseOrderOrderClientDetails clientDetails?;
+    @jsondata:Name {value: "referring_site"}
     string referringSite?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "processed_at"}
     string processedAt?;
     string currency?;
+    @jsondata:Name {value: "shipping_address"}
     ReopenCloseOrderOrderBillingAddress|() shippingAddress?;
+    @jsondata:Name {value: "browser_ip"}
     string browserIp?;
     string email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "total_price_set"}
     ReopenCloseOrderOrderTotalPriceSet totalPriceSet?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
     string token?;
+    @jsondata:Name {value: "cancel_reason"}
     anydata? cancelReason?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
+    @jsondata:Name {value: "financial_status"}
     string financialStatus?;
     string gateway?;
     ReopenCloseOrderOrderCustomer customer?;
@@ -9770,16 +13105,25 @@
 
 
 type MoveFulfillmentOrderResponseOriginalFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     MoveFulfillmentOrderResponseOriginalFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     MoveFulfillmentOrderResponseOriginalFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     anydata[] supportedActions?;
+    @jsondata:Name {value: "assigned_location"}
     FulfillmentOrdersAssignedLocation assignedLocation?;
+    @jsondata:Name {value: "merchant_requests"}
     anydata[] merchantRequests?;
     string status?;
 };
@@ -9793,21 +13137,29 @@
     string city?;
     string phone?;
     string address1?;
+    @jsondata:Name {value: "last_name"}
     string lastName?;
     anydata? company?;
     int id?;
+    @jsondata:Name {value: "first_name"}
     string firstName?;
     string email?;
 };
 
 
 type MoveFulfillmentOrderResponseOriginalFulfillmentOrderLineItems record {
+    @jsondata:Name {value: "fulfillment_order_id"}
     int fulfillmentOrderId?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
+    @jsondata:Name {value: "fulfillable_quantity"}
     int fulfillableQuantity?;
+    @jsondata:Name {value: "line_item_id"}
     int lineItemId?;
     int quantity?;
+    @jsondata:Name {value: "variant_id"}
     int? variantId?;
+    @jsondata:Name {value: "inventory_item_id"}
     int inventoryItemId?;
     int id?;
 };
@@ -9820,33 +13172,41 @@
 
 
 type MoveFulfillmentOrderResponse record {
+    @jsondata:Name {value: "original_fulfillment_order"}
     MoveFulfillmentOrderResponseOriginalFulfillmentOrder originalFulfillmentOrder?;
+    @jsondata:Name {value: "remaining_fulfillment_order"}
     anydata? remainingFulfillmentOrder?;
+    @jsondata:Name {value: "moved_fulfillment_order"}
     MoveFulfillmentOrderResponseMovedFulfillmentOrder movedFulfillmentOrder?;
 };
 
 
 type InventoryLevel record {
+    @jsondata:Name {value: "inventory_level"}
     InventoryLevelInventoryLevel inventoryLevel?;
 };
 
 
 type PriceRulespriceRuleIdJsonBody record {
+    @jsondata:Name {value: "price_rule"}
     AdminapiapiVersionpriceRulespriceRuleIdJsonPriceRule priceRule?;
 };
 
 
 type CarrierServiceList record {
+    @jsondata:Name {value: "carrier_services"}
     CarrierServiceListCarrierServices[] carrierServices?;
 };
 
 
 type ConnectInventoryItem record {
+    @jsondata:Name {value: "inventory_level"}
     ConnectInventoryItemInventoryLevel inventoryLevel?;
 };
 
 
 type ScriptTagsList record {
+    @jsondata:Name {value: "script_tags"}
     SingleScriptTagScriptTag[] scriptTags?;
 };
 
@@ -9857,6 +13217,7 @@
 
 
 type FulfillmentOrder record {
+    @jsondata:Name {value: "fulfillment_order"}
     FulfillmentOrderFulfillmentOrder fulfillmentOrder?;
 };
 
@@ -9869,30 +13230,41 @@
 
 
 type CollectionList record {
+    @jsondata:Name {value: "custom_collections"}
     CollectionListCustomCollections[] customCollections?;
 };
 
 
 type SingleArticleArticle record {
     SingleArticleArticleImage image?;
+    @jsondata:Name {value: "blog_id"}
     int blogId?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     string author?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string 'handle?;
     string title?;
     string tags?;
+    @jsondata:Name {value: "template_suffix"}
     anydata? templateSuffix?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
+    @jsondata:Name {value: "user_id"}
     int userId?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
+    @jsondata:Name {value: "summary_html"}
     anydata? summaryHtml?;
 };
 
 
 type CreateMarketingEvent record {
+    @jsondata:Name {value: "marketing_event"}
     CreateMarketingEventMarketingEvent marketingEvent?;
 };
 
@@ -9910,11 +13282,13 @@
 
 
 type InventoryItem record {
+    @jsondata:Name {value: "inventory_item"}
     InventoryItemInventoryItem inventoryItem?;
 };
 
 
 type UpdateDiscountCode record {
+    @jsondata:Name {value: "discount_code"}
     UpdateDiscountCodeDiscountCode discountCode?;
 };
 
@@ -9925,16 +13299,21 @@
 
 
 type SmartCollectionssmartCollectionIdJsonBody record {
+    @jsondata:Name {value: "smart_collection"}
     AdminapiapiVersionsmartCollectionssmartCollectionIdJsonSmartCollection smartCollection?;
 };
 
 
 type UpdateCarrierServiceCarrierService record {
+    @jsondata:Name {value: "callback_url"}
     string callbackUrl?;
+    @jsondata:Name {value: "carrier_service_type"}
     string carrierServiceType?;
+    @jsondata:Name {value: "admin_graphql_api_id"}
     string adminGraphqlApiId?;
     string format?;
     string name?;
+    @jsondata:Name {value: "service_discovery"}
     boolean serviceDiscovery?;
     boolean active?;
     int id?;
@@ -9942,60 +13321,107 @@
 
 
 type UpdateCheckoutResponseCheckout record {
+    @jsondata:Name {value: "privacy_policy_url"}
     anydata? privacyPolicyUrl?;
+    @jsondata:Name {value: "payment_url"}
     string paymentUrl?;
+    @jsondata:Name {value: "refund_policy_url"}
     anydata? refundPolicyUrl?;
+    @jsondata:Name {value: "requires_shipping"}
     boolean requiresShipping?;
+    @jsondata:Name {value: "terms_of_sale_url"}
     anydata? termsOfSaleUrl?;
+    @jsondata:Name {value: "billing_address"}
     SinglePaymentResponsePaymentCheckoutBillingAddress|() billingAddress?;
+    @jsondata:Name {value: "line_items"}
     SinglePaymentResponsePaymentCheckoutLineItems[] lineItems?;
+    @jsondata:Name {value: "presentment_currency"}
     string presentmentCurrency?;
+    @jsondata:Name {value: "location_id"}
     anydata? locationId?;
+    @jsondata:Name {value: "reservation_time_left"}
     int reservationTimeLeft?;
+    @jsondata:Name {value: "source_url"}
     anydata? sourceUrl?;
+    @jsondata:Name {value: "payment_due"}
     string paymentDue?;
+    @jsondata:Name {value: "source_identifier"}
     anydata? sourceIdentifier?;
+    @jsondata:Name {value: "tax_lines"}
     anydata[] taxLines?;
+    @jsondata:Name {value: "customer_locale"}
     anydata? customerLocale?;
+    @jsondata:Name {value: "tax_manipulations"}
     anydata[] taxManipulations?;
     anydata? 'order?;
+    @jsondata:Name {value: "terms_of_service_url"}
     anydata? termsOfServiceUrl?;
+    @jsondata:Name {value: "subtotal_price"}
     string subtotalPrice?;
+    @jsondata:Name {value: "subscription_policy_url"}
     anydata? subscriptionPolicyUrl?;
+    @jsondata:Name {value: "order_status_url"}
     anydata? orderStatusUrl?;
+    @jsondata:Name {value: "device_id"}
     anydata? deviceId?;
+    @jsondata:Name {value: "tax_exempt"}
     boolean taxExempt?;
+    @jsondata:Name {value: "discount_code"}
     anydata? discountCode?;
+    @jsondata:Name {value: "total_tax"}
     string totalTax?;
+    @jsondata:Name {value: "completed_at"}
     anydata? completedAt?;
+    @jsondata:Name {value: "shipping_rate"}
     anydata? shippingRate?;
     anydata? phone?;
+    @jsondata:Name {value: "user_id"}
     anydata? userId?;
+    @jsondata:Name {value: "note_attributes"}
     SinglePaymentResponsePaymentCheckoutNoteAttributes noteAttributes?;
     string name?;
+    @jsondata:Name {value: "shipping_line"}
     anydata? shippingLine?;
+    @jsondata:Name {value: "order_id"}
     anydata? orderId?;
     string? note?;
+    @jsondata:Name {value: "applied_discount"}
     anydata? appliedDiscount?;
     anydata[] payments?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
+    @jsondata:Name {value: "shopify_payments_account_id"}
     anydata? shopifyPaymentsAccountId?;
+    @jsondata:Name {value: "taxes_included"}
     boolean taxesIncluded?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     string currency?;
+    @jsondata:Name {value: "shipping_address"}
     UpdateCheckoutResponseCheckoutShippingAddress|() shippingAddress?;
     string email?;
+    @jsondata:Name {value: "source_name"}
     string sourceName?;
+    @jsondata:Name {value: "total_price"}
     string totalPrice?;
+    @jsondata:Name {value: "legal_notice_url"}
     anydata? legalNoticeUrl?;
+    @jsondata:Name {value: "total_line_items_price"}
     string totalLineItemsPrice?;
+    @jsondata:Name {value: "reservation_time"}
     anydata? reservationTime?;
+    @jsondata:Name {value: "total_tip_received"}
     string totalTipReceived?;
     string token?;
+    @jsondata:Name {value: "credit_card"}
     anydata? creditCard?;
+    @jsondata:Name {value: "gift_cards"}
     anydata[] giftCards?;
+    @jsondata:Name {value: "web_url"}
     string webUrl?;
+    @jsondata:Name {value: "shipping_policy_url"}
     anydata? shippingPolicyUrl?;
+    @jsondata:Name {value: "customer_id"}
     int customerId?;
 };
 
@@ -10008,16 +13434,25 @@
 
 
 type SingleFulfillmentOrderFulfillmentOrder record {
+    @jsondata:Name {value: "request_status"}
     string requestStatus?;
+    @jsondata:Name {value: "fulfillment_service_handle"}
     string fulfillmentServiceHandle?;
+    @jsondata:Name {value: "shop_id"}
     int shopId?;
     SingleFulfillmentOrderFulfillmentOrderDestination destination?;
+    @jsondata:Name {value: "assigned_location_id"}
     int assignedLocationId?;
     int id?;
+    @jsondata:Name {value: "line_items"}
     SingleFulfillmentOrderFulfillmentOrderLineItems[] lineItems?;
+    @jsondata:Name {value: "order_id"}
     int orderId?;
+    @jsondata:Name {value: "supported_actions"}
     string[] supportedActions?;
+    @jsondata:Name {value: "assigned_location"}
     FulfillmentOrdersAssignedLocation assignedLocation?;
+    @jsondata:Name {value: "merchant_requests"}
     anydata[] merchantRequests?;
     string status?;
 };
@@ -10036,11 +13471,13 @@
 
 
 type UpdateSmartCollection record {
+    @jsondata:Name {value: "smart_collection"}
     UpdateSmartCollectionSmartCollection smartCollection?;
 };
 
 
 type SingleFulfillmentOrder record {
+    @jsondata:Name {value: "fulfillment_order"}
     SingleFulfillmentOrderFulfillmentOrder fulfillmentOrder?;
 };
 
@@ -10048,16 +13485,22 @@
 
 type RetrieveACountOfSmartCollectionsQueries record {
     # Show smart collections last updated before this date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show smart collections last updated after this date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Show smart collections that include the specified product. 
+    @http:Query {name: "product_id"}
     string productId?;
     # Show smart collections published after this date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "published_at_min"}
     string publishedAtMin?;
     # Show smart collections published before this date. (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "published_at_max"}
     string publishedAtMax?;
     # Filter results based on the published status of smart collections.(default: any) 
+    @http:Query {name: "published_status"}
     string publishedStatus?;
     # Show smart collections with the specified title. 
     string title?;
@@ -10069,14 +13512,17 @@
     # A number between 0 and 1 that's assigned to the order. The closer the score is to 1, the more likely it is that the order is fraudulent
     string score?;
     # The ID of the checkout that the order risk belongs to
+    @jsondata:Name {value: "checkout_id"}
     int checkoutId?;
     # Whether the order risk is displayed on the order details page in the Shopify admin. If false, then this order risk is ignored when Shopify determines your app's overall risk level for the order
     boolean display?;
     # The recommended action given to the merchant. Valid values are, `cancel` - There is a high level of risk that this order is fraudulent. The merchant should cancel the order. `investigate` - There is a medium level of risk that this order is fraudulent. The merchant should investigate the order. `accept` - There is a low level of risk that this order is fraudulent. The order risk found no indication of fraud
     "cancel"|"investigate"|"accept" recommendation?;
     # Whether this order risk is severe enough to force the cancellation of the order. If true, then this order risk is included in the Order canceled message that's shown on the details page of the canceled order
+    @jsondata:Name {value: "cause_cancel"}
     boolean causeCancel?;
     # The message that's displayed to the merchant to indicate the results of the fraud check. The message is displayed only if display is set to true
+    @jsondata:Name {value: "merchant_message"}
     string merchantMessage?;
     # A unique numeric identifier for the order risk
     int id?;
@@ -10085,6 +13531,7 @@
     # The message that's displayed to the merchant to indicate the results of the fraud check. The message is displayed only if display is set to true
     string message?;
     # The ID of the order that the order risk belongs to
+    @jsondata:Name {value: "order_id"}
     int orderId?;
 };
 
@@ -10114,6 +13561,7 @@
     # Show only certain fields, specified by a comma-separated list of field names. 
     string fields?;
     # Show amounts in the shop currency.(default: false) 
+    @http:Query {name: "in_shop_currency"}
     string inShopCurrency?;
 };
 
@@ -10124,6 +13572,7 @@
 
 
 type UpdateCarrierService record {
+    @jsondata:Name {value: "carrier_service"}
     UpdateCarrierServiceCarrierService carrierService?;
 };
 
@@ -10148,6 +13597,7 @@
 
 
 type PriceRuleIdBatchJsonBody record {
+    @jsondata:Name {value: "discount_codes"}
     AdminapiapiVersionpriceRulespriceRuleIdbatchJsonDiscountCodes[] discountCodes?;
 };
 
@@ -10160,6 +13610,7 @@
 
 type ApiKeysConfig record {
     # The Shopify access token used to authenticate API requests.
+    @display {label: "", kind: "password"}
     string xShopifyAccessToken;
 };
 
@@ -10186,10 +13637,13 @@
 
 type RetrieveAListOfInventoryLevelsQueries record {
     # Show inventory levels updated at or after date (format: 2019-03-19T01:21:44-04:00). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # A comma-separated list of inventory item IDs.(maximum: 50) 
+    @http:Query {name: "inventory_item_ids"}
     string inventoryItemIds?;
     # A comma-separated list of location IDs. To find the ID of a location, use the [Location resource](/api/reference/location).(maximum: 50) 
+    @http:Query {name: "location_ids"}
     string locationIds?;
     # The maximum number of results to show.(default: 50)(maximum: 250) 
     string 'limit?;
@@ -10216,16 +13670,19 @@
 
 
 type DraftOrders record {
+    @jsondata:Name {value: "draft_orders"}
     DraftOrdersDraftOrders[]|() draftOrders?;
 };
 
 
 type ApiVersionCustomCollectionsJsonBody record {
+    @jsondata:Name {value: "custom_collection"}
     AdminapiapiVersioncustomCollectionsJsonCustomCollection customCollection?;
 };
 
 
 type PriceRule record {
+    @jsondata:Name {value: "price_rule"}
     PriceRulePriceRule priceRule?;
 };
 
@@ -10242,16 +13699,19 @@
     # A comma-separated list of fields to include in the response
     string fields?;
     # Restrict results to after the specified ID
+    @http:Query {name: "since_id"}
     string sinceId?;
 };
 
 
 type CreateFulfillmentService record {
+    @jsondata:Name {value: "fulfillment_service"}
     CreateFulfillmentServiceFulfillmentService fulfillmentService?;
 };
 
 
 type UpdateScriptTagResponse record {
+    @jsondata:Name {value: "script_tag"}
     UpdateScriptTagResponseScriptTag scriptTag?;
 };
 
@@ -10263,8 +13723,10 @@
     # Return presentment prices in only certain currencies, specified by a comma-separated list of [ISO 4217][1] currency codes. 
 
 [1]: https://en.wikipedia.org/wiki/ISO_4217
+    @http:Query {name: "presentment_currencies"}
     string presentmentCurrencies?;
     # Restrict results to after the specified ID 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # A comma-separated list of fields to include in the response 
     string fields?;
@@ -10272,6 +13734,7 @@
 
 
 type AccessScopes record {
+    @jsondata:Name {value: "access_scopes"}
     AccessScopesAccessScopes[] accessScopes?;
 };
 
@@ -10298,16 +13761,22 @@
 
 type RetrieveACountOfCustomCollectionsQueries record {
     # Count custom collections last updated before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Count custom collections last updated after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Count custom collections that include a given product. 
+    @http:Query {name: "product_id"}
     string productId?;
     # Count custom collections published after date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_min"}
     string publishedAtMin?;
     # Count custom collections published before date (format: 2014-04-25T16:15:47-04:00). 
+    @http:Query {name: "published_at_max"}
     string publishedAtMax?;
     # Count custom collections with a given published status.(default: any) 
+    @http:Query {name: "published_status"}
     string publishedStatus?;
     # Count custom collections with given title. 
     string title?;
@@ -10315,33 +13784,43 @@
 
 
 type FulfillmentOrderIdReleaseHoldJsonBody record {
+    @jsondata:Name {value: "fulfillment_order"}
     AdminapiapiVersionfulfillmentOrdersfulfillmentOrderIdholdJsonFulfillmentOrder fulfillmentOrder?;
 };
 
 
 type RemoveCommentResponse record {
+    @jsondata:Name {value: "blog_id"}
     int blogId?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     string author?;
     string ip?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string body?;
+    @jsondata:Name {value: "article_id"}
     int articleId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     anydata? publishedAt?;
     string email?;
+    @jsondata:Name {value: "user_agent"}
     string userAgent?;
     string status?;
 };
 
 
 type StorefrontAccessTokens record {
+    @jsondata:Name {value: "storefront_access_tokens"}
     StorefrontAccessTokensStorefrontAccessTokens[] storefrontAccessTokens?;
 };
 
 
 type PriceRules record {
+    @jsondata:Name {value: "price_rules"}
     SinglePriceRulePriceRule[] priceRules?;
 };
 
@@ -10352,16 +13831,19 @@
 
 
 type FulfillmentServicesfulfillmentServiceIdJsonBody record {
+    @jsondata:Name {value: "fulfillment_service"}
     AdminapiapiVersionfulfillmentServicesfulfillmentServiceIdJsonFulfillmentService fulfillmentService?;
 };
 
 
 type SingleDraftOrder record {
+    @jsondata:Name {value: "draft_order"}
     SingleDraftOrderDraftOrder draftOrder?;
 };
 
 
 type ApiVersionPriceRulesJsonBody record {
+    @jsondata:Name {value: "price_rule"}
     AdminapiapiVersionpriceRulesJsonPriceRule priceRule?;
 };
 
@@ -10377,6 +13859,7 @@
 
 
 type ApiVersionFulfillmentServicesJsonBody record {
+    @jsondata:Name {value: "fulfillment_service"}
     AdminapiapiVersionfulfillmentServicesJsonFulfillmentService fulfillmentService?;
 };
 
@@ -10389,12 +13872,16 @@
 
 type RetrieveAListOfMetafieldsFromTheResourceSEndpointQueries record {
     # Show metafields created after date (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_min"}
     string createdAtMin?;
     # Show metafields created before date (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "created_at_max"}
     string createdAtMax?;
     # Show metafields last updated before date (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_max"}
     string updatedAtMax?;
     # Show metafields last updated after date (format: 2014-04-25T16:15:47-04:00) 
+    @http:Query {name: "updated_at_min"}
     string updatedAtMin?;
     # Amount of results(default: 50)(maximum: 250) 
     string 'limit?;
@@ -10403,6 +13890,7 @@
     # comma-separated list of fields to include in the response 
     string fields?;
     # Restrict results to after the specified ID 
+    @http:Query {name: "since_id"}
     string sinceId?;
     # The type of data that the metafield stores in the `value` field. Refer to the list of supported types
     string 'type?;
@@ -10412,6 +13900,7 @@
 
 
 type SingleCustomCollection record {
+    @jsondata:Name {value: "custom_collection"}
     SingleCustomCollectionCustomCollection customCollection?;
 };
 
@@ -10432,23 +13921,31 @@
 
 
 type RestoreRemoveComment record {
+    @jsondata:Name {value: "blog_id"}
     int blogId?;
+    @jsondata:Name {value: "body_html"}
     string bodyHtml?;
     string author?;
     string ip?;
+    @jsondata:Name {value: "created_at"}
     string createdAt?;
     string body?;
+    @jsondata:Name {value: "article_id"}
     int articleId?;
+    @jsondata:Name {value: "updated_at"}
     string updatedAt?;
     int id?;
+    @jsondata:Name {value: "published_at"}
     string publishedAt?;
     string email?;
+    @jsondata:Name {value: "user_agent"}
     string userAgent?;
     string status?;
 };
 
 
 type AvailableShippingRates record {
+    @jsondata:Name {value: "shipping_rates"}
     AvailableShippingRatesShippingRates[] shippingRates?;
 };
 
@@ -10464,11 +13961,13 @@
 
 
 type MobilePlatformApplication record {
+    @jsondata:Name {value: "mobile_platform_application"}
     MobilePlatformApplicationMobilePlatformApplication mobilePlatformApplication?;
 };
 
 
 type ApiVersionResourceFeedbackJsonBody record {
+    @jsondata:Name {value: "resource_feedback"}
     AdminapiapiVersionresourceFeedbackJsonResourceFeedback resourceFeedback?;
 };
 
@@ -10484,6 +13983,7 @@
 
 
 type UsageChargeList record {
+    @jsondata:Name {value: "usage_charges"}
     UsageChargeListUsageCharges[] usageCharges?;
 };
 
@@ -10520,7 +14020,7 @@
 
     # Retrieves a list of application charges
     # 
-    remote function retrieveAListOfApplicationCharges(map<string|string[]> headers = {}, string fields = "", string sinceId = "", anydata Additional Values, RetrieveAListOfApplicationChargesQueries queries) returns ApplicationChargesList|error;
+    remote function retrieveAListOfApplicationCharges(map<string|string[]> headers = {}, string fields = "", string sinceId = "", RetrieveAListOfApplicationChargesQueries queries) returns ApplicationChargesList|error;
 
     # Creates an application charge
     # 
@@ -10528,19 +14028,19 @@
 
     # Retrieves an application charge
     # 
-    remote function retrieveAnApplicationCharge(string applicationChargeId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveAnApplicationChargeQueries queries) returns ApplicationChargeResult|error;
+    remote function retrieveAnApplicationCharge(string applicationChargeId, map<string|string[]> headers = {}, string fields = "", RetrieveAnApplicationChargeQueries queries) returns ApplicationChargeResult|error;
 
     # Retrieves all application credits
     # 
-    remote function retrieveAllApplicationCredits(map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveAllApplicationCreditsQueries queries) returns ApplicationCredits|error;
+    remote function retrieveAllApplicationCredits(map<string|string[]> headers = {}, string fields = "", RetrieveAllApplicationCreditsQueries queries) returns ApplicationCredits|error;
 
     # Retrieves a single application credit
     # 
-    remote function retrieveASingleApplicationCredit(string aplicationCreditId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleApplicationCreditQueries queries) returns ApplicationCredit|error;
+    remote function retrieveASingleApplicationCredit(string aplicationCreditId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleApplicationCreditQueries queries) returns ApplicationCredit|error;
 
     # Retrieves a list of recurring application charges
     # 
-    remote function retrieveAListOfRecurringApplicationCharges(map<string|string[]> headers = {}, string fields = "", string sinceId = "", anydata Additional Values, RetrieveAListOfRecurringApplicationChargesQueries queries) returns RecurringApplicationCharges|error;
+    remote function retrieveAListOfRecurringApplicationCharges(map<string|string[]> headers = {}, string fields = "", string sinceId = "", RetrieveAListOfRecurringApplicationChargesQueries queries) returns RecurringApplicationCharges|error;
 
     # Creates a recurring application charge
     # 
@@ -10548,7 +14048,7 @@
 
     # Retrieves a single charge
     # 
-    remote function retrieveASingleCharge(string recurringApplicationChargeId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleChargeQueries queries) returns SingleCharge|error;
+    remote function retrieveASingleCharge(string recurringApplicationChargeId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleChargeQueries queries) returns SingleCharge|error;
 
     # Cancels a recurring application charge
     # 
@@ -10556,11 +14056,11 @@
 
     # Updates the capped amount of a recurring application charge
     # 
-    remote function updateTheCappedAmountOfARecurringApplicationCharge(string recurringApplicationChargeId, string payload, map<string|string[]> headers = {}, string recurringApplicationChargeCappedAmount = "", anydata Additional Values, UpdateTheCappedAmountOfARecurringApplicationChargeQueries queries) returns CappedAmountCharge|error;
+    remote function updateTheCappedAmountOfARecurringApplicationCharge(string recurringApplicationChargeId, string payload, map<string|string[]> headers = {}, string recurringApplicationChargeCappedAmount = "", UpdateTheCappedAmountOfARecurringApplicationChargeQueries queries) returns CappedAmountCharge|error;
 
     # Retrieves a list of usage charges
     # 
-    remote function retrieveAListOfUsageCharges(string recurringApplicationChargeId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveAListOfUsageChargesQueries queries) returns UsageChargeList|error;
+    remote function retrieveAListOfUsageCharges(string recurringApplicationChargeId, map<string|string[]> headers = {}, string fields = "", RetrieveAListOfUsageChargesQueries queries) returns UsageChargeList|error;
 
     # Creates a usage charge
     # 
@@ -10568,11 +14068,11 @@
 
     # Retrieves a single charge
     # 
-    remote function retrieveASingleCharge1(string recurringApplicationChargeId, string usageChargeId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleCharge1Queries queries) returns SingleUsageCharge|error;
+    remote function retrieveASingleCharge1(string recurringApplicationChargeId, string usageChargeId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleCharge1Queries queries) returns SingleUsageCharge|error;
 
     # Retrieves a list of customers
     # 
-    remote function retrieveAListOfCustomers(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string limit = "", string ids = "", string fields = "", string sinceId = "", anydata Additional Values, RetrieveAListOfCustomersQueries queries) returns Customers|error;
+    remote function retrieveAListOfCustomers(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string limit = "", string ids = "", string fields = "", string sinceId = "", RetrieveAListOfCustomersQueries queries) returns Customers|error;
 
     # Creates a customer
     # 
@@ -10588,7 +14088,7 @@
 
     # Retrieves a single customer
     # 
-    remote function retrieveASingleCustomer(string customerId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleCustomerQueries queries) returns CustomerResponse|error;
+    remote function retrieveASingleCustomer(string customerId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleCustomerQueries queries) returns CustomerResponse|error;
 
     # Updates a customer
     # 
@@ -10608,7 +14108,7 @@
 
     # Searches for customers that match a supplied query
     # 
-    remote function searchForCustomersThatMatchASuppliedQuery(map<string|string[]> headers = {}, string query = "", string limit = "", string fields = "", string order = "", anydata Additional Values, SearchForCustomersThatMatchASuppliedQueryQueries queries) returns Customers|error;
+    remote function searchForCustomersThatMatchASuppliedQuery(map<string|string[]> headers = {}, string query = "", string limit = "", string fields = "", string order = "", SearchForCustomersThatMatchASuppliedQueryQueries queries) returns Customers|error;
 
     # Retrieves a list of addresses for a customer
     # 
@@ -10652,7 +14152,7 @@
 
     # Retrieves a count of discount codes for a shop
     # 
-    remote function retrieveACountOfDiscountCodesForAShop(map<string|string[]> headers = {}, string timesUsedMax = "", string timesUsedMin = "", string timesUsed = "", anydata Additional Values, RetrieveACountOfDiscountCodesForAShopQueries queries) returns EventsCount|error;
+    remote function retrieveACountOfDiscountCodesForAShop(map<string|string[]> headers = {}, string timesUsedMax = "", string timesUsedMin = "", string timesUsed = "", RetrieveACountOfDiscountCodesForAShopQueries queries) returns EventsCount|error;
 
     # Retrieves the location of a discount code
     # 
@@ -10680,7 +14180,7 @@
 
     # Retrieves a list of price rules
     # 
-    remote function retrieveAListOfPriceRules(map<string|string[]> headers = {}, string createdAtMin = "", string startsAtMin = "", string createdAtMax = "", string updatedAtMax = "", string startsAtMax = "", string updatedAtMin = "", string limit = "", string timesUsed = "", string sinceId = "", string endsAtMin = "", string endsAtMax = "", anydata Additional Values, RetrieveAListOfPriceRulesQueries queries) returns PriceRules|error;
+    remote function retrieveAListOfPriceRules(map<string|string[]> headers = {}, string createdAtMin = "", string startsAtMin = "", string createdAtMax = "", string updatedAtMax = "", string startsAtMax = "", string updatedAtMin = "", string limit = "", string timesUsed = "", string sinceId = "", string endsAtMin = "", string endsAtMax = "", RetrieveAListOfPriceRulesQueries queries) returns PriceRules|error;
 
     # Creates a price rule
     # 
@@ -10704,19 +14204,19 @@
 
     # Retrieves a list of events
     # 
-    remote function retrieveAListOfEvents(map<string|string[]> headers = {}, string createdAtMin = "", string filter = "", string createdAtMax = "", string limit = "", string verb = "", string sinceId = "", string fields = "", anydata Additional Values, RetrieveAListOfEventsQueries queries) returns EventsList|error;
+    remote function retrieveAListOfEvents(map<string|string[]> headers = {}, string createdAtMin = "", string filter = "", string createdAtMax = "", string limit = "", string verb = "", string sinceId = "", string fields = "", RetrieveAListOfEventsQueries queries) returns EventsList|error;
 
     # Retrieves a single event
     # 
-    remote function retrieveASingleEvent(string eventId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleEventQueries queries) returns SingleEvent|error;
+    remote function retrieveASingleEvent(string eventId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleEventQueries queries) returns SingleEvent|error;
 
     # Retrieves a count of events
     # 
-    remote function retrieveACountOfEvents(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", anydata Additional Values, RetrieveACountOfEventsQueries queries) returns EventsCount|error;
+    remote function retrieveACountOfEvents(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", RetrieveACountOfEventsQueries queries) returns EventsCount|error;
 
     # Retrieves a list of gift cards
     # 
-    remote function retrieveAListOfGiftCards(map<string|string[]> headers = {}, string limit = "", string sinceId = "", string fields = "", string status = "", anydata Additional Values, RetrieveAListOfGiftCardsQueries queries) returns GiftCardsList|error;
+    remote function retrieveAListOfGiftCards(map<string|string[]> headers = {}, string limit = "", string sinceId = "", string fields = "", string status = "", RetrieveAListOfGiftCardsQueries queries) returns GiftCardsList|error;
 
     # Creates a gift card
     # 
@@ -10728,7 +14228,7 @@
 
     # Retrieves a single gift card
     # 
-    remote function retrieveASingleGiftCard(string giftCardId, map<string|string[]> headers = {}, string status = "", anydata Additional Values, RetrieveASingleGiftCardQueries queries) returns SingleGiftCard|error;
+    remote function retrieveASingleGiftCard(string giftCardId, map<string|string[]> headers = {}, string status = "", RetrieveASingleGiftCardQueries queries) returns SingleGiftCard|error;
 
     # Updates an existing gift card
     # 
@@ -10736,15 +14236,15 @@
 
     # Retrieves a count of gift cards
     # 
-    remote function retrieveACountOfGiftCards(map<string|string[]> headers = {}, string status = "", anydata Additional Values, RetrieveACountOfGiftCardsQueries queries) returns EventsCount|error;
+    remote function retrieveACountOfGiftCards(map<string|string[]> headers = {}, string status = "", RetrieveACountOfGiftCardsQueries queries) returns EventsCount|error;
 
     # Searches for gift cards
     # 
-    remote function searchForGiftCards(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string query = "", string limit = "", string fields = "", string order = "", anydata Additional Values, SearchForGiftCardsQueries queries) returns GiftCardSearch|error;
+    remote function searchForGiftCards(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string query = "", string limit = "", string fields = "", string order = "", SearchForGiftCardsQueries queries) returns GiftCardSearch|error;
 
     # Retrieves a detailed list for inventory items by IDs
     # 
-    remote function retrieveADetailedListForInventoryItemsByIds(map<string|string[]> headers = {}, string limit = "", string ids = "", anydata Additional Values, RetrieveADetailedListForInventoryItemsByIdsQueries queries) returns error?;
+    remote function retrieveADetailedListForInventoryItemsByIds(map<string|string[]> headers = {}, string limit = "", string ids = "", RetrieveADetailedListForInventoryItemsByIdsQueries queries) returns error?;
 
     # Retrieves a single inventory item by ID
     # 
@@ -10768,7 +14268,7 @@
 
     # Retrieves a list of inventory levels
     # 
-    remote function retrieveAListOfInventoryLevels(map<string|string[]> headers = {}, string updatedAtMin = "", string inventoryItemIds = "", string locationIds = "", string limit = "", anydata Additional Values, RetrieveAListOfInventoryLevelsQueries queries) returns InventoryLevels|error;
+    remote function retrieveAListOfInventoryLevels(map<string|string[]> headers = {}, string updatedAtMin = "", string inventoryItemIds = "", string locationIds = "", string limit = "", RetrieveAListOfInventoryLevelsQueries queries) returns InventoryLevels|error;
 
     # Deletes an inventory level from a location
     # 
@@ -10792,7 +14292,7 @@
 
     # Retrieves a list of all marketing events
     # 
-    remote function retrieveAListOfAllMarketingEvents(map<string|string[]> headers = {}, string offset = "", string limit = "", anydata Additional Values, RetrieveAListOfAllMarketingEventsQueries queries) returns MarketingEvents|error;
+    remote function retrieveAListOfAllMarketingEvents(map<string|string[]> headers = {}, string offset = "", string limit = "", RetrieveAListOfAllMarketingEventsQueries queries) returns MarketingEvents|error;
 
     # Creates a marketing event
     # 
@@ -10820,7 +14320,7 @@
 
     # Retrieve a list of metafields from the resource's endpoint
     # 
-    remote function retrieveAListOfMetafieldsFromTheResourceSEndpoint(string ownerId, string ownerResource, map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string limit = "", string namespace = "", string fields = "", string sinceId = "", string type = "", string key = "", anydata Additional Values, RetrieveAListOfMetafieldsFromTheResourceSEndpointQueries queries) returns MetafieldList|error;
+    remote function retrieveAListOfMetafieldsFromTheResourceSEndpoint(string ownerId, string ownerResource, map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string limit = "", string namespace = "", string fields = "", string sinceId = "", string type = "", string key = "", RetrieveAListOfMetafieldsFromTheResourceSEndpointQueries queries) returns MetafieldList|error;
 
     # Create a metafield
     # 
@@ -10828,7 +14328,7 @@
 
     # [Shop] Retrieve a list of metafields from the resource's endpoint
     # 
-    remote function shopRetrieveAListOfMetafieldsFromTheResourceSEndpoint(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string metafieldOwnerId = "", string updatedAtMin = "", string limit = "", string namespace = "", string fields = "", string sinceId = "", string type = "", string key = "", string metafieldOwnerResource = "", anydata Additional Values, ShopRetrieveAListOfMetafieldsFromTheResourceSEndpointQueries queries) returns error?;
+    remote function shopRetrieveAListOfMetafieldsFromTheResourceSEndpoint(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string metafieldOwnerId = "", string updatedAtMin = "", string limit = "", string namespace = "", string fields = "", string sinceId = "", string type = "", string key = "", string metafieldOwnerResource = "", ShopRetrieveAListOfMetafieldsFromTheResourceSEndpointQueries queries) returns error?;
 
     # [Shop] Create a metafield
     # 
@@ -10836,7 +14336,7 @@
 
     # Retrieve a specific metafield
     # 
-    remote function retrieveASpecificMetafield(string ownerId, string ownerResource, string metafieldId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASpecificMetafieldQueries queries) returns MetafieldResponse|error;
+    remote function retrieveASpecificMetafield(string ownerId, string ownerResource, string metafieldId, map<string|string[]> headers = {}, string fields = "", RetrieveASpecificMetafieldQueries queries) returns MetafieldResponse|error;
 
     # Updates a metafield
     # 
@@ -10848,7 +14348,7 @@
 
     # [Shop] Retrieve a specific metafield
     # 
-    remote function shopRetrieveASpecificMetafield(string metafieldId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, ShopRetrieveASpecificMetafieldQueries queries) returns MetafieldResponse|error;
+    remote function shopRetrieveASpecificMetafield(string metafieldId, map<string|string[]> headers = {}, string fields = "", ShopRetrieveASpecificMetafieldQueries queries) returns MetafieldResponse|error;
 
     # [Shop] Updates a metafield
     # 
@@ -10888,7 +14388,7 @@
 
     # Retrieves a list of all articles from a blog
     # 
-    remote function retrieveAListOfAllArticlesFromABlog(string blogId, map<string|string[]> headers = {}, string createdAtMin = "", string updatedAtMax = "", string author = "", string publishedAtMin = "", string handle = "", string publishedStatus = "", string sinceId = "", string createdAtMax = "", string updatedAtMin = "", string limit = "", string publishedAtMax = "", string tag = "", string fields = "", anydata Additional Values, RetrieveAListOfAllArticlesFromABlogQueries queries) returns Articles|error;
+    remote function retrieveAListOfAllArticlesFromABlog(string blogId, map<string|string[]> headers = {}, string createdAtMin = "", string updatedAtMax = "", string author = "", string publishedAtMin = "", string handle = "", string publishedStatus = "", string sinceId = "", string createdAtMax = "", string updatedAtMin = "", string limit = "", string publishedAtMax = "", string tag = "", string fields = "", RetrieveAListOfAllArticlesFromABlogQueries queries) returns Articles|error;
 
     # Creates an article for a blog
     # 
@@ -10900,11 +14400,11 @@
 
     # Retrieves a list of all article tags
     # 
-    remote function retrieveAListOfAllArticleTags(map<string|string[]> headers = {}, string limit = "", string popular = "", anydata Additional Values, RetrieveAListOfAllArticleTagsQueries queries) returns TagsList|error;
+    remote function retrieveAListOfAllArticleTags(map<string|string[]> headers = {}, string limit = "", string popular = "", RetrieveAListOfAllArticleTagsQueries queries) returns TagsList|error;
 
     # Receive a single Article
     # 
-    remote function receiveASingleArticle(string blogId, string articleId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, ReceiveASingleArticleQueries queries) returns SingleArticle|error;
+    remote function receiveASingleArticle(string blogId, string articleId, map<string|string[]> headers = {}, string fields = "", ReceiveASingleArticleQueries queries) returns SingleArticle|error;
 
     # Updates an article
     # 
@@ -10916,15 +14416,15 @@
 
     # Retrieves a count of all articles from a blog
     # 
-    remote function retrieveACountOfAllArticlesFromABlog(string blogId, map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string publishedAtMin = "", string publishedAtMax = "", string publishedStatus = "", anydata Additional Values, RetrieveACountOfAllArticlesFromABlogQueries queries) returns ArticlesCount|error;
+    remote function retrieveACountOfAllArticlesFromABlog(string blogId, map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string publishedAtMin = "", string publishedAtMax = "", string publishedStatus = "", RetrieveACountOfAllArticlesFromABlogQueries queries) returns ArticlesCount|error;
 
     # Retrieves a list of all article tags from a specific blog
     # 
-    remote function retrieveAListOfAllArticleTagsFromASpecificBlog(string blogId, map<string|string[]> headers = {}, string limit = "", string popular = "", anydata Additional Values, RetrieveAListOfAllArticleTagsFromASpecificBlogQueries queries) returns Articles|error;
+    remote function retrieveAListOfAllArticleTagsFromASpecificBlog(string blogId, map<string|string[]> headers = {}, string limit = "", string popular = "", RetrieveAListOfAllArticleTagsFromASpecificBlogQueries queries) returns Articles|error;
 
     # Retrieves a list of assets for a theme
     # 
-    remote function retrieveAListOfAssetsForATheme(string themeId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveAListOfAssetsForAThemeQueries queries) returns AssetsList|error;
+    remote function retrieveAListOfAssetsForATheme(string themeId, map<string|string[]> headers = {}, string fields = "", RetrieveAListOfAssetsForAThemeQueries queries) returns AssetsList|error;
 
     # Creates or updates an asset for a theme
     # 
@@ -10936,7 +14436,7 @@
 
     # Retrieve a list of all blogs
     # 
-    remote function retrieveAListOfAllBlogs(map<string|string[]> headers = {}, string limit = "", string handle = "", string sinceId = "", string fields = "", anydata Additional Values, RetrieveAListOfAllBlogsQueries queries) returns Blogs|error;
+    remote function retrieveAListOfAllBlogs(map<string|string[]> headers = {}, string limit = "", string handle = "", string sinceId = "", string fields = "", RetrieveAListOfAllBlogsQueries queries) returns Blogs|error;
 
     # Create a new Blog
     # 
@@ -10944,7 +14444,7 @@
 
     # Receive a single Blog
     # 
-    remote function receiveASingleBlog(string blogId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, ReceiveASingleBlogQueries queries) returns SingleBlog|error;
+    remote function receiveASingleBlog(string blogId, map<string|string[]> headers = {}, string fields = "", ReceiveASingleBlogQueries queries) returns SingleBlog|error;
 
     # Modify an existing Blog
     # 
@@ -10960,7 +14460,7 @@
 
     # Retrieves a list of comments
     # 
-    remote function retrieveAListOfComments(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string publishedAtMin = "", string limit = "", string publishedAtMax = "", string publishedStatus = "", string sinceId = "", string fields = "", string status = "", anydata Additional Values, RetrieveAListOfCommentsQueries queries) returns ArticleComments|error;
+    remote function retrieveAListOfComments(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string publishedAtMin = "", string limit = "", string publishedAtMax = "", string publishedStatus = "", string sinceId = "", string fields = "", string status = "", RetrieveAListOfCommentsQueries queries) returns ArticleComments|error;
 
     # Creates a comment for an article
     # 
@@ -10988,7 +14488,7 @@
 
     # Retrieves a single comment by its ID
     # 
-    remote function retrieveASingleCommentByItsId(string commentId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleCommentByItsIdQueries queries) returns SingleCommentResponse|error;
+    remote function retrieveASingleCommentByItsId(string commentId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleCommentByItsIdQueries queries) returns SingleCommentResponse|error;
 
     # Updates a comment of an article
     # 
@@ -10996,11 +14496,11 @@
 
     # Retrieves a count of comments
     # 
-    remote function retrieveACountOfComments(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string publishedAtMin = "", string publishedAtMax = "", string publishedStatus = "", string status = "", anydata Additional Values, RetrieveACountOfCommentsQueries queries) returns BlogsCount|error;
+    remote function retrieveACountOfComments(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string publishedAtMin = "", string publishedAtMax = "", string publishedStatus = "", string status = "", RetrieveACountOfCommentsQueries queries) returns BlogsCount|error;
 
     # Retrieves a list of pages
     # 
-    remote function retrieveAListOfPages(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string publishedAtMin = "", string limit = "", string publishedAtMax = "", string handle = "", string publishedStatus = "", string sinceId = "", string title = "", string fields = "", anydata Additional Values, RetrieveAListOfPagesQueries queries) returns PagesListResponse|error;
+    remote function retrieveAListOfPages(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string publishedAtMin = "", string limit = "", string publishedAtMax = "", string handle = "", string publishedStatus = "", string sinceId = "", string title = "", string fields = "", RetrieveAListOfPagesQueries queries) returns PagesListResponse|error;
 
     # Create a new Page
     # 
@@ -11008,7 +14508,7 @@
 
     # Retrieves a single page by its ID
     # 
-    remote function retrieveASinglePageByItsId(string pageId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASinglePageByItsIdQueries queries) returns SinglePageResponse|error;
+    remote function retrieveASinglePageByItsId(string pageId, map<string|string[]> headers = {}, string fields = "", RetrieveASinglePageByItsIdQueries queries) returns SinglePageResponse|error;
 
     # Updates a page
     # 
@@ -11020,11 +14520,11 @@
 
     # Retrieves a page count
     # 
-    remote function retrieveAPageCount(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string publishedAtMin = "", string publishedAtMax = "", string publishedStatus = "", string title = "", anydata Additional Values, RetrieveAPageCountQueries queries) returns ArticlesCount|error;
+    remote function retrieveAPageCount(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string publishedAtMin = "", string publishedAtMax = "", string publishedStatus = "", string title = "", RetrieveAPageCountQueries queries) returns ArticlesCount|error;
 
     # Retrieves a list of URL redirects
     # 
-    remote function retrieveAListOfUrlRedirects(map<string|string[]> headers = {}, string path = "", string limit = "", string sinceId = "", string fields = "", string target = "", anydata Additional Values, RetrieveAListOfUrlRedirectsQueries queries) returns UrlList|error;
+    remote function retrieveAListOfUrlRedirects(map<string|string[]> headers = {}, string path = "", string limit = "", string sinceId = "", string fields = "", string target = "", RetrieveAListOfUrlRedirectsQueries queries) returns UrlList|error;
 
     # Creates a redirect
     # 
@@ -11032,7 +14532,7 @@
 
     # Retrieves a single redirect
     # 
-    remote function retrieveASingleRedirect(string redirectId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleRedirectQueries queries) returns SingleRedirect|error;
+    remote function retrieveASingleRedirect(string redirectId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleRedirectQueries queries) returns SingleRedirect|error;
 
     # Updates an existing redirect
     # 
@@ -11044,11 +14544,11 @@
 
     # Retrieves a count of URL redirects
     # 
-    remote function retrieveACountOfUrlRedirects(map<string|string[]> headers = {}, string path = "", string target = "", anydata Additional Values, RetrieveACountOfUrlRedirectsQueries queries) returns EventsCount|error;
+    remote function retrieveACountOfUrlRedirects(map<string|string[]> headers = {}, string path = "", string target = "", RetrieveACountOfUrlRedirectsQueries queries) returns EventsCount|error;
 
     # Retrieves a list of all script tags
     # 
-    remote function retrieveAListOfAllScriptTags(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string src = "", string limit = "", string sinceId = "", string fields = "", anydata Additional Values, RetrieveAListOfAllScriptTagsQueries queries) returns ScriptTagsList|error;
+    remote function retrieveAListOfAllScriptTags(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string src = "", string limit = "", string sinceId = "", string fields = "", RetrieveAListOfAllScriptTagsQueries queries) returns ScriptTagsList|error;
 
     # Creates a new script tag
     # 
@@ -11056,7 +14556,7 @@
 
     # Retrieves a single script tag
     # 
-    remote function retrieveASingleScriptTag(string scriptTagId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleScriptTagQueries queries) returns SingleScriptTag|error;
+    remote function retrieveASingleScriptTag(string scriptTagId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleScriptTagQueries queries) returns SingleScriptTag|error;
 
     # Updates a script tag
     # 
@@ -11068,11 +14568,11 @@
 
     # Retrieves a count of all script tags
     # 
-    remote function retrieveACountOfAllScriptTags(map<string|string[]> headers = {}, string src = "", anydata Additional Values, RetrieveACountOfAllScriptTagsQueries queries) returns BlogsCount|error;
+    remote function retrieveACountOfAllScriptTags(map<string|string[]> headers = {}, string src = "", RetrieveACountOfAllScriptTagsQueries queries) returns BlogsCount|error;
 
     # Retrieves a list of themes
     # 
-    remote function retrieveAListOfThemes(map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveAListOfThemesQueries queries) returns ThemesList|error;
+    remote function retrieveAListOfThemes(map<string|string[]> headers = {}, string fields = "", RetrieveAListOfThemesQueries queries) returns ThemesList|error;
 
     # Creates a theme
     # 
@@ -11080,7 +14580,7 @@
 
     # Retrieves a single theme
     # 
-    remote function retrieveASingleTheme(string themeId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleThemeQueries queries) returns SingleTheme|error;
+    remote function retrieveASingleTheme(string themeId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleThemeQueries queries) returns SingleTheme|error;
 
     # Modify an existing Theme
     # 
@@ -11092,11 +14592,11 @@
 
     # Retrieves a count of checkouts
     # 
-    remote function retrieveACountOfCheckouts(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string sinceId = "", string status = "", anydata Additional Values, RetrieveACountOfCheckoutsQueries queries) returns CheckoutCount|error;
+    remote function retrieveACountOfCheckouts(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string sinceId = "", string status = "", RetrieveACountOfCheckoutsQueries queries) returns CheckoutCount|error;
 
     # Retrieves a list of abandoned checkouts
     # 
-    remote function retrieveAListOfAbandonedCheckouts(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string limit = "", string sinceId = "", string status = "", anydata Additional Values, RetrieveAListOfAbandonedCheckoutsQueries queries) returns AbandonedCheckouts|error;
+    remote function retrieveAListOfAbandonedCheckouts(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string limit = "", string sinceId = "", string status = "", RetrieveAListOfAbandonedCheckoutsQueries queries) returns AbandonedCheckouts|error;
 
     # Creates a checkout
     # 
@@ -11104,7 +14604,7 @@
 
     # Retrieves a list of draft orders
     # 
-    remote function retrieveAListOfDraftOrders(map<string|string[]> headers = {}, string updatedAtMax = "", string updatedAtMin = "", string limit = "", string ids = "", string fields = "", string sinceId = "", string status = "", anydata Additional Values, RetrieveAListOfDraftOrdersQueries queries) returns DraftOrders|error;
+    remote function retrieveAListOfDraftOrders(map<string|string[]> headers = {}, string updatedAtMax = "", string updatedAtMin = "", string limit = "", string ids = "", string fields = "", string sinceId = "", string status = "", RetrieveAListOfDraftOrdersQueries queries) returns DraftOrders|error;
 
     # Create a new DraftOrder
     # 
@@ -11116,7 +14616,7 @@
 
     # Receive a single DraftOrder
     # 
-    remote function receiveASingleDraftOrder(string draftOrderId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, ReceiveASingleDraftOrderQueries queries) returns SingleDraftOrder|error;
+    remote function receiveASingleDraftOrder(string draftOrderId, map<string|string[]> headers = {}, string fields = "", ReceiveASingleDraftOrderQueries queries) returns SingleDraftOrder|error;
 
     # Modify an existing DraftOrder
     # 
@@ -11128,7 +14628,7 @@
 
     # Receive a count of all DraftOrders
     # 
-    remote function receiveACountOfAllDraftOrders(map<string|string[]> headers = {}, string updatedAtMax = "", string updatedAtMin = "", string sinceId = "", string status = "", anydata Additional Values, ReceiveACountOfAllDraftOrdersQueries queries) returns StoreLocationCount|error;
+    remote function receiveACountOfAllDraftOrders(map<string|string[]> headers = {}, string updatedAtMax = "", string updatedAtMin = "", string sinceId = "", string status = "", ReceiveACountOfAllDraftOrdersQueries queries) returns StoreLocationCount|error;
 
     # Complete a draft order
     # 
@@ -11136,7 +14636,7 @@
 
     # Retrieves a list of orders
     # 
-    remote function retrieveAListOfOrders(map<string|string[]> headers = {}, string createdAtMin = "", string updatedAtMax = "", string fulfillmentStatus = "", string sinceId = "", string processedAtMax = "", string processedAtMin = "", string createdAtMax = "", string updatedAtMin = "", string financialStatus = "", string name = "", string limit = "", string ids = "", string attributionAppId = "", string fields = "", string status = "", anydata Additional Values, RetrieveAListOfOrdersQueries queries) returns OrdersList|error;
+    remote function retrieveAListOfOrders(map<string|string[]> headers = {}, string createdAtMin = "", string updatedAtMax = "", string fulfillmentStatus = "", string sinceId = "", string processedAtMax = "", string processedAtMin = "", string createdAtMax = "", string updatedAtMin = "", string financialStatus = "", string name = "", string limit = "", string ids = "", string attributionAppId = "", string fields = "", string status = "", RetrieveAListOfOrdersQueries queries) returns OrdersList|error;
 
     # Create an order
     # 
@@ -11168,7 +14668,7 @@
 
     # Retrieves an order count
     # 
-    remote function retrieveAnOrderCount(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string fulfillmentStatus = "", string updatedAtMin = "", string financialStatus = "", string status = "", anydata Additional Values, RetrieveAnOrderCountQueries queries) returns ObjectCount|error;
+    remote function retrieveAnOrderCount(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string fulfillmentStatus = "", string updatedAtMin = "", string financialStatus = "", string status = "", RetrieveAnOrderCountQueries queries) returns ObjectCount|error;
 
     # Retrieves a list of all order risks for an order
     # 
@@ -11192,7 +14692,7 @@
 
     # Retrieves a list of refunds for an order
     # 
-    remote function retrieveAListOfRefundsForAnOrder(string orderId, map<string|string[]> headers = {}, string limit = "", string fields = "", string inShopCurrency = "", anydata Additional Values, RetrieveAListOfRefundsForAnOrderQueries queries) returns Refunds|error;
+    remote function retrieveAListOfRefundsForAnOrder(string orderId, map<string|string[]> headers = {}, string limit = "", string fields = "", string inShopCurrency = "", RetrieveAListOfRefundsForAnOrderQueries queries) returns Refunds|error;
 
     # Creates a refund
     # 
@@ -11204,11 +14704,11 @@
 
     # Retrieves a specific refund
     # 
-    remote function retrieveASpecificRefund(string orderId, string refundId, map<string|string[]> headers = {}, string fields = "", string inShopCurrency = "", anydata Additional Values, RetrieveASpecificRefundQueries queries) returns RefundResponse|error;
+    remote function retrieveASpecificRefund(string orderId, string refundId, map<string|string[]> headers = {}, string fields = "", string inShopCurrency = "", RetrieveASpecificRefundQueries queries) returns RefundResponse|error;
 
     # Retrieves a list of transactions
     # 
-    remote function retrieveAListOfTransactions(string orderId, map<string|string[]> headers = {}, string sinceId = "", string fields = "", string inShopCurrency = "", anydata Additional Values, RetrieveAListOfTransactionsQueries queries) returns TransactionsList|error;
+    remote function retrieveAListOfTransactions(string orderId, map<string|string[]> headers = {}, string sinceId = "", string fields = "", string inShopCurrency = "", RetrieveAListOfTransactionsQueries queries) returns TransactionsList|error;
 
     # Creates a transaction for an order
     # 
@@ -11216,7 +14716,7 @@
 
     # Retrieves a specific transaction
     # 
-    remote function retrieveASpecificTransaction(string orderId, string transactionId, map<string|string[]> headers = {}, string fields = "", string inShopCurrency = "", anydata Additional Values, RetrieveASpecificTransactionQueries queries) returns TransactionResponse|error;
+    remote function retrieveASpecificTransaction(string orderId, string transactionId, map<string|string[]> headers = {}, string fields = "", string inShopCurrency = "", RetrieveASpecificTransactionQueries queries) returns TransactionResponse|error;
 
     # Retrieves a count of an order's transactions
     # 
@@ -11236,7 +14736,7 @@
 
     # Retrieves a list of collects
     # 
-    remote function retrieveAListOfCollects(map<string|string[]> headers = {}, string limit = "", string sinceId = "", string fields = "", anydata Additional Values, RetrieveAListOfCollectsQueries queries) returns CollectsList|error;
+    remote function retrieveAListOfCollects(map<string|string[]> headers = {}, string limit = "", string sinceId = "", string fields = "", RetrieveAListOfCollectsQueries queries) returns CollectsList|error;
 
     # Adds a product to a custom collection
     # 
@@ -11244,7 +14744,7 @@
 
     # Retrieves a specific collect by its ID
     # 
-    remote function retrieveASpecificCollectByItsId(string collectId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASpecificCollectByItsIdQueries queries) returns CollectResponse|error;
+    remote function retrieveASpecificCollectByItsId(string collectId, map<string|string[]> headers = {}, string fields = "", RetrieveASpecificCollectByItsIdQueries queries) returns CollectResponse|error;
 
     # Removes a product from a collection
     # 
@@ -11256,15 +14756,15 @@
 
     # Retrieves a single collection
     # 
-    remote function retrieveASingleCollection(string collectionId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleCollectionQueries queries) returns SingleCollection|error;
+    remote function retrieveASingleCollection(string collectionId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleCollectionQueries queries) returns SingleCollection|error;
 
     # Retrieve a list of products belonging to a collection
     # 
-    remote function retrieveAListOfProductsBelongingToACollection(string collectionId, map<string|string[]> headers = {}, string limit = "", anydata Additional Values, RetrieveAListOfProductsBelongingToACollectionQueries queries) returns ProductsList|error;
+    remote function retrieveAListOfProductsBelongingToACollection(string collectionId, map<string|string[]> headers = {}, string limit = "", RetrieveAListOfProductsBelongingToACollectionQueries queries) returns ProductsList|error;
 
     # Retrieves a list of custom collections
     # 
-    remote function retrieveAListOfCustomCollections(map<string|string[]> headers = {}, string updatedAtMax = "", string updatedAtMin = "", string productId = "", string publishedAtMin = "", string limit = "", string ids = "", string publishedAtMax = "", string handle = "", string publishedStatus = "", string sinceId = "", string title = "", string fields = "", anydata Additional Values, RetrieveAListOfCustomCollectionsQueries queries) returns CollectionList|error;
+    remote function retrieveAListOfCustomCollections(map<string|string[]> headers = {}, string updatedAtMax = "", string updatedAtMin = "", string productId = "", string publishedAtMin = "", string limit = "", string ids = "", string publishedAtMax = "", string handle = "", string publishedStatus = "", string sinceId = "", string title = "", string fields = "", RetrieveAListOfCustomCollectionsQueries queries) returns CollectionList|error;
 
     # Creates a custom collection
     # 
@@ -11272,7 +14772,7 @@
 
     # Retrieves a single custom collection
     # 
-    remote function retrieveASingleCustomCollection(string customCollectionId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleCustomCollectionQueries queries) returns SingleCustomCollection|error;
+    remote function retrieveASingleCustomCollection(string customCollectionId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleCustomCollectionQueries queries) returns SingleCustomCollection|error;
 
     # Updates an existing custom collection
     # 
@@ -11284,11 +14784,11 @@
 
     # Retrieves a count of custom collections
     # 
-    remote function retrieveACountOfCustomCollections(map<string|string[]> headers = {}, string updatedAtMax = "", string updatedAtMin = "", string productId = "", string publishedAtMin = "", string publishedAtMax = "", string publishedStatus = "", string title = "", anydata Additional Values, RetrieveACountOfCustomCollectionsQueries queries) returns BlogsCount|error;
+    remote function retrieveACountOfCustomCollections(map<string|string[]> headers = {}, string updatedAtMax = "", string updatedAtMin = "", string productId = "", string publishedAtMin = "", string publishedAtMax = "", string publishedStatus = "", string title = "", RetrieveACountOfCustomCollectionsQueries queries) returns BlogsCount|error;
 
     # Retrieves a list of products
     # 
-    remote function retrieveAListOfProducts(map<string|string[]> headers = {}, string createdAtMin = "", string updatedAtMax = "", string publishedAtMin = "", string handle = "", string publishedStatus = "", string sinceId = "", string title = "", string collectionId = "", string createdAtMax = "", string productType = "", string updatedAtMin = "", string vendor = "", string limit = "", string presentmentCurrencies = "", string ids = "", string publishedAtMax = "", string fields = "", anydata Additional Values, RetrieveAListOfProductsQueries queries) returns ProductsResponse|error;
+    remote function retrieveAListOfProducts(map<string|string[]> headers = {}, string createdAtMin = "", string updatedAtMax = "", string publishedAtMin = "", string handle = "", string publishedStatus = "", string sinceId = "", string title = "", string collectionId = "", string createdAtMax = "", string productType = "", string updatedAtMin = "", string vendor = "", string limit = "", string presentmentCurrencies = "", string ids = "", string publishedAtMax = "", string fields = "", RetrieveAListOfProductsQueries queries) returns ProductsResponse|error;
 
     # Creates a new product
     # 
@@ -11296,7 +14796,7 @@
 
     # Retrieves a single product
     # 
-    remote function retrieveASingleProduct(string productId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleProductQueries queries) returns SingleProduct|error;
+    remote function retrieveASingleProduct(string productId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleProductQueries queries) returns SingleProduct|error;
 
     # Updates a product
     # 
@@ -11308,11 +14808,11 @@
 
     # Retrieves a count of products
     # 
-    remote function retrieveACountOfProducts(map<string|string[]> headers = {}, string collectionId = "", string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string productType = "", string updatedAtMin = "", string vendor = "", string publishedAtMin = "", string publishedAtMax = "", string publishedStatus = "", anydata Additional Values, RetrieveACountOfProductsQueries queries) returns ObjectCount|error;
+    remote function retrieveACountOfProducts(map<string|string[]> headers = {}, string collectionId = "", string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string productType = "", string updatedAtMin = "", string vendor = "", string publishedAtMin = "", string publishedAtMax = "", string publishedStatus = "", RetrieveACountOfProductsQueries queries) returns ObjectCount|error;
 
     # Receive a list of all Product Images
     # 
-    remote function receiveAListOfAllProductImages(string productId, map<string|string[]> headers = {}, string sinceId = "", string fields = "", anydata Additional Values, ReceiveAListOfAllProductImagesQueries queries) returns ProductImages|error;
+    remote function receiveAListOfAllProductImages(string productId, map<string|string[]> headers = {}, string sinceId = "", string fields = "", ReceiveAListOfAllProductImagesQueries queries) returns ProductImages|error;
 
     # Create a new Product Image
     # 
@@ -11320,7 +14820,7 @@
 
     # Receive a single Product Image
     # 
-    remote function receiveASingleProductImage(string productId, string imageId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, ReceiveASingleProductImageQueries queries) returns SingleProductImage|error;
+    remote function receiveASingleProductImage(string productId, string imageId, map<string|string[]> headers = {}, string fields = "", ReceiveASingleProductImageQueries queries) returns SingleProductImage|error;
 
     # Modify an existing Product Image
     # 
@@ -11332,11 +14832,11 @@
 
     # Receive a count of all Product Images
     # 
-    remote function receiveACountOfAllProductImages(string productId, map<string|string[]> headers = {}, string sinceId = "", anydata Additional Values, ReceiveACountOfAllProductImagesQueries queries) returns BlogsCount|error;
+    remote function receiveACountOfAllProductImages(string productId, map<string|string[]> headers = {}, string sinceId = "", ReceiveACountOfAllProductImagesQueries queries) returns BlogsCount|error;
 
     # Retrieves a list of product variants
     # 
-    remote function retrieveAListOfProductVariants(string productId, map<string|string[]> headers = {}, string limit = "", string presentmentCurrencies = "", string sinceId = "", string fields = "", anydata Additional Values, RetrieveAListOfProductVariantsQueries queries) returns ProductVariants|error;
+    remote function retrieveAListOfProductVariants(string productId, map<string|string[]> headers = {}, string limit = "", string presentmentCurrencies = "", string sinceId = "", string fields = "", RetrieveAListOfProductVariantsQueries queries) returns ProductVariants|error;
 
     # Create a new Product Variant
     # 
@@ -11348,7 +14848,7 @@
 
     # Receive a single Product Variant
     # 
-    remote function receiveASingleProductVariant(string variantId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, ReceiveASingleProductVariantQueries queries) returns ProductVariantResponse|error;
+    remote function receiveASingleProductVariant(string variantId, map<string|string[]> headers = {}, string fields = "", ReceiveASingleProductVariantQueries queries) returns ProductVariantResponse|error;
 
     # Modify an existing Product Variant
     # 
@@ -11360,7 +14860,7 @@
 
     # Retrieves a list of smart collections
     # 
-    remote function retrieveAListOfSmartCollections(map<string|string[]> headers = {}, string updatedAtMax = "", string updatedAtMin = "", string productId = "", string publishedAtMin = "", string limit = "", string ids = "", string publishedAtMax = "", string handle = "", string publishedStatus = "", string sinceId = "", string title = "", string fields = "", anydata Additional Values, RetrieveAListOfSmartCollectionsQueries queries) returns SmartCollectionList|error;
+    remote function retrieveAListOfSmartCollections(map<string|string[]> headers = {}, string updatedAtMax = "", string updatedAtMin = "", string productId = "", string publishedAtMin = "", string limit = "", string ids = "", string publishedAtMax = "", string handle = "", string publishedStatus = "", string sinceId = "", string title = "", string fields = "", RetrieveAListOfSmartCollectionsQueries queries) returns SmartCollectionList|error;
 
     # Creates a smart collection
     # 
@@ -11368,7 +14868,7 @@
 
     # Retrieves a single smart collection
     # 
-    remote function retrieveASingleSmartCollection(string smartCollectionId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleSmartCollectionQueries queries) returns SmartCollectionResponse|error;
+    remote function retrieveASingleSmartCollection(string smartCollectionId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleSmartCollectionQueries queries) returns SmartCollectionResponse|error;
 
     # Updates an existing smart collection
     # 
@@ -11380,7 +14880,7 @@
 
     # Retrieves a count of smart collections
     # 
-    remote function retrieveACountOfSmartCollections(map<string|string[]> headers = {}, string updatedAtMax = "", string updatedAtMin = "", string productId = "", string publishedAtMin = "", string publishedAtMax = "", string publishedStatus = "", string title = "", anydata Additional Values, RetrieveACountOfSmartCollectionsQueries queries) returns ObjectCount|error;
+    remote function retrieveACountOfSmartCollections(map<string|string[]> headers = {}, string updatedAtMax = "", string updatedAtMin = "", string productId = "", string publishedAtMin = "", string publishedAtMax = "", string publishedStatus = "", string title = "", RetrieveACountOfSmartCollectionsQueries queries) returns ObjectCount|error;
 
     # Updates the ordering type of products in a smart collection
     # 
@@ -11404,11 +14904,11 @@
 
     # Retrieve collection listings that are published to your app
     # 
-    remote function retrieveCollectionListingsThatArePublishedToYourApp(map<string|string[]> headers = {}, string limit = "", anydata Additional Values, RetrieveCollectionListingsThatArePublishedToYourAppQueries queries) returns CollectionListingResponse|error;
+    remote function retrieveCollectionListingsThatArePublishedToYourApp(map<string|string[]> headers = {}, string limit = "", RetrieveCollectionListingsThatArePublishedToYourAppQueries queries) returns CollectionListingResponse|error;
 
     # Retrieve product_ids that are published to a collection_id
     # 
-    remote function retrieveProductIdsThatArePublishedToACollectionId(string collectionListingId, map<string|string[]> headers = {}, string limit = "", anydata Additional Values, RetrieveProductIdsThatArePublishedToACollectionIdQueries queries) returns ProductIds|error;
+    remote function retrieveProductIdsThatArePublishedToACollectionId(string collectionListingId, map<string|string[]> headers = {}, string limit = "", RetrieveProductIdsThatArePublishedToACollectionIdQueries queries) returns ProductIds|error;
 
     # Retrieve a specific collection listing that is published to your app
     # 
@@ -11444,7 +14944,7 @@
 
     # Retrieve product listings that are published to your app
     # 
-    remote function retrieveProductListingsThatArePublishedToYourApp(map<string|string[]> headers = {}, string collectionId = "", string productIds = "", string updatedAtMin = "", string limit = "", string handle = "", string page = "", anydata Additional Values, RetrieveProductListingsThatArePublishedToYourAppQueries queries) returns ProductListings|error;
+    remote function retrieveProductListingsThatArePublishedToYourApp(map<string|string[]> headers = {}, string collectionId = "", string productIds = "", string updatedAtMin = "", string limit = "", string handle = "", string page = "", RetrieveProductListingsThatArePublishedToYourAppQueries queries) returns ProductListings|error;
 
     # Retrieve a specific product listing that is published to your app
     # 
@@ -11464,7 +14964,7 @@
 
     # Retrieve product_ids that are published to your app
     # 
-    remote function retrieveProductIdsThatArePublishedToYourApp(map<string|string[]> headers = {}, string limit = "", anydata Additional Values, RetrieveProductIdsThatArePublishedToYourAppQueries queries) returns ProductIdAppResponse|error;
+    remote function retrieveProductIdsThatArePublishedToYourApp(map<string|string[]> headers = {}, string limit = "", RetrieveProductIdsThatArePublishedToYourAppQueries queries) returns ProductIdAppResponse|error;
 
     # Receive a list of all ResourceFeedbacks
     # 
@@ -11476,7 +14976,7 @@
 
     # Retrieves a list of fulfillment orders assigned to the shop locations that are owned by the app
     # 
-    remote function retrievesAListOfFulfillmentOrdersAssignedToTheShopLocationsThatAreOwnedByTheApp(map<string|string[]> headers = {}, string assignmentStatus = "", string locationIds = "", anydata Additional Values, RetrievesAListOfFulfillmentOrdersAssignedToTheShopLocationsThatAreOwnedByTheAppQueries queries) returns FulfillmentOrders|error;
+    remote function retrievesAListOfFulfillmentOrdersAssignedToTheShopLocationsThatAreOwnedByTheApp(map<string|string[]> headers = {}, string assignmentStatus = "", string locationIds = "", RetrievesAListOfFulfillmentOrdersAssignedToTheShopLocationsThatAreOwnedByTheAppQueries queries) returns FulfillmentOrders|error;
 
     # Sends a cancellation request
     # 
@@ -11528,15 +15028,15 @@
 
     # Retrieves fulfillments associated with an order
     # 
-    remote function retrieveFulfillmentsAssociatedWithAnOrder(string orderId, map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string limit = "", string fields = "", string sinceId = "", anydata Additional Values, RetrieveFulfillmentsAssociatedWithAnOrderQueries queries) returns FulfillmentListForOrder|error;
+    remote function retrieveFulfillmentsAssociatedWithAnOrder(string orderId, map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", string limit = "", string fields = "", string sinceId = "", RetrieveFulfillmentsAssociatedWithAnOrderQueries queries) returns FulfillmentListForOrder|error;
 
     # Receive a single Fulfillment
     # 
-    remote function receiveASingleFulfillment(string orderId, string fulfillmentId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, ReceiveASingleFulfillmentQueries queries) returns SingleFulfillment|error;
+    remote function receiveASingleFulfillment(string orderId, string fulfillmentId, map<string|string[]> headers = {}, string fields = "", ReceiveASingleFulfillmentQueries queries) returns SingleFulfillment|error;
 
     # Retrieves a count of fulfillments associated with a specific order
     # 
-    remote function retrieveACountOfFulfillmentsAssociatedWithASpecificOrder(string orderId, map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", anydata Additional Values, RetrieveACountOfFulfillmentsAssociatedWithASpecificOrderQueries queries) returns ObjectCount|error;
+    remote function retrieveACountOfFulfillmentsAssociatedWithASpecificOrder(string orderId, map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string updatedAtMin = "", RetrieveACountOfFulfillmentsAssociatedWithASpecificOrderQueries queries) returns ObjectCount|error;
 
     # Retrieves a list of fulfillment events for a specific fulfillment
     # 
@@ -11608,7 +15108,7 @@
 
     # Receive a list of all FulfillmentServices
     # 
-    remote function receiveAListOfAllFulfillmentServices(map<string|string[]> headers = {}, string scope = "", anydata Additional Values, ReceiveAListOfAllFulfillmentServicesQueries queries) returns FulfillmentServicesList|error;
+    remote function receiveAListOfAllFulfillmentServices(map<string|string[]> headers = {}, string scope = "", ReceiveAListOfAllFulfillmentServicesQueries queries) returns FulfillmentServicesList|error;
 
     # Create a new FulfillmentService
     # 
@@ -11636,7 +15136,7 @@
 
     # Return a list of all disputes
     # 
-    remote function returnAListOfAllDisputes(map<string|string[]> headers = {}, string lastId = "", string sinceId = "", string initiatedAt = "", string status = "", anydata Additional Values, ReturnAListOfAllDisputesQueries queries) returns Disputes|error;
+    remote function returnAListOfAllDisputes(map<string|string[]> headers = {}, string lastId = "", string sinceId = "", string initiatedAt = "", string status = "", ReturnAListOfAllDisputesQueries queries) returns Disputes|error;
 
     # Return a single dispute
     # 
@@ -11660,7 +15160,7 @@
 
     # Return a list of all payouts
     # 
-    remote function returnAListOfAllPayouts(map<string|string[]> headers = {}, string date = "", string dateMin = "", string dateMax = "", string lastId = "", string sinceId = "", string status = "", anydata Additional Values, ReturnAListOfAllPayoutsQueries queries) returns PayoutsList|error;
+    remote function returnAListOfAllPayouts(map<string|string[]> headers = {}, string date = "", string dateMin = "", string dateMax = "", string lastId = "", string sinceId = "", string status = "", ReturnAListOfAllPayoutsQueries queries) returns PayoutsList|error;
 
     # Return a single payout
     # 
@@ -11668,11 +15168,11 @@
 
     # Return a list of all balance transactions
     # 
-    remote function returnAListOfAllBalanceTransactions(map<string|string[]> headers = {}, string payoutId = "", string test = "", string payoutStatus = "", string lastId = "", string sinceId = "", anydata Additional Values, ReturnAListOfAllBalanceTransactionsQueries queries) returns TransactionsListForPayout|error;
+    remote function returnAListOfAllBalanceTransactions(map<string|string[]> headers = {}, string payoutId = "", string test = "", string payoutStatus = "", string lastId = "", string sinceId = "", ReturnAListOfAllBalanceTransactionsQueries queries) returns TransactionsListForPayout|error;
 
     # Receive a list of all Countries
     # 
-    remote function receiveAListOfAllCountries(map<string|string[]> headers = {}, string sinceId = "", string fields = "", anydata Additional Values, ReceiveAListOfAllCountriesQueries queries) returns CountriesList|error;
+    remote function receiveAListOfAllCountries(map<string|string[]> headers = {}, string sinceId = "", string fields = "", ReceiveAListOfAllCountriesQueries queries) returns CountriesList|error;
 
     # Creates a country
     # 
@@ -11680,7 +15180,7 @@
 
     # Retrieves a specific county
     # 
-    remote function retrieveASpecificCounty(string countryId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASpecificCountyQueries queries) returns CountryResponse|error;
+    remote function retrieveASpecificCounty(string countryId, map<string|string[]> headers = {}, string fields = "", RetrieveASpecificCountyQueries queries) returns CountryResponse|error;
 
     # Updates an existing country
     # 
@@ -11704,11 +15204,11 @@
 
     # Retrieves a list of provinces for a country
     # 
-    remote function retrieveAListOfProvincesForACountry(string countryId, map<string|string[]> headers = {}, string sinceId = "", string fields = "", anydata Additional Values, RetrieveAListOfProvincesForACountryQueries queries) returns ProvincesList|error;
+    remote function retrieveAListOfProvincesForACountry(string countryId, map<string|string[]> headers = {}, string sinceId = "", string fields = "", RetrieveAListOfProvincesForACountryQueries queries) returns ProvincesList|error;
 
     # Retrieves a single province for a country
     # 
-    remote function retrieveASingleProvinceForACountry(string countryId, string provinceId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleProvinceForACountryQueries queries) returns SingleProvince|error;
+    remote function retrieveASingleProvinceForACountry(string countryId, string provinceId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleProvinceForACountryQueries queries) returns SingleProvince|error;
 
     # Updates an existing province for a country
     # 
@@ -11720,19 +15220,19 @@
 
     # Receive a list of all ShippingZones
     # 
-    remote function receiveAListOfAllShippingzones(map<string|string[]> headers = {}, string fields = "", anydata Additional Values, ReceiveAListOfAllShippingzonesQueries queries) returns ShippingZonesList|error;
+    remote function receiveAListOfAllShippingzones(map<string|string[]> headers = {}, string fields = "", ReceiveAListOfAllShippingzonesQueries queries) returns ShippingZonesList|error;
 
     # Retrieves the shop's configuration
     # 
-    remote function retrieveTheShopSConfiguration(map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveTheShopSConfigurationQueries queries) returns ShopConfigurations|error;
+    remote function retrieveTheShopSConfiguration(map<string|string[]> headers = {}, string fields = "", RetrieveTheShopSConfigurationQueries queries) returns ShopConfigurations|error;
 
     # Retrieves a list of tender transactions
     # 
-    remote function retrieveAListOfTenderTransactions(map<string|string[]> headers = {}, string processedAtMin = "", string limit = "", string processedAt = "", string sinceId = "", string processedAtMax = "", string order = "", anydata Additional Values, RetrieveAListOfTenderTransactionsQueries queries) returns TenderTransactions|error;
+    remote function retrieveAListOfTenderTransactions(map<string|string[]> headers = {}, string processedAtMin = "", string limit = "", string processedAt = "", string sinceId = "", string processedAtMax = "", string order = "", RetrieveAListOfTenderTransactionsQueries queries) returns TenderTransactions|error;
 
     # Retrieves a list of webhooks
     # 
-    remote function retrieveAListOfWebhooks(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string address = "", string updatedAtMin = "", string limit = "", string topic = "", string fields = "", string sinceId = "", anydata Additional Values, RetrieveAListOfWebhooksQueries queries) returns SubscriptionsList|error;
+    remote function retrieveAListOfWebhooks(map<string|string[]> headers = {}, string createdAtMin = "", string createdAtMax = "", string updatedAtMax = "", string address = "", string updatedAtMin = "", string limit = "", string topic = "", string fields = "", string sinceId = "", RetrieveAListOfWebhooksQueries queries) returns SubscriptionsList|error;
 
     # Create a new Webhook
     # 
@@ -11740,7 +15240,7 @@
 
     # Receive a single Webhook
     # 
-    remote function receiveASingleWebhook(string webhookId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, ReceiveASingleWebhookQueries queries) returns SingleWebhook|error;
+    remote function receiveASingleWebhook(string webhookId, map<string|string[]> headers = {}, string fields = "", ReceiveASingleWebhookQueries queries) returns SingleWebhook|error;
 
     # Modify an existing Webhook
     # 
@@ -11752,11 +15252,11 @@
 
     # Receive a count of all Webhooks
     # 
-    remote function receiveACountOfAllWebhooks(map<string|string[]> headers = {}, string address = "", string topic = "", anydata Additional Values, ReceiveACountOfAllWebhooksQueries queries) returns ObjectCount|error;
+    remote function receiveACountOfAllWebhooks(map<string|string[]> headers = {}, string address = "", string topic = "", ReceiveACountOfAllWebhooksQueries queries) returns ObjectCount|error;
 
     # Retrieves a list of reports
     # 
-    remote function retrieveAListOfReports(map<string|string[]> headers = {}, string updatedAtMax = "", string updatedAtMin = "", string limit = "", string ids = "", string fields = "", string sinceId = "", anydata Additional Values, RetrieveAListOfReportsQueries queries) returns ReportList|error;
+    remote function retrieveAListOfReports(map<string|string[]> headers = {}, string updatedAtMax = "", string updatedAtMin = "", string limit = "", string ids = "", string fields = "", string sinceId = "", RetrieveAListOfReportsQueries queries) returns ReportList|error;
 
     # Creates a new report
     # 
@@ -11764,7 +15264,7 @@
 
     # Retrieves a single report
     # 
-    remote function retrieveASingleReport(string reportId, map<string|string[]> headers = {}, string fields = "", anydata Additional Values, RetrieveASingleReportQueries queries) returns SingleReportResponse|error;
+    remote function retrieveASingleReport(string reportId, map<string|string[]> headers = {}, string fields = "", RetrieveASingleReportQueries queries) returns SingleReportResponse|error;
 
     # Updates a report
     # 
`````
