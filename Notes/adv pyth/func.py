def officers_details(**kwargs):
    """prints out the details of officers"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
officers_details(name = "Adams", age = 20 , rank = "copra", location = "Lagos")

