# Evidence rules

How to source, date, qualify and log every fact in the report. Read this before the first search.

## Contents

1. Which source for which claim
2. Reading discipline
3. Dates, units and periods
4. Company claims and interested parties
5. When sources disagree
6. Estimates
7. Founder data
8. Corrections
9. The evidence log, with examples

## 1. Which source for which claim

Prefer the source closest to the fact. Go down the list only when the level above does not exist or cannot be opened.

| Claim | First choice | Then | Last resort |
|---|---|---|---|
| Market size, client counts | Regulator, statistical office, industry association report | Trade press quoting that report with figures | Consultancy or vendor estimates |
| Company revenue, profit, assets | Filings (IPO prospectus, annual report), company release | Trade press citing the company | Data aggregators' estimates, labelled as estimates |
| Funding round, valuation | Company or investor release | Trade press | Aggregators; note when a valuation is "reported" rather than announced |
| What a product does and costs | The company's own product and pricing pages | Trade press | Review sites |
| Why something failed | Statements by the company or its people, filings | Trade press with named sources | Commentary |
| Customer attitudes | The survey's own report or its publisher | Trade press quoting sample and wording | Summaries without sample size |
| Rules and licenses | The regulator's text | Law-firm or compliance-firm notes | Trade press |

Encyclopedias and aggregator profiles are useful for founding years and round histories. Mark them as tertiary in the note column and do not rest a verdict on them.

## 2. Reading discipline

- **Open the page behind every fact that carries weight.** A search-result title is a lead, not a fact. Titles get numbers wrong, drop qualifiers and outlive corrections.
- **Record what you actually read.** `opened` means you read the relevant part. `partial` means the page was cut off or you read only a section; say how much. `snippet` means you never opened it.
- **Paywalls and failed fetches.** Try another outlet covering the same event. If none exists, keep the fact as `snippet`, say so in the report, and keep it off the verdict page.
- **Hedged wording is a warning.** "May", "typically", "reportedly", "according to people familiar" mean the writer did not know. Find the primary page or carry the hedge into your own sentence.
- **Nothing from memory.** If you believe you know a figure, treat that as a reason to search for it, not as a source.

## 3. Dates, units and periods

- Give every figure an `as_of` date: the period it describes, not the day you read it.
- Give the publication date and the day you accessed the page.
- Keep the source's unit and period: fiscal year, last twelve months, annualised run rate, six months. Do not turn a run rate into "revenue".
- Keep the sector's own metric (assets under management, gross written premium, members) and say what it is. Do not convert between metrics unless you show the conversion as an estimate.
- Name the currency. Convert only for comparison, and say which rate and date you used.

## 4. Company claims and interested parties

- A company's statement about itself is a claim: "according to the company", "the company says".
- User counts, "leading", "first" and growth percentages without a base are marketing until a filing or a third party confirms them.
- Say when a source has a stake: a reviewer who is an investor or affiliate, a vendor sizing its own market, an investor describing its portfolio company.
- "Unicorn" without a figure is not a valuation. Log it as "valuation not disclosed; described as above $1B".

## 5. When sources disagree

Log both rows. In the report, give both figures, their dates and sources, and say which you use and why (usually the more recent primary source). If you cannot tell, give the range. Do not average.

## 6. Estimates

An estimate is any number you computed. Each one needs:

- the formula in the `note` column, with the ids of its inputs
- a label in the text ("own estimate")
- rounding that matches the weakest input; one company-claimed input does not justify three significant figures

Keep estimates for the places they are needed: bottom-up market checks, multiples, exit math. Do not estimate a company's undisclosed revenue and then compare others against it as if it were reported.

## 7. Founder data

Waitlist tests, ad tests, customer requests and sales conversations are evidence, often the best available. Log them with status `founder` and describe the method: sample size, period, channel, what counted as a signal.

Keep people out of it. Use counts and categories. Never copy names, contact details, account data or health and financial details of individual customers into the report or the log. If the founder's data concerns identifiable people, aggregate it and say that you did.

## 8. Corrections

When a later source overturns something you wrote earlier in the run, fix the text and add a line under "Corrections" in section 16: what was claimed, what is right, and which source settled it. If a correction removes a claimed gap, say so on the verdict page.

## 9. The evidence log

Columns: `id, claim, value, unit, as_of, source, url, published, accessed, status, note`

Give each source a number and each fact from it a letter: `E18a`, `E18b`. Estimates get `X01, X02, …`. One row per fact; split a sentence with three figures into three rows. The report cites the source number, `[E18]`, and section 17 lists the sources by that number.

Examples (from the public example in this repository):

```csv
id,claim,value,unit,as_of,source,url,published,accessed,status,note
E18a,Wealthfront revenue last twelve months,339,USD million,2025-07-31,InvestmentNews,https://www.investmentnews.com/equities/wealthfront-seeks-485m-in-ipo-as-robo-platforms-vie-for-younger-investors/263335,2025-12-02,2026-11-15,opened,From the IPO filing as reported; up 25%
E18c,Wealthfront valuation at top of IPO range,2.05,USD billion,2025-12-02,InvestmentNews,https://www.investmentnews.com/equities/wealthfront-seeks-485m-in-ipo-as-robo-platforms-vie-for-younger-investors/263335,2025-12-02,2026-11-15,opened,Implied by the top of the price range
X01,Wealthfront valuation to revenue multiple,6.0,x,2025-12-02,own calculation,,,2026-11-15,estimate,E18c / E18a = 2050 / 339
```
