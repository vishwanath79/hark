"""Climate change collection for the hark MCP server.

Facts sourced from IPCC AR6 (2021-2023), NASA, NOAA, WMO, and IEA.
Numbers reflect published values as of 2023-2024.
"""

QUOTES: dict = {
    "co2_emissions": {
        "title": "Carbon Dioxide Emissions",
        "summary": (
            "Atmospheric CO2 is at its highest level in at least 2 million years. "
            "Fossil fuel burning is the dominant driver. Annual emissions continue "
            "to rise, though growth has slowed in some regions. The concentration "
            "and the cumulative total both matter for warming."
        ),
        "quotes": [
            {
                "text": "Global annual average atmospheric CO2 concentration reached 421.08 parts per million in 2024, up from about 280 ppm before the industrial era.",
                "speaker": "NOAA Mauna Loa Observatory",
                "themes": ["emissions", "carbon", "atmosphere"],
            },
            {
                "text": "Global fossil CO2 emissions reached 37.4 GtCO2 in 2023, a record high.",
                "speaker": "Global Carbon Project",
                "themes": ["fossil_fuels", "emissions", "records"],
            },
            {
                "text": "Cumulative human-caused CO2 emissions since 1850 total approximately 2500 GtCO2. About 1000 GtCO2 remain in the atmosphere.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["cumulative", "carbon_budget", "history"],
            },
            {
                "text": "The remaining carbon budget to limit warming to 1.5C with 50% likelihood is about 500 GtCO2 as of the start of 2020.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["carbon_budget", "targets", "mitigation"],
            },
            {
                "text": "CO2 levels are higher than at any point in at least 2 million years.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["geological_context", "records", "atmosphere"],
            },
            {
                "text": "China was the largest national emitter of CO2 from fossil fuels in 2023, followed by the United States and India.",
                "speaker": "Global Carbon Project",
                "themes": ["national", "fossil_fuels", "geography"],
            },
        ],
    },
    "temperature_records": {
        "title": "Global Temperature Records",
        "summary": (
            "Global surface temperature has risen about 1.1C above the pre-industrial "
            "average. The last decade contained the ten warmest years on record. "
            "2023 was the warmest year observed, and 2024 matched or exceeded it."
        ),
        "quotes": [
            {
                "text": "The 2011-2020 decade was 1.09C warmer than the 1850-1900 pre-industrial baseline.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["warming", "baseline", "decadal"],
            },
            {
                "text": "2023 was the warmest year on record, with global average temperature 1.45C above the pre-industrial baseline.",
                "speaker": "World Meteorological Organization",
                "themes": ["records", "warming", "annual"],
            },
            {
                "text": "The ten warmest years in the instrumental record have all occurred in the last decade.",
                "speaker": "NASA GISS",
                "themes": ["records", "decadal", "warming"],
            },
            {
                "text": "Global average sea surface temperature hit record highs in 2023 and early 2024.",
                "speaker": "NOAA",
                "themes": ["ocean", "records", "warming"],
            },
            {
                "text": "Arctic temperatures have warmed at roughly twice the rate of the global average since 1900.",
                "speaker": "NASA",
                "themes": ["arctic", "amplification", "polar"],
            },
            {
                "text": "It is unequivocal that human influence has warmed the atmosphere, ocean, and cryosphere.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["attribution", "human_influence", "consensus"],
            },
            {
                "text": "Each of the last four decades has been warmer than any decade that preceded it since 1850.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["decadal", "trend", "warming"],
            },
        ],
    },
    "sea_level": {
        "title": "Sea Level Rise",
        "summary": (
            "Global mean sea level has risen about 20 cm since 1900. The rate has "
            "accelerated, driven by thermal expansion of seawater and melting land "
            "ice. Current satellite-era rise is about 3.4 mm per year."
        ),
        "quotes": [
            {
                "text": "Global mean sea level rose about 20 cm between 1901 and 2018.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["sea_level", "history", "observations"],
            },
            {
                "text": "The rate of global mean sea level rise increased from 1.3 mm per year over 1901-1971 to 3.7 mm per year over 2006-2018.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["acceleration", "rate", "satellite_era"],
            },
            {
                "text": "Satellite altimetry shows global mean sea level rising at about 3.4 mm per year since 1993.",
                "speaker": "NASA",
                "themes": ["satellites", "rate", "observations"],
            },
            {
                "text": "Thermal expansion of ocean water contributed about half of observed sea level rise during 1971-2018.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["thermal_expansion", "ocean", "causes"],
            },
            {
                "text": "Ice loss from Greenland contributed about 0.6 mm per year to sea level rise over 2006-2018, and Antarctica about 0.4 mm per year.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["ice_sheets", "greenland", "antarctica"],
            },
            {
                "text": "Sea level rise of 0.3 to 1.0 m is projected by 2100 under intermediate emissions scenarios.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["projections", "scenarios", "future"],
            },
        ],
    },
    "extreme_weather": {
        "title": "Extreme Weather Trends",
        "summary": (
            "Climate change is intensifying many extremes. Heatwaves are more "
            "frequent and hotter. Heavy precipitation events are stronger. "
            "Tropical cyclones are getting more intense on average. Attribution "
            "science now links specific events to warming."
        ),
        "quotes": [
            {
                "text": "Human-induced climate change has increased the frequency and intensity of heavy precipitation events since the 1950s.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["precipitation", "attribution", "extremes"],
            },
            {
                "text": "Hot extremes have increased over land in most regions since the 1950s, and cold extremes have decreased.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["heatwaves", "trend", "attribution"],
            },
            {
                "text": "The proportion of intense tropical cyclones (Category 4-5) has increased over the past four decades.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["hurricanes", "cyclones", "intensity"],
            },
            {
                "text": "The area burned by wildfires has increased in parts of western North America and Australia over recent decades.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["wildfires", "drought", "regional"],
            },
            {
                "text": "Agricultural and ecological droughts have increased in some regions due to increased evapotranspiration.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["drought", "agriculture", "regional"],
            },
            {
                "text": "Concurrent extremes, such as heat and drought occurring together, have become more frequent since the 1950s.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["compound_events", "heat", "drought"],
            },
        ],
    },
    "ipcc_findings": {
        "title": "IPCC AR6 Key Findings",
        "summary": (
            "The Sixth Assessment Report (2021-2023) is the most comprehensive "
            "climate assessment to date. It strengthens attribution, narrows "
            "climate sensitivity estimates, and links impacts to specific warming "
            "levels. It identifies a narrow window to limit warming to 1.5C."
        ),
        "quotes": [
            {
                "text": "Human-induced warming reached approximately 1.1C above pre-industrial levels by 2011-2020.",
                "speaker": "IPCC AR6 SYR",
                "themes": ["attribution", "warming", "current_state"],
            },
            {
                "text": "Equilibrium climate sensitivity is now estimated at 3.0C, with a likely range of 2.5C to 4.0C.",
                "speaker": "IPCC AR6 WGI",
                "themes": ["sensitivity", "science", "projections"],
            },
            {
                "text": "Limiting warming to 1.5C requires global greenhouse gas emissions to peak before 2025 and fall 43% by 2030 relative to 2019.",
                "speaker": "IPCC AR6 WGIII",
                "themes": ["mitigation", "targets", "pathways"],
            },
            {
                "text": "Net zero CO2 emissions must be reached in the early 2050s to limit warming to 1.5C with no or limited overshoot.",
                "speaker": "IPCC AR6 WGIII",
                "themes": ["net_zero", "targets", "mitigation"],
            },
            {
                "text": "Impacts and risks increase with every increment of warming. Some are irreversible, such as ice sheet collapse.",
                "speaker": "IPCC AR6 WGII",
                "themes": ["risks", "tipping_points", "irreversibility"],
            },
            {
                "text": "Adaptation and mitigation actions are underway in all regions and sectors, but current pace and scale are insufficient.",
                "speaker": "IPCC AR6 SYR",
                "themes": ["adaptation", "policy", "gaps"],
            },
            {
                "text": "Methane emissions reductions of about 50% by 2030 are a key component of 1.5C-compatible pathways.",
                "speaker": "IPCC AR6 WGIII",
                "themes": ["methane", "non_co2", "mitigation"],
            },
        ],
    },
    "renewable_energy": {
        "title": "Renewable Energy Growth",
        "summary": (
            "Renewable energy capacity is expanding faster than any other source. "
            "Solar and wind dominate new installations. Costs have fallen sharply. "
            "Even so, fossil fuels still supply most of global primary energy, and "
            "the transition pace must accelerate to meet climate goals."
        ),
        "quotes": [
            {
                "text": "Global renewable power capacity additions reached about 510 GW in 2023, a 50% increase over 2022.",
                "speaker": "International Energy Agency",
                "themes": ["capacity", "growth", "records"],
            },
            {
                "text": "Solar PV module costs have fallen by about 90% since 2010.",
                "speaker": "International Renewable Energy Agency",
                "themes": ["solar", "costs", "trend"],
            },
            {
                "text": "Renewables are projected to overtake coal as the largest source of global electricity generation by early 2025.",
                "speaker": "International Energy Agency",
                "themes": ["electricity", "coal", "milestone"],
            },
            {
                "text": "China accounted for nearly 60% of new global renewable capacity additions in 2023.",
                "speaker": "International Energy Agency",
                "themes": ["china", "capacity", "geography"],
            },
            {
                "text": "Fossil fuels still supplied about 80% of global primary energy in 2023.",
                "speaker": "Statistical Review of World Energy",
                "themes": ["fossil_fuels", "share", "current_state"],
            },
            {
                "text": "Tripling global renewable capacity by 2030 is a key pledge of the COP28 climate summit.",
                "speaker": "COP28 UAE Consensus",
                "themes": ["targets", "policy", "international"],
            },
        ],
    },
}