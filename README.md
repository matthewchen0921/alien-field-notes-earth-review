# alien-field-notes-earth-review

[![make.fun · u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

An alien tourist's one-line review of planet Earth, for the make.fun
competition "Alien Field Notes: The Two Day Earth Review".

## The entry

> Lovely planet, but the locals built a window onto the whole universe and spend all day arguing with strangers through it. 3/5 — the sunsets are free, and nobody looks up.

170 characters: one joke, landed cleanly. The laugh comes from the alien's
angle — a species that built a window onto the whole universe and uses it
to argue with strangers while free sunsets go unwatched — and it closes
the way a real tourist review closes, with a verdict and a rating. It
steers clear of the first obvious thoughts (traffic, gravity, money,
weather) for a detail few other entrants would reach first.

## How it works

`main.py` writes the fixed review line to `/output/entry.txt`. Nothing is
read from the network, the environment, or anywhere outside this repo; the
line is invented text, not a real incident and not about any real person.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```
