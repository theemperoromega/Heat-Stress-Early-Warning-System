

from collections.abc import Mapping


def risk_tiers(wbtg: float) -> Mapping[str, str]:
    """Returns the risk tier and advice based on the WBGT value safe, caution, danger, extreme"""
    if wbtg < 26.0:
        tier = "Low/Safe"
        advice = "Advice: Normal operations; hydration 0.5L/hr."
    elif wbtg >= 26.0 and wbtg < 28.4:
        tier = "Caution/Moderate temp"
        advice = "Heat strain possible during unaccustomed hard work; hydration 0.75L/hr."
    elif wbtg >= 28.5 and wbtg < 30.9:
        tier = "Danger/High"
        advice = "Advice: Mandatory rest breaks required; active monitoring; hydration 1.0 L/hr."
    else:
        tier = "Extreme/Hazardous"
        advice = "Advice: Strenuous work suspended; active cooling required; electrolyte replacement mandatory"

    return {
        "tier": tier,
        "advice": advice
    }


def ExertionLevel(wbgt: float):
    #Returns the exertion level based on the WBGT value
    if wbgt < 200:
        return "Light"
    elif wbgt > 200 and wbgt <= 400:
        return "Moderate"
    elif wbgt > 400 and wbgt <= 500:
        return "Heavy"
    else:
        return "Very Heavy"


  #Allowable work alllocation per hour

  
def Work-Rest Cycle(exertion_level: str, wbgt: float):
    #Returns the work-rest cycle based on the WBGT value
    if exertion_level == "Light" and  Acc_status = "Acclimatized":
        if wbgt <= 31.0:
            return "Work 60 min, Rest 0 min"
        elif wbgt >= 26.0 and wbgt < 28.4:
            return "Work 45 min, Rest 15 min"  
        elif  wbgt >= 26.0 and wbgt < 28.4:
            return "Work 45 min, Rest 15 min"
        elif wbgt >= 28.5 and wbgt < 30.9:
            return "Work 30 min, Rest 30 min"
    elif exertion_level == "Moderate":
        if wbgt >= 26.0 and wbgt < 28.4:
            return "Work 45 min, Rest 15 min"
        elif wbgt >= 28.5 and wbgt < 30.9:
            return "Work 30 min, Rest 30 min"
    elif exertion_level == "Heavy":
        if wbgt >= 28.5 and wbgt < 30.9:
            return "Work 15 min, Rest 45 min"
        return "Work 15 min, Rest 45 min"
    else:














        if exertion_level == "Very Heavy" and acc_status == "Unacclimatized":
            if wbgt >= 30.9:
                return "Work 0 min, Rest 60 min"
        return "Prohibited"
        
""
