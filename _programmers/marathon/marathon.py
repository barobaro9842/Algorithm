participant = ["mislav", "stanko", "mislav", "ana"]	
completion = ["stanko", "ana", "mislav"]

participant.sort()
completion.sort()

for i in range(len(completion)) :
    if participant[i] != completion[i]:
        answer = participant[i]
        break
    answer = participant[-1]

print(answer)