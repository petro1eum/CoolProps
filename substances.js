const substances = {
  "Water": {
    "name_ru": "Wатер",
    "name_en": "Water",
    "critical_temperature": 647.096,
    "critical_pressure": 22064000.0,
    "critical_density": 322.00000000000006,
    "molar_mass": 0.018015268
  },
  "Nitrogen": {
    "name_ru": "Нитроген",
    "name_en": "Nitrogen",
    "critical_temperature": 126.192,
    "critical_pressure": 3395800.0,
    "critical_density": 313.3,
    "molar_mass": 0.02801348
  },
  "Oxygen": {
    "name_ru": "Оxыген",
    "name_en": "Oxygen",
    "critical_temperature": 154.58100000000002,
    "critical_pressure": 5043000.0,
    "critical_density": 436.143644,
    "molar_mass": 0.0319988
  },
  "Argon": {
    "name_ru": "Аргон",
    "name_en": "Argon",
    "critical_temperature": 150.687,
    "critical_pressure": 4863000.0,
    "critical_density": 535.6,
    "molar_mass": 0.039948
  },
  "Air": {
    "name_ru": "Аир",
    "name_en": "Air",
    "critical_temperature": 132.5306,
    "critical_pressure": 3786000.0,
    "critical_density": 342.68456416799995,
    "molar_mass": 0.02896546
  },
  "Ammonia": {
    "name_ru": "Аммониа",
    "name_en": "Ammonia",
    "critical_temperature": 405.56,
    "critical_pressure": 11363400.0,
    "critical_density": 233.25000192000002,
    "molar_mass": 0.01703052
  },
  "CarbonDioxide": {
    "name_ru": "ЦарбонДиоxиде",
    "name_en": "CarbonDioxide",
    "critical_temperature": 304.1282,
    "critical_pressure": 7377300.0,
    "critical_density": 467.60000128174005,
    "molar_mass": 0.0440098
  },
  "Helium": {
    "name_ru": "Хелиум",
    "name_en": "Helium",
    "critical_temperature": 5.1953000000000005,
    "critical_pressure": 227600.0,
    "critical_density": 72.56717426,
    "molar_mass": 0.004002602
  },
  "Hydrogen": {
    "name_ru": "Хыдроген",
    "name_en": "Hydrogen",
    "critical_temperature": 33.145,
    "critical_pressure": 1296400.0,
    "critical_density": 31.262267039999998,
    "molar_mass": 0.00201588
  },
  "Methane": {
    "name_ru": "Метхане",
    "name_en": "Methane",
    "critical_temperature": 190.564,
    "critical_pressure": 4599200.0,
    "critical_density": 162.6600026784,
    "molar_mass": 0.0160428
  },
  "Ethane": {
    "name_ru": "Етхане",
    "name_en": "Ethane",
    "critical_temperature": 305.322,
    "critical_pressure": 4872200.0,
    "critical_density": 206.18000000673237,
    "molar_mass": 0.03006904
  },
  "Propane": {
    "name_ru": "Пропане",
    "name_en": "Propane",
    "critical_temperature": 369.89,
    "critical_pressure": 4251200.0,
    "critical_density": 220.47810000000004,
    "molar_mass": 0.04409562
  },
  "Butane": {
    "name_ru": "Бутане",
    "name_en": "Butane",
    "critical_temperature": 425.125,
    "critical_pressure": 3796000.0,
    "critical_density": 228.00000000000003,
    "molar_mass": 0.0581222
  },
  "Pentane": {
    "name_ru": "Пентане",
    "name_en": "Pentane",
    "critical_temperature": 469.7000000000001,
    "critical_pressure": 3367518.9947363394,
    "critical_density": 232.0,
    "molar_mass": 0.07214878
  },
  "Hexane": {
    "name_ru": "Хеxане",
    "name_en": "Hexane",
    "critical_temperature": 507.82,
    "critical_pressure": 3044115.328359688,
    "critical_density": 233.19052415999997,
    "molar_mass": 0.08617535999999999
  },
  "Ethylene": {
    "name_ru": "Етхылене",
    "name_en": "Ethylene",
    "critical_temperature": 282.35,
    "critical_pressure": 5041800.0,
    "critical_density": 214.23999999999998,
    "molar_mass": 0.02805376
  },
  "Propylene": {
    "name_ru": "Пропылене",
    "name_en": "Propylene",
    "critical_temperature": 364.211,
    "critical_pressure": 4555000.0,
    "critical_density": 229.62914117999998,
    "molar_mass": 0.04207974
  },
  "Acetone": {
    "name_ru": "Ацетоне",
    "name_en": "Acetone",
    "critical_temperature": 508.1,
    "critical_pressure": 4700000.0,
    "critical_density": 272.971958,
    "molar_mass": 0.05807914
  },
  "R11": {
    "name_ru": "Р11",
    "name_en": "R11",
    "critical_temperature": 471.06,
    "critical_pressure": 4394000.0,
    "critical_density": 565.0,
    "molar_mass": 0.137368
  },
  "R12": {
    "name_ru": "Р12",
    "name_en": "R12",
    "critical_temperature": 385.12,
    "critical_pressure": 4136100.000000001,
    "critical_density": 565.0000000000001,
    "molar_mass": 0.120913
  },
  "R13": {
    "name_ru": "Р13",
    "name_en": "R13",
    "critical_temperature": 301.88,
    "critical_pressure": 3879000.0,
    "critical_density": 582.88122,
    "molar_mass": 0.104459
  },
  "R14": {
    "name_ru": "Р14",
    "name_en": "R14",
    "critical_temperature": 227.51,
    "critical_pressure": 3750000.0,
    "critical_density": 625.6616105292401,
    "molar_mass": 0.0880046
  },
  "R21": {
    "name_ru": "Р21",
    "name_en": "R21",
    "critical_temperature": 451.48,
    "critical_pressure": 5181200.0,
    "critical_density": 526.01379461912,
    "molar_mass": 0.1029227
  },
  "R22": {
    "name_ru": "Р22",
    "name_en": "R22",
    "critical_temperature": 369.295,
    "critical_pressure": 4990000.0,
    "critical_density": 523.8421669600001,
    "molar_mass": 0.086468
  },
  "R23": {
    "name_ru": "Р23",
    "name_en": "R23",
    "critical_temperature": 299.293,
    "critical_pressure": 4832000.0,
    "critical_density": 526.504152,
    "molar_mass": 0.07001385
  },
  "R32": {
    "name_ru": "Р32",
    "name_en": "R32",
    "critical_temperature": 351.255,
    "critical_pressure": 5782000.0,
    "critical_density": 424.00000123039996,
    "molar_mass": 0.052024
  },
  "R41": {
    "name_ru": "Р41",
    "name_en": "R41",
    "critical_temperature": 317.28000000000003,
    "critical_pressure": 5897000.0,
    "critical_density": 316.50615599999986,
    "molar_mass": 0.03403291999999999
  },
  "R114": {
    "name_ru": "Р114",
    "name_en": "R114",
    "critical_temperature": 418.83,
    "critical_pressure": 3257000.0,
    "critical_density": 579.9691372000001,
    "molar_mass": 0.170921
  },
  "R116": {
    "name_ru": "Р116",
    "name_en": "R116",
    "critical_temperature": 293.03000000000003,
    "critical_pressure": 3048000.0,
    "critical_density": 613.32452808,
    "molar_mass": 0.13801182
  },
  "R123": {
    "name_ru": "Р123",
    "name_en": "R123",
    "critical_temperature": 456.831,
    "critical_pressure": 3672000.0,
    "critical_density": 550.003648227,
    "molar_mass": 0.152931
  },
  "R125": {
    "name_ru": "Р125",
    "name_en": "R125",
    "critical_temperature": 339.173,
    "critical_pressure": 3617700.0,
    "critical_density": 573.5822706,
    "molar_mass": 0.1200214
  },
  "R134a": {
    "name_ru": "Р134а",
    "name_en": "R134a",
    "critical_temperature": 374.21,
    "critical_pressure": 4059280.0,
    "critical_density": 511.89995169599996,
    "molar_mass": 0.102032
  },
  "R141b": {
    "name_ru": "Р141б",
    "name_en": "R141b",
    "critical_temperature": 477.5,
    "critical_pressure": 4212000.0,
    "critical_density": 458.55946002000013,
    "molar_mass": 0.11694962
  },
  "R142b": {
    "name_ru": "Р142б",
    "name_en": "R142b",
    "critical_temperature": 410.26,
    "critical_pressure": 4055000.0,
    "critical_density": 445.99694314,
    "molar_mass": 0.10049503
  },
  "R143a": {
    "name_ru": "Р143а",
    "name_en": "R143a",
    "critical_temperature": 345.857,
    "critical_pressure": 3761000.0,
    "critical_density": 431.00006644999996,
    "molar_mass": 0.08404099999999999
  },
  "R152a": {
    "name_ru": "Р152а",
    "name_en": "R152a",
    "critical_temperature": 386.411,
    "critical_pressure": 4520000.0,
    "critical_density": 368.0,
    "molar_mass": 0.066051
  },
  "R218": {
    "name_ru": "Р218",
    "name_en": "R218",
    "critical_temperature": 345.02,
    "critical_pressure": 2640000.0,
    "critical_density": 627.9845622000001,
    "molar_mass": 0.18801933
  },
  "R227EA": {
    "name_ru": "Р227ЕА",
    "name_en": "R227EA",
    "critical_temperature": 374.9,
    "critical_pressure": 2925242.2339447653,
    "critical_density": 594.2508657,
    "molar_mass": 0.17002886
  },
  "R236EA": {
    "name_ru": "Р236ЕА",
    "name_en": "R236EA",
    "critical_temperature": 412.44,
    "critical_pressure": 3420000.0,
    "critical_density": 564.9999999999999,
    "molar_mass": 0.1520384
  },
  "R236FA": {
    "name_ru": "Р236ФА",
    "name_en": "R236FA",
    "critical_temperature": 398.07,
    "critical_pressure": 3200000.0,
    "critical_density": 551.2912384,
    "molar_mass": 0.1520384
  },
  "R245ca": {
    "name_ru": "Р245ца",
    "name_en": "R245ca",
    "critical_temperature": 447.57,
    "critical_pressure": 3940740.488750428,
    "critical_density": 525.4679248,
    "molar_mass": 0.13404794
  },
  "R245fa": {
    "name_ru": "Р245фа",
    "name_en": "R245fa",
    "critical_temperature": 427.01,
    "critical_pressure": 3651000.0,
    "critical_density": 519.4357675,
    "molar_mass": 0.13404794
  },
  "R290": {
    "name_ru": "Р290",
    "name_en": "R290",
    "critical_temperature": 369.89,
    "critical_pressure": 4251200.0,
    "critical_density": 220.47810000000004,
    "molar_mass": 0.04409562
  },
  "R365MFC": {
    "name_ru": "Р365МФЦ",
    "name_en": "R365MFC",
    "critical_temperature": 460.0,
    "critical_pressure": 3266207.0678832484,
    "critical_density": 473.83846399999993,
    "molar_mass": 0.14807452
  },
  "R404A": {
    "name_ru": "Р404А",
    "name_en": "R404A",
    "critical_temperature": 345.27,
    "critical_pressure": 3734800.0,
    "critical_density": 482.16277199999996,
    "molar_mass": 0.0976038
  },
  "R407C": {
    "name_ru": "Р407Ц",
    "name_en": "R407C",
    "critical_temperature": 359.345,
    "critical_pressure": 4631700.0,
    "critical_density": 453.43094,
    "molar_mass": 0.08620359999999999
  },
  "R410A": {
    "name_ru": "Р410А",
    "name_en": "R410A",
    "critical_temperature": 344.494,
    "critical_pressure": 4901200.0,
    "critical_density": 459.0300696,
    "molar_mass": 0.07258540000000001
  },
  "R507A": {
    "name_ru": "Р507А",
    "name_en": "R507A",
    "critical_temperature": 343.765,
    "critical_pressure": 3704900.0,
    "critical_density": 490.74,
    "molar_mass": 0.0988592
  },
  "R600": {
    "name_ru": "Р600",
    "name_en": "R600",
    "critical_temperature": 425.125,
    "critical_pressure": 3796000.0,
    "critical_density": 228.00000000000003,
    "molar_mass": 0.0581222
  },
  "R600a": {
    "name_ru": "Р600а",
    "name_en": "R600a",
    "critical_temperature": 407.817,
    "critical_pressure": 3629000.0,
    "critical_density": 225.5,
    "molar_mass": 0.0581222
  },
  "R717": {
    "name_ru": "Р717",
    "name_en": "R717",
    "critical_temperature": 405.56,
    "critical_pressure": 11363400.0,
    "critical_density": 233.25000192000002,
    "molar_mass": 0.01703052
  },
  "R744": {
    "name_ru": "Р744",
    "name_en": "R744",
    "critical_temperature": 304.1282,
    "critical_pressure": 7377300.0,
    "critical_density": 467.60000128174005,
    "molar_mass": 0.0440098
  },
  "R1233zd(E)": {
    "name_ru": "Р1233зд(Е)",
    "name_en": "R1233zd(E)",
    "critical_temperature": 439.6,
    "critical_pressure": 3623637.7763647954,
    "critical_density": 480.219392,
    "molar_mass": 0.1304944
  },
  "R1234yf": {
    "name_ru": "Р1234ыф",
    "name_en": "R1234yf",
    "critical_temperature": 367.85,
    "critical_pressure": 3382200.0,
    "critical_density": 475.553441976,
    "molar_mass": 0.1140415928
  },
  "R1234ze(E)": {
    "name_ru": "Р1234зе(Е)",
    "name_en": "R1234ze(E)",
    "critical_temperature": 382.52,
    "critical_pressure": 3634936.851021726,
    "critical_density": 489.238433112,
    "molar_mass": 0.1140415928
  },
  "SES36": {
    "name_ru": "СЕС36",
    "name_en": "SES36",
    "critical_temperature": 450.7000000000001,
    "critical_pressure": 2849000.0,
    "critical_density": 517.5799999999999,
    "molar_mass": 0.18485
  },
  "Methanol": {
    "name_ru": "Метханол",
    "name_en": "Methanol",
    "critical_temperature": 512.5,
    "critical_pressure": 8215850.0,
    "critical_density": 273.0,
    "molar_mass": 0.03204216
  },
  "Ethanol": {
    "name_ru": "Етханол",
    "name_en": "Ethanol",
    "critical_temperature": 514.71,
    "critical_pressure": 6268000.0,
    "critical_density": 273.1858492,
    "molar_mass": 0.04606844
  },
  "Neon": {
    "name_ru": "Неон",
    "name_en": "Neon",
    "critical_temperature": 44.4,
    "critical_pressure": 2661630.8085948555,
    "critical_density": 486.3139,
    "molar_mass": 0.020179
  },
  "SulfurHexafluoride": {
    "name_ru": "СулфурХеxафлуориде",
    "name_en": "SulfurHexafluoride",
    "critical_temperature": 318.7232,
    "critical_pressure": 3754983.0,
    "critical_density": 742.3000000000001,
    "molar_mass": 0.1460554192
  },
  "Xenon": {
    "name_ru": "Xенон",
    "name_en": "Xenon",
    "critical_temperature": 289.733,
    "critical_pressure": 5842000.0,
    "critical_density": 1102.8612,
    "molar_mass": 0.131293
  },
  "CarbonMonoxide": {
    "name_ru": "ЦарбонМоноxиде",
    "name_en": "CarbonMonoxide",
    "critical_temperature": 132.86,
    "critical_pressure": 3494000.0,
    "critical_density": 303.909585,
    "molar_mass": 0.0280101
  },
  "HydrogenSulfide": {
    "name_ru": "ХыдрогенСулфиде",
    "name_en": "HydrogenSulfide",
    "critical_temperature": 373.1,
    "critical_pressure": 9000000.0,
    "critical_density": 347.2841672,
    "molar_mass": 0.03408088
  },
  "NitrousOxide": {
    "name_ru": "НитроусОxиде",
    "name_en": "NitrousOxide",
    "critical_temperature": 309.52,
    "critical_pressure": 7245000.0,
    "critical_density": 452.01145600000007,
    "molar_mass": 0.0440128
  },
  "SulfurDioxide": {
    "name_ru": "СулфурДиоxиде",
    "name_en": "SulfurDioxide",
    "critical_temperature": 430.64,
    "critical_pressure": 7886587.6003464125,
    "critical_density": 525.002841,
    "molar_mass": 0.0640638
  }
};