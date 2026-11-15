---
name: commercial-due-diligence
description: "Commercial due diligence for a startup idea: sourced market size, players, comps, deals, exit math, gap check and a verdict. Use for any market research, competitor analysis or idea validation."
license: MIT
compatibility: Needs web search and page-fetch tools. PDF export uses the bundled script (Python 3 with the markdown package, plus Playwright/Chromium, wkhtmltopdf or pandoc). Without them the report is delivered as Markdown.
metadata:
  author: Caesar Schütz
  version: "1.0.0"
---

# Commercial due diligence for startup ideas

Turn a startup idea into the analysis an investor would commission before writing a check: how big the market is, who already serves it and how well, what comparable companies are worth, what the deals in the sector say, whether the claimed gap is real, and what would have to be true for the idea to become a billion-dollar company. The output is a sourced paper with the verdict on page one.

The job is to find out whether the idea holds. Look as hard for reasons it fails as for reasons it works. A report that only confirms the founder's hopes is worth nothing to them, and they can usually tell.

## What you deliver

A folder `cdd-<idea-slug>/` in the working directory:

- `report.md`: the paper, in the user's language, following "Report structure" below
- `evidence.csv`: one row per fact used, with source, date and read status
- `report.pdf`: exported from `report.md` when a converter is available

If you cannot write files, deliver the report in the conversation in the same structure, with the numbered source list at the end.

## Before you start

1. **Check your tools.** You need live web search and the ability to open pages. If you have neither, say so and offer a research plan instead. Numbers recalled from memory are stale and nobody can check them, which defeats the purpose of a due diligence.
2. **Note today's date.** Every figure is "as of" a date. Funding rounds, prices and headcounts change within months.
3. **Load the references if they exist.** If this skill came with a `references/` folder, read `references/evidence-rules.md` now, and `references/search-playbook.md` and `references/scorecard.md` when you reach the steps that mention them. If you only have this file, it contains everything you need.
4. **Frame the idea** (Step 1). Ask the user at most three questions, and only about things you cannot sensibly assume: target country, target customer, how the company earns money. If nobody is there to answer, write your assumptions at the top of the report and continue.

Depth: the default is the full analysis. If the user asks for a quick scan, keep every step, halve the floors under "Minimum bar", and say on page one that it is a quick scan.

## Four rules that keep the analysis from being shallow

1. **Every number carries a source, a date and a read status.** Mark whether you opened the page, read part of it, saw only a search snippet, calculated the figure yourself, or got it from the founder. A reader must be able to tell a checked fact from a headline.
2. **A gap is a claim to disprove.** "Nobody does this" is the most common error in market research, and it usually comes from not searching hard enough. A gap counts only after searches designed to find an occupant have failed, and after you have checked the neighbours, the incumbents and the graveyard.
3. **Conflicts and corrections stay visible.** When two sources disagree, show both. When you find that something you wrote earlier in the run was wrong, correct it and list it under "Corrections". Hiding a correction costs the reader's trust in every other number.
4. **Answer the question that was asked.** Stay in the stated country and segment. Put the verdict first. Do not drift into neighbouring ideas or markets; list them in one line under "Not examined" if they matter.

## Workflow

Keep `evidence.csv` open from the first search and add a row whenever you learn a fact you might use. Write the report from the log, not from your memory of what you read.

Run searches in parallel where your tools allow it, and open the page behind any fact that will carry weight. `references/search-playbook.md` has query patterns for each step.

### Step 1: Frame the idea

Write one money sentence: *who pays whom, how much, for what, how often, through which channel.* If you cannot write it, that is the first finding.

Fix the scope: country, customer segment, business model. In a regulated market, add the license position: who in the chain is allowed to perform the regulated act, and who earns on it.

If the idea has variants that change who does the work or who pays (software only versus human-led with software, direct versus through partners), analyse them side by side. They often get different verdicts.

### Step 2: Size and define the market

- Define the market by money flow, not by product category: the amount customers already pay each year for the job (fees, premiums, commissions, subscriptions).
- Size it top-down from primary sources (regulators, statistical offices, industry associations, company filings), then cross-check bottom-up (customers times price). Show both and explain any difference.
- Break the price into its parts where you can: cost of delivering the service, cost of distribution, margin. Software can change the most where most of the price is labour or distribution, and little where it is risk or cost of goods.
- State growth and what drives it, and whether the driver is structural or a cycle.

### Step 3: Map the business models

Segment the market by business model (who pays, pricing unit, role of people versus software, channel), not by feature list. Most markets have four to eight models. For each: price point, example companies, and status (growing, flat, shrinking, unproven). This map is the spine of the report. A two-axis chart is not enough to describe a market.

### Step 4: Profile the players

Profile 12 to 20 companies across the models, including the largest incumbent in each and the best-funded entrants. For each: founding year, model, target customer, price, role of people versus software, traction in the sector's native metric (customers, revenue, assets, premium), funding and valuation, growth, channel.

Use tables. Write "n/d" where a company has not disclosed a figure. A blank is information; an estimate dressed as a fact is not.

Read each company's own page for what it offers before repeating a third party's description. Review sites hedge ("may not include") and get details wrong.

### Step 5: Explain the winners

Say who is growing fastest and why. Compare traction over time, distribution channel, pricing moves (who raised prices, who cut them), and unit economics where disclosed. Look for what the winners share: how they reach customers, where they sit in the money flow, how long it took them. The patterns become theses in Step 11.

### Step 6: Comps and precedent transactions

- **Comps.** Five to ten comparable companies, public and private, with latest revenue (or the sector's native metric), growth, valuation and the resulting multiple. Say what each valuation is (market cap, last round, IPO range) and its date. Report the range and the median and how many data points they rest on. If only one or two companies disclose both revenue and valuation, say that the multiple is thin evidence.
- **Precedent transactions.** Funding rounds of the last 24 to 36 months and exits (acquisitions, IPOs, sales after a shutdown), with date, price, buyer and multiple where it can be computed. Include exits below the last private valuation, because they bound the downside.
- **Deal lists.** Find at least three independent lists of deals in the sector: investment-bank sector reports, funding trackers, accelerator directories. Step 9 needs them too.

### Step 7: Graveyard and absentees

- **Graveyard.** Who tried this, or something close, and stopped: shutdowns, fire-sale exits, pivots, layoffs, withdrawn products. For each: what they tried, when, and the stated or reported reason. A graveyard with a common cause of death is among the most useful things a founder can be shown.
- **Absentees.** Who could do this tomorrow and does not: incumbents with the customers, platforms with the distribution, large technology companies with the capability. For each: what they do instead and why they hold back (regulation, cannibalising their own margin, channel conflict, economics). If the reason is temporary, they are the future competitor.

### Step 8: Demand evidence

Rank the evidence by strength and say which level your case rests on:

1. **Behaviour.** People paying, switching or leaving; price increases that stick; products withdrawn for lack of uptake; usage figures.
2. **The founder's own data**, if they have any: waitlist or ad tests, customer requests, sales calls. Ask once. Report the sample size and how the test was run.
3. **Stated attitudes.** Surveys. Report who was asked, how many, when, and the wording where it matters. Interest in a survey is not demand.

### Step 9: Gap check

Treat every "nobody does this" as a hypothesis and try to break it.

- Build a grid: business models and segments down the side, funded players across. Fill it from the deal lists.
- For each empty cell that matters to the idea, run counter-searches designed to find an occupant: the product described in other words, the customer's own wording, "raises", "launches" or "acquires" plus the segment, recent accelerator batches, and the incumbents' own announcements. Log the queries you ran.
- Check the neighbours: companies one step away that already hold the customers or the license and have announced a move.
- Check incumbents' in-house efforts and the graveyard. An empty cell with three dead companies in it is not a gap.
- Classify each candidate as **occupied**, **occupied by small or unproven players**, **empty for a structural reason** (name it), or **open**. Only the last is a gap. Say what you could not check.

### Step 10: Exit math

Work backwards from a $1 billion outcome, or the outcome the user names:

- Revenue needed = target value ÷ sector multiple. Use the range from Step 6.
- Customers needed = revenue ÷ price per customer per year. Compare with the largest existing player of the same model.
- Share needed = revenue ÷ the market's revenue pool from Step 2, and the rank among incumbents that implies.
- Time: how long comparable companies took to reach that scale.
- Buyers: who has bought companies like this, and for how much.

Label every result as your own calculation and show the arithmetic. `references/scorecard.md` has a worked example.

### Step 11: Theses

Write three to five statements that explain how this market works (for example, "distribution beats product here"). Each takes at most two sentences and comes with the evidence for it and the strongest evidence against it. If you cannot name evidence against a thesis, you have not looked for it yet.

### Step 12: Scorecard and verdict

Score each criterion green, yellow or red, with a one-line reason that cites evidence.

| Criterion | Green | Yellow | Red |
|---|---|---|---|
| Problem | Customers demonstrably pay to solve it, or lose measurable money without a solution | Stated need, no behaviour yet | Evidence that customers do not care or will not pay |
| Urgency | A forced or dated trigger: legal requirement, deadline, renewal | Event-driven, no deadline | Can be put off indefinitely |
| Market | The share needed in Step 10 is one that entrants in this sector have reached | Needs a top-three position | Pool too small even for the leader |
| Why now | A dated, durable change that was not true three years ago | A change that helps everyone equally, or a window that closes | Nothing has changed |
| Competition and edge | No funded player in the position after Step 9, neighbours not moving | Small or unproven players, or incumbents moving in | Funded winners present and no stated edge |
| Distribution | A channel the winners used and a newcomer can enter | Plausible channel, unproven | Channels owned by others, or direct acquisition shown to fail |
| Economics | Comps show margins and payback that work | Unknown or mixed | Comps show structural losses or falling prices |

Founder-side criteria (fit, commitment, resources) are scored only if the user gives you the context. Show them in a separate block. They do not change the market verdict.

Then give the verdict: **Go**, **Go with conditions** (name the tests that must pass first) or **No-go** (name the reasons). The verdict has to follow from the scorecard. If it does not, one of the two is wrong.

Add the kill criteria (facts that would end the idea if they turned out true) and the cheapest next test (what to do this week, for little money, that would teach the most).

### Step 13: Write, audit, export

Write `report.md` from the evidence log, run the self-audit, export the PDF, and deliver the files with a three-sentence summary of the verdict.

## Minimum bar for the full analysis

- 40 or more sources opened and logged
- 12 or more players profiled
- 3 or more independent deal lists
- 5 or more comps, or a stated reason why fewer exist
- 3 or more graveyard or absentee cases
- Logged counter-searches for every candidate gap

These are floors for a typical market, not targets to pad. If the market is small enough that fewer exist, say so.

## Evidence log

`evidence.csv` has these columns:

`id, claim, value, unit, as_of, source, url, published, accessed, status, note`

Status is one of:

- `opened`: you read the page, or the relevant part of it, yourself
- `partial`: you read only part of a long page; say how much in `note`
- `snippet`: you saw only a search-result title or snippet
- `estimate`: your own calculation; put the formula and its inputs in `note`
- `founder`: data supplied by the user

How to use it:

- Anything on the verdict page must be `opened`, `estimate` (with its formula) or `founder`. If a fact matters and you only have a snippet, open the page or drop the fact.
- A company's statement about itself is a claim. Write "according to the company".
- When two sources disagree, log both rows and state the conflict in the report.
- Give each source a number and each fact from it a letter: `E12a`, `E12b`. Estimates get `X` ids. Cite in the report with the source number in square brackets, like `[E12]`, and estimates as `(X03)`.

## Report structure

Use these sections in this order. If `templates/report.md` is available, start from it.

```markdown
# <Idea in one line>: commercial due diligence
<Country and segment> · as of <date> · <full analysis | quick scan>

## 1. Verdict
Go, Go with conditions, or No-go, in one sentence. Then: the three to five facts
that decide it, the biggest risk, the kill criteria, the cheapest next test,
and the scorecard as a small table.

## 2. The idea and the scope
Money sentence, scope, variants analysed, assumptions made.

## 3. Market size and money flow
## 4. Business models
## 5. Players
## 6. What the winners do
## 7. Comps
## 8. Precedent transactions
## 9. Graveyard and absentees
## 10. Demand evidence
## 11. Gap check
## 12. Exit math
## 13. Theses
## 14. Scorecard
## 15. Risks, kill criteria and next test
## 16. Corrections, open questions and what was not examined
## 17. Sources
One line per source number: title, publisher, date, link, read status.
```

Writing rules:

- Open each section with its conclusion in one or two sentences, then the evidence.
- Use a table for anything with more than three comparable items.
- Use plain words and define each sector term once. Do not let adjectives do the work of numbers.
- Give amounts with currency and date.
- Keep section 1 to one page. A reader who stops there should still have the answer.

## Export to PDF

If `scripts/build_pdf.py` is available next to this file, run:

```bash
python <skill-folder>/scripts/build_pdf.py cdd-<idea-slug>/report.md
```

It writes `report.pdf` beside the Markdown file and tries Playwright with Chromium, a system Chrome or Chromium, wkhtmltopdf and pandoc in that order. Open the PDF or render a page to check that tables fit the page width before you deliver it.

If the script is not available, convert with whatever the environment offers: pandoc, a headless browser printing an HTML render of the Markdown, or a document tool. If nothing works, deliver the Markdown and say that the PDF could not be built.

## Self-audit before delivering

- Every number in the report has an id that exists in `evidence.csv`, or is marked as an estimate with its formula.
- Everything on the verdict page is `opened`, `estimate` or `founder`.
- Each candidate gap lists the counter-searches that were run and what they found.
- Conflicts between sources are stated. Corrections are listed.
- Every figure has a date.
- The verdict follows from the scorecard.
- No company is described from memory alone.
- The report says what was not checked.

## Failure modes seen in real runs

- **A gap built on a hedged sentence.** A review said a provider "may not" offer a dedicated advisor; the provider's own page said it does. Read the primary page before calling something a gap.
- **Two dimensions.** Reducing a market to a two-by-two chart hides the differences that matter: who pays, at what price, through which channel.
- **"No results" read as "no competitors".** Search engines miss small funded companies. Deal lists and accelerator directories catch them.
- **A gap that was being closed while the report was written.** An "empty" processing layer turned out to be handled by an incumbent platform with more than half the market's volume and an industry standards project. Check the infrastructure players, not only the startups.
- **Survey interest read as demand.** People say they want many things they never pay for.
- **Drift.** Answering with a neighbouring country or a different idea when the question was about this one.
- **Founder fit deciding the market verdict.** Whether this founder is the right one is a separate question from whether the market holds.
- **Sell-side tone.** Bankers write to sell a deal. This report is written for the person who would lose the money.
