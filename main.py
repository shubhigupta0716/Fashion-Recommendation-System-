def color_score(outfit, makeup, shoes):
    score = 50

    if "black" in outfit and "black" in shoes:
        score += 20
    if "red" in outfit and "red" in makeup:
        score += 15
    if "pastel" in outfit and "soft" in makeup:
        score += 15
    if "brown" in shoes and "red" in outfit:
        score -= 15

    return score


def style_score(outfit, makeup, shoes, occasion):
    score = 50

    if occasion == "party":
        if "heels" in shoes:
            score += 20
        if "bold" in makeup:
            score += 15

    if occasion == "casual":
        if "sneakers" in shoes:
            score += 20
        if "minimal" in makeup:
            score += 15

    if occasion == "formal":
        if "formal" in shoes:
            score += 20
        if "neutral" in makeup:
            score += 15

    return score


def suggest_makeup(outfit):
    if "black" in outfit:
        return "Nude base with bold red lipstick"
    elif "pastel" in outfit:
        return "Soft pink or peach tones"
    else:
        return "Neutral makeup"


def suggest_shoes(outfit):
    if "dress" in outfit:
        return "Heels"
    elif "jeans" in outfit:
        return "Sneakers"
    else:
        return "Flats"


def suggest_outfit(makeup, shoes):
    if "bold" in makeup and "heels" in shoes:
        return "Solid color party dress"
    elif "sneakers" in shoes:
        return "Casual jeans and t-shirt"
    else:
        return "Simple elegant outfit"


print("\n===== SMART FASHION AI ASSISTANT =====")
print("1. Enter Outfit only")
print("2. Enter Makeup only")
print("3. Enter Shoes only")
print("4. Enter Outfit + Makeup")
print("5. Enter Outfit + Shoes")
print("6. Enter Makeup + Shoes")
print("7. Enter Outfit + Makeup + Shoes (Check Compatibility)")

choice = int(input("Enter choice: "))

occasion = input("Enter occasion (casual / party / formal): ").lower()

outfit = ""
makeup = ""
shoes = ""

if choice == 1:
    outfit = input("Enter outfit: ").lower()
    print("Suggested Makeup:", suggest_makeup(outfit))
    print("Suggested Shoes:", suggest_shoes(outfit))

elif choice == 2:
    makeup = input("Enter makeup: ").lower()
    print("Suggested Outfit: Neutral outfit based on makeup")
    print("Suggested Shoes: Heels or flats depending on occasion")

elif choice == 3:
    shoes = input("Enter shoes: ").lower()
    print("Suggested Outfit: Outfit matching shoe style")
    print("Suggested Makeup: Minimal or bold based on shoes")

elif choice == 4:
    outfit = input("Enter outfit: ").lower()
    makeup = input("Enter makeup: ").lower()
    print("Suggested Shoes:", suggest_shoes(outfit))

elif choice == 5:
    outfit = input("Enter outfit: ").lower()
    shoes = input("Enter shoes: ").lower()
    print("Suggested Makeup:", suggest_makeup(outfit))

elif choice == 6:
    makeup = input("Enter makeup: ").lower()
    shoes = input("Enter shoes: ").lower()
    print("Suggested Outfit:", suggest_outfit(makeup, shoes))

elif choice == 7:
    outfit = input("Enter outfit: ").lower()
    makeup = input("Enter makeup: ").lower()
    shoes = input("Enter shoes: ").lower()

    c_score = color_score(outfit, makeup, shoes)
    s_score = style_score(outfit, makeup, shoes, occasion)
    final_score = int((c_score * 0.5) + (s_score * 0.5))

    print("\nCompatibility Score:", final_score, "%")

    if final_score >= 80:
        print("Verdict: Perfect match")
    elif final_score >= 60:
        print("Verdict: Good, minor improvements possible")
    else:
        print("Verdict: Needs improvement")

else:
    print("Invalid choice")