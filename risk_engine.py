from collections.abc import Mapping

#Risk_tiers
# Returns the risk tier and advice based on the WBGT value safe, caution, danger, extreme

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

# ExertionLevel
# Returns the exertion level based on the WBGT value

def ExertionLevel(wbgt: float):
    
    if wbgt < 200:
        return "Light"
    elif wbgt > 200 and wbgt <= 400:
        return "Moderate"
    elif wbgt > 400 and wbgt <= 500:
        return "Heavy"
    else:
        return "Very Heavy"


# Work_Rest_Cycle
# Returns the allowable work allocation per hour

  

    
def work_rest_cycle(exertion_level: str, wbgt: float, acc_status: str) -> str:

#Returns the work-rest cycle based on the exertion level and WBGT value"""

# LIGHT

    if exertion_level == "Light":

        if acc_status == "Acclimatized":
            if wbgt <= 31.0:
                return "45 min Work / 15 min Rest"
            elif wbgt <= 32.0:
                return "30 min Work / 30 min Rest"
            elif wbgt <= 32.5:
                return "15 min Work / 45 min Rest"
            else:
                return "Stop Work"



        elif acc_status == "Unacclimatized":
            if wbgt <= 31.0:
                return "Work 60 min, Rest 0 min"
            elif wbgt >= 26.0 and wbgt < 28.4:
                return "Work 45 min, Rest 15 min"  
            elif  wbgt >= 26.0 and wbgt < 28.4:
                return "Work 45 min, Rest 15 min"
            elif wbgt >= 28.5 and wbgt < 30.9:
                return "Work 30 min, Rest 30 min"
            elif wbgt >= 30.9:
                return "Work 15 min, Rest 45 min"
            else:
                return "Stop Work"
    
    # MODERATE 

    if exertion_level == "Moderate":
        
        if   acc_status == "Acclimatized":
            if wbgt <= 31.0:
                return "Work 60 min, Rest 0 min"
            elif wbgt >= 26.0 and wbgt < 28.4:
                return "Work 45 min, Rest 15 min"  
            elif  wbgt >= 26.0 and wbgt < 28.4:
                return "Work 45 min, Rest 15 min"
            elif wbgt >= 28.5 and wbgt < 30.9:
                return "Work 30 min, Rest 30 min"
            elif wbgt >= 30.9:
                return "Work 15 min, Rest 45 min"
            else:
                return "Stop Work"



        elif acc_status == "Unacclimatized":
            if wbgt <= 31.0:
                return "Work 60 min, Rest 0 min"
            elif wbgt >= 26.0 and wbgt < 28.4:
                return "Work 45 min, Rest 15 min"  
            elif  wbgt >= 26.0 and wbgt < 28.4:
                return "Work 45 min, Rest 15 min"
            elif wbgt >= 28.5 and wbgt < 30.9:
                return "Work 30 min, Rest 30 min"
            elif wbgt >= 30.9:
                return "Work 15 min, Rest 45 min"
            else:
                return "Stop Work"

    if exertion_level == "Heavy":
        
        if   acc_status == "Acclimatized":
            if wbgt <= 31.0:
                return "Work 60 min, Rest 0 min"
            elif wbgt >= 26.0 and wbgt < 28.4:
                return "Work 45 min, Rest 15 min"  
            elif  wbgt >= 26.0 and wbgt < 28.4:
                return "Work 45 min, Rest 15 min"
            elif wbgt >= 28.5 and wbgt < 30.9:
                return "Work 30 min, Rest 30 min"
            elif wbgt >= 30.9:
                return "Work 15 min, Rest 45 min"
            else:
                return "Stop Work"



        elif acc_status == "Unacclimatized":
            if wbgt <= 31.0:
                return "Work 60 min, Rest 0 min"
            elif wbgt >= 26.0 and wbgt < 28.4:
                return "Work 45 min, Rest 15 min"  
            elif  wbgt >= 26.0 and wbgt < 28.4:
                return "Work 45 min, Rest 15 min"
            elif wbgt >= 28.5 and wbgt < 30.9:
                return "Work 30 min, Rest 30 min"
            elif wbgt >= 30.9:
                return "Work 15 min, Rest 45 min"
            else:
                return "Stop Work"
    
    if exertion_level == "Very Heavy":
        
        if   acc_status == "Acclimatized":
            if wbgt <= 31.0:
                return "Work 60 min, Rest 0 min"
            elif wbgt >= 26.0 and wbgt < 28.4:
                return "Work 45 min, Rest 15 min"  
            elif  wbgt >= 26.0 and wbgt < 28.4:
                return "Work 45 min, Rest 15 min"
            elif wbgt >= 28.5 and wbgt < 30.9:
                return "Work 30 min, Rest 30 min"
            elif wbgt >= 30.9:
                return "Work 15 min, Rest 45 min"
            else:
                return "Stop Work"



        elif acc_status == "Unacclimatized":
            if wbgt <= 31.0:
                return "Work 60 min, Rest 0 min"
            elif wbgt >= 26.0 and wbgt < 28.4:
                return "Work 45 min, Rest 15 min"  
            elif  wbgt >= 26.0 and wbgt < 28.4:
                return "Work 45 min, Rest 15 min"
            elif wbgt >= 28.5 and wbgt < 30.9:
                return "Work 30 min, Rest 30 min"
            elif wbgt >= 30.9:
                return "Work 15 min, Rest 45 min"
            else:
                return "Stop Work"