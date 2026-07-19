
# Dictionaries = store key value pair , of diff types of data 
monthConversions = {
    "Jan" : "January",
    "Feb" : "February", 
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(monthConversions["Mar"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Lov", "Not a valid key"))