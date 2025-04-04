import json
import time
from CoolProp.CoolProp import PropsSI, get_global_param_string

# Расширенные русские названия веществ с правильными n-префиксами
russian_names = {
    "Water": "Вода",
    "Nitrogen": "Азот",
    "Oxygen": "Кислород",
    "Argon": "Аргон",
    "Air": "Воздух",
    "Ammonia": "Аммиак",
    "CarbonDioxide": "Углекислый газ",
    "Helium": "Гелий",
    "Hydrogen": "Водород",
    "Methane": "Метан",
    "n-Propane": "н-Пропан",
    "Propane": "Пропан",
    "n-Butane": "н-Бутан",
    "Butane": "Бутан",
    "n-Pentane": "н-Пентан",
    "Pentane": "Пентан",
    "n-Hexane": "н-Гексан",
    "Hexane": "Гексан",
    "n-Heptane": "н-Гептан",
    "Heptane": "Гептан",
    "n-Octane": "н-Октан",
    "Octane": "Октан",
    "n-Nonane": "н-Нонан",
    "Nonane": "Нонан",
    "n-Decane": "н-Декан",
    "Decane": "Декан",
    "n-Undecane": "н-Ундекан",
    "Undecane": "Ундекан",
    "n-Dodecane": "н-Додекан",
    "Dodecane": "Додекан",
    "Ethane": "н-Этан",
    "Ethylene": "Этилен",
    "Propylene": "Пропилен",
    "Acetone": "Ацетон",
    "R11": "R11 (Трихлорфторметан)",
    "R12": "R12 (Дихлордифторметан)",
    "R13": "R13 (Хлортрифторметан)",
    "R14": "R14 (Тетрафторметан)",
    "R21": "R21 (Дихлорфторметан)",
    "R22": "R22 (Хлордифторметан)",
    "R23": "R23 (Трифторметан)",
    "R32": "R32 (Дифторметан)",
    "R40": "R40 (Хлорметан)",
    "R41": "R41 (Фторметан)",
    "R113": "R113 (Трихлортрифторэтан)",
    "R114": "R114 (Дихлортетрафторэтан)",
    "R115": "R115 (Хлорпентафторэтан)",
    "R116": "R116 (Гексафторэтан)",
    "R123": "R123 (Дихлортрифторэтан)",
    "R124": "R124 (Хлортетрафторэтан)",
    "R125": "R125 (Пентафторэтан)",
    "R134a": "R134a (1,1,1,2-Тетрафторэтан)",
    "R141b": "R141b (1,1-Дихлор-1-фторэтан)",
    "R142b": "R142b (1-Хлор-1,1-дифторэтан)",
    "R143a": "R143a (1,1,1-Трифторэтан)",
    "R152A": "R152A (1,1-Дифторэтан)",
    "R161": "R161 (Фторэтан)",
    "R218": "R218 (Октафторпропан)",
    "R227EA": "R227EA (1,1,1,2,3,3,3-Гептафторпропан)",
    "R236EA": "R236EA (1,1,1,2,3,3-Гексафторпропан)",
    "R236FA": "R236FA (1,1,1,3,3,3-Гексафторпропан)",
    "R245ca": "R245ca (1,1,2,2,3-Пентафторпропан)",
    "R245fa": "R245fa (1,1,1,3,3-Пентафторпропан)",
    "R365MFC": "R365MFC (1,1,1,3,3-Пентафторбутан)",
    "R404A": "R404A (Смесь R125/R143a/R134a)",
    "R407C": "R407C (Смесь R32/R125/R134a)",
    "R410A": "R410A (Смесь R32/R125)",
    "R507A": "R507A (Смесь R125/R143a)",
    "R1233zd(E)": "R1233zd(E) (транс-1-Хлор-3,3,3-трифторпропен)",
    "R1234yf": "R1234yf (2,3,3,3-Тетрафторпропен)",
    "R1234ze(E)": "R1234ze(E) (транс-1,3,3,3-Тетрафторпропен)",
    "R1234ze(Z)": "R1234ze(Z) (цис-1,3,3,3-Тетрафторпропен)",
    "R1243zf": "R1243zf (3,3,3-Трифторпропен)",
    "R1336MZZE": "R1336MZZE ((Z)-1,1,1,4,4,4-Гексафтор-2-бутен)",
    "SES36": "SES36 (Смесь R365mfc/PFPE)",
    "Methanol": "Метанол",
    "Ethanol": "Этанол",
    "Neon": "Неон",
    "SulfurHexafluoride": "Гексафторид серы",
    "Xenon": "Ксенон",
    "CarbonMonoxide": "Монооксид углерода (CO)",
    "HydrogenSulfide": "Сероводород",
    "NitrousOxide": "Закись азота (N₂O)",
    "SulfurDioxide": "Диоксид серы",
    "Acetylene": "Ацетилен",
    "Benzene": "Бензол",
    "Toluene": "Толуол",
    "Cyclopentane": "Циклопентан",
    "CycloHexane": "Циклогексан",
    "CycloPropane": "Циклопропан",
    "Deuterium": "Дейтерий",
    "ParaHydrogen": "Пара-водород",
    "OrthoHydrogen": "Орто-водород",
    "HeavyWater": "Тяжелая вода (D₂O)",
    "Isohexane": "Изогексан",
    "IsoButane": "Изобутан",
    "IsoButene": "Изобутен",
    "Isopentane": "Изопентан",
    "Krypton": "Криптон",
    "MM": "Гексаметилдисилоксан",
    "MDM": "Октаметилтрисилоксан",
    "MD2M": "Декаметилтетрасилоксан",
    "MD3M": "Додекаметилпентасилоксан",
    "MD4M": "Тетрадекаметилгексасилоксан",
    "D4": "Октаметилциклотетрасилоксан",
    "D5": "Декаметилциклопентасилоксан",
    "D6": "Додекаметилциклогексасилоксан",
    "Neopentane": "Неопентан",
    "OrthoDeuterium": "Орто-дейтерий",
    "ParaDeuterium": "Пара-дейтерий",
    "DimethylCarbonate": "Диметилкарбонат",
    "DimethylEther": "Диметиловый эфир",
    "EthylBenzene": "Этилбензол",
    "DiethylEther": "Диэтиловый эфир",
    "Fluorine": "Фтор",
    "HFE143m": "HFE143m (Метилтрифторметиловый эфир)",
    "HydrogenChloride": "Хлороводород",
    "Dichloroethane": "Дихлорэтан",
    "MethylLinoleate": "Метиллинолеат",
    "MethylLinolenate": "Метиллиноленат",
    "MethylOleate": "Метилолеат",
    "MethylPalmitate": "Метилпальмитат",
    "MethylStearate": "Метилстеарат",
    "Novec649": "Novec649 (Перфторкетон C6F12O)",
    "RC318": "RC318 (Октафторциклобутан)",
    "R13I1": "R13I1 (Трифториодометан)",
    "EthyleneOxide": "Этиленоксид",
    "CarbonylSulfide": "Карбонилсульфид",
    "o-Xylene": "о-Ксилол",
    "m-Xylene": "м-Ксилол",
    "p-Xylene": "п-Ксилол",
    "1-Butene": "1-Бутен",
    "cis-2-Butene": "цис-2-Бутен",
    "trans-2-Butene": "транс-2-Бутен",
    "Propyne": "Пропин"
}

def get_fluid_list():
    """Получает список всех доступных флюидов из CoolProp"""
    try:
        fluid_list_str = get_global_param_string('FluidsList')
        return [fluid.strip() for fluid in fluid_list_str.split(',')]
    except Exception as e:
        print(f"Не удалось получить список флюидов: {str(e)}")
        return []

# Определяем диапазоны температур и давлений для расчетов
def get_temperature_pressure_ranges(fluid):
    try:
        # Получаем критические параметры и тройные точки
        T_crit = PropsSI('Tcrit', fluid)
        P_crit = PropsSI('pcrit', fluid)
        T_triple = PropsSI('Ttriple', fluid)
        
        # Определяем диапазоны для температур (от тройной точки до близко к критической)
        # Избегаем приближения слишком близко к критической точке для численной стабильности
        T_min = T_triple + 1  # Немного выше тройной точки
        T_max = min(T_crit * 0.95, 500)  # Не более 95% от критической или 500K
        
        # Генерируем 5 температурных точек в логарифмической шкале
        temp_range = [T_min]
        
        if T_max > T_min:
            # Линейные точки между мин и макс
            step = (T_max - T_min) / 4
            for i in range(1, 4):
                temp_range.append(T_min + i * step)
            temp_range.append(T_max)
        
        # Определяем диапазоны давлений
        # Используем 5 точек: низкое давление, 25%, 50%, 75% и 90% от критического
        p_range = [1e5]  # Атмосферное давление (примерно)
        if P_crit > 1e5:
            p_step = (P_crit - 1e5) / 4
            for i in range(1, 4):
                p_range.append(1e5 + i * p_step)
            p_range.append(P_crit * 0.9)  # 90% от критического
        
        return temp_range, p_range
    
    except Exception as e:
        print(f"Ошибка при определении диапазонов для {fluid}: {str(e)}")
        # Возвращаем стандартные диапазоны в случае ошибки
        return [250, 300, 350, 400, 450], [1e5, 5e5, 1e6, 2e6, 5e6]

# Функция для расчета свойств вещества при различных температурах и давлениях
def calculate_properties_at_conditions(fluid):
    try:
        # Получаем базовые критические свойства
        properties = {
            "critical_temperature": PropsSI('Tcrit', fluid),
            "critical_pressure": PropsSI('pcrit', fluid),
            "critical_density": PropsSI('rhocrit', fluid),
            "molar_mass": PropsSI('M', fluid),
            "triple_temperature": PropsSI('Ttriple', fluid),
            "triple_pressure": PropsSI('ptriple', fluid),
            "acentric_factor": PropsSI('acentric', fluid),
            "gas_constant": PropsSI('gas_constant', fluid)
        }
        
        # Получаем диапазоны температур и давлений для этого вещества
        temp_range, pressure_range = get_temperature_pressure_ranges(fluid)
        
        # Создаем структуру для хранения свойств при разных условиях
        properties["temperature_pressure_data"] = {}
        
        # Рассчитываем свойства для каждой комбинации температуры и давления
        for temperature in temp_range:
            temp_key = f"T{temperature:.2f}"
            properties["temperature_pressure_data"][temp_key] = {}
            
            for pressure in pressure_range:
                press_key = f"P{pressure:.2f}"
                
                try:
                    # Проверяем, находится ли точка в допустимой области
                    # Используем метод PropsSI с входными параметрами T и P
                    density = PropsSI('D', 'T', temperature, 'P', pressure, fluid)
                    
                    # Если плотность допустима, то вычисляем другие свойства
                    properties["temperature_pressure_data"][temp_key][press_key] = {
                        "temperature": temperature,
                        "pressure": pressure,
                        "density": density,
                        "specific_heat_cp": PropsSI('C', 'T', temperature, 'P', pressure, fluid),
                        "specific_heat_cv": PropsSI('O', 'T', temperature, 'P', pressure, fluid),
                        "conductivity": PropsSI('L', 'T', temperature, 'P', pressure, fluid),
                        "viscosity": PropsSI('V', 'T', temperature, 'P', pressure, fluid),
                        "enthalpy": PropsSI('H', 'T', temperature, 'P', pressure, fluid),
                        "entropy": PropsSI('S', 'T', temperature, 'P', pressure, fluid),
                        "speed_of_sound": PropsSI('A', 'T', temperature, 'P', pressure, fluid),
                        "phase": get_phase(fluid, temperature, pressure)
                    }
                    
                except Exception as prop_error:
                    # Если точка находится за пределами допустимой области, 
                    # добавляем информацию об ошибке
                    properties["temperature_pressure_data"][temp_key][press_key] = {
                        "temperature": temperature,
                        "pressure": pressure,
                        "error": str(prop_error)
                    }
        
        return properties
        
    except Exception as e:
        print(f"Ошибка при расчёте свойств для {fluid}: {str(e)}")
        return None

# Функция для определения фазы вещества
def get_phase(fluid, T, P):
    try:
        # Получаем фазовый флаг от CoolProp
        phase_flag = PropsSI('Phase', 'T', T, 'P', P, fluid)
        
        # Интерпретируем фазовый флаг
        phase_map = {
            0: "неопределенная",
            1: "жидкость",
            2: "пар/газ",
            3: "сверхкритическая жидкость",
            4: "сверхкритический газ",
            5: "сверхкритическая фаза",
            6: "двухфазная область"
        }
        
        return phase_map.get(phase_flag, f"неизвестная ({phase_flag})")
        
    except Exception as e:
        return f"ошибка определения фазы: {str(e)}"

# Получаем список всех доступных веществ
print("Получение списка всех доступных веществ...")
all_fluids = get_fluid_list()
print(f"Найдено {len(all_fluids)} веществ")

# Словарь для сохранения данных о веществах
substances_data = {}
total_fluids = len(all_fluids)
processed = 0

print(f"Расчет свойств для {total_fluids} веществ при различных температурах и давлениях...")

# Обработка каждого вещества
for fluid in all_fluids:
    processed += 1
    if processed % 5 == 0 or processed == total_fluids:
        print(f"Обработано {processed}/{total_fluids} веществ ({processed/total_fluids*100:.1f}%)")
    
    # Получаем и рассчитываем свойства вещества при различных условиях
    properties = calculate_properties_at_conditions(fluid)
    
    if properties:
        # Получаем русское название (если есть)
        ru_name = russian_names.get(fluid, fluid)
        
        # Сохраняем данные о веществе
        substances_data[fluid] = {
            "name_ru": ru_name,
            "name_en": fluid,
            **properties
        }
    
    # Небольшая пауза, чтобы не перегружать систему
    time.sleep(0.01)

print(f"Расчеты завершены. Успешно получены данные для {len(substances_data)} веществ.")

# Создаем файл с полным списком веществ и их названий
print("\nПолный список обработанных веществ:")
with open('substances_list.txt', 'w', encoding='utf-8') as f:
    for i, (fluid, data) in enumerate(substances_data.items(), 1):
        substance_info = f"{i}. {fluid} - {data['name_ru']}"
        print(substance_info)
        f.write(substance_info + "\n")

# Создаем JavaScript-объект для вставки в веб-приложение
js_object = "const substances = {\n"
for fluid, data in substances_data.items():
    js_object += f'  "{fluid}": {{\n'
    
    # Добавляем названия
    js_object += f'    "name_ru": "{data["name_ru"]}",\n'
    js_object += f'    "name_en": "{data["name_en"]}",\n'
    
    # Добавляем критические параметры
    for key, value in data.items():
        if key not in ["name_ru", "name_en", "temperature_pressure_data"] and value is not None:
            js_object += f'    "{key}": {value},\n'
    
    # Добавляем данные для различных температур и давлений
    js_object += f'    "temperature_pressure_data": {{\n'
    
    for temp_key, pressure_data in data.get("temperature_pressure_data", {}).items():
        js_object += f'      "{temp_key}": {{\n'
        
        for press_key, props in pressure_data.items():
            js_object += f'        "{press_key}": {{\n'
            
            # Добавляем все свойства для данной комбинации T-P
            for prop_key, prop_value in props.items():
                if isinstance(prop_value, str):
                    js_object += f'          "{prop_key}": "{prop_value}",\n'
                else:
                    js_object += f'          "{prop_key}": {prop_value},\n'
            
            # Удаляем последнюю запятую и закрываем объект давления
            js_object = js_object.rstrip(",\n") + "\n        },\n"
        
        # Удаляем последнюю запятую и закрываем объект температуры
        js_object = js_object.rstrip(",\n") + "\n      },\n"
    
    # Удаляем последнюю запятую и закрываем объект temperature_pressure_data
    js_object = js_object.rstrip(",\n") + "\n    }\n"
    
    # Закрываем объект вещества
    js_object += "  },\n"

# Закрываем объект всех веществ
js_object = js_object.rstrip(",\n") + "\n};"

# Создаем файл с JavaScript-объектом
with open('substances_data.js', 'w', encoding='utf-8') as f:
    f.write(js_object)

# Создаем файл с JSON-данными для более универсального использования
with open('substances_data.json', 'w', encoding='utf-8') as f:
    json.dump(substances_data, f, ensure_ascii=False, indent=2)

print(f"\nВсего веществ: {len(substances_data)}")
print(f"Полный JavaScript-объект сохранен в файл substances_data.js")
print(f"Данные также сохранены в формате JSON в файл substances_data.json")
print("Данные содержат свойства веществ при различных температурах и давлениях.")
