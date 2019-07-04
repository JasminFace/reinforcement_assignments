ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]

points = {
  'Bella': 0,
  'Boots': 0,
  'Felix': 0,
  'Lucky': 0,
  'Simba': 0,
  'Smudge': 0,
  'Tigger': 0,
}

for ballot in ballots:
  for tier, candidate in ballot.items():
    if tier == 'gold':
      points[candidate] += 3
    elif tier == 'silver':
      points[candidate] += 2
    elif tier == 'bronze':
      points[candidate] += 1

winner = max(points, key=points.get)
print(f'The winner is.... {winner.upper()}!')