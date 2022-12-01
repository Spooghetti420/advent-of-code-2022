def part_i():
    highest = 0
    highest_line = -1
    running_total = 0
    with open("input.txt", mode="r", encoding="utf-8") as data:
        for i, line in enumerate(data):
            line = line.strip()
            if line:
                num_calories = int(line.strip())
                running_total += num_calories
            else:
                if running_total > highest:
                    highest = running_total # Update current calorie highscore
                    highest_line = i

                running_total = 0

    print("Highscore is", highest, "on line", highest_line)

def part_ii(max_scores: int = 3):
    highscores = [0 for _ in range(max_scores)]
    def update_scoreboard(new_score: int) -> None:
        for i, score in enumerate(highscores):
            if new_score > score:
                highscores.insert(i, new_score)
                highscores.pop() # Remove the new lowest tracked score
                return
    
    running_total = 0
    with open("input.txt", mode="r", encoding="utf-8") as data:
        for line in data:
            line = line.strip()
            if line:
                num_calories = int(line.strip())
                running_total += num_calories
            else:
                update_scoreboard(running_total)
                running_total = 0
    print(highscores, "whose sum is", sum(highscores))


if __name__ == "__main__":
    # part_i()
    part_ii(3)