# Newsparser - API

Uses [news-please](https://github.com/fhamborg/news-please) to generate formatted JSON outputs for news articles

## Installation
```
pip install -r requirements.txt
```

## Usage
```
python app.py
```

## Example

```
curl "http://localhost:5000/?url=https://techcrunch.com/2018/06/14/atoms-shoes/"
```

```json
{
  "authors": [
    "Josh Constine"
  ],
  "date_download": "2018-06-15 00:37:40",
  "date_modify": null,
  "date_publish": "2018-06-14 16:12:13",
  "description": null,
  "filename": "https%3A%2F%2Ftechcrunch.com%2F2018%2F06%2F14%2Fatoms-shoes%2F.json",
  "image_url": "https://techcrunch.com/wp-content/uploads/2018/06/Atoms-Shoes1.jpg?w=753",
  "language": "en",
  "localpath": null,
  "source_domain": "techcrunch.com",
  "text": "Step aside, Allbirds. Atoms come in quarter-sizes you can mix-and-match. Emerging from stealth today in a TechCrunch exclusive, this shoe startup’s obsession with satisfaction allowed it to replace my Nikes. I’ve spent the last two months wearing Atoms every day. They’re the first sneaker classy-looking enough for semi-formal occasions, butthat I can comfortably walk or even hike in for hours.\nHere’s how Atoms is modernizing the footwear experience:\nPick your quarter-size, say 10.25, and Atoms sends you 10s, 10.25s, and 10.5s, plus socks\nTry them on and pick any two, even different sizes for different feet, and send the rest back free\nNo logos. Atoms come in jet black, pure white orblack top/white bottom, but don’t stick an ad on your feet\nCopper threads inside eat bacteria, preventing funky smells\nElastic laces with subtle oval eyelets let Atoms slip on but stay tight so you rarely have to tie them\nGet a discount on your next pair if you send in your old Atoms for analysis and donation\nAt $179, Atoms are pricier than $100 lifestyle Nikes or $79 Allbirds. But the basketball shoe giant just sells in half sizes, while Allbirds offers only whole sizes that fit few perfectly. The right quarter-size Atoms for each foot makes them feel molded to your body.\n“To make shoes better, you need to know why people wear shoes,” Atoms co-founder Waqas Ali tells me. People buy fancy dress shoes they never wear, yet feel embarrassed by the childish designs and branding on most sneakers. “We perfected Atoms for your everyday routine — walking, standing and commuting,” he explains. “You are a person not a billboard, so there’s no logo.”\nThat hasn’t stopped the shoes from going viral during their beta-testing phase. Everyone who tries them on seems to rave about them. That’s driven 4,000 people to sign up on the Atoms waitlist, which you can join to be first in line. Atoms launch this summer in the U.S., with the first wave of customers getting their shoes in late June/early July.\nThe big bang\nHusband and wife duo Waqas and Sidra Ali started their first shoe company Markhor in Okara, Pakistan back in 2012. They attacked the market with one of the best qualities you can find in an entrepreneur: curiosity. Instead of coming in with preconceived notions, theytraveled the world to research how people actually wear shoes. “You might assume that ‘Oh in Italy, everyone wears leather shoes,’ but the young people there were all wearing sneakers,” Waqas recalls.\nAfter launching a Kickstarter, the Alis came to Silicon Valley to go through the prestigious Y Combinator startup accelerator in Summer 2015. There, they drilled into more customer research and product design.\nComfort and style were the big deciding factors in most sneaker purchases, so that’s where the couple wanted to differentiate. They discovered that more than 70 percent of people have at least a quarter-size difference in their two feet, and more than 7 percent have a half-size discrepancy. Sowhy don’t other shoe companies offer quarter-sizes? “They make tons of different shoes,” Waqas says.\nSuddenly, the two guiding principles of Atoms aligned. By designing just asingle unisex model in a limited set of colors, it could make quarter-sizing scalable while stripping away all the goofy extra fabrics and patterns. Indeed, 35 percent of customers already take two different sizes. That breakthrough attracted $560,000 in seed funding from LinkedIn’s ex-head of growth Aatif Awan and Shrug Capital.\nBut Atoms is determined to avoid being labeled a Silicon Valley shoe. Rather than coders, the company wants creative types like painters and graphic designers to be its early adopters. The vision is to create a sneaker a head chef could wear all night in the kitchen without hurting, but that look elegant enough that they could stride into the chic dining room with confidence.\nThe future of footwear\n“Most shoes in the market that claim they’re comfortable are only comfortable when you try them on,” Waqas laments. Take that other shoe startup Allbirds. They’re super-soft and made of wool, and the first steps feel like you’re wearing cloud slippers. But walk 10 blocks and you’ll find the bendy bottoms don’t protect you much.\nThat’s why Atoms hired 18-year-veteran of the shoe business Sangmin Lee, who’s worked with Adidas and Puma out of Portland and South Korea. He prototyped tons of different versions for Atoms. The result is a strong but light outsole on the bottom with indents cut out for anti-slip traction and to reduce weight. Meanwhile, the upper’s tough mesh material breathes but holds its shape, and refuses stains.\n“Shoe companies say they use sustainable materials but you go to the factories and everything is falling apart,” Sidra tells me. Organic materials sound nice but can break down too quickly. “The way we make our shoes environmentally friendly is that they last long,” Waqas says with a laugh.\nTwo months of tough wear later, my Atoms are holding up great. The foamy mid-sole has frayed a tiny bit in the front like many shoes. And the knit materials ingrained some dust when I went camping in them that needed some brushing to get out. But they’ve succeeded in becoming my go-to shoe I can chill, work and play in.\nNow Atoms is trying to build more commerce innovation to turn buyers into lifetime wearers. It’s working on a special pattern for the insole that will rub off based on where you put your weight. The idea is that when people send their old pairs in for a discount on the next, it can analyze that insole pattern to improve the shape of future models.\nOne day, Atoms hopes to create a completely personalized shoe shopping experience. It hopes to actually give you slightly different insoles with more or less arch support depending on how you wore the last ones. And it’s planning early access to new color combinations and laces for repeat buyers.\nAtoms will need loyalty in case the shoe giants come out with their own minimalist, quarter-sized sneakers. Such a limited set of colors and single style mean plenty of people will simply find them ugly or outside their taste. And no, they’re not a great fit for the gym or with a suit. But if you want understated, durable shoes you don’t have to think about, Atoms excel.\nThe startup must rely on its nimbleness and a flawless customer experience if it’s going to gain a foothold in a business dominated by brands with huge ad campaigns and brick-and-mortar distribution. One thing it’s thankful to its shoe startup competitor for is that “Allbirds has shown the world is not just ruled by Nike and Adidas.”\nLuckily Atoms has strong differentiation in a world of interchangeable sneakers. “I thought quarter-sizing was a joke or gimmick until I tried the 10.25s,” one customer said. “How will I go back to a 10.5 when 10.25 fits so well?” Personally, there hasn’t been another tech or startup product in the past 10 years beyond Apple’s AirPods that has cemented itself so deeply into my daily life.\n“There’s no way to hack shoes” Waqas concludes.“You just have to make a good shoes.”",
  "title": "Meet Atoms, the minimalist startup shoes you’ll actually wear",
  "title_page": null,
  "title_rss": null,
  "url": "https://techcrunch.com/2018/06/14/atoms-shoes/"
}
```
