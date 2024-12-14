import os
import random



def generate_n_lotto_tickets():
    n = int(input("Внесете број на корисници: "))
    if not os.path.exists("tickets"):
        os.makedirs("tickets")

    global user_tickets
    user_tickets = {}

    for _ in range(n):
        name = input("Внесете име и презиме: ").replace(" ", "_").lower()
        tickets = []
        for i in range(1, 11):
            ticket_numbers = sorted(random.sample(range(1, 38), 7))
            ticket_id = f"#{random.randint(100000, 999999)}"
            tickets.append((ticket_id, ticket_numbers))

        user_tickets[name] = tickets


        with open(f"tickets/{name}.txt", "w") as f:
            f.write(f"{name.upper()}\n===\n")
            for i, (ticket_id, numbers) in enumerate(tickets, start=1):
                f.write(f"#{i} {ticket_id}:\n")
                f.write(" ".join(map(str, numbers)) + "\n===\n")


# Функција за влечење на добитни броеви
def lotto_draw():
    global winning_combination
    winning_combination = sorted(random.sample(range(1, 38), 7))
    with open("tickets/winning_combination.txt", "w") as f:
        f.write(" ".join(map(str, winning_combination)))



def check_winning_combinations():
    prize_map = {7: 15000000, 6: 250000, 5: 78000, 4: 9000}

    for user, tickets in user_tickets.items():
        total_winnings = 0
        with open(f"tickets/{user}_amount.txt", "w") as f:
            f.write(f"{user.upper()}\n===\n")
            for i, (ticket_id, numbers) in enumerate(tickets, start=1):
                matched = len(set(numbers) & set(winning_combination))
                amount = prize_map.get(matched, 0)
                total_winnings += amount
                f.write(f"#{i} {ticket_id}:\n")
                f.write("Matched: {matched}\n")
                f.write(f"Amount: {amount}\n===\n")
            f.write(f"Total amount: {total_winnings}\n")



def generate_report():
    prize_map = {7: 15000000, 6: 250000, 5: 78000, 4: 9000}
    category_wins = {7: 0, 6: 0, 5: 0, 4: 0}
    category_amounts = {7: 0, 6: 0, 5: 0, 4: 0}

    for user, tickets in user_tickets.items():
        for _, numbers in tickets:
            matched = len(set(numbers) & set(winning_combination))
            if matched in category_wins:
                category_wins[matched] += 1
                category_amounts[matched] += prize_map[matched]

    with open("tickets/lotto_report.txt", "w") as f:
        for category in sorted(category_wins.keys(), reverse=True):
            f.write(f"{category} matches\n")
            f.write(f"Number of wins: {category_wins[category]}\n")
            f.write(f"Amount: {category_amounts[category]}\n-----\n")
        f.write(f"Total amount: {sum(category_amounts.values())}\n")



if __name__ == "__main__":
    generate_n_lotto_tickets()
    lotto_draw()
    check_winning_combinations()
    generate_report()

    # fajlovite vi sluzhat za da dobiete pojasna slika koj fajl kako treba da izgleda, potrebno e da se zadrzhi istiot
    # format pri nivno kreiranje, vnimavajte na zapishuvanje na podatocite, specijalni znaci, itn.

    # marija_atanasova.txt e primer za kako treba da izgleda kreiran fajl za sekoj uchesnik vo loto igrata.
    # imenuvanjeto na fajlovite potrebno e da bide ime_prezime.txt

    # winning_combination.txt e kako treba da izgleda fajl za dobitnite broevi

    # marija_atanasova_amount.txt e primer za kako treba da izgleda fajl otkako kje bidat izvlecheni dobitnite broevi
    # vo ovoj fajl se chuva iznosot na dobivkata na uchesnikot
    # za sekoj uchesnik treba da imame dva fajla - ime_prezime.txt i ime_prezime_amount.txt

    # lotto_report.txt e primer za kako treba da izgleda kreiraniot izveshtaj za loto koloto
