def total_points(results):
    points = 0

    for result in results:
        scores = result.split(":")
        team_score = int(scores[0])
        opponent_score = int(scores[1])

        if team_score > opponent_score:
            points += 3
        elif team_score == opponent_score:
            points += 1

    return points


print(total_points(["1:0", "1:1", "0:1"]))