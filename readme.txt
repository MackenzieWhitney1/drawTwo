Problem

Suppose you are given a shuffled deck of playing cards and you flipped cards two at a time,
taking the difference of the first and second card (in that exact order) where J=11, Q=12, K=13,
and adding that difference to a running total per flip.
ex. You flip K, 4. The net difference is 13-4 = 9. Running total = 9
You next flip 6,Q. The net difference is 6-12 = -6. Running total = 3
and so on.

What would be a good strategy, if any, to maximize this running total for any shuffled deck?

Related questions to investigate could be:
* If this was adapted for gambling, where a positive running total was paid out, is there/what would be a reasonable
"entry fee", given that such a fee would cover for ending a game with any negative running total?
(ie. the player doesn't have to pay anything after paying the fee for any one game)
* How does the game change if made a competition with the same shuffled deck(s) to get a higher numeric total than any
other to win a prize pool? (would require total state based strategies based on other player positions)

Types of Strategies

Exhaustive Strategy - Go through the whole deck as each flip result is independent anyway.

Target Strategy - waits for a target, and it's surpassed, exits.
16 (a naive average) as a target seems to do poorly.
0 as a target is rational if the game doesn't have an entry fee
Possible add: include a negative threshold

Coin Flip Strategy - Think of draws as coin flips.
ie. For standard deck, move the expectation that you will win 13/26 draws (positive including adding 0)

Probability - The choice to continue is based on chance.
Consideration: A strategy that always continues when "in the red", and only relies on chance to continue while
"in the green"
