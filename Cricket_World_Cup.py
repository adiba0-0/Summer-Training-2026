Cricket_World_Cup={

    2021: {
        "Year": "2021",
        "Teams": ["India", "Australia", "England", "New Zealand", "West Indies", "South Africa", "Bangladesh", "Afghanistan", "Sri Lanka"],
        "Captain": ["Virat Kohli", "Aaron Finch", "Eoin Morgan", "Kieran Pollard", "Temba Bavuma", "Mahmudullah", "Mohammad Nabi", "Dasun Shanaka", "Sri Lanka"],
        "Winner": "AUSTRALIA!"
    },

    2023: {
        "Year": "2023",
        "Teams": ["India", "Australia", "England", "New Zealand", "Netherlands", "South Africa", "Bangladesh", "Sri Lanka"],
        "Captain": ["Rohit Sharma", "Pat Cummins", "Jos Buttler", "Kane Williamson", "Temba Bavuma", "Shakib Al Hasan", " Hashmatullah Shahidi", "Dasun Shanaka"],
        "Winner": "AUSTRALIA!"
    }

}

i = int(input("Enter the year of world cup you want: "))
if i in Cricket_World_Cup:
    print("Teams: ", Cricket_World_Cup[i]["Teams"])
    print("Captains: ", Cricket_World_Cup[i]["Captain"])
    print("Winner: ", Cricket_World_Cup[i]["Winner"])