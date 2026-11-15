# Scorecard, exit math and verdict

Read this when you reach Steps 10 and 12.

## Contents

1. Exit math, with a worked example
2. Scoring the criteria
3. Founder-side block
4. From scorecard to verdict
5. Kill criteria
6. Cheapest next test

## 1. Exit math

The question: what would this company have to look like to be worth $1 billion, and has anyone in this market ever looked like that?

Four numbers, each a labelled estimate with its arithmetic:

1. **Revenue needed** = target value ÷ sector multiple. Use the comps from Step 6. Give a range when the comps give one, and say how many data points stand behind it.
2. **Customers needed** = revenue needed ÷ price per customer per year, for each price point the idea could charge. Put the largest existing player of the same model next to it.
3. **Share needed** = revenue needed ÷ the market's revenue pool. Say which rank among incumbents that would be.
4. **Time** = how long the comps took to reach that revenue.

Then the buyers: who has acquired companies of this kind, at what prices, and what they bought (customers, a license, technology, assets).

### Worked example

From the public example in this repository (AI-native wealth advice, US, as of November 2026):

- The one comp with disclosed revenue and valuation is Wealthfront: about $2.05B at the top of its IPO range on $339M of revenue, so about 6x revenue. One data point is thin evidence, and the report says so.
- Revenue needed for $1B at 6x: about $165M.
- Customers needed at observed price points:

| Price per year | Seen at | Customers for $165M |
|---|---|---|
| $99 | AI planner subscription | about 1.67 million |
| $399 | AI-only advice, lower tier | about 414,000 |
| $999 | AI-only advice, upper tier | about 165,000 |
| $3,950 | Flat-fee planning with a human team, entry tier | about 42,000 |

- The largest flat-fee provider reports about 24,000 members after roughly nine years. A well-funded newer one reports about 3,100 households after five.
- Share needed: $165M against a fee-based advisory revenue pool of about $260B is 0.06%. The pool is not the constraint. Winning that many paying customers at that price is.

The useful sentence at the end of exit math is of this kind: "A $1B outcome needs about 42,000 households paying $3,950 a year, more than thirteen times what a well-funded entrant has reached in five years."

## 2. Scoring the criteria

Score what the evidence shows, not what the idea promises. Each score gets one line of reasoning with evidence ids.

**Problem**
- Green: customers demonstrably pay to solve it today, or lose measurable money for lack of a solution.
- Yellow: the need is stated in surveys or interviews, but there is no behaviour behind it.
- Red: evidence that customers do not care or will not pay, such as withdrawn products or failed tests.

**Urgency**
- Green: a forced or dated trigger. A legal requirement, a deadline, a renewal, a penalty for waiting.
- Yellow: the need arises at life or business events but can wait.
- Red: it can be put off indefinitely without cost.

**Market**
- Green: the share needed in the exit math is one that entrants in this sector have reached.
- Yellow: the outcome needs a top-three position among incumbents.
- Red: the revenue pool is too small even for the leader.

**Why now**
- Green: a dated, durable change that was not true three years ago: a technology, a rule, a price, a behaviour.
- Yellow: the change is real but helps every competitor equally, or it is a window that will close (a rate cycle, a subsidy).
- Red: nothing has changed.

**Competition and edge**
- Green: after the gap check, no funded player holds the position and the neighbours are not moving toward it.
- Yellow: small or unproven players hold it, or incumbents are building toward it.
- Red: funded winners are present and the idea states no edge over them.

**Distribution**
- Green: there is a channel the market's winners grew through, and a newcomer can enter it.
- Yellow: a plausible channel without evidence.
- Red: the channels belong to others, or direct acquisition has been shown to fail at this price.

**Economics**
- Green: comps show margins and payback that work at scale.
- Yellow: unknown or mixed.
- Red: comps show structural losses, falling prices, or cost that grows with every customer.

Two yellows with a known test are better than one green that rests on a company's own claim. Say which scores rest on weak evidence.

## 3. Founder-side block

Only when the user has told you about themselves. Keep it apart from the market scorecard and say that it does not change the market verdict.

- **Founder fit:** what the founder brings that this business needs (domain, license, network, distribution), and what is missing.
- **Commitment:** what the idea demands in years, capital and licenses, and whether the founder has said they will give it.

Do not use what you know about the founder to soften or harden the market scores.

## 4. From scorecard to verdict

- **Go:** no red, and the greens include Problem and at least one of Distribution or Competition and edge.
- **Go with conditions:** no red on Problem, Market or Economics, and every yellow that matters has a test that could turn it green or red within weeks. Name the tests.
- **No-go:** a red on Problem, Market or Economics, or two or more reds anywhere. Name the reasons, and say whether a different variant of the idea (another customer, channel or position in the money flow) scored better.

These are defaults. If you depart from them, say why. The reader should be able to reconstruct the verdict from the table.

## 5. Kill criteria

Two to four facts that would end the idea if they turned out true, each one checkable. For example:

- "The incumbent's instant-approval programme already covers the size band the idea targets."
- "The neighbour with the customers and the license ships this within twelve months."
- "A paid test at the target price converts below one percent."

## 6. Cheapest next test

One test, sized to the biggest open question, that fits in a week or two and little money. Pick by the weakest score:

| Weakest score | Test |
|---|---|
| Problem or Urgency | Ten conversations with the buyer about the last time the problem occurred and what they paid to fix it |
| Demand at a price | A landing page with the price on it and paid traffic to it; count pre-orders or deposits, not sign-ups |
| Distribution | Ask five holders of the channel (agents, partners, platforms) for a pilot, and count who says yes in writing |
| Economics | Deliver the service by hand to three customers and measure the hours |
| Competition | Ask the nearest competitor's customers why they chose it and what they still lack |

Say what result would count as a pass and what would count as a fail before the test is run.
